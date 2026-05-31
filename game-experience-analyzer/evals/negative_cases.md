# Negative Cases / 反例评测

这些反例用于检查 skill 是否从“体验分析”升级为“诊断引擎”。每个反例都必须触发边界、证据、模式和反幻觉检查。

## 字段定义

| 字段 | 用途 |
| --- | --- |
| 用户输入 | 触发错误倾向的最小 prompt。 |
| 错误输出模式 | 评测时要判为失败的行为。 |
| 正确行为 | 通过评测必须出现的处理方式。 |
| Rubric 关注 | 对应 `evals/rubric.yaml` 的维度。 |

## 最小可执行示例

输入“只有截图，判断手感”时，合格输出必须先写样本边界：截图可判断静态反馈可读性，不可判断操作手感；手感判断进入 `unsupported_by_sample`；下一步要求 10-30 秒战斗录屏。

## Case 1: 只给截图却判断手感

**用户输入**

> 只有 3 张战斗截图，帮我判断这个动作游戏打击手感好不好。

**错误输出模式**

- 高置信写“打击感很强”“操作反馈顺滑”。
- 没有说明截图不能判断输入延迟、震屏节奏、受击反馈连续性。

**正确行为**

- `sample_scope_gate` 写明截图只能判断静态反馈可读性、特效遮挡、命中反馈是否可见。
- 手感判断标 `unsupported_by_sample` 或 `uncertain`。
- 补料要求：10-30 秒战斗录屏、输入/命中/受击/失败片段。

**Rubric 关注**

- `sample_scope_boundary`
- `uncertainty_calibration`
- `anti_hallucination`

## Case 2: 只给 PV 却预测销量

**用户输入**

> 这是一个 45 秒 PV，帮我预测能卖多少份。

**错误输出模式**

- 给出确定销量、流水或下载量数字。
- 把视觉热度和商业结果混为一谈。

**正确行为**

- 路由到 `PV 热度诊断包` / `trailer_heat_prediction`。
- 只输出热度潜力分层、验证指标、关键 unknown。
- 如需销量预测，要求 Steam 愿望单、曝光、CTR、Demo 转化、竞品基准等数据。

**Rubric 关注**

- `mode_selection_accuracy`
- `uncertainty_calibration`
- `validation_quality`

## Case 3: 链接不可访问却编造时间轴

**用户输入**

> 这个视频链接打不开也没关系，你帮我按时间轴拆一下。

**错误输出模式**

- 编造 `00:00-00:30` 的事件流。
- 写出未观看画面、玩法、剧情或 UI 事实。

**正确行为**

- 生成 `access_blocked` evidence，写清 `access_notes`。
- 只能基于页面可见标题、封面、简介或用户描述做弱诊断。
- 要求用户补截图、本地录屏、可访问链接或手动时间戳片段。

**Rubric 关注**

- `anti_hallucination`
- `evidence_linkage`
- `sample_scope_boundary`

## Case 4: 用户问玩法机制，却只套四步法

**用户输入**

> 分析这个 Roguelike 构筑玩法机制，重点看选择、Build、资源和失败反馈。

**错误输出模式**

- 只输出 Hook/Loop/Link/Surprise 分数。
- 不分析玩家决策、构筑取舍、失败复盘和资源经济。

**正确行为**

- 路由到 `核心循环诊断包` / `gameplay_mechanics`，可辅助 `genre_benchmark`。
- 必须输出 `decision_point`、`resource_economy`、`progression_unlock`、`failure_signal` 的证据。
- 四步法最多作为辅助，不作为主框架。

**Rubric 关注**

- `mode_selection_accuracy`
- `genre_sensitivity`
- `actionability`

## Case 5: 用户问单机关卡，却套手游留存模型

**用户输入**

> 这是一个单机动作冒险关卡 12 分钟录屏，帮我看主路径、节奏、玩家自主权和 Boss 前铺垫。

**错误输出模式**

- 用 D1/D7、首充、广告、日常任务作为主分析框架。
- 没有说明样本是 `level_slice`，不能当完整通关。

**正确行为**

- 路由到 `单机流程节奏诊断包` / `single_player_design`。
- 输出 `single_player_scope`、`critical_path`、`pacing_beats`、`agency_map`、`challenge_skill_feedback`。
- 商业化/留存只在样本出现或用户要求时作为辅助。

**Rubric 关注**

- `mode_selection_accuracy`
- `genre_sensitivity`
- `sample_scope_boundary`

## Case 6: schema 文件名误导，`*.schema.json` 不是 schema

**用户输入**

> 按 `templates/structured-output.schema.json` 校验输出结构。

**错误输出模式**

- `*.schema.json` 实际只是填好字段的示例对象，没有 `$schema`、`type`、`properties`、`required`。
- 把 example/contract 当成 JSON Schema 宣称“已校验”。

**正确行为**

- `*.schema.json` 必须是真正的 JSON Schema。
- 如果文件只是示例，必须命名为 `*.example.json` 或在 README 明确标注为 example/contract。
- 结构化输出应区分 `structured-output.schema.json` 和 `structured-output.example.json`。

**Rubric 关注**

- `output_contract_integrity`
- `anti_hallucination`
- `validation_quality`

## Case 7: 诊断包绕过 mode router

**用户输入**

> 做一个 PV 热度诊断包，顺便整体分析一下这个项目。

**错误输出模式**

- 直接新增“综合热度分析”“泛游戏分析”等未定义 mode。
- 诊断包只作为标题，不映射到 `references/analysis-mode-router.yaml` 的既有 modes。
- 把所有镜头一次性堆上，不说明主 mode 和辅助 mode。

**正确行为**

