# 埋点与指标口径

ED 实验必须能被数据验证。埋点的目标不是收集越多越好，而是让设计假设、玩家行为和复盘判断能连起来。

## 指标周期门

先判断 `game_metric_model`，再选择 P1。单机/买断制默认看总旅程质量，手游/liveops 才默认看每日和持续天数。

| game_metric_model | 默认 P1 | 默认观察周期 | 不适用提醒 |
| --- | --- | --- | --- |
| `premium_single_player` | 总游戏时长、Demo/章节完成率、核心循环到达率、通关/重玩意愿 | 完整 Demo、章节段、单局 run 或总旅程 | 不默认使用 D1/D7、连续登录、每日任务 |
| `mobile_liveops` | D1/D3/D7/D30、每日会话、连续活跃、活动留存、回流后有效循环进入率 | 自然日、活动周期、回流窗口 | 不只看总时长，必须看持续天数和疲劳 |
| `hybrid` | 总旅程 P1 + liveops P1 分开 | 两套周期并行 | 任一周期受损都不能直接宣布成功 |
| `unknown` | unknown | unknown | 不默认承诺 D1/D7 或总时长提升 |

## 必备事件

| event_name | 触发时机 | 必备字段 | 用途 |
| --- | --- | --- | --- |
| `variant_assigned` | 玩家进入实验范围并完成分流 | `experiment_id`, `variant_id`, `user_segment`, `assignment_time` | 确认分流和样本口径 |
| `session_started` | 会话开始 | `session_id`, `user_id_hash`, `variant_id`, `entry_source`, `account_age_days` | 计算会话、分群、进入来源 |
| `meaningful_decision_made` | 玩家做出有意义选择 | `decision_id`, `decision_type`, `option_count`, `expected_impact_window_sec`, `context_id` | 计算 `MD/min` 和决策后窗口 |
| `choice_impact_observed` | 选择造成的结果首次可见 | `choice_id`, `impact_type`, `delta_summary`, `latency_sec` | 判断决策是否有短期可见重量 |
| `salient_feedback_fired` | 关键反馈触发 | `feedback_id`, `feedback_type`, `sensory_channels`, `clarity_score`, `linked_decision_id` | 判断 `SF` 是否足够可感知和可归因 |
| `embodiment_signal_observed` | 具身反馈窗口出现 | `signal_id`, `control_context`, `input_latency_ms`, `camera_state`, `hitstop_ms` | 判断 `EB` 相关改动是否触发 |
| `atmosphere_segment_seen` | 氛围段落出现 | `segment_id`, `duration_sec`, `audio_layer`, `visual_state`, `interactive` | 判断 `AR` 与留白质感 |
| `cognitive_load_signal` | 认知负荷信号出现 | `signal_type`, `ui_context`, `interruption_type`, `confusion_proxy`, `timestamp_ms` | 判断 `CLP` 是否过高 |
| `optimal_stimulation_window_observed` | QA、访谈或遥测代理标注当前刺激窗口 | `window_id`, `stimulation_band`, `boredom_type`, `player_resource_segment`, `stimulus_profile`, `context_stimulation`, `design_direction` | 判断 OLSO 是否匹配，避免把过载误判成刺激不足 |
| `prediction_error_window_observed` | 预期和结果出现关键差异 | `window_id`, `expected_state`, `actual_state`, `surprise_intensity`, `attribution_clarity`, `recovery_action_available` | 判断自由能区间和可控惊讶 |
| `blanket_coupling_signal` | 行动-反馈耦合被观测或标注 | `coupling_id`, `action_source`, `sensory_channel`, `input_latency_ms`, `feedback_latency_ms`, `noise_source`, `mapping_clarity`, `agency_score` | 判断玩家-游戏边界质量 |
| `anti_habituation_signal` | 老玩家或长线内容出现习惯化/反习惯化信号 | `content_loop_id`, `habituation_signal`, `anti_habituation_lever`, `familiar_anchor`, `novel_delta`, `attribution_clarity` | 判断长期疲劳是否来自模型不再更新 |
| `session_checkpoint` | 到达关键节点 | `checkpoint_id`, `elapsed_sec`, `state_summary` | 计算 TTE、退出点和进度 |
| `session_ended` | 会话结束 | `duration_sec`, `end_reason`, `last_checkpoint_id`, `last_event_id` | 计算会话时长和退出位置 |

## 推荐字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `experiment_id` | string | 实验唯一 ID，例如 `ed_first_session_2026w23` |
| `variant_id` | string | `A_control` / `B_reduce_clp` / `C_raise_vertical_quality` / `D_tune_md_frequency` |
| `user_segment` | string | `new_user` / `returning_user` / `existing_user` |
| `platform` | string | iOS、Android、PC、Web 等 |
| `client_version` | string | 客户端版本，避免混版本 |
| `channel` | string | 投放、自然、Steam、测试群等 |
| `elapsed_sec` | number | 从会话开始到当前节点的秒数 |
| `context_id` | string | 关卡、房间、波次、章节或任务上下文 |
| `confidence` | number | 设计标注置信度，0-1，可选 |
| `game_metric_model` | string | `premium_single_player` / `mobile_liveops` / `hybrid` / `unknown` |
| `metric_horizon` | string | `total_journey` / `chapter_segment` / `run_based` / `daily_retention` / `event_cycle` / `hybrid_split` |
| `stimulation_band` | string | `too_low` / `optimal` / `too_high` / `uneven` / `unknown` |
| `boredom_type` | string | `under_stimulation` / `over_stimulation` / `habituation` / `low_agency` / `low_meaning` / `mixed` / `unknown` |
| `player_resource_segment` | string | 新手、回流、核心、疲劳、低注意力窗口等设计/数据分群 |
| `stimulus_profile` | string | 当前刺激组合，例如 high_information、high_randomness、low_agency、repetitive_loop |
| `context_stimulation` | string | 外部或会话语境，例如 first_session、late_night、event_grind、boss_retry、demo_opening |
| `anti_habituation_lever` | string | `alternative_use` / `attention_investment` / `conscious_reframing` / `context_shift` / `combinatorial_depth` |

