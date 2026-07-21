# UL（Uncertainty Ladder，不确定性阶梯）工程协议

> Copyright (c) 2026 @Paranoia. All rights reserved.

## 1. 目的

UL 是 Uncertainty Ladder（不确定性阶梯）的统一缩写。它不是另一套学习口号，而是 AI 系统演化的实验环境设计协议。它解决一个现有 VOI / OODA 闭环没有单独解决的问题：下一轮验证应当释放多少不确定性，才能既接近真实世界，又保留失败的可归因性。

核心循环：

```text
建立模型
-> 拆分动作
-> 受控组合
-> 暴露失败
-> 诊断瓶颈
-> 针对训练
-> 增加复杂度
-> 迁移验证
-> 更新模型
```

对 AI 工程而言，“训练”包括 prompt、context、tool routing、memory、workflow、schema、eval、agent 协作和权限设计的可逆修改，不等同于修改模型权重。

## 2. 与现有控制层的关系

| 控制层 | 回答的问题 |
| --- | --- |
| Intent Work Order / WOOP | 要改变什么现实，怎样算完成，失败后怎样恢复？ |
| Decision Object / VOI | 当前要决定什么，哪个未知最值得消除？ |
| UL | 下一轮释放哪些未知、保留哪些支架，怎样让失败可归因？ |
| OODA | 这一轮如何观察、定向、决定、行动和更新？ |
| Eval | 这一层是否通过，是否出现负迁移，能否升级？ |
| RJR-AI / Human Gate | AI 能自治到哪里，哪些真实后果必须由人批准？ |

VOI 选目标不确定性，UL 控制暴露剂量。不要把“高 VOI”误解成“立刻在完整生产环境中测试”。

## 3. 阶梯不是单一难度分数

真实 AI 系统至少有六类不确定性：

- `input_novelty`：输入分布、任务类型和边界样本的新颖度；
- `context_ambiguity`：上下文缺失、冲突和意图模糊程度；
- `tool_environment_variability`：工具、网络、文件、接口和运行环境变化；
- `coordination_variability`：多 agent、人机协作和交接的不稳定性；
- `authority_and_consequence`：自主权限、可逆性和真实后果；
- `evaluation_ambiguity`：验收标准、反馈延迟和结果噪声。

因此阶梯应记录一个暴露向量，而不是伪装成精确的总分。每轮默认只释放一个主要变量；若同时释放两个，必须说明为什么仍能归因。`authority_and_consequence` 不能因为其他维度通过就自动升级。

## 4. 六个工程阶段

### UL-L0：建立最小世界模型

建立足以开始行动的 source contract：目标对象、基础规则、因果链、可观察信号、合格行动、已知失败和权限边界。

通过证据：模型能解释代表性样本，能生成至少一个可证伪预测，并明确 `needs_more_evidence`。只有术语总结不算通过。

### UL-L1：隔离变量，验证基础动作

把完整能力拆成可单独观察的原子行为，例如：正确路由、抽取约束、调用一个工具、写一个 schema、识别 Human Gate、停止低 VOI 调研。

通过证据：主要变量只有一个，输入和验收固定，失败能定位到具体动作。单元测试通过只证明该动作在当前夹具中成立。

### UL-L2：受控组合

把若干已通过的动作接入一条短链，例如“识别意图 -> 选择工具 -> 生成候选 -> 验证 -> 回滚”。保留固定输入、明确范围、低后果、可重复和可观察支架。

通过证据：链路在代表性受控样本中稳定，且能分辨是路由、执行、验证还是状态传递失败。

### UL-L3：暴露失败并诊断瓶颈

主动加入一个高 VOI 扰动，让系统在低代价环境中暴露失效边界。失败必须压缩为主要瓶颈假设，而不是归因于“模型不行”或“任务太复杂”。

```text
observed_failure
-> candidate_bottlenecks
-> ablation_or_counterfactual
-> primary_bottleneck
-> targeted_intervention
```

若无法区分两个以上主要解释，标记 `confounded`，退回更受控环境；不要在混杂失败上叠加永久规则。

### UL-L4：逐步释放真实不确定性

逐轮移除支架：固定样例、完整上下文、标准答案、人工监督、无限重试、稳定工具、低后果环境。每轮记录新增暴露、仍保留的支架、失败成本和回退条件。

通过证据：能力在新的暴露向量下仍成立，或者失败能产生可执行的瓶颈更新。真实用户、生产写入、发布、资金、权限和长期记忆仍受 Human Gate 约束。

### UL-L5：迁移与稳健性验证

验证能力是否只记住夹具：

- 近迁移：相似输入或相似工具变化；
- 中迁移：结构相同、表面不同的任务或项目；
- 远迁移：跨领域复用底层控制原则。

