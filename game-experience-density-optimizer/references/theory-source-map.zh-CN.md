# 理论来源映射

本文档记录本 skill 的外部理论来源、转译方式和边界。它不是参考文献综述，而是防止误用理论的 source map。

## 使用边界

所有理论都只作为游戏设计启发式使用。输出必须保留：

```yaml
theory_status: design_hypothesis
```

不要把下列来源写成“已证明会提升留存”“神经科学证明会进入心流”“心理学量表评分”。本 skill 的真正产物仍然是可上线、可埋点、可复盘、可回滚的设计实验。

## 来源与转译

| 来源 | 稳定结论/启发 | 在本 skill 中的用法 | 禁止误用 |
| --- | --- | --- | --- |
| Optimal Stimulation Level / OSL 文献与 variety seeking 综述 | 人会在太低与太高刺激之间寻找适合自己的刺激水平；刺激不足会导致寻求变化，刺激过高会导致回避 | 建立 `optimal_stimulation_fit`，先区分低刺激、过载、习惯化、低能动性、低意义感 | 把“无聊”直接等同于刺激不足 |
| Friston 的 Free-Energy Principle | 认知系统可被理解为通过感知和行动降低不确定性/预测误差 | 把游戏转译为可控预测误差训练场，建立 `free_energy_window` | 写成神经科学证明或留存必然提升 |
| Predictive Processing in video games | 游戏可以提供可消费的不确定性，玩家会享受比预期更有效地降低不确定性 | 支撑“可控惊讶”“自由能斜坡”“成长是处理更高阶惊讶” | 把随机、噪声、惩罚都叫挑战 |
| Markov blanket / Active inference | 系统通过感官状态与行动状态和外界耦合 | 把 UI、音效、镜头、反馈视为感官状态；把按键、Build、资源分配视为行动状态 | 把“马尔可夫毯”当玄学标签，或用它允许多系统乱改 |
| GameFlow | 享受与注意力、挑战/技能匹配、控制、目标、反馈、沉浸、社交等门槛相关 | 建立 `motivation_flow_gate`，防止 ED 只追求更密更刺激 | 用 flow 语言掩盖目标不清或反馈不清 |
| SDT 游戏研究 | 游戏动机可从自主、胜任、关系等需要满足理解 | 检查 autonomy、competence、relatedness，防止强迫式留存方案 | 把红点、焦虑或不可逆损失写成自主 |
| SDT novelty candidate need | 新颖性可能是动机支持因素，但证据仍是候选性质 | 在 `motivation_flow_gate` 中加入 `optimal_novelty_fit` | 把 novelty 写成越多越好 |
| Silvia 的 interest appraisal | 兴趣通常同时需要新颖/复杂和可理解/可应对 | 把有效新颖定义为半熟半新、可归因、可学习、可行动、可复盘 | 把信息轰炸、不可解释随机和换皮写成兴趣 |

## 核心整合

理论层级如下：

```text
OLSO：当前玩家和情境的刺激窗口是否匹配
FEP/PP：刺激是否成为可消化的预测误差
Markov blanket：玩家通过哪些感官/行动边界接收和调节刺激
GameFlow/SDT：目标、控制、自主、胜任、关系和最佳新颖性是否被保护
ED：把诊断编译成一个主旋钮、变体、埋点、看板和预注册决策
```

因此，本 skill 的独特性不是“懂很多理论”，而是把这些理论压成一个执行顺序：

```text
先判窗口 -> 再降噪 -> 再提质 -> 后调频 -> 埋点验证 -> 预注册决策
```

## 公开来源

- Optimal stimulation / variety seeking review: https://pmc.ncbi.nlm.nih.gov/articles/PMC9207504/
- Steenkamp & Baumgartner OSL consumer behavior entry: https://www.researchgate.net/publication/24098751_The_Role_of_Optimum_Stimulation_Level_in_Exploratory_Consumer_Behavior
- Friston FEP paper: https://www.nature.com/articles/nrn2787
- Predictive processing and video games: https://pmc.ncbi.nlm.nih.gov/articles/PMC9363017/
- GameFlow paper: https://www.valuesatplay.org/wp-content/uploads/2007/09/sweetser.pdf
- Ryan/Rigby/Przybylski SDT games paper entry: https://cir.nii.ac.jp/crid/1363951796172665984?lang=en
- Novelty in SDT: https://www.sciencedirect.com/science/article/pii/S0191886916307863
- Silvia interest appraisal entry: https://www.researchgate.net/publication/7979583_What_Is_Interesting_Exploring_the_Appraisal_Structure_of_Interest
