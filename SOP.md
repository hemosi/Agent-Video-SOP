# Agent 知识类视频全自动制作 SOP 与 24-Skill 协同总纲

> **工程主目录**：`E:\AI自媒体\Agent知识类视频SOP`
> **参考知识库（只读文档库）**：`E:\Obsidian_Note\知识库\04_领域\代码类视频`
> **核心定位**：以「林佳佳」虚拟数字人为主讲的 2~5 分钟（`1920×1080 @ 30fps`）泛知识类视频全自动生产流水线（涵盖 AI/代码科普、科技趋势、商业逻辑、社会观察、方法论拆解等，**非单一财经模板**）。

---

## 一、 核心架构设计：「叙事节奏核」与「开放视觉核」双核解耦

为彻底杜绝“做 10 期视频长一个样”的跨集同质化问题，本 SOP 采用严格的 **职责解耦架构**：

1. **【叙事与节奏核】`xiaolin-director`（只管讲故事、降维与视听节奏，0% 限定具体特效！）**：
   - 我们从小Lin说拉片中吸收的**只有她讲故事的能力、把专业词变人话的降维能力、留存钩子心机、以及 5~7 秒一变的剪辑节奏密度**；
   - **`xiaolin-director` 绝不规定具体的画面特效或固定图形模板**（严禁把财经图表、天平、圆球盖章等固定零件强加给所有视频）。
2. **【开放视觉与动效核】23 个筛选出的专业视觉 Skills（占 100% 视觉权重，按题材自由创造）**：
   - 每期视频的**美学基调、数字人舞台包装、界面变形、空间运镜与高级视觉特效**，完全由 `.claude/skills/` 下筛选出的 **23 个开源专业视觉 Skill** 与 `weilanx-claude-videos/styles/解说语法/` 根据当期具体题材自由组合与从零生成！

```text
E:\AI自媒体\Agent知识类视频SOP\
├── CLAUDE.md                                # Agent 全局指令入口（每次会话自动加载）
├── SOP.md                                   # 本文件：7 步全自动 SOP 与双核 Skill 调度总纲
├── Auk-TTS接口与视频配音使用文档.md            # 本地 Auk-TTS 自动检测、后台无阻塞启动与调用规范
├── .claude/skills/                          # 【双核 Skill 矩阵：共 24 个】
│   │
│   ├── ★ [叙事与节奏核：只管剧本故事、口语降维、节奏密度与声音卡点]
│   │   ├── xiaolin-director/                    # 10大降维公式、6大留存心机、5~7s节奏与林佳佳出镜配比
│   │   ├── beat-sync-editing/                   # 声画帧级对齐、重拍切镜与转折处 BGM 骤停留白
│   │   └── sound-design/                        # 37款精选无损音效映射 + Python 物理音效合成兜底 + -14 LUFS母带
│   │
│   ├── ★ [开放视觉与高级动效核：100% 主导画面风格与特效，按每期题材自由选型]
│   │   ├── motion-art-direction/                # [视觉总控] 为每期定制独立的 Tone & Energy 动态语言与运动层级
│   │   ├── color-motion/                        # [色彩总控] 为每期定制专属 OKLCH 色板与对比度规范
│   │   ├── shot-composition/                    # [构图总控] 视觉焦点、网格留白与人像防切头规范
│   │   ├── cinetic/                             # [电影级特效引擎] RackFocus光学景深、Morph变形、Iris遮罩、3D视差漫游
│   │   ├── motion-effects/                      # [16种高级交互变形] 按钮变播放器、搜索变结果、卡片展开为工作区、3D透视
│   │   ├── klik-anim/                           # [元素动效法则] 非线性弹簧缓动、预备动作、防机械感与阅读停留计算
│   │   ├── klik-cam/                            # [摄像机运镜] C0-C5 运镜能量拨盘、动量交接与速度峰值快门模糊
│   │   ├── animation-principles/                # [动画物理十二法则] 挤压拉伸、跟随重叠、次级动作
│   │   ├── motion-design/                       # [UI动效质感] 弹簧物理参数与交错延迟(Stagger)
│   │   ├── gsap-timeline/ & gsap-plugins/       # [复杂时间线与SVG] 多步时间线编排、路径生长追踪与文字解码
│   │   ├── title-sequence-3d/                   # [3D空间片头] Three.js 电影级 3D 空间穿梭章节片头
│   │   ├── milestone-reveal/                    # [粒子聚字] 漫天粒子聚拢成核心极值数字特效
│   │   ├── animated-chart/                      # [动态数据图] 仅在需要展示数据变化时调用的平滑变形图表
│   │   ├── weilanx-creator-desk-video/          # [数字人工作台骨架] 暖纸/深色工作台 + HostCam 数字人窗 + 终端/流程卡
│   │   ├── weilanx-creator-vox-video/           # [纪实文献拼贴骨架] 真实影像、文献剪报、动态高亮与硬切拼贴
│   │   └── weilanx-creator-blackgold-video/     # [暗调光影推演骨架] 粒子光晕、聚光灯推演与发光模型
│   │
│   └── ★ [方法论、蒸馏与质检核]
│       ├── klik-remotion-method/                # SSOT 单一事实源锁定与静态帧门禁
│       ├── weilanx-creator-distill-video/       # 新参考视频机器拆解与画面语法蒸馏
│       ├── reference-to-motion/                 # 参考片动作编排提取
│       └── review-loop/                         # 自动抽帧联系表 (Contact Sheet) 视觉质检闭环
│
├── 音效_精选/                                # 37 个工业级无损音效（见 音效索引.md & sfx_manifest.json）
├── sfx/                                     # Python 动态音效合成引擎（供 sound-design 实时兜底）
├── weilanx-claude-videos/                   # 含 src/library/ 组件库及 styles/ 下 48 套艺术与解说语法卡
└── projects/                                # 各期视频独立工程目录
```

