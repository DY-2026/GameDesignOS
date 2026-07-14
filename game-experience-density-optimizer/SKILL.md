---
name: game-experience-density-optimizer
description: "当用户需要把游戏体验浓度、留存、首局节奏、Demo 完成率、单机总旅程、D1/D7、反馈、具身感、氛围、认知负荷、最佳刺激窗口、FEP/free-energy、预测误差、Markov blanket、习惯化或 liveops 参与问题，编译成可上线、可埋点、可复盘、可回滚的一周 ED 实验包时使用。Use when converting game experience-density and engagement problems into rollback-ready ED experiments."
license: MIT
compatibility: 可处理文本、截图、录屏或遥测摘要；生产实验、真实用户触达和指标承诺必须经过 Human Gate。
metadata:
  version: "1.3.0-candidate"
  short-description: 体验浓度实验编译器
---

# Game Experience Density Optimizer

Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## Mission

把模糊的游戏体验问题编译成可上线、可埋点、可复盘、可回滚的 ED 实验包。

这里的 ED 是 `Experience Density / 体验浓度`。中文统一叫“体验浓度”，不要另造概念名。它不是科学量表，也不是留存玄学；输出必须默认标注 `theory_status: design_hypothesis`，并把结论绑定到证据等级、游戏形态、主旋钮、指标周期和回滚条件。

默认内部管线：

```text
输入材料 -> 输出模式路由 -> Evidence Gate -> 游戏形态分流 -> 最佳刺激窗口 ->
ED 公式项定位 -> 主旋钮选择 -> 实验变体编译 -> 埋点/看板编译 ->
预注册决策门 -> 输出门检查
```

## When To Use

用户讨论以下问题时触发本 skill：

- “体验浓度”、`ED / Experience Density`、每分钟有多少有意义选择、首局太空、首个爆点太晚。
- 留存实验、D1/D3/D7、每日会话、回流 rehook、活动留存、老玩家钝化、中段疲劳。
- 单机总游戏时长、买断制完成率、Steam Demo 完成率、章节推进、核心循环到达率、重玩意愿。
- 反馈不爽、不清楚、不跟手、打击软、操控延迟、镜头/触觉/动作节拍问题。
- 氛围空、留白无质感、叙事停顿、信息太吵、认知负荷高。
- 最佳刺激、低刺激无聊、过载无聊、习惯化、半熟半新、可控惊讶。
- FEP/free-energy、预测误差、Markov blanket、玩家和游戏的输入输出边界。
- 一周 A/B 测试、埋点字典、看板字段、预注册规则、回滚/Kill 条件。

不要用于只有一句创意、还没有核心循环的任务；先用 `game-concept-architect`。不要把截图、PV 或商店页直接当真实节奏证据；先用 `game-experience-analyzer` 建证据层。不要设计暗黑模式、误导奖励、焦虑红点、虚假倒计时、付费压力或不可逆损失伪装。

## Mode Router

先判断输出模式，再决定交付深度。强 skill 的默认不是写大报告，而是给当前场景刚好够用的结果。

| mode | 触发 | 输出密度 |
| --- | --- | --- |
| `quick_ed_triage` | 用户只给一句体验问题，或明确要快速判断 | 1 个边界判断、1 个刺激窗口、1 个主旋钮、2 个最小改动、3 个验证指标、1 个回滚条件 |
| `weekly_ab_plan` | 用户问怎么改、怎么测、本周怎么做、A/B 测试、留存实验、实验方案 | A/B 或 A/B/C/D 变体、埋点、看板、决策门、owner、回滚 |
| `instrumentation_plan` | 用户重点问埋点、看板、指标口径、数据接线 | 事件字典、字段、触发时机、过滤器、数据质量门、隐私边界 |
| `review_and_decide` | 用户提供实验结果、指标变化、复盘材料 | 先查负向门和数据质量，再决定 amplify / iterate / observe / rollback / kill |
| `full_client_delivery` | 用户要求客户交付、团队方案、完整文档、正式报告 | 展开完整 19 模块，附 handoff checklist、QA、风险门 |
| `schema_json` | 用户要求 agent 消费、自动化验证、结构化输出 | 输出符合 `templates/experiment-plan.schema.json` 的 JSON，保留证据和 unknown 字段 |

如果用户没有说明模式：一句话问题默认 `quick_ed_triage`；出现“本周、实验、A/B、怎么测、留存方案”默认 `weekly_ab_plan`；出现“完整、交付、客户、团队评审”默认 `full_client_delivery`。

## Hard Gates

所有输出必须经过这些门：

