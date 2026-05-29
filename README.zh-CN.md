<p align="center">
  <img src="./assets/demo-game-experience-before-after.png" alt="60 秒 demo：Game Experience Analyzer 把 PV 输入转成证据化报告" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  面向游戏设计、设计研究和 AI-assisted creator 的可复用 Agent Skill 库。
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#60-秒-demo">60 秒 demo</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#当前-skill">当前 Skill</a> ·
  <a href="#图文展示">图文展示</a> ·
  <a href="#项目治理">项目治理</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-4-2ea44f">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Evidence%20%7C%20VOI%20%7C%20OODA-f9a825">
</p>

> Copyright (c) 2026 @Paranoia. All rights reserved.

## 60 秒 Demo

输入一张截图、一段录屏、一个 PV/宣传片或视频链接，让 skill 直接输出证据化设计报告：

```text
Use $game-experience-analyzer to analyze this PV, predict heat potential, separate visible evidence from unknowns, and give validation metrics.
```

当前最强案例是 [`《黑神话：钟馗》6 分钟实机小短片热度潜力预测示例`](./game-experience-analyzer/examples/black-myth-zhongkui-trailer-heat-report.md)：一个公开视频样本会被拆成可见证据、热度分层、不确定性边界、Conditional Go 和下一轮素材验证计划。

## 这个项目是什么

`ParanoiaSkills` 是一套游戏设计工作流 Skill 库，把游戏体验分析、AI 工作流演化、专业翻译和资料策展，沉淀成可复用、可验证、可迁移的 agent instructions、references、templates 和 examples。

它不是一堆提示词合集。这个项目更像一套小型游戏设计操作系统：

```text
分析游戏截图、录屏、PV 和视频链接
-> 演化执行这些工作的 agent workflow
-> 翻译并结构化设计知识
-> 策展高质量资料和可复用来源
```

## 为什么值得收藏

- **Evidence-first:** 不写泛泛总结，尽量把判断绑定到来源、截图区域、时间戳、样本证据或验证指标。
- **Workflow-first:** 不追求一次漂亮回答，而是把可复用流程沉淀到 `SKILL.md`、`references/` 和 `templates/`。
- **Game-design native:** 面向真实游戏设计工作：体验、玩法、MDA、系统叙事、品类、窗口期、商业化、素材和生产流程。
- **Agent portable:** 不绑定单一工具；Codex、Claude Code、OpenCode 或其他能读取 Markdown skill 的 agent 环境都可以迁移。
- **Controlled evolution:** 用 VOI、OODA、eval、Human Gate 和 rollback 防止工作流越改越漂。

## 快速开始

在支持 skill 的 agent 环境里，直接点名对应 skill：

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema with VOI, OODA, evals, Human Gate, and rollback.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

## 图文展示

<table>
  <tr>
    <td width="25%">
      <img src="./assets/showcase-game-experience-analyzer.png" alt="Game Experience Analyzer 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator 展示图">
    </td>
  </tr>
  <tr>
    <td><b>分析游戏体验</b><br>把截图、录屏、宣传片和视频链接，转成证据优先的游戏设计报告。</td>
    <td><b>演化工作流</b><br>用 VOI、OODA、eval、Human Gate 和 rollback 升级 prompt、schema、memory 和 tool routing。</td>
    <td><b>翻译设计知识</b><br>把严肃的游戏设计书籍和章节，变成自然、专业、可复查的中文设计写作。</td>
    <td><b>策展资料</b><br>把散落在文章、视频、作者、专栏和网站里的内容，变成可长期维护的游戏设计知识库。</td>
  </tr>
</table>

## 当前 Skill

| Skill | 一句话用途 | 适合场景 | 包目录 |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | 把截图、录屏、PV/宣传片和视频链接拆成证据优先的中文游戏设计报告。 | 体验分析、玩法机制、整体项目、MDA、系统叙事、单机流程、热度预测、前瞻窗口、商业化、UX。 | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | 把 prompt、workflow、memory、schema、tool routing 和 eval 改动变成受控系统演化。 | VOI/OODA、模型压缩、因果中介、Human Gate、rollback、可验证升级。 | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | 把英文游戏设计/研发材料翻译成真正像中文设计写作的专业文本。 | 术语、章节、图注、表格、QA、来源边界检查。 | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | 把散落资料变成可长期维护的游戏设计知识库。 | 来源筛选、评分、HTML 归档、registry、update history、设计实验卡。 | [`game-design-source-curator/`](./game-design-source-curator/) |

