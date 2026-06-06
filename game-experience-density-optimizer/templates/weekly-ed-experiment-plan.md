# Weekly ED Experiment Plan

## 1. Case Boundary

| 字段 | 值 |
| --- | --- |
| experiment_id | unknown |
| case_visibility | unknown |
| game_name | unknown |
| build_version | unknown |
| platform | unknown |
| game_metric_model | premium_single_player / mobile_liveops / hybrid / unknown |
| metric_horizon | total_journey / chapter_segment / run_based / daily_retention / event_cycle / hybrid_split / unknown |
| primary_success_horizon | unknown |
| target_user_segment | unknown |
| session_scope | unknown |
| available_evidence | unknown |
| evidence_status | unknown |
| theory_status | design_hypothesis |

## 2. Metric Horizon Gate

| 字段 | 值 |
| --- | --- |
| game_metric_model | premium_single_player / mobile_liveops / hybrid / unknown |
| primary_time_horizon | total_journey / chapter_segment / run_based / daily_retention / event_cycle / hybrid_split / unknown |
| p1_metric_family | total_playtime / completion_progress / replay_intent / daily_retention / liveops_continuity / hybrid_split / unknown |
| excluded_metrics | unknown |
| rationale | unknown |

## 3. Optimal Stimulation Fit

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

## 4. ED Diagnosis

| 公式项 | 当前判断 | 证据/观察 | 优先级 |
| --- | --- | --- | --- |
| CLP | unknown | unknown | unknown |
| SF | unknown | unknown | unknown |
| EB | unknown | unknown | unknown |
| AR | unknown | unknown | unknown |
| MD/min | unknown | unknown | unknown |

当前浓度问题：`unknown`

当前段落意图：`高压 / 建立规则 / 放松观察 / 情绪沉淀 / 决策规划 / 爽感释放 / unknown`

建议顺序：`先判窗口 / 再降噪 / 再提质 / 后调频 / unknown`

## 5. Free Energy Window & Markov Blanket Coupling

| 字段 | 值 |
| --- | --- |
| free_energy_band | too_low / optimal / too_high / unknown |
| prediction_error_source | unknown |
| player_tolerance_reason | unknown |
| intervention_direction | reduce_noise / improve_quality / tune_frequency / preserve_curve / unknown |
| sensory_state_quality | unknown |
| action_state_quality | unknown |
| coupling_break | none / latency / noise / unclear_mapping / weak_agency / overload / unknown |
| repair_action | unknown |

## 6. Growth Surprise Ladder

| 字段 | 值 |
| --- | --- |
| current_model_level | explicit / system / strategy / meta / unknown |
| next_learnable_surprise | unknown |
| evidence_that_player_can_recover | unknown |
| risk_if_too_steep | unknown |

## 7. Motivation & Flow Gate

| 字段 | 值 |
| --- | --- |
| clear_goal_quality | unknown |
| feedback_timeliness | unknown |
| challenge_skill_fit | too_easy / matched / too_hard / uneven / unknown |
| player_control_quality | unknown |
| autonomy_support | unknown |
| competence_support | unknown |
| relatedness_support | not_applicable / weak / adequate / strong / unknown |
| novelty_support | weak / adequate / strong / noisy / unknown |
| optimal_novelty_fit | too_low / matched / too_high / unknown |
| novelty_quality | learnable / cosmetic / random_noise / overwhelming / unknown |
| risk_if_optimized_only_for_density | unknown |

## 8. Anti-habituation Plan

长线、老玩家、赛季、刷子、肉鸽、UGC、重复日常或疲劳问题必须填写；不适用时写 `not_applicable`。

| 字段 | 值 |
| --- | --- |
| applicable | yes / no / unknown |
| selected_lever | alternative_use / attention_investment / conscious_reframing / context_shift / combinatorial_depth / not_applicable / unknown |
| familiar_anchor | unknown |
| novel_delta | unknown |
| attribution_plan | unknown |
| risk_if_only_add_rewards | unknown |

