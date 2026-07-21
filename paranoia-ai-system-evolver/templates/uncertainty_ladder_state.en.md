# UL State Template

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
ul_state:
  schema_version: "1.0.0"
  ul_id: "UL-YYYYMMDD-001"
  target_capability: ""
  decision_ref: ""
  voi_gate_ref: ""
  current_rung: "UL-L0 | UL-L1 | UL-L2 | UL-L3 | UL-L4 | UL-L5"
  world_model_ref: ""
  uncertainty_exposure:
    input_novelty: "controlled | partial | real"
    context_ambiguity: "controlled | partial | real"
    tool_environment_variability: "controlled | partial | real"
    coordination_variability: "controlled | partial | real"
    authority_and_consequence: "sandbox | reversible | human_gated_real"
    evaluation_ambiguity: "controlled | partial | real"
  released_this_round: []
  held_constant: []
  scaffolds_present: []
  consequence_budget: ""
  preregistered_signals:
    pass: []
    fail: []
    confounded: []
    stop: []
  attribution_gate:
    observable_failure: ""
    candidate_bottlenecks: []
    discriminating_probe: ""
    primary_bottleneck: ""
    attribution_confidence: "not_tested | low | medium | high | confounded"
    evidence_refs: []
  targeted_intervention: ""
  same_rung_replay: []
  graduation_evidence: []
  transfer_checks:
    near: []
    medium: []
    far: []
    negative_transfer: []
  next_uncertainty_to_release: ""
  fallback_rung: ""
  rollback: ""
  stop_rule: ""
  human_gate:
    required: false
    reason: ""
  status: "candidate | shadow | warn | enforce"
```