---

## 二、 完整 7 步 SOP 全链路

### 环节 1：事实考据、素材搜集与「图片肉眼验真」（Research & Asset QA）
- **调用 Skill**：
  - `.claude/skills/klik-remotion-method/SKILL.md`（锁定单一事实源 `facts.json`）
  - `.claude/skills/shot-composition/SKILL.md`（构图焦点与人像头顶留白规范）
- **执行动作**：
  1. **联网考据一手事实（`facts.json`）**：查清当期主题的核心事实、数据、开源仓库/论文/报道原文。
  2. **按题材搜集真实视觉素材（`assets/photos/`）**：
     - 搜集与当期话题直接相关的真实图片（人物处境纪实照、真实产品界面截图、论文/文档原件、历史现场照等，优先选 `16:9 / 3:2` 横图）。
  3. **【强制门禁 1：下载后必过 `Read` 肉眼验图关 + 标注人像焦点 `(focalX, focalY)`】**：
     - 下载完每一张照片后，**必须立即调用 `Read` 工具逐张看图**！凡是：①原图本身人物无头或面部残缺；②图文不符；③带刺眼水印，当场删除重抓。
     - 为每张图片在 `PHOTO_META` 中记录主体/人物头部的归一化焦点坐标 `(focalX, focalY)`（如人像头部在 `focalY: 0.18 ~ 0.28`），供后续智能防切头裁剪使用。

---

### 环节 2：吸收小Lin讲故事与降维能力——编写高留存口播剧本（Script & Storytelling）
- **调用 Skill**：
  - `.claude/skills/xiaolin-director/SKILL.md`（维度二：四类选题讲故事路由与 6 大留存心机；维度三：10 大口语降维公式）
  - `.claude/skills/xiaolin-director/references/lapian-rules-compendium.md`（降维话术参考）
- **执行动作**：
  1. **选定当期讲故事路由**：根据题材属于「A.反直觉揭秘型 / B.技术工具方法论拆解型 / C.多方博弈大战型 / D.人物产品闯关型」选择最自然的叙事脉络，确立本期 **2~4 字核心锚词**。
  2. **植入 6 大留存心机**：前 20 秒立悬念钩子、先顺着直觉说再反转打脸（预期违背）、层层递进留扣子、前半程埋伏笔后半程回收、替观众抢先吐槽给大脑降压、片尾首尾呼应并抛出评论区互动问题。
  3. **执行口语化降维改写**：
     - 把复杂术语翻成“XX版的生活常识词”；
     - 先用大白话算明白再抛专业概念（先俗后雅）；
     - 把枯燥原理放进“林佳佳奶茶店/小工作室”生活沙盘或第一人称戏精小剧场里演出来；
     - 用 `【】` 标出每一句的核心重音词（供字幕花字实时放大高亮）。
- **产出物**：`facts.json` + `script.md`。

