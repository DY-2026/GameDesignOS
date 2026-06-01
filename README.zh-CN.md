<p align="center">
  <img src="./assets/demo-game-experience-before-after.png" alt="60 秒 demo：Game Experience Analyzer 把 PV 输入转成证据化报告" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  一套基于 Paranoia Method 的游戏设计与 agent 工作流 skill 系统。
  把玩法证据、创意种子、工作流突变、翻译与资料来源，压缩成可验证的操作模型。
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#60-秒-demo">60 秒 demo</a> ·
  <a href="#轻松上手">轻松上手</a> ·
  <a href="#当前-skill">当前 Skill</a> ·
  <a href="#图文展示">图文展示</a> ·
  <a href="#license">License</a>
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/Skills-5-2ea44f">
  <img alt="Domain" src="https://img.shields.io/badge/Domain-Game%20Design-blue">
  <img alt="Agent Ready" src="https://img.shields.io/badge/Agent--Ready-Codex%20%7C%20Claude%20Code%20%7C%20OpenCode-6f42c1">
  <img alt="Method" src="https://img.shields.io/badge/Method-Paranoia%20Method-f9a825">
</p>

> License: skill documents and tooling are released under the MIT License. Paranoia 名称、logo、视觉识别和项目品牌不作为商标授权。

> ParanoiaSkills 把 skill 当成操作模型来设计：一个足够轻的入口，加上证据账本、成本门、验证面和可回滚路径。

## 60 秒 Demo

输入一张截图、一段录屏、一个 PV/宣传片或视频链接，让 skill 直接输出证据化设计报告：

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, feature exposure/unlock/first-use ledger, Hook/Loop/Link/Surprise diagnosis, and actionable fixes.
```

当前最强案例是 [`《生存33天》41 分钟试玩录屏前期体验复盘示例`](./game-experience-analyzer/examples/survival-33-days-gameplay-experience-report.md)：一个公开视频样本会被拆成时间戳证据、功能暴露/解锁/首用账本、前期循环诊断、UI/引导风险和可验证修改建议。

## 这个项目是什么

`ParanoiaSkills` 是一套围绕 Paranoia Method 搭建的游戏设计与 AI agent 工作流系统：把混乱的创意、样本、判断和工作流改动，压缩成可调用、可检查、可修订、可迁移的操作模型。

每个 skill 都不是一段提示词配方，而是一个被打包的机制：轻量入口、深入 references、可复制 templates、确定性 validator，以及必要时的 eval 和 rollback 面。

```text
原始玩法证据 -> 带证据账本的设计诊断
创意碎片 -> 玩家承诺、动词、循环与验证门
工作流突变 -> 带成本/信任/eval/rollback gate 的候选规则
设计文本或资料来源 -> 可复用的知识资产
```

## 为什么值得收藏

- **Open and portable:** 每个 skill 都是可读、可复制、可审计的 Markdown 包，不把你的工作流锁死在某个产品里。
- **不是“谨慎措辞”，而是证据账本:** 关键断言要区分已验证事实、工具观察、推理判断、未验证假设和人类待确认。
- **Concept-to-validation:** 不把“绝妙点子”直接扩写成 GDD，而是拆成 seed、玩家承诺、核心循环、scope gate 和原型验证计划。
- **操作模型优先:** 不追求一次漂亮回答，而是把可复用行为压缩进 `SKILL.md`、`references/`、`templates/`、validator 和 eval gate。
- **Game-design native:** 面向真实游戏设计工作：体验、玩法、MDA、系统叙事、品类、窗口期、商业化、素材和生产流程。
- **Agent portable:** 不绑定单一工具；Codex、Claude Code、OpenCode 或其他能读取 Markdown skill 的 agent 环境都可以迁移。
- **受控演化:** 系统改动先过成本检查、反遗漏检查、shadow-first 发布、eval、Human Gate 和 rollback，再进入长期规则。

## 轻松上手

最简单的用法只有三步：选一个 skill，把材料交给 agent，要求它按 skill 输出可复查的结果。

### 1. 不知道选哪个？先看这张表

| 你手里的材料 | 该用哪个 skill | 你会得到什么 |
| --- | --- | --- |
| 截图、录屏、PV、视频链接 | `$game-experience-analyzer` | 带时间戳/证据/问题优先级的体验报告，或游戏拆解、机制迁移和验证计划 |
| 一句话游戏创意 | `$game-concept-architect` | concept seed、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate、验证计划 |
| 一段 prompt、workflow、schema 或 agent 规则 | `$paranoia-ai-system-evolver` | 带操作模型、证据账本、成本变化、替代方案检查、shadow 发布、eval 和 rollback 的 Paranoia Method 演化提案 |
| 英文游戏设计章节或长文 | `$game-design-book-translator` | 专业、自然、可复查的中文设计翻译 |
| 一批文章、视频、作者或网站 | `$game-design-source-curator` | 可长期维护的游戏设计知识库条目 |

### 2. 复制一句最小提示词

在支持 skill 的 agent 环境里，直接点名对应 skill：

```text
Use $game-experience-analyzer to analyze this gameplay recording into timestamped evidence, design lenses, heat potential, foresight windows, Go/No-Go, and validation recommendations.
```

```text
Use $game-experience-analyzer to dissect this game into player verbs, action-goal alignment, uncertainty sources, system dynamics, content flow, audience desire, transfer boundaries, and validation recommendations.
```

```text
Use $paranoia-ai-system-evolver to upgrade this prompt/workflow/schema through the Paranoia Method: map the operating model, compare total description cost, build an assertion evidence ledger, check missing alternatives, plan shadow-first rollout, evals, Human Gate, and rollback.
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

