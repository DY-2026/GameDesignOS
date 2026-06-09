---
case_type: synthetic_example
source_status: synthetic
contains_private_project_info: false
license_status: original_synthetic_public_example
intended_use: public_repo_example
---

# Synthetic Hybrid Conflict Review

## Case Boundary

| field | value |
| --- | --- |
| output_mode | review_and_decide |
| case_visibility | synthetic_case |
| game_name | Star Bazaar Chronicles |
| build_version | synthetic_event_v1 |
| target_user_segment | mixed new and existing players |
| game_metric_model | hybrid |
| metric_horizon | hybrid_split |
| evidence_level | L5_ab_result |
| evidence_status | measured_evidence |
| theory_status | design_hypothesis |

Observed conflict: event D7 improved, but main story checkpoint completion fell and refund-risk comments increased.

## Review Order

1. Data quality gate: split by `client_version`, `channel`, `new_user`, `returning_user`, `existing_user`.
2. Negative gate: check refund-risk comments, early story exit, failure rate, fatigue complaints, economy disturbance.
3. P1 split: liveops P1 and total-journey P1 are separate. D7 alone cannot declare success.
4. P2 explanation: use ED proxy, CLP, SF, MD/min, and optimal stimulation fit to identify the conflict.
5. Decision: choose `iterate` or `rollback`, not `amplify`.

## Diagnosis

| field | value |
| --- | --- |
| liveops_signal | D7 improved for existing players |
| total_journey_signal | main story completion decreased for new players |
| likely_formula_conflict | event MD/min increased, but CLP and attention diversion harmed story progression |
| optimal_stimulation_risk | uneven |
| unsupported_claim | cannot declare overall success from D7 alone |

## Decision

| decision | rule |
| --- | --- |
| amplify | not allowed while story P1 and refund-risk gates are harmed |
| iterate | split event prompts away from first-story chapter and reduce CLP for new players |
| rollback | if story completion and refund-risk do not recover after segmentation |
| kill | if improvement depends on coercive red dots, misleading reward pressure, or unskippable event friction |

## Next Experiment

| variant_id | primary_lever | concrete_change | owner | rollback |
| --- | --- | --- | --- | --- |
| A_control | none | current event routing | design/data | none |
| B_segmented_event_prompt | CLP | hide event pressure until first story checkpoint for new players | design/ui/client | config off |
| C_existing_player_rehook | anti_habituation | keep event rehook only for existing players with a familiar-anchor recap and one new combinatorial rule | liveops/system | config off |

Required events: `variant_assigned`, `session_started`, `journey_checkpoint_reached`, `daily_return_observed`, `cognitive_load_signal`, `anti_habituation_signal`, `session_ended`.
