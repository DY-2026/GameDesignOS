---
name: game-experience-density-optimizer
description: Use when turning game retention, first-session pacing, prototype feel, feedback, embodiment, atmosphere, cognitive-load, or live-engagement problems into rollback-ready ED (Experience Density, 体验浓度) experiments with instrumentation and weekly decision rules.
metadata:
  short-description: Design weekly ED experiments for experience density
---

# Game Experience Density Optimizer

Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 什么时候使用

当用户想讨论或提升游戏的体验浓度、留存、首局体验、前 10 分钟节奏、教程清晰度、局内上头感、中段疲劳、回流体验、交互反馈、预测-反馈循环、具身感、氛围感、认知负荷、A/B 测试方案、埋点字典、数据看板、D1/D3/D7 留存、会话时长、首个有效选择时间、反馈强度、功能暴露节奏或小版本验证时，使用这个 skill。

以下请求要强触发：

- “体验浓度”
- “ED / Experience Density”
- “每分钟有多少事情发生”
- “有意义选择频率”
- “反馈不够爽/不够清楚”
- “操控不跟手/不够具身”
- “氛围感不足”
- “认知负荷太高”
- “先降噪，再提质，后调频”
- “首局/新手期节奏”
- “一周 A/B 测试”
- “用小成本改体验”
- “埋点字典”
- “看板字段”
- “D1/D7 怎么验证”
- “首个爆点太晚”
- “中段疲劳”
- “做三组可发布改动”
- “给我留存实验方案”

这个 skill 的任务不是写一个大版本方案，也不是把节奏简单加快。它要把体验浓度问题压缩成一周能跑完的小实验，让设计判断变成可上线、可埋点、可复盘、可回滚的改动包。

## 概念边界

中文统一叫“体验浓度”。英文保留 `ED` / `Experience Density`，但不要在中文解释里把核心概念写成另一个名称。

体验浓度指：在游戏进行过程中，每单位时间内玩家所经历的有意义互动和可感知反馈的密集程度。它关注游戏体验的浓缩水平：每分钟有多少有意义的选择、多少新反馈、多少能被玩家理解和归因的体验信号。

这个概念来自设计观察和方法论假设，不是经过科学验证的心理学量表。可以借用预测处理、受控幻觉、具身感和注意力调动作为启发式镜头，但输出时必须标注为 `theory_status: design_hypothesis`，不能包装成科学结论。

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

## 默认诊断顺序

必须按“先降噪，再提质，后调频”处理：

1. 先看 `CLP`：玩家是否看不懂、学不会、无法归因、被 UI/特效/弹窗/术语打断。CLP 是分母，没降下来之前不要加事件。
2. 再看 `SF / EB / AR`：反馈是否显著、操控是否人机一体、音画氛围是否自洽。这里决定瞬时体验的纵向质量。
3. 最后看 `MD/min`：玩家是否有足够频率的有意义选择。只有在信息清晰、反馈有质感后，调频才有意义。

不要把“更多事件”“更多奖励”“更多红点”“更长在线”直接等同于体验浓度提升。

## 默认流程

