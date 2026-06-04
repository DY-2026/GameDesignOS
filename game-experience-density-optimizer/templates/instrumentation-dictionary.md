# Instrumentation Dictionary

| event_name | trigger | required_fields | purpose | privacy_boundary |
| --- | --- | --- | --- | --- |
| `variant_assigned` | 玩家进入实验范围并完成分流 | `experiment_id`, `variant_id`, `user_segment`, `assignment_time` | 确认分流和样本口径 | no raw identity |
| `session_started` | 会话开始 | `session_id`, `user_id_hash`, `variant_id`, `entry_source`, `account_age_days` | 计算会话、分群、进入来源 | hash only |
| `meaningful_decision_made` | 玩家做出会影响后续体验的选择 | `decision_id`, `decision_type`, `option_count`, `expected_impact_window_sec`, `context_id` | 计算 `MD/min` | no chat/raw text |
| `choice_impact_observed` | 选择结果首次可见 | `decision_id`, `impact_type`, `delta_summary`, `latency_sec` | 判断选择是否可归因 | aggregate summary |
| `salient_feedback_fired` | 关键反馈触发 | `feedback_id`, `feedback_type`, `sensory_channels`, `clarity_score`, `linked_decision_id` | 判断 `SF` | no biometric data |
| `embodiment_signal_observed` | 具身反馈窗口出现 | `signal_id`, `control_context`, `input_latency_ms`, `camera_state`, `hitstop_ms` | 判断 `EB` | device-safe only |
| `atmosphere_segment_seen` | 氛围段落出现 | `segment_id`, `duration_sec`, `audio_layer`, `visual_state`, `interactive` | 判断 `AR` | no private media |
| `cognitive_load_signal` | 出现困惑、打断或噪音代理信号 | `signal_type`, `ui_context`, `interruption_type`, `confusion_proxy`, `timestamp_ms` | 判断 `CLP` | no personal content |
| `session_checkpoint` | 到达关键节点 | `checkpoint_id`, `elapsed_sec`, `state_summary` | 计算 TTE、退出点和进度 | no raw location |
| `session_ended` | 会话结束 | `duration_sec`, `end_reason`, `last_checkpoint_id`, `last_event_id` | 计算会话时长和退出位置 | no raw identity |

## Field Notes

- `clarity_score`、`confusion_proxy` 等字段可以先由设计标注或 QA 标注，不能伪装成真实玩家心理测量。
- `user_id_hash` 必须是稳定匿名 ID。
- 不记录真实姓名、手机号、支付凭据、聊天原文、精确定位或不必要个人信息。
