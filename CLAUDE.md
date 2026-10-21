# CLAUDE.md — Agent 知识类视频 SOP 全局工作规范

本目录（`E:\AI自媒体\Agent知识类视频SOP`）是以「林佳佳」虚拟数字人为主讲的泛知识类视频（2~5 分钟，`1920×1080 @ 30fps`，涵盖 AI/代码科普、科技趋势、商业逻辑、社会观察、方法论拆解等）全自动生产工程目录。只读文档与拉片知识库位于 `E:\Obsidian_Note\知识库\04_领域\代码类视频`。

---

## 1. 核心架构：双核解耦（叙事节奏学小Lin × 视觉特效靠 23 个专业 Skill）

1. **【叙事与节奏核】`xiaolin-director`（低视觉权重：只管讲故事、降维与节奏，0% 限定具体特效！）**
   - 位置：[`.claude/skills/xiaolin-director/SKILL.md`](./.claude/skills/xiaolin-director/SKILL.md) 及 [`references/lapian-rules-compendium.md`](./.claude/skills/xiaolin-director/references/lapian-rules-compendium.md)。
   - 职责：**只吸收小Lin说的讲故事结构、6 大留存钩子心机、10 大把专业概念变人话的降维公式、5~7 秒一次推进的剪辑节奏、林佳佳数字人三级出镜配比、以及配音气口与音效卡点**。
   - **禁令**：**绝不规定、不限制任何具体的 UI 组件或固定特效模板**！严禁把财经图表、天平、圆球盖章等固定特效套用到所有视频里。
2. **【开放视觉与动效核】筛选出的 23 个专业视觉 Skills（100% 视觉主导权，按每期题材自由创造）**
   - 位置：[`.claude/skills/`](./.claude/skills/) 与 [`weilanx-claude-videos/styles/解说语法/`](./weilanx-claude-videos/styles/解说语法/)。
   - 职责：每期视频的**美学基调（`motion-art-direction`、`color-motion`、`shot-composition`）、数字人舞台与工作台交互（`weilanx-creator-desk-video` / `vox-video` / `blackgold-video`）、电影级镜头与变形特效（`cinetic`、`motion-effects`、`title-sequence-3d`、`milestone-reveal`）、非线性弹簧缓动与运镜（`klik-anim`、`klik-cam`、`animation-principles`、`gsap-timeline/plugins`）**，100% 根据当期题材从零自由组合与设计！
3. **主流程与声音资产入口**：
   - 全链路 SOP：[`SOP.md`](./SOP.md)
   - 本机配音自启动文档：[`Auk-TTS接口与视频配音使用文档.md`](./Auk-TTS接口与视频配音使用文档.md)
   - 37 款无损音效索引：[`音效_精选/音效索引.md`](./音效_精选/音效索引.md) 与 [`音效_精选/sfx_manifest.json`](./音效_精选/sfx_manifest.json)（配合 `sfx/synth.py` 动态合成兜底；**严禁遍历原始未整理的音效文件夹**）。

---

## 2. 本机 Auk-TTS 自动检测与后台无阻塞启动（Audio First）
1. **健康检查**：
   ```bash
   curl -s http://127.0.0.1:7863/api/health
   ```
2. **未启动时的后台无阻塞自启动命令**（切勿直接同步执行带 `pause` 的 `.bat`，在 Bash 工具中用 `run_in_background: true` 执行以下命令，会自动拉起 `8080` 端口 `audiocpp_server.exe` 与 `7863` 端口网关）：
   ```bash
   cd "F:/Aku-tts/Auk-TTS/Auk-TTS" && "F:/Aku-tts/Auk-TTS/Auk-TTS/py312/python.exe" "F:/Aku-tts/Auk-TTS/Auk-TTS/app.py"
   ```
3. **默认音色与铁律**：
   - 可选音色：`小林`（`52920896bd09`）、`女主播`（`08482905d56e`）、`烛灵儿`（`3528e1c71180`）、`jok老师`（`cd792a2ee73c`）。
   - **必须保持 `speed=1.0` 原生自然语速**，严禁调高 `speed` 或使用 `ffmpeg atempo` 二次加速；发送给 TTS 前必须用正则剥离剧本中的 `【】` 重音括号。

---

## 3. 五大工程质量红线（实测防坑铁律，严禁违背）

1. **【红线一：严禁复制上一集代码或套用固定特效顺序】**
   - 每一集必须根据当期题材用 23 个视觉 Skill 全新设计视觉语言与特效，**绝对禁止复制上一期项目的 `engine.html` 场景绘制函数或照搬分镜顺序**！
2. **【红线二：词组级渐进揭示，拒绝放 PPT 与拒绝无意义整屏缩放】**
   - 台词没念到的信息绝不提前画在屏幕上！每个镜头按语音词组时间戳（`t1, t2, t3`）分步生长、变形或展开，每一次视觉动作 100% 绑定物理音效；遵循 `motion-art-direction` 的运动层级（Hero / Support / Texture），严禁对整张画布做机械的来回缩放。
3. **【红线三：「林佳佳」数字人三级灵动出镜（严禁全屏裸放超过 3 秒）】**
   - `55%~65%` 时长为角落灵动伴讲窗（`HostCam / PiP`，占屏高 `15%~20%`，随主视觉重心避让）；`20%~25%` 时长为半屏立体相框主讲（重点词 `100% ➔ 115%` 瞬切推近）；`15%~20%` 时长为纯全屏高燃视觉特效。
4. **【红线四：实拍图片必过 `Read` 肉眼验图关 + 人像防斩首焦点裁剪】**
   - 每张下载的图片必须立即调用 `Read` 肉眼审阅，淘汰原图无头、图文不符或带水印的照片。
   - **严禁使用 `ctx.drawImage(img, cx - dw/2, cy - dh/2, dw, dh)` 几何居中裁剪**！必须在 `PHOTO_META` 中声明每张图的人物头部焦点 `(focalX, focalY)`，将头部锚定在视口上黄金位 `y + h * 0.30` 并钳制边界，确保 100% 零无头人像。
5. **【红线五：零黑屏确定性渲染参数 + 文本框动态测量安全边距】**
   - Playwright Chromium 渲染时必须传入 `--allow-file-access-from-files --disable-web-security --disable-gpu --disable-accelerated-2d-canvas --disable-gpu-compositing`，并在编码前通过像素均值扫描验证 `0 black frames`。
   - 所有带边框/背景的文字容器宽度必须通过 `ctx.measureText(text).width + padX * 2`（`padX >= 48px`）动态计算，杜绝文字挤边或溢出。