至少要有一个正迁移样本和一个反例/负迁移样本。远迁移失败不必否定局部能力，但必须缩小适用范围。

## 5. 最小状态契约

```yaml
ul_state:
  schema_version: "1.0.0"
  ul_id: "UL-YYYYMMDD-001"
  status: "candidate | shadow | warn | enforce"
  target_capability: ""
  decision_ref: null
  voi_gate_ref: null
  current_rung: "UL-L0 | UL-L1 | UL-L2 | UL-L3 | UL-L4 | UL-L5"
  world_model_ref: null
  uncertainty_exposure:
    input_novelty: "controlled | partial | real"
    context_ambiguity: "controlled | partial | real"
    tool_environment_variability: "controlled | partial | real"
    coordination_variability: "controlled | partial | real"
    authority_and_consequence: "sandbox | reversible | human_gated_real"
    evaluation_ambiguity: "controlled | partial | real"
  released_this_round: []
  held_constant: []
  scaffolds_present: []
  consequence_budget: ""
  preregistered_signals:
    pass: []
    fail: []
    confounded: []
    stop: []
  attribution_gate:
    observable_failure: null
    candidate_bottlenecks: []
    discriminating_probe: null
    primary_bottleneck: null
    attribution_confidence: "not_tested | low | medium | high | confounded"
    evidence_refs: []
  targeted_intervention: null
  same_rung_replay: []
  graduation_evidence: []
  transfer_checks:
    near: []
    medium: []
    far: []
    negative_transfer: []
  next_uncertainty_to_release: null
  fallback_rung: null
  rollback: ""
  stop_rule: ""
  human_gate:
    required: false
    reason: ""
```

## 6. 一轮运行协议

1. 从 Decision Object 和 VOI Gate 选择一个会改变行动的目标不确定性。
2. 声明当前 rung、暴露向量、支架和后果预算。
3. 只释放一个主要变量；若是组合测试，说明组合必要性和观测点。
4. 预注册成功、失败、混杂和停止信号。
5. 用 OODA 执行最小探针，保留 trace。
6. 若成功，先做同层复现，再升级一个维度；不要一次跳到生产。
7. 若失败，用消融、对照或反事实区分瓶颈。
8. 只针对主瓶颈修改；修改后回放原样本和至少一个反例。
9. 进入 UL-L5 后，明确适用范围；迁移证据不足时保留 `candidate`。
10. 更新 world model、eval set、停止规则或 rollback；不把单次成功自动写成长效规则。

## 7. 升级门与回退门

允许升级必须同时满足：

- 当前层的主要动作稳定；
- 失败可观察，关键 trace 没有缺失；
- attribution 不是 `confounded`；
- 下一层只增加少数可描述的不确定性；
- 失败成本在预算内；
- rollback 已验证；
- 涉及真实后果时已完成 Human Gate。

出现以下任一情况就回退：

- 多个主要变量同时变化，无法解释结果；
- 只看到了最终好坏，没看到中介过程；
- 修复一个案例后代表性样本退化；
- eval 夹具通过，但陌生输入立即失效；
- 需要用更多文档和例外掩盖同一个瓶颈；
- 权限或后果升级超过当前授权。

## 8. 常见误用

- 把六阶段写成固定瀑布：真实运行允许在 UL-L2～UL-L4 之间往返。
- 把任务复杂度和真实后果绑在一起增加：可以先增加输入变化，不必同时开放生产写入。
- 用更多样本代替瓶颈诊断：重复同类失败不会自动产生归因。
- 把通过 benchmark 当作迁移完成：benchmark 可能只是固定分布内表现。
- 每次失败都加 prompt：若瓶颈在工具、状态、权限或验收，prompt 补丁只会抬高描述成本。
- 把“逐步放权”当作权限自动晋升：A3/A4 行为始终需要对应 Human Gate。

## 9. AI 工程示例

目标能力：agent 能在模糊请求中选择正确 skill 并完成可验证交付。

```text
UL-L0  建立 router、skill 边界、验收和 Human Gate 模型
UL-L1  分别测试意图识别、路由选择、reference 读取、验证调用
UL-L2  在固定请求集上组合完整短链
UL-L3  加入一个混淆意图，定位是 signal 权重还是边界定义失败
UL-L4  逐步加入缺失上下文、工具失败、跨项目差异和用户纠偏
UL-L5  换到表面不同但结构相同的 workflow 升级任务，并加入不应触发该 skill 的反例
```

只有当它在受控组合、瓶颈诊断和迁移反例上都成立，才能说“路由能力得到验证”；某个漂亮案例只能算候选证据。