1. `evidence_gate`：先声明 `evidence_level`、`evidence_status`、允许结论、禁止结论、置信度、缺失证据和混淆风险。读取 `references/evidence-gate.zh-CN.md`。
2. `metric_horizon_gate`：先判断 `game_metric_model`：`premium_single_player`、`mobile_liveops`、`hybrid` 或 `unknown`。单机/买断制默认总旅程指标；手游/liveops 才默认 D1/D7。
3. `stimulation_window_gate`：先判断最佳刺激窗口和无聊类型。无聊不自动等于刺激不足。
4. `density_formula_gate`：把问题落到 `CLP`、`SF`、`EB`、`AR`、`MD/min`，并说明为什么。
5. `one_primary_lever_gate`：每个变体只能有一个主旋钮，最多一个不影响归因的辅助动作。
6. `instrumentation_gate`：没有埋点/看板/复盘口径的方案不能说已可验证。
7. `decision_rule_gate`：成功、观察、回滚、Kill 条件必须在实验前写死。
8. `ethics_gate`：不得用暗黑模式或纯数值膨胀伪装体验优化。
9. `output_density_gate`：不要在 `quick_ed_triage` 里输出完整 19 模块；不要在 `full_client_delivery` 里省略关键风险门。

## Core Model

体验浓度指：当前玩家在当前情境下，单位时间内可吸收、可解释、可转化为探索/学习/意义的刺激密度。

默认工作公式：

```text
ED = MD/min * (SF + EB + AR) / CLP
```

- `MD/min`：每分钟有意义选择次数。不是点击频率，也不是选项数量。
- `SF`：可感知反馈。不是光污染，而是能被玩家看见、听见、感到并归因。
- `EB`：具身感加成。不是剧情代入，而是输入、动作、镜头、触觉和反馈的耦合。
- `AR`：氛围感加成。不是堆素材，而是留白、音画、世界反应和风格一致性。
- `CLP`：认知负荷惩罚。玩家看不懂、学不会、被噪音打断时，先降分母。

诊断顺序固定为：**先判窗口，再降噪，再提质，后调频**。只有在信息清晰、反馈可归因、耦合可理解之后，调高 `MD/min` 才有意义。

FEP、自由能、预测处理、Markov blanket、GameFlow、SDT 只作为设计启发式镜头，不得写成神经科学或心理学证明。涉及这些理论时必须保留 `theory_status: design_hypothesis`。

## Evidence Gate

不要凭感觉跑太远。证据等级决定允许输出什么：

| level | 材料 | 允许 | 禁止 |
| --- | --- | --- | --- |
| `L0_text_only` | 只有口述 | 假设、最小实验、埋点需求 | 声称真实原因或承诺指标提升 |
| `L1_static_assets` | 截图、商店页、PV 截帧 | 信息层级、视觉噪音、可能风险 | 判断真实节奏、手感或会话行为 |
| `L2_recording` | 录屏、试玩视频 | 时间轴、反馈窗口、节奏断点、退出前行为 | 推断全部玩家心理 |
| `L3_playtest_notes` | 试玩笔记、访谈摘要 | 玩家分群假设、问题卡、方向性实验 | 忽略样本偏差 |
| `L4_telemetry_snapshot` | 指标快照 | 分流、埋点核对、方向性实验 | 混版本、混渠道、混新老用户 |
| `L5_ab_result` | 实验结果 | 复盘决策 | 跳过负向门、数据质量门和预注册规则 |

证据不足时输出 `evidence_status: assumption_only` 或 `partial_evidence`。没有真实埋点或试玩证据时，只能说“验证假设”，不能说“一定提升 D1/D7、总时长或完成率”。

## Metric Horizon

先选游戏形态，再选 P1。

- `premium_single_player`：买断制、单机、Steam Demo、章节制、完整旅程承诺。P1 优先看总有效游玩时长、Demo/章节完成率、核心循环到达率、通关/重玩意愿、评价/退款风险。不默认 D1/D7。
- `mobile_liveops`：手游、长线运营、活动、每日循环、回流。P1 可以看 D1/D3/D7/D30、每日会话、连续活跃、活动留存、回流成功率，同时必须看疲劳和投诉。
- `hybrid`：总旅程和 liveops 两套 P1 分开预注册。任一关键周期受损，都不能宣布整体成功。
- `unknown`：材料不足时标 unknown，并写清暂不适用的指标。

## Output Contracts

### quick_ed_triage

必须包含：

- `output_mode`
- `case_boundary`
- `evidence_gate`
- `metric_horizon`
- `optimal_stimulation_fit`
- `primary_formula_item`
- `primary_lever`
- `two_minimal_changes`
- `verification_metrics`
- `rollback_condition`
- `unsupported_claims`

### weekly_ab_plan

必须包含：

