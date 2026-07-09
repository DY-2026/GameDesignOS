# Intent Engineering Work Order

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. 定位

意图工程不是把 prompt 写得更漂亮，而是把一次 AI 工作从“帮我做某个动作”升级成“在明确边界内改变一个现实状态”。

```text
AI 工程 = 意图定义 + 情境供给 + 循环执行 + 验收标准 + 边界约束 + 复盘沉淀
```

`Intent Work Order` 放在 WOOP、Decision Object、RJR-AI、VOI 和 OODA 之前，负责回答：这件事到底要改变什么现实，谁来验收，AI 可以自治到哪里，什么时候必须停下来交还人。

它不是让 agent 无限自主。它的目标是减少人类微操，同时提高任务边界、验收画面、失败信号和回滚路径的清晰度。

## 2. 指令单与意图单

| 指令单 | 意图单 |
| --- | --- |
| 帮我写一版 | 写完后哪类人会改变判断或行动 |
| 帮我优化 | 哪个外部状态要变好，什么不能牺牲 |
| 帮我分析 | 分析要服务哪个决策，不分析什么 |
| 帮我出图 | 谁第一眼要看懂什么，哪些风格边界不能破 |
| 多给几个方案 | 哪些方案会改变下注，哪些只是信息消费 |

指令单容易让 AI 变成执行员：人不断拆任务、补边界、改措辞、追问细节。意图单让 AI 成为受控循环系统：agent 可以在授权范围内观察、判断、行动、验收和复盘，但不能越过 Human Gate。

## 3. 十个开工问题

每次启动复杂任务前，至少回答这些问题。回答不完整时，agent 应先降级为探索、草稿或澄清，不直接进入生产模式。

1. 我要改变什么现实？
2. 这个任务服务于哪个更大的项目目标？
3. 完成后，外部世界应该变成什么状态？
4. 谁是验收者？老板、投资人、玩家、主美、程序、我自己，还是另一个角色？
5. 验收者第一眼必须看懂什么？
6. 哪些东西绝对不能牺牲？
7. AI 可以自由改哪些东西？
8. AI 不允许碰哪些东西？
9. 如果原计划不成立，AI 应该依据什么原则改方向？
10. 交付前必须自查哪几个失败信号？

这些问题映射到现有控制层：

| 意图问题 | 落地层 |
| --- | --- |
| 现实改变、上级目标、外部状态 | `Intent Spec` 与 `Decision Object` |
| 验收者、第一眼必须看懂什么 | `Evaluation Rubric` |
| 不能牺牲、可自由改、不允许碰 | `RJR-AI authority gate` 与 `scope_boundary` |
| 改方向原则 | `If-Then Protocol` 与 `OODA Decide` |
| 失败信号 | `Failure Pattern`、eval 与交付前自查 |

## 4. 意图单最小结构

```yaml
intent_work_order:
  intent:
    reality_to_change: ""
    parent_project_goal: ""
    desired_world_state: ""
  acceptance:
    verifier_role: ""
    first_impression_must_understand: ""
    acceptance_criteria: []
    failure_signals_to_check_before_delivery: []
  boundaries:
    must_not_sacrifice: []
    ai_can_freely_change: []
    ai_must_not_touch: []
    cost_boundaries: []
  autonomy:
    authority_level: "P0_read | P1_suggest | P2_draft | P3_reversible_execute | P4_approved_execute"
    decision_principles_if_plan_breaks: []
    human_gate_triggers: []
    rollback_expectation: ""
  loop_contract:
    context_sources: []
    allowed_tools_or_actions: []
    loop_steps: ["observe", "orient", "decide", "act", "evaluate"]
    stop_conditions: []
  retrospective_contract:
    original_intent: ""
    completion_state: ""
    verified_judgments: []
    uncertain_items: []
    next_change: ""
    reusable_rules: []
    prompts_acceptance_or_failure_signals_to_promote: []
    promotion_status: "candidate"
```

