# 进化闭环 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. 系统定义

自我进化 AI 不等于模型权重失控地自己改自己。它指 AI 应用在稳定目标下持续改进外部系统：prompt、memory、retrieval、tool routing、workflow、schema、eval set 与 skill reference。

闭环：

```text
真实任务压力
-> WOOP Task Card
-> Decision Object
-> RJR-AI 剩余判断权授权门
-> VOI 决策门
-> 场景 VOI Adapter
-> 最小信息探针
-> UL：控制暴露剂量与可归因性
-> Orient-first OODA
-> 结果反馈
-> 候选改进
-> behavior eval
-> Human Gate
-> 版本化上线
-> rollback path
```

## 2. WOOP 任务准入

在进入 VOI/OODA 前，把任务转成 `WOOP Task Card`：

- Wish：任务目标、输出物、范围和停止条件；
- Outcome：验收画面、评价尺和决策收益；
- Obstacle：人机系统内在失败模式，而不是外部困难；
- Plan：失败出现时的 If-Then Protocol、判断者、重试或 Human Gate。

准入规则：Wish 不清楚先拆小；Outcome 不清楚不进入生产；Obstacle 不清楚降低自主性；Plan 不清楚不执行高风险或不可逆动作。

## 3. Decision Object

VOI 之前必须声明：

```yaml
decision:
  decision_question:
  options: []
  current_default_action:
  owner:
  deadline:
  stakes:
  reversibility:
  boundary_status: "undefined | far | near | locked"
```

没有默认行动，就无法判断信息是否改变行动。没有真实选项，就无法比较信息后的最优选择。没有截止时间，就容易把调研变成拖延。

## 4. RJR-AI：剩余判断权授权门

RJR-AI 不是新 agent，也不是让 AI 替代领导者。它是 Decision Object 和 VOI 之间的授权层，用来回答：

```text
哪些可以交给 AI 扩大可能性？
哪些必须由 Workflow 压缩混乱？
哪些可以交给 Eval 提供反馈？
哪些只能在权限系统内做可逆执行？
哪些经验可以进入知识库？
最后剩下的高耦合、低可逆、证据不足、必须下注的问题，谁拍板？
```

每个系统演化提案必须写出 `rjr_authority_gate`：

```yaml
rjr_authority_gate:
  residual_judgment: "人需要亲自拍板的方向性问题"
  coupling: "low | high"
  reversibility: "reversible | costly_to_reverse | irreversible"
  authority_level: "P0_read | P1_suggest | P2_draft | P3_reversible_execute | P4_approved_execute"
  delegation_matrix:
    ai: "read | suggest | draft | execute"
    workflow: "none | route | gate | orchestrate"
    eval: "none | sample_check | regression | acceptance_gate"
    automation: "none | reversible_only | approved_execution"
    human: "not_required | review | approve | decide"
```

默认分层：

| 类型 | 默认授权 |
| --- | --- |
| 低耦合、高可逆 | AI / automation 可执行，保留抽查 |
| 低耦合、低可逆 | AI 草稿，workflow / eval / 专家规则确认 |
| 高耦合、高可逆 | AI 多路探索，workflow 收束，eval 对比，人选优 |
| 高耦合、低可逆 | AI 只能辅助论证，必须 Human Gate |

RJR 的关键是减少人的低价值判断，而不是减少人的最终责任。若 `coupling: high` 且 `reversibility: irreversible | costly_to_reverse`，并且证据仍不足以稳定选择，输出必须显式保留 `residual_judgment`，不能把它包装成 AI 已经决定。

## 5. 稀缺资源

agent 必须把 token、时间、用户注意力、工具调用、上下文窗口、可信反馈、标注样本、金钱、信任额度和决策窗口当成稀缺资源。

AI 让生成信息变便宜，却可能让人的评估和收束成本上升。系统优化目标不是生成最多方案，而是在有限认知带宽内关闭低 VOI 分支。

## 6. VOI 决策门

完整方法见 `references/value-of-information-playbook.zh-CN.md`。快速门如下：

```text
1. 当前决策是什么？
2. 没有新信息时采取什么行动？
3. 哪些不确定性会改变选项排序？
4. 哪些具体信息行动能降低这些不确定性？
5. 每种可能信号会触发什么不同动作？
6. EVPI 上界和现实 EVSI 大约多大？
7. 获取、延迟、注意力、隐私与污染成本是多少？
8. 最小高价值探针和停止规则是什么？
```

通过通用 VOI 门后，再选择场景 VOI Adapter：`skill_evolution`、`game_direction`、`experience_diagnosis`、`source_curation`、`content_decision`、`platform_fact`、`high_risk_action` 或 `ai_branch_management`。场景 Adapter 只定义该领域的有效证据、弱证据、默认探针和领域停止规则，不能替代 Decision Object。

操作性近似：

```text
approx_net_voi
= P(action_switch)
× decision_delta
× reuse_or_scale
× reversibility_factor
- acquisition_cost
- latency_cost
- attention_cost
- risk_cost
- contamination_cost
```

这只是排序启发式。若所有合理信号都不会改变行动，则停止调研或标记为 `model_learning` / `information_consumption`。

四种默认行动：

| 不确定性 | 影响 | 行动 |
| --- | --- | --- |
| 高 | 高 | 设计最小 EVSI 探针或请人审批 |
| 高 | 低 | 用默认假设推进并记录风险 |
| 低 | 高 | 做轻量确认 |
| 低 | 低 | 直接行动 |

## 7. UL（Uncertainty Ladder）：控制下一轮暴露

