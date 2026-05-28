# OODA / VOI 状态模板

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
ooda_state:
  observe:
    user_goal:          # 用户真实目标
    context_used: []    # 已使用上下文、真源、记忆、资料
    surprising_signals: []  # 预期之外的信号
    tool_results: []
  orient:
    current_frame:      # 当前如何定性这个局
    old_frame_risk:     # 旧地图可能错在哪里
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
    hypothesis:         # 当前最值得下注验证的假设
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
