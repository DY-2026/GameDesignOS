---
case_type: synthetic_example
source_status: synthetic
contains_private_project_info: false
license_status: original_synthetic_public_example
intended_use: public_repo_example
---

# Synthetic First-Session ED Experiment Plan

## Case Boundary

| field | value |
| --- | --- |
| case_visibility | synthetic_case |
| game_name | Neon Orchard Survivors |
| build_version | synthetic_v0.1 |
| target_user_segment | new_user |
| session_scope | first_8_minutes |
| game_metric_model | mobile_liveops |
| metric_horizon | daily_retention |
| evidence_status | assumption_only |
| theory_status | design_hypothesis |

## Optimal Stimulation Fit

| field | value |
| --- | --- |
| stimulation_band | too_high |
| boredom_type | over_stimulation |
| player_resource_profile | new users with low rule knowledge |
| stimulus_profile | high UI information before the first fight |
| context_stimulation | first_session |
| design_direction | reduce_overload / add_familiar_anchor |
| risk_if_misdiagnosed | adding more events may make the first 3 minutes feel noisier |

## Diagnosis Summary

| formula_item | judgment | note |
| --- | --- | --- |
| CLP | high | early UI shows three currencies and two upgrade menus before the first fight |
| SF | medium | hits are visible but rewards have weak audio and no clear pickup moment |
| EB | medium | movement is responsive, but hitstop and camera emphasis are absent |
| AR | medium | art direction is coherent, but quiet gaps feel empty |
| MD/min | low | first meaningful build choice arrives after minute 4, but should not be moved before CLP is reduced |

建议顺序：先判窗口，再降噪，再提质，后调频。

## Experiment Hypothesis

如果我们先减少首局 UI 噪音、增加熟悉锚点，再把第一组 Build 选择前移到第 90 秒，玩家会更早形成“我正在构筑”的预测-反馈循环，首个 checkpoint 到达率和 D1 会方向性改善，同时不提高早退率和失败率。

## Variant Matrix

| variant_id | primary_lever | optimal_stimulation_target | concrete_change | impact_window | rollback |
| --- | --- | --- | --- | --- | --- |
| A_control | none | current | 当前版本 | first session | none |
| B_reduce_clp | CLP | reduce_overload / add_familiar_anchor | 首局隐藏非必要货币入口，只保留下一步目标和当前技能说明 | 0-180 sec | config off |
| C_raise_vertical_quality | SF / EB | improve_attributable_interest | 升级拾取增加音效、短镜头强调和轻量停顿 | 60-180 sec | asset/config off |
| D_tune_md_frequency | MD/min | add_semi_novelty_only_if_window_allows | 第 90 秒给第一次三选一 Build 方向，影响后两波敌人 | 90-240 sec | config off |

## Metric Plan

| layer | metric | target |
| --- | --- | --- |
| P1 | first_checkpoint_reach_rate | improve directionally |
| P1 | D1 | no decline, observe uplift |
| P2 | optimal_stimulation_band / boredom_type_mix | over_stimulation decreases |
| P2 | TTE_to_first_meaningful_decision | below 100 sec after CLP decreases |
| P2 | CLP proxy | tutorial hesitation decreases |
| negative | early_exit_rate / failure_rate / crash_rate | no spike |

## Decision Rules

- amplify: P1 improves, negative gates stay clean, and P2 supports the formula item changed.
- iterate: P2 improves but P1 is inconclusive.
- rollback: early exit, failure, crash, or confusion proxy spikes.
- kill: improvement comes from dark pattern pressure or misleading rewards.

## Instrumentation Notes

- Add `optimal_stimulation_window_observed` to mark `stimulation_band` and `boredom_type`.
- Keep `prediction_error_window_observed` and `blanket_coupling_signal` as design/QA labels, not player psychology claims.
