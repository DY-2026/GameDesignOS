# 进化提案模板

> Copyright (c) 2026 @Paranoia. All rights reserved.

```yaml
proposal_id: "mutation-YYYYMMDD-001"
trigger: ""          # 触发原因：重复失败、高影响反馈、工具错误、风格返工等
evidence:
  traces: []         # 可追溯任务轨迹
  user_feedback: []  # 用户反馈或修改证据
  failed_evals: []   # 失败样本或低分 eval
  repeated_pattern: ""
target_layer: "prompt | memory | rag | tool | workflow | eval | schema | docs | skill"
change_summary: ""
expected_benefit: ""
risk: ""
voi_reason:
  decision_changed_if_known: ""  # 这条信息或改动会改变什么决策
  expected_value: "high | medium | low"
  cost: "high | medium | low"
  conclusion: "do | skip | ask_human"
eval_plan:
  samples: []
  graders: []
  regression_checks: []
human_gate:
  required: true
  reason: ""
rollback: ""
status: "candidate"
```
