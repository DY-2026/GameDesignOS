# 最佳刺激窗口与体验浓度

本文档把最佳刺激水平模型（Optimal Level of Stimulation / OLSO）转译成体验浓度的第一诊断层。它用于回答：为什么同样的信息量、难度、随机、画面复杂度和新内容，对不同玩家可能分别表现为无聊、上头或崩溃。

本文件只作为设计启发式使用。输出时必须保留：

```yaml
theory_status: design_hypothesis
olso_usage: design_metaphor
```

## 核心命题

体验浓度不是单位时间内事件越多越好，而是当前玩家在当前情境下，单位时间内可吸收、可解释、可转化为探索/学习/意义的刺激密度。

OLSO 的设计翻译是：

```text
玩家会主动寻找一个“刚好”的刺激窗口。
太低，玩家会寻找更复杂/更新颖的刺激。
太高，玩家会退回更熟悉/更简单/更安全的刺激。
刚好，玩家愿意探索、学习、复盘并继续投入。
```

所以，“无聊”至少有两种相反来源：

| 无聊类型 | 真实问题 | 常见误判 | 正确方向 |
| --- | --- | --- | --- |
| `under_stimulation` | 刺激低于最佳窗口，预测误差太少 | 以为玩家不喜欢该玩法 | 增加可解释的新颖、复杂度或意义 |
| `over_stimulation` | 刺激高于最佳窗口，玩家无法处理 | 以为还不够刺激 | 降低并发、增加熟悉锚点、先降 CLP |
| `habituation` | 原本有效的刺激被玩透，边际信息消失 | 继续加数值奖励 | 反习惯化：新用途、新环境、新视角 |
| `low_agency` | 玩家无法通过行动调节刺激 | 继续加反馈或提示 | 修复行动-反馈耦合 |
| `low_meaning` | 刺激存在但不能接入目标/身份/世界意义 | 继续加内容量 | 赋予用途、关系、叙事或精通价值 |

## 为什么它必须在 ED 公式之前

ED 公式：

```text
ED = MD/min * (SF + EB + AR) / CLP
```

只能说明该改哪个设计旋钮。OLSO 先说明这个旋钮该往哪个方向改。

同一个 `MD/min` 低：

- 如果玩家是新手、题材陌生、UI 混乱，可能已经 `over_stimulation`，不能加频率。
- 如果玩家是老手、框架熟悉、系统被玩透，才可能需要增加半熟半新的选择。

同一个 `CLP` 高：

- 可能是 UI 噪声。
- 也可能是玩家资源不足、类型素养不足、情绪压力高、环境刺激已经过强。

因此，诊断顺序必须是：

```text
玩家资源/情境 -> 刺激画像 -> 最佳刺激窗口 -> ED 公式项 -> 实验主旋钮
```

## 玩家资源画像

不要把“玩家”当成平均人。至少检查：

| 维度 | 设计问题 |
| --- | --- |
| `game_literacy` | 玩家是否理解该品类的默认语言、镜头、操作、数值和目标 |
| `genre_familiarity` | 玩家对该类型是新手、普通玩家、核心玩家还是专家 |
| `cognitive_budget` | 当前会话可用注意力是否被生活压力、疲劳、通勤、碎片时间压缩 |
| `mood_or_pressure` | 玩家处在促进焦点（想探索成长）还是预防焦点（怕错、怕亏、怕被惩罚） |
| `arousability` | 玩家是否更容易被唤醒、过载或寻求强刺激 |
| `social_context` | 玩家是在独玩、排位、组队、直播、社群压力还是亲友旁观中玩 |

材料不足时可以写 `unknown`，但不能假装已经知道玩家心理。

## 刺激画像

把体验刺激拆成五类：

| 维度 | 太低时 | 太高时 | 最佳状态 |
| --- | --- | --- | --- |
| `familiarity` | 完全陌生，无法建模 | 完全熟悉，习惯化 | 熟悉结构作为安全锚点 |
| `novelty` | 没有新信息 | 随机、换皮、无法归因 | 半熟半新，可学习 |
| `complexity` | 过于简单，没深度 | 规则/信息/状态过载 | 有层次，可逐步处理 |
| `intensity` | 没有峰值 | 轰炸、疲劳、压力 | 峰值后有释放和留白 |
| `surprise` | 完全可预期 | 反复不可解释 | 意外但有因果线索 |

## 情境刺激

刺激不单独存在，总是和情境一起被处理。

| 情境 | 设计含义 |
| --- | --- |
| 熟悉情境 | 降低总体刺激，更适合加入新颖性 |
| 新奇情境 | 提高总体刺激，更需要熟悉锚点 |
| 正向情绪效价 | 更容易接近新颖、复杂和探索 |
| 负向情绪效价 | 更容易退回熟悉、安全和确定 |
| 高社交/排位压力 | 增加预防焦点，降低新系统承受度 |
| 低代价安全场 | 更容易接受失败、试错和高唤醒 |

## 半熟半新原则

有效新颖性不是“全新”，而是“熟悉结构中的小差异”。

