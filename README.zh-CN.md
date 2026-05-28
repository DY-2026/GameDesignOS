<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills 游戏设计工作流封面图" width="100%">
</p>

<h1 align="center">ParanoiaSkills</h1>

<p align="center">
  Paranoia 的游戏设计 skill 库，适用于 Claude Code、Codex、OpenCode 和任意智能体 CLI 工作流。
</p>

<p align="center">
  <a href="./README.zh-CN.md">简体中文</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="#当前-skill">当前 Skill</a> ·
  <a href="#图文展示">图文展示</a> ·
  <a href="#未来-skill">未来 Skill</a>
</p>

<p align="center">
  Copyright (c) 2026 @Paranoia. All rights reserved.
</p>

ParanoiaSkills 是一个开放 skill 库，把游戏设计阅读、翻译、资料策展和 AI 工作流演化，沉淀成可复用的操作方法。

它不是 Codex 专用。这里的 skill 以可迁移的 agent instruction、references 和 templates 组织，Claude Code、Codex、OpenCode，或者任何能加载 Markdown skill / prompt / template 的智能体 CLI，都可以根据自己的环境使用或改造。

大多数 AI 工作流停在“答得不错”。ParanoiaSkills 关心的是更难的第二步：把一次好结果变成可重复调用的 skill、可维护的知识资产，以及不会失控漂移的进化流程。

这个项目的野心很清楚：把它做成 GitHub 上最值得游戏设计师、设计研究者和 AI-assisted creators 长期收藏与复用的游戏设计工作流项目之一。

它也会随着社区关注继续生长：每当这个仓库获得更多认可，ParanoiaSkills 都会把新的、更成熟的游戏设计 skill 加进来，让这个库从个人方法沉淀，逐步长成一套可共享的游戏设计基础设施。

## 这个仓库是什么

这是 Paranoia 的游戏设计库：一组面向游戏设计阅读、翻译、资料策展和 AI-assisted workflow 的可复用 skill。

每个包都是一个可安装 skill，拥有自己的 agent 入口、人类说明文档、方法论 references、可复制 templates 和验证边界。这个库服务的是认真对待游戏设计这门手艺的人：来源质量、术语、证据、迭代、回退，以及真正可复用的方法。

## 图文展示

<table>
  <tr>
    <td width="33%">
      <img src="./assets/showcase-source-curator.png" alt="Game Design Source Curator 展示图">
    </td>
    <td width="33%">
      <img src="./assets/showcase-book-translator.png" alt="Game Design Book Translator 展示图">
    </td>
    <td width="33%">
      <img src="./assets/showcase-voi-ooda.png" alt="Paranoia AI System Evolver 展示图">
    </td>
  </tr>
  <tr>
    <td><b>策展资料</b><br>把散落在文章、视频、作者、专栏和网站里的内容，变成可长期维护的游戏设计知识库。</td>
    <td><b>翻译设计知识</b><br>把严肃的游戏设计书籍和章节，变成自然、专业、可复查的中文设计写作。</td>
    <td><b>演化工作流</b><br>用 VOI、OODA、eval、Human Gate 和 rollback 升级 prompt、schema、memory 和 tool routing。</td>
  </tr>
</table>

## 当前 Skill

| Skill | 为什么值得用 | 包目录 |
| --- | --- | --- |
| **Paranoia AI System Evolver** | 把 prompt、workflow、memory、schema、RAG、tool routing 和 eval 的改动，变成受控的系统演化。它用模型压缩和因果中介找关键控制点，用 VOI/OODA 校准现实，对高影响改动设置 Human Gate，并让升级可以 rollback。 | [`paranoia-ai-system-evolver/`](./paranoia-ai-system-evolver/) |
| **Game Design Book Translator** | 把英文游戏设计/研发材料翻译成真正像中文设计写作的专业文本，而不是机翻腔。它覆盖术语表、章节、图注、表格、QA 和来源边界检查。 | [`game-design-book-translator/`](./game-design-book-translator/) |
| **Game Design Source Curator** | 把散落在文章、视频、作者、专栏和网站里的游戏设计资料，变成可长期维护的知识库。它使用证据门、评分、HTML 归档、registry、update history 和设计实验卡。 | [`game-design-source-curator/`](./game-design-source-curator/) |

