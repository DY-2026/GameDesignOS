# 单机与手游的指标周期门

本文件用于防止把所有游戏都当成手游留存产品来分析。体验浓度可以服务不同游戏形态，但 P1 指标、观察周期和看板结构必须先按游戏形态分流。

## 先判断 game_metric_model

| game_metric_model | 典型对象 | 默认时间尺度 | 不要默认使用 |
| --- | --- | --- | --- |
| `premium_single_player` | 买断制单机、线性/半开放主线、Steam Demo、章节制叙事、单机动作/肉鸽 | 总游戏旅程、章节段落、单局 run、Demo 完成 | D1/D7、连续登录、每日任务、日活 |
| `mobile_liveops` | 手游、长线运营、活动循环、每日任务、回流活动、赛季制数值成长 | 每日、连续天数、活动周期、回流窗口 | 只看总时长而忽略日留存 |
| `hybrid` | 单机主体加赛季/多人/活动，或手游内含完整单机章节 | 分开建模：总旅程 + 活动/日留存 | 把两个周期混成一个成功标准 |
| `unknown` | 材料不足 | 暂不判断 | 把 D1/D7 或总时长当成默认胜利 |

## 单机/买断制：总旅程指标

单机游戏的核心问题通常不是“玩家明天会不会登录”，而是“玩家是否愿意把这段旅程玩下去、玩完、推荐、重玩或购买正式版”。

默认 P1 指标可以从这里选：

| 指标 | 用途 |
| --- | --- |
| `total_playtime_hours` | 总游戏时长或 Demo 总停留，观察是否愿意继续玩 |
| `main_path_completion_rate` | 主线、章节或 Demo 完成率 |
| `chapter_checkpoint_reach_rate` | 关键章节、Boss、教学结束、核心玩法解锁到达率 |
| `time_to_core_loop` | 到达第一个完整核心循环的时间 |
| `ending_reach_rate` | 通关或结局到达率 |
| `replay_intent_signal` | 二周目、重新开局、再次挑战、愿望单/评价倾向等代理信号 |
| `refund_or_negative_review_risk` | 买断制的重要负向风险，若可获得再使用 |

单机也可以看 session，但 session 是解释指标，不是默认 P1。比如会话时长上升可能只是不可跳过演出变长；必须结合退出点、完成率、失败率和负反馈判断。

## 手游/liveops：每日和持续天数指标

手游和长线运营产品的价值承诺通常包含每日节奏、活动窗口、回流和持续成长。这里可以把日留存作为 P1。

默认 P1 指标可以从这里选：

| 指标 | 用途 |
| --- | --- |
| `D1 / D3 / D7 / D30` | 首次进入实验后的自然日回访 |
| `daily_active_session_count` | 每日会话次数和日内节奏 |
| `consecutive_active_days` | 持续活跃天数，不能用焦虑式连续登录强推 |
| `return_session_rehook_rate` | 回流后是否进入有效循环 |
| `event_retention_rate` | 活动期间留存或复访 |
| `daily_task_completion_quality` | 日常循环是否被完成且没有明显厌烦 |

手游也要避免暗黑模式。连续登录、每日任务和活动压力只能用于健康节奏设计，不能用强迫红点、虚假倒计时或损失厌恶包装成体验浓度。

## hybrid：拆开两套胜利标准

hybrid 项目必须显式拆出两个周期：

```yaml
metric_horizon:
  game_metric_model: hybrid
  journey_p1: total_playtime_hours | completion_rate | chapter_checkpoint_reach_rate
  liveops_p1: D1 | D7 | event_retention_rate | return_session_rehook_rate
  conflict_rule: if one improves and the other worsens, do not declare success
```

例如，一个有赛季活动的单机肉鸽可以看总游戏时长、run 完成率、重开局意愿，也可以在活动模式里看 D7。但不能因为 D7 上升就掩盖主线完成率下降，也不能因为总时长上升就忽略每日疲劳。

## 标准输出字段

```yaml
metric_horizon:
  game_metric_model: premium_single_player | mobile_liveops | hybrid | unknown
  primary_time_horizon: total_journey | chapter_segment | run_based | daily_retention | event_cycle | hybrid_split | unknown
  p1_metric_family: total_playtime | completion_progress | replay_intent | daily_retention | liveops_continuity | hybrid_split | unknown
  excluded_metrics: []
  rationale: unknown
```

如果用户没有说明游戏形态，不要主动把 D1/D7 写成 P1。可以写：

```yaml
game_metric_model: unknown
excluded_metrics:
  - D1/D7 are not assumed until mobile/liveops context is confirmed
```

## 决策门

| 模型 | 成功门示例 | 负向门示例 |
| --- | --- | --- |
| `premium_single_player` | Demo 完成率提升、核心循环到达率提升、章节退出率下降、总有效游玩时长提升 | 不可跳过内容变长、失败率上升、关键章节差评、退款/负评风险 |
| `mobile_liveops` | D1/D7 提升、回流后有效循环进入率提升、活动留存改善 | 日常厌烦、投诉、付费误触、经济异常、老玩家疲劳 |
| `hybrid` | 两套 P1 至少不互相伤害，并且目标周期内主指标改善 | 总旅程和日留存彼此冲突、活动伤害主线体验 |

所有成功门必须预注册。不要事后挑对自己有利的周期解释胜利。
