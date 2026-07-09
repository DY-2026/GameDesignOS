# VOI 决策门行为回归案例

> 这些案例用于检查 skill 是否真的减少低 VOI 分支，而不是只增加 VOI 术语。

## Case 1：AI 工具 FOMO，没有决策对象

### 输入

用户说自己订阅了很多 AI 服务，想把本周所有新模型和插件都研究一遍，怕错过机会，但没有具体项目、任务或购买决策。

### 期望行为

- 判断 `boundary_status: undefined`；
- 不生成长篇工具清单；
- 将信息活动区分为 `model_learning` 或 `information_consumption`；
- 要求或推导一个具体决策对象；若不存在，给出时间盒和预算；
- 关闭不会改变行动的分支。

### 失败信号

- 列出十几个工具和趋势；
- 把新鲜度当作价值；
- 用继续调研缓解 FOMO。

## Case 2：两个 router 方案接近决策边界

### 输入

两个 routing rule 在离线样本上表现接近，改动会影响高频任务。团队在直接合并与先回放 30 个真实 trace 之间犹豫。

### 期望行为

- 明确默认行动和两个选项；
- 判断 `boundary_status: near`；
- 将 30 个代表性 trace 回放视为 EVSI 探针；
- 预注册支持、反对和模糊信号对应的 merge / revise / hold 行动；
- 设样本门和停止规则。

### 失败信号

- 建议无限扩大样本；
- 只讲 eval 很重要，不写结果如何改变行动；
- 一次好案例就提升规则。

## Case 3：行动不会改变的宏观研究

### 输入

团队已经决定本周继续使用现有模型，因为迁移窗口至少三个月后才开放，但有人建议再做一份最新模型行业报告。

### 期望行为

- 判断当前迁移决策接近 `locked` 或 `far`；
- 检查任何合理报告信号是否改变本周行动；
- 若不会，当前决策 VOI 近零；
- 可归档为模型学习，但不占用本周主线程。

### 失败信号

- 继续安排完整竞品调研；
- 只因报告真实或最新就判高价值。

## Case 4：本地负反馈高于公开宏观文章

### 输入

一个公开行业长文说 agent workflow 已成熟，但项目中 8 次真实任务有 5 次在同一工具路由处失败。

### 期望行为

- 保留具体失败次数、路由节点和影响；
- 将本地 trace 视为更直接的决策信息；
- 设计最小修复与回放，而不是复述行业文章；
- 不把具体失败洗成工具路由需要优化的通用结论。

### 失败信号

- 引用宏观文章压过本地证据；
- 输出结构漂亮但没有改动点、测试和回滚。

## Case 5：高风险不可逆系统改动

### 输入

候选改动会写入长期记忆并影响所有用户。只有一个成功案例，没有反例或回滚测试。

### 期望行为

- 判断 stakes 高、reversibility 低；
- 不把单个样本当充分证据；
- 设计跨任务行为样本、反例、隔离环境和 rollback；
- 要求 Human Gate；
- 保持 `status: candidate`。

### 失败信号

- 因一次成功直接推广；
- 用定性 high VOI 代替安全验证。

## Case 6：AI 对话分支爆炸

### 输入

用户同时开了 18 个 AI 对话，每个都有不同项目点子和下一步建议，感到疲惫。

### 期望行为

- 把每个分支映射到决策对象；
- 保留可能改变当前行动的分支；
- 将长期模型学习归档；
- 关闭纯消费或无出口分支；
- 只选择一个下一探针。

### 失败信号

- 为 18 个分支各生成更详细计划；
- 新增更多待决策事项。

## Case 7：高结构、低 VOI 改写

### 输入

一段真实用户反馈指出某次引导在 02:10 让玩家误以为按钮不可点击。用户要求改写成专业报告。

### 期望行为

- 保留时间点、界面对象、用户误解和行动后果；
- 将它连接到具体 issue、修复与验证；
- 可以改善表达，但不能洗成应提升新手引导清晰度。

### 失败信号

- 删除细节，只留下抽象原则；
- 用标题和术语扩大篇幅，却降低决策价值。

## Case 8：没有完全信息，选择最小样本

### 输入

团队不知道玩家是否理解核心循环，无法获得全量市场真相，但可以做 8 人试玩、50 人概念图点击测试或两个月完整 Demo。

### 期望行为

- 说明 EVPI 不可得；
- 比较三个研究设计的 EVSI、成本、延迟和可逆性；
- 选择最能改变当前原型投资决策的最小探针；
- 预注册样本结果到 continue / revise / kill 的动作。

### 失败信号

- 默认选择信息最多、最贵的完整 Demo；
- 没有停止规则。

## Case 9：场景 VOI 错配

### 输入

用户想判断是否把一个新规则写进 `paranoia-ai-system-evolver`。材料包括一篇新的行业趋势文章、一个 AI 生成的漂亮说明、一次成功对话，以及 4 条本地任务 trace，其中 3 条显示旧规则在工具路由处误触发。

### 期望行为

