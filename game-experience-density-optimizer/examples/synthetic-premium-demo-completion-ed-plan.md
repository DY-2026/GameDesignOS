---
case_type: synthetic_example
source_status: synthetic
contains_private_project_info: false
license_status: original_synthetic_public_example
intended_use: public_repo_example
---

# Synthetic Premium Demo ED Experiment Plan

## Case Boundary

| field | value |
| --- | --- |
| output_mode | weekly_ab_plan |
| case_visibility | synthetic_case |
| game_name | Clockwork Ferry Demo |
| build_version | synthetic_v0.2 |
| target_user_segment | Steam demo new players |
| session_scope | first_20_minutes |
| game_metric_model | premium_single_player |
| metric_horizon | total_journey |
| evidence_level | L0_text_only |
| evidence_status | assumption_only |
| theory_status | design_hypothesis |

Unsupported claims: this example cannot claim real completion uplift without playtest or telemetry. D1/D7 are not assumed as P1 because the value promise is demo completion and total journey quality.

## Evidence Gate

| field | value |
| --- | --- |
| allowed_claims | hypothesis, low-cost experiment, telemetry needs |
| forbidden_claims | guaranteed completion uplift, D1/D7 as default P1 |
| confidence | low |
| missing_evidence | demo funnel, recording, checkpoint reach, exit reasons |
| confounder_risks | instrumentation_missing, player_segment_mix |

## Metric Horizon

| field | value |
| --- | --- |
| game_metric_model | premium_single_player |
| primary_time_horizon | total_journey |
| p1_metric_family | completion_progress |
| p1_metrics | demo_completion_rate, core_loop_reach_rate, total_effective_playtime |
| excluded_metrics | D1/D7, consecutive_login |

## Optimal Stimulation Fit

| field | value |
| --- | --- |
| band | unknown |
| boredom_type | mixed |
| suspected_risk | first 20 minutes may be too low in meaningful decisions but could also hide CLP from rules setup |
| design_direction | add_familiar_anchor before add_semi_novelty |

## Diagnosis Summary

| item | judgment | note |
| --- | --- | --- |
| CLP | medium/high | demo premise and three resources arrive before the first meaningful tradeoff |
| SF | medium | rewards are visible but not tied to the ferry route decision |
| EB | low relevance | no strong action-feel evidence from text |
| AR | medium | atmosphere supports the promise, but waiting gaps need state change |
| MD/min | low after CLP is reduced | first route decision lands too late for a demo promise |

Primary lever: `CLP` for B, then `MD/min` only after readability is repaired.

## Variant Matrix

| variant_id | primary_lever | concrete_change | config_keys | owner | qa_checks | rollback |
| --- | --- | --- | --- | --- | --- | --- |
| A_control | none | current demo | none | design/data | baseline events fire | none |
| B_reduce_clp | CLP | hide advanced cargo rules until first route decision resolves | `demo_rules_reveal_stage` | design/ui/client | no missing tutorial path | config off |
| C_raise_vertical_quality | SF | after first route decision, show one clear downstream consequence in the town state | `route_consequence_preview` | design/narrative/audio | consequence is attributable | config off |
| D_tune_md_frequency | MD/min | move the first route tradeoff to minute 4 after B's familiar anchor | `first_tradeoff_time_sec` | design/level | no overload spike | config off |

## Instrumentation

Required events: `variant_assigned`, `session_started`, `meaningful_decision_made`, `choice_impact_observed`, `salient_feedback_fired`, `cognitive_load_signal`, `journey_checkpoint_reached`, `session_ended`.

## Decision Rules

- amplify: demo completion or core-loop reach improves, early exit does not move earlier, and CLP proxy improves.
- iterate: CLP improves but completion is inconclusive.
- observe: sample is too small or checkpoint coverage is incomplete.
- rollback: early exit, skip rate, confusion proxy, or negative review proxy worsens.
- kill: improvement relies on misleading countdowns, forced friction, or hidden skip removal.
