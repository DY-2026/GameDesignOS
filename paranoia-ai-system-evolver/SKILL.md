---
name: paranoia-ai-system-evolver
description: 用于升级 AI 系统、agent workflow、Codex skill、prompt、memory、RAG、tool routing、schema、eval set 或 feedback loop；也用于对研究、检索、测试和 AI 对话做 VOI 决策门审计。需要 WOOP 任务准入、决策对象、VOI/EVPI/EVSI、OODA、eval、Human Gate、versioning 与 rollback 的受控演化时使用。Use when controlled AI system evolution or a decision-oriented information audit is needed.
metadata:
  short-description: 用 WOOP、VOI 决策门、OODA 与 Evals 受控进化 AI 系统
---

# Paranoia AI System Evolver

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 核心立场

把 AI 系统演化当成受控系统设计，而不是神秘的自我改良；把信息获取当成决策投资，而不是越多越好的默认动作。

```text
WOOP 定义任务意图、验收结果、失败模式和恢复协议。
Decision Object 定义现在到底要决定什么，以及没有新信息时会做什么。
VOI 判断哪些信息、检索、追问、实验或 AI 分支值得付出成本。
Scenario VOI Adapter 定义不同使用场景里什么证据才真的会改变行动。
OODA 让 agent 用现实反馈刷新地图。
Evals 决定哪些改动值得留下。
Human Gate 防止一次有用突变污染长期系统。
Rollback 让每次提升都可逆。
```

VOI 的硬规则：真实、新鲜或结构清晰的信息不一定有价值。只有当合理信号可能改变行动、优先级、资源配置或停止条件时，它才具有当前决策价值。

## 何时使用

用于改动这些层：

- prompt、system instruction、memory、RAG、tool routing、workflow、schema、eval set、docs 或 Codex skill；
- agent feedback loop、trace format、release gate 与 rollback policy；
- 需要 model compression、causal mediator、WOOP harness protocol 或 total description cost 降低的 AI engineering 结构；
- 需要判断某次搜索、追问、读记忆、日志分析、实验或更多 AI 对话是否值得；
- 出现 FOMO、信息过载、分支爆炸、研究替代行动或高结构低价值输出时。

不要用它来合理化失控的模型权重改动、静默长期记忆写入、未经批准的全局 skill 安装，或没有 Human Gate 的生产影响行为。它也不是通用热点总结器；没有决策对象时，只允许有预算的探索或明确的信息消费。

## 快速流程

1. 定义任务和被改动的系统层：`prompt`、`memory`、`RAG`、`tool routing`、`workflow`、`eval`、`schema`、`docs` 或 `skill`。
2. 写轻量 `WOOP Task Card`：
   - `Wish / Intent Spec`：目标、输出物、范围与停止条件；
   - `Outcome / Evaluation Rubric`：验收标准与决策收益；
   - `Obstacle / Failure Pattern`：目标漂移、过度信任、上下文污染、工具滥用、FOMO 调研、选项爆炸、虚假确定性等内在失败模式；
   - `Plan / If-Then Protocol`：触发条件、判断者、恢复动作、重试、交还人或 rollback。
3. 在获取更多信息前定义 `Decision Object`：
   - 决策问题、owner、deadline；
   - 真实可选项；
   - `current_default_action`，即没有新信息时的行动；
   - stakes、reversibility 与 `boundary_status: undefined | far | near | locked`。
4. 建立 VOI 决策门：
   - 只保留会影响选项排序的不确定性；
   - 每轮最多提出 3 个 `candidate_information_actions` 候选信息行动；
   - 为可能信号预注册 `posterior_update` 与 `action_if_seen`；
   - 若所有信号都不会改变行动，停止调研或标记为 `model_learning` / `information_consumption`；
   - 用 EVPI 作为价值上界，用 EVSI 判断具体样本、实验或探针；
   - 扣除获取、延迟、注意力、隐私、污染和实施风险成本；
   - 选择净价值最高的最小探针，并写停止规则。
