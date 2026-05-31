# 游戏拆解诊断报告

## 1. 样本边界门

| 字段 | 内容 |
| --- | --- |
| 样本边界 `sample_boundary` |  |
| 可判断范围 `supported_judgment_scope` |  |
| 不可判断范围 `unsupported_judgment_scope` |  |
| 关键 unknown `key_unknowns` |  |
| 本次置信度上限 |  |

## 2. 拆解目标

| 字段 | 内容 |
| --- | --- |
| `dissection_goal` | understand_success / find_breakpoints / transfer_mechanic / benchmark_genre / improve_prototype |
| 用户真实问题 |  |
| 本次不回答的问题 |  |
| 需要降级的判断 |  |

## 3. 证据索引

| evidence_id | Image ID / Timestamp | event_type | observed_fact | supports_judgment | confidence |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 4. 玩家动词清单

| 动词 | 类型 | 玩家实际做什么 | 系统如何响应 | 服务的目标 | 频率 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | direct / indirect / abstract / interface |  |  |  | high / medium / low |  |  |

## 5. 动作和目标对齐

| 核心动作 | moment_goal | session_goal | mid_term_goal | long_term_goal | self_authored_goal | 对齐判断 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | aligned / weak / broken |

## 6. 不确定性来源

| 来源 | 具体表现 | 服务的挑战 | 玩家是否可读 | 风险 | 证据 |
| --- | --- | --- | --- | --- | --- |
| other_players / hidden_information / physical_skill / mental_skill / randomness |  |  | yes / partial / no |  |  |

## 7. 系统动态图

```text
rule_or_input -> player_strategy_shift -> system_response -> experience_dynamic -> risk_or_opportunity
```

| 动态 | 类型 | 证据 | 设计含义 | 风险/机会 |
| --- | --- | --- | --- | --- |
|  | reinforcing / tension / degenerative |  |  |  |

## 8. 内容流

| 内容层级 | 当前证据 | 是否改变玩家判断 | 风险 |
| --- | --- | --- | --- |
| repeated_content |  | yes / partial / no |  |
| variation_axis |  | yes / partial / no |  |
| onboarding_to_mastery |  | yes / partial / no |  |
| content_cost |  | known / unknown |  |
| exhausted_point |  | known / unknown |  |

## 9. 受众动机

| 动机 | 被什么动作承载 | 被什么目标承载 | 被什么反馈承载 | 证据 | 风险 |
| --- | --- | --- | --- | --- | --- |
| mastery / fantasy / expression / social_status / relaxation / drama |  |  |  |  |  |

## 10. 可玩主题和意义

| 字段 | 内容 |
| --- | --- |
| 机制奖励什么 |  |
| 机制惩罚什么 |  |
| 玩家被迫权衡什么价值 |  |
| 后果是否具象化 |  |
| 是否形成复述/讨论/二创 |  |
| 主题判断置信度 |  |

## 11. 迁移边界

| 字段 | 内容 |
| --- | --- |
| transferable_structure |  |
| non_transferable_surface |  |
| dependency |  |
| adaptation_cost |  |
| minimum_validation |  |
| kill_condition |  |

## 12. P0/P1 问题卡

| priority | issue | evidence_id | root_cause | minimum_fix | owner | validation |
| --- | --- | --- | --- | --- | --- | --- |
| P0/P1/P2 |  |  |  |  |  |  |

## 13. 验证计划

| 假设 | 最小样本 | 指标 | 通过线 | 失败即停止 / 降级 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
