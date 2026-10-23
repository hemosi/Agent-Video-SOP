# CLAUDE.md — Agent 具象电影画面渲染（Cinematic Scene Rendering）全局规范

本目录（`E:\AI自媒体\Agent知识类视频SOP`）的核心目标是：**渲染具象、有光影、有生命力的电影级【画面（Scene）】，彻底禁止画抽象的【框、点、线、面】！**

---

## 1. 最高铁律：画「具象画面」，严禁画「框、点、线、面」！

- **绝对禁止（见一个毙一个）**：
  - 严禁画任何矩形方框、卡片框、胶囊框、表格框！
  - 严禁拿“写着字的方框”代表某个器官、概念或阶段！
  - 严禁拿“两个圆圈连一根虚线”代表运动或关系！
  - 严禁拿“几个椭圆线框和散点”代表世界或城市！
- **必须做到（对标 [`参考视频/extracted_frames/contact_sheet_part1.jpg`](./参考视频/extracted_frames/contact_sheet_part1.jpg)）**：
  - 台词讲什么事物，画面就必须渲染出那个事物的**真实具象场景与光影**：
    - 讲房间 ➔ 画透视墙角、发光四格窗、斜射地板的体积光柱、飘落的灰尘与桌上的花；
    - 讲城市 ➔ 画夜色下的摩天大楼剪影、成百上千扇亮着暖光的窗户、向上蔓延的绿色藤蔓；
    - 讲眼睛/身体 ➔ 画微距虹膜瞳孔、射入眼底的光束、或 4000 颗发光微粒构成的精细人体半身像；
    - 讲文字/数字 ➔ 无任何外框，直接以发光宋体与超大数字悬浮融入画面光影中。

---

## 2. 核心入口与强制执行的脚本

1. **唯一总控 Skill**：[`.claude/skills/xiaolin-director/SKILL.md`](./.claude/skills/xiaolin-director/SKILL.md)
2. **主流程 SOP**：[`SOP.md`](./SOP.md)
3. **本机 Auk-TTS 自动检测与启动**：
   ```bash
   curl -s http://127.0.0.1:7863/api/health
   # 若未启动，用 run_in_background: true 执行：
   cd "F:/Aku-tts/Auk-TTS/Auk-TTS" && "F:/Aku-tts/Auk-TTS/Auk-TTS/py312/python.exe" "F:/Aku-tts/Auk-TTS/Auk-TTS/app.py"
   ```
4. **强制双静帧表与质检脚本**：
   ```bash
   python "E:/AI自媒体/Agent知识类视频SOP/scripts/master_qa.py" --project "<项目目录>"
   ```
   - 必须生成 `qa_contact_sheet.jpg` 与 `qa_motion_sheet.jpg` 并用 `Read` 检查：**凡出现方框、圆圈虚线等几何简笔画，一律判废重画为具象场景！**
