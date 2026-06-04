# game-experience-density-optimizer

`game-experience-density-optimizer` 是“体验浓度”skill。英文技术名保留 `Experience Density / ED`，但中文概念统一叫“体验浓度”。

它用于把留存、节奏、首局上头感、中段疲劳、交互反馈、具身感、氛围感和认知负荷问题，改造成一周能跑完的 ED 实验。

它不是泛泛的留存建议生成器，也不是“把游戏做得更快”的工具。它的核心任务是把体验问题拆成五个可控项：`MD/min`、`SF`、`EB`、`AR`、`CLP`，再给出可上线变体、埋点字典、看板字段、预注册判定规则和回滚条件。

<p align="center">
  <img src="../assets/showcase-game-experience-concentration-optimizer.png" alt="Game Experience Concentration Optimizer showcase" width="100%">
</p>

## 定位

这个 skill 面向游戏策划、制作人、数据分析、独立开发者和 AI agent。它适合处理已经有原型、Demo、线上版本、测试录像、数据快照或明确体验问题的项目。

它解决的是从“感觉体验不够浓”到“本周怎么改、怎么测、怎么回滚”的断层。很多设计建议听起来对，但无法上线验证；很多 A/B 测试能跑数据，却不知道设计上到底改了什么。这个 skill 要让二者咬在一起。

核心原则：

- 中文统一叫“体验浓度”，英文可写 `ED / Experience Density`。
- 这是设计启发式，不是科学量表；输出需标注 `theory_status: design_hypothesis`。
- 先写边界，再写判断。
- 先降噪，再提质，后调频。
- 高浓度不是绝对好，低浓度也不是绝对差；关键是浓度曲线和设计意图匹配。
- 有意义选择不是选项数量，可感知反馈不是光污染，具身感不是剧情代入，氛围感不是堆素材。
- 成功标准、负向指标、回滚条件必须在实验前写死。
- 任何留存建议都必须能落到埋点、看板和版本动作。
- 不使用暗黑模式、误导奖励、虚假倒计时或焦虑驱动。

## 工作公式

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
- 玩家觉得看不懂、太累、反馈弱、不跟手、世界很空。
- 中段 15-30 分钟开始疲劳，需要局内节奏再点燃。
- 回流用户进入后不知道该干什么，需要快速 rehook。
- 原型已经能玩，但不知道该优先降认知负荷、打磨反馈、强化具身感、补氛围还是调选择频率。
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
    density-formula.zh-CN.md
    density-diagnosis-workflow.zh-CN.md
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
