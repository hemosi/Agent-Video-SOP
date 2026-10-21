# Auk-TTS API 接口与本机视频配音对接文档（Agent 自启动与实战版）

本文档定义位于 `F:\Aku-tts\Auk-TTS\Auk-TTS` 的 **Auk-TTS (AuK Flash)** 本机配音服务如何由 Agent 自动检测、后台无阻塞启动、查询音色并生成逐镜口播音频。

---

## 一、Agent 自动检测与后台启动流程（必读）

> **重要说明**：Agent 在新会话中切勿直接同步运行 `一键启动_自动接口服务.bat`（因为 `.bat` 末尾含 `pause` 及 `start` 浏览器弹窗，在命令行中会导致阻塞）。请严格按以下 **3 步标准流程** 检测与自启动：

### 第 1 步：健康检查（判断服务是否已在线）
在 Bash 中执行：
```bash
curl -s http://127.0.0.1:7863/api/health
```
- **已在线响应**：
  ```json
  {
    "gateway": "ok",
    "family": "auk",
    "audiocpp": { "status": "ok", "backend": "cuda", "models": 1 },
    "models": { "auk": "auk-flash", "auk-flash": "auk-flash" }
  }
  ```
- 若返回上述 JSON，说明 `7863`（FastAPI 网关）与 `8080`（`audiocpp_server.exe` CUDA 推理后端）均已就绪，直接跳至第二节调用配音。

### 第 2 步：若未启动，Agent 后台无阻塞自启动命令
若 `curl` 连接失败（`Connection refused`），使用 Bash 工具并设置 **`run_in_background: true`** 执行以下命令（`app.py` 会自动拉起 `cpp/audiocpp_server.exe` 监听 `8080` 端口并启动 `7863` API 网关）：
```bash
cd "F:/Aku-tts/Auk-TTS/Auk-TTS" && "F:/Aku-tts/Auk-TTS/Auk-TTS/py312/python.exe" "F:/Aku-tts/Auk-TTS/Auk-TTS/app.py"
```

### 第 3 步：等待 6~8 秒后再次验证就绪
```bash
sleep 7 && curl -s http://127.0.0.1:7863/api/health
```
确认返回 `"gateway": "ok"` 后即可开始批量合成配音。

---

## 二、本机音色库清单（含「小林」专属音色）

### 1. 查询当前可用音色列表
```bash
curl -s http://127.0.0.1:7863/api/voices
```

### 2. 已注册核心音色表（截至 2026-10-21）
| 音色名称 (`speaker`) | 音色 ID (`id`) | 角色定位与适用场景 | 优先级 |
| :--- | :--- | :--- | :---: |
| **`小林`** | **`52920896bd09`** | **小Lin说风格知识类视频首选主讲音色**（节奏干脆、亲和力强） | ★ **默认首选** |
| **`女主播`** | `08482905d56e` | 标准新闻解说、短视频口播女声 | 备选女声 |
| **`烛灵儿`** | `3528e1c71180` | 虚拟年轻女性角色（林佳佳年轻态）、二次元旁白 | 备选女声 |
| **`jok老师`** | `cd792a2ee73c` | 沉稳知识科普男声 | 备选男声 |
| **`叶奈法`** | `adc02dbb286d` | 成熟叙事女声、纪录片旁白 | 备选女声 |

### 3. 注册并保存新音色接口
如需上传新的 5~15 秒干声样本注册新音色：
- **请求方式**：`POST http://127.0.0.1:7863/api/voices` (`multipart/form-data`)
- **表单字段**：`name`（音色名）、`audio`（WAV/MP3 文件）

---

## 三、核心配音 API 调用规范与铁律

### 1. 配音铁律（严禁违背）
1. **原生语速铁律**：调用接口时必须保持 **`speed=1.0`** 原生自然语速！**严禁将 `speed` 调高至 1.15+，严禁在后期使用 `ffmpeg atempo` 二次加速**（会导致声音发紧、机械失真）。
2. **重音括号清洗铁律**：剧本 `script.md` 中用于标记字幕放大花字的 `【】` 符号，在发送给 TTS 前必须用正则剥离（`re.sub(r"[【】]", "", text)`），防止 TTS 在括号处产生怪异停顿；而原始带 `【】` 的文本保留在 `timing.json` 中供画面花字机高亮。
3. **分镜气口留白**：每段分镜配音生成后，在末尾预留 **`0.30s ~ 0.45s`** 的自然呼吸气口（设问句后留白 `0.45s`），由配音真实时长反向驱动分镜总帧数（`Audio-First`）。

