---
name: game-experience-density-optimizer
description: Use when turning game retention, single-player total-playtime, premium-game completion, mobile daily-retention, first-session pacing, prototype feel, optimal-stimulation/OLSO, boredom from under-stimulation or over-stimulation, habituation, novelty, feedback, embodiment, atmosphere, cognitive-load, FEP/free-energy, prediction-error, Markov-blanket, controllable-surprise, or live-engagement problems into rollback-ready ED (Experience Density, 体验浓度) experiments with instrumentation and metric-horizon-specific decision rules.
metadata:
  short-description: Design weekly ED experiments for experience density
---

# Game Experience Density Optimizer

Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 什么时候使用

当用户想讨论或提升游戏的体验浓度、留存、单机总游戏时长、买断制完成率、Demo 完成率、章节推进、首局体验、前 10 分钟节奏、教程清晰度、局内上头感、中段疲劳、回流体验、手游 D1/D3/D7 留存、每日活跃、持续天数、交互反馈、预测-反馈循环、具身感、氛围感、认知负荷、A/B 测试方案、埋点字典、数据看板、会话时长、首个有效选择时间、反馈强度、功能暴露节奏或小版本验证时，使用这个 skill。

以下请求要强触发：

- “体验浓度”
- “ED / Experience Density”
- “每分钟有多少事情发生”
- “有意义选择频率”
- “反馈不够爽/不够清楚”
- “操控不跟手/不够具身”
- “氛围感不足”
- “认知负荷太高”
- “自由能 / FEP”
- “最佳刺激 / OLSO / Optimal Level of Stimulation”
- “刺激太低 / 刺激太高”
- “低刺激无聊 / 过载无聊”
- “半熟半新”
- “习惯化 / 反习惯化”
- “预测误差”
- “可控惊讶”
- “马尔可夫毯 / Markov blanket”
- “玩家和游戏的输入输出边界”
- “先判窗口，再降噪，再提质，后调频”
- “首局/新手期节奏”
- “一周 A/B 测试”
- “用小成本改体验”
- “埋点字典”
- “看板字段”
- “D1/D7 怎么验证”
- “单机总游戏时长”
- “买断制 / premium game”
- “Demo 完成率 / 通关率”
- “手游日留存 / 每日活跃 / 持续天数”
- “首个爆点太晚”
- “中段疲劳”
- “做三组可发布改动”
- “给我留存实验方案”

这个 skill 的任务不是写一个大版本方案，也不是把节奏简单加快。它要把体验浓度问题压缩成一周能跑完的小实验，让设计判断变成可上线、可埋点、可复盘、可回滚的改动包。

## 独特用途

这个 skill 值得单独存在，是因为它解决的是一个常见断层：团队能感觉“体验淡、爽不起来、太累、不上头”，但不知道本周到底改哪一个旋钮、看什么指标、如何避免改完无法归因。

它不是通用游戏策划 skill，也不是留存报表 skill，而是一个“最佳刺激窗口诊断 + 体验实验编译器”：

```text
主观体验问题 -> 玩家/情境边界 -> 最佳刺激窗口 -> 公式项诊断 -> 指标周期门 -> 一个主旋钮 -> 可上线变体 -> 埋点/看板 -> 预注册决策
```

与相邻 skill 的边界：

- `game-experience-analyzer` 负责从录屏、截图、PV、试玩样本建立证据层；本 skill 负责把证据转成可上线实验。
- `game-concept-architect` 负责从创意建立核心循环和设计蓝图；本 skill 只在已有原型、Demo、线上版本或明确体验问题时使用。
- 普通数据分析负责解释指标变化；本 skill 先规定哪些指标适用于当前游戏形态，并把指标绑定到具体体验改动。
- OLSO、FEP、GameFlow、SDT 在这里不是理论展示，而是防止错误优化的诊断门：不把更密当更好，不把过载无聊误判成刺激不足，不把 D1/D7 套给单机，不把随机当新颖，不把数字成长当真实成长。

## 概念边界

中文统一叫“体验浓度”。英文保留 `ED` / `Experience Density`，但不要在中文解释里把核心概念写成另一个名称。

体验浓度指：在游戏进行过程中，每单位时间内玩家所经历的有意义互动和可感知反馈的密集程度。它关注游戏体验的浓缩水平：每分钟有多少有意义的选择、多少新反馈、多少能被玩家理解和归因的体验信号。