- 先选 `pv_heat_diagnosis`，再映射到 `trailer_heat_prediction`。
- 如需补充整体视角，只能作为 supporting mode 或后续升级条件，不能绕过 mode router。
- 输出 `diagnosis_route`：`diagnosis_pack`、`primary_modes`、`supporting_modes`、`required_sections`、`not_enabled`。

**Rubric 关注**

- `mode_selection_accuracy`
- `diagnosis_pack_routing`
- `scope_control`

## Case 8: 截图样本输出动态高置信结论

**用户输入**

> 只有一张主界面截图，判断新手教程节奏、战斗手感和留存会不会好。

**错误输出模式**

- 高置信判断教程节奏、点击手感、战斗反馈连续性或 D7 留存。
- 没有把动态过程放进 `uncertain` 或 `unsupported_by_sample`。

**正确行为**

- 路由到 `ux_ui`，输出静态 UI 层级、主目标、入口拥挤、可读性风险。
- 动态判断必须标 `uncertain` 或 `unsupported_by_sample`。
- 补料要求：首次进入录屏、战斗片段、点击热区或漏斗数据。

**Rubric 关注**

- `sample_scope_boundary`
- `uncertainty_calibration`
- `anti_hallucination`

## Case 9: PV 样本输出确定商业结果

**用户输入**

> 这条 PV 看起来挺炸，直接告诉我能不能卖 100 万份，流水大概多少，D7 会不会高。

**错误输出模式**

- 直接给确定销量、流水或 D7 留存判断。
- 用“视觉冲击强”替代真实商业验证链。
- 没有要求愿望单、CTR、Demo 转化、投放数据或竞品基准。

**正确行为**

- 路由到 `pv_heat_diagnosis` / `trailer_heat_prediction`。
- 只输出热度潜力分层、关键 unknown、验证计划。
- 明确 PV 不能预测确定销量、流水、下载量或 D7 留存。

**Rubric 关注**

- `uncertainty_calibration`
- `validation_quality`
- `anti_hallucination`

## Case 10: 无法访问链接却编造时间轴

**用户输入**

> 链接打不开，你就按经验帮我拆一个 0-60 秒时间轴。

**错误输出模式**

- 编造 `00:00-00:10`、`00:10-00:30` 等视频事件。
- 写出未观看的画面、玩法、UI、剧情、音频或 CTA。
- 不保留 `access_notes` 和 `tool_readiness`。

**正确行为**

- 记录 `access_blocked` evidence，写清 `access_notes` 和 `tool_readiness`。
- 只能保留 page-level evidence 或用户明确提供的描述。
- 请求用户提供截图、本地 clip、可访问 mirror link 或手动时间戳片段。

**Rubric 关注**

- `anti_hallucination`
- `evidence_linkage`
- `tool_readiness`

## Case 11: 完整拆解没有拆解目标

**用户输入**

> 完整拆解这个游戏，告诉我为什么它成立。

**错误输出模式**

- 直接堆 MDA、四步法、市场、商业化等所有框架。
- 没有说明本次拆解是为了理解成功、找断点、迁移机制、对标品类还是改原型。
- 没有样本边界和不回答的问题。

**正确行为**

- 路由到 `game_dissection_diagnosis`。
- 先输出 `dissection_goal`，并说明主 mode、辅助 mode 和不启用镜头。
- 样本边界限制后续所有判断。

**Rubric 关注**

- `game_dissection_quality`
- `mode_selection_accuracy`
- `sample_scope_boundary`

## Case 12: 只复刻竞品表层

**用户输入**

> 这个竞品机制很好，我们照着做一个类似的方案。

**错误输出模式**

- 复制或鼓励复制 IP、角色、剧情、美术、文案、数值、活动节奏或运营包装。
- 只列“抄哪些功能”，不拆可迁移结构和依赖条件。

**正确行为**

- 输出 `transferability_boundary`。
- 区分 `transferable_structure` 与 `non_transferable_surface`。
- 说明迁移到目标项目需要验证的平台、受众、内容产能、社交密度、商业模型和指标。

**Rubric 关注**

- `game_dissection_quality`
- `genre_sensitivity`
- `validation_quality`

## Case 13: 短片段当完整游戏结论

**用户输入**

> 这是一个 5 分钟片段，完整拆解它的后期深度、长线留存和社区生态。

**错误输出模式**

- 高置信判断后期内容、长期留存、全局口碑或社区生态。
- 没有把片段样本外的判断标为 `unsupported_by_sample`。

**正确行为**

- 保留完整拆解框架，但把长期内容、后期经济、社区生态和商业结果降级为 unknown。
- 只分析片段内可见的玩家动词、短期目标、反馈和动态假设。
- 给出需要补充的多段样本、full_run_review、留存/社区数据或竞品基准。

**Rubric 关注**

- `sample_scope_boundary`
- `uncertainty_calibration`
- `anti_hallucination`

## Case 14: 只输出 MDA，不做玩家动词和目标

**用户输入**

> 拆一下这个机制为什么好玩，不用太商业，主要看玩法结构。

**错误输出模式**

- 只输出 Mechanics / Dynamics / Aesthetics 三段。
- 没有玩家动词清单、动作-目标对齐、不确定性来源和系统动态图。

**正确行为**

- 路由到 `game_dissection_diagnosis` 或 `gameplay_mechanics`。
- 必须输出 `player_verb_inventory`、`action_goal_alignment`、`uncertainty_sources` 和 `system_dynamics_map`。
- MDA 只能作为辅助解释，除非用户明确点名 MDA。

**Rubric 关注**

- `game_dissection_quality`
- `mode_selection_accuracy`
- `evidence_linkage`
