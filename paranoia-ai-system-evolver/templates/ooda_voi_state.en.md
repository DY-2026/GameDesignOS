# OODA / VOI State Template

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
ooda_state:
  woop:
    wish:
      intent_spec:
      output_artifact:
      scope_boundary:
      stop_condition:
    outcome:
      decision_value:
      acceptance_rubric: []
    obstacle:
      failure_patterns:
        - pattern:
          trigger:
          severity: "low | medium | high"
    plan:
      if_then_protocols:
        - if:
          then:
          judge:
          next_step: "continue | retry | rewrite | verify | ask_human | rollback"
  observe:
    user_goal:
    context_used: []
    surprising_signals: []
    tool_results: []
  orient:
    current_frame:
    old_frame_risk:
    domain_model:
    operating_model:
      core_model:
      mediator_chain: []
      control_points: []
      description_cost:
        core_model_length:
        data_patch_length:
        routing_rule_length:
        state_injection_length:
        validation_observation_length:
        exception_patch_length:
        failure_recovery_length:
    user_model:
    uncertainty_map:
      - item:
        confidence:
        impact:
        action:
  voi:
    candidate_information_actions:
      - action:
        could_change_decision: "high | medium | low"
        decision_delta: "high | medium | low"
        reuse_value: "high | medium | low"
        cost: "high | medium | low"
        risk: "high | medium | low"
        conclusion: "do | skip | ask_human"
  decide:
    chosen_action:
    rejected_actions: []
    hypothesis:
  act:
    artifact_or_probe:
    permission_level: "A0 | A1 | A2 | A3 | A4"
  evaluate:
    result_check:
    process_check:
    outcome_score:
    triggered_obstacles: []
    if_then_actions: []
    failure_signals: []
  evolve:
    candidate_improvements: []
    enter_evolution_flow: false
```
