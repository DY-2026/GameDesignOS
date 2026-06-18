# 信息价值（VOI）决策门 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. 核心定义

信息价值不是信息的新鲜度、真实性、稀缺性、知识含量或表达质量。它是新信息让决策者在不确定环境中选择更优行动，从而提高期望效用的程度。

形式化表达：

```text
VOI(I)
= E_I [ max_a E[U(a, θ) | I] ]
- max_a E_θ [ U(a, θ) ]
```

其中：

- `a` 是可选行动；
- `θ` 是尚不确定的现实状态；
- `U(a, θ)` 是行动在现实状态下的效用；
- `I` 是未来可能获得的信息。

因此，真实信息也可能没有决策价值。若所有合理信号出现后，行动都不会改变，则它对当前决策的 VOI 接近于零。

净信息价值还必须扣除获取信息带来的代价：

```text
net_voi
= gross_voi
- acquisition_cost
- latency_cost
- attention_cost
- implementation_risk
- privacy_or_contamination_cost
```

在无法建立完整效用模型时，可用一个操作性近似：

```text
approx_net_voi
= P(action_switch)
× decision_delta
× reuse_or_scale
× reversibility_factor
- total_information_cost
```

这只是排序启发式，不是精确数学等式。高风险、资金、生产发布或真实用户影响决策，应尽量使用明确的概率、损益和 Human Gate，而不是把高、中、低评分伪装成精确计算。

## 2. 信息的三种价值

先判断正在消费哪一种信息，避免把消费误认为决策。

| 类型 | 作用 | 默认处理 |
| --- | --- | --- |
| 决策信息 | 可能改变当前行动、优先级、资源配置或停止条件 | 进入 VOI 决策门 |
| 模型信息 | 暂不改变当前行动，但可能改善长期世界模型或未来判断 | 设学习预算、复用场景和复查日期 |
| 消费信息 | 提供娱乐、身份认同、社交谈资或情绪满足 | 可以消费，但不占用决策主线程 |

信息没有决策价值，不等于毫无价值。问题在于必须正确记账，不能用消费价值替代行动结果。

## 3. 信息之前先定义决策对象

没有决策对象，不启动无限调研。先写最小决策对象：

```yaml
decision:
  decision_id: "DEC-..."
  owner: ""
  deadline: ""
  decision_question: ""
  options: []
  current_default_action: ""
  stakes: ""
  reversibility: "reversible | costly_to_reverse | irreversible"
  boundary_status: "undefined | far | near | locked"
```

必须能够回答：

1. 现在到底要决定什么？
2. 不再获取信息时，会采取哪个默认行动？
3. 哪些替代行动仍然真实可选？
4. 最晚何时必须做决定？
5. 错误决定的主要代价是什么？
6. 决策是否可逆？

若这些问题无法回答，任务应进入有预算的探索，而不是伪装成决策调研。

## 4. 决策边界

VOI 通常在决策边界附近最高。

| 状态 | 含义 | 默认行动 |
| --- | --- | --- |
| `undefined` | 连决策、选项或默认行动都没有定义 | 先定义问题；限制探索预算 |
| `far` | 一个选项明显占优，常见信号很难改变行动 | 直接行动或只做轻验证 |
| `near` | 两个或多个选项接近，有限信息可能让行动翻转 | 优先获取高 VOI 信息 |
| `locked` | 决策已承诺、不可逆或窗口已关闭 | 停止为旧决策继续搜集信息；转向执行或复盘 |

判断是否接近边界，不看主观纠结程度，而看合理的信号是否会改变行动。

## 5. 不确定性地图

只追踪可能改变行动的不确定性：

```yaml
uncertainty_map:
  - uncertainty: ""
    current_belief_or_range: ""
    confidence: "low | medium | high"
    impact_if_wrong: "low | medium | high"
    affected_options: []
    observable: true
    controllable: false
```

优先级通常来自：

```text
uncertainty_priority
≈ impact_if_wrong
× probability_current_model_is_wrong
× action_sensitivity
```

高不确定但低影响的变量可以使用默认假设。低不确定但高影响的变量可做轻量确认。高不确定且高影响的变量才值得投入显著成本。

## 6. 候选信息行动

信息不是抽象名词。必须把它写成可执行动作：看哪份日志、问谁、跑什么测试、观察哪组用户、做什么原型、检查哪个样本。

```yaml
information_action:
  action_id: "INFO-..."
  action: ""
  target_uncertainty: ""
  expected_signals: []
  reliability_and_bias: ""
  acquisition_cost: ""
  latency_cost: ""
  attention_cost: ""
  risk_or_contamination: ""
```

高 VOI 信息常有这些特征：

