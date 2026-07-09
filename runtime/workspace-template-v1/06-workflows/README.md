# 06-workflows

## Governance

每条 workflow run 都应保留 `governance` 区块，让 `paranoia-ai-system-evolver` 作为流程治理层参与：

- `intent_work_order_ref`：本轮要改变什么现实、谁验收、哪些边界不能牺牲；
- `decision_ref` / `voi_gate_ref`：本轮信息或实验服务哪个决策，以及为什么值得继续；
- `rjr_authority_ref`：AI、workflow、eval、automation 和 human 的授权边界；
- `paranoia_review_ref`：漂移、低 VOI 分支、过度结构化、证据不足或越界风险；
- `human_gate_refs`：需要人拍板的承诺、发布、资金、权限或方向变更；
- `rollback_ref`：失败后如何收缩、撤回或改方向；
- `candidate_learning_refs`：复盘后可复用但尚未晋升的规则。

默认 `enforcement_mode` 是 `shadow`。只有当 eval 证明检查点稳定改善流程和产出时，才升级为 `warn` 或 `enforce`。

这里保存工作流运行记录。

workflow 的目标不是自动替你完成所有步骤，而是指出当前卡在哪一步、缺哪个资产、下一步最小动作是什么。