VOI 负责选择最值得消除的未知，UL 负责决定下一轮释放多少未知。完整协议见 `references/uncertainty-ladder-protocol.zh-CN.md`。

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

六个工程阶段是 `UL-L0`、`UL-L1`、`UL-L2`、`UL-L3`、`UL-L4`、`UL-L5`。它不是固定瀑布，也不是单一难度分数；要分别记录输入新颖度、上下文歧义、工具环境、协作、权限与后果、验收歧义。

每轮默认只释放一个主要变量，并记录 `held_constant`、`scaffolds_present`、`consequence_budget` 与 `fallback_rung`。若失败不能通过消融、对照或反事实区分主要解释，标记 `confounded`，退回更受控环境；不要在混杂失败上叠加长期规则。

受控环境成功只能支持当前 rung。进入真实输入前要逐步移除支架；声称能力稳定前要有迁移与负迁移证据。权限、发布、资金、长期记忆和真实用户影响不随 rung 自动升级，仍由 RJR-AI / Human Gate 决定。

## 8. Orient-first OODA

Observe 抓取目标、证据、惊讶信号、失败、用户纠偏、成本、延迟和触发的 Obstacle。

Orient 刷新：

- 当前叙事和可能已过期的旧叙事；
- 决策边界是否移动；
- 哪个信号真正改变选项排序；
- 用户、领域和 operating model；
- WOOP Outcome 是否仍是正确评价尺；
- 已获得的信息属于决策、模型还是消费价值。

Decide 选择一个当前最值得下注的行动或探针，同时拒绝低 VOI 分支。

Act 产生 artifact、tool call、probe 或 test。若行动是信息获取，必须绑定 `target_uncertainty`、`expected_signals` 和 `action_if_seen`。

Evaluate 记录：

```text
prior -> observed signal -> posterior -> action_before -> action_after -> stop reason
```

## 9. 模型压缩 Gate

Orient 阶段检查当前系统模型：

- 模型是否太短，导致只盯终点、无法定位中介？
- 模型是否太长，导致路由、状态和例外补丁吞掉执行能力？
- 改动优化哪个中介变量？
- 中介是否可观察、可干预、可验证？
- 新增规则是否减少未来决策成本，还是制造更多待处理分支？
- 总描述成本是下降，还是把复杂度转移到别处？

```text
total_description_cost
= core_model_length
+ routing_rule_length
+ state_injection_length
+ validation_observation_length
+ exception_patch_length
+ failure_recovery_length
```

## 10. 任务循环与元循环

任务循环：

```text
Decision Object
-> VOI Gate
-> UL
-> smallest probe or direct action
-> result
-> Human Gate / stop
```

元循环：

```text
trace
-> repeated or high-impact failure
-> bottleneck attribution
-> mutation candidate
-> behavior eval
-> approval
-> promotion / rollback
```

永远不要让元循环从单个案例自动提升长期规则。一次输出看起来更完整，不代表它降低了决策错误或注意力成本。

## 11. 候选突变规则

系统改动只有满足以下条件才进入进化队列：

- 重复出现或高影响；
- 会改变系统决策或显著降低高影响风险；
- 可修复、可复用、有证据、可回滚；
- 新增复杂度低于预期收益；
- 有至少一个反例或负迁移检查；
- 当前 rung、暴露变量和失败归因清楚，受控通过没有被误报为迁移通过；
- 有停止条件，而不是永久增加研究步骤。

否则只保留为任务笔记、模型学习或消费记录。

## 12. AI 疲劳与反 AI 味 Gate

### AI 疲劳

```text
open_branches
-> map to decisions
-> keep action-changing branches
-> archive model-learning branches
-> close consumption branches
-> choose one next probe
```

不要让每个 AI 对话都成为一个永久待办。

### 反 AI 味

改写、总结和提案必须保留本地事实、负反馈、失败细节、来源、约束和行动影响。若文本只增加标题、结构和抽象概念，却没有增加决策边界、信号、成本或动作，它属于高结构低 VOI 输出。

## 13. 行动权限阶梯

| 等级 | 例子 | 默认规则 |
| --- | --- | --- |
| A0 | 分析、草稿、VOI 审计 | 可自动 |
| A1 | 只读调研、本地检查、日志采样 | 可自动，但记录目标决策与成本 |
| A2 | 文档、模板、候选 skill 文件、可回滚实验 | 可自动，但要备份、验证和停止规则 |
| A3 | 长期记忆、全局 skill 安装、生产策略 | 需要 Human Gate |
| A4 | 删除、发布、资金、真实用户影响 | 必须明确审批 |

## 14. 公开 Skill 包检查

- `SKILL.md` frontmatter `name` 与文件夹名一致；
- `agents/openai.yaml` 与 `SKILL.md` 一致；
- `SKILL.md` 轻量并路由到本 skill 的 references/templates；
- VOI 模板包含 decision、current_default_action、signal-to-action、cost 与 stop rule；
- 行为 eval 包含无决策 FOMO、决策边界、高价值负反馈、低价值重复调研和不可逆动作案例；
- 不确定性阶梯 eval 包含过早真实化、混杂失败、组合崩溃、迁移失败和权限不自动晋升；
- 参考文件是一层可达，不把一次性 rollout 塞入长期 reference；
- 版权、来源、公开/私有边界和 rollback 清楚；
- 最后扫描陈旧命名和旧项目措辞。

## 15. README 视觉资产 Gate

生成图只承载氛围、结构隐喻和识别度，不承载关键文字。关键流程必须另有 Markdown、表格或 Mermaid 版本；图片路径、alt text、水印、错字、品牌边界和体积均需检查。