- 本地：来自当前团队、用户、项目、日志、代码、原型和真实约束；
- 专门：针对当前选项和不确定性，而不是泛泛行业叙事；
- 反常：能挑战现有先验，包含负反馈、失败信号或不舒服的证据；
- 边界化：可能让当前行动翻转；
- 可执行：获得后能立即改变下一步，而不是只增加谈资；
- 有时效：在决策窗口关闭前获得，且不会因延迟失效。

## 7. 信号—行动映射

这是 VOI 决策门最重要的一步。对每个候选信息行动，写出可能信号及其对应动作：

| 可能信号 | 后验如何更新 | 看到后采取什么行动 |
| --- | --- | --- |
| 支持当前方案 | 当前方案成功概率提高 | 继续、加注或缩短下一轮验证 |
| 反对当前方案 | 当前方案成功概率下降 | 换方案、缩减范围、回滚或停止 |
| 模糊/无效 | 不确定性没有显著下降 | 不继续购买同类信息，换探针或按默认行动推进 |

如果所有信号对应的行动都一样，则：

```text
could_change_action = false
current_decision_voi ≈ 0
```

此时应停止调研，或把它明确归类为模型学习/信息消费。

## 8. EVPI、EVPPI、EVSI 与净样本价值

### EVPI：完全信息期望价值

```text
EVPI
= E_θ [ max_a U(a, θ) ]
- max_a E_θ [ U(a, θ) ]
```

EVPI 是消除全部不确定性的价值上界。任何调研、测试或报告的价格都不应高于其可影响决策的 EVPI。现实里完全信息很少可得。

### EVPPI：部分完全信息价值

EVPPI 只消除一个变量或一组变量的不确定性，用来判断最值得研究哪个不确定性。

### EVSI：样本信息期望价值

```text
EVSI
= E_X [ max_a E[U(a, θ) | X] ]
- max_a E_θ [ U(a, θ) ]
```

`X` 是尚未观察到的实验、抽样、试玩、A/B、访谈或日志样本。EVSI 衡量一个具体研究设计降低决策错误的期望价值。

### 净样本价值

```text
ENBS_or_net_EVSI
= EVSI
- study_cost
- delay_cost
- operational_risk
```

默认原则是用最小、最快、可回滚的样本信息降低重大决策的不确定性，而不是等待不存在的上帝视角。

## 9. 八步 VOI 决策门

### 第一步：Decision

定义决策、选项、默认行动、截止时间、可逆性和损失函数。

### 第二步：Boundary

判断 `undefined / far / near / locked`。只有 `near` 通常值得高强度信息投入。

### 第三步：Uncertainty

列出会影响选项排序的关键不确定性。删掉无法改变行动的变量。

### 第四步：Information Actions

最多生成 3 个候选信息行动，优先本地证据、负反馈和最小实验，避免 AI 无限制扩展研究清单。

### 第五步：Signal-to-Action

为候选信号预注册行动。没有行动差异的信息不进入决策调研。

### 第六步：Value and Cost

估算 EVPI 上界、样本价值、获取成本、延迟、注意力、隐私和污染风险。

### 第七步：Probe

选择净价值最高的最小探针。探针应尽可能可逆、可快速观察，并只改变一个关键判断。

### 第八步：Stop and Record

满足任一条件就停止继续收集信息：

- 最优行动在合理信号范围内不再翻转；
- 下一份信息的边际 VOI 不高于边际成本；
- 已达到预注册的样本量或证据门；
- 决策截止时间到达；
- 剩余不确定性不会改变行动；
- Human Gate 已做出承诺，任务转入执行。

记录先验、信号、后验、行动变化、剩余不确定性和停止理由。

## 10. AI 工作流中的 VOI

AI 极大降低了生成信息的成本，却没有自动降低人类判断信息价值的成本。每个新方案、对话和分支都会制造待处理决策，因此系统必须主动关闭低 VOI 分支。

默认规则：

- 每个 AI 对话先声明要支持的决策或产物；
- 没有决策对象时，只允许有时间盒和预算的探索；
- 每轮最多提出 3 个真正可选的信息行动；
- 不重复搜索无法改变当前行动的宏观材料；
- 优先读取当前项目数据、失败轨迹、用户负反馈和局部约束；
- 输出必须说明停止什么、开始什么、加注什么、放弃什么或验证什么；
- 若输出不改变行动，明确标记为 `model_learning` 或 `information_consumption`；
- 高风险写入、发布、资金、生产改动仍经过 Human Gate。

### AI 疲劳 Gate

当出现大量打开的对话、候选方案或未处理产物时，先执行：