---

### 环节 3：本地 Auk-TTS 自动检测启动与声画时间轴构建（Audio First）
- **调用文档与 Skill**：
  - [`Auk-TTS接口与视频配音使用文档.md`](./Auk-TTS接口与视频配音使用文档.md)
  - [`音效_精选/音效索引.md`](./音效_精选/音效索引.md) & `.claude/skills/sound-design/SKILL.md` & `.claude/skills/beat-sync-editing/SKILL.md`
- **执行动作**：
  1. **自动检测并后台无阻塞启动 `Auk-TTS`**：
     - 先执行 `curl -s http://127.0.0.1:7863/api/health`；
     - **若未启动，Agent 直接在 Bash 中设置 `run_in_background: true` 执行以下命令**（切勿直接跑带 `pause` 的 `.bat`）：
       ```bash
       cd "F:/Aku-tts/Auk-TTS/Auk-TTS" && "F:/Aku-tts/Auk-TTS/Auk-TTS/py312/python.exe" "F:/Aku-tts/Auk-TTS/Auk-TTS/app.py"
       ```
     - 等待 7 秒确认 `/api/health` 返回 `"gateway": "ok"`。
  2. **合成自然语速干声与词级时间轴**：
     - 根据角色设定选用音色：`小林`（`52920896bd09`）、`女主播`（`08482905d56e`）或 `烛灵儿`（`3528e1c71180`），保持 **`speed=1.0` 原生语速**（严禁 `atempo` 加速），发送前用正则剥离 `【】` 括号。
     - 由真实音频时长驱动每镜总帧数及镜内 **3~4 个词组级渐进揭示点（`t1, t2, t3, t4`）**。
  3. **混入 BGM（含转折骤停）与 100% 物理音效**：
     - 优先从 `音效_精选/sfx_manifest.json` 调取 37 款无损音效；遇到科技/代码/特殊物理场景音效，调用 `sfx/synth.py`（`sound-design`）实时合成 48kHz 采样；
     - 在重大反转句或破冰打断处，**将 BGM 瞬间静音留白 0.8~1.2 秒**；母带统一标准化至 `-14 LUFS`。
- **产出物**：`timing.json` + `build/audio_master.wav`。

---

### 环节 4：由 23 个视觉 Skill 定义当期专属视觉语言与「林佳佳」数字人舞台（Visual Direction）
- **调用 Skill（高权重视觉核心）**：
  - `.claude/skills/motion-art-direction/SKILL.md`（确定当期 Tone & Energy 矩阵定位与动态语言表）
  - `.claude/skills/color-motion/SKILL.md`（定制当期专属色板，避免花花绿绿，也避免期期同色）
  - `.claude/skills/weilanx-creator-desk-video/SKILL.md` / `vox-video` / `blackgold-video` + `weilanx-claude-videos/styles/解说语法/`
- **执行动作**：
  1. **【跨集反克隆铁律：严禁复制上一期代码或套用固定特效顺序】**：
     - 每一期必须根据当期知识主题（如 AI Agent 架构、社会现象、科技产品、心理学效应），从 `motion-effects`、`cinetic`、`weilanx-claude-videos/styles/解说语法/` 中选择最契合本期主题的视觉语言，编写当期独立的 `style_spec.md`。
     - **绝对禁止复制上一期项目的 `engine.html` 场景绘制函数！**
  2. **「林佳佳」数字人三级灵动出镜包装（规避数字人全屏久看瑕疵）**：
     - **角落灵动伴讲窗（`HostCam / PiP`，占 55%~65% 时长）**：数字人占屏高 `15%~20%`，挂在角落随主视觉焦点平滑避让；
     - **半屏立体相框主讲（占 20%~25% 时长）**：用于开场钩子、关键转折、第一人称演戏（说到转折词前一帧景别 `100% ➔ 115%` 瞬切推近），旁侧同步展开动态视觉；
     - **纯全屏沉浸特效（占 15%~20% 时长，隐藏数字人）**：用于 3D 空间片头（`title-sequence-3d`）、粒子聚字（`milestone-reveal`）、实拍快切、高潮特效变形。

---

