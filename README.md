# Agent 知识类视频全自动生产 SOP 与视觉动效体系

本项目为 2~5 分钟（`1920×1080 @ 30fps`）高阶动态视觉知识视频的全自动生产 SOP，采用**双核解耦架构**：
- **叙事与节奏核**：小Lin级故事留存逻辑、反直觉反转钩子、通俗大白话降维与微行动破局收尾；
- **视觉机制推演核**：包含 24 套专业级视觉动效 Skills（推演图形、巨型排版、动效缓动、相机景深、音效卡点）。

---

## 核心规范直达（AI / 开发者直接读取链接）

若使用大模型（Claude Opus、GPT-4o 等）进行分析，可直接读取以下 **Raw 纯文本直链**：

1. **全链路制作流程（SOP）**：
   - [SOP.md (Raw 直链)](https://raw.githubusercontent.com/hemosi/Agent-Video-SOP/main/SOP.md)
2. **全局工作规范与核心生死线**：
   - [CLAUDE.md (Raw 直链)](https://raw.githubusercontent.com/hemosi/Agent-Video-SOP/main/CLAUDE.md)
3. **视觉叙事与机制推演总导演 Skill**：
   - [xiaolin-director/SKILL.md (Raw 直链)](https://raw.githubusercontent.com/hemosi/Agent-Video-SOP/main/.claude/skills/xiaolin-director/SKILL.md)
4. **配音自启动与音效使用规范**：
   - [Auk-TTS 接口与视频配音使用文档.md (Raw 直链)](https://raw.githubusercontent.com/hemosi/Agent-Video-SOP/main/Auk-TTS%E6%8E%A5%E5%8F%A3%E4%B8%8E%E8%A7%86%E9%A2%91%E9%85%8D%E9%9F%B3%E4%BD%BF%E7%94%A8%E6%96%87%E6%A1%A3.md)

---

## 仓库架构

```
.
├── .claude/skills/         # 24 套视觉动效、运镜、图表与总导演 Skills
├── sfx/                    # 动态音频合成、响度计算与分贝匹配工具
├── weilanx-claude-videos/  # 动效解说语法与视觉资产子模块
├── SOP.md                  # 七步全自动制作标准 SOP
├── CLAUDE.md               # 视觉机制推演核心原则与四项一票否决门禁
└── Auk-TTS接口与视频配音使用文档.md  # 本地配音自启动与音效卡点规范
```

---

## 四项一票否决门禁（静音遮字幕盲测）

1. **静音推理盲测**：遮住最底部字幕，仅看画面中的大字、大数字、公式和图形推导，必须能秒懂推导逻辑，严禁“空洞风景画/屏保”。
2. **字阶主角检查**：关键数字、公式与核心命题字号必须达到 `60px ~ 200px` 充当画面主体。
3. **零 PPT 外壳检查**：严禁 UI 方框卡片面板、顶部状态栏和底部胶囊框。
4. **收尾实效检查**：结尾必须给出定律破局金圈与具体微行动清单，杜绝空洞口号。
