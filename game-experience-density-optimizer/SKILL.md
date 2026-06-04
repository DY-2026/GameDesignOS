---
name: game-experience-density-optimizer
description: Use when improving game retention, first-session pacing, prototype feel, onboarding density, or live game engagement through weekly EPM experiments that tune event frequency, decision weight, narrative compression, instrumentation, dashboards, and rollback-ready A/B test plans.
metadata:
  short-description: Design weekly EPM experiments for retention and pacing
---

# Game Experience Density Optimizer

Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 什么时候使用

当用户想提升游戏留存、首局体验、前 10 分钟节奏、教程密度、局内上头感、中段疲劳、回流体验、版本小改验证、A/B 测试方案、埋点字典、数据看板、D1/D3/D7 留存、会话时长、首个有效事件时间、功能暴露节奏、剧情压缩、决策重量或体验密度时，使用这个 skill。

以下中文请求要强触发：

- “提升留存”
- “体验密度”
- “EPM”
- “首局/新手期节奏”
- “一周 A/B 测试”
- “用小成本改体验”
- “事件频率怎么调”
- “决策权重怎么设计”
- “剧情/对白太拖，怎么压缩”
- “埋点字典”
- “看板字段”
- “D1/D7 怎么验证”
- “首个爆点太晚”
- “中段疲劳”
- “每分钟体验太空”
- “做三组可发布改动”
- “给我留存实验方案”

这个 skill 的任务不是直接写一个大版本方案，而是把体验问题压缩成一周能跑完的小实验。它要让设计建议变成可上线、可埋点、可复盘、可回滚的改动包。

## 核心判断

Experience per Minute，简称 EPM，指单位时间内玩家真正感受到的有效体验信号密度。它不是事件越多越好，而是有意义的反馈、选择、状态变化和情绪峰值，能否在正确节奏里出现。

默认把 EPM 拆成三个主旋钮：

1. `event_frequency`：玩家每分钟遇到多少可感知事件，包括战斗峰值、掉落、目标完成、临时增益、环境变化、微剧情、系统反馈。
2. `decision_weight`：玩家一次选择对接下来 30-120 秒的可见影响有多强，包括路线、Build、资源、风险、敌人形态、叙事态度。
3. `narrative_compression`：同样的信息、情绪和设定，能否用更短文本、更少停顿、更明确的镜头、音画和交互节拍交付。

辅助旋钮包括 `feedback_intensity`、`objective_chain`、`recovery_window`、`reward_clarity`、`failure_friction`。除非用户点名，不要一次打开太多旋钮。

## 默认流程

1. 先判断输入类型：`gameplay_recording`、`prototype_build`、`telemetry_snapshot`、`design_doc`、`liveops_problem`、`store_demo_feedback`、`text_only_request`。如果用户只给一段描述，不要追问一串问题，先输出 `unknown` 字段和可执行的假设版实验。
2. 建立边界：读取 `templates/experiment-intake.md`，输出 `case_boundary`、`available_evidence`、`unsupported_claims`、`key_unknowns`。没有真实数据时只能设计验证方案，不能声称一定提升留存。
3. 读取 `references/epm-framework.zh-CN.md`，先判断当前问题更像低密度、假密度、过载密度，还是反馈不可理解。
4. 读取 `references/lever-playbook.zh-CN.md`，把问题映射到 `event_frequency`、`decision_weight`、`narrative_compression` 三个主旋钮。每个实验变体只能有一个主旋钮，最多一个辅助旋钮。
5. 选择实验模式：`first_session_activation`、`mid_session_fatigue`、`return_session_rehook`、`build_formation`、`narrative_pacing`、`liveops_micro_tuning`。
6. 设计实验：默认输出 A/B/C/D 四组。A 是对照组，B 调事件频率，C 调决策权重，D 调叙事压缩。用户要求极小范围时，只输出 A/B。
7. 读取 `references/weekly-experiment-sop.zh-CN.md`，把方案压成一周节奏：周一冻结假设，周二上版，周三监控阻断项，周四小复查，周五到周日收样本，周一复盘决策。
8. 读取 `references/telemetry-metric-dictionary.zh-CN.md`，生成埋点字典。必须至少包含 `variant_assigned`、`session_started`、`meaningful_event_fired`、`player_choice_made`、`narrative_packet_seen`、`session_checkpoint`、`session_ended`。
9. 读取 `references/retention-risk-gates.zh-CN.md`，提前写死成功、观察、回滚和 Kill 条件。不要事后看数据再改胜利标准。
10. 按交付深度选择模板：快速方案用 `templates/variant-matrix.md`，标准方案用 `templates/weekly-epm-experiment-plan.md`，数据接线用 `templates/instrumentation-dictionary.md`，看板需求用 `templates/dashboard-spec.md`，复盘用 `templates/weekly-review.md`。
11. 最后执行输出门检查。