## 核心指标

| 指标 | 口径 | 用途 |
| --- | --- | --- |
| total_playtime_hours | 玩家在 Demo、章节、单局 run 或完整旅程中的总有效游玩时长 | 单机/买断制 P1 候选 |
| main_path_completion_rate | 主线、章节或 Demo 完成比例 | 单机/买断制 P1 候选 |
| chapter_checkpoint_reach_rate | 到达关键章节、Boss、教学结束或核心玩法解锁的比例 | 单机/买断制 P1 候选 |
| replay_intent_signal | 重开局、再次挑战、二周目、愿望单/评价倾向等代理信号 | 单机/肉鸽/买断制 P1 候选 |
| D1 / D3 / D7 / D30 | 首次进入实验后的自然日回访 | 手游/liveops P1 候选 |
| consecutive_active_days | 连续活跃天数 | 手游/liveops P1 候选，不能用焦虑式连续登录强推 |
| daily_active_session_count | 每日会话次数和日内节奏 | 手游/liveops P1/P2 候选 |
| session_median_duration | 会话时长中位数 | 避免均值被极端玩家拉高 |
| TTE | 从会话开始到首个有效事件的秒数 | 检查首个爆点是否太晚 |
| ED proxy | `MD/min * (SF + EB + AR) / CLP` 的归一化代理分 | 解释体验浓度变化 |
| MD/min | 每分钟有意义选择次数 | 判断水平频率 |
| SF score | 关键反馈清晰度和归因评分 | 判断爽点和反馈质量 |
| EB score | 输入响应、镜头、命中停顿、触觉等代理评分 | 判断具身感 |
| AR score | 氛围段落质量、停留、观察和正向反馈 | 判断氛围感 |
| CLP score | 困惑、打断、重复点击、教程卡顿等代理评分 | 判断认知负荷 |
| prediction_error_band | `too_low` / `optimal` / `too_high` 的设计或 QA 标注 | 判断自由能区间 |
| optimal_stimulation_band | `too_low` / `optimal` / `too_high` / `uneven` 的设计或 QA 标注 | 判断刺激窗口是否匹配玩家资源和情境 |
| boredom_type_mix | 各类无聊信号占比 | 区分刺激不足、过载、习惯化、低能动性、低意义感 |
| attribution_clarity | 预期和结果差异是否能被玩家归因的代理评分 | 判断可控惊讶 |
| blanket_coupling_quality | 行动-反馈低延迟、低噪声、高解释性的代理评分 | 判断马尔可夫毯耦合 |
| anti_habituation_fit | 旧循环中半熟半新差异的可归因、可学习程度 | 判断反习惯化方案是否成立 |
| meaningful_decision_gap_p75 | 相邻有意义选择间隔 P75 | 找空窗 |
| decision_impact_latency | 玩家选择到结果可见的延迟 | 判断决策重量 |
| narrative_blocking_time | 不可交互叙事时长 | 判断叙事停顿 |
| early_exit_rate | 关键 checkpoint 前退出比例 | 负向风险 |
| failure_rate | 失败或死亡比例 | 难度风险 |
| skip_rate | 剧情或演出跳过率 | 叙事风险 |

## P1 / P2 / 负向指标

默认 P1 必须按游戏形态选择，P2 指标是解释性体验指标。

| 模型 | P1 示例 | P2 示例 | 负向示例 |
| --- | --- | --- | --- |
| `premium_single_player` | 总有效游玩时长、Demo/章节完成率、核心循环到达率、通关/重玩意愿 | ED proxy、TTE、CLP、SF/EB/AR、有效选择空窗、optimal_stimulation_band、prediction_error_band、blanket_coupling_quality | 退出点提前、失败率上升、跳过后差评、退款/负评风险 |
| `mobile_liveops` | D1/D3/D7/D30、每日会话、连续活跃、活动留存、回流成功率 | ED proxy、TTE、CLP、SF/EB/AR、有效选择空窗、optimal_stimulation_band、boredom_type_mix、anti_habituation_fit、prediction_error_band、blanket_coupling_quality | 早退、投诉、付费误触、经济异常、日常疲劳 |
| `hybrid` | 总旅程 P1 与 liveops P1 分开预注册 | 两套 P2 分开解释 | 任一周期明显受损都不能宣布成功 |

## 看板过滤器

看板至少要支持这些过滤器：实验 ID、变体、`game_metric_model`、`metric_horizon`、用户阶段、平台、渠道、客户端版本、账号年龄、是否新装、是否回流、首局/非首局、关键关卡或章节、`stimulation_band`、`boredom_type`。

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
