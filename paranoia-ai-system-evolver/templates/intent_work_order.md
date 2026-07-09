# 意图工作单模板

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

```yaml
intent_work_order:
  schema_version: "1.2.0"
  work_order_id: "IWO-YYYYMMDD-001"
  title: ""
  status: "draft | active | completed | blocked | candidate_learning"

  intent:
    reality_to_change: ""          # 我要改变什么现实？
    parent_project_goal: ""        # 服务于哪个更大的项目目标？
    desired_world_state: ""        # 完成后外部世界应该是什么状态？

  acceptance:
    verifier_role: ""              # 谁验收？
    first_impression_must_understand: ""  # 验收者第一眼必须看懂什么？
    acceptance_criteria:
      - ""
      - ""
      - ""
    failure_signals_to_check_before_delivery:
      - ""
      - ""
      - ""

  boundaries:
    must_not_sacrifice:
      - ""
    ai_can_freely_change:
      - ""
    ai_must_not_touch:
      - ""
    cost_boundaries:
      - ""

  autonomy:
    authority_level: "P0_read | P1_suggest | P2_draft | P3_reversible_execute | P4_approved_execute"
    decision_principles_if_plan_breaks:
      - ""
    human_gate_triggers:
      - "touches long-term memory"
      - "changes global skill or project rule"
      - "publishes, pays, deletes, overwrites, or changes real account permissions"
    rollback_expectation: ""

  context_supply:
    known_context:
      - ""
    required_sources:
      - ""
    assumptions_to_mark:
      - ""
    evidence_boundaries:
      - ""

  loop_contract:
    allowed_tools_or_actions:
      - ""
    loop_steps:
      - "observe"
      - "orient"
      - "decide"
      - "act"
      - "evaluate"
    stop_conditions:
      - ""

  woop_mapping:
    wish:
      intent_spec: ""
      output_artifact: ""
      scope_boundary: ""
      stop_condition: ""
    outcome:
      decision_value: ""
      acceptance_rubric: []
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

  retrospective_contract:
    original_intent: ""
    completion_state: ""
    verified_judgments:
      - ""
    uncertain_items:
      - ""
    next_change: ""
    reusable_rules:
      - ""
    prompts_acceptance_or_failure_signals_to_promote:
      - ""
    promotion_status: "candidate | validated | rejected"
```
