# game-experience-density-optimizer

`game-experience-density-optimizer` 是“体验浓度”skill。英文技术名保留 `Experience Density / ED`，但中文概念统一叫“体验浓度”。

它用于把留存、单机总游戏时长、买断制完成率、手游每日留存、节奏、首局上头感、中段疲劳、最佳刺激窗口、低刺激无聊、过载无聊、习惯化、交互反馈、具身感、氛围感、认知负荷、自由能区间、预测误差和玩家-游戏输入输出边界问题，改造成一周能跑完的 ED 实验。

它不是泛泛的留存建议生成器，也不是“把游戏做得更快”的工具。它的核心任务是先判断玩家是否处在合适的刺激窗口，再把体验问题拆成五个可控项：`MD/min`、`SF`、`EB`、`AR`、`CLP`，用 FEP/马尔可夫毯镜头检查可承受预测误差和行动-反馈耦合，最后给出可上线变体、埋点字典、看板字段、预注册判定规则和回滚条件。

<p align="center">
  <img src="../assets/showcase-game-experience-density-optimizer.png" alt="Game Experience Density Optimizer showcase" width="100%">
</p>

## 定位

这个 skill 面向游戏策划、制作人、数据分析、独立开发者和 AI agent。它适合处理已经有原型、Demo、线上版本、测试录像、数据快照或明确体验问题的项目。

它解决的是从“感觉体验不够浓”到“本周怎么改、怎么测、怎么回滚”的断层。很多设计建议听起来对，但无法上线验证；很多 A/B 测试能跑数据，却不知道设计上到底改了什么。这个 skill 要让二者咬在一起。

它的独特价值是把模糊主观体验编译成可验证实验：

```text
主观体验问题 -> 玩家/情境边界 -> 最佳刺激窗口 -> 公式项诊断 -> 指标周期门 -> 一个主旋钮 -> 可上线变体 -> 埋点/看板 -> 预注册决策
```

它不是游戏设计百科，也不是 FEP/心流/SDT 理论解释器。理论只作为诊断门：帮助判断为什么淡、为什么炸、为什么不跟手、为什么成长只是数字变大。最终产物必须是本周能做、能埋点、能复盘、能回滚的体验改动包。

核心原则：

- 中文统一叫“体验浓度”，英文可写 `ED / Experience Density`。
- 这是设计启发式，不是科学量表；输出需标注 `theory_status: design_hypothesis`。
- 体验浓度的完整定义是：当前玩家在当前情境下，单位时间内可吸收、可解释、可转化为探索/学习/意义的刺激密度。
- “无聊”不等于刺激太少；必须区分 `under_stimulation`、`over_stimulation`、`habituation`、`low_agency`、`low_meaning` 或 `unknown`。
- FEP/自由能和马尔可夫毯只作为设计隐喻：游戏是可控惊讶发生器，手感是玩家行动状态与游戏反馈状态的高质量耦合。
- SDT 中的新颖性必须是最佳新颖性：半熟半新、可归因、可学习、可行动、可复盘。
- 成长系统不是只让数字变大，而是设计自由能斜坡，让玩家逐步处理更高阶的惊讶。
- 先区分游戏形态：单机/买断制看总旅程、总游戏时长、章节推进和完成率；手游/liveops 才默认看 D1/D7、每日活跃和持续天数。
- 先写边界，再写判断。
- 先判窗口，再降噪，再提质，后调频。
- 高浓度不是绝对好，低浓度也不是绝对差；关键是浓度曲线和设计意图匹配。
- 有意义选择不是选项数量，可感知反馈不是光污染，具身感不是剧情代入，氛围感不是堆素材。
- 成功标准、负向指标、回滚条件必须在实验前写死。
- 任何指标建议都必须能落到对应游戏形态的埋点、看板和版本动作。
- 不使用暗黑模式、误导奖励、虚假倒计时或焦虑驱动。

## 工作公式

公式前必须先判断 `optimal_stimulation_fit`，否则容易把“过载导致的无聊”误修成“更多事件”。

```text
ED = MD/min * (SF + EB + AR) / CLP
```

| 缩写 | 含义 | 设计问题 |
| --- | --- | --- |
| `MD/min` | 每分钟有意义选择次数 | 玩家多久做一次能改变局势、收益、表达或下一段体验的选择 |
| `SF` | 可感知反馈 | 玩家是否看得见、听得出、感受得到，并能归因 |
| `EB` | 具身感加成 | 操控、角色、镜头、物理和触觉是否让玩家人机一体 |
| `AR` | 氛围感加成 | 音画、美术、环境、风格和 UI 是否自洽、有质感 |
| `CLP` | 认知负荷惩罚 | UI 混乱、规则不清、打断、噪音和学习成本是否稀释体验 |

## Case Visibility

skill 本身允许用户在自己的环境中处理真实项目、私有项目、客户项目、线上数据、公开案例或 synthetic cases。

输出时可以使用以下字段管理边界：

