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
voi_reason:
  decision_changed_if_known: ""  # what decision this information or change would affect
  expected_value: "high | medium | low"
  cost: "high | medium | low"
  conclusion: "do | skip | ask_human"
eval_plan:
  samples: []
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
