# Game Experience Analyzer

<p align="center">
  <img src="./assets/game-experience-analyzer-hero.png" alt="Game Experience Analyzer hero banner" width="100%">
</p>

<p align="center">
  <b>把游戏截图、录屏、PV/宣传片和视频链接，转成可追溯证据 + 可执行设计判断。</b>
</p>

<p align="center">
  <img alt="Skill" src="https://img.shields.io/badge/Codex%20Skill-game--experience--analyzer-2ea44f">
  <img alt="Language" src="https://img.shields.io/badge/Reports-Chinese-blue">
  <img alt="Inputs" src="https://img.shields.io/badge/Inputs-Screenshot%20%7C%20Recording%20%7C%20PV%20%7C%20URL-6f42c1">
  <img alt="Evidence First" src="https://img.shields.io/badge/Method-Evidence--First-f9a825">
</p>

`game-experience-analyzer` 是一个面向游戏设计分析的 Codex skill。它不会把视频看完后写成泛泛观后感，而是先建立截图/关键帧/时间戳证据，再根据任务选择合适镜头：前期体验、玩法机制、整体项目、MDA、系统叙事融合、单机流程、PV 热度预测、前瞻机会、品类策略、商业化或 UX/UI。

它适合游戏设计师、制作人、发行/宣发、竞品研究、AI-assisted game team 和任何需要把“我觉得这游戏不错/不行”变成“证据在哪里、问题是什么、下一步怎么验证”的使用者。

Copyright (c) 2026 @Paranoia. All rights reserved.

## Why This Exists

游戏体验分析最容易出两个问题：

- **只讲感受，不讲证据。** 说“上头”“节奏差”“卖点强”，但回不到哪一帧、哪一秒、哪个 UI、哪个循环。
- **一种模板打所有游戏。** 小游戏、单机、SLG、X+SLG、PV、试玩录屏、截图诊断全被套进同一套话术。

这个 skill 的目标很窄，也很实用：

```text
Input media -> Evidence timeline -> Mode router -> Design lenses -> Actionable report
```

它先判断输入来源和分析意图，再按品类和样本边界选择策略。四步体验法只是其中一种镜头，不是全局默认答案。

## What It Can Analyze

| Input | Best For | Output Style |
| --- | --- | --- |
| Screenshot | UI 层级、主目标、入口拥挤、奖励表达、静态 Hook | 画面证据表 + UX/体验诊断 |
| Local recording | 首小时、新手期、教程、玩法循环、商业化打断 | 时间轴 + event stream + feature ledger |
| Trailer / PV | 会不会火、卖点是否清楚、能否转化、是否需要重剪 | 热度潜力分层 + 验证计划 |
| Video link | 公开视频、竞品录屏、云端素材、社媒片段 | 访问边界 + 可见证据 + 降级分析 |

## Analysis Modes

| Mode | Use When | Core Questions |
| --- | --- | --- |
| `early_experience` | 首登、新手期、首小时、上头程度 | 玩家为什么继续？第一轮循环是否闭合？ |
| `gameplay_mechanics` | 玩法、机制、核心循环 | 玩家做什么动作？动作如何反馈和成长？ |
| `holistic_game_analysis` | 整体项目、产品定位、体验和市场一起看 | 产品承诺、玩法结构、内容供给、商业化和窗口是否互相支撑？ |
| `whole_game_mda` | 用户明确点名 MDA | Mechanics、Dynamics、Aesthetics 是否断裂？ |
| `systems_narrative_fusion` | 主题、价值冲突、玩法即叙事 | 主题是否由机制、选择和后果生成？ |
| `single_player_design` | 单机、关卡、Boss、叙事、开放/半开放流程 | critical path、pacing、agency 和挑战反馈是否成立？ |
| `trailer_heat_prediction` | PV、宣传片、预告片、买量素材 | 首秒钩子、卖点复述、可玩性证明、平台适配和转化承接如何？ |
| `foresight_opportunity` | 窗口期、立项价值、能不能跟 | 机会类型、剩余窗口、Go/No-Go、最小验证截止和 Kill 条件是什么？ |
| `genre_benchmark` | 品类、对标、X+SLG | 哪些策略可迁移，哪些不可迁移？ |
| `problem_diagnosis` | 哪里不好、怎么改 | 根因、最小改动、owner 和验证指标是什么？ |

## Foresight Window Defaults

前瞻判断会把“机会窗口”和“完整研发周期”分开。

