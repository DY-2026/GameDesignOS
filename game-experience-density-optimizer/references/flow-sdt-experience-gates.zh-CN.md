# GameFlow 与 SDT 体验门

本文件用于给 ED/FEP 方案加一层体验交叉检查，防止方案只追求更密、更刺激、更可控，却没有真正支持玩家“想继续玩”。

这里借用两类设计启发式：

- GameFlow：关注注意力、挑战、技能、控制、清晰目标、反馈、沉浸和社交。
- Self-Determination Theory（SDT）：经典三项关注自主、胜任和关系；在游戏体验中额外把新颖作为扩展检查维度。这里的新颖必须是“最佳新颖性”，不是越新越好。

这些框架在本 skill 中同样是设计启发式，不是强行套用的科学量表。输出仍需标注 `theory_status: design_hypothesis`。

## GameFlow 检查

| 检查项 | ED/FEP 中的作用 | 常见失败 |
| --- | --- | --- |
| concentration | 玩家注意力是否落在核心任务 | UI/特效/弹窗让注意力漂移 |
| challenge_skill_fit | 自由能是否适中 | 挑战太低无聊，太高崩溃 |
| player_skill_growth | 自由能斜坡是否成立 | 玩家没有获得处理更高阶惊讶的能力 |
| control | 行动状态是否有效影响世界 | 输入迟滞、结果不可控、随机太强 |
| clear_goals | 玩家能否形成预测 | 目标不清、路径不明、胜负原因不明 |
| feedback | 预测误差是否能被解释 | 反馈延迟、噪声大、归因弱 |
| immersion | 体验边界是否稳定 | 打断、加载、风格割裂、过度解释 |
| social_interaction | 关系和社交是否支持体验 | 队友/公会/匹配/协作只带来压力 |

## SDT 检查

| 需求 | 设计翻译 | ED 方案中的检查 |
| --- | --- | --- |
| autonomy | 玩家感觉自己在做有意义选择 | `MD/min` 不能只是按钮或红点，选择要有后果 |
| competence | 玩家感觉自己变得更会玩 | `SF`、`EB`、清晰目标和反馈要支持学习 |
| relatedness | 玩家感觉与人、角色、世界有连接 | 社交、NPC、叙事回应、共同目标不能只服务指标 |
| novelty | 玩家感觉持续遇到可理解的新东西 | 新敌人、新组合、新地图信息、新 Build 可能性、新叙事回应必须半熟半新、可归因、可学习 |

`novelty` 在这里作为游戏体验扩展维度使用，不改写 SDT 经典三需求。它的价值是解释“为什么数值还在涨但玩家疲劳”：如果系统不再提供可控的新预测误差，玩家就不会觉得自己在继续发现或成长。

但新颖性必须经过 `optimal_stimulation_fit` 检查：

| optimal_novelty_fit | 表现 | 设计判定 |
| --- | --- | --- |
| `too_low` | 换皮、重复、完全可预测 | 需要增加半熟半新的可学习差异 |
| `matched` | 熟悉结构中出现小惊讶 | 可以作为正向 novelty |
| `too_high` | 随机、信息轰炸、规则跳变 | 这不是正向 novelty，而是 `CLP` 或过载 |
| `unknown` | 证据不足 | 只能写假设和验证方式 |

## 标准输出字段

```yaml
motivation_flow_gate:
  clear_goal_quality: unknown
  feedback_timeliness: unknown
  challenge_skill_fit: too_easy | matched | too_hard | uneven | unknown
  player_control_quality: unknown
  autonomy_support: unknown
  competence_support: unknown
  relatedness_support: not_applicable | weak | adequate | strong | unknown
  novelty_support: weak | adequate | strong | noisy | unknown
  optimal_novelty_fit: too_low | matched | too_high | unknown
  novelty_quality: learnable | cosmetic | random_noise | overwhelming | unknown
  risk_if_optimized_only_for_density: unknown
```

## 设计判定

- 如果玩家没有清晰目标，不要先增加惊讶。
- 如果玩家没有控制感，不要把随机性包装成新颖性。
- 如果玩家没有胜任感，不要只提高难度或惩罚。
- 如果玩家没有自主感，不要用强红点、虚假倒计时或不可逆损失推行为。
- 如果社交只制造压力和义务感，不要把 relatedness 写成正向加成。
- 如果新颖只是换皮、随机或信息轰炸，不要把它写成正向 novelty；它可能只是 `CLP` 或 `too_high` 自由能。
- 如果玩家已经过载，不要用“提高新颖性”解释方案；应先降低噪声、增加熟悉锚点，再引入半熟半新的差异。

## 和 ED 公式的对应

| ED 项 | GameFlow/SDT 交叉门 |
| --- | --- |
| `CLP` | concentration、clear_goals、feedback |
| `SF` | feedback、competence |
| `EB` | control、competence |
| `AR` | immersion、relatedness to world |
| `MD/min` | autonomy、challenge_skill_fit、novelty |

方案最终要能说清：这次改动除了改变密度，还如何保护玩家的清晰目标、控制感、自主感、胜任感和最佳新颖性。