### 环节 5：调用高级特效 Skill 编写动态画面（Build & Choreography）
- **调用 Skill**：
  - `.claude/skills/cinetic/SKILL.md`（`<RackFocus>` 光学景深、`<Morph>` 变形、`<Iris>/<MaskRise>` 遮罩、`<Scramble>/<Roll>` 文字解码与滚轮、多层 3D 视差）
  - `.claude/skills/motion-effects/SKILL.md`（16 种界面/数据/文字/系统级动态变形特效）
  - `.claude/skills/klik-anim/SKILL.md` & `.claude/skills/klik-cam/SKILL.md` & `.claude/skills/animation-principles/SKILL.md`
  - `.claude/skills/gsap-timeline/SKILL.md` & `.claude/skills/gsap-plugins/SKILL.md`
- **四大编码硬核规范**：
  1. **词组级渐进揭示（拒绝放 PPT 与拒绝无意义整屏缩放）**：
     - **台词没念到的信息绝不提前画在屏幕上**！每个镜头按 `t1, t2, t3` 随语音词组一步步生长、变形或展开。
     - 遵循 `motion-art-direction` 的 **Restraint（克制）与 Motion Hierarchy（Hero / Support / Texture 三层运动）法则**：同一帧内只有一个视觉主角（Hero）做大幅度慢缓动运动，背景与支撑框架保持稳定，严禁对整张画布做无意义的来回缩放。
  2. **人像防斩首焦点裁剪（Focal-Point Smart Crop）**：
     - **严禁使用 `ctx.drawImage(img, cx - dw/2, cy - dh/2, dw, dh)` 几何居中裁剪**（竖图或全身照放进横框时必切掉人头）！
     - 必须读取 `PHOTO_META` 中该图的 `(focalX, focalY)`，将人物头部锚定在视口上黄金位 `y + h * 0.30` 并钳制边界：
       ```javascript
       const scale = Math.max(w / iw, h / ih) * zoom;
       const dw = iw * scale, dh = ih * scale;
       const ox = Math.min(x, Math.max(x + w - dw, x + w * 0.50 - dw * focalX));
       const oy = Math.min(y, Math.max(y + h - dh, y + h * 0.30 - dh * focalY));
       ctx.drawImage(img, ox, oy, dw, dh);
       ```
  3. **文本框动态测量安全边距（Zero Border Squeeze）**：
     - 所有带边框/背景的文字容器必须通过 `ctx.measureText(text).width + padX * 2`（`padX >= 48px, padY >= 20px`）动态计算宽度，严禁文字贴边或溢出。

---

### 环节 6：抽帧联系表质检闭环与确定性无黑屏渲染（Critic Loop & Render）
- **调用 Skill**：
  - `.claude/skills/review-loop/SKILL.md` & `.claude/skills/cinetic/references/review-loop.md`
- **执行动作**：
  1. **先跑 `--mode qa` 生成全片分镜网格联系表（`qa_contact_sheet.jpg`）并调用 `Read` 肉眼审查**：
     - ① **人像完整性**：所有人物照片头部是否 100% 完整（零切头、零无头人像）？
     - ② **单集节奏与渐进性**：相邻镜头是否有明显的构图与景别变化？镜头内是否有词组级分步揭示？
     - ③ **排版与可读性**：文字对比度是否清晰，距边框是否有充足呼吸空间，有无被底部字幕遮挡？
     - ④ **跨集新鲜度（遮字盲测）**：与上一集联系表对比，是否做到了根据本期主题全新设计视觉（零复制上一集代码、零照搬上一集特效顺序）？
  2. **确定性无黑屏全量渲染（`--mode full`）**：
     - Playwright 启动 MS Edge/Chromium 时，**必须传入禁用 GPU 硬件加速标志**（防止多并发标签页 GPU 纹理回收黑屏）：
       ```python
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
       ```
     - 渲染后自动执行像素均值扫描（`arr.mean() < 8.0`），确认 `0 black frames detected` 后调用 FFmpeg 合成 1080p MP4。

---

### 环节 7：一锅出标准交付（MP4 + 封面 + 悬念标题发布文案）
每个单期项目目录（`projects/<ep_name>/`）最终输出：
1. `<ep_name>_1080p.mp4`（1080p @ 30fps 成片，`-14 LUFS` 响度标准化，0 黑屏认证）
2. `qa_contact_sheet.jpg`（全片分镜网格质检图）
3. `facts.json` & `script.md` & `timing.json`
4. `发布文案.md`（含 5 组 ≤20 字痛点悬念标题 + 简介 + 章节时间戳 + 评论区互动问题）