从最佳刺激水平模型（OLSO）的设计隐喻看，体验浓度更完整的定义是：当前玩家在当前情境下，单位时间内可吸收、可解释、可转化为探索/学习/意义的刺激密度。这里的“当前玩家”和“当前情境”是核心。相同刺激对新手可能过载，对老手可能钝化；同样的 3A 复杂度，可能让轻度玩家看不懂，也可能让核心玩家觉得没新东西。

因此，体验浓度诊断必须先判断 `optimal_stimulation_fit`：玩家是低刺激无聊、过载无聊、习惯化、低能动性还是低意义感。只有确定刺激窗口后，才进入 ED 公式项。

从自由能原理的设计隐喻看，体验浓度也可以写成：单位时间内玩家可承受预测误差的密度。游戏是可控惊讶发生器：让玩家在可理解、可操作、可复盘、可成长的边界内预测、行动、遭遇误差、更新模型。太低会淡，太高会炸，刚好会沉浸。

从马尔可夫毯的设计隐喻看，玩家和游戏之间的输入输出接口就是体验边界。UI、音效、震动、镜头、打击反馈、敌人动作、地图信息属于感官状态；按键、摇杆、Build 选择、资源分配、路径选择、社交指令属于行动状态。好的手感，是低延迟、低噪声、高解释性的玩家-游戏边界。

这个概念来自设计观察和方法论假设，不是经过科学验证的心理学量表。可以借用自由能原理、马尔可夫毯、预测处理、受控幻觉、具身感和注意力调动作为启发式镜头，但输出时必须标注为 `theory_status: design_hypothesis`，不能包装成科学结论。

高浓度不是绝对好，低浓度也不是绝对差。关键是设计意图、玩家偏好和浓度曲线是否匹配。恐怖、探索、叙事、模拟经营或禅意游戏可以低水平频率、高氛围纵深；割草、动作、短局竞技或短视频式买量素材可能需要更高频的选择与反馈。

## 工作公式

体验浓度的默认工作公式：

```text
ED = MD/min * (SF + EB + AR) / CLP
```

其中：

- `MD/min`：Meaningful Decisions per minute，每分钟有意义选择次数。
- `SF`：Salient Feedback，可被玩家感知并归因的反馈。
- `EB`：Embodiment Bonus，操控、镜头、角色和物理一致性带来的具身感加成。
- `AR`：Atmospheric Richness，音乐、环境、美术、光影、UI 风格一致性带来的氛围感加成。
- `CLP`：Cognitive Load Penalty，学习成本、信息噪音、UI 混乱、打断感带来的认知负荷惩罚。

这个公式主要用于同一游戏、同一阶段、同一用户群体内的相对比较。不要用它跨品类机械打分。

公式不是第一步。先用 `optimal_stimulation_fit` 判断刺激窗口，再用公式把问题落到可改旋钮。否则容易把“过载导致的无聊”误修成“再加事件”。

## 指标周期门

在任何指标、看板或成功门之前，必须先判断 `game_metric_model`：

- `premium_single_player`：买断制、单机、主线体验、Demo、章节制或以完整旅程为价值承诺的游戏。P1 默认看总游戏时长、主线/章节推进、Demo 完成率、通关率、关键节点到达率、重玩意愿或评价风险。不要默认把 D1/D7 当主指标。
- `mobile_liveops`：手游、长期运营、活动、日常循环、持续登录和回流节奏。P1 可以看 D1/D3/D7/D30、每日会话、连续活跃、活动留存和回流成功率。
- `hybrid`：既有完整旅程又有长期运营或赛季结构。必须把总旅程指标和日留存指标拆开，不要混成一个胜利标准。
- `unknown`：证据不足时先标 unknown，并写明哪些指标暂不适用。除非材料明确是手游/liveops，不要主动承诺 D1/D7 提升。

## 默认诊断顺序

必须按“先判窗口，再降噪，再提质，后调频”处理：

0. 先判断最佳刺激窗口：玩家是 `too_low`、`optimal`、`too_high`、`uneven` 还是 `unknown`。无聊可能来自刺激不足，也可能来自过载、习惯化、低能动性或低意义感。先读 `references/optimal-stimulation-window.zh-CN.md`。
0.5 再判断自由能区间：玩家是无聊、沉浸还是崩溃。FEP/PP 用于解释预测误差是否可消化、是否能被玩家更快降低，而不是替代 OLSO 的刺激窗口判断。
1. 先看 `CLP`：玩家是否看不懂、学不会、无法归因、被 UI/特效/弹窗/术语打断。CLP 是分母，没降下来之前不要加事件。
2. 再看 `SF / EB / AR`：反馈是否显著、操控是否人机一体、音画氛围是否自洽。这里决定瞬时体验的纵向质量。
3. 再看马尔可夫毯耦合：玩家行动是否能有效影响世界，世界变化是否能准确返回给玩家。手感和反馈问题要落到延迟、噪声、解释性和能动性。
4. 最后看 `MD/min`：玩家是否有足够频率的有意义选择。只有在信息清晰、反馈有质感后，调频才有意义。