| Scope | Default Validation Window | Meaning |
| --- | --- | --- |
| 休闲轻度 | 1-3 个月 | 必须快速用素材、原型、点击、留存或转化信号证明方向 |
| 微小中重度 | 3-6 个月 | 必须证明核心玩法、留存、付费承接或市场转化，不能无限观察 |
| 大体量项目 | 自定义研发周期 | 研发可以更长，但阶段性机会验证仍按前两类拆分 |

## Quick Start

Use it directly in Codex:

```text
Use $game-experience-analyzer to analyze this local gameplay recording into timestamped evidence, gameplay mechanics, MDA, Hook/Loop/Link/Surprise scores, and actionable recommendations.
```

中文请求也可以很自然：

```text
用 game-experience-analyzer 分析这个单机游戏录屏，重点看关卡主路径、节奏、玩家自主权、挑战反馈和整体 MDA。
```

```text
用 game-experience-analyzer 分析这个游戏宣传片，预测它有没有爆款潜力，并给出证据、置信度和验证指标。
```

```text
用 game-experience-analyzer 判断这个题材和玩法方向现在还值不值得做，给出窗口期、Go/No-Go、最小验证截止和 Kill 条件。
```

```text
用 game-experience-analyzer 整体分析这个游戏项目，不要只做 MDA，要把产品定位、玩法结构、内容供给、商业化长线、市场窗口和最小验证一起看。
```

## Example Output

示例报告见：

- [`examples/black-myth-zhongkui-trailer-heat-report.md`](./examples/black-myth-zhongkui-trailer-heat-report.md)

这个案例展示了一个重要边界：PV 可以证明传播兴趣、题材辨识度和文化讨论潜力，但不能直接证明核心玩法、系统叙事和长期产品质量。

## Tooling

| Source | Minimum Setup | Better Setup |
| --- | --- | --- |
| Screenshot | 可直接分析 | OCR when UI text changes judgment |
| Local video | `ffmpeg` for frame extraction | sampled frames + dense event timeline |
| Video URL | browser access or visible metadata | `yt-dlp` equivalent + frame extraction |
| Speech/subtitles | optional | ASR only when voice/subtitle changes judgment |

缺工具时，报告会保留 `tool_readiness`：说明缺失项、影响范围、建议安装方式和本次降级范围，而不是编造没有看见的内容。

## Evidence Rules

- 每个重要判断都必须能回到截图区域、时间戳、关键帧、页面元数据或用户提供事实。
- 截图不能直接判断节奏、手感、等待和循环闭合；这些必须标 `uncertain`。
- PV/宣传片只能预测热度潜力和验证路径，不能包装成确定销量、流水或下载量预测。
- 外部调研必须符合 VOI：只有会改变品类判断、版本事实、竞品基准、市场热度、窗口阶段、Go/No-Go 或建议优先级时才做。
- 输出必须区分 `known`、`unknown`、`uncertain`、`access_notes` 和 `tool_readiness`。

## Project Boundary

协作中的临时命令不等于开源项目规则。用户可能在一次对话里要求 Codex 执行某个步骤、避开某个表述、临时采用某个案例或按某种顺序工作；这些只约束当前任务。

只有满足以下条件之一，才写进这个 skill：

- 它能稳定提升其他使用者的分析质量。
- 它是可公开、可复用、可验证的方法、模板、示例或维护规则。
- 用户明确要求把它沉淀到项目里。

否则，把它当成本次协作上下文处理，不放进 README、SKILL、references、templates 或 examples。

## Package Layout

```text
game-experience-analyzer/
|-- SKILL.md
|-- README.md
|-- agents/
|   `-- openai.yaml
|-- evals/
|   `-- evals.json
|-- examples/
|   `-- black-myth-zhongkui-trailer-heat-report.md
|-- references/
|   |-- analysis-mode-router.yaml
|   |-- foresight-opportunity-lens.zh-CN.md
|   |-- genre-strategy-router.yaml
|   |-- single-player-analysis.zh-CN.md
|   |-- system-design-review-lens.zh-CN.md
|   |-- tooling-setup.zh-CN.md
|   |-- trailer-heat-prediction.zh-CN.md
|   `-- video-analysis-workflow.zh-CN.md
`-- templates/
    |-- analysis-input.json
    |-- experience-report.md
    |-- mode-output-map.yaml
    |-- structured-output.schema.json
    `-- trailer-heat-report.md
```

## Validation

The package should pass:

```powershell
$env:PYTHONUTF8='1'
python C:\Users\Admin\.codex\skills\.system\skill-creator\scripts\quick_validate.py D:\ai\voi-ooda-ai-system-evolver\game-experience-analyzer
```

And all JSON/YAML files should parse cleanly.

## Design Principle

```text
Evidence first.
Mode before framework.
Genre before recommendation.
VOI before research.
Validation before confidence.
```
