# 咨询交付诊断报告模板

用于正式交付、复盘会、立项评审或版本改版方案。它比标准报告更强调证据链、问题卡、优先级、验证计划和决策结论。

## 使用规则

- 先输出 `sample_scope_gate`，再给执行摘要。
- 每个关键结论必须引用 `evidence_id`；每个 P0/P1 问题必须有 issue card。
- 外部研究必须过 VOI：写明“会改变什么判断”，否则不展开。
- 输出应落到 `keep / change / cut / validate` 四类动作。

## 字段定义

| 字段 | 规则 |
| --- | --- |
| `executive_decision` | `Go` / `Conditional Go` / `No-Go` / `Watch` / `Fix Before Scale`。 |
| `diagnosis_pack` | 选择一个主诊断包，可叠加 1-2 个辅助包。 |
| `evidence_index` | 覆盖所有 P0/P1/P2 结论。 |
| `issue_cards` | 使用 `templates/issue-card.md` 字段。 |
| `validation_plan` | 使用 `templates/validation-plan.md` 字段。 |
| `confidence_statement` | 说明哪些结论高置信，哪些受样本限制。 |

## 模板

```markdown
# 咨询交付诊断报告

## 1. 样本边界门

| 字段 | 内容 |
| --- | --- |
| 样本边界 |  |
| 可判断范围 |  |
| 不可判断范围 |  |
| 关键 unknown |  |

## 2. 执行摘要

| 字段 | 内容 |
| --- | --- |
| 交付结论 | Go / Conditional Go / No-Go / Watch / Fix Before Scale |
| 主诊断包 |  |
| 辅助诊断包 |  |
| 最大机会 |  |
| 最大风险 |  |
| 30 天内必须验证 |  |

## 3. Evidence Index

| evidence_id | 来源 | 定位 | event_type | observed_fact | supports_judgment | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| E001 |  |  |  |  |  |  |

## 4. 诊断包路由

| 诊断包 | modes | required sections | 本次启用原因 | 不启用原因 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 5. 关键问题卡

粘贴 `templates/issue-card.md`，按 P0/P1/P2 排序。

## 6. 方案路线

| 动作 | 对象 | 证据 | 预期收益 | 成本 | 风险 | owner |
| --- | --- | --- | --- | --- | --- | --- |
| keep / change / cut / validate |  |  |  |  |  |  |

## 7. 验证计划

粘贴 `templates/validation-plan.md`。

## 8. 置信度声明

- 高置信：
- 中置信：
- 低置信 / unsupported：
- 仍需补料：
```

## 最小示例

```markdown
| 交付结论 | Fix Before Scale |
| 主诊断包 | 商业化打断诊断包 |
| 最大风险 | 首轮胜利反馈前出现广告双倍奖励，削弱成就感。 |
| 30 天内必须验证 | A/B：广告双倍奖励延后到第二轮结算后，比较首 10 分钟留存和广告点击。 |
```
