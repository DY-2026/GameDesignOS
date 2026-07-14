---
name: game-design-proposal-writer
description: 将调研、概念架构、体验诊断、验证计划、脑图/xmind/系统设计图、已有策划案和生产约束收束为商业游戏策划案、独立游戏设计案、立项评审稿、发行/投资 pitch 或 vertical slice 设计文档。适用于一句话创意先经 game-concept-architect 生成概念契约后再成案、玩法/系统脑图转可落地策划案、审核并改进已有策划案。强调证据边界、受众与商业适配、scope gate、里程碑、风险、决策请求和下一步投入条件；不替代上游创意生成或体验诊断。
license: MIT
compatibility: 需要读取上游概念、证据或实验材料；公开发布、真实投资或范围锁定必须经过 Human Gate。
metadata:
  version: "1.3.0-candidate"
  short-description: Write decision-ready commercial and indie game design proposals
---
# Game Design Proposal Writer

使用本 skill 时，把已经存在的调研材料、创意方案、玩家承诺、竞品证据、体验诊断、ED 实验、生产约束和商业目标，整理成可以被制作人、老板、发行、投资人、合作方或独立团队成员评审的游戏策划案/独游设计案。

它不是普通 GDD 生成器，也不是把一句话创意扩写成长文的工具。创意还没有被拆出 design nucleus 时，优先提醒使用 `game-concept-architect`；样本体验还没有证据层时，优先提醒使用 `game-experience-analyzer`；需要一周体验实验时，优先提醒使用 `game-experience-density-optimizer`。本 skill 的核心工作是把上游产物变成一份有受众、有论证、有取舍、有风险、有下一步决策的文档。

如果用户给的是一句话创意，但明确要求“写策划案/立项案/独游设计案/pitch/GDD”，不要直接跳过上游。先调用 `game-concept-architect` 产出 concept brief、player-promise-contract、core loop、scope gate 和 validation plan，再用本 skill 成案。最终文档要标注“上游概念由本轮自动生成，证据等级仍为 assumption / needs_research”。

用户可在自己的环境中处理真实项目、私有项目或客户项目。准备公开仓库案例时，只能使用 synthetic、公开或明确授权的材料，并在发布前执行 Human Gate。

## 什么时候使用

当用户想写、改写、压缩或评审以下材料时，使用本 skill：

- 商业游戏策划案、立项案、产品方案、项目建议书。
- 独立游戏设计案、GDD、Steam/发行 pitch、Demo/Vertical Slice 方案。
- 给老板、制作人、发行、投资人、合作方或团队看的项目说明。
- 把调研报告、创意方案、竞品分析、玩家承诺和验证计划整合成一份文档。
- 把一句话创意先经 `game-concept-architect` 拆成概念契约，再整理成正式策划案。
- 把玩法脑图、系统设计脑图、xmind、OPML、Markdown 大纲、Word/Excel 导出的设计表，整理成可落地策划案。
- 审核、重写、压缩或改进已有商业策划案、独游设计案、GDD、pitch outline、vertical slice 文档。
- 把过长、幻想化、没有决策点的设计案改成可评审版本。
- 需要说明平台、商业模式、目标用户、核心循环、系统范围、制作成本、里程碑和风险。

以下请求要强触发：

- 写一份商业游戏策划案
- 写一份独游设计案
- 写 GDD / Game Design Document
- 写立项案 / 项目方案 / 产品方案 / pitch deck 文案
- 给发行 / 投资人 / 老板看的游戏方案
- 把这个创意整理成正式策划案
- 只有一句话创意，帮我写成策划案 / 立项案 / pitch
- 这个 xmind / 脑图 / 系统图帮我做成可落地策划案
- 审核这份策划案 / 改进这份 GDD / 帮我把已有方案改成能评审的版本
- 把调研和创意合成一份文档
- 改成能立项评审的版本
- 做 vertical slice 文档 / demo 方案

## 不适用场景

如果用户只有一句话创意，并且目标是判断创意是否成立，应优先使用 `game-concept-architect`。如果用户同时要求产出策划案，本 skill 应作为第二步，在 `game-concept-architect` 输出后接续成案。

如果用户给的是录屏、PV、截图或试玩反馈，并希望诊断体验问题，应优先使用 `game-experience-analyzer`。

