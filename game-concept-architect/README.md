# game-concept-architect

`game-concept-architect` 用于把一句话游戏创意扩展为完整但可验证的游戏设计蓝图。

它不是普通 GDD 生成器。核心任务不是“把创意写长”，而是先从创意中提取 concept seed，比较 design nucleus options，建立 assumption ledger，再定义玩家承诺、核心循环、scope gate 和 validation plan。

## 定位

这个 skill 面向游戏策划、独立开发者、制作人和 AI agent，适合把模糊创意变成可讨论、可删减、可验证、可进入原型制作的设计蓝图。

核心原则：

- 先拆 seed，再写方案。
- 先比较多个 design nucleus options，再选择方向。
- 先标注 assumptions 和 unknown，再写确定判断。
- 先定义玩家承诺，再展开系统。
- 题材、世界观、品类都不是设计核。
- 外部调研由 VOI 决定，不强制联网或泛搜。
- 所有新增系统必须能改变玩家行为、选择、节奏、成长或表达。
- 任何方案都必须经过 `scope gate` 和 `validation plan`。
- 能不能落地要同时看团队能力、内容产能、技术成熟度、时间成本和商业预期。

## Case Visibility

skill 本身允许用户在自己的环境中处理真实项目、私有项目、客户项目、公开案例或 synthetic cases。

输出时可以使用以下字段管理边界：

| 字段 | 可选值 | 用途 |
| --- | --- | --- |
| `case_visibility` | `private_user_work` / `public_repo_example` / `public_article` / `client_confidential` / `synthetic_case` / `unknown` | 说明案例可见性 |
| `output_destination` | `private_notes` / `repo_example` / `public_post` / `client_delivery` / `unknown` | 说明交付去向 |
| `redaction_required` | `true` / `false` / `unknown` | 说明是否需要脱敏 |

这些字段只用于输出管理，不限制用户在本地环境中使用真实或保密项目。只有提交到本仓库的 `examples/`、`assets/`、showcases、eval cases 需要遵守 [CONTRIBUTING.md](../CONTRIBUTING.md)。

## Public Base Skill / Private Overlay Pattern

本仓库只包含 public base skill：通用方法、可公开模板、synthetic examples、公开或 cleared 的说明材料。

用户可以在仓库外维护 private overlays，用于保存自己的私有项目、客户项目、工作室规则、个人偏好、真实案例和内部验证记录。

不要把 private overlays、client work、unreleased projects、真实项目代号、路线图、私有平台策略或可反推出真实项目的信息提交到本公开仓库。

## 适用场景

- 只有一句话创意，需要判断是否值得继续。
- 已有题材和品类，但玩法核不清楚。
- 想把“像某某游戏 + 某个题材”变成不复制原作内容、可验证的新设计。
- 需要比较多个设计核候选，而不是过早锁死一个方案。
- 独立游戏需要控制 MVP / Demo / Vertical Slice 范围。
- 微信小游戏、App、Steam、Web、主机等平台方向需要反推设计边界。
- AI agent 需要从一个 pitch 生成结构化设计案，而不是幻想型长文档。

## 不适用场景

- 只想生成世界观设定集。
- 只想写市场宣传文案。
- 已经有完整可测原型，只需要体验诊断。
- 需要数值表、关卡表、剧情脚本等生产细项，而没有先完成设计核验证。

## 输入示例

```text
做一个在废弃温室里培育机械植物、抵御夜间虫群的轻量策略防守游戏。
```

```text
做一个在梦境城市里投递信件、用卡牌改变街区规则的短局冒险游戏。
```

```text
做一个指挥三人小队在废弃太空站回收物资、每次行动都会改变站内结构的战术生存游戏。
```

## 输出模式

| 模式 | 用途 | 推荐交付物 |
| --- | --- | --- |
| `idea_triage` | 一句话创意的快速判断 | case visibility、seed、design nucleus options、unknown、external evidence status、下一步验证建议 |
| `one_page_pitch` | 轻量 pitch 或立项判断 | 一页 pitch、玩家承诺、核心循环、scope 摘要、验证计划摘要 |
| `full_design_brief` | 完整设计案 | seed、nucleus、assumptions、玩家承诺、循环、系统、平台商业、生产可行性、scope、风险、验证 |
| `vertical_slice_plan` | 进入原型制作 | 垂直切片目标、功能优先级、生产边界、里程碑、测试标准、下一步投入条件 |

如果用户只给一句话且没有指定完整方案，默认使用 `idea_triage`。如果用户说“完整方案 / 设计案”，使用 `full_design_brief`；如果用户说“做原型 / vertical slice / demo 计划”，使用 `vertical_slice_plan`。

