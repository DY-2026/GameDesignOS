# Production Profile

## Production Profile Gate

| Field | Current Judgment | Confidence | Risk | Fallback |
| --- | --- | --- | --- | --- |
| team_shape | solo / small_team / mid_team / outsourcing_mix / unknown |  |  |  |
| core_strengths |  | known / assumption / unknown |  |  |
| unknown_capabilities |  | unknown |  |  |
| technical_risk |  | low / medium / high |  |  |
| content_risk |  | low / medium / high |  |  |
| operation_risk |  | low / medium / high |  |  |
| budget_time_assumption |  | assumption / unknown |  |  |
| fallback_plan |  |  |  |  |

## Scope Consequence

| Design Element | Keep / Cut / Defer | Reason | Validation |
| --- | --- | --- | --- |
|  |  |  |  |

## Minimal Example

| Field | Current Judgment | Confidence | Risk | Fallback |
| --- | --- | --- | --- | --- |
| team_shape | unknown | unknown | 不能默认支持开放世界或实时多人 | 先按小团队离线单人原型设计 |
| content_risk | 植物和事件数量可能膨胀 | medium | 内容产能不明 | MVP 限制为 3 种植物、2 类敌人 |

## Quality Gate

- 团队能力未知时，不得默认支持高风险生产项。
- 核心卖点必须有可控能力来源、替代方案或验证路径。
- 内容产能风险必须影响 scope gate。
