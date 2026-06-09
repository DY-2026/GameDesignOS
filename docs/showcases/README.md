# Showcase 路由报告

这个目录用来给新用户展示 `ParanoiaSkills` 的最小 proof path：每个 showcase 都必须说明输入材料、使用哪个项目内 skill、稳定输出是什么、不能声称什么，以及下一个 skill 如何消费它。

公开 showcase 只能使用 synthetic、public、explicitly cleared，或标记为 `needs_review` 的材料。真实项目、客户项目、未公开路线图、后台数据、收入数据和私有素材不要放进本公开仓库。

## 项目内协作链

本报告只描述本仓库内的 skill 协作关系，不接入外部或全局 design-master 类 skill。

```text
game-concept-architect
  -> player-promise-contract / validation-plan
  -> game-experience-analyzer
  -> evidence-index / issue-card / ed-handoff
  -> game-experience-density-optimizer
  -> weekly ED experiment / instrumentation / dashboard / decision rules
  -> game-design-proposal-writer
  -> proposal / pitch / decision memo / vertical-slice document
```

`paranoia-ai-system-evolver` 是元层，只在修改 skill、schema、eval、router、workflow、promotion 或 rollback 规则时介入。

`game-design-source-curator` 和 `game-design-book-translator` 是知识输入层；它们可以丰富 reference，但不替代概念架构、证据诊断、ED 实验或成案写作。

## 路由总表

| 用户手里的材料或意图 | 首选 skill | 稳定输出 | 不应该做什么 |
| --- | --- | --- | --- |
| 一句话创意、粗概念、还没有核心循环 | `$game-concept-architect` | `player-promise-contract`、`validation-plan` | 不直接写 GDD，不直接做 ED 实验 |
| 截图、录屏、PV、商店页、试玩样本 | `$game-experience-analyzer` | `evidence-index`、`issue-card`、`ed-handoff` | 不直接承诺留存、收入或真实手感结论 |
| 留存、首局节奏、反馈、具身感、氛围、认知负荷、Demo 完成、回流、习惯化 | `$game-experience-density-optimizer` | 一周 ED 实验、埋点字典、看板字段、决策规则 | 不重复媒体证据分析，不把无聊自动等同于刺激不足 |
| 已有概念、证据、ED 实验、source notes 或生产约束，需要正式文档 | `$game-design-proposal-writer` | 商业策划案、独游设计案、pitch、decision memo、vertical slice doc | 不替代上游诊断或实验设计 |
| 要改 skill、router、schema、eval、workflow | `$paranoia-ai-system-evolver` | evolution proposal、OODA/VOI state、eval plan | 不静默提升候选规则为长期规则 |
| 要沉淀文章、视频、作者、资料 | `$game-design-source-curator` | source notes、reference boundary、知识条目 | 不替代具体项目方案 |
| 要翻译/润色游戏设计书或长文 | `$game-design-book-translator` | 中文译文、术语表、章节包 | 不作为 ED 实验运行入口 |

## Showcase 1：Game Experience Analyzer

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 需要从 PV、录屏、截图或视频链接中获得证据化体验诊断的设计师、制作人、独立团队和 agent 用户。 |
| 输入材料 | PV、trailer、gameplay recording、screenshot set、video link。 |
| 使用 skill | `$game-experience-analyzer` |
| 输出 artifact | 带样本边界、证据索引、诊断路径、issue cards 和验证建议的体验报告。 |
| 证明什么 | 媒体样本可以变成可复查诊断，但不假装知道留存、收入或私有遥测。 |
| 示例 | [Survival 33 Days gameplay experience report](../../game-experience-analyzer/examples/survival-33-days-gameplay-experience-report.md) |

### 通过门

- 必须有 `sample_boundary`。
- 必须把判断连到证据、时间戳、截图区域或材料来源。
- 必须列出 `unsupported_claims`。
- 若要进入 ED 实验，输出 `ed-handoff` 或可转成 `ed-handoff` 的 issue cards。

## Showcase 2：Game Concept Architect

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 想把一句话创意或 rough concept seed 变成可验证概念计划的开发者、设计师和 agent 用户。 |
| 输入材料 | One-line game idea、rough concept seed。 |
| 使用 skill | `$game-concept-architect` |
| 输出 artifact | concept seed、assumption ledger、player promise、core loop、scope gate、validation plan。 |
| 证明什么 | 一句话创意可以变成有边界的设计计划，而不是膨胀成 oversized GDD。 |
| 示例 | [Clockwork Garden Defense synthetic example](../../game-concept-architect/examples/clockwork-garden-defense.md) |