## 典型用例

- **竞品体验复盘:** 给一段录屏，输出时间轴、功能账本、玩法循环、问题优先级和修改建议。
- **PV 热度预测:** 给宣传片链接，判断首秒钩子、卖点复述、可玩性证明、平台适配、转化承接和验证计划。
- **前瞻机会判断:** 判断题材/玩法是否还有窗口；休闲轻度默认 1-3 个月，微小中重度默认 3-6 个月。
- **资料策展:** 把文章、视频、作者、专栏和网站沉淀成可检索、可引用、可实验的知识库。
- **专业翻译:** 把游戏设计书籍或长文翻成自然中文，同时保留术语、论证结构和图表语境。
- **工作流升级:** 把一次有用的 agent 行为升级成候选规则，并用 eval、Human Gate 和 rollback 控制风险。

## 项目结构

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- assets/
|   |-- demo-game-experience-before-after.png
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-game-experience-analyzer.png
|   |-- showcase-voi-ooda.png
|   |-- showcase-book-translator.png
|   `-- showcase-source-curator.png
|-- game-experience-analyzer/
|-- paranoia-ai-system-evolver/
|-- game-design-book-translator/
`-- game-design-source-curator/
```

每个 skill 通常使用同一套结构：

```text
SKILL.md      -> agent 入口、触发条件、核心流程、边界
references/  -> 方法、评分规则、路由、质量门、验证 playbook
templates/   -> 可复制到真实任务中的表单和输出结构
examples/    -> 可复查的示例输出
agents/      -> 支持对应元数据的 agent 环境可读取
evals/       -> 用于回归检查的提示和预期行为
```

## 安装与使用

这个仓库里的 skill 是可迁移包。典型使用方式：

1. 将某个 skill 目录复制或同步到你的 agent skill 目录。
2. 确认 `SKILL.md` frontmatter 的 `name` 与目录名一致。
3. 在 agent 中用 `$skill-name` 或自然语言触发。
4. 按对应 README 或 `SKILL.md` 的验证方式检查 JSON/YAML、引用路径和示例。

## 项目治理

- 根目录 README 只讲整个 `ParanoiaSkills`：定位、目录、结构、用例和治理规则。
- 每个 skill 目录只讲一个具体可安装 skill。
- 区分会话命令和项目规则：用户在协作中给 Codex 的临时指令、执行命令、偏好纠偏和一次性上下文，不会自动写入这个公开项目。只有可复用、可公开、可验证，或用户明确要求沉淀的内容，才进入 README、SKILL、references、templates 或 examples。
- `SKILL.md` 保持轻量，只放触发条件、核心流程、边界和按需读取路径。
- 长文方法论放进 `references/`。
- 可复制工作表单放进 `templates/`。
- `SKILL.md` frontmatter `name`、文件夹名、`agents/openai.yaml` 默认提示保持一致。
- 如果某个 skill 有运行副本，后续运行副本发生变化时，必须同步回本项目同名目录，并校验两边副本。

## 设计原则

```text
Evidence before opinion.
Workflow before one-off prompts.
VOI before research.
Eval before promotion.
Rollback before confidence.
```

## 未来 Skill

未来根据社区反馈和 skill 成熟度，可能继续加入 AI + 独游实战全流程方向的包，例如：

- `indie-game-production-master`：覆盖独游从想法验证、GDD/Gate、原型、playtest、AI 资产流水线、Steam/发布策略到复盘沉淀的全流程制作 skill。
- `godot-ai-game-production`：覆盖 Godot + AI 项目搭建、设计真源、数据契约、资源流水线、headless/keyshot 验证、Demo/Release Gate 和工程复盘的生产 skill。

## 版权

Copyright (c) 2026 @Paranoia. All rights reserved.
