# Game Experience Analyzer

**所属项目:** [ParanoiaSkills](../README.zh-CN.md)

**语言:** 简体中文 | [English](./README.en.md)

<p align="center">
  <img src="./assets/game-experience-analyzer-hero.png" alt="Game Experience Analyzer hero banner" width="100%">
</p>

<p align="center">
  <b>把游戏截图、录屏、PV/宣传片、买量素材、商店页和视频链接，转成可追溯证据 + 可执行诊断交付。</b>
</p>

<p align="center">
  <img alt="Skill" src="https://img.shields.io/badge/Codex%20Skill-game--experience--analyzer-2ea44f">
  <img alt="Language" src="https://img.shields.io/badge/Reports-Chinese-blue">
  <img alt="Inputs" src="https://img.shields.io/badge/Inputs-Screenshot%20%7C%20Recording%20%7C%20PV%20%7C%20URL-6f42c1">
  <img alt="Evidence First" src="https://img.shields.io/badge/Method-Evidence--First-f9a825">
</p>

`game-experience-analyzer` 是一个面向游戏诊断交付的 Codex skill。它不会把视频看完后写成泛泛观后感，而是先输出样本边界门，再建立 `evidence_id` 索引，最后根据用户场景选择诊断包和既有分析模式：前期体验、玩法机制、整体项目、MDA、系统叙事融合、单机流程、PV 热度预测、前瞻机会、品类策略、商业化或 UX/UI。

它适合游戏设计师、制作人、发行/宣发、竞品研究、AI-assisted game team 和任何需要把“我觉得这游戏不错/不行”变成“证据在哪里、问题是什么、下一步怎么验证”的使用者。

Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 为什么需要它

游戏体验分析最容易出两个问题：

- **只讲感受，不讲证据。** 说“上头”“节奏差”“卖点强”，但回不到哪一帧、哪一秒、哪个 UI、哪个循环。
- **一种模板打所有游戏。** 小游戏、单机、SLG、X+SLG、PV、试玩录屏、截图诊断全被套进同一套话术。

这个 skill 的目标很窄，也很实用：

```text
Input media -> Sample Scope Gate -> Evidence Index -> Diagnosis Pack -> Mode router -> Actionable report
```

它先判断输入来源和分析意图，再按样本边界、诊断包、品类和验证价值选择策略。四步体验法只是其中一种镜头，不是全局默认答案。

## 能分析什么

| 输入 | 适合分析 | 输出样式 |
| --- | --- | --- |
| Screenshot | UI 层级、主目标、入口拥挤、奖励表达、静态 Hook | 画面证据表 + UX/体验诊断 |
| Local recording | 首小时、新手期、教程、玩法循环、商业化打断 | 时间轴 + event stream + feature ledger |
| Trailer / PV | 会不会火、卖点是否清楚、能否转化、是否需要重剪 | 热度潜力分层 + 验证计划 |
| Paid creative | 首秒钩子、CTR 假设、素材误导、落地承接 | 快速诊断 + 创意验证计划 |
| Steam/store page | 首屏转化、标签/卖点、截图顺序、CTA 承接 | 页面转化诊断 + A/B 计划 |
| Video link | 公开视频、竞品录屏、云端素材、社媒片段 | 访问边界 + 可见证据 + 降级分析 |

## 分析模式

| 模式 | 适用场景 | 核心问题 |
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

## 诊断包

诊断包不是新分析模式，而是把用户场景映射到已有 modes 和必填 sections。路由定义在 [`references/diagnosis-pack-router.yaml`](./references/diagnosis-pack-router.yaml)。

| 诊断包 | 主 mode | 用途 |
| --- | --- | --- |
| PV 热度诊断包 | `trailer_heat_prediction` | 判断首秒钩子、卖点复述、可传播峰值和验证路径。 |
| 首小时留存诊断包 | `early_experience` | 诊断首小时流程、功能账本、困惑/失败信号和留存钩子。 |
| 核心循环诊断包 | `gameplay_mechanics` | 诊断核心动作、决策点、资源经济、成长解锁和循环闭合。 |
| Steam 页面转化诊断包 | `trailer_heat_prediction` + `ux_ui` | 诊断商店页首屏、标签、截图顺序、预告片和愿望单 CTA。 |
| 项目立项风险诊断包 | `foresight_opportunity` | 判断窗口期、机会类型、Go/No-Go、最小验证和 Kill 条件。 |
| 商业化打断诊断包 | `commercialization` | 诊断付费/广告/福利请求是否破坏当前玩家目标。 |
| 单机流程节奏诊断包 | `single_player_design` | 诊断主路径、pacing beats、agency、挑战反馈和 finish intent。 |

## 前瞻窗口默认值

前瞻判断会把“机会窗口”和“完整研发周期”分开。

| 范围 | 默认验证窗口 | 含义 |
| --- | --- | --- |
| 休闲轻度 | 1-3 个月 | 必须快速用素材、原型、点击、留存或转化信号证明方向 |
| 微小中重度 | 3-6 个月 | 必须证明核心玩法、留存、付费承接或市场转化，不能无限观察 |
| 大体量项目 | 自定义研发周期 | 研发可以更长，但阶段性机会验证仍按前两类拆分 |

## 快速开始

Use it directly in Codex:

```text
Use $game-experience-analyzer to analyze this local gameplay recording into a sample scope gate, evidence index, diagnosis pack route, gameplay mechanics findings, issue cards, and a validation plan.
```

中文请求也可以很自然：

```text
用 game-experience-analyzer 做一个单机流程节奏诊断包。先写样本边界和 evidence_id，再看关卡主路径、节奏、玩家自主权、挑战反馈和 finish intent。
```

