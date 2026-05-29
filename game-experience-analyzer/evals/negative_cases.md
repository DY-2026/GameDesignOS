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