1. 判断输入类型：`gameplay_recording`、`prototype_build`、`telemetry_snapshot`、`design_doc`、`liveops_problem`、`store_demo_feedback`、`text_only_request`。如果用户只给一段描述，不要追问一串问题，先输出 `unknown` 字段和可执行的假设版实验。
2. 建立边界：读取 `templates/experiment-intake.md`，输出 `case_boundary`、`available_evidence`、`unsupported_claims`、`key_unknowns`、`theory_status`。没有真实数据时只能设计验证方案，不能声称一定提升留存。
3. 读取 `references/ed-framework.zh-CN.md` 和 `references/density-formula.zh-CN.md`，把当前问题定位到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
4. 读取 `references/density-diagnosis-workflow.zh-CN.md`，按“先降噪，再提质，后调频”输出诊断顺序。
5. 读取 `references/interaction-prediction-lens.zh-CN.md`，只在需要解释交互优势、预测-反馈循环、具身幻觉和注意力调动时使用；不要过度科学化。
6. 读取 `references/lever-playbook.zh-CN.md`，把问题映射到一个主旋钮。每个实验变体只能有一个主旋钮，最多一个不影响归因的辅助动作。
7. 选择实验模式：`first_session_activation`、`mid_session_fatigue`、`return_session_rehook`、`embodiment_feedback`、`atmosphere_pacing`、`liveops_micro_tuning`。
8. 设计实验：默认输出 A/B/C/D 四组。A 是对照组，B 优先降 CLP，C 提升 SF/EB/AR 的纵向质量，D 调整 MD/min。用户要求极小范围时，只输出 A/B。
9. 读取 `references/weekly-experiment-sop.zh-CN.md`，把方案压成一周节奏：周一冻结假设，周二上版，周三监控阻断项，周四小复查，周五到周日收样本，周一复盘决策。
10. 读取 `references/telemetry-metric-dictionary.zh-CN.md`，生成埋点字典。必须至少包含 `variant_assigned`、`session_started`、`meaningful_decision_made`、`salient_feedback_fired`、`cognitive_load_signal`、`session_checkpoint`、`session_ended`。
11. 读取 `references/retention-risk-gates.zh-CN.md`，提前写死成功、观察、回滚和 Kill 条件。不要事后看数据再改胜利标准。
12. 按交付深度选择模板：快速方案用 `templates/variant-matrix.md`，标准方案用 `templates/weekly-ed-experiment-plan.md`，数据接线用 `templates/instrumentation-dictionary.md`，看板需求用 `templates/dashboard-spec.md`，复盘用 `templates/weekly-review.md`。
13. 最后执行输出门检查。

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
2. `theory_status`：默认 `design_hypothesis`，说明该方法是设计启发式而非科学量表。
3. `diagnosis_summary`：当前问题主要落在 `CLP`、`SF`、`EB`、`AR`、`MD/min` 哪一项。
4. `density_curve_intent`：当前段落意图是高压、建立规则、放松观察、情绪沉淀、决策规划还是爽感释放。
5. `experiment_hypothesis`：一句话假设，写清玩家行为、设计改动、目标指标。
6. `variant_matrix`：A/B/C/D 组，写清主旋钮、具体改动、影响窗口、owner、上线风险。
7. `instrumentation_dictionary`：事件名、触发时机、字段、示例值、用途、隐私边界。
8. `metric_plan`：P1、P2、负向指标、分群、观察周期、最小样本提醒。
9. `dashboard_spec`：看板字段、图表、过滤器、每日检查项。
10. `decision_rules`：成功、放大、继续观察、回滚和 Kill 条件。
11. `weekly_schedule`：一周执行节奏。
12. `handoff_checklist`：策划、客户端、关卡/叙事、美术/音频、数据、QA 的交接清单。

## 证据与数据规则

- 没有真实埋点时，不要承诺 D1/D7 会提升，只能写验证假设。
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
- 体验浓度公式：`references/density-formula.zh-CN.md`
- 诊断流程：`references/density-diagnosis-workflow.zh-CN.md`
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
- 是否标注 `theory_status: design_hypothesis`。
- 是否把体验浓度问题落到 `CLP`、`SF`、`EB`、`AR`、`MD/min`。
- 是否遵守“先降噪，再提质，后调频”。
- 是否区分水平频率、纵向质量和认知负荷。
- 是否每个变体只有一个主旋钮，避免一次改太多导致无法归因。
- 是否写清具体可上线改动，而不是抽象建议。
- 是否包含埋点事件、字段、触发时机和用途。
- 是否预注册成功标准、负向指标、回滚和 Kill 条件。
- 是否按新手、回流、老玩家或渠道分群。
- 是否避免暗黑模式和纯数值膨胀。
- 是否有一周执行节奏和 owner handoff。