## 输入边界

### 只有描述 `text_only_request`

可以输出假设版实验，但要标注 `evidence_status: assumption_only`。建议必须写成低成本、可回滚、不会破坏经济和主线的改动。

### 有录屏或截图 `gameplay_recording` / `screenshots`

优先让 `game-experience-analyzer` 建立证据层，再把时间轴和问题卡转换成 EPM 实验。不要把静态截图直接当成节奏证据。

### 有数据 `telemetry_snapshot`

可以设计更具体的指标和分流规则。若数据口径不明，先生成字段核对表，不能把不同版本、不同渠道或不同新老用户混在一起得出结论。

### 有线上版本 `liveops_problem`

必须保留风险门：经济安全、难度安全、新手/老玩家分层、付费影响、公平性、公告/热更窗口。这个 skill 不设计暗黑模式，不用误导、焦虑、强迫红点或损失厌恶去抬指标。

## 输出结构

标准输出必须包含：

1. `case_boundary`：材料来源、版本、平台、用户阶段、已有数据和未知项。
2. `diagnosis_summary`：当前 EPM 问题属于低密度、假密度、过载还是不可理解。
3. `experiment_hypothesis`：一句话假设，写清玩家行为、设计改动、目标指标。
4. `variant_matrix`：A/B/C/D 组，写清主旋钮、具体改动、影响窗口、owner、上线风险。
5. `instrumentation_dictionary`：事件名、触发时机、字段、示例值、用途、隐私边界。
6. `metric_plan`：P1、P2、负向指标、分群、观察周期、最小样本提醒。
7. `dashboard_spec`：看板字段、图表、过滤器、每日检查项。
8. `decision_rules`：成功、放大、继续观察、回滚和 Kill 条件。
9. `weekly_schedule`：一周执行节奏。
10. `handoff_checklist`：策划、客户端、关卡/叙事、数据、QA 的交接清单。

## 证据与数据规则

- 没有真实埋点时，不要承诺 D1/D7 会提升，只能写验证假设。
- 不把会话时长上升自动等同于体验变好；必须同时看退出点、失败率、重复行为和负反馈。
- 不把更多事件等同于更高 EPM；有效事件必须能被玩家理解，并改变状态、目标、选择或情绪。
- 决策权重不是选项数量。弱选择要合并，少而重优先。
- 叙事压缩不是删除剧情。优先压停顿、重复解释、不可交互文本和延迟反馈。
- 新手、回流、老玩家要分群；不同渠道和版本要分开。
- 不得使用 dark pattern，包括强迫红点、误导奖励、虚假倒计时、付费焦虑和不可逆损失伪装。
- 所有成功标准必须在实验前写死。

## 按需读取

- EPM 基础框架：`references/epm-framework.zh-CN.md`
- 一周实验 SOP：`references/weekly-experiment-sop.zh-CN.md`
- 三个主旋钮玩法库：`references/lever-playbook.zh-CN.md`
- 埋点与指标口径：`references/telemetry-metric-dictionary.zh-CN.md`
- 风险门和反例：`references/retention-risk-gates.zh-CN.md`
- 输入表：`templates/experiment-intake.md`
- 标准实验方案：`templates/weekly-epm-experiment-plan.md`
- 变体矩阵：`templates/variant-matrix.md`
- 埋点字典：`templates/instrumentation-dictionary.md`
- 看板规格：`templates/dashboard-spec.md`
- 周复盘：`templates/weekly-review.md`
- 结构化 schema：`templates/experiment-plan.schema.json`
- 可选验证提示：`evals/evals.json`、`evals/rubric.yaml`、`evals/negative_cases.md`
- 示例：`examples/synthetic-survivors-first-session-epm-plan.md`

## 输出门

最终输出前检查：

- 是否先写边界，再写判断。
- 是否把 EPM 问题归类为低密度、假密度、过载或不可理解。
- 是否明确区分事件频率、决策权重、叙事压缩。
- 是否每个变体只有一个主旋钮，避免一次改太多导致无法归因。
- 是否写清具体可上线改动，而不是抽象建议。
- 是否包含埋点事件、字段、触发时机和用途。
- 是否预注册成功标准、负向指标、回滚和 Kill 条件。
- 是否按新手、回流、老玩家或渠道分群。
- 是否避免暗黑模式和纯数值膨胀。
- 是否有一周执行节奏和 owner handoff。
