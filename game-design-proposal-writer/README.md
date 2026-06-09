# game-design-proposal-writer

`game-design-proposal-writer` 用于把已有调研、创意、玩家承诺、体验诊断、验证计划和生产约束，整理成商业游戏策划案、独立游戏设计案、立项评审稿、发行 pitch 或 vertical slice 设计文档。

它不是普通 GDD 生成器。核心任务不是把创意写长，而是把上游材料收束成一份可评审、可删减、可执行、可验证的决策文档。

## 定位

这个 skill 面向游戏策划、制作人、独立开发者、发行沟通、投资/孵化器材料和 AI agent。它适合接在 `game-concept-architect`、`game-experience-analyzer`、`game-experience-density-optimizer` 和 `game-design-source-curator` 之后，负责最终成案。

核心原则：

- 先确定文档受众，再决定章节。
- 先收拢已有证据，再补充假设。
- 先写玩家承诺和核心循环，再写系统清单。
- 先做 scope gate，再写生产计划。
- 商业案要服务投决，独游案要保护创作锋利度和制作边界。
- 没有当前证据时，不写确定市场判断。
- 每份案子都必须有下一步决策请求和投入条件。

## Case Visibility

skill 本身允许用户在自己的环境中处理真实项目、私有项目、客户项目、公开案例或 synthetic cases。

输出时可以使用以下字段管理边界：

| 字段 | 可选值 | 用途 |
| --- | --- | --- |
| `case_visibility` | `private_user_work` / `public_repo_example` / `public_article` / `client_confidential` / `synthetic_case` / `unknown` | 说明案例可见性 |
| `output_destination` | `private_notes` / `repo_example` / `public_post` / `client_delivery` / `publisher_pitch` / `internal_review` / `unknown` | 说明交付去向 |
| `redaction_required` | `true` / `false` / `unknown` | 说明是否需要脱敏 |

这些字段只用于输出管理，不限制用户在本地环境中使用真实或保密项目。只有提交到本仓库的 `examples/`、`assets/`、showcases、eval cases 需要遵守 [`CONTRIBUTING.md`](../CONTRIBUTING.md)。

## 适用场景

- 调研和创意已有，需要写成正式策划案。
- 只有一句话创意，但希望先自动形成概念契约，再写成策划案。
- 玩法脑图、系统设计脑图、xmind、OPML 或 Markdown 大纲需要转成可落地策划案。
- 已有策划案、GDD、pitch 或立项文档需要审核、改进、压缩或重写。
- 商业游戏需要内部立项、老板评审、制作人评审或产品方向说明。
- 独立游戏需要整理成设计案、GDD、发行 pitch 或 demo 计划。
- 过长的幻想文档需要改成可评审的项目方案。
- 需要把玩家承诺、核心循环、系统范围、平台商业、生产计划、风险和验证条件写到一份文档里。
- 需要从概念设计走向 MVP、Vertical Slice、Demo 或下一阶段投入。

## 不适用场景

- 只有一句话创意，且尚未拆出 design nucleus。优先使用 `game-concept-architect`。
- 只有录屏、PV、截图或试玩反馈，需要诊断体验。优先使用 `game-experience-analyzer`。
- 主要目标是留存、节奏、体验浓度、埋点和 A/B 实验。优先使用 `game-experience-density-optimizer`。
- 只想写世界观设定集、宣传文案或商店页短描述。

## 输出模式

| 模式 | 用途 | 推荐交付物 |
| --- | --- | --- |
| `commercial_product_proposal` | 商业游戏、手游、网游、小游戏、F2P、内部立项 | 商业游戏策划案、产品定位、平台商业适配、scope、指标、风险、投决请求 |
| `indie_design_dossier` | 独立游戏、Steam、主机/PC 买断、小团队 | 独游设计案、创作命题、商店页承诺、内容最小化、vertical slice、发行验证 |
| `one_page_decision_memo` | 会前材料、快速判断、老板只看一页 | 一页结论、最大假设、最小验证、投入边界和需要的决策 |
| `publisher_pitch_outline` | 发行、投资、合作方、孵化器 | pitch 结构、卖点证明、demo 计划、团队可信度和请求 |
| `vertical_slice_design_doc` | Demo、first playable、vertical slice | 切片目标、体验路径、功能边界、里程碑、测试和 Go/No-Go |

如果用户说商业游戏策划案，默认使用 `commercial_product_proposal`。如果用户说独游设计案，默认使用 `indie_design_dossier`。