```text
open_branches
-> map each branch to a decision
-> keep branches that may change action
-> archive model-learning branches
-> close consumption branches
-> choose one next probe
```

AI 疲劳常来自未收束的低 VOI 可能性，而不只是任务数量。

### 反 AI 味 Gate

高结构不等于高信息价值。改写或总结时必须保留：

- 具体场景、对象、时间、约束和局部数据；
- 负反馈、反例、失败细节和不舒服的信号；
- 信息如何改变行动；
- 尚未得到证明的边界。

若一段话删除具体细节后仍然完全成立，它可能只是低 VOI 的通用正确话。不要把一条关键本地事实润色成宏大空话。

## 11. GameDesignOS 中的应用

### 创意到验证

决策不是是否喜欢这个创意，而是优先验证哪个玩家承诺、核心循环或生产风险。使用 EVSI 选择最小原型、概念测试或访谈。

### 媒体到诊断

只收集会改变 issue priority、修改方案或下一轮验证的证据。样本无法支持的留存、收入和真实手感判断必须保持未知。

### 体验浓度实验

用样本价值比较 A/B 变体、遥测或试玩方案。每个实验必须说明结果如何触发 amplify、iterate、observe、rollback 或 kill。

### 证据到策划案

缺失材料只有在会改变 Go/No-Go、范围、预算、里程碑或 pitch 请求时才值得补。不能把更多调研自动当成更专业。

### 系统演化

在修改 prompt、memory、router、schema、eval 或 skill 前，先判断新信息或新规则能否改变提升决策。一次漂亮案例不是高 VOI 的长期证据；重复失败、高影响回归和跨任务行为样本更重要。

## 12. 常见失败模式

| 失败模式 | 症状 | 修复 |
| --- | --- | --- |
| FOMO 调研 | 追热点但没有决策对象 | 定义决策，否则设消费预算并停止 |
| 研究戏剧 | 调研本身替代行动 | 预注册信号—行动映射和截止时间 |
| 确认偏误 | 只找支持现有方案的信息 | 主动寻找最可能推翻当前方案的信号 |
| 选项爆炸 | AI 不断生成新方案 | 限制真实选项和候选信息行动数量 |
| 信息洗平 | 具体负反馈被改写成通用结论 | 保留本地事实、来源和行动影响 |
| 虚假精确 | 用无依据百分比包装直觉 | 标明近似、范围和敏感性 |
| 延迟忽视 | 忽略信息过期和错过窗口 | 把 latency cost 纳入净 VOI |
| 低价值重复 | 多份材料不会改变行动 | 触发停止规则 |
| 决策锁定后继续搜 | 已承诺仍为旧选择找论据 | 转向执行指标或复盘，不继续购买旧决策信息 |
| 高 VOI 无行动 | 获取了关键信号但没有改变流程 | 把行动写进 Human Gate 或 if-then 协议 |

## 13. 行为 Eval

一个合格的 VOI 输出至少满足：

1. 有明确决策对象、选项和当前默认行动；
2. 判断了决策边界，而不是只描述不确定性；
3. 每个信息行动都绑定目标不确定性；
4. 至少写出一个可能改变行动的信号；
5. 说明信息成本、延迟和风险；
6. 区分 EVPI 上界与现实 EVSI；
7. 选择最小高价值探针；
8. 有停止规则；
9. 获取信息后记录后验和行动变化；
10. 没有用更多研究替代拍板。

以下输出应判失败：

- 提供长篇资料清单，却没有说明要改变哪个决策；
- 把信息真实性直接等同于信息价值；
- 建议继续调研，但没有可能信号和行动分支；
- 忽略注意力、延迟、隐私或污染成本；
- 把一次案例直接提升为长期规则；
- 把本地负反馈洗成抽象、无行动含义的总结。

## 14. 来源与适用边界

本 playbook 的正式定义参考 Ronald A. Howard 的信息价值理论，以及后续关于 EVPI、EVPPI、EVSI 与净样本价值的决策分析研究。GameDesignOS 中的高/中/低评分、决策边界分类和近似公式是工程化启发式，用于快速排序，不替代高风险场景的完整统计决策模型。

建议参考：

- Ronald A. Howard, Information Value Theory, IEEE Transactions on Systems Science and Cybernetics, 1966, DOI: 10.1109/TSSC.1966.300074.
- Mark Strong et al., Estimating the Expected Value of Sample Information Using the Probabilistic Sensitivity Analysis Sample, Medical Decision Making, 2015, DOI: 10.1177/0272989X15575286.
- Natalia Kunst et al., Computing the Expected Value of Sample Information Efficiently, Value in Health, 2020, DOI: 10.1016/j.jval.2020.02.010.
