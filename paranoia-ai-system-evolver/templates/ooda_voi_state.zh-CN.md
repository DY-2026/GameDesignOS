# OODA / VOI 状态模板

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

  decision_gate:
    decision_id:
    owner:
    deadline:
    decision_question:
    options: []
    current_default_action:
    stakes: "low | medium | high | critical"
    reversibility: "reversible | costly_to_reverse | irreversible"
    boundary_status: "undefined | far | near | locked"
    information_mode: "decision_information | model_learning | information_consumption"

  observe:
    user_goal:
    context_used: []
    surprising_signals: []
    local_negative_evidence: []
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
      - uncertainty_id:
        item:
        current_belief_or_range:
        confidence: "low | medium | high"
        impact_if_wrong: "low | medium | high | critical"
        could_change_option_ranking: true
        action:

  voi:
    evpi_upper_bound:
    candidate_information_actions:
      - action_id:
        action:
        target_uncertainty:
        information_type: "perfect | partial_perfect | sample | proxy | expert | internal_record"
        expected_signals:
          - signal:
            posterior_update:
            action_if_seen:
        could_change_action: true
        reliability_and_bias:
        gross_value_estimate: "low | medium | high | quantified"
        evsi_estimate:
        acquisition_cost:
        latency_cost:
        attention_cost:
        privacy_or_contamination_cost:
        approximate_net_voi:
        conclusion: "do | skip | timebox_learning | ask_human"
    selected_probe:
      action_id:
      sample_or_evidence_gate:
      why_smallest_high_value_probe:
    stop_rule:
      stop_when: []
      fallback_action:

  decide:
    chosen_action:
    rejected_actions: []
    hypothesis:
    rejected_information_branches: []

  act:
    artifact_or_probe:
    permission_level: "A0 | A1 | A2 | A3 | A4"

  evaluate:
    result_check:
    process_check:
    outcome_score:
    observed_signal:
    prior:
    posterior:
    action_before_information:
    action_after_information:
    decision_changed: false
    stop_reason:
    triggered_obstacles: []
    if_then_actions: []
    failure_signals: []

  evolve:
    candidate_improvements: []
    enter_evolution_flow: false
```
