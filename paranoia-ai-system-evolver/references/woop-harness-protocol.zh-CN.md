# WOOP Harness Protocol

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

## 1. 定位

WOOP 在 AI harness 中不是心理激励，而是一套任务进入、执行校验、失败恢复的控制协议。

外部参考：

- Harness engineering 把 model 之外的 guide、sensor、tooling、feedback loop 看成让 agent 更可信的外层系统：<https://martinfowler.com/articles/harness-engineering.html>
- WOOP 的四步是 Wish、Outcome、Obstacle、Plan，并要求按顺序完成：<https://woopmylife.org/en/practice>

本 skill 只吸收它们的工程含义：把愿望、结果、障碍和计划转成 harness 能识别、能触发、能执行、能记录的控制面。

## 2. 四个工程模块

| WOOP | 人的用法 | AI harness 中的模块 | 控制作用 |
| --- | --- | --- | --- |
| Wish | 想达成什么 | `Intent Spec` | 定义目标、输出物、边界和停止条件 |
| Outcome | 成功后的好结果 | `Evaluation Rubric` | 定义验收画面、评分尺和价值函数 |
| Obstacle | 内在障碍 | `Failure Pattern` | 定义人机协作里高概率会坏的模式 |
| Plan | if-then 计划 | `If-Then Protocol` | 定义触发器、校验器、重试、降级和 Human Gate |

WOOP 放在 OODA 之前，给任务一个可执行入口；也放在 Evaluate 阶段，帮助判断是否已经触发失败模式。

## 3. Obstacle 必须写成内在失败模式

不要把 Obstacle 写成外部困难。外部困难只能解释“为什么难”，不能告诉 harness “何时触发、触发后做什么”。

更好的写法是把外部困难翻译成人机系统的内在失败模式：

| 不适合的 Obstacle | 可进入 harness 的 Failure Pattern |
| --- | --- |
| 资料不足 | 资料不足时，我容易让 AI 脑补，并因为答案流畅就接受 |
| 时间太少 | 时间紧时，我会省掉校验，只看结论不看依据 |
| AI 幻觉 | 当 AI 给出自信解释时，我容易把流畅度误判成真实性 |
| 任务太复杂 | 任务复杂时，agent 容易把局部完整性当成整体正确 |
| 工具很多 | 可用工具很多时，agent 容易过度调用工具，忘记 VOI |
| 需求变动 | 用户追加细节时，agent 容易目标漂移，忘记原始 Outcome |

好的 Failure Pattern 必须满足三点：

- 可识别：有明确触发信号。
- 可干预：有可执行动作。
- 可回放：能在 trace 或 eval 中被复盘。

## 4. WOOP Task Card

每个复杂任务进入生产模式前，至少填到这个粒度：

```yaml
woop_task_card:
  wish:
    intent_spec: ""      # 真正要完成什么
    output_artifact: ""  # 交付物是什么
    scope_boundary: ""   # 到哪里为止，不做什么
    stop_condition: ""   # 何时停止或交还给人
  outcome:
    decision_value: ""   # 成功后帮助人做什么决策或动作
    acceptance_rubric:
      - ""
      - ""
      - ""
  obstacle:
    failure_patterns:
      - pattern: ""      # 内在失败模式
        trigger: ""      # 何时判断它出现
        severity: "low | medium | high"
  plan:
    if_then_protocols:
      - if: ""           # 触发条件
        then: ""         # 具体动作
        judge: ""        # agent | user | validator | test | reviewer
        next_step: "continue | retry | rewrite | verify | ask_human | rollback"
```

## 5. 任务准入规则

用 WOOP 先决定任务能否开始：

| 缺失项 | 默认动作 |
| --- | --- |
| Wish 不清楚 | 先澄清、拆小或进入探索模式 |
| Outcome 不清楚 | 不进入生产模式，只能做候选草案或补验收标准 |
| Obstacle 不清楚 | 套用默认 Failure Pattern，并降低自主性 |
| Plan 不清楚 | 不自动执行 A3/A4 或不可逆动作 |

默认 Failure Pattern 可以从这些项里选择：

- 流畅度被误判成真实性
- 目标漂移
- 把资料整理误认为洞察
- 工具调用过度或过早
- 上下文污染
- 局部优化
- 无停止条件
- 评价器被格式骗过
- 用户想快速通过而省掉校验

## 6. 执行监控

每完成一个阶段，都做两件事：

1. 用 Outcome 打分：结果是否满足最初的验收画面、决策收益或行动价值？
2. 用 Obstacle 查风险：是否触发了预设 Failure Pattern？

如果触发 Obstacle，不要继续美化答案；先执行 Plan。例子：

- 事实性判断没有来源：停止生成，要求来源、不确定性、推断链分栏。
- 输出超过 800 字但没有核心结论：先压缩成 30 字 thesis。
- 方案出现多个并列系统但没有核心循环：要求指出唯一核心循环和放弃项。
- 连续三轮只在微调措辞：停止生成，评价这件事是否值得继续。
- AI 开始迎合用户预设：切换为反方审稿人或红队检查。

## 7. 失败恢复

Plan 必须小到能执行。不要写“保持批判性”，要写触发条件和动作。

常用 If-Then Protocol：

```text
If 事实性判断没有真源,
Then 标注 source / uncertainty / inference，必要时降级为假设。

If 用户或 agent 想跳过验证,
Then 至少跑一个轻量反例或 red-team check。

If 输出看似完整但没有决策张力,
Then 删除装饰性模块，只保留 1 个核心循环和 2-3 个取舍变量。

If 工具调用成本高但不会改变决策,
Then 记录低置信假设并继续，不调用工具。

If 高影响动作缺少 rollback,
Then 停在 candidate，交给 Human Gate。
```

## 8. 与 VOI/OODA/Eval 的关系

WOOP 不替代 VOI/OODA/Eval，而是给它们提供任务控制面：

- WOOP 定义入口：要去哪、什么叫好、哪里会坏、坏了怎么办。
- VOI 决定信息动作：是否值得查、问、读、测。
- OODA 执行循环：用现实反馈刷新 Orient。
- Eval 判断候选改动：是否真的提高结果、过程或演化质量。
- Human Gate 决定长期提升：是否允许从 `candidate` 变成当前规则。
- Rollback 保证恢复：触发失败时能退回上一版，不靠人记忆。

## 9. 记录与回写

任务结束时，记录真实触发过的 Obstacle：

```yaml
woop_trace:
  triggered_obstacles:
    - pattern:
      trigger_seen:
      plan_executed:
      outcome_after_plan:
      should_become_candidate_rule: true | false
```

只有当失败模式重复出现、高影响、可复用、可回滚，并且有 eval 或行为样本时，才进入 meta OODA 成为 `candidate`。长期记忆、全局 skill 或生产策略的回写必须经过 Human Gate。
