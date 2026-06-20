# GameDesignOS Contracts

`contracts/` 定义 GameDesignOS 的稳定产物形状、路由边界和 workspace 记忆结构。

目标不是让文档更漂亮，而是保证不同 skill、runtime 命令和长期项目记录能互相交接：证据能追到来源，实验能追到假设，承诺能追到 Human Gate，学习能追到复盘。

## 三层契约

### 1. Skill-Level Contracts

专家工作流之间交换这些结构化产物：

- player promise；
- validation plan；
- evidence index；
- issue card；
- ED handoff；
- router selection。

### 2. Decision / Information Contract

[`information-value-assessment.schema.json`](./information-value-assessment.schema.json) 定义跨工作流 VOI gate：

```text
Decision Object
-> current default action
-> boundary status
-> action-sensitive uncertainty
-> candidate information actions
-> signal-to-action mapping
-> EVPI / EVSI / total cost
-> selected smallest probe
-> stop rule
-> posterior and action update
```

它不要求每个项目都算出精确货币化 VOI；它要求决策结构、信息成本、信号到行动映射和停止规则可复查。

### 3. Workspace-Level Contracts

workspace 契约组织长期项目记录：

- project manifest；
- design-asset index；
- information-value assessment；
- decision log。

它们记录资产在哪里、由谁生成、来源状态是什么、依赖什么、是否经过人类接受，以及什么时候应该停止继续获取信息。

## Project-Ready v1 Contracts

v1.0 新增一等项目记忆对象：

- Decision Object；
- Assumption Registry；
- Evidence Ledger；
- Experiment Plan；
- Experiment Result；
- Learning Record；
- Gate Result；
- Workflow Run。

这些对象让真实项目可以回答：

```text
一个设计决定是怎么产生的？
基于什么证据？
验证过什么？
谁拍板？
结果如何？
以后还能不能复用？
```

## 默认生产路径

```text
Decision Object
  -> Assumption Registry
  -> VOI / Evidence / Scope / Experiment / Rollback Gate
  -> Experiment Plan
  -> Evidence Ledger
  -> Experiment Result
  -> Experiment Review
  -> Human Gate
  -> Decision accepted / rejected / superseded
  -> Retrospective
  -> Learning candidate
```

VOI gate 是横切层。它不强迫每个项目走完所有 skill，但会阻止“没有决策对象的信息获取”伪装成项目推进。

## 路由边界

| 情况 | 路由 | 稳定输出 |
| --- | --- | --- |
| 研究冲动、FOMO、信息过载、不知道该测什么 | VOI audit / `paranoia-ai-system-evolver` | information-value-assessment、决策 brief、stop rule |
| 一句话创意，没有核心循环或玩家承诺 | `game-concept-architect` | player-promise-contract、validation-plan |
| 截图、录屏、PV、商店页、原型样本 | `game-experience-analyzer` | evidence-index、issue-card、ed-handoff |
| 留存、节奏、反馈、具身感、氛围感、认知负荷实验 | `game-experience-density-optimizer` | weekly ED experiment、instrumentation、dashboard、decision rules |
| 已有概念、证据、实验和约束，需要成案 | `game-design-proposal-writer` | proposal、pitch、decision memo、vertical-slice document |
| skill、schema、eval、router、workflow、promotion 或 rollback 改动 | `paranoia-ai-system-evolver` | evolution proposal、VOI decision gate、OODA state、eval plan |
| 设计资料策展 | `game-design-source-curator` | source notes、reference boundary、knowledge entry |
| 设计书籍翻译 | `game-design-book-translator` | 翻译或润色后的参考材料 |

## Workspace 协作规则

workspace-aware host 应该：

1. 读取 `game.designos.yaml`；
2. 检查 accepted decision 和 supersession 链；
3. 广泛调研前声明 Decision Object 和 current default action；
4. 把边界分为 `undefined`、`far`、`near`、`locked`；
5. 每轮 VOI 最多生成三个 candidate information actions；
6. 要求 signal-to-action mapping 和 stop rule；
7. 通过 design-asset index 解析资产路径；
8. 保留负反馈和来源边界；
9. 把新产物保存到生命周期目录；
10. 更新 upstream/downstream refs、VOI outcome 和 decision log；
11. 在改变项目承诺前停到 Human Gate。

## Schema 列表

### Skill-Level

- [`player-promise-contract.schema.json`](./player-promise-contract.schema.json)
- [`validation-plan.schema.json`](./validation-plan.schema.json)
- [`evidence-index.schema.json`](./evidence-index.schema.json)
- [`issue-card.schema.json`](./issue-card.schema.json)
- [`ed-handoff.schema.json`](./ed-handoff.schema.json)
- [`router.yaml`](./router.yaml)

### Decision / Information

- [`information-value-assessment.schema.json`](./information-value-assessment.schema.json)

### Workspace-Level

- [`project-workspace.schema.json`](./project-workspace.schema.json)
- [`design-asset-index.schema.json`](./design-asset-index.schema.json)
- [`decision-log.schema.json`](./decision-log.schema.json)

### Project-Ready v1

- [`decision.schema.json`](./decision.schema.json)
- [`assumption-registry.schema.json`](./assumption-registry.schema.json)
- [`evidence-ledger.schema.json`](./evidence-ledger.schema.json)
- [`experiment-plan.schema.json`](./experiment-plan.schema.json)
- [`experiment-result.schema.json`](./experiment-result.schema.json)
- [`learning-record.schema.json`](./learning-record.schema.json)
- [`gate-result.schema.json`](./gate-result.schema.json)
- [`workflow-run.schema.json`](./workflow-run.schema.json)

## 公私边界

Contracts 不应包含真实私有项目示例。公开示例只能使用 synthetic、public、cleared 或明确 `needs_review` 的材料。

VOI 不会因为决策重要就自动合理化敏感数据收集；隐私、污染、同意、发布风险和误用风险都属于 information cost。