## 输出示例片段

输入：

```text
废弃温室机械植物防守
```

输出片段：

```markdown
## Case Visibility

| 字段 | 值 |
| --- | --- |
| case_visibility | unknown |
| output_destination | private_notes |
| redaction_required | unknown |

## Concept Seed Extraction

| 字段 | 提取结果 | 确定性 | 影响 |
| --- | --- | --- | --- |
| 题材母体 | 废弃温室、机械植物、夜间虫群 | 中 | 中 |
| 玩法母体 | 轻量策略防守、格位培育、波次压力 | 中 | 高 |
| 情绪承诺 | 白天精打细算地培育，夜晚看防线在虫群压力下运转 | 高 | 高 |
| 差异化种子 | 植物不是静态塔，而是会随照料顺序改变功能的半机械生命体 | 中 | 高 |
| 关键 unknown | 变形是局内即时选择，还是局间 build 成长？ | unknown | 高 |

## Design Nucleus Options

| 候选 | 玩家行为变化 | 最大风险 | 最小验证 |
| --- | --- | --- | --- |
| 照料顺序改变植物形态 | 玩家不只是摆塔，而是在白天安排照料优先级 | 反馈不够清晰 | 3 种植物、2 种照料动作、2 波夜袭 |
| 温室布局改变夜间虫群路径 | 玩家用有限空间制造风险可控的防线 | 关卡设计成本上升 | 单屏 6x6 网格和两类虫群 |

## External Evidence Status

| 状态 | VOI 判断 | 下一步 |
| --- | --- | --- |
| not-run | 当前问题主要是设计核选择，外部调研暂不会改变最小原型 | 原型前再查塔防/培育混合品类评论动机 |
```

## 与 game-experience-analyzer 的配合方式

`game-concept-architect` 负责从 0 到 1 建立“该做什么、为什么做、如何验证”的设计架构。

`game-experience-analyzer` 更适合在已有原型、视频、试玩反馈或竞品体验之后使用，用来分析玩家实际体验是否兑现了承诺。

- GCA can export player-promise-contract.
- GEA can validate whether a prototype/video fulfills that contract.

推荐配合流程：

1. 用 `game-concept-architect` 生成 `idea_triage`、`one_page_pitch` 或 `vertical_slice_plan`。
2. 制作最小可玩原型。
3. 收集试玩录像、玩家反馈、指标数据。
4. 用 `game-experience-analyzer` 检查体验是否匹配宣传承诺、前 10 分钟承诺和长期承诺。
5. 把分析结论回写到 `assumption ledger`、`risk register` 和下一版 `validation plan`。

## 文件结构

```text
game-concept-architect/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    concept-seed-extraction.zh-CN.md
    core-loop-expansion.zh-CN.md
    design-nucleus-options.zh-CN.md
    external-feasibility-scan.zh-CN.md
    genre-fit-matrix.zh-CN.md
    platform-business-fit.zh-CN.md
    player-promise-framework.zh-CN.md
    production-feasibility.zh-CN.md
    production-profile-gate.zh-CN.md
    prototype-validation-gate.zh-CN.md
    reference-game-boundary.zh-CN.md
    scope-gate.zh-CN.md
    voi-feasibility-gate.zh-CN.md
  templates/
    assumption-ledger.md
    concept-brief.schema.json
    design-nucleus-options.md
    feature-priority-matrix.md
    feasibility-scan.md
    full-design-brief.md
    idea-triage.md
    one-page-pitch.md
    player-promise-contract.md
    player-promise-contract.schema.json
    production-budget-snapshot.md
    production-profile.md
    reference-game-boundary.md
    risk-register.md
    validation-plan.md
    vertical-slice-plan.md
  assets/
    clockwork-garden-defense-key-art.png
  examples/
    clockwork-garden-defense-illustrated.md
    clockwork-garden-defense.md
    dream-postman-card-adventure.md
    tiny-crew-space-salvage.md
  evals/
    evals.json
    negative_cases.md
    rubric.yaml
```

`SKILL.md` 是 agent 执行入口。`agents/` 提供宿主环境展示元数据。`references/` 提供方法框架。`templates/` 提供可复制的交付格式和 schema。`assets/` 提供示例图像资源。`examples/` 提供 synthetic cases。`evals/` 用于检查输出是否落入常见失败模式。

## 验证

在仓库根目录运行：

```text
python scripts/validate_skill.py game-concept-architect
```