5. 选择 `Scenario VOI Adapter`，按具体使用场景定义有效证据：
   - `skill_evolution`：看真实 trace、行为 eval、负迁移、rollback，而不是一次漂亮案例；
   - `game_direction`：看玩家承诺、核心循环、题材解释规则、生产风险和最小原型信号；
   - `experience_diagnosis`：看 evidence_id、issue priority、修复动作和下一轮验证是否改变；
   - `source_curation`：看材料是否改变入库、分类、沉淀或拒绝，而不是只看内容新鲜；
   - `content_decision`：看选题、角度、标题承诺、论证主线和发布判断是否改变；
   - `platform_fact`：看当前一手来源、实际平台状态、兼容策略和时效边界；
   - `high_risk_action`：看是否降低不可逆错误，并默认进入 Human Gate；
   - `ai_branch_management`：看分支是否改变下一探针，不能改变行动的分支应归档或关闭。
6. 显式写出 operating model：
   - compression：什么短模型能解释多数真实案例；
   - causality：哪些 mediator 把输入连接到结果；
   - control points：agent、workflow 或 human 能干预哪个 mediator；
   - cost：core model、routing、state、validation、exception、recovery 的成本在哪里累积。
7. 维护紧凑 OODA 状态：
   - Observe：目标、上下文、证据、惊讶信号、触发的 Obstacle；
   - Orient：当前框架、用户模型、领域模型、决策边界、不确定性地图；
   - Decide：选择动作、拒绝动作、VOI 理由与停止条件；
   - Act：artifact、tool call、最小探针或 test；
   - Evaluate：用 Outcome 打分，记录先验—信号—后验—行动变化。
8. 分离 task OODA 和 meta OODA。任务循环完成当前工作；元循环只提出未来系统可考虑的 `candidate` 改动。
9. 每个演化改动保持 `candidate`，直到证据、行为 eval、必要审批和 rollback 都存在。
10. 当目标层是 `skill`，回放代表性任务，检查是否减少低 VOI 分支、是否保留具体负反馈、是否出现更啰嗦、更慢或误触发的负迁移。
11. 满足任一条件即停止继续获取信息：行动对合理信号已稳健、边际 VOI 不高于边际成本、样本门达到、deadline 到达、剩余不确定性不改变行动，或 Human Gate 已承诺执行。

## 按需读取

- 完整 VOI、EVPI、EVPPI、EVSI、决策边界、AI 疲劳与反 AI 味规则：`references/value-of-information-playbook.zh-CN.md`；英文：`references/value-of-information-playbook.en.md`。
- WOOP 任务准入、执行监控和失败恢复：`references/woop-harness-protocol.zh-CN.md`；英文：`references/woop-harness-protocol.en.md`。
- VOI/OODA 系统演化闭环：`references/evolution-loop-playbook.zh-CN.md`；英文：`references/evolution-loop-playbook.en.md`。
- Model compression、causal mediator、control point 与 total description cost：`references/model-compression-playbook.zh-CN.md`；英文：`references/model-compression-playbook.en.md`。
- Eval、trace、versioning、promotion 与 rollback：`references/eval-versioning-playbook.zh-CN.md`；英文：`references/eval-versioning-playbook.en.md`。
- 可复制表单：
  - VOI 决策门：`templates/voi_decision_gate.md`、`templates/voi_decision_gate.zh-CN.md`、`templates/voi_decision_gate.en.md`；
  - OODA / VOI 状态：`templates/ooda_voi_state.md`、`templates/ooda_voi_state.zh-CN.md`、`templates/ooda_voi_state.en.md`；
  - 进化提案：`templates/evolution_proposal.md`、`templates/evolution_proposal.zh-CN.md`、`templates/evolution_proposal.en.md`。
- VOI 行为回归案例：`evals/voi-decision-gate-cases.md` 与 `evals/voi-decision-gate-cases.en.md`。

## Human Gate 默认项

执行以下动作前必须询问人：

- 写入长期记忆；
- 安装或替换全局 skill；
- 改动生产策略、发布行为、真实账号、资金或用户可见系统；
- 把生成内容或 workflow mutation 从 `candidate` 提升为当前规则；
- 删除、镜像、批量移动或覆盖项目工作区；
- 在高风险决策中用定性 VOI 评分替代真实损益模型。

## 输出契约

结束时说明：

- 当前要支持的决策、选项和默认行动；
- 决策边界与最高价值不确定性；
- 使用的场景 VOI Adapter、有效证据标准和最小探针；
- 选择或拒绝了哪些信息行动，以及信号如何改变行动；
- 何时停止继续调研；
- 改了什么；
- WOOP 如何落到结果；
- 哪些 eval 或检查已经运行；
- 哪些仍然是 `candidate`；
- 哪些需要 Human Gate；
- 如何 rollback。