如果用户要的是首局节奏、反馈、具身感、氛围、认知负荷、留存或一周 A/B 实验，应优先使用 `game-experience-density-optimizer`。

如果用户只是要宣传文案、商店页短描述、众筹页面、PR 文案或广告脚本，本 skill 可以给文档中的定位和承诺，但不应替代专门的 marketing copywriting。

## 项目内上游产物审核门

写案前先做一次项目内协作自检，但不要把本 skill 退化成泛品类设计回答。本 skill 只负责把项目内其他 skill 或用户已有材料收束成评审文档，不继承项目外的全局设计总师口径。

- `primary_category`：先判断主品类/副品类、平台、商业模型和项目阶段。
- `core_player_action`：先看玩家反复做什么，再看题材、系统和文案。
- `anti_pollution`：商业案、独游案、Steam pitch、手游立项、Demo 文档不要互相套模板。
- `proof_of_play`：对外 pitch 必须说明 playable build、gameplay video、demo、vertical slice、玩家反馈或指标的状态。
- `scope_feasibility`：所有系统、内容、预算和里程碑都必须受团队能力约束。
- `negative_example`：至少写一个看似相似但不应采用/不应投递的反例。

如果用户的真实需求还停留在一句话创意、媒体样本诊断或体验浓度实验，应先交给项目内对应 skill 形成稳定上游产物，再由本 skill 负责整理成评审文档：

- `game-concept-architect`：输出 concept brief、player-promise-contract、core loop、scope gate 和 validation plan。
- `game-experience-analyzer`：输出 evidence-index、issue-card、sample boundary 和体验诊断。
- `game-experience-density-optimizer`：输出 ED handoff、一周实验、埋点字段、决策规则和 rollback 条件。
- `game-design-source-curator`：输出 source notes、reference boundary 和可追溯知识条目。

## 三类新增触发流程

### 一句话创意 -> 自动概念架构 -> 策划案

当输入只有一句话创意但目标是策划案时，按两段式执行：

1. 先用 `game-concept-architect` 生成 concept brief、player-promise-contract、core loop、scope gate、validation plan。
2. 再用本 skill 选择输出模式，生成商业策划案、独游设计案、一页 memo、pitch outline 或 vertical slice 文档。
3. 在 `Source Artifact Inventory` 里标注 `generated_this_turn_by_game-concept-architect`，不要伪装成用户已提供证据。

### 脑图 / xmind / 系统设计图 -> 可落地策划案

当用户给出 xmind、脑图截图、OPML、Markdown 大纲、Word/Excel 导出、玩法系统表或系统设计结构图时，先读取 `references/mindmap-and-existing-proposal-input.zh-CN.md`：

- 保留脑图层级，不要把节点直接散文化。
- 识别核心循环、系统模块、资源流、玩家行为、产出/消耗、成长线、内容范围、未决问题和冲突节点。
- 把“想法树”改成“制作树”：MVP、Vertical Slice、Demo、Release、Post-launch、Cut。
- 输出可落地策划案时必须补 owner、里程碑、验证标准和砍项理由。

### 审核 / 改进已有策划案

当用户给出已有策划案、GDD、pitch、立项文档或 vertical slice 文档并要求审核、重写、改进、压缩、变正式时：

- 先输出 `proposal review`，指出缺失、过度承诺、scope 风险、证据伪装、读者不匹配、无法执行的里程碑。
- 再输出 `revision plan`，说明保留什么、重写什么、删除什么、需要补什么证据。
- 用户要求直接改时，给出改写版，并保留 `Change Log` 和 `Remaining Unknowns`。

## 强制顺序

在写任何完整策划案前，必须按下面顺序完成。用户要求短稿时可以压缩，但不要跳过边界、证据、scope 和决策门。

