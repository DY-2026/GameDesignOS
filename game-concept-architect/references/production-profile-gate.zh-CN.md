# Production Profile Gate

目的：在承诺功能和体验之前，先判断当前生产画像是否能支撑设计核。团队能力未知时，必须降低确定语气，并把高风险能力放入 assumption ledger。

## Production Profile 字段

| 字段 | 说明 |
| --- | --- |
| `team_shape` | solo、小团队、中型团队、外包混合、未知 |
| `core_strengths` | 已知擅长能力，例如系统、关卡、叙事、美术、联网、工具 |
| `unknown_capabilities` | 未知但会影响方案的能力 |
| `technical_risk` | 引擎、联网、物理、生成、AI、工具链风险 |
| `content_risk` | 剧情、美术、关卡、角色、活动、LiveOps 产能风险 |
| `operation_risk` | 长线运营、社区、客服、数据分析、版本节奏风险 |
| `budget_time_assumption` | 时间、预算、人力假设 |
| `fallback_plan` | 能力不足时的降级方案 |

## 高风险默认项

团队能力未知时，不要把以下内容当作默认可做：

- 开放世界。
- 实时多人或强同步联网。
- 长期 live ops 和高频活动。
- 大量剧情分支或全语音内容。
- 高精度物理、复杂 AI、UGC 审核体系。
- 大规模角色池、关卡池、装备池或持续内容产出。

## 最小示例

```markdown
## Production Profile Gate

| 字段 | 当前判断 | 风险 | 降级方案 |
| --- | --- | --- | --- |
| team_shape | unknown | 不能默认支持开放世界或实时多人 | 先按小团队离线单人原型设计 |
| core_strengths | assumption: 系统设计可控 | 需要实际原型证明 | 用纸面/灰盒验证循环 |
| content_risk | 中 | 植物种类和事件数量可能膨胀 | MVP 限制为 3 种植物、2 类敌人 |
| fallback_plan | 保留照料-变形核心，砍掉多温室叙事 | scope 可控 | Demo 后再评估扩展 |
```

## 质量门

- 团队能力未知时，必须写 `unknown` 或 `assumption`。
- 核心卖点不得依赖不可控能力，除非同时提供替代方案和验证路径。
- 内容产能必须进入 scope gate，不得用“后续补内容”替代。
- 如果生产画像不支持当前 design nucleus，必须降 scope、换 nucleus 或标为高风险。