### 3. 安装到自己的 agent 环境

如果你的工具支持本地 skill / Markdown skill package，把对应目录复制或同步到它的 skill 目录即可。常见宿主可以是 Codex、Claude Code、OpenCode，或其他能读取 Markdown skill 的 agent 环境：

```text
game-experience-analyzer/
paranoia-ai-system-evolver/
game-design-book-translator/
game-design-source-curator/
game-concept-architect/
```

安装后确认两件事：`SKILL.md` frontmatter 的 `name` 和目录名一致；`references/`、`templates/`、`examples/` 里的相对路径还能打开。

## 图文展示

<table>
  <tr>
    <td width="20%">
      <img src="./assets/showcase-game-experience-analyzer.png" alt="Game Experience Analyzer 展示图">
    </td>
    <td width="20%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver 展示图">
    </td>
    <td width="20%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator 展示图">
    </td>
    <td width="20%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator 展示图">
    </td>
    <td width="20%">
      <img src="./assets/showcase-game-concept-architect.png" alt="Game Concept Architect 展示图">
    </td>
  </tr>
  <tr>
    <td><b>分析游戏体验</b><br>把截图、录屏、宣传片和视频链接，转成证据优先的体验诊断、游戏拆解和机制迁移判断。</td>
    <td><b>演化工作流</b><br>把 prompt、schema、memory、eval 和 routing 改动变成带成本、证据、shadow 和 rollback gate 的候选操作模型升级。</td>
    <td><b>翻译设计知识</b><br>把严肃的游戏设计书籍和章节，变成自然、专业、可复查的中文设计写作。</td>
    <td><b>策展资料</b><br>把散落在文章、视频、作者、专栏和网站里的内容，变成可长期维护的游戏设计知识库。</td>
    <td><b>架构游戏概念</b><br>把一句话创意拆成 seed、玩家动词、动作-目标、玩家承诺、核心循环、scope gate 和验证计划。</td>
  </tr>
</table>

## Skill Architecture

`ParanoiaSkills` 分为三层操作模型。本仓库只包含公开基础 skill。私有项目规则、客户材料、真实案例和个人工作室偏好应放在仓库外的 private overlay。

- **Design Production Layer**
  - [`game-concept-architect/`](./game-concept-architect/)：one-line idea -> verifiable design blueprint。
  - [`game-experience-analyzer/`](./game-experience-analyzer/)：media/sample -> evidence-linked diagnosis。
- **Workflow Governance Layer**
  - [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/)：system changes -> Paranoia Method evolution gates。
- **Knowledge Asset Layer**
  - [`game-design-book-translator/`](./game-design-book-translator/)：design texts -> professional Chinese design writing。
  - [`game-design-source-curator/`](./game-design-source-curator/)：scattered sources -> durable knowledge base。

用户仍然可以在自己的环境中用这些 skill 处理真实项目、私有项目、客户项目或 synthetic cases。公开案例规则只约束提交回本仓库的内容。

## 当前 Skill

