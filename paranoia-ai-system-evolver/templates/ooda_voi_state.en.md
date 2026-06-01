# OODA / VOI State Template

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
ooda_state:
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
      highest_cost_term:
      expected_cost_delta:
      complexity_displacement_risk:
      mdl_verdict:
    trust_gate_vnext:
      assertion_evidence_ledger:
        verified_facts: []
        tool_observations: []
        inference_judgments: []
        unverified_assumptions: []
        human_confirmation_needed: []
      missing_alternative_check:
        alternatives_considered: []
        rejected_reasons: []
        omission_risk:
      subagent_loss_audit:
        dropped_or_weakened_findings: []
        compression_loss_risk:
      shadow_first_interceptor_policy:
        release_mode: "off | shadow | warn | enforce"
        rollbackable: true
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
    failure_signals: []
  evolve:
    candidate_improvements: []
    enter_evolution_flow: false
```
