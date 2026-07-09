# Intent Work Order Template

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
intent_work_order:
  schema_version: "1.2.0"
  work_order_id: "IWO-YYYYMMDD-001"
  title: ""
  status: "draft | active | completed | blocked | candidate_learning"

  intent:
    reality_to_change: ""
    parent_project_goal: ""
    desired_world_state: ""

  acceptance:
    verifier_role: ""
    first_impression_must_understand: ""
    acceptance_criteria: []
    failure_signals_to_check_before_delivery: []

  boundaries:
    must_not_sacrifice: []
    ai_can_freely_change: []
    ai_must_not_touch: []
    cost_boundaries: []

  autonomy:
    authority_level: "P0_read | P1_suggest | P2_draft | P3_reversible_execute | P4_approved_execute"
    decision_principles_if_plan_breaks: []
    human_gate_triggers: []
    rollback_expectation: ""

  context_supply:
    known_context: []
    required_sources: []
    assumptions_to_mark: []
    evidence_boundaries: []

  loop_contract:
    allowed_tools_or_actions: []
    loop_steps: ["observe", "orient", "decide", "act", "evaluate"]
    stop_conditions: []

  retrospective_contract:
    original_intent: ""
    completion_state: ""
    verified_judgments: []
    uncertain_items: []
    next_change: ""
    reusable_rules: []
    prompts_acceptance_or_failure_signals_to_promote: []
    promotion_status: "candidate | validated | rejected"
```
