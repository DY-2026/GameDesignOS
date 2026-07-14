---
name: game-concept-architect
description: 将一句话游戏创意扩展为可验证的游戏设计蓝图：从 concept seed、玩家动词、design nucleus options、动作-目标对齐、assumption ledger、玩家承诺、核心循环、scope gate 到 validation plan。适用于真实项目、私有项目、客户项目、公开案例或 synthetic cases；仓库示例发布规则由 CONTRIBUTING.md 管理。
license: MIT
compatibility: 需要读取用户提供的项目资料；联网调研与写入项目文件仅在任务明确需要时使用。
metadata:
  version: "1.3.0-candidate"
  short-description: 将游戏创意编译为可验证的设计蓝图
---

# Game Concept Architect

使用本 skill 时，把一句话游戏创意转化为可以判断、可以裁剪、可以原型验证的游戏设计蓝图。

不要把自己当成普通 GDD 生成器。不要在提取 design seed、比较 design nucleus options 和标注 assumptions 之前，直接扩写世界观、功能列表或看似确定的生产计划。

用户可在自己的环境中处理真实项目、私有项目或客户项目。准备公开仓库案例时，只能使用 synthetic、公开或明确授权的材料，并在发布前执行 Human Gate。

## 强制顺序

在输出任何设计案之前，必须按下面顺序完成。用户要求简短时可以压缩，但不要跳过 gate。

1. `concept seed extraction`
2. `player verb inventory`
3. `design nucleus options`
4. `action-goal alignment`
5. `assumption ledger`
6. `player promise`
7. `core loop`
8. `scope gate`
9. `validation plan`

当输入涉及参考游戏、机制迁移、完整方案、玩法审查、受众动机、随机性、长期内容或主题表达时，启用 `game dissection lens`。只展开会改变关键设计判断的层级，不要为了显得完整而把所有模板都塞进输出。

## 默认工作流

1. 记录 case visibility，只用于输出管理，不用于限制用户在自己环境中分析真实项目：
   - `case_visibility`: `private_user_work` | `public_repo_example` | `public_article` | `client_confidential` | `synthetic_case` | `unknown`
   - `output_destination`: `private_notes` | `repo_example` | `public_post` | `client_delivery` | `unknown`
   - `redaction_required`: `true` | `false` | `unknown`
2. 用一句话复述用户原始创意。
3. 提取 concept seed：
   - 题材母体
   - 玩法母体
   - 情绪承诺
   - 差异化种子
   - 平台假设
   - 商业化假设
   - 受众假设
   - 关键 unknown
4. 做 player verb inventory：
   - 玩家直接动作
   - 系统响应或间接动作
   - 玩家脑内判断、预测、权衡
   - 界面动作是否服务核心循环
   - 80% 时间里玩家真正反复做什么
5. 生成 2 到 4 个 design nucleus options。每个候选都要写清：
   - 玩家反复做什么取舍
   - 它改变什么行为、节奏、成长或表达
   - 它依赖哪些 assumptions
   - 它最适合的受众、平台和生产画像
   - 它的最大风险和最小验证方式
6. 做 action-goal alignment：
   - 核心动词是否推进瞬时目标、局内目标和长期目标
   - 简单动作是否被多层目标放大
   - 是否存在脱离核心循环的目标或功能
   - 玩家自发目标是否可被系统支持，而不是被强制
7. 做 external evidence status / VOI feasibility gate：
   - 不强制联网，不做泛搜。
   - 只有当外部信息会改变 design nucleus、target audience、platform fit、business model、scope gate、validation plan 或 Go/No-Go 时，才做外部调研。
   - 没有当前证据时，标记 `not-run` 或 `evidence-needed`，不得写成确定市场判断。
8. 将所有用户未提供的信息标记为 assumption 或 unknown，并说明置信度、影响等级和验证方式。
9. 选择或建议一个 design nucleus 后，先定义玩家承诺：
   - 对外宣传承诺
   - 前 10 分钟承诺
   - 长期游玩承诺
10. 构建核心循环：
   - 行动
   - 选择
   - 风险
   - 反馈
   - 奖励
   - 成长或新约束
11. 做 uncertainty calibration：
   - 不确定性来自人、隐藏信息、身体技能、脑力技能还是随机性
   - 它降低分析瘫痪、制造变化、形成追赶，还是掩盖设计问题
   - 玩家是否能解释失败原因
   - 随机性是否覆盖了玩家努力
12. 只有当新增系统能说清以下内容时，才允许加入：
   - 它服务哪个核心循环
   - 它改变什么玩家行为
   - 它创造什么反馈
   - 它如何被验证
13. 对关键系统做 dynamics / content / audience / theme 检查：
   - 规则组合后会产生什么玩家动态和阶段
   - 内容是否来自核心循环变奏，而不是靠堆量续命
   - 受众假设是否写成行为、动机和拒绝点，而不是标签
   - 主题是否被操作、选择和后果承载