## 9. Experiment Hypothesis

```text
如果我们通过【主旋钮】改变【具体体验段】，玩家会在【影响窗口】内产生【行为变化】，并在【目标指标】上体现改善，同时不触发【负向门】。
```

## 10. Variant Matrix

| variant_id | primary_lever | optimal_stimulation_target | prediction_error_target | blanket_coupling_target | concrete_change | impact_window | owner | risk | rollback |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A_control | none | current | current | current | 当前版本 | current session | design/data | none | none |
| B_reduce_clp | CLP | reduce_overload / add_familiar_anchor | reduce_unexplainable_error | lower_noise | unknown | 30-120 sec | design/ui/client | missing_information | config off |
| C_raise_vertical_quality | SF / EB / AR | improve_attributable_interest | improve_attribution | improve_sensory_action_mapping | unknown | 30-180 sec | design/3c/art/audio | sensory_noise | config off |
| D_tune_md_frequency | MD/min | add_semi_novelty_only_if_window_allows | add_controllable_surprise | preserve_readability | unknown | 60-180 sec | design/system/level | overload | config off |
| E_anti_habituation | MD/min / system_depth | anti_habituation | restore_learnable_surprise | preserve_readability | optional: only for long-term fatigue | event cycle / run segment | design/system/liveops | balance_shift | config off |

## 11. Instrumentation Dictionary

引用 `templates/instrumentation-dictionary.md`，至少包含：`variant_assigned`、`session_started`、`meaningful_decision_made`、`salient_feedback_fired`、`cognitive_load_signal`、`optimal_stimulation_window_observed`、`session_checkpoint`、`session_ended`。FEP/马尔可夫毯相关实验推荐增加 `prediction_error_window_observed` 和 `blanket_coupling_signal`。长线/疲劳实验增加 `anti_habituation_signal`。

## 12. Metric Plan

| 层级 | 指标 | 目标 | 口径 | 分群 |
| --- | --- | --- | --- | --- |
| P1 | unknown | unknown | single-player: total journey/completion; mobile: daily retention/continuity | new/returning/existing |
| P2 | ED proxy / optimal_stimulation_band / boredom_type_mix / prediction_error_band / blanket_coupling_quality | unknown | same version/session | new/returning/existing |
| negative | unknown | no spike | pre-registered | all segments |

## 13. Dashboard Spec

引用 `templates/dashboard-spec.md`。默认过滤器：experiment_id、variant_id、game_metric_model、metric_horizon、user_segment、platform、channel、client_version、session_scope、checkpoint_id、stimulation_band、boredom_type。

## 14. Decision Rules

| 决策 | 预注册条件 |
| --- | --- |
| amplify | unknown |
| iterate | unknown |
| observe | unknown |
| rollback | unknown |
| kill | dark pattern / negative gate / unsupported evidence |

## 15. Weekly Schedule

| 日期 | 目标 | 产物 |
| --- | --- | --- |
| 周一 | 冻结假设 | variant matrix / metric plan / risk gates |
| 周二 | 上版或发 playtest 分支 | config / instrumentation / QA pass |
| 周三 | 阻断项检查 | crash / event missing / split balance |
| 周四 | 小复查 | TTE / ED proxy / exit point |
| 周五-周日 | 收样本 | 单机看总旅程/章节推进；手游看每日和持续天数 |
| 下周一 | 复盘决策 | amplify / iterate / observe / rollback / kill |

## 16. Handoff Checklist

| 角色 | 交付物 |
| --- | --- |
| design | 假设、变体、成功标准、风险门 |
| client | 开关位、埋点、回滚配置 |
| level/narrative/audio/art | 可上线内容与资源边界 |
| data | 看板、分群、数据质量门 |
| QA | 分流、埋点触发、回滚、关键路径可玩 |