```text
熟悉负责安全感。
差异负责注意力。
可理解负责兴趣。
可行动负责成长。
```

在游戏中，半熟半新可以表现为：

- 熟悉敌人增加一个可预读变招。
- 熟悉地图出现一条新路线或新资源关系。
- 熟悉角色获得一个新用途，而不是只涨数值。
- 熟悉赛季框架里改变少数关键规则。
- 熟悉 Boss 阶段里加入可学习的反击窗口。

如果新颖性不可归因、不可学习、不可复盘，它不是体验浓度，而是 CLP。

## 兴趣判定：新且能懂

兴趣不只来自新奇，还来自玩家相信自己有能力理解这个新东西。

设计判定：

| 组合 | 玩家体验 | 设计判断 |
| --- | --- | --- |
| 不新 + 能懂 | 顺滑但可能钝化 | 适合作为锚点 |
| 新 + 能懂 | 有趣、想探索 | 最佳新颖性 |
| 新 + 不能懂 | 困惑、压力、退出 | 先补线索和反馈 |
| 不新 + 不能懂 | 烦躁、无意义劳动 | 先降 CLP 或重写目标 |

## 安全高唤醒

恐怖、过山车、Boss 濒死反杀、魂类受苦等体验可以短暂高于平时最佳窗口，但必须满足：

- 玩家知道这是安全/有限/可重来的。
- 高唤醒后有明确释放。
- 失败能带回信息，而不是只带回惩罚。
- 下一次行动能更好。

否则，高唤醒会从“刺激”变成“创伤式噪声”。

## 长线与反习惯化

玩家把游戏玩透后，问题常常不是奖励不够，而是刺激被习惯化，预测误差消失，意义变淡。

长线改动优先考虑五类反习惯化旋钮：

| 旋钮 | 设计翻译 | 例子 |
| --- | --- | --- |
| `alternative_use` | 给已有内容新用途 | 老角色进入新模式、旧装备出现新构筑 |
| `attention_investment` | 让玩家更在意已有内容 | 角色故事、精通循环、社交关系、收藏展示 |
| `conscious_reframing` | 让玩家用新视角理解游戏 | 电竞化、身份叙事、世界观意义、社区挑战 |
| `context_shift` | 改变环境而不推翻核心 | 赛季、版本规则、地图条件、玩法修饰 |
| `combinatorial_depth` | 让系统自己生成新刺激 | 肉鸽组合、UGC、Build 深度、玩家自定目标 |

这五类比“继续加新内容”更适合解释长期体验浓度。

## 输出字段

标准 ED 方案中加入：

```yaml
optimal_stimulation_fit:
  band: too_low | optimal | too_high | uneven | unknown
  boredom_type: under_stimulation | over_stimulation | habituation | low_agency | low_meaning | mixed | unknown
  player_resource_profile:
    game_literacy: novice | regular | expert | unknown
    genre_familiarity: low | medium | high | unknown
    cognitive_budget: low | medium | high | unknown
    mood_or_pressure: promotion | prevention | mixed | unknown
    arousability: low | medium | high | unknown
  stimulus_profile:
    familiarity: too_low | balanced | too_high | unknown
    novelty: too_low | optimal | too_high | unknown
    complexity: too_low | optimal | too_high | unknown
    intensity: too_low | optimal | too_high | unknown
    surprise: too_low | optimal | too_high | unknown
  context_stimulation:
    familiarity_anchor: weak | adequate | strong | unknown
    emotional_valence: positive | neutral | negative | mixed | unknown
    social_pressure: low | medium | high | unknown
  design_direction: add_semi_novelty | add_familiar_anchor | reduce_overload | anti_habituation | repair_agency | add_meaning | preserve_curve | unknown
```

长线、后期疲劳、赛季、肉鸽、刷子、UGC、老玩家钝化时，额外输出：

```yaml
anti_habituation_plan:
  habituated_element: unknown
  selected_lever: alternative_use | attention_investment | conscious_reframing | context_shift | combinatorial_depth | unknown
  familiar_anchor_to_preserve: unknown
  semi_novel_delta: unknown
  proof_player_can_understand: unknown
```

## 诊断问题

1. 这是哪个玩家群体的最佳刺激窗口，不是平均玩家的窗口？
2. 当前刺激是太低、太高、习惯化，还是意义/能动性不足？
3. 玩家是否有足够熟悉锚点来处理新颖性？
4. 玩家是否有足够认知资源和情绪安全感来探索？
5. 新东西是否可理解、可行动、可复盘？
6. 如果是长线问题，是加内容，还是给已有内容反习惯化？

## 与其他理论层的关系

```text
OLSO：判断当前刺激是否适合这个玩家和情境。
FEP/PP：解释刺激如何成为可消化的预测误差，以及乐趣为何来自更快的误差降低。
Markov blanket：检查玩家通过哪些感官/行动边界接收和调节刺激。
GameFlow/SDT：检查刺激是否支持清晰目标、控制、自主、胜任、关系和最佳新颖性。
ED：把上述判断编译成一个主旋钮、一组变体、埋点、看板和预注册决策。
```
