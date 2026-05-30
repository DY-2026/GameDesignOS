# game-concept-architect

`game-concept-architect` 用于把一句话游戏创意扩展为完整但可验证的游戏设计案。

它不是普通 GDD 生成器。它的核心任务不是“把创意写长”，而是先从创意中提取可设计的种子，定义玩家承诺，再构建核心循环、关键系统、scope gate 和原型验证计划。

## 定位

这个 skill 面向游戏策划、独立开发者、制作人和 AI agent，适合把模糊创意变成可讨论、可删减、可验证、可进入原型制作的设计蓝图。

核心原则：

- 先拆 seed，再写方案。
- 先做外部可行性扫描，再相信自己的直觉。
- 先定义玩家承诺，再展开系统。
- 题材、世界观、品类都不是设计核。
- 所有新增系统必须能改变玩家行为、选择、节奏、成长或表达。
- 所有用户未提供的信息必须进入 `assumption ledger`。
- 任何方案都必须经过 `scope gate` 和 `validation plan`。
- 能不能落地要同时看团队能力、内容产能、技术成熟度、时间成本和商业预期。

## 适用场景

- 只有一句话创意，需要判断是否值得立项。
- 已有题材和品类，但玩法核不清楚。
- 想知道一个“绝妙点子”是否已有市场信号、竞品参照和真实玩家动机。
- 想把“像某某游戏 + 某个题材”变成不抄袭、可验证的新设计。
- 独立游戏需要控制 MVP / Demo / Vertical Slice 范围。
- 微信小游戏、App、Steam、Web 等平台方向需要反推设计边界。
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
| `one_page_pitch` | 快速立项判断 | 一页 pitch、外部验证状态、核心承诺、scope 摘要、验证计划摘要 |
| `full_design_brief` | 完整设计案 | seed、外部可行性、玩家承诺、循环、系统、平台商业、生产可行性、scope、风险、验证 |
| `vertical_slice_plan` | 进入原型制作 | 垂直切片目标、功能优先级、生产边界、里程碑、测试标准 |

如果用户没有指定模式，默认使用 `one_page_pitch`；如果用户说“完整方案 / 设计案”，使用 `full_design_brief`；如果用户说“做原型 / vertical slice / demo 计划”，使用 `vertical_slice_plan`。

## 输出示例片段

输入：

```text
废弃温室机械植物防守
```

输出片段：

```markdown
## Concept Seed Extraction

| 字段 | 提取结果 | 确定性 |
| --- | --- | --- |
| 题材母体 | 废弃温室、机械植物、夜间虫群 | 中 |
| 玩法母体 | 轻量策略防守、格位培育、波次压力 | 中 |
| 情绪承诺 | 白天精打细算地培育，夜晚看防线在虫群压力下运转 | 高 |
| 差异化种子 | 植物不是静态塔，而是会随照料顺序改变功能的半机械生命体 | 中 |
| 关键 unknown | 植物变形是局内即时选择，还是局间 build 成长？ | 高影响 |

## 玩家承诺

- 对外宣传承诺：在废弃温室中培育会变形的机械植物，用有限白昼资源撑过夜间虫群。
- 前 10 分钟承诺：玩家会体验种植、调校、夜袭、防线反馈和一次失败或险胜。
- 长期游玩承诺：玩家会探索不同植物协同和温室布局，追求更稳定的夜间防守路线。

## Scope Gate

| 层级 | 内容 |
| --- | --- |
| MVP 必须有 | 3 种植物、1 个温室网格、2 类虫群、昼夜循环、基础升级 |
| Vertical Slice 应该有 | 植物变形、温室设施、夜间特殊事件 |
| Demo 后再做 | 多温室章节、稀有植物谱系、剧情探索 |
| 宣传概念可以保留但暂不开发 | 失落园艺协会、巨大玻璃穹顶、植物图鉴故事 |
| 建议砍掉 | 开放世界探索、实时多人协作、复杂自动化工厂 |
```

## 与 game-experience-analyzer 的配合方式

`game-concept-architect` 负责从 0 到 1 建立“该做什么、为什么做、如何验证”的设计架构。

`game-experience-analyzer` 更适合在已有原型、视频、试玩反馈或竞品体验之后使用，用来分析玩家实际体验是否兑现了承诺。

推荐配合流程：

1. 用 `game-concept-architect` 生成 `one_page_pitch` 或 `vertical_slice_plan`。
2. 制作最小可玩原型。
3. 收集试玩录像、玩家反馈、指标数据。
4. 用 `game-experience-analyzer` 检查体验是否匹配宣传承诺、前 10 分钟承诺和长期承诺。
5. 把分析结论回写到 `assumption ledger`、`risk register` 和下一版 `validation plan`。

## 文件结构

```text
game-concept-architect/
  SKILL.md
  README.md
  references/
    external-feasibility-scan.zh-CN.md
    production-feasibility.zh-CN.md
  templates/
    feasibility-scan.md
    production-budget-snapshot.md
  assets/
    clockwork-garden-defense-key-art.png
  examples/
    clockwork-garden-defense-illustrated.md
    clockwork-garden-defense.md
    dream-postman-card-adventure.md
    tiny-crew-space-salvage.md
  evals/
```

`SKILL.md` 是 agent 执行入口。`references/` 提供方法框架。`templates/` 提供可复制的交付格式。`assets/` 提供示例图像资源。`examples/` 提供虚构案例。`evals/` 用于检查输出是否落入常见失败模式。
