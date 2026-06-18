# 进化提案模板

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
proposal_id: "mutation-YYYYMMDD-001"
trigger: ""
target_layer: "prompt | memory | rag | tool | workflow | eval | schema | docs | skill"
affected_files: []

evidence:
  traces: []
  user_feedback: []
  failed_evals: []
  repeated_pattern: ""
  local_negative_evidence: []

change_summary: ""
expected_benefit: ""
risk: ""

woop_task_card:
  wish:
    intent_spec: ""
    output_artifact: ""
    scope_boundary: ""
    stop_condition: ""
  outcome:
    decision_value: ""
    acceptance_rubric: ["", "", ""]
  obstacle:
    failure_patterns:
      - pattern: ""
        trigger: ""
        severity: "low | medium | high"
  plan:
    if_then_protocols:
      - if: ""
        then: ""
        judge: "agent | user | validator | test | reviewer"
        next_step: "continue | retry | rewrite | verify | ask_human | rollback"

voi_decision_gate:
  assessment_id: "VOI-YYYYMMDD-001"
  information_mode: "decision_information | model_learning | information_consumption"
  decision:
    decision_id: "DEC-..."
    owner: ""
    deadline: ""
    decision_question: ""
    options: []
    current_default_action: ""
    stakes: "low | medium | high | critical"
    reversibility: "reversible | costly_to_reverse | irreversible"
    boundary_status: "undefined | far | near | locked"
  uncertainty_map:
    - uncertainty_id: "U-001"
      uncertainty: ""
      current_belief_or_range: ""
      confidence: "low | medium | high"
      impact_if_wrong: "low | medium | high | critical"
      could_change_option_ranking: true
  candidate_information_actions:
    - action_id: "INFO-001"
      action: ""
      target_uncertainty: "U-001"
      expected_signals:
        - signal: ""
          posterior_update: ""
          action_if_seen: ""
      could_change_action: true
      evpi_upper_bound: ""
      evsi_estimate: ""
      acquisition_cost: ""
      latency_cost: ""
      attention_cost: ""
      privacy_or_contamination_cost: ""
      approximate_net_voi: ""
      conclusion: "do | skip | timebox_learning | ask_human"
  selected_probe:
    action_id: "INFO-001"
    sample_or_evidence_gate: ""
  stop_rule:
    stop_when: []
    fallback_action: ""

model_audit:
  current_model: ""
  proposed_model: ""
  woop_compression:
    intent_spec:
    evaluation_rubric: []
    failure_patterns: []
    if_then_protocols: []
  causal_chain: []
  control_points: []
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

eval_plan:
  samples: []
  behavior_samples: []
  voi_behavior_checks:
    - "decision object and default action are explicit"
    - "signal-to-action mapping exists"
    - "low-VOI branches are closed"
    - "local negative evidence is preserved"
    - "stop rule prevents research theater"
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