```text
用 game-experience-analyzer 做 PV 热度诊断包。不要预测确定销量，只判断热度潜力分层、关键 unknown 和验证指标。
```

```text
用 game-experience-analyzer 做项目立项风险诊断包。给出窗口期、Go/No-Go、最小验证截止和 Kill 条件。
```

```text
用 game-experience-analyzer 做商业化打断诊断包。重点看广告/付费请求出现前玩家正在追什么目标，以及最小改法和验证计划。
```

输出分三档：

- 快速诊断：[`templates/quick-triage-report.md`](./templates/quick-triage-report.md)
- 标准报告：[`templates/experience-report.md`](./templates/experience-report.md)
- 咨询交付：[`templates/consulting-diagnosis-report.md`](./templates/consulting-diagnosis-report.md)

## 示例输出

示例索引见：

- [`examples/README.md`](./examples/README.md)

索引列出当前公开示例的 `input_type`、`diagnosis_pack`、`main_mode`、`confidence_boundary` 和输出文件。

## Contract Input

- GCA can export player-promise-contract.
- GEA can validate whether a prototype/video fulfills that contract.

当用户提供 `player-promise-contract` 时，先读取其中的 external promise、first 10 minutes promise 和 long-term promise，再用 Evidence Index 检查样本是否兑现了承诺、在哪些环节失真、下一轮 validation plan 应该验证什么。

## 工具准备

| 来源 | 最小配置 | 更好配置 |
| --- | --- | --- |
| Screenshot | 可直接分析 | OCR when UI text changes judgment |
| Local video | `ffmpeg` for frame extraction | sampled frames + dense event timeline |
| Video URL | browser access or visible metadata | `yt-dlp` equivalent + frame extraction |
| Speech/subtitles | optional | ASR only when voice/subtitle changes judgment |

缺工具时，报告会保留 `tool_readiness`：说明缺失项、影响范围、建议安装方式和本次降级范围，而不是编造没有看见的内容。

## 证据规则

- 报告必须先输出 Sample Scope Gate：样本边界、可判断范围、不可判断范围、关键 unknown。
- 每个重要判断都必须能回到 `evidence_id`，并能定位到截图区域、时间戳、关键帧、页面元数据或用户提供事实。
- 关键截图必须图文并茂：插入截图，并解释可观察事实、设计含义、诊断判断和迭代动作。
- Evidence Index 字段见 [`references/evidence-taxonomy.zh-CN.md`](./references/evidence-taxonomy.zh-CN.md)，结构校验见 [`templates/evidence-index.schema.json`](./templates/evidence-index.schema.json)。
- 结构化输出校验见 [`templates/structured-output.schema.json`](./templates/structured-output.schema.json)；字段示例/contract 见 [`templates/structured-output.example.json`](./templates/structured-output.example.json)，不得把 example 文件误称为 schema。
- 截图不能直接判断节奏、手感、等待和循环闭合；这些必须标 `uncertain`。
- PV/宣传片只能预测热度潜力和验证路径，不能包装成确定销量、流水或下载量预测。
- 外部调研必须符合 VOI：只有会改变品类判断、版本事实、竞品基准、市场热度、窗口阶段、Go/No-Go 或建议优先级时才做。
- 输出必须区分 `known`、`unknown`、`uncertain`、`access_notes` 和 `tool_readiness`。

## 项目边界

协作中的临时命令不等于开源项目规则。用户可能在一次对话里要求 Codex 执行某个步骤、避开某个表述、临时采用某个案例或按某种顺序工作；这些只约束当前任务。

只有满足以下条件之一，才写进这个 skill：

- 它能稳定提升其他使用者的分析质量。
- 它是可公开、可复用、可验证的方法、模板、示例或维护规则。
- 用户明确要求把它沉淀到项目里。

否则，把它当成本次协作上下文处理，不放进 README、SKILL、references、templates 或 examples。

## 包结构

```text
game-experience-analyzer/
|-- SKILL.md
|-- README.md
|-- README.en.md
|-- agents/
|   `-- openai.yaml
|-- evals/
|   |-- evals.json
|   |-- negative_cases.md
|   `-- rubric.yaml
|-- examples/
|   |-- README.md
|   `-- survival-33-days-gameplay-experience-report.md
|-- references/
|   |-- analysis-mode-router.yaml
|   |-- diagnosis-pack-router.yaml
|   |-- evidence-taxonomy.zh-CN.md
|   |-- foresight-opportunity-lens.zh-CN.md
|   |-- genre-strategy-router.yaml
|   |-- sample-scope-gate.zh-CN.md
|   |-- single-player-analysis.zh-CN.md
|   |-- system-design-review-lens.zh-CN.md
|   |-- tooling-setup.zh-CN.md
|   |-- trailer-heat-prediction.zh-CN.md
|   `-- video-analysis-workflow.zh-CN.md
`-- templates/
    |-- analysis-input.json
    |-- consulting-diagnosis-report.md
    |-- evidence-index.schema.json
    |-- experience-report.md
    |-- issue-card.md
    |-- mode-output-map.yaml
    |-- quick-triage-report.md
    |-- structured-output.example.json
    |-- structured-output.schema.json
    |-- trailer-heat-report.md
    |-- validation-plan.md
    `-- visual-evidence-card.md
```

## 验证

在仓库根目录运行：

```text
python scripts/validate_repo.py
python scripts/validate_skill.py game-experience-analyzer
```

所有 JSON/YAML 文件都应该能解析通过。

## 设计原则

```text
Evidence first.
Mode before framework.
Genre before recommendation.
VOI before research.
Validation before confidence.
```
