import argparse
import asyncio
import base64
import json
import os
import sys
from PIL import Image, ImageDraw
import numpy as np
from playwright.async_api import async_playwright

CHROMIUM_ARGS = [
    "--allow-file-access-from-files",
    "--disable-web-security",
    "--disable-gpu",
    "--disable-accelerated-2d-canvas",
    "--disable-gpu-compositing",
    "--disable-renderer-backgrounding",
    "--disable-background-timer-throttling",
    "--disable-backgrounding-occluded-windows",
]

SAMPLE_RATIOS = [0.15, 0.32, 0.50, 0.68, 0.82, 0.95]


async def run_qa(project_dir: str, strict: bool = True):
    project_dir = os.path.abspath(project_dir)
    timing_path = os.path.join(project_dir, "timing.json")
    engine_path = os.path.join(project_dir, "engine.html")
    if not os.path.exists(timing_path) or not os.path.exists(engine_path):
        print(f"[ERROR] Missing timing.json or engine.html in {project_dir}")
        sys.exit(2)

    with open(timing_path, "r", encoding="utf-8") as fp:
        timing_data = json.load(fp)

    shots = timing_data.get("shots", [])
    if not shots:
        print("[ERROR] timing.json contains 0 shots")
        sys.exit(2)

    build_dir = os.path.join(project_dir, "build", "qa_frames")
    os.makedirs(build_dir, exist_ok=True)
    engine_url = "file:///" + engine_path.replace("\\", "/")

    tw, th = 480, 270
    motion_cols = len(SAMPLE_RATIOS)
    motion_sheet = Image.new("RGB", (tw * motion_cols, th * len(shots)), (8, 10, 14))
    motion_draw = ImageDraw.Draw(motion_sheet)

    contact_cols = 4
    contact_rows = (len(shots) + contact_cols - 1) // contact_cols
    contact_w, contact_h = 640, 360
    contact_sheet = Image.new("RGB", (contact_w * contact_cols, contact_h * contact_rows), (8, 10, 14))
    contact_draw = ImageDraw.Draw(contact_sheet)

    stasis_failures = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="msedge", args=CHROMIUM_ARGS)
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto(engine_url)
        await page.evaluate(
            """async (td) => {
                if (window.initTimeline) await window.initTimeline(td);
                else window.TIMING = td;
            }""",
            timing_data,
        )

        for s_idx, sh in enumerate(shots):
            sid = sh["id"]
            f0 = sh["start_frame"]
            total_f = max(1, sh["total_frames"])
            shot_arrays = []

            for r_idx, ratio in enumerate(SAMPLE_RATIOS):
                target_f = min(sh["end_frame"] - 1, f0 + int(total_f * ratio))
                b64 = await page.evaluate(
                    f"""(() => {{
                        if (window.renderFrame) window.renderFrame({target_f});
                        else if (window.draw) window.draw({target_f} / 30.0);
                        const c = document.getElementById('stage') || document.querySelector('canvas');
                        return c.toDataURL('image/jpeg', 0.92).split(',')[1];
                    }})()"""
                )
                raw_bytes = base64.b64decode(b64)
                frame_path = os.path.join(build_dir, f"{sid}_{r_idx}_{int(ratio*100):02d}.jpg")
                with open(frame_path, "wb") as out_f:
                    out_f.write(raw_bytes)

                im_full = Image.open(frame_path)
                arr_full = np.asarray(im_full, dtype=np.float32)
                # Crop main visual reasoning stage (y: 60..820, excluding bottom subtitle region!)
                shot_arrays.append(arr_full[60:820, :, :])

                # Paste into 6-column motion sheet
                im_thumb = im_full.resize((tw, th), Image.Resampling.LANCZOS)
                mx, my = r_idx * tw, s_idx * th
                motion_sheet.paste(im_thumb, (mx, my))
                motion_draw.rectangle([mx + 6, my + 6, mx + 165, my + 28], fill=(0, 0, 0))
                motion_draw.text((mx + 10, my + 9), f"{sid} p={ratio:.2f} (f={target_f})", fill=(255, 220, 130))

                # Use ratio=0.68 as representative peak frame for contact sheet
                if r_idx == 3:
                    im_contact = im_full.resize((contact_w, contact_h), Image.Resampling.LANCZOS)
                    cx, cy = (s_idx % contact_cols) * contact_w, (s_idx // contact_cols) * contact_h
                    contact_sheet.paste(im_contact, (cx, cy))
                    contact_draw.rectangle([cx + 8, cy + 8, cx + 220, cy + 34], fill=(0, 0, 0))
                    contact_draw.text((cx + 14, cy + 12), f"{sid} p=0.68 (f={target_f})", fill=(255, 220, 130))

            # Quantitative Motion Audit (Check pixel delta across the 5 intervals in main stage y:60..820)
            deltas = []
            for k in range(len(shot_arrays) - 1):
                diff = np.abs(shot_arrays[k + 1] - shot_arrays[k]).mean()
                deltas.append(round(float(diff), 2))

            # Check brightness/contrast & half-screen emptiness on peak frame (r_idx == 3, ratio=0.68)
            peak_stage = shot_arrays[3]
            luma = peak_stage.mean(axis=2)
            # Active visible pixels brighter than dark background (luma > 38)
            vis_mask = luma > 38.0
            vis_pct = float(vis_mask.mean() * 100.0)
            left_vis = float(vis_mask[:, :960].mean() * 100.0)
            right_vis = float(vis_mask[:, 960:].mean() * 100.0)

            late_motion = max(deltas[2:])
            active_intervals = sum(1 for d in deltas if d >= 0.90)
            print(
                f"[QA] {sid}: deltas={deltas} | late_max={late_motion:.2f} | "
                f"vis_area={vis_pct:.1f}% (L={left_vis:.1f}%, R={right_vis:.1f}%)"
            )

            reasons = []
            if active_intervals < 2 or late_motion < 0.60:
                reasons.append(f"frozen/static late frames (deltas={deltas})")
            if vis_pct < 3.5:
                reasons.append(f"too dark / low contrast (vis_area={vis_pct:.1f}% < 3.5%)")
            if left_vis < 0.8 or right_vis < 0.8:
                reasons.append(f"half-screen empty (L={left_vis:.1f}%, R={right_vis:.1f}%)")

            if reasons:
                stasis_failures.append((sid, "; ".join(reasons)))

        await browser.close()

    out_contact = os.path.join(project_dir, "qa_contact_sheet.jpg")
    out_motion = os.path.join(project_dir, "qa_motion_sheet.jpg")
    contact_sheet.save(out_contact, quality=94)
    motion_sheet.save(out_motion, quality=92)
    print(f"[+] Saved Contact Sheet: {out_contact}")
    print(f"[+] Saved 6-Column Motion Sheet: {out_motion}")

    if stasis_failures and strict:
        print("\n[FAIL] Quantitative Motion Gate Rejected the Following Shots (Frozen/Dead Screen):")
        for sid, d in stasis_failures:
            print(f"  - {sid}: pixel deltas across [0.15, 0.32, 0.50, 0.68, 0.82, 0.95] = {d}")
        sys.exit(1)

    print("[PASS] Quantitative Motion Gate Passed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True, help="Path to episode project folder")
    parser.add_argument("--no-strict", action="store_true")
    args = parser.parse_args()
    asyncio.run(run_qa(args.project, strict=not args.no_strict))