### 通过门

- 必须输出玩家承诺和验证计划。
- 必须说明 scope gate。
- 如果后续有原型或媒体样本，交给 `game-experience-analyzer` 做证据诊断。

## Showcase 3：Concept-To-Diagnosis Loop

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 希望从玩家承诺走到原型/媒体诊断，并保持同一证据契约的团队。 |
| 输入材料 | `player-promise-contract`、prototype recording、screenshot set、PV、synthetic test sample。 |
| 使用 skill | `$game-concept-architect` -> `$game-experience-analyzer` |
| 输出 artifact | 玩家承诺、prototype/media diagnosis、unsupported-claim list、next validation plan。 |
| 证明什么 | 同一个玩家承诺可以驱动概念架构，也可以驱动后续证据化诊断。 |
| 占位反馈 | [Concept-to-Diagnosis Loop feedback issue](https://github.com/DY-2026/ParanoiaSkills/issues/new?template=showcase_feedback.md&title=Concept-to-Diagnosis%20Loop%20showcase) |

### 通过门

- GCA 输出必须能被 GEA 读懂：玩家承诺、核心循环、假设、验证计划。
- GEA 不能把媒体诊断写成产品成功结论。
- 后续如果问题落在首局、反馈、认知负荷、留存或节奏，才进入 EDO。

## Showcase 4：Experience Density Experiment Compiler

这一段必须按新版体验浓度流程重写。旧写法的问题是把 ED showcase 写成“体验浓度报告”或“体验建议”，没有突出编译器的关键动作：先证据门，再模式路由，再指标周期，再一周实验。

新版定位：`game-experience-density-optimizer` 不是上游体验分析器，也不是通用策划案生成器。它只在已有明确体验问题、issue cards、`ed-handoff`、试玩笔记、遥测快照，或合成/文本假设边界清楚时，把问题编译成可验证实验。

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 需要把留存、首局节奏、反馈、具身感、氛围、认知负荷、Demo 完成率、回流或习惯化问题变成实验的设计师、制作人、数据分析和 agent 用户。 |
| 输入材料 | `ed-handoff`、issue cards、playtest notes、telemetry snapshot，或边界清楚的 synthetic/text-only experience problem。 |
| 使用 skill | `$game-experience-density-optimizer` |
| 第一步 | 输出 `output_mode`、`case_boundary`、`evidence_gate`。 |
| 输出 artifact | Weekly ED experiment：`CLP/SF/EB/AR/MD-min` 诊断、每个变体一个 primary lever、埋点字典、看板字段、预注册决策规则、rollback gates。 |
| 证明什么 | 模糊体验浓度问题可以变成一周内可上线、可埋点、可复盘、可回滚的实验，而不是未验证的留存承诺。 |
| 首局示例 | [Synthetic first-session ED plan](../../game-experience-density-optimizer/examples/synthetic-survivors-first-session-ed-plan.md) |
| 买断制 Demo 示例 | [Synthetic premium Demo ED plan](../../game-experience-density-optimizer/examples/synthetic-premium-demo-completion-ed-plan.md) |
| Hybrid 复盘示例 | [Synthetic hybrid conflict review](../../game-experience-density-optimizer/examples/synthetic-hybrid-conflict-review.md) |

### EDO 输入分流

| 输入情况 | `output_mode` | 处理方式 |
| --- | --- | --- |
| 只有一句体验问题 | `quick_ed_triage` | 输出 1 个边界、1 个刺激窗口、1 个主旋钮、2 个最小改动、3 个指标、1 个回滚条件 |
| 用户问本周怎么改、怎么测、A/B | `weekly_ab_plan` | 输出 A/B 或 A/B/C/D 变体、埋点、看板、决策门、owner、rollback |
| 用户只问埋点、看板、指标口径 | `instrumentation_plan` | 输出事件字典、字段、触发时机、过滤器、数据质量门、隐私边界 |
| 用户给实验结果或指标变化 | `review_and_decide` | 先查数据质量和负向门，再看 P1/P2，最后决定 amplify / iterate / observe / rollback / kill |
| 用户要客户交付或完整团队方案 | `full_client_delivery` | 展开完整 19 模块 |
| 用户要 agent/脚本消费 | `schema_json` | 按 `templates/experiment-plan.schema.json` 输出结构化 JSON |

### EDO 输出门

一个 ED showcase 只有满足这些条件，才算是新版流程：

- `evidence_gate`：声明 `L0_text_only` 到 `L5_ab_result`，并写清 allowed claims、forbidden claims、missing evidence、confounder risks。
- `metric_horizon`：先判断 `premium_single_player`、`mobile_liveops`、`hybrid` 或 `unknown`。
- `optimal_stimulation_fit`：无聊不能自动解释成刺激不足；必须考虑过载、习惯化、低能动性、低意义感。
- `diagnosis_summary`：问题必须落到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
- `variant_matrix`：每个变体只有一个 primary lever，并有 owner、QA、config 或 implementation surface、rollback。
- `instrumentation_dictionary`：事件和字段能把设计假设连到可复盘数据。
- `decision_rules`：成功、观察、迭代、回滚、Kill 条件必须预注册。
- `ethics_gate`：不能用暗黑模式、误导奖励、虚假倒计时、焦虑红点或纯数值膨胀。

### 什么时候不能直接进 EDO

| 情况 | 正确路由 |
| --- | --- |
| 只有一句游戏创意，还没玩家承诺和核心循环 | 先用 `$game-concept-architect` |
| 只有截图、PV、商店页或录屏，但还没有证据层 | 先用 `$game-experience-analyzer` |
| 目标是写商业策划案、pitch、vertical slice 文档 | 先产生 ED artifact，再用 `$game-design-proposal-writer` |
| 目标是修改 ED skill、schema、eval 或 router 本身 | 用 `$paranoia-ai-system-evolver` |

## Showcase 5：Analyzer-To-ED Loop

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 已有媒体诊断，想把 P0/P1 issue cards 转成一周实验的团队。 |
| 输入材料 | `$game-experience-analyzer` 输出的 `evidence-index`、`issue-card`、`ed-handoff`。 |
| 使用 skill | `$game-experience-analyzer` -> `$game-experience-density-optimizer` |
| 输出 artifact | 消费 `issue_cards_for_ed`、`evidence_refs`、`suggested_primary_lever`、`secondary_noise`、`confounder_risk`、`unknowns` 的 ED 实验。 |
| 证明什么 | EDO 不应该重做媒体诊断；它应该消费 handoff，把证据卡编译成可测试方案。 |
| contract | [ED handoff schema](../../contracts/ed-handoff.schema.json) |

### 推荐提示词

```text
Use $game-experience-density-optimizer to consume this ed-handoff and compile a weekly_ab_plan.
Do not redo the media diagnosis. Start with output_mode, case_boundary, evidence_gate, and metric_horizon.
Then produce variant_matrix, instrumentation_dictionary, dashboard_spec, decision_rules, weekly_schedule, and rollback gates.
```

## Showcase 6：Proposal Assembly

| 字段 | 内容 |
| --- | --- |
| 目标用户 | 需要把概念、证据、ED、source 和生产约束整合成正式决策文档的团队。 |
| 输入材料 | concept brief、player promise、validation plan、evidence index、issue cards、ED experiment、source notes、production constraints。 |
| 使用 skill | `$game-design-proposal-writer` |
| 输出 artifact | commercial product proposal、indie design dossier、one-page decision memo、publisher pitch outline、vertical-slice design doc。 |
| 证明什么 | 成案写作是稳定上游 artifact 之后的 assembly step，不替代概念架构、证据诊断或 ED 实验设计。 |
| 示例 | [Clockwork Garden commercial proposal](../../game-design-proposal-writer/examples/synthetic-clockwork-garden-commercial-proposal.md) |

## 维护规则

- 新增 showcase 时，先确认它属于哪条项目内协作链。
- 不要把外部/全局 skill 写进本仓库的协作图。
- 不要把 `candidate` router 规则写成已强制执行的生产规则。
- 新增真实案例前，先检查 public/private boundary。
- 每个 showcase 都要说明：输入、skill、输出 artifact、证明什么、不能声称什么、下一步谁消费。
