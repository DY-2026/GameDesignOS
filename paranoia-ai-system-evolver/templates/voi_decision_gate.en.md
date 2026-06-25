# VOI Decision Gate Template

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
voi_decision_gate:
  assessment_id: "VOI-YYYYMMDD-001"
  information_mode: "decision_information | model_learning | information_consumption"

  decision:
    decision_id: "DEC-..."
    owner: ""
    deadline: ""
    decision_question: ""
    options:
      - option_id: "A"
        action: ""
        expected_benefit: ""
        main_risk: ""
    current_default_action: ""
    stakes: "low | medium | high | critical"
    reversibility: "reversible | costly_to_reverse | irreversible"
    boundary_status: "undefined | far | near | locked"

  utility_model:
    objective: ""
    decision_delta_if_wrong: ""
    key_payoffs_or_losses: []
    assumptions: []

  scenario_voi:
    scenario: "skill_evolution | game_direction | experience_diagnosis | source_curation | content_decision | platform_fact | high_risk_action | ai_branch_management | other"
    action_that_must_change: ""
    valid_evidence: []
    weak_evidence: []
    preferred_probe: ""
    domain_stop_rule: ""
    human_gate: "not_required | required | already_committed"

  uncertainty_map:
    - uncertainty_id: "U-001"
      uncertainty: ""
      current_belief_or_range: ""
      confidence: "low | medium | high"
      impact_if_wrong: "low | medium | high | critical"
      affected_options: []
      observable: true
      controllable: false

  candidate_information_actions:
    - action_id: "INFO-001"
      action: ""
      target_uncertainty: "U-001"
      information_type: "perfect | partial_perfect | sample | proxy | expert | internal_record"
      expected_signals:
        - signal: ""
          posterior_update: ""
          action_if_seen: ""
      could_change_action: true
      reliability_and_bias: ""
      gross_value_estimate: "low | medium | high | quantified"
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
    why_smallest_high_value_probe: ""
    sample_or_evidence_gate: ""
    owner: ""
    due: ""

  stop_rule:
    stop_when:
      - "preferred action is robust across plausible signals"
      - "marginal VOI <= marginal information cost"
      - "sample/evidence gate is reached"
      - "deadline is reached"
      - "remaining uncertainty cannot change action"
    fallback_action: ""

  outcome:
    observed_signal: ""
    prior: ""
    posterior: ""
    action_before_information: ""
    action_after_information: ""
    decision_changed: false
    residual_uncertainty: []
    stop_reason: ""
    decision_log_ref: ""
```