1. `proposal intake`：确认文档受众、使用场景、输出模式、平台、商业模式、项目阶段和材料来源。
2. `source artifact inventory`：列出已有材料，例如 concept brief、player-promise-contract、validation plan、evidence-index、issue-card、ed-handoff、market/source notes、production profile。
3. `case visibility`：记录可见性、输出去向和是否需要脱敏。它只用于输出管理，不限制用户在本地环境处理真实项目。
4. `document purpose`：明确这份文档要推动什么决策，而不是只追求完整。
5. `evidence and assumption boundary`：把事实、引用、用户提供信息、模型推断、assumption 和 unknown 分开。
6. `proposal mode selection`：选择商业游戏策划案、独游设计案、一页决策 memo、发行 pitch outline 或 vertical slice design doc。
7. `proposal spine`：先写一句话定位、玩家承诺、核心循环、目标玩家、平台/商业假设和差异化边界。
8. `scope and production gate`：区分 MVP、Vertical Slice、Demo/公开试玩、Release、Post-launch、暂不开发和建议砍掉。
9. `risk and validation narrative`：写清最大风险、验证动作、通过/失败标准、下一步投入条件。
10. `document assembly`：再按选定模板写成正式文档。
11. `quality gate`：检查是否可评审、可执行、可删减、可验证，且没有把未知写成确定事实。

## 默认工作流

1. 读取 `templates/proposal-intake.md`，建立输入边界。若用户没有提供足够材料，不要停下；先产出 assumption draft，并最多提出 3 个会改变文档方向的问题。
2. 读取 `references/proposal-intake-router.zh-CN.md`，判断输出模式。
3. 如果用户给出上游产物，先抽取可复用 contract：玩家承诺、核心循环、验证计划、证据索引、问题卡、ED 实验、scope gate。不要改写成无法追溯的散文。
4. 如果用户给的是脑图/xmind/OPML/Markdown 大纲/系统图/已有策划案，读取 `references/mindmap-and-existing-proposal-input.zh-CN.md`，先做结构提取或 review，再成案。
5. 读取 `references/evidence-assumption-boundary.zh-CN.md`，把每个关键判断标成 `provided`、`derived`、`external_evidence`、`assumption`、`unknown` 或 `needs_research`。
6. 读取 `references/commercial-game-proposal-framework.zh-CN.md` 或 `references/indie-design-dossier-framework.zh-CN.md`，根据文档目标建立章节结构。
7. 读取 `references/audience-business-scope-gate.zh-CN.md`，检查目标玩家、平台、商业模式和 scope 是否互相支持。
8. 当任务涉及发行、投资、平台、Steam、孵化器、pitch deck、store page 或外部提交时，读取 `references/publisher-platform-proof-gate.zh-CN.md`，补齐 proof of play、publisher/platform fit、ask、budget、timeline 和 recheck gate。
9. 读取 `references/scope-and-milestone-gates.zh-CN.md`，输出里程碑和下一步投入条件。
10. 读取 `references/pitch-document-quality-gate.zh-CN.md`，执行最终文档门。
11. 按任务选择模板：
   - `templates/commercial-game-proposal.md`
   - `templates/indie-design-dossier.md`
   - `templates/one-page-decision-memo.md`
   - `templates/publisher-pitch-outline.md`
   - `templates/vertical-slice-design-doc.md`
   - `templates/proposal-evidence-ledger.md`
   - `templates/milestone-gate-plan.md`
   - `templates/risk-register.md`
   - `templates/existing-proposal-review.md`

## 输出模式

| 模式 | 默认触发 | 交付重点 |
| --- | --- | --- |
| `commercial_product_proposal` | 商业游戏、手游、网游、小游戏、F2P、内部立项、老板评审 | 产品定位、目标玩家、核心体验、系统与商业闭环、平台渠道、制作成本、指标、风险和立项决策 |
| `indie_design_dossier` | 独立游戏、Steam、主机/PC 买断、solo/small team、发行 pitch | 创作命题、玩家幻想、可卖点、最小内容策略、vertical slice、制作边界、社区/发行验证和风险 |
| `one_page_decision_memo` | 用户要求快速判断、老板只看一页、会前材料 | 结论、为什么值得看、最大风险、最小验证、需要什么决策 |
| `publisher_pitch_outline` | 发行、投资、合作方、比赛/孵化器 | 可被外部人快速理解的 pitch 结构、卖点证明、demo 计划、团队可信度和请求 |
| `vertical_slice_design_doc` | Demo、first playable、vertical slice、下一阶段制作 | 切片目标、功能边界、体验路径、资产/系统清单、里程碑、测试和 Go/No-Go |
| `proposal_review_and_rewrite` | 审核/改进已有策划案、GDD、pitch、立项文档 | 问题诊断、证据/范围/读者/执行性修正、改写计划、可选改写版 |