不要把“更多事件”“更多奖励”“更多红点”“更长在线”直接等同于体验浓度提升。

## 默认流程

1. 判断 `game_metric_model` 和 `metric_horizon`：读取 `references/metric-horizon-by-game-model.zh-CN.md`，先区分单机/买断制、手游/liveops、hybrid 或 unknown。
2. 判断输入类型：`gameplay_recording`、`prototype_build`、`telemetry_snapshot`、`design_doc`、`liveops_problem`、`store_demo_feedback`、`text_only_request`。如果用户只给一段描述，不要追问一串问题，先输出 `unknown` 字段和可执行的假设版实验。
3. 建立边界：读取 `templates/experiment-intake.md`，输出 `case_boundary`、`metric_horizon`、`available_evidence`、`unsupported_claims`、`key_unknowns`、`theory_status`。没有真实数据时只能设计验证方案，不能声称一定提升留存或总时长。
4. 读取 `references/optimal-stimulation-window.zh-CN.md`，输出 `optimal_stimulation_fit`。先区分低刺激无聊、过载无聊、习惯化、低能动性和低意义感。
5. 读取 `references/ed-framework.zh-CN.md` 和 `references/density-formula.zh-CN.md`，把当前问题定位到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
6. 读取 `references/density-diagnosis-workflow.zh-CN.md`，按“先判窗口，再降噪，再提质，后调频”输出诊断顺序。
7. 读取 `references/free-energy-markov-blanket-lens.zh-CN.md`，输出 `free_energy_window` 和 `markov_blanket_coupling`。只作为设计启发式使用，不要写成神经科学结论。
8. 读取 `references/flow-sdt-experience-gates.zh-CN.md`，用 GameFlow 与 SDT 做交叉检查：清晰目标、反馈、控制、挑战/技能匹配，以及自主、胜任、关系、最佳新颖性是否被支持。
9. 读取 `references/interaction-prediction-lens.zh-CN.md`，只在需要解释交互优势、预测-反馈循环、具身幻觉和注意力调动时使用；不要过度科学化。
10. 读取 `references/lever-playbook.zh-CN.md`，把问题映射到一个主旋钮。每个实验变体只能有一个主旋钮，最多一个不影响归因的辅助动作。
11. 选择实验模式：`first_session_activation`、`mid_session_fatigue`、`return_session_rehook`、`embodiment_feedback`、`atmosphere_pacing`、`liveops_micro_tuning`、`single_player_journey_quality`、`demo_completion_quality`。
12. 设计实验：默认输出 A/B/C/D 四组。A 是对照组，B 优先降 CLP 或增加熟悉锚点，C 提升 SF/EB/AR 的纵向质量，D 在窗口允许时调整 MD/min 或半熟半新的有效选择。用户要求极小范围时，只输出 A/B。
13. 如果问题涉及长线、后期疲劳、赛季、刷子、肉鸽、UGC 或老玩家钝化，输出 `anti_habituation_plan`，不要只写“加新内容”。
14. 读取 `references/weekly-experiment-sop.zh-CN.md`，把方案压成一周节奏。单机/买断制用一周 playtest 或 Demo 分支验证；手游/liveops 用一周灰度或活动窗口验证。
15. 读取 `references/telemetry-metric-dictionary.zh-CN.md`，生成埋点字典。必须至少包含 `variant_assigned`、`session_started`、`meaningful_decision_made`、`salient_feedback_fired`、`cognitive_load_signal`、`session_checkpoint`、`session_ended`。
16. 读取 `references/retention-risk-gates.zh-CN.md`，提前写死成功、观察、回滚和 Kill 条件。不要事后看数据再改胜利标准。
17. 按交付深度选择模板：快速方案用 `templates/variant-matrix.md`，标准方案用 `templates/weekly-ed-experiment-plan.md`，数据接线用 `templates/instrumentation-dictionary.md`，看板需求用 `templates/dashboard-spec.md`，复盘用 `templates/weekly-review.md`。
18. 最后执行输出门检查。