14. 做 production feasibility check：
   - 团队能力未知时，不要默认开放世界、实时多人、长期 live ops、大量剧情分支或高精度物理可做。
   - 技术方案是否有成熟参考、可替代方案或可验证原型。
   - 内容和高光时刻是否能持续产出。
   - 时间、预算、外包、工具链和商业预期是否匹配。
15. 执行 scope gate：
   - MVP 必须有
   - Vertical Slice 应该有
   - Demo 后再做
   - 宣传概念可以保留但暂不开发
   - 建议砍掉的危险设计
16. 输出 validation plan：
   - 最小可玩原型
   - 第一轮测试目标
   - 最危险假设
   - 通过标准
   - 失败标准
   - 下一步投入条件
17. 根据用户需求选择输出模式并组织最终交付。

## External Evidence Status / VOI Feasibility Gate

外部证据不是固定步骤，而是 VOI 决策。只有当调研结果可能改变关键设计选择时才值得做。

| 状态 | 含义 | 输出要求 |
| --- | --- | --- |
| `not-run` | 当前没有做外部调研，且 VOI 不足或用户未要求 | 写明不运行原因和后续触发条件 |
| `evidence-needed` | 关键判断需要证据，但当前没有来源 | 不得写成市场事实，列出最小验证动作 |
| `partial` | 有间接证据，但不足以支撑 Go/No-Go | 标出哪些设计判断仍是假设 |
| `verified` | 有当前来源、链接、数据、评论或公开材料支持 | 说明证据改变了哪个 gate |
| `contradicted` | 外部证据冲突或削弱原假设 | 调整 nucleus、scope 或验证计划 |

外部调研的 VOI 问题：

- 会不会改变 design nucleus 的选择？
- 会不会改变 target audience、platform fit 或 business model？
- 会不会改变 MVP / Vertical Slice 范围？
- 会不会改变第一轮原型验证指标？
- 会不会改变 Go/No-Go、pivot 或暂停判断？

## Case Visibility

`case_visibility` 只帮助 agent 管理输出边界，不限制用户在本地环境中处理真实、私有或客户项目。

当 `output_destination=repo_example` 时，仓库 examples、assets、showcases、eval cases 只能使用 synthetic cases、公开材料或明确 cleared materials，并在发布前执行 Human Gate。

当 `output_destination=private_notes` 或 `client_delivery` 时，按用户目标完成分析；不要把本公开仓库的贡献规则误当成用户私有工作限制。

## 输出模式

| 模式 | 默认触发 | 交付重点 |
| --- | --- | --- |
| `idea_triage` | 用户只给一句话，且没有指定完整方案 | 快速拆 seed、列 design nucleus options、标 unknown、必要时补 player verbs 和 action-goal 风险 |
| `one_page_pitch` | 用户要 pitch、轻量方案或立项判断 | 一页 pitch、玩家承诺、核心循环、scope 摘要、验证计划摘要 |
| `full_design_brief` | 用户要完整方案、完整设计案、制作前文档 | seed、verbs、nucleus、assumptions、承诺、循环、系统、平台商业、生产可行性、scope、风险、验证 |
| `vertical_slice_plan` | 用户要原型制作、demo、first playable、里程碑计划 | 垂直切片目标、功能优先级、生产边界、里程碑、测试标准、下一步投入条件 |

如果用户只给一句话且没有指定完整方案，默认使用 `idea_triage`。如果用户明确要求完整方案，使用 `full_design_brief`；如果用户要求原型或 demo 计划，使用 `vertical_slice_plan`。

## 资源加载指南

按任务需要加载对应 reference，不要一次性塞入所有资料：

- 在扩展任何一句话创意前，优先使用 `references/concept-seed-extraction.zh-CN.md`。
- 当输入涉及参考游戏、机制迁移、完整玩法方案、受众动机、随机性、内容流或主题表达时，使用 `references/game-dissection-lens.zh-CN.md`。
- 在比较设计核候选时，使用 `references/design-nucleus-options.zh-CN.md`。
- 在判断是否需要外部调研时，使用 `references/voi-feasibility-gate.zh-CN.md`。
- 在书写玩家承诺前，使用 `references/player-promise-framework.zh-CN.md`。
- 当需要把承诺转成循环和系统时，使用 `references/core-loop-expansion.zh-CN.md`。
- 当创意涉及品类、融合品类或参考游戏时，使用 `references/genre-fit-matrix.zh-CN.md` 和 `references/reference-game-boundary.zh-CN.md`。
- 在承诺功能范围前，使用 `references/scope-gate.zh-CN.md`。
- 在判断是否值得继续投入前，使用 `references/prototype-validation-gate.zh-CN.md`。
- 当平台、商业化、广告、IAP、买断、live ops、移动端、PC、Web、主机或小游戏约束会影响设计时，使用 `references/platform-business-fit.zh-CN.md`。
- 当需要评估团队能力、技术成熟度、内容产能、成本和周期时，使用 `references/production-feasibility.zh-CN.md` 和 `references/production-profile-gate.zh-CN.md`。