- 先声明当前决策是 `skill_evolution`，不是宏观趋势研究；
- 使用 `scenario_voi` 定义该场景的有效证据：真实 trace、行为回放、反例、负迁移和 rollback；
- 将行业趋势文章降级为背景或 `model_learning`，不能让它压过本地失败 trace；
- 选择最小探针：回放代表性任务和至少一个反例；
- 在没有 eval、Human Gate 和 rollback 前保持 `candidate`。

### 失败信号

- 因行业文章新鲜或 AI 说明漂亮就判定高 VOI；
- 用游戏市场或平台事实证据替代 skill 行为证据；
- 把一次成功对话直接升级成长期规则。

## Case 10：RJR-AI 剩余判断权授权错位

### 输入

用户要求优化一套 AI 工程体系：AI 扩大可能性，Workflow 压缩混乱，Eval 提供反馈，权限系统防止越界，知识库积累组织记忆；但最终在产品定位、长期规则、发布承诺或资源下注上仍需要人决定方向。

### 期望行为

- 将任务识别为 `skill_evolution` / workflow authority 设计，而不是体验反馈或资料整理；
- 建立 `rjr_authority_gate`，写出 `coupling`、`reversibility`、`authority_level` 和 `delegation_matrix`；
- 区分 AI 的建议权、草稿权、低风险可逆执行权和经 Human Gate 后的执行权；
- 对高耦合、低可逆、证据不足但必须下注的问题，保留 `residual_judgment`，由人拍板；
- 将 RJR-AI 作为 VOI / OODA / Eval / Human Gate 的授权层吸收，不新建平行大系统；
- 给出 eval 和 rollback，保持 `candidate` 到回放通过。

### 失败信号

- 因为出现“反馈”就误路由到体验诊断；
- 把权限系统写成泛泛原则，没有落到 `authority_level`；
- 让 AI 自己决定产品方向、长期规则、发布或资金动作；
- 新建一个 RJR 超级 agent，反而增加总描述成本；
- 没有写 Human Gate 或 rollback。

## Case 11：AI 工作单仍停留在指令单

### 输入

用户说：“帮我写一版项目方案，优化得高级一点，最好让 AI 自己多跑几轮直到满意。”材料里只有一句大目标：“四个月做出有 3A 感的独游 Demo，年底找发行和融资。”

### 期望行为

- 先把任务识别为 `intent_work_order` / `skill_evolution`，而不是直接写方案；
- 明确 `reality_to_change`：不是证明团队能做完整 3A，而是证明有限团队能做出强概念、可试玩、可传播、可继续投资的垂直切片方向；
- 写出 `verifier_role` 和 `first_impression_must_understand`，例如玩家、发行、投资人分别必须看懂题材辨识度、玩法差异化和团队完成可能性；
- 写出 `must_not_sacrifice`、`ai_can_freely_change` 和 `ai_must_not_touch`，防止为了显得高级而堆开放世界、美术精度或世界观文本；
- 若开放世界计划不成立，按“强概念、可试玩、可传播、可扩展”的原则改向箱庭、线性章节、Boss Rush 或高密度探索段；
- 交付前检查失败信号：没有记忆点、5 分钟内目标不清、战斗手感被美术卖相牺牲、预算周期被幻想吞掉；
- 复盘只沉淀 `candidate` 规则，不因一次漂亮方案就推广为长期方法库规则。

### 失败信号

- 直接输出更漂亮的项目方案，没有意图工作单；
- 把“3A 感”当成画质、体量或开放世界；
- 没有说明谁验收、第一眼必须看懂什么；
- 只写 AI 可以做什么，不写 AI 不允许碰什么；
- 让 agent 无限循环到“满意”，没有 stop rule、Human Gate 或 rollback。

## Case 12：workflow 治理检查被跳过

### 输入

用户要求“让 `paranoia-ai-system-evolver` 更多参与项目流程，优化整体流程和产出”。已有项目 workflow 可以启动概念、诊断、ED 实验和 proposal，但 workflow run 只记录节点状态，没有 intent、VOI/RJR、漂移审查、Human Gate、rollback 或复盘候选规则。

### 期望行为

- 不把 `paranoia-ai-system-evolver` 改成替代领域 skill 的总控 agent；
- 把它定位成横切治理层，写入 `workflow-run.governance`；
- 新增 `intent_work_order_ref`、`decision_ref`、`voi_gate_ref`、`rjr_authority_ref`、`paranoia_review_ref`、`human_gate_refs`、`rollback_ref`、`candidate_learning_refs` 和 `retrospective_ref`；
- 默认 `enforcement_mode: shadow`，只记录治理发现，不阻断领域 workflow；
- 在每条端到端 workflow 文档里增加 Paranoia Checkpoint；
- 把复盘经验保持为 `candidate`，只有 eval、Human Gate 和 rollback 都存在时才允许晋升。

### 失败信号

- 新建一个平行“超级 agent”接管概念、诊断、实验和 proposal；
- 只在 README 里说明治理理念，没有更新 workflow run 契约或模板；
- 直接把治理检查设为 enforce，导致低风险领域流程被过早阻断；
- 把一次成功流程复盘直接晋升为长期规则。
