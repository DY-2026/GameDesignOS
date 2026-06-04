# 埋点与指标口径

EPM 实验必须能被数据验证。埋点的目标不是收集越多越好，而是让设计假设、玩家行为和复盘判断能连起来。

## 必备事件

| event_name | 触发时机 | 必备字段 | 用途 |
| --- | --- | --- | --- |
| `variant_assigned` | 玩家进入实验范围并完成分流 | `experiment_id`, `variant_id`, `user_segment`, `assignment_time` | 确认分流和样本口径 |
| `session_started` | 会话开始 | `session_id`, `user_id_hash`, `variant_id`, `entry_source`, `account_age_days` | 计算会话、分群、进入来源 |
| `meaningful_event_fired` | 有效体验事件触发 | `event_id`, `event_type`, `intensity`, `source_system`, `timestamp_ms`, `context_id` | 计算 EPM 和事件节奏 |
| `player_choice_made` | 玩家做出可归因选择 | `choice_id`, `choice_type`, `option_count`, `expected_impact_window_sec`, `context_id` | 计算决策频率和决策后窗口 |
| `choice_impact_observed` | 选择造成的结果首次可见 | `choice_id`, `impact_type`, `delta_summary`, `latency_sec` | 判断决策是否有短期可见重量 |
| `narrative_packet_seen` | 剧情、对白、演出或文本包出现 | `packet_id`, `duration_sec`, `skipped`, `interactive`, `critical_info` | 判断叙事压缩与跳过风险 |
| `session_checkpoint` | 到达关键节点 | `checkpoint_id`, `elapsed_sec`, `state_summary` | 计算 TTE、退出点和进度 |
| `session_ended` | 会话结束 | `duration_sec`, `end_reason`, `last_checkpoint_id`, `last_event_id` | 计算会话时长和退出位置 |

## 推荐字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `experiment_id` | string | 实验唯一 ID，例如 `epm_first_session_2026w23` |
| `variant_id` | string | `A_control` / `B_event_frequency` / `C_decision_weight` / `D_narrative_compression` |
| `user_segment` | string | `new_user` / `returning_user` / `existing_user` |
| `platform` | string | iOS、Android、PC、Web 等 |
| `client_version` | string | 客户端版本，避免混版本 |
| `channel` | string | 投放、自然、Steam、测试群等 |
| `elapsed_sec` | number | 从会话开始到当前节点的秒数 |
| `context_id` | string | 关卡、房间、波次、章节或任务上下文 |
| `confidence` | number | 设计标注置信度，0-1，可选 |

## 核心指标

| 指标 | 口径 | 用途 |
| --- | --- | --- |
| D1 / D3 / D7 | 首次进入实验后的自然日回访 | 留存结果指标 |
| session_median_duration | 会话时长中位数 | 避免均值被极端玩家拉高 |
| TTE | 从会话开始到首个有效事件的秒数 | 检查首个爆点是否太晚 |
| EPM | 有效事件数乘以清晰度和相关性，再除以可玩分钟 | 解释体验密度变化 |
| meaningful_event_gap_p75 | 相邻有效事件间隔 P75 | 找空窗 |
| decision_impact_latency | 玩家选择到结果可见的延迟 | 判断决策重量 |
| narrative_blocking_time | 不可交互叙事时长 | 判断叙事停顿 |
| early_exit_rate | 关键 checkpoint 前退出比例 | 负向风险 |
| failure_rate | 失败或死亡比例 | 难度风险 |
| skip_rate | 剧情或演出跳过率 | 叙事风险 |

## P1 / P2 / 负向指标

默认 P1 指标是留存和会话质量，P2 指标是解释性体验指标。

| 层级 | 示例 |
| --- | --- |
| P1 | D1 提升、D3/D7 不下降、首局关键 checkpoint 到达率提升 |
| P2 | EPM 提升、TTE 下降、有效事件空窗减少、选择后窗口行为改善 |
| 负向 | 崩溃率、早退率、失败率、跳过后流失、投诉、付费误触、经济异常 |

## 看板过滤器

看板至少要支持这些过滤器：实验 ID、变体、用户阶段、平台、渠道、客户端版本、账号年龄、是否新装、是否回流、首局/非首局、关键关卡或章节。

## 数据质量门

| 检查 | 失败表现 | 处理 |
| --- | --- | --- |
| 分流平衡 | A/B/C/D 样本比例异常 | 暂停判断，检查开关 |
| 埋点完整 | 关键事件缺失或重复 | 修复埋点后重启实验 |
| 版本一致 | 多版本混跑 | 按版本分层或废弃样本 |
| 时间口径 | 时区、自然日、安装日混乱 | 统一口径后重算 |
| 用户去重 | 同一用户多设备重复 | 使用稳定匿名 ID |

## 隐私与安全

只记录验证设计假设所需字段。用户 ID 应使用匿名或 hash 标识。不要记录聊天原文、真实姓名、手机号、支付凭据、精确定位或其他不必要的个人信息。公开示例只使用 synthetic 数据。
