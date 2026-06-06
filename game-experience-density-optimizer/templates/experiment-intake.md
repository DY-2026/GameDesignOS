# ED Experiment Intake

## Case Boundary

| 字段 | 值 |
| --- | --- |
| case_visibility | unknown |
| data_sensitivity | unknown |
| output_destination | private_notes |
| redaction_required | unknown |
| game_name | unknown |
| build_version | unknown |
| platform | unknown |
| channel | unknown |
| game_metric_model | premium_single_player / mobile_liveops / hybrid / unknown |
| metric_horizon | total_journey / chapter_segment / run_based / daily_retention / event_cycle / hybrid_split / unknown |
| primary_success_horizon | unknown |
| target_user_segment | unknown |
| session_scope | first_session |
| current_problem | unknown |
| available_material | text_only_request |
| evidence_status | assumption_only |
| theory_status | design_hypothesis |

## Optimal Stimulation Fit

| 字段 | 值 |
| --- | --- |
| stimulation_band | too_low / optimal / too_high / uneven / unknown |
| boredom_type | under_stimulation / over_stimulation / habituation / low_agency / low_meaning / mixed / unknown |
| player_resource_profile | unknown |
| stimulus_profile | unknown |
| context_stimulation | first_session / boss_retry / late_session / daily_grind / event_cycle / demo_opening / unknown |
| design_direction | add_semi_novelty / add_familiar_anchor / reduce_overload / anti_habituation / repair_agency / add_meaning / preserve_curve / unknown |
| evidence_for_window | unknown |
| risk_if_misdiagnosed | unknown |

## Available Evidence

| 来源 | 是否可用 | 说明 |
| --- | --- | --- |
| gameplay_recording | unknown | unknown |
| screenshots | unknown | unknown |
| telemetry_snapshot | unknown | unknown |
| design_doc | unknown | unknown |
| player_feedback | unknown | unknown |
| store/demo feedback | unknown | unknown |

## Current Metrics

| 指标 | 当前值 | 口径 | 置信度 |
| --- | --- | --- | --- |
| total_playtime_hours | unknown | 单机/买断制优先 | unknown |
| main_path_completion_rate | unknown | 单机/买断制优先 | unknown |
| chapter_checkpoint_reach_rate | unknown | 单机/买断制优先 | unknown |
| demo_completion_rate | unknown | Demo 优先 | unknown |
| replay_intent_signal | unknown | 单机/肉鸽/买断制可选 | unknown |
| D1 | unknown | 手游/liveops 优先 | unknown |
| D3 | unknown | 手游/liveops 优先 | unknown |
| D7 | unknown | 手游/liveops 优先 | unknown |
| consecutive_active_days | unknown | 手游/liveops 优先 | unknown |
| session_median_duration | unknown | unknown | unknown |
| TTE | unknown | unknown | unknown |
| ED_proxy | unknown | unknown | unknown |
| optimal_stimulation_band | unknown | 设计/QA/玩家反馈代理标注 | unknown |
| boredom_type_mix | unknown | 区分刺激不足、过载、习惯化、低能动性、低意义感 | unknown |
| CLP_proxy | unknown | unknown | unknown |
| SF_proxy | unknown | unknown | unknown |
| EB_proxy | unknown | unknown | unknown |
| AR_proxy | unknown | unknown | unknown |
| MD_per_min | unknown | unknown | unknown |
| early_exit_rate | unknown | unknown | unknown |
| failure_rate | unknown | unknown | unknown |
| anti_habituation_fit | unknown | 长线/老玩家/重复循环时适用 | unknown |

## Key Unknowns

- unknown

## Unsupported Claims

- 没有真实数据时，不判断留存必然提升。
- 没有确认手游/liveops 时，不把 D1/D7 当成默认 P1。
- 没有确认单机/买断制时，不把总游戏时长或完成率当成默认 P1。
- 没有录屏或可玩样本时，不判断真实操作节奏和手感。
- 没有经济数据时，不判断奖励改动对长期经济安全的影响。
- 没有区分 `boredom_type` 时，不把“无聊”直接解释成刺激不足。
- 没有玩家资源和语境证据时，不判断新颖性一定是正向。
