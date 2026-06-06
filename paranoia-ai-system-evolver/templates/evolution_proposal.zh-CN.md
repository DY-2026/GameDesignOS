# 进化提案模板

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

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
woop_task_card:
  wish:
    intent_spec: ""      # 真正要完成什么
    output_artifact: ""  # 交付物是什么
    scope_boundary: ""   # 到哪里为止，不做什么
    stop_condition: ""   # 何时停止或交还给人
  outcome:
    decision_value: ""   # 成功后帮助人做什么决策或动作
    acceptance_rubric:
      - ""
      - ""
      - ""
  obstacle:
    failure_patterns:
      - pattern: ""      # 人机系统内在失败模式
        trigger: ""      # 何时判断它出现
        severity: "low | medium | high"
  plan:
    if_then_protocols:
      - if: ""           # 触发条件
        then: ""         # 具体动作
        judge: ""        # agent | user | validator | test | reviewer
        next_step: "continue | retry | rewrite | verify | ask_human | rollback"
model_audit:
  current_model: ""   # 当前隐含模型
  proposed_model: ""  # 新模型如何更短、更稳、更可验证
  woop_compression:
    intent_spec:
    evaluation_rubric: []
    failure_patterns: []
    if_then_protocols: []
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
  behavior_samples: []  # target_layer=skill 时填写：真实/高频调用、期望行为、失败信号
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
