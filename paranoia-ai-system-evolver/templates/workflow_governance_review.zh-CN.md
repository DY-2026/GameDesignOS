# workflow_governance_review

```yaml
workflow_governance_review:
  schema_version: 1.0.0
  workflow_id:
  run_id:
  reviewed_at:
  reviewer: paranoia-ai-system-evolver
  enforcement_mode: shadow
  status: pending

intake_intent:
  intent_work_order_ref:
  reality_to_change:
  parent_project_goal:
  desired_world_state:
  verifier_role:
  first_impression_must_understand:
  must_not_sacrifice: []
  ai_can_freely_change: []
  ai_must_not_touch: []

decision_and_voi:
  decision_ref:
  decision_question:
  current_default_action:
  boundary_status: undefined
  voi_gate_ref:
  candidate_information_actions: []
  rejected_information_actions: []
  stop_rule:

ul_control:
  ul_state_ref:
  current_rung: "UL-L0 | UL-L1 | UL-L2 | UL-L3 | UL-L4 | UL-L5"
  released_this_round: []
  held_constant: []
  attribution_confidence: "not_tested | low | medium | high | confounded"
  fallback_rung:
  transfer_status: "not_tested | partial | passed | failed"

rjr_authority:
  rjr_authority_ref:
  coupling:
  reversibility:
  authority_level:
  delegation_matrix:
    ai:
    workflow:
    eval:
    automation:
    human:
  residual_judgment:
  human_gate_trigger:

drift_review:
  paranoia_review_ref:
  branch_explosion_signals: []
  low_voi_research_signals: []
  over_structured_output_signals: []
  evidence_boundary_gaps: []
  scope_creep_signals: []
  corrective_action:

delivery_gate:
  acceptance_check:
  unsupported_claims: []
  human_gate_refs: []
  rollback_ref:
  rollback_trigger:
  blocked_actions: []

retrospective:
  retrospective_ref:
  original_intent:
  completion_level:
  validated_judgments: []
  remaining_uncertainties: []
  next_round_change:
  candidate_learning_refs: []
  rules_to_promote_later: []
  promotion_status: candidate
```

## 使用规则

- 默认 `enforcement_mode: shadow`，先记录不阻断。
- 只有 eval 证明检查点稳定改善流程和产出，才升级到 `warn` 或 `enforce`。
- 领域 skill 的主产出不在本模板里重写，只引用其资产。
- UL 为可选区块；普通领域任务不需要为了填表而启用。
- 任何真实账号、发布、资金、权限、删除、长期规则晋升，都必须进入 Human Gate。