## 5. 执行规则

### 5.1 先意图，后工具

如果用户只给出“写、优化、分析、出图、做 PPT、拆竞品”等动作，agent 应先把动作翻译为意图单。能从上下文合理推断的，不必反复问用户；但高风险边界必须进入 Human Gate。

### 5.2 先验收，后循环

没有验收者和第一眼必须看懂的内容，就不要进入长循环。否则 agent 会把“结构完整”误判成“结果有用”。

### 5.3 先边界，后自治

AI 的自由度来自边界清楚，而不是来自用户少说话。`ai_can_freely_change` 和 `ai_must_not_touch` 必须同时存在；只有前者没有后者，会制造越界风险。

### 5.4 原计划失败时按原则改向

意图单必须允许计划被现实推翻。改向不是逃避失败，而是继续服务原始意图。比如“开放世界做不动”时，可以收缩为箱庭、线性章节、Boss Rush 或高密度探索段，只要仍能证明核心钩子、可试玩、可传播、可扩展。

### 5.5 每轮复盘只沉淀候选规则

复盘要回答：

- 本轮任务的原始意图是什么？
- 实际完成到什么程度？
- 哪些判断被验证了？
- 哪些地方还不确定？
- 下一轮最应该改什么？
- 本次新增的可复用规则是什么？
- 哪些提示词、验收标准、失败信号应该沉淀进方法库？

除非已经有行为 eval、负迁移检查、Human Gate 和 rollback，否则新规则只能保持 `candidate`。

## 6. 独游立项例：把口号改成意图

原始指令：

```text
我们要做一个有 3A 感的国产独游，四个月内拿出 Demo，年底找发行和融资。
```

意图单应该改写为：

```text
我们不是要证明十人团队能做完整 3A，而是要证明这个团队能用有限成本做出一个 2027 年玩家一眼记住、发行和投资人相信的独游方向。
```

成功画面：

- 四个月后有 10 到 15 分钟垂直切片；
- 玩家第一眼能说出核心钩子；
- 试玩后能记住一个独特战斗或探索机制；
- 30 秒视频能传播；
- 发行和投资人能判断题材辨识度、玩法差异化和团队完成可能性。

不能牺牲：

- 不能为了像大作而堆无意义开放世界；
- 不能为了美术卖相牺牲战斗手感；
- 不能为了设定完整让玩家前 5 分钟不知道要干什么；
- 不能做什么都有但没有记忆点的中型 RPG；
- 预算、团队规模和周期不能被幻想吞掉。

AI 或团队可自由改：

- 题材、战斗形式、关卡结构、美术风格、叙事切入点；
- 只要仍能证明强概念、可试玩、可传播、可扩展。

这样 AI 或团队遇到计划失败时，不会死守“开放世界”这个表层方案，而会回到真实意图：用锋利的垂直切片证明项目值得继续投资。

## 7. 与现有 GameDesignOS 对象的关系

```text
Intent Work Order
-> WOOP Task Card
-> Decision Object
-> RJR-AI authority gate
-> VOI decision gate
-> OODA loop
-> acceptance check
-> retrospective
-> candidate learning record
```

意图单不替代 VOI，也不替代具体领域 skill。它只负责把“用户要 AI 做什么”提前翻译成“这个系统要改变什么现实，以及 agent 在什么边界内循环”。

## 8. 失败信号

交付前至少检查这些回归：

- 输出只是更长、更正式，但没有外部状态变化；
- 验收者不清楚，第一眼看不出重点；
- AI 自由改了边界外的东西；
- 为了完成表面任务牺牲了用户明说不能牺牲的东西；
- 原计划失败后继续硬跑，没有按原则收缩或改向；
- 复盘把单次经验直接升级成长期规则；
- 没有 Human Gate 却触碰发布、资金、账号、长期记忆、全局 skill 或不可逆项目承诺。

触发这些信号时，结果应降级为 `candidate` 或 `needs_rework`，而不是包装成完成。
