# Project Workflow Governance Playbook

## 目标

`paranoia-ai-system-evolver` 在 GameDesignOS 项目里不是新的领域执行者，而是跨 workflow 的治理层。

它要让每条项目流程都能回答：

1. 本轮到底要改变什么现实？
2. 哪个决策会因为本轮工作而改变？
3. AI、workflow、eval、automation 和 human 的授权边界在哪里？
4. 中途有没有低 VOI 调研、分支爆炸、过度结构化、证据不足或范围漂移？
5. 交付前哪些承诺、发布、资金、权限或方向变更必须进入 Human Gate？
6. 失败后如何 rollback？
7. 哪些复盘经验只能先作为 candidate learning，不能直接晋升为长期规则？

## 不替代领域 Skill

领域 skill 仍然拥有主产出：

- `game-concept-architect` 负责概念、玩家承诺、核心循环和验证计划；
- `game-experience-analyzer` 负责样本边界、证据、问题卡和诊断；
- `game-experience-density-optimizer` 负责 ED 实验、指标、仪表盘和回滚规则；
- `game-design-proposal-writer` 负责面向决策者的 proposal、pitch、memo 或 vertical slice 文档；
- `game-design-source-curator` 和 `game-design-book-translator` 负责知识资产。

`paranoia-ai-system-evolver` 只做治理检查：意图、VOI、RJR-AI、漂移、Human Gate、rollback、复盘沉淀。

## workflow-run.governance

每条 workflow run 应保留一个 `workflow-run.governance` 区块：

```yaml
governance:
  evolver_required: true
  enforcement_mode: shadow
  status: pending
  intent_work_order_ref: null
  decision_ref: DEC-...
  voi_gate_ref: GATE-...
  rjr_authority_ref: null
  paranoia_review_ref: null
  human_gate_refs: []
  rollback_ref: null
  candidate_learning_refs: []
  retrospective_ref: null
```

字段含义：

- `intent_work_order_ref`：开工意图。说明要改变什么现实、谁验收、第一眼必须看懂什么、哪些不能牺牲、AI 可自治到哪里。
- `decision_ref`：本轮服务的 Decision Object。
- `voi_gate_ref`：本轮为什么值得继续获取信息、做实验或开分支。
- `rjr_authority_ref`：AI、workflow、eval、automation 和 human 的授权边界。
- `paranoia_review_ref`：中途或交付前的治理审查记录。
- `human_gate_refs`：必须由人拍板的承诺、发布、资金、权限、删除、范围锁定或方向变更。
- `rollback_ref`：失败或负信号出现时的收缩、撤回、改方向条件。
- `candidate_learning_refs`：可复用但尚未晋升的复盘规则。
- `retrospective_ref`：本轮结束后的复盘记录。

## 三个参与时刻

### 1. Intake Gate

触发条件：

- 用户给的是“帮我写、优化、分析、出图、做个方案”等指令单；
- 任务目标大、模糊、容易分支爆炸；
- 输出将影响项目方向、生产投入、对外承诺或长期规则。

动作：

- 写轻量 Intent Work Order；
- 建立 Decision Object 和 `current_default_action`；
- 如果只是普通领域任务，保持 governance 为 `shadow`，不要阻断领域 skill 开工。

### 2. Drift Gate

触发条件：

- agent 开始反复补资料却不能说明会改变什么行动；
- 输出越来越完整但越来越不服务验收者；
- 方案分支超过三个且没有 signal-to-action mapping；
- 领域 skill 正在替代人做高耦合、低可逆、证据不足的判断。

动作：

- 运行 VOI/RJR-AI 审查；
- 关闭低 VOI 分支；
- 把不可授权判断推回 Human Gate；
- 把产出重新压回最小可验收状态。

### 3. Delivery / Retrospective Gate

触发条件：

- 准备交付 proposal、实验结论、workflow 改动、router 改动、schema 改动或长期规则；
- 结果会进入公开仓库、长期 skill、自动化、真实账号、发布或资金动作；
- 本轮经验看起来值得复用。

动作：

- 检查第一眼验收点、不可牺牲项、unsupported claims 和 rollback；
- 记录 Human Gate；
- 复盘“哪些判断被验证、哪些仍不确定、下一轮最应该改什么”；
- 新增规则默认写成 `candidate`，按 `shadow -> warn -> enforce -> rollbackable` 推进。

## enforcement_mode

- `shadow`：只记录治理发现，不阻断领域流程。默认模式。
- `warn`：发现明显漂移、越界、低 VOI 或证据不足时提醒，但仍可由人继续。
- `enforce`：在 eval 证明稳定有效后，才允许阻断高风险或不合规路径。

任何从 `shadow` 晋升到 `warn` 或 `enforce` 的规则，都必须有代表性 eval、负迁移检查、Human Gate 和 rollback。

## 成功标准

一次 workflow governance review 成功，不是因为它产出更多文档，而是因为：

- 领域 skill 的主产出更聚焦；
- 低价值调研和分支减少；
- 验收者更快看懂当前结论；
- 证据边界、不可牺牲项和 rollback 更清楚；
- 高耦合低可逆判断没有被 agent 私自接管；
- 复盘沉淀进入 candidate learning，而不是直接污染长期规则。
