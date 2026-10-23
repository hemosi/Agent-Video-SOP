# Agent 具象电影画面渲染（Cinematic Scene Rendering）全自动 SOP

> **工程主目录**：`E:\AI自媒体\Agent知识类视频SOP`
> **唯一总控 Skill**：[`.claude/skills/xiaolin-director/SKILL.md`](./.claude/skills/xiaolin-director/SKILL.md)
> **第一铁律**：**我们要渲染的是「具象的电影画面（Scene / Picture）」，绝对禁止画「框、点、线、面（方框、圆圈、虚线、箭头、几何面板）」！**

---

## 一、 最高禁令：彻底封杀「框、点、线、面」几何画图

无论什么题材，画面上**严禁出现以下抽象几何符号**：
1. **禁画方框/卡片/面板**：不准画矩形框、圆角框、胶囊框、表格框，不准拿一个写着字的方框代表某个事物！
2. **禁画空心圆圈 + 虚线 + 箭头**：不准拿两个圆圈连一条虚线代表两个事物之间的关系！
3. **禁画死板的坐标轴与线框圈**：
- **必须画什么？—— 画具象的【画面（Scene）】！**
  - 讲“房间与灰尘” ➔ 渲染真实的透视房间墙角、发光四格窗、斜射到地板上的暖黄丁达尔光柱、光柱中飘落的灰尘与桌上的花；
  - 讲“城市与灯火” ➔ 渲染夜幕下的高低楼群剪影、成百上千扇亮着暖光的窗户、地面车流光带或蔓延的植物藤蔓；
  - 讲“眼睛与大脑” ➔ 渲染微距的虹膜纹理、收缩的瞳孔、射入眼底的光束与精细的神经元森林；
  - 讲“人与关系” ➔ 渲染数千发光微粒构成的精细人体轮廓、真实的聊天字句失重飘散、或星空地平线下的人物场景。

---

## 二、 完整 5 步极速生产流程

### 步骤 1：编写「具象画境分镜表」（`script.md`）
- 每个镜头的画面描述必须是一幅**具体的场景画（有环境、有具体器物/建筑/自然主体、有主光源、有物理动态）**；
- 分镜描述中**严禁出现“方框、卡片、圆圈、虚线、箭头、面板”字样**！

### 步骤 2：本地 Auk-TTS 配音与声画时间轴（`build_audio.py`）
1. 检测 `curl -s http://127.0.0.1:7863/api/health`；未启动则后台运行：
   `cd "F:/Aku-tts/Auk-TTS/Auk-TTS" && "F:/Aku-tts/Auk-TTS/Auk-TTS/py312/python.exe" "F:/Aku-tts/Auk-TTS/Auk-TTS/app.py"`
2. 调用 `http://127.0.0.1:7863/api`（`speed=1.0` 原生语速，自动裁切尾部静音），混入 [`音效_精选/sfx_manifest.json`](./音效_精选/sfx_manifest.json) 输出 `-14 LUFS` 母带与 `timing.json`。

### 步骤 3：渲染具象场景画面（`engine.html`）
每个镜头必须完整渲染四层视觉：
1. **环境氛围层**：天空/室内/地平线/体积光锥，拒绝死黑底干画线；
2. **具象主体造型层**：精细的建筑、窗户、植物、虹膜、沙漏、人物点云雕塑或实拍影像视差合成；
3. **物理动态与光影层**：尘埃飘落、灯火点亮、冰晶生长、粒子聚散；
4. **无框融入式文字层**：文字与核心数字直接悬浮融入场景光影中，**零边框、零底条**。

### 步骤 4：运行 `scripts/master_qa.py` 双表门禁
```bash
python "E:/AI自媒体/Agent知识类视频SOP/scripts/master_qa.py" --project "<项目目录>"
```
用 `Read` 检查生成的 `qa_contact_sheet.jpg` 与 `qa_motion_sheet.jpg`：**只要任何一镜还在画“方框、圆圈、虚线”而不是具象画面，立即重做！**

### 步骤 5：无黑屏导出 MP4
- Playwright Chromium 携带 `--allow-file-access-from-files --disable-web-security --disable-gpu --disable-accelerated-2d-canvas --disable-gpu-compositing` 导出 `1080p.mp4`。