### 2. 极简配音端点 `/api`（推荐自动化脚本直接调用）
- **URL**：`GET http://127.0.0.1:7863/api` 或 `POST http://127.0.0.1:7863/api`
- **请求参数**：
  | 参数名 | 类型 | 必填 | 推荐值 | 说明 |
  | :--- | :--- | :---: | :---: | :--- |
  | `text` | string | **是** | 清洗后的分镜台词 | 去除 `【】` 后的纯文本 |
  | `speaker` | string | **是** | `小林` 或 `52920896bd09` | 音色名称或音色 ID |
  | `speed` | float | 否 | **`1.0`** | 固定 `1.0` 自然语速 |
  | `seed` | int | 否 | `42` | 固定随机种子保证全片声线一致 |
- **响应**：直接返回 `audio/wav` 二进制音频流（服务端同时在 `F:\Aku-tts\Auk-TTS\Auk-TTS\生成结果\` 备份）。

---

## 四、Python 自动检测自启动 + 逐镜配音标准模板

在项目的 `build_audio.py` 中直接复用以下自包含函数（即使 TTS 未打开也能自动拉起）：

```python
import os
import re
import time
import subprocess
import urllib.request
import urllib.parse
import json

AUK_ROOT = r"F:\Aku-tts\Auk-TTS\Auk-TTS"
AUK_PYTHON = r"F:\Aku-tts\Auk-TTS\Auk-TTS\py312\python.exe"
AUK_APP = r"F:\Aku-tts\Auk-TTS\Auk-TTS\app.py"
FFMPEG_BIN = r"F:\Aku-tts\Auk-TTS\Auk-TTS\py312\ffmpeg\bin\ffmpeg.exe"
HEALTH_URL = "http://127.0.0.1:7863/api/health"
TTS_API_URL = "http://127.0.0.1:7863/api"
DEFAULT_SPEAKER = "小林"  # id: 52920896bd09


def ensure_auk_tts_running(timeout_sec: int = 25) -> bool:
    """检查 Auk-TTS 是否在线；若未在线则自动在后台拉起 app.py 并等待就绪"""
    def check_health():
        try:
            with urllib.request.urlopen(HEALTH_URL, timeout=2) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("gateway") == "ok"
        except Exception:
            return False

    if check_health():
        print("[+] Auk-TTS 服务已在线 (127.0.0.1:7863)")
        return True

    print("[*] Auk-TTS 未启动，正在后台自动拉起服务...")
    subprocess.Popen(
        [AUK_PYTHON, AUK_APP],
        cwd=AUK_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=subprocess.CREATE_NO_WINDOW if os.name == "nt" else 0,
    )

    t0 = time.time()
    while time.time() - t0 < timeout_sec:
        if check_health():
            print(f"[+] Auk-TTS 后台自启动成功 (耗时 {time.time() - t0:.1f}s)")
            return True
        time.sleep(1.0)

    raise RuntimeError("[-] Auk-TTS 启动超时，请检查 F:\\Aku-tts\\Auk-TTS\\Auk-TTS 目录与显存状态")


def synthesize_shot_voice(raw_text: str, out_wav: str, speaker: str = DEFAULT_SPEAKER, seed: int = 42):
    """剥离【】重音标记并调用本地 Auk-TTS 生成单镜自然语速 WAV"""
    ensure_auk_tts_running()
    clean_text = re.sub(r"[【】]", "", raw_text).strip()
    query = urllib.parse.urlencode({
        "text": clean_text,
        "speaker": speaker,
        "speed": "1.0",
        "seed": str(seed),
    })
    req = urllib.request.Request(f"{TTS_API_URL}?{query}", headers={"User-Agent": "XiaolinSOP/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        wav_bytes = resp.read()
    with open(out_wav, "wb") as fp:
        fp.write(wav_bytes)
    return out_wav
```
