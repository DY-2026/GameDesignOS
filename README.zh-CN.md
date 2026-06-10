<p align="center">
  <img src="./assets/paranoia-skills-overview-banner-v6.png" alt="ParanoiaSkills v0.6.1 - A verifiable agent-skill operating system for game design production" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  一套面向游戏设计生产与 AI 工作流治理的可验证 agent-skill 操作系统。
  它把证据转成诊断，把概念转成验证契约，把生产约束转成可评审策划案，把 ED 问题转成一周实验，把 workflow 改动转成带 eval 的受控演化。
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#这个项目是什么">这个项目是什么</a> ·
  <a href="./docs/try-it-in-10-minutes.md">10 分钟试用</a> ·
  <a href="#轻松上手">轻松上手</a> ·
  <a href="#60-秒-demo">60 秒 demo</a> ·
  <a href="#github-案例">GitHub 案例</a> ·
  <a href="#当前-skill">当前 Skill</a> ·
  <a href="#图文展示">图文展示</a> ·
  <a href="#star-history">Star History</a> ·
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-7-2ea44f">
  <img alt="Version" src="https://img.shields.io/badge/Version-v0.6.1-31e1d6">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Evidence%20%7C%20Contracts%20%7C%20Evals-f9a825">
</p>

> License: skill documents and tooling are released under the MIT License. Paranoia 名称、logo、视觉识别和项目品牌不作为商标授权。

> 像给游戏设计师和 AI agent 用的“小型操作系统”：不是收集提示词，而是把可复用的证据规则、跨 skill 契约、验证门、回滚路径和输出模板打包成 skill。

## 这个项目是什么

`ParanoiaSkills` 是一套 AI 辅助游戏设计工作的公开基础 Skill 库，把游戏体验分析、概念架构、策划案写作、体验浓度实验、工作流演化、专业翻译和资料策展，沉淀成可复用的 agent instructions、references、schemas、templates、examples 和 evals。

它不是一堆提示词合集。它更像一套小型游戏设计操作系统，并用契约让不同 skill 之间能交接工作，而不是各自输出孤立长文：

```text
媒体证据 -> evidence index -> issue cards -> ED handoff -> 一周实验
一句话创意 -> player-promise contract -> validation plan -> 后续媒体诊断
概念/证据/生产约束 -> 可评审策划案 -> pitch 或 milestone gate
workflow 改动 -> WOOP Task Card -> VOI/OODA probe -> eval -> Human Gate -> rollback
书籍与资料 -> 结构化知识资产 -> 未来任务可复用 reference
```

## 它哪里不一样

- **Evidence-first:** 判断尽量绑定到来源、截图区域、时间戳、样本证据或验证指标。
- **Contract-driven:** concept brief、evidence index、issue card、ED handoff 和 validation plan 可以跨 skill 流转。
- **Concept-to-validation:** 不把“绝妙点子”直接扩写成 GDD，而是拆成 seed、玩家承诺、核心循环、scope gate 和原型验证计划。
- **Workflow-governed:** 不追求一次漂亮回答，而是把可复用流程沉淀到 `SKILL.md`、`references/`、`templates/`、eval、Human Gate 和 rollback。
- **Agent portable:** Codex、Claude Code、OpenCode 或其他能读取 Markdown skill 的 agent 环境都可以迁移。
- **Public/private safe:** 公开示例只使用 synthetic、public、cleared 或 `needs_review` 材料；真实项目留在你自己的环境中。

## Try It in 5 Prompts

```text
Use $game-experience-analyzer to diagnose this PV or gameplay recording into sample boundary, timestamped evidence, Hook/Loop/Link/Surprise diagnosis, issue cards, and validation recommendations.
```

```text
Use $game-concept-architect to turn this one-line game idea into concept seed extraction, design nucleus options, player promise contract, core loop, scope gate, and prototype validation plan.
```

```text
Use $game-design-proposal-writer to turn this concept brief, validation plan, evidence notes, and production constraints into a decision-ready commercial proposal, indie dossier, publisher pitch, or vertical-slice document.
```