## 输入边界

### 只有描述 `text_only_request`

可以输出假设版实验，但要标注 `evidence_status: assumption_only` 和 `theory_status: design_hypothesis`。建议必须写成低成本、可回滚、不会破坏经济和主线的改动。

### 有录屏或截图 `gameplay_recording` / `screenshots`

优先让 `game-experience-analyzer` 建立证据层，再把时间轴和问题卡转换成 ED 实验。不要把静态截图直接当成真实节奏证据。
当 GEA 已输出 `ed-handoff` 时，优先消费其中的 `issue_cards_for_ed`、`evidence_refs`、`suggested_primary_lever`、`secondary_noise`、`confounder_risk` 和 `unknowns`；不要重新做一遍完整体验分析。

### 有数据 `telemetry_snapshot`

可以设计更具体的指标和分流规则。若数据口径不明，先生成字段核对表，不能把不同版本、不同渠道或不同新老用户混在一起得出结论。

### 有线上版本 `liveops_problem`

必须保留风险门：经济安全、难度安全、新手/老玩家分层、付费影响、公平性、公告/热更窗口。这个 skill 不设计暗黑模式，不用误导、焦虑、强迫红点或损失厌恶去抬指标。

## 输出结构

标准输出必须包含：

1. `case_boundary`：材料来源、版本、平台、用户阶段、已有数据和未知项。
2. `metric_horizon`：写清 `game_metric_model`、`primary_time_horizon`、P1 指标族和不适用指标。
3. `theory_status`：默认 `design_hypothesis`，说明该方法是设计启发式而非科学量表。
4. `optimal_stimulation_fit`：写清最佳刺激窗口、无聊类型、玩家资源画像、刺激画像、情境刺激和设计方向。
5. `diagnosis_summary`：当前问题主要落在 `CLP`、`SF`、`EB`、`AR`、`MD/min` 哪一项，并说明它和最佳刺激窗口的关系。
6. `density_curve_intent`：当前段落意图是高压、建立规则、放松观察、情绪沉淀、决策规划还是爽感释放。
7. `free_energy_window`：当前自由能区间是 `too_low`、`optimal`、`too_high` 还是 `unknown`，写清预测误差来源、玩家承受理由和干预方向。
8. `markov_blanket_coupling`：写清感官状态、行动状态、耦合断点、延迟/噪声/解释性/能动性问题和修复动作。
9. `growth_surprise_ladder`：当问题涉及成长、疲劳、后期钝化、Boss、肉鸽、策略或探索时，写清玩家当前能处理哪一阶惊讶，下一阶惊讶如何可学习、可行动、可复盘。
10. `anti_habituation_plan`：当问题涉及长线、老玩家钝化、赛季、刷子、肉鸽、UGC 或内容被玩透时，写清反习惯化旋钮，而不是只说“加新内容”。
11. `motivation_flow_gate`：检查清晰目标、即时反馈、控制感、挑战/技能匹配、自主、胜任、关系和最佳新颖性支持，避免只提高刺激或指标。
12. `experiment_hypothesis`：一句话假设，写清玩家行为、设计改动、目标指标。
13. `variant_matrix`：A/B/C/D 组，写清主旋钮、最佳刺激目标、具体改动、影响窗口、owner、上线风险。
14. `instrumentation_dictionary`：事件名、触发时机、字段、示例值、用途、隐私边界。
15. `metric_plan`：P1、P2、负向指标、分群、观察周期、最小样本提醒。
16. `dashboard_spec`：看板字段、图表、过滤器、每日检查项。
17. `decision_rules`：成功、放大、继续观察、回滚和 Kill 条件。
18. `weekly_schedule`：一周执行节奏。
19. `handoff_checklist`：策划、客户端、关卡/叙事、美术/音频、数据、QA 的交接清单。

## 证据与数据规则