| Skill | 一句话用途 | 适合场景 | 包目录 |
| --- | --- | --- | --- |
| **Game Experience Analyzer** | 把截图、录屏、PV/宣传片和视频链接拆成证据优先的中文游戏设计报告。 | 体验分析、玩法机制、游戏拆解、机制迁移、整体项目、MDA、系统叙事、单机流程、热度预测、前瞻窗口、商业化、UX。 | [`game-experience-analyzer/`](./game-experience-analyzer/) |
| **Paranoia AI System Evolver** | 把 prompt、workflow、memory、schema、tool routing 和 eval 改动变成 Paranoia Method 演化提案。 | 操作模型审计、总描述成本、证据账本、反遗漏检查、子 agent 损失审计、shadow-first 发布、Human Gate、rollback。 | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | 把英文游戏设计/研发材料翻译成真正像中文设计写作的专业文本。 | 术语、章节、图注、表格、QA、来源边界检查。 | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | 把散落资料变成可长期维护的游戏设计知识库。 | 来源筛选、评分、HTML 归档、registry、update history、设计实验卡。 | [`game-design-source-curator/`](./game-design-source-curator/) |
| **Game Concept Architect** | 把一句话游戏创意扩展为可验证的概念设计案，包含 seed extraction、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate 和原型验证计划。 | 独游创意、立项 pitch、外部可行性、平台/商业适配、MVP/Vertical Slice 规划、生产约束。 | [`game-concept-architect/`](./game-concept-architect/) |

## 典型用例

- **竞品体验复盘:** 给一段录屏，输出时间轴、功能账本、玩法循环、问题优先级和修改建议。
- **游戏拆解与机制迁移:** 按玩家动词、目标层级、不确定性、系统动态、内容流、受众动机和可玩主题，判断哪些结构可迁移、哪些表层不能照搬。
- **PV 热度预测:** 给宣传片链接，判断首秒钩子、卖点复述、可玩性证明、平台适配、转化承接和验证计划。
- **前瞻机会判断:** 判断题材/玩法是否还有窗口；休闲轻度默认 1-3 个月，微小中重度默认 3-6 个月。
- **资料策展:** 把文章、视频、作者、专栏和网站沉淀成可检索、可引用、可实验的知识库。
- **专业翻译:** 把游戏设计书籍或长文翻成自然中文，同时保留术语、论证结构和图表语境。
- **工作流升级:** 把一次有用的 agent 行为升级成候选操作模型改动，并用证据、成本变化、shadow 发布、eval、Human Gate 和 rollback 控制风险。
- **创意可行性:** 把一句话创意拆成 concept seed、玩家动词、动作-目标对齐、玩家承诺、核心循环、scope gate、生产可行性和原型验证计划。

## 项目结构

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- LICENSE
|-- CONTRIBUTING.md
|-- adapters/
|-- contracts/
|-- docs/
|-- .github/
|-- releases/
|-- scripts/
|-- assets/
|   |-- demo-game-experience-before-after.png
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-game-experience-analyzer.png
|   |-- showcase-voi-ooda.png
|   |-- showcase-book-translator.png
|   |-- showcase-source-curator.png
|   `-- showcase-game-concept-architect.png
|-- game-experience-analyzer/
|-- paranoia-ai-system-evolver/
|-- game-design-book-translator/
|-- game-design-source-curator/
`-- game-concept-architect/
```

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
```

## License

本仓库的 skill documents and tooling 使用 [MIT License](./LICENSE) 发布。

Paranoia 名称、logo、视觉识别和项目品牌不作为商标授权。examples 可能有各自的 `source_status`、`case_type` 或来源元数据，复用前请检查对应文件 frontmatter。

## Skill 包约定

每个 skill 都是一个可独立安装的包：`SKILL.md` 放运行入口，`references/` 放方法说明，`templates/` 放可复用表单，`examples/` 和 `evals/` 用于展示与回归检查。

## 贡献

提交公开 examples、evals、assets、showcases 或 release notes 前，请确保材料为 synthetic、公开材料或明确 cleared material。具体规则见 [CONTRIBUTING.md](./CONTRIBUTING.md)。

## 设计原则

```text
Evidence ledger before opinion.
Operating model before prompt.
Feasibility before scope.
Alternatives before recommendation.
Shadow before enforcement.
Eval before promotion.
Rollback before confidence.
```

## 未来 Skill

未来根据社区反馈和 skill 成熟度，可能继续加入 AI + 独游实战全流程方向的包，例如：

- `indie-game-production-master`：覆盖独游从想法验证、GDD/Gate、原型、playtest、AI 资产流水线、Steam/发布策略到复盘沉淀的全流程制作 skill。
- `godot-ai-game-production`：覆盖 Godot + AI 项目搭建、设计真源、数据契约、资源流水线、headless/keyshot 验证、Demo/Release Gate 和工程复盘的生产 skill。
