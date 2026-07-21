# workflow_governance_review

```yaml
workflow_governance_review:
  schema_version: 1.0.0
  workflow_id:
  run_id:
  reviewer: paranoia-ai-system-evolver
  enforcement_mode: shadow
  status: pending

intake_intent:
  intent_work_order_ref:
  reality_to_change:
  verifier_role:
  first_impression_must_understand:
  must_not_sacrifice: []
  ai_can_freely_change: []
  ai_must_not_touch: []

decision_and_voi:
  decision_ref:
  current_default_action:
  boundary_status:
  voi_gate_ref:
  stop_rule:

ul_control:
  ul_state_ref:
  current_rung: "UL-L0 | UL-L1 | UL-L2 | UL-L3 | UL-L4 | UL-L5"
  released_this_round: []
  held_constant: []
  attribution_confidence: "not_tested | low | medium | high | confounded"
  fallback_rung:
  transfer_status: "not_tested | partial | passed | failed"

rjr_authority:
  rjr_authority_ref:
  authority_level:
  residual_judgment:
  human_gate_trigger:

drift_review:
  paranoia_review_ref:
  branch_explosion_signals: []
  low_voi_research_signals: []
  over_structured_output_signals: []
  evidence_boundary_gaps: []
  corrective_action:

delivery_gate:
  human_gate_refs: []
  rollback_ref:
  blocked_actions: []

retrospective:
  retrospective_ref:
  candidate_learning_refs: []
  promotion_status: candidate
```