| 字段 | 可选值 | 用途 |
| --- | --- | --- |
| `case_visibility` | `private_user_work` / `public_repo_example` / `client_confidential` / `synthetic_case` / `unknown` | 说明案例可见性 |
| `data_sensitivity` | `none` / `telemetry_summary` / `raw_user_data` / `revenue_sensitive` / `unknown` | 说明数据敏感度 |
| `output_destination` | `private_notes` / `client_delivery` / `repo_example` / `public_post` / `unknown` | 说明交付去向 |
| `redaction_required` | `true` / `false` / `unknown` | 说明是否需要脱敏 |

公开仓库里的 examples、evals、assets、showcases 只能使用 synthetic、public、cleared 或标记 `needs_review` 的材料。真实项目数据、客户信息、未公开路线图、留存后台截图和收入数据不要提交到本公开仓库。

## 适用场景

- 首局 3-10 分钟太空，玩家没有形成再来一局动机。
- 新手期提示、剧情、战斗和奖励都存在，但体验不够浓。
- Demo 或测试版 D1 留存偏低，需要一周小改验证。
- 单机、买断制或 Steam Demo 想提升总游戏时长、Demo 完成率、章节推进或重玩意愿。
- 手游或 liveops 想提升 D1/D7、每日会话、持续活跃、活动留存或回流质量。
- 玩家觉得看不懂、太累、反馈弱、不跟手、世界很空。
- 玩家说无聊，但不确定是刺激不足、过载、习惯化、低能动性还是低意义感。
- 中段 15-30 分钟开始疲劳，需要局内节奏再点燃。
- 老玩家、赛季、刷子、肉鸽、UGC 或日常循环开始钝化，需要反习惯化而不是只加奖励。
- 回流用户进入后不知道该干什么，需要快速 rehook。
- 原型已经能玩，但不知道该优先降认知负荷、打磨反馈、强化具身感、补氛围还是调选择频率。
- 想把“无聊/崩溃/沉浸”转成 `too_low`、`too_high`、`optimal` 的自由能区间判断。
- 想把“不跟手/反馈乱/行动没影响”转成感官状态、行动状态和耦合断点。
- 需要给客户端、关卡、叙事、美术、音频、数据、QA 一份可执行实验包。

## 不适用场景

- 只有一句话创意，尚未定义核心循环。先用 `game-concept-architect`。
- 只有截图或 PV，无法判断真实节奏。先用 `game-experience-analyzer` 建立样本边界。
- 需要完整商业化设计、经济系统重构或长期版本规划。
- 想通过强红点、虚假稀缺、付费焦虑或误导性奖励提升指标。

## 输出模式

| 模式 | 用途 | 推荐交付物 |
| --- | --- | --- |
| `quick_ed_triage` | 快速判断体验浓度问题 | ED 诊断、公式项优先级、最小改动建议 |
| `weekly_ab_plan` | 设计一周实验 | A/B/C/D 变体矩阵、指标、埋点、回滚条件 |
| `instrumentation_plan` | 数据接线 | 事件字典、字段、触发时机、看板需求 |
| `review_and_decide` | 实验复盘 | 指标读法、胜负判断、放大/回滚/二次实验 |

如果用户只说提升留存或体验浓度，默认使用 `weekly_ab_plan`。如果用户只要很快判断问题，使用 `quick_ed_triage`。如果用户重点问埋点或看板，使用 `instrumentation_plan`。

## 与其他 skill 的配合方式

`game-experience-analyzer` 负责把录屏、截图、PV、试玩样本拆成证据化问题。`game-experience-density-optimizer` 负责把这些问题变成可上线实验。

推荐配合流程：

1. 用 `game-experience-analyzer` 输出样本边界、时间轴证据、功能账本和问题卡。
2. 把 P0/P1 问题卡输入 `game-experience-density-optimizer`。
3. 生成一周 ED 实验、埋点字典和看板字段。
4. 上测试服或灰度版本。
5. 用 `weekly-review` 模板复盘，再把结论回写到下一版设计。

## 文件结构

```text
game-experience-density-optimizer/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    ed-framework.zh-CN.md
    theory-source-map.zh-CN.md
    metric-horizon-by-game-model.zh-CN.md
    optimal-stimulation-window.zh-CN.md
    flow-sdt-experience-gates.zh-CN.md
    density-formula.zh-CN.md
    density-diagnosis-workflow.zh-CN.md
    free-energy-markov-blanket-lens.zh-CN.md
    interaction-prediction-lens.zh-CN.md
    weekly-experiment-sop.zh-CN.md
    lever-playbook.zh-CN.md
    telemetry-metric-dictionary.zh-CN.md
    retention-risk-gates.zh-CN.md
  templates/
    experiment-intake.md
    weekly-ed-experiment-plan.md
    variant-matrix.md
    instrumentation-dictionary.md
    dashboard-spec.md
    weekly-review.md
    experiment-plan.schema.json
  examples/
    synthetic-survivors-first-session-ed-plan.md
  evals/
    evals.json
    rubric.yaml
    negative_cases.md
```

## 验证

在仓库根目录运行：

```text
python scripts/validate_skill.py game-experience-density-optimizer
```