- `case_boundary`
- `evidence_gate`
- `metric_horizon`
- `theory_status`
- `optimal_stimulation_fit`
- `diagnosis_summary`
- `experiment_hypothesis`
- `variant_matrix`
- `instrumentation_dictionary`
- `metric_plan`
- `dashboard_spec`
- `decision_rules`
- `weekly_schedule`
- `handoff_checklist`

### instrumentation_plan

必须至少生成 `variant_assigned`、`session_started`、`meaningful_decision_made`、`salient_feedback_fired`、`cognitive_load_signal`、`session_checkpoint`、`session_ended`。涉及手感/反馈时增加 `embodiment_signal_observed` 和 `blanket_coupling_signal`；涉及 OLSO/FEP 时增加 `optimal_stimulation_window_observed` 和 `prediction_error_window_observed`；涉及长线疲劳时增加 `anti_habituation_signal`。

### review_and_decide

复盘顺序固定：

1. 数据质量门：分流、版本、渠道、样本、埋点完整性。
2. 负向门：崩溃、早退、失败率、投诉、疲劳、经济、公平、暗黑模式。
3. P1：按 `game_metric_model` 读取主周期。
4. P2：用 ED proxy、CLP、SF、EB、AR、MD/min、最佳刺激窗口解释原因。
5. 决策：`amplify`、`iterate`、`observe`、`rollback` 或 `kill`。

### full_client_delivery

完整交付才展开 19 模块：`case_boundary`、`metric_horizon`、`theory_status`、`optimal_stimulation_fit`、`diagnosis_summary`、`density_curve_intent`、`free_energy_window`、`markov_blanket_coupling`、`growth_surprise_ladder`、`anti_habituation_plan`、`motivation_flow_gate`、`experiment_hypothesis`、`variant_matrix`、`instrumentation_dictionary`、`metric_plan`、`dashboard_spec`、`decision_rules`、`weekly_schedule`、`handoff_checklist`。

### schema_json

按 `templates/experiment-plan.schema.json` 输出结构化 JSON。未知信息保留 `unknown`，不要省略证据不足项。

## Handoff

当输入来自 `game-experience-analyzer`，优先消费已有 `ed-handoff`，尤其是 `issue_cards_for_ed`、`evidence_refs`、`suggested_primary_lever`、`secondary_noise`、`confounder_risk` 和 `unknowns`。不要重做完整体验分析。

GameDesignOS runtime 提供规范名为 `ed-handoff.schema.json` 的跨 skill contract。本 skill 不创建平行 schema；独立使用时按 [ED Handoff 最小契约](references/ed-handoff-contract.md) 接收，再编译成 `weekly_ab_plan` 或 `schema_json`。

## References

按需读取，不要一次性加载所有文件：

- 证据门：`references/evidence-gate.zh-CN.md`
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
- 主旋钮玩法库：`references/lever-playbook.zh-CN.md`
- 埋点与指标口径：`references/telemetry-metric-dictionary.zh-CN.md`
- 风险门和反例：`references/retention-risk-gates.zh-CN.md`

## Templates

- 输入表：`templates/experiment-intake.md`
- 标准实验方案：`templates/weekly-ed-experiment-plan.md`
- 变体矩阵：`templates/variant-matrix.md`
- ED 相对评分卡：`templates/ed-scorecard.md`
- 埋点字典：`templates/instrumentation-dictionary.md`
- 看板规格：`templates/dashboard-spec.md`
- 周复盘：`templates/weekly-review.md`
- 结构化 schema：`templates/experiment-plan.schema.json`

## Output Gate

最终输出前检查：

- 是否先写 `output_mode`、`case_boundary`、`evidence_gate`，再写诊断。
- 是否证据不足时降级为 `assumption_only` 或 `partial_evidence`。
- 是否先区分 `premium_single_player`、`mobile_liveops`、`hybrid` 或 `unknown`。
- 是否为单机/买断制使用总旅程指标，为手游/liveops 使用每日和持续天数指标。
- 是否标注 `theory_status: design_hypothesis`。
- 是否先判断最佳刺激窗口，区分低刺激、过载、习惯化、低能动性、低意义感或 unknown。
- 是否把问题落到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
- 是否遵守“先判窗口，再降噪，再提质，后调频”。
- 是否每个变体只有一个主旋钮，并写清配置开关、owner、QA 和回滚。
- 是否包含埋点事件、字段、触发时机、看板过滤器和数据质量门。
- 是否预注册成功、观察、回滚和 Kill 条件。
- 如果涉及长线、赛季、刷子、肉鸽、UGC 或老玩家钝化，是否输出 `anti_habituation_plan`。
- 是否避免暗黑模式、误导奖励、焦虑红点、虚假倒计时和纯数值膨胀。
- 是否让输出密度匹配 mode，而不是每次都写完整大报告。
