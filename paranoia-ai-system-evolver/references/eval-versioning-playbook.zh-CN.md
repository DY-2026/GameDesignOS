# Eval 与版本管理 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Eval 表面

至少评估三件事：

| 表面 | 问题 |
| --- | --- |
| 结果 | 输出是否真正解决了任务？ |
| 过程 | agent 是否正确使用 VOI、工具、记忆和验证？ |
| 进化 | 候选系统突变是否让未来任务更好，同时没有显著抬高风险？ |

## 2. Trace 最小字段

每个候选改进都必须保留足够证据，让后来的人能重建它为什么存在：

```yaml
trace_summary:
  task_id:
  user_goal:
  context_used:
  tool_calls:
  uncertainties:
  cost:
  result:
  feedback:
  failure_signals:
  candidate_improvements:
```

## 3. 突变提案

使用这个结构：

```yaml
proposal_id:
trigger:
evidence:
target_layer: prompt | memory | rag | tool | workflow | eval | schema | docs | skill
change_summary:
expected_benefit:
risk:
eval_plan:
human_gate:
rollback:
status: candidate
```

## 4. 分层最低 Eval

| 层级 | 最低检查 |
| --- | --- |
| prompt | 回放代表任务，对比指令遵循和风格匹配 |
| memory | 要有证据、置信度、适用范围、过期机制，并至少做一次反例检查 |
| RAG | 检查来源质量、召回精度、过期风险和引用行为 |
| tool routing | 检查工具使用是否正确、过早、过晚或缺失 |
| workflow | 检查 source contract 与 output gate 是否完整 |
| schema | 验证结构可机器解析，并覆盖边界样本 |
| skill | 检查 frontmatter、metadata、引用路径、模板可用性、陈旧措辞、真实调用场景和行为回归 |
| README visual | 检查图片路径、alt text、无水印、无误导文字、关键流程有文本版本 |

## 5. Skill Package 回归清单

改 skill 包时，至少跑这些检查：

```text
frontmatter name == folder name
agents/openai.yaml default_prompt uses the same skill name
all referenced files exist
templates are non-empty and copy-paste usable
root README is human-facing
SKILL.md is agent-facing and lightweight
no stale old name remains in public entrypoints
copyright/provenance is explicit
```

### Skill 行为回归门

结构检查只能证明 skill 可安装，不能证明它让真实任务变好。`target_layer: skill` 的候选突变必须补一层行为证据：

- 选择 2-3 个来自真实任务或高频场景的 `behavior_samples`，写清输入、期望行为和失败信号。
- 对比改动前后；如果旧版本不可运行，至少对照当前 `SKILL.md` 声称的输出契约。
- 检查是否出现负迁移：更啰嗦、更慢、误触发、跳过 VOI、忽视证据、破坏既有高价值场景。
- 若行为没有变好，只能保留为 `candidate` 或失败样本；不要因为结构更完整就提升为当前规则。
- 若行为变好但描述成本明显上升，回到模型压缩 Gate，判断收益是否覆盖新增复杂度。

### MDL 回归 Gate

候选改动可能改善局部结果，却让整个系统更难描述。提升前必须对比 `before_description_cost` 和 `after_description_cost` 的七项成本：

- `core_model_length`
- `data_patch_length`
- `routing_rule_length`
- `state_injection_length`
- `validation_observation_length`
- `exception_patch_length`
- `failure_recovery_length`

如果改动只是把复杂度从 prompt/context 挪到 routing、state、validation、exception patches 或 recovery，不要提升为长期规则。除非 eval 证据证明质量收益足以覆盖新增描述成本，否则保持 `candidate`。

### Trust Gate vNext

重大建议和会改变行为的 gate，在提升前必须同时验证证据和遗漏：

- Assertion Evidence Ledger：关键断言必须标记为 `verified_fact`、`tool_observation`、`inference_judgment`、`unverified_assumption` 或 `human_confirmation_needed`。
- Missing-Alternative Check：给出重要替代方案、未选择原因和遗漏风险，再推荐单一路径。
- Subagent Loss Audit：当子 agent 输出或长上下文被压缩时，记录被丢弃、变弱或未检查的高价值信息。
- Code-Deterministic First：确定性 routing、schema、validator、retry、rollback 和 gate 逻辑优先于 LLM 判断；LLM 只处理模糊语义、权衡和综合。
- Shadow-First Interceptor Policy：UAV 检查、路由、票据、记忆写入、重试、阻断 hook 或 trust gate 的变更，按 `off -> shadow -> warn -> enforce -> rollbackable` 推进。

## 6. 版本管理

每个被接受的突变都需要：

- version id
- 改动文件
- 改动理由
- eval 证据
- 风险
- 回滚路径
- 提升日期

被拒绝的突变在有复盘价值时，应保留为可搜索的失败样本。

## 7. 提升与回滚

以下情况不得提升为当前规则：

- 缺少 eval
- 高价值任务出现回退
- 复杂度增加但质量没有提升
- Human Gate 尚未完成
- 回滚方案不清楚

回滚应恢复上一个 prompt、memory 记录、skill 版本、workflow 文档、schema 或 eval 规则，不得触碰无关项目状态。