```text
Use $paranoia-ai-system-evolver to upgrade this workflow with a WOOP Task Card, VOI, OODA, eval checks, Human Gate, and rollback.
```

```text
Use $game-experience-density-optimizer to turn this first-session retention, pacing, or experience density problem into an ED diagnosis, CLP/SF/EB/AR/MD-min levers, a weekly A/B plan, instrumentation, dashboard fields, decision rules, and rollback gates.
```

完整上手路径见 [Try It in 10 Minutes](./docs/try-it-in-10-minutes.md)。如果你希望继续看到更多公开游戏分析案例和可迁移的 agent skill 模板，欢迎 star 这个仓库；star 越多，我会越优先补更好的公开 demo、adapter 和可复用 skill 模板。

## 60 秒 Demo

输入一张截图、一段录屏、一个 PV/宣传片或视频链接，让 skill 直接输出证据化设计报告：

<p align="center">
  <img src="./assets/demo-game-experience-before-after.png" alt="60 秒 demo：Game Experience Analyzer 把 PV 输入转成证据化报告" width="100%">
</p>

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, feature exposure/unlock/first-use ledger, Hook/Loop/Link/Surprise diagnosis, and actionable fixes.
```

当前可查看示例是 [`《生存33天》41 分钟试玩录屏前期体验复盘示例`](./game-experience-analyzer/examples/survival-33-days-gameplay-experience-report.md)：一个录屏样本会被拆成时间戳证据、功能暴露/解锁/首用账本、前期循环诊断、UI/引导风险和可验证修改建议。该示例在正式作为 public material 展示前已标为 `needs_review`。

## GitHub 案例

如果只是打开 GitHub 页面想快速看懂这次新增的体验浓度 proof path，先看这一个案例即可。`game-experience-analyzer` 已经在自己的 package 和上面的 60 秒 demo 里有示例，不在这里重复加入口。

| 案例 | Skill 路线 | 重点看什么 | 链接 |
| --- | --- | --- | --- |
| `《冒险家艾略特的千年奇谭》Demo` | `$game-experience-analyzer -> $game-experience-density-optimizer` | 公开视频关键帧如何变成 ED 证据门、指标周期、截图证据卡、变体矩阵、埋点和回滚规则。 | [打开案例](./docs/showcases/elliot-experience-density-report/README.md) |

## 轻松上手

最简单的用法只有三步：选一个 skill，把材料交给 agent，要求它按 skill 输出可复查的结果。

### 1. 不知道选哪个？先看这张表

| 你手里的材料 | 该用哪个 skill | 你会得到什么 |
| --- | --- | --- |
| 截图、录屏、PV、视频链接 | `$game-experience-analyzer` | 带时间戳/证据/问题优先级的体验报告，或游戏拆解、机制迁移和验证计划 |
| 一句话游戏创意 | `$game-concept-architect` | concept seed、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate、验证计划 |
| 概念案、证据、验证计划或生产约束 | `$game-design-proposal-writer` | 可评审的商业策划案、独游设计案、发行 pitch、一页决策 memo 或 vertical slice 文档 |
| 一段 prompt、workflow、schema 或 agent 规则 | `$paranoia-ai-system-evolver` | 带 WOOP/VOI/OODA/eval/Human Gate/rollback 的系统演化提案 |
| 英文游戏设计章节或长文 | `$game-design-book-translator` | 专业、自然、可复查的中文设计翻译 |
| 一批文章、视频、作者或网站 | `$game-design-source-curator` | 可长期维护的游戏设计知识库条目 |
| 留存、节奏、反馈、具身感、氛围感或认知负荷问题 | `$game-experience-density-optimizer` | ED 诊断、一周 A/B 变体、埋点字典、看板字段和回滚门 |

### 2. 复制一句最小提示词

在支持 skill 的 agent 环境里，直接点名对应 skill：

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $game-experience-analyzer to dissect this game into player verbs, action-goal alignment, uncertainty sources, system dynamics, content flow, audience desire, transfer boundaries, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema with a WOOP Task Card, VOI, OODA, evals, Human Gate, and rollback.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

```text
Use $game-concept-architect to turn this one-line game idea into a concept seed, player verbs, action-goal alignment, player promise, core loop, scope gate, production feasibility check, and prototype validation plan.
```

```text
Use $game-design-proposal-writer to assemble this research, concept brief, evidence index, validation plan, and team constraints into a publisher pitch outline with proof of play, scope gate, budget assumptions, risks, and decision request.
```

```text
Use $game-experience-density-optimizer to turn this first-session experience density problem into CLP/SF/EB/AR/MD-min diagnosis, rollbackable weekly variants, telemetry events, dashboard fields, and pre-registered decision rules.
```

### 3. 安装到自己的 agent 环境

如果你的工具支持本地 skill / Markdown skill package，把对应目录复制或同步到它的 skill 目录即可。常见宿主可以是 Codex、Claude Code、OpenCode，或其他能读取 Markdown skill 的 agent 环境：

```text
game-experience-analyzer/
paranoia-ai-system-evolver/
game-design-book-translator/
game-design-source-curator/
game-concept-architect/
game-experience-density-optimizer/
game-design-proposal-writer/
```

安装后确认两件事：`SKILL.md` frontmatter 的 `name` 和目录名一致；`references/`、`templates/`、`examples/` 里的相对路径还能打开。

## 图文展示

<table>
  <tr>
    <td width="25%">
      <img src="./assets/showcase-game-experience-analyzer.png" alt="Game Experience Analyzer 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator 展示图">
    </td>
  </tr>
  <tr>
    <td><b>分析游戏体验</b><br>把截图、录屏、宣传片和视频链接，转成证据优先的体验诊断、游戏拆解和机制迁移判断。</td>
    <td><b>演化工作流</b><br>用 WOOP、VOI、OODA、eval、Human Gate 和 rollback 升级 prompt、schema、memory 和 tool routing。</td>
    <td><b>翻译设计知识</b><br>把严肃的游戏设计书籍和章节，变成自然、专业、可复查的中文设计写作。</td>
    <td><b>策展资料</b><br>把散落在文章、视频、作者、专栏和网站里的内容，变成可长期维护的游戏设计知识库。</td>
  </tr>
  <tr>
    <td width="25%">
      <img src="./assets/showcase-game-concept-architect.png" alt="Game Concept Architect 展示图">
    </td>
    <td width="25%">
      <img src="./assets/showcase-game-experience-density-optimizer.png" alt="Game Experience Density Optimizer 展示图">
    </td>
    <td width="25%"></td>
    <td width="25%"></td>
  </tr>
  <tr>
    <td><b>架构游戏概念</b><br>把一句话创意拆成 seed、玩家动词、动作-目标、玩家承诺、核心循环、scope gate 和验证计划。</td>
    <td><b>优化体验浓度</b><br>把留存、节奏、反馈、具身感、氛围感和认知负荷问题，转成一周可验证的 ED 实验。</td>
    <td></td>
    <td></td>
  </tr>
</table>

更小的 proof-path 列表见 [showcase index](./docs/showcases/README.md)。

## Skill Architecture

`ParanoiaSkills` 分为公开基础层和契约层。本仓库只包含公开基础 skill。私有项目规则、客户材料、真实案例和个人工作室偏好应放在仓库外的 private overlay。

- **Design Production Layer**
  - [`game-concept-architect/`](./game-concept-architect/)：one-line idea -> verifiable design blueprint。
  - [`game-design-proposal-writer/`](./game-design-proposal-writer/)：research/concept/evidence/production notes -> decision-ready proposal or pitch。
  - [`game-experience-analyzer/`](./game-experience-analyzer/)：media/sample -> evidence-linked diagnosis。
  - [`game-experience-density-optimizer/`](./game-experience-density-optimizer/)：retention/pacing/feedback issue -> weekly ED experiment。
- **Workflow Governance Layer**
  - [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/)：prompt/workflow/schema/eval changes -> controlled evolution。
- **Knowledge Asset Layer**
  - [`game-design-book-translator/`](./game-design-book-translator/)：design texts -> professional Chinese design writing。
  - [`game-design-source-curator/`](./game-design-source-curator/)：scattered sources -> durable knowledge base。
- **Contract Layer**
  - [`contracts/`](./contracts/)：router rules，以及 player promise、validation plan、evidence index、issue card、ED handoff 的共享 schema。

用户仍然可以在自己的环境中用这些 skill 处理真实项目、私有项目、客户项目或 synthetic cases。公开案例规则只约束提交回本仓库的内容。

## 当前 Skill

| Skill | 一句话用途 | 适合场景 | 包目录 |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | 把截图、录屏、PV/宣传片和视频链接拆成证据优先的中文游戏设计报告。 | 体验分析、玩法机制、游戏拆解、机制迁移、整体项目、MDA、系统叙事、单机流程、热度预测、前瞻窗口、商业化、UX。 | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | 把 prompt、workflow、memory、schema、tool routing 和 eval 改动变成受控系统演化。 | WOOP Task Card、VOI/OODA、模型压缩、因果中介、Human Gate、rollback、可验证升级。 | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | 把英文游戏设计/研发材料翻译成真正像中文设计写作的专业文本。 | 术语、章节、图注、表格、QA、来源边界检查。 | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | 把散落资料变成可长期维护的游戏设计知识库。 | 来源筛选、评分、HTML 归档、registry、update history、设计实验卡。 | [`game-design-source-curator/`](./game-design-source-curator/) |
| **Game Concept Architect** | 把一句话游戏创意扩展为可验证的概念设计案，包含 seed extraction、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate 和原型验证计划。 | 独游创意、立项 pitch、外部可行性、平台/商业适配、MVP/Vertical Slice 规划、生产约束。 | [`game-concept-architect/`](./game-concept-architect/) |
| **Game Experience Density Optimizer** | 把体验浓度、留存、节奏、反馈、具身感、氛围感和认知负荷问题转成一周 ED 实验。 | 首局调优、原型手感、LiveOps 小实验、A/B 变体、埋点字典、看板规格、回滚门。 | [`game-experience-density-optimizer/`](./game-experience-density-optimizer/) |
| **Game Design Proposal Writer** | 把调研、概念契约、证据、验证计划、生产约束和商业目标整理成可决策的游戏策划案。 | 商业游戏策划案、独游设计案、发行/投资 pitch、一页决策 memo、Demo/Vertical Slice 规划。 | [`game-design-proposal-writer/`](./game-design-proposal-writer/) |

## 典型用例

- **竞品体验复盘:** 给一段录屏，输出时间轴、功能账本、玩法循环、问题优先级和修改建议。
- **游戏拆解与机制迁移:** 按玩家动词、目标层级、不确定性、系统动态、内容流、受众动机和可玩主题，判断哪些结构可迁移、哪些表层不能照搬。
- **PV 热度预测:** 给宣传片链接，判断首秒钩子、卖点复述、可玩性证明、平台适配、转化承接和验证计划。
- **前瞻机会判断:** 判断题材/玩法是否还有窗口；休闲轻度默认 1-3 个月，微小中重度默认 3-6 个月。
- **资料策展:** 把文章、视频、作者、专栏和网站沉淀成可检索、可引用、可实验的知识库。
- **专业翻译:** 把游戏设计书籍或长文翻成自然中文，同时保留术语、论证结构和图表语境。
- **工作流升级:** 把一次有用的 agent 行为升级成候选规则，并用 eval、Human Gate 和 rollback 控制风险。
- **跨 skill 交接:** 用共享 contract 从概念承诺走到媒体诊断，再走到 ED 实验，而不是每一步都重新解释上下文。
- **创意可行性:** 把一句话创意拆成 concept seed、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate、生产可行性和原型验证计划。
- **策划案成案:** 把已验证概念、资料、证据、风险和生产约束整理成可评审的商业策划案、独游设计案、pitch outline 或 vertical slice 文档。
- **体验浓度实验:** 把首局、节奏、反馈、具身感、氛围感或认知负荷问题，转成带指标和回滚门的一周 ED 实验。

## 项目结构

可以把这个仓库理解成“一组可安装 skill 包 + 支撑公开发布的基础设施”，而不是一个普通素材目录。

| 层级 | 路径 | 作用 |
| --- | --- | --- |
| Skill packages | `game-experience-analyzer/`, `game-concept-architect/`, `game-design-proposal-writer/`, `paranoia-ai-system-evolver/`, `game-design-book-translator/`, `game-design-source-curator/`, `game-experience-density-optimizer/` | 可复制到 agent 环境里的 skill 包。每个包都有自己的运行入口、方法参考、模板、示例和 eval。 |
| Public onboarding | `README.md`, `README.zh-CN.md`, `README.en.md`, `docs/`, `releases/` | 说明项目是什么、怎么试用、showcase 边界、release 草稿和公开文档。 |
| GitHub 可读案例 | `docs/showcases/elliot-experience-density-report/` | 可直接点击阅读的体验浓度案例页，展示公开视频证据如何转成 ED 实验方案。 |
| Integration and contracts | `adapters/`, `contracts/`, `.github/`, `scripts/` | 适配器说明、共享 schema、router contract、GitHub workflow/templates、行为 eval 和仓库校验工具。 |
| Governance and media | `CONTRIBUTING.md`, `LICENSE`, `assets/` | 贡献规则、授权信息，以及 README/showcase 使用的公开视觉素材。 |

每个 skill 通常使用同一套结构：

```text
SKILL.md      -> agent 入口、触发条件、核心流程、边界
references/  -> 方法、评分规则、路由、质量门、验证 playbook
templates/   -> 可复制到真实任务中的表单和输出结构
examples/    -> 可复查的示例输出
agents/      -> 支持对应元数据的 agent 环境可读取
evals/       -> 用于回归检查的提示和预期行为
```

## 安装与使用

这个仓库里的 skill 是可迁移包。典型使用方式：

1. 将某个 skill 目录复制或同步到你的 agent skill 目录。
2. 确认 `SKILL.md` frontmatter 的 `name` 与目录名一致。
3. 在 agent 中用 `$skill-name` 或自然语言触发。
4. 按对应 README 或 `SKILL.md` 的验证方式检查 JSON/YAML、引用路径和示例。

## 验证

在仓库根目录运行：

```text
python scripts/validate_repo.py
python scripts/validate_skill.py game-experience-analyzer
python scripts/validate_skill.py game-concept-architect
python scripts/validate_skill.py game-experience-density-optimizer
python scripts/validate_skill.py game-design-proposal-writer
```

## Star History

<a href="https://star-history.com/#DY-2026/ParanoiaSkills&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date&theme=dark">
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date">
    <img alt="Star History Chart for DY-2026/ParanoiaSkills" src="https://api.star-history.com/svg?repos=DY-2026/ParanoiaSkills&type=Date">
  </picture>
</a>

## License

本仓库的 skill documents and tooling 使用 [MIT License](./LICENSE) 发布。

Paranoia 名称、logo、视觉识别和项目品牌不作为商标授权。examples 可能有各自的 `source_status`、`case_type` 或来源元数据，复用前请检查对应文件 frontmatter。

## Skill 包约定

每个 skill 都是一个可独立安装的包：`SKILL.md` 放运行入口，`references/` 放方法说明，`templates/` 放可复用表单，`examples/` 和 `evals/` 用于展示与回归检查。

## 贡献

提交公开 examples、evals、assets、showcases 或 release notes 前，请确保材料为 synthetic、公开材料或明确 cleared material。具体规则见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 设计原则

```text
Evidence before opinion.
Feasibility before scope.
Workflow before one-off prompts.
VOI before research.
Eval before promotion.
Rollback before confidence.
```

## 未来 Skill

未来根据社区反馈和 skill 成熟度，可能继续加入 AI + 独游实战全流程方向的包，例如：

- `indie-game-production-master`：覆盖独游从想法验证、GDD/Gate、原型、playtest、AI 资产流水线、Steam/发布策略到复盘沉淀的全流程制作 skill。
- `godot-ai-game-production`：覆盖 Godot + AI 项目搭建、设计真源、数据契约、资源流水线、headless/keyshot 验证、Demo/Release Gate 和工程复盘的生产 skill。
