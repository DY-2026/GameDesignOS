# Evolution Proposal Template

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
proposal_id: "mutation-YYYYMMDD-001"
trigger: ""          # repeated failure, high-impact feedback, tool error, style rework, etc.
target_layer: "prompt | memory | rag | tool | workflow | eval | schema | docs | skill"
affected_files: []
evidence:
  traces: []         # reconstructable task traces
  user_feedback: []  # user feedback or revision evidence
  failed_evals: []   # failed samples or low-score evals
  repeated_pattern: ""
change_summary: ""
expected_benefit: ""
risk: ""
model_audit:
  current_model: ""   # current implicit model
  proposed_model: ""  # how the new model is shorter, steadier, and more verifiable
  causal_chain: []    # input -> mediator -> output
  control_points: []  # observable, intervenable, verifiable mediator nodes
  description_cost:
    core_model_length: "low | medium | high"
    data_patch_length: "low | medium | high"
    routing_rule_length: "low | medium | high"
    state_injection_length: "low | medium | high"
    validation_observation_length: "low | medium | high"
    exception_patch_length: "low | medium | high"
    failure_recovery_length: "low | medium | high"
  diagnosis: "underfit | overfit | missing_mediator | balanced"
  expected_cost_delta: ""
voi_reason:
  decision_changed_if_known: ""  # what decision this information or change would affect
  expected_value: "high | medium | low"
  cost: "high | medium | low"
  conclusion: "do | skip | ask_human"
eval_plan:
  samples: []
  behavior_samples: []  # for target_layer=skill: real/frequent invocation, expected behavior, failure signals
  graders: []
  regression_checks: []
acceptance_criteria: []
human_gate:
  required: true
  reason: ""
rollback:
  method: ""
  files_to_restore: []
status: "candidate"
```
