# Uncertainty Calibration

## 不确定性目标

| 字段 | 内容 |
| --- | --- |
| 想让玩家不知道什么 |  |
| 不确定性服务的目标 |  |
| 不确定性不应该破坏什么 |  |

## 来源映射

| 来源 | 当前设计 | 玩家可读性 | 玩家可控性 | 风险 | 调整动作 |
| --- | --- | --- | --- | --- | --- |
| 人 |  | high / medium / low | high / medium / low |  |  |
| 隐藏信息 |  | high / medium / low | high / medium / low |  |  |
| 身体技能 |  | high / medium / low | high / medium / low |  |  |
| 脑力技能 |  | high / medium / low | high / medium / low |  |  |
| 随机性 |  | high / medium / low | high / medium / low |  |  |

## 放置检查

| 检查项 | 通过标准 | 当前判断 |
| --- | --- | --- |
| 随机是否放在玩家可接受的位置 | 生成局面、奖励候选、扰动，而不是抹掉明确努力 | pass / weak / fail |
| 玩家是否能解释失败 | 失败原因可见、可复盘、可调整 | pass / weak / fail |
| 不确定性是否降低分析瘫痪 | 限制过远推演，但不剥夺策略 | pass / weak / fail |
| 不确定性是否匹配受众 | 竞技、休闲、社交、叙事受众的容忍度不同 | pass / weak / fail |

## 验证指标

| 指标 | 目标 |
| --- | --- |
| failure_explanation_rate | 玩家能说出失败原因的比例 |
| replay_intent_after_bad_luck | 坏运气后仍愿意再试的比例 |
| analysis_time_per_decision | 单次决策耗时 |
| perceived_fairness | 玩家公平感评分 |
