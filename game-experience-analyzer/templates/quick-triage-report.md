# 快速诊断报告模板

用于 10-20 分钟内给出可执行方向。只输出最关键的样本边界、证据索引、3-5 个问题和下一步验证，不展开完整理论。

## 使用规则

- 适合材料少、时间紧、用户要“先快速看看”的场景。
- 必须先输出样本边界门，不能先给总评。
- 每个问题必须引用至少 1 个 `evidence_id`；没有证据的判断进入 `key_unknowns`。
- 不输出与当前诊断包无关的通用章节。

## 字段定义

| 字段 | 规则 |
| --- | --- |
| `diagnosis_pack` | 来自 `references/diagnosis-pack-router.yaml`，不能新造泛泛模式。 |
| `sample_scope_gate` | 写 `sample_boundary`、`supported_judgment_scope`、`unsupported_judgment_scope`、`key_unknowns`。 |
| `evidence_index` | 只列支撑关键判断的证据，编号 `E001` 起。 |
| `top_findings` | 最多 5 条，每条包含 `evidence_refs`、影响、建议动作。 |
| `next_validation` | 只列会改变判断的验证项。 |

## 模板

```markdown
## 1. 样本边界门

| 字段 | 内容 |
| --- | --- |
| 样本边界 |  |
| 可判断范围 |  |
| 不可判断范围 |  |
| 关键 unknown |  |

## 2. 诊断路由

| 字段 | 内容 |
| --- | --- |
| 诊断包 |  |
| 对应 modes |  |
| 本次不启用的镜头 |  |

## 3. Evidence Index

| evidence_id | 定位 | event_type | observed_fact | supports_judgment | confidence |
| --- | --- | --- | --- | --- | --- |
| E001 |  |  |  |  |  |

## 4. Top Findings

| 优先级 | 判断 | evidence_refs | 影响 | 建议动作 |
| --- | --- | --- | --- | --- |
| P0 |  |  |  |  |

## 5. 下一步验证

| 验证项 | 会改变什么判断 | 最小样本 | 通过标准 | 停止条件 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
```

## 最小示例

```markdown
## 1. 样本边界门

| 字段 | 内容 |
| --- | --- |
| 样本边界 | 1 条 18 秒竖版买量素材，可见战斗和 CTA，但没有落地页。 |
| 可判断范围 | 首秒钩子、素材误导风险、CTA 可读性。 |
| 不可判断范围 | D1 留存、真实付费、完整核心循环。 |
| 关键 unknown | 落地页承接、试玩前 3 分钟、投放 CTR。 |

## 4. Top Findings

| 优先级 | 判断 | evidence_refs | 影响 | 建议动作 |
| --- | --- | --- | --- | --- |
| P0 | 素材第 2 秒给出强视觉冲突，但没有展示玩家输入，容易形成“像动画不像游戏”的风险。 | E001, E002 | 点击后转化可能断层 | 补 3 秒可控操作和即时反馈镜头。 |
```