- 没有真实埋点时，不要承诺 D1/D7 会提升，只能写验证假设。
- 单机/买断制不默认关注每天和持续天数，优先看总游戏时长、完成率、章节推进、Demo 完成率、重玩意愿和评价风险。
- 手游/liveops 才默认关注 D1/D3/D7/D30、每日会话、连续活跃、活动周期和回流。
- 不把无聊自动解释为刺激不足；过载、习惯化、低能动性和低意义感也会表现为无聊。
- 不把新颖自动解释为正向；有效新颖必须是半熟半新、可归因、可学习、可行动、可复盘。
- 不把会话时长上升自动等同于体验变好；必须同时看退出点、失败率、重复行为和负反馈。
- 不把更多事件等同于更高 ED；有效事件必须能被玩家理解，并改变状态、目标、选择或情绪。
- 有意义选择不是选项数量。弱选择要合并，少而重优先。
- 反馈增强不是光污染。视觉、听觉、触觉、镜头和 UI 应同频共振，传递同一核心信息。
- 具身感不是剧情代入。重点看输入响应、动作节拍、命中停顿、镜头、触觉和物理一致性。
- 氛围感不是堆美术资源。重点看风格一致性和留白时的质感。
- 叙事压缩不是删除剧情。优先压停顿、重复解释、不可交互文本和延迟反馈。
- 新手、回流、老玩家要分群；不同渠道和版本要分开。
- 不得使用 dark pattern，包括强迫红点、误导奖励、虚假倒计时、付费焦虑和不可逆损失伪装。
- 所有成功标准必须在实验前写死。

## 按需读取

- ED 基础框架：`references/ed-framework.zh-CN.md`
- 理论来源映射：`references/theory-source-map.zh-CN.md`
- 单机/手游指标周期门：`references/metric-horizon-by-game-model.zh-CN.md`
- 最佳刺激窗口：`references/optimal-stimulation-window.zh-CN.md`
- GameFlow 与 SDT 体验门：`references/flow-sdt-experience-gates.zh-CN.md`
- 体验浓度公式：`references/density-formula.zh-CN.md`
- 诊断流程：`references/density-diagnosis-workflow.zh-CN.md`
- 自由能与马尔可夫毯镜头：`references/free-energy-markov-blanket-lens.zh-CN.md`
- 交互与预测反馈镜头：`references/interaction-prediction-lens.zh-CN.md`
- 一周实验 SOP：`references/weekly-experiment-sop.zh-CN.md`
- 公式旋钮玩法库：`references/lever-playbook.zh-CN.md`
- 埋点与指标口径：`references/telemetry-metric-dictionary.zh-CN.md`
- 风险门和反例：`references/retention-risk-gates.zh-CN.md`
- 输入表：`templates/experiment-intake.md`
- 标准实验方案：`templates/weekly-ed-experiment-plan.md`
- 变体矩阵：`templates/variant-matrix.md`
- GEA 到 ED 的交接模板：`../game-experience-analyzer/templates/ed-handoff.md`
- 埋点字典：`templates/instrumentation-dictionary.md`
- 看板规格：`templates/dashboard-spec.md`
- 周复盘：`templates/weekly-review.md`
- 结构化 schema：`templates/experiment-plan.schema.json`
- 可选验证提示：`evals/evals.json`、`evals/rubric.yaml`、`evals/negative_cases.md`
- 示例：`examples/synthetic-survivors-first-session-ed-plan.md`

## 输出门

最终输出前检查：

- 是否先写边界，再写判断。
- 是否先区分 `premium_single_player`、`mobile_liveops`、`hybrid` 或 `unknown`。
- 是否为单机/买断制使用总旅程指标，为手游/liveops 使用每日和持续天数指标。
- 是否标注 `theory_status: design_hypothesis`。
- 是否先输出 `optimal_stimulation_fit`，区分低刺激无聊、过载无聊、习惯化、低能动性或低意义感。
- 是否把体验浓度问题落到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
- 是否输出 `free_energy_window`，并避免把 FEP 写成未经验证的科学断言。
- 是否输出 `markov_blanket_coupling`，并把手感/反馈问题落到感官状态、行动状态和耦合质量。
- 是否输出 `motivation_flow_gate`，避免只加刺激、密度或指标而破坏自主、胜任、关系、最佳新颖性、目标清晰和控制感。
- 是否遵守“先判窗口，再降噪，再提质，后调频”。
- 如果涉及后期疲劳、长线、赛季、刷子、肉鸽或老玩家钝化，是否输出 `anti_habituation_plan`。
- 是否区分水平频率、纵向质量和认知负荷。
- 是否每个变体只有一个主旋钮，避免一次改太多导致无法归因。
- 是否写清具体可上线改动，而不是抽象建议。
- 是否包含埋点事件、字段、触发时机和用途。
- 是否预注册成功标准、负向指标、回滚和 Kill 条件。
- 是否按新手、回流、老玩家或渠道分群。
- 是否避免暗黑模式和纯数值膨胀。
- 是否有一周执行节奏和 owner handoff。