如果用户说商业游戏策划案，默认使用 `commercial_product_proposal`。如果用户说独游设计案，默认使用 `indie_design_dossier`。如果用户说只要一页或先给老板看，默认使用 `one_page_decision_memo`。如果用户说给发行或投资人看，默认使用 `publisher_pitch_outline`。如果用户说做 demo 或 vertical slice，默认使用 `vertical_slice_design_doc`。

如果用户说“审核/改进/重写已有策划案/GDD/pitch”，默认使用 `proposal_review_and_rewrite`，除非用户明确只要最终改写版。

## Case Visibility

`case_visibility` 只帮助 agent 管理输出边界，不限制用户在本地环境处理真实、私有或客户项目。

可选字段：

- `case_visibility`: `private_user_work` | `public_repo_example` | `public_article` | `client_confidential` | `synthetic_case` | `unknown`
- `output_destination`: `private_notes` | `repo_example` | `public_post` | `client_delivery` | `publisher_pitch` | `internal_review` | `unknown`
- `redaction_required`: `true` | `false` | `unknown`

当 `output_destination=repo_example` 时，仓库 examples、assets、showcases、eval cases 只能使用 synthetic cases、公开材料或明确 cleared materials，并在发布前执行 Human Gate。

## 证据规则

- 没有来源时，不要写成市场事实。
- 没有用户提供团队规模、周期、预算或技术能力时，不要承诺大型在线、开放世界、实时多人、长期 live ops、大量剧情分支或高精度资产量产。
- 没有当前平台、商店、发行、竞品、买量或政策证据时，只能写成 `assumption` 或 `needs_research`。
- 发行方、投资方、孵化器和平台规则会变化；真实投递前必须重新检查目标页面，状态写成 `verified_current`、`needs_recheck` 或 `unknown`。
- 对外 pitch 不能只靠概念图、设定或 AI 视觉稿。没有 playable build、gameplay video、demo、vertical slice、玩家反馈或指标时，必须把 proof 写成 `missing`。
- 外部调研不是固定动作。只有当调研结果会改变定位、目标玩家、平台/商业模型、scope gate、风险等级或 Go/No-Go 时，才建议执行。
- 文档可以有愿景，但愿景必须和可验证路径分开。
- 参考游戏只能作为行为结构、受众动机、体验节奏或生产边界的参照；不要复制设定、术语、阵营、剧情、关卡或商业表达。
- 脑图、xmind 和系统图只说明“结构关系”，不自动等于已验证设计。节点必须转成玩家行为、系统责任、scope、风险和验证项。

## 商业游戏策划案硬规则

商业游戏策划案必须让评审者知道三件事：为什么值得做、做成什么算成立、下一步要花多少钱或多少人力去验证。

- 受众不能只写年龄、性别或泛二次元/泛休闲；必须写玩家行为、动机、付出意愿、拒绝点和相邻产品。
- 商业模式不能先行吞掉核心体验；广告、IAP、订阅、买断、赛季、付费皮肤、UGC 或 LiveOps 都要说明和玩家承诺的关系。
- 系统列表必须回连核心循环，不允许堆功能名。
- 指标不能只写 DAU、留存、收入；必须说明这些指标如何验证玩家承诺、循环强度或商业假设。
- 立项建议必须包含最大风险、最小验证、通过标准、失败标准和下一步投入条件。

## 独游设计案硬规则

独游设计案必须保护创作锋利度和制作边界。不要把商业游戏的全系统模板套进小团队项目。

- 先写创作命题、玩家幻想、可卖点和玩法承诺，再写系统清单。
- 目标玩家要写成细分动机和拒绝点，例如喜欢短局解谜中的顿悟、喜欢低压探索中的环境叙事、拒绝刷数值或强操作压力。
- 内容策略必须说明少量资产如何产生足够变化，而不是承诺大量关卡、剧情、角色或区域。
- 美术和音频方向要写 production boundary：哪些风格可以用小团队做，哪些会拖垮。
- Demo/Vertical Slice 要证明最独特的体验，而不是做一个正式版小切片。
- 发行、社区、愿望单、展会、众筹、媒体、创作者传播等内容必须标注为当前证据或待调研，不得写成确定机会。