## 输入示例

```text
Use $game-design-proposal-writer，把这个 game-concept-architect 输出改成一份商业游戏立项策划案，目标读者是老板和制作人，平台先假设微信小游戏 + App，商业模式先假设广告 + IAP。
```

```text
Use $game-design-proposal-writer，把这个梦境投递员卡牌冒险创意整理成独游设计案，目标是 Steam Demo 和发行沟通，不要写成手游商业案。
```

```text
Use $game-design-proposal-writer，把这份调研、竞品拆解和概念方案合成一页决策 memo，告诉我是否值得花两周做 first playable。
```

```text
Use $game-design-proposal-writer，我只有一句话创意：在废弃商场里用声音引导影子顾客完成交易。先自动走 concept architect，再写一版独游设计案。
```

```text
Use $game-design-proposal-writer，把这个 xmind 玩法脑图做成可落地商业游戏策划案，重点补 scope、里程碑、风险和验证标准。
```

```text
Use $game-design-proposal-writer，审核这份已有 GDD，指出不能立项评审的问题，并给一版改写方案。
```

## 输出示例片段

```markdown
## Decision Request

建议批准 2 周 first playable 验证，而不是直接进入 3 个月完整 demo。当前最危险假设不是题材吸引力，而是玩家能否在 3 分钟内理解照料顺序会改变机械植物形态，并在夜袭时把这个变化归因到自己的白天选择。

| 决策项 | 建议 | 理由 |
| --- | --- | --- |
| 下一步投入 | 1 策划 + 1 程序 + 临时美术占位，2 周 | 足以验证核心循环，不需要提前量产内容 |
| 暂不投入 | 商店页、长期养成、完整数值经济 | 这些判断依赖核心循环是否成立 |
| 通过标准 | 5 名测试者中至少 3 名能在第二局主动调整照料顺序 | 证明玩家理解核心因果 |
| 失败标准 | 玩家把夜袭结果主要归因为随机或数值不透明 | 说明核心承诺无法成立，需要 pivot |
```

## 与其他 skill 的配合方式

`game-concept-architect` 负责从 0 到 1 建立概念结构、玩家承诺、核心循环、scope gate 和验证计划。

`game-experience-analyzer` 负责把录屏、PV、截图或试玩样本转成 evidence index、issue cards 和体验诊断。

`game-experience-density-optimizer` 负责把留存、节奏、反馈、具身感、氛围和认知负荷问题转成一周实验。

`game-design-proposal-writer` 负责把这些上游产物汇总成面向决策的商业策划案或独游设计案。

推荐流程：

1. 用 `game-concept-architect` 生成 concept brief、player-promise-contract 和 validation plan。
2. 如果有竞品或原型材料，用 `game-experience-analyzer` 生成 evidence index 和 issue cards。
3. 如果核心问题是体验浓度或留存节奏，用 `game-experience-density-optimizer` 生成实验计划。
4. 用 `game-design-proposal-writer` 整合成商业游戏策划案、独游设计案、发行 pitch 或 vertical slice 文档。
5. 把评审反馈回写到 assumption ledger、risk register 和 milestone gate。

## 文件结构

```text
game-design-proposal-writer/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    proposal-intake-router.zh-CN.md
    commercial-game-proposal-framework.zh-CN.md
    indie-design-dossier-framework.zh-CN.md
    evidence-assumption-boundary.zh-CN.md
    audience-business-scope-gate.zh-CN.md
    scope-and-milestone-gates.zh-CN.md
    pitch-document-quality-gate.zh-CN.md
  templates/
    proposal-intake.md
    proposal-evidence-ledger.md
    commercial-game-proposal.md
    indie-design-dossier.md
    one-page-decision-memo.md
    publisher-pitch-outline.md
    vertical-slice-design-doc.md
    existing-proposal-review.md
    milestone-gate-plan.md
    risk-register.md
    game-design-proposal.schema.json
  examples/
    synthetic-clockwork-garden-commercial-proposal.md
    synthetic-dream-postman-indie-dossier.md
  evals/
    evals.json
    rubric.yaml
    synthetic_outputs.json
    negative_cases.md
```

`SKILL.md` 是 agent 执行入口。`references/` 提供方法框架。`templates/` 提供可复制的交付格式和 schema。`examples/` 提供 synthetic cases。`evals/` 用于检查输出是否落入常见失败模式。

## 验证

在仓库根目录运行：

```text
python scripts/validate_skill.py game-design-proposal-writer
```