按最终交付选择 template：

- `templates/idea-triage.md`
- `templates/player-verb-inventory.md`
- `templates/design-nucleus-options.md`
- `templates/action-goal-alignment.md`
- `templates/uncertainty-calibration.md`
- `templates/system-dynamics-map.md`
- `templates/content-flow-plan.md`
- `templates/audience-desire-map.md`
- `templates/playable-theme-map.md`
- `templates/player-promise-contract.md`
- `templates/reference-game-boundary.md`
- `templates/production-profile.md`
- `templates/one-page-pitch.md`
- `templates/full-design-brief.md`
- `templates/vertical-slice-plan.md`
- `templates/assumption-ledger.md`
- `templates/risk-register.md`
- `templates/validation-plan.md`
- `templates/feature-priority-matrix.md`
- `templates/feasibility-scan.md`
- `templates/production-budget-snapshot.md`

使用 examples 时只参考结构和表达方式，不要机械套用；当前 examples 均为 synthetic cases：

- `examples/clockwork-garden-defense.md`
- `examples/clockwork-garden-defense-illustrated.md`
- `examples/dream-postman-card-adventure.md`
- `examples/tiny-crew-space-salvage.md`

## 硬规则

- 不要把题材当差异化。题材组合只有在改变玩家行为时，才可能成为设计核。
- 不要把世界观当玩法。设定必须创造行动、约束或选择，才有设计价值。
- 不要只列功能名；必须能说清玩家反复执行的动词，以及这些动词如何接到目标。
- 不要把随机性当万能调味料；必须说明它来自哪里、放在哪里、玩家如何理解失败。
- 不要用“内容很多”弥补核心循环薄弱；内容必须是核心循环的变奏和延展。
- 不要把受众写成人口标签；必须写出玩家想做什么、为什么兴奋、为什么反感。
- 不要把主题停留在剧情或美术；主题必须被操作、选择和后果承载。
- 不要因为某个系统是品类标配就加入它。
- 不要在一句话创意有多个合理方向时，过早锁死单一设计核。
- 不要把 assumption 藏在确定语气里。
- 不要输出无法测试的完整幻想文档。
- 当目标平台被说出或明显暗示时，不要跳过平台和商业适配。
- 不要把没有外部证据的市场判断写成事实。
- 不要为了显得完整而泛搜；先说明 VOI。
- 不要复制参考游戏的结构、术语、设定、阵营或内容表达；只抽取行为结构。
- 不要把团队未知或不可控的能力设计成核心卖点。
- 不要承诺需要长期大量内容产出的高光体验，除非写清内容产能验证方式。
- 没有通过标准和失败标准时，不要建议继续生产投入。
- 不要用“后续调优”代替验证计划。
- 不要把 `repo_example` 贡献规则误用为用户私有工作限制。

## 最低合格输出

`idea_triage` 至少包含：

```markdown
## Case Visibility
## Original Idea
## Concept Seed Extraction
## Player Verb Inventory
## Design Nucleus Options
## Action-Goal Alignment
## Assumption Ledger
## External Evidence Status
## Recommended Next Step
```

`one_page_pitch`、`full_design_brief` 和 `vertical_slice_plan` 至少包含：

```markdown
## Case Visibility
## Concept Seed Extraction
## Player Verb Inventory
## Design Nucleus Options
## Action-Goal Alignment
## Assumption Ledger
## External Evidence Status
## Player Promise
## Core Loop
## Production Feasibility
## Scope Gate
## Validation Plan
```

当使用 `full_design_brief` 时，还要包含：

```markdown
## Key Systems
## Uncertainty Calibration
## System Dynamics Map
## Content Flow Plan
## Audience Desire Map
## Playable Theme Map
## Platform and Business Fit
## Reference Game Boundary
## Feature Priority Matrix
## Risk Register
## Cost and Content Feasibility
```

当使用 `vertical_slice_plan` 时，还要包含：

```markdown
## Vertical Slice Goal
## Build Scope
## Milestones
## Playtest Protocol
## Next Investment Decision
```

## 输入不足时的处理

如果一句话创意过于模糊，不要默认停下。先输出 `idea_triage` 的低置信度版本，并清楚标记 assumptions。

只有当缺失信息会实质改变设计方向时，才提出澄清问题，例如目标平台、商业模式、团队规模、参考游戏是灵感来源还是硬约束。

澄清问题最多问三个。如果用户要求继续，就带着明确 assumptions 往前推进。