这三个 skill 合起来，形成一条完整链路：

```text
发现高质量资料
-> 翻译并结构化设计知识
-> 连接到方法、项目和实验
-> 升级执行这套工作的 agent workflow
-> 在需要时验证、版本化和回退
```

## 为什么游戏设计师会需要它

游戏设计知识天然是散的。好东西藏在书、演讲、postmortem、论坛、内部笔记、视频和制作经验里。普通 AI 总结很容易把这些材料压扁，变成一段“看似懂了”的概括。

ParanoiaSkills 做的是更慢、但更值钱的那部分工作：

- **从链接到知识:** 资料要经过筛选、评分、归档，并连接到具体设计用途。
- **从翻译到设计素养:** 翻译要保住论证结构、术语、图表和生产语境。
- **从 prompt 成功到 workflow 记忆:** 有用的 agent 行为，只有在有证据、eval 和 rollback 路径后，才进入候选方法。
- **从个人笔记到可复用基础设施:** templates、references 和包边界让方法可以迁移、复查和继续升级。

## 它怎么工作

每个 skill 都用轻量 `SKILL.md` 作为 agent 入口。长方法放在 `references/`，可复制表单放在 `templates/`，工具或平台相关元数据放在 `agents/`。

```text
SKILL.md      -> 什么时候用、边界是什么、快速流程是什么
references/  -> 更完整的方法、Gate、评分规则和验证 playbook
templates/   -> 可直接复制到真实项目里的工作表单
agents/      -> 支持这些元数据的 agent 环境可读取
```

## Prompt 示例

```text
Use $game-design-source-curator to review these game design sources and turn accepted items into a maintainable local knowledge base.
```

```text
Use $game-design-book-translator to translate and polish this game design chapter into professional Chinese, including terminology and figure captions.
```

```text
Use $paranoia-ai-system-evolver to turn this AI workflow problem into a controlled evolution proposal with model compression, causal mediators, VOI, OODA, evals, Human Gate, and rollback.
```

## 未来 Skill

未来根据社区反馈和 skill 成熟度，可能继续加入 AI + 独游实战全流程方向的包，例如：

- `indie-game-production-master`：覆盖独游从想法验证、GDD/Gate、原型、playtest、AI 资产流水线、Steam/发布策略到复盘沉淀的全流程制作 skill。
- `godot-ai-game-production`：覆盖 Godot + AI 项目搭建、设计真源、数据契约、资源流水线、headless/keyshot 验证、Demo/Release Gate 和工程复盘的生产 skill。

## 当前结构

```text
ParanoiaSkills/
|-- README.md
|-- README.zh-CN.md
|-- README.en.md
|-- assets/
|   |-- voi-ooda-system-evolver-hero.png
|   |-- showcase-source-curator.png
|   |-- showcase-book-translator.png
|   `-- showcase-voi-ooda.png
|-- game-design-book-translator/
|-- game-design-source-curator/
`-- paranoia-ai-system-evolver/
```

## 总体管理规则

- 根目录 README 只讲整个 `ParanoiaSkills`：定位、目录、结构和治理规则。
- 每个 skill 目录只讲一个具体可安装 skill。
- `SKILL.md` 保持轻量，只放触发条件、核心流程、边界和按需读取路径。
- 长文方法论放进 `references/`。
- 可复制工作表单放进 `templates/`。
- `SKILL.md` frontmatter `name`、文件夹名、`agents/openai.yaml` 默认提示保持一致。
- 如果某个 skill 在 `C:\Users\Admin\.codex\skills` 下还有运行副本，后续运行副本发生变化时，必须同步回本项目同名目录，并校验两边副本。

## 版权

Copyright (c) 2026 @Paranoia. All rights reserved.