## 最低合格输出

`commercial_product_proposal` 至少包含：

```markdown
## Case Visibility
## Proposal Intake
## Source Artifact Inventory
## Executive Summary
## Product Positioning
## Target Player and Desire
## Player Promise
## Core Loop and Key Systems
## Platform and Business Fit
## Scope Gate
## Production Feasibility
## Milestone and Gate Plan
## Metrics and Validation Plan
## Risk Register
## Decision Request
## Evidence and Assumption Ledger
```

`indie_design_dossier` 至少包含：

```markdown
## Case Visibility
## Proposal Intake
## Source Artifact Inventory
## Creative Thesis
## Store-Page Promise
## Target Player and Niche
## Player Verbs and Core Loop
## Design Pillars
## Content Minimalism Strategy
## Art and Audio Direction Boundary
## Vertical Slice Plan
## Production Plan
## Release and Community Validation
## Risk Register
## Next Investment Decision
## Evidence and Assumption Ledger
```

`one_page_decision_memo` 至少包含：

```markdown
## Decision Memo
## Why This, Why Now
## Core Promise
## Biggest Assumptions
## Minimum Validation
## Scope and Cost Boundary
## Recommendation
## Decision Needed
```

`publisher_pitch_outline` 至少包含：

```markdown
## Pitch Goal
## One-Line Pitch
## Market/Reference Boundary
## Player Promise
## Proof of Play
## Publisher / Platform Fit
## Demo or Vertical Slice Plan
## Production Credibility
## Ask, Budget, and Timeline
## Risk and Validation
## Materials Checklist
## Recheck Before Submission
```

`vertical_slice_design_doc` 至少包含：

```markdown
## Slice Goal
## Experience Path
## Must-Prove Assumptions
## Build Scope
## Feature Priority
## Asset and Content Scope
## Milestones
## Playtest Protocol
## Go/No-Go Criteria
## Handoff Checklist
```

`proposal_review_and_rewrite` 至少包含：

```markdown
## Review Target
## Reader and Decision Fit
## Structure Diagnosis
## Evidence and Assumption Problems
## Scope and Production Risks
## Missing Proof / Missing Decisions
## Revision Plan
## Suggested Rewrite
## Change Log
## Remaining Unknowns
```

## 输入不足时的处理

如果缺失信息很多，不要直接停下。先写低置信度版本，并明确标注 `assumption` 和 `unknown`。只有当缺失信息会改变文档模式或关键判断时，才提出澄清问题。最多问三个问题。

优先追问这些会改变文档方向的问题：

1. 文档受众是谁：内部老板、制作人、发行、投资人、团队成员，还是自己梳理？
2. 目标平台和商业模式是否已定？
3. 团队规模、周期、预算或当前项目阶段是什么？

如果用户要求继续，就带着明确假设往前推进。

## 输出门

最终输出前检查：

- 是否先写文档目标，再写章节内容。
- 如果输入是一句话创意，是否先形成 `game-concept-architect` 上游产物，再进入本 skill 成案。
- 如果输入是脑图/xmind/系统图，是否保留层级并转成可执行 scope、里程碑和验证项。
- 如果输入是已有策划案，是否先 review 再改写，而不是直接润色。
- 是否区分已提供事实、外部证据、推断、assumption、unknown 和 needs_research。
- 是否从玩家承诺和核心循环组织文档，而不是从功能清单堆起。
- 商业案是否说明目标玩家、商业模式、平台渠道、制作成本、指标和立项请求。
- 独游案是否保护创作命题、最小内容策略、制作边界和 demo 验证。
- 是否有 scope gate，而不是把所有想法都塞进正式版。
- 是否有里程碑、owner、成功标准、失败标准和下一步投入条件。
- 是否说明最大风险和最小验证。
- 是否避免没有证据的市场断言、收入承诺、愿望单承诺或买量判断。
- 对外 pitch 是否说明发行方/平台匹配、proof of play、ask、budget、timeline 和投递前重新检查项。
- 是否能被目标读者在 5 分钟内理解项目为什么值得继续看。
