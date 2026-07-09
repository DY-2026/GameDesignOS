# Project Workflow Governance Playbook

`paranoia-ai-system-evolver` 是 GameDesignOS 的跨 workflow 治理层，不替代领域 skill。

它检查：

- Intent Work Order：要改变什么现实、谁验收、哪些不能牺牲、AI 可自治到哪里；
- Decision Object / VOI：本轮服务哪个决策、默认行动是什么、哪些信息真的能改变行动；
- RJR-AI：AI、workflow、eval、automation 和 human 的授权边界；
- Drift Gate：低 VOI 调研、分支爆炸、过度结构化、证据不足或范围漂移；
- Human Gate / rollback：哪些承诺必须由人拍板，失败后如何撤回；
- Candidate Learning：复盘经验先保持 candidate，再按 `shadow -> warn -> enforce -> rollbackable` 晋升。

每条 `workflow-run.governance` 至少保留：

```yaml
evolver_required: true
enforcement_mode: shadow
status: pending
intent_work_order_ref: null
decision_ref: null
voi_gate_ref: null
rjr_authority_ref: null
paranoia_review_ref: null
human_gate_refs: []
rollback_ref: null
candidate_learning_refs: []
retrospective_ref: null
```

默认 `enforcement_mode` 是 `shadow`。只有代表性 eval 证明检查点稳定改善流程和产出，才升级到 `warn` 或 `enforce`。
