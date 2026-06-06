# Instrumentation Dictionary

| event_name | trigger | required_fields | purpose | privacy_boundary |
| --- | --- | --- | --- | --- |
| `variant_assigned` | 玩家进入实验范围并完成分流 | `experiment_id`, `variant_id`, `user_segment`, `assignment_time` | 确认分流和样本口径 | no raw identity |
| `session_started` | 会话开始 | `session_id`, `user_id_hash`, `variant_id`, `game_metric_model`, `metric_horizon`, `entry_source`, `account_age_days` | 计算会话、分群、进入来源，并区分总旅程/日留存周期 | hash only |
| `meaningful_decision_made` | 玩家做出会影响后续体验的选择 | `decision_id`, `decision_type`, `option_count`, `expected_impact_window_sec`, `context_id` | 计算 `MD/min` | no chat/raw text |
| `choice_impact_observed` | 选择结果首次可见 | `decision_id`, `impact_type`, `delta_summary`, `latency_sec` | 判断选择是否可归因 | aggregate summary |
| `salient_feedback_fired` | 关键反馈触发 | `feedback_id`, `feedback_type`, `sensory_channels`, `clarity_score`, `linked_decision_id` | 判断 `SF` | no biometric data |
| `embodiment_signal_observed` | 具身反馈窗口出现 | `signal_id`, `control_context`, `input_latency_ms`, `camera_state`, `hitstop_ms` | 判断 `EB` | device-safe only |
| `atmosphere_segment_seen` | 氛围段落出现 | `segment_id`, `duration_sec`, `audio_layer`, `visual_state`, `interactive` | 判断 `AR` | no private media |
| `cognitive_load_signal` | 出现困惑、打断或噪音代理信号 | `signal_type`, `ui_context`, `interruption_type`, `confusion_proxy`, `timestamp_ms` | 判断 `CLP` | no personal content |
| `optimal_stimulation_window_observed` | QA、访谈或遥测代理标注当前刺激窗口 | `window_id`, `stimulation_band`, `boredom_type`, `player_resource_segment`, `stimulus_profile`, `context_stimulation`, `design_direction` | 区分刺激不足、过载、习惯化、低能动性、低意义感 | aggregate/design label only |
| `prediction_error_window_observed` | 玩家遭遇预期与结果差异的关键窗口 | `window_id`, `expected_state`, `actual_state`, `surprise_intensity`, `attribution_clarity`, `recovery_action_available` | 判断自由能区间和可控惊讶 | aggregate/design label only |
| `blanket_coupling_signal` | 行动-反馈耦合被观测或标注 | `coupling_id`, `action_source`, `sensory_channel`, `input_latency_ms`, `feedback_latency_ms`, `noise_source`, `mapping_clarity`, `agency_score` | 判断马尔可夫毯耦合质量 | device-safe only |
| `anti_habituation_signal` | 长线、老玩家或重复循环出现习惯化/反习惯化信号 | `content_loop_id`, `habituation_signal`, `anti_habituation_lever`, `familiar_anchor`, `novel_delta`, `attribution_clarity` | 判断半熟半新是否恢复可学习惊讶 | aggregate/design label only |
| `session_checkpoint` | 到达关键节点 | `checkpoint_id`, `elapsed_sec`, `state_summary` | 计算 TTE、退出点和进度 | no raw location |
| `session_ended` | 会话结束 | `duration_sec`, `end_reason`, `last_checkpoint_id`, `last_event_id` | 计算会话时长和退出位置 | no raw identity |
| `journey_checkpoint_reached` | 单机/Demo/章节到达关键旅程节点 | `journey_id`, `checkpoint_id`, `elapsed_total_playtime_sec`, `completion_percent`, `optional` | 判断总旅程、章节推进和 Demo 完成 | no raw identity |
| `daily_return_observed` | 手游/liveops 用户跨自然日回访 | `natural_day_index`, `consecutive_active_days`, `return_source`, `effective_loop_entered` | 判断 D1/D7、持续活跃和回流质量 | hash only |

## Field Notes

- `clarity_score`、`confusion_proxy` 等字段可以先由设计标注或 QA 标注，不能伪装成真实玩家心理测量。
- `stimulation_band`、`boredom_type`、`player_resource_segment` 只能作为设计/QA/访谈编码或代理指标，不能写成玩家真实心理状态。
- `surprise_intensity`、`attribution_clarity`、`agency_score` 只能作为设计/QA 标注或代理指标，不能写成玩家真实脑内状态。
- `anti_habituation_lever` 只在长线疲劳、老玩家或重复循环诊断中使用；不要把奖励补贴写成反习惯化。
- `journey_checkpoint_reached` 主要用于单机/买断制；`daily_return_observed` 主要用于手游/liveops。不要把两者混成一个 P1。
- `user_id_hash` 必须是稳定匿名 ID。
- 不记录真实姓名、手机号、支付凭据、聊天原文、精确定位或不必要个人信息。
