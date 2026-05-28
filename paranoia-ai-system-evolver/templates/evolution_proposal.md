# 进化提案模板

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
proposal_id: "mutation-YYYYMMDD-001"
trigger: ""          # 触发原因：重复失败、高影响反馈、工具错误、风格返工等
target_layer: "prompt | memory | rag | tool | workflow | eval | schema | docs | skill"
affected_files: []
evidence:
  traces: []         # 可追溯任务轨迹
  user_feedback: []  # 用户反馈或修改证据
  failed_evals: []   # 失败样本或低分 eval
  repeated_pattern: ""
change_summary: ""
expected_benefit: ""
risk: ""
model_audit:
  current_model: ""   # 当前隐含模型
  proposed_model: ""  # 新模型如何更短、更稳、更可验证
  causal_chain: []    # input -> mediator -> output
  control_points: []  # 可观察、可干预、可验证的中介节点
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
  decision_changed_if_known: ""  # 这条信息或改动会改变什么决策
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
