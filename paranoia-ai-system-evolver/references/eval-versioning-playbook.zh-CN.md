# Eval 与版本管理 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. Eval 表面

至少评估三件事：

| 表面 | 问题 |
| --- | --- |
| 结果 | 输出是否真正解决了任务？ |
| 过程 | agent 是否正确使用 WOOP 准入、Decision Object、VOI、工具、记忆和验证？ |
| 进化 | 候选系统突变是否让未来任务更好，同时没有显著抬高风险？ |

## 2. Trace 最小字段

每个候选改进都必须保留足够证据，让后来的人能重建它为什么存在：

```yaml
trace_summary:
  task_id:
  user_goal:
  woop_task_card:
  decision_object:
  voi_decision_gate:
  ul_state:
  context_used:
  tool_calls:
  uncertainties:
  cost:
  result:
  feedback:
  triggered_obstacles:
  if_then_actions:
  failure_signals:
  candidate_improvements:
```

## 3. 突变提案

```yaml
proposal_id:
trigger:
evidence:
target_layer: prompt | memory | rag | tool | workflow | eval | schema | docs | skill
change_summary:
expected_benefit:
risk:
woop_task_card:
voi_decision_gate:
ul_state:
eval_plan:
human_gate:
rollback:
status: candidate
```

## 4. 分层最低 Eval

| 层级 | 最低检查 |
| --- | --- |
| prompt | 回放代表任务，对比指令遵循、信息密度和行动收束 |
| memory | 要有证据、置信度、适用范围、过期机制，并至少做一次反例检查 |
| RAG | 检查来源质量、召回精度、过期风险、引用行为和检索是否会改变行动 |
| tool routing | 检查工具使用是否正确、过早、过晚、缺失或低 VOI |
| workflow | 检查 WOOP Task Card、Decision Object、source contract、不确定性暴露、output gate 与停止规则 |
| schema | 验证结构可机器解析，并覆盖边界样本 |
| skill | 检查 frontmatter、metadata、VOI/WOOP/不确定性阶梯 reference、引用路径、模板可用性、陈旧措辞、真实调用场景、迁移和行为回归 |
| README visual | 检查图片路径、alt text、无水印、无误导文字、关键流程有文本版本 |

## 5. Skill Package 回归清单

```text
frontmatter name == folder name
agents/openai.yaml default_prompt uses the same skill name
all referenced files exist
templates are non-empty and copy-paste usable
Decision Object and VOI stop-rule fields exist when the skill can trigger research or tools
WOOP Task Card fields exist when the skill controls task admission or recovery
UL State fields expose the current rung, released variables, attribution, transfer, and fallback
root README is human-facing
SKILL.md is agent-facing and lightweight
no stale old name remains in public entrypoints
copyright/provenance is explicit
```

### Skill 行为回归门

结构检查只能证明 skill 可安装，不能证明它让真实任务变好。`target_layer: skill` 的候选突变必须补一层行为证据：

- 选择 2-3 个来自真实任务或高频场景的 `behavior_samples`，写清输入、期望行为和失败信号。
- 对比改动前后；如果旧版本不可运行，至少对照当前 `SKILL.md` 声称的输出契约。
- 检查 WOOP 是否改善了任务准入、Outcome 验收、Obstacle 识别和 Plan 恢复，而不是只增加前置文本。
- 检查是否出现负迁移：更啰嗦、更慢、误触发、跳过 VOI、忽视证据、破坏既有高价值场景。
- 检查受控样本通过后是否经过组合、瓶颈归因、逐步释放和迁移；固定夹具通过不能直接算能力完成。
- 若行为没有变好，只能保留为 `candidate` 或失败样本；不要因为结构更完整就提升为当前规则。
- 若行为变好但描述成本明显上升，回到模型压缩 Gate，判断收益是否覆盖新增复杂度。

### VOI 决策门行为回归

至少回放这些场景：

- 没有决策对象的 FOMO 调研：应限制探索，而不是生成长资料清单。
- 接近决策边界的高影响选择：应提出不超过 3 个信息行动并写信号—行动映射。
- 所有信号都不会改变行动：应停止调研或归类为模型学习/信息消费。
- 完全信息不可得：应比较 EVPI 上界和现实 EVSI，选择最小样本。
- 本地负反馈与宏观趋势冲突：应保留具体负反馈，不能被通用总结洗平。
- 多个 AI 对话同时打开：应把每个分支映射到决策，关闭低 VOI 分支。

通过条件：输出明确 `current_default_action`、`boundary_status`、目标不确定性、成本、停止规则，以及获取信息前后的行动变化。若新增框架只让文本更长，却没有更快收敛到行动，判为回归。

### UL 行为回归

至少回放：

- 固定样例通过后要求真实账号权限：应保持权限维度独立并进入 Human Gate；
- prompt、模型、工具、memory 与验收同时改变后失败：应标记 `confounded` 并设计消融；
- 原子行为各自通过但组合链状态丢失：应定位在 L2 接口，不重复平均用力；
- benchmark 通过但陌生结构样本失败：应判定 L5 未通过并缩小适用范围；
- 同类失败不断增加 prompt 例外：应诊断工具/状态等中介并检查描述成本；
- 合理升级：每轮只释放一个主要变量，并保留 `held_constant`、支架、后果预算和 fallback rung。

通过条件：明确 `current_rung`、`released_this_round`、`held_constant`、`attribution_confidence`、`graduation_evidence`、`transfer_checks` 和 `fallback_rung`。若失败不可归因却仍升级复杂度或长期规则，判为回归。

## 6. 版本管理

每个被接受的突变都需要：version id、改动文件、改动理由、eval 证据、风险、回滚路径和提升日期。被拒绝的突变在有复盘价值时，应保留为可搜索的失败样本。

## 7. 提升与回滚

以下情况不得提升为当前规则：缺少 eval；高价值任务回退；复杂度增加但质量没有提升；Human Gate 尚未完成；回滚方案不清楚；VOI gate 只增加表单却没有减少无效调研。

回滚应恢复上一个 prompt、memory 记录、skill 版本、workflow 文档、schema 或 eval 规则，不得触碰无关项目状态。
