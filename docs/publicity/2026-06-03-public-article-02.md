# ParanoiaSkills 第二篇：这次不是又加了几个文件，而是把项目做成了一个可试用的工作台

> 面向游戏设计师、独立开发者和 AI agent workflow builder 的公开介绍稿。  
> 建议发布渠道：公众号、知乎、即刻、GitHub Release / README 引流帖。  
> 更新依据：2026-05-28 至 2026-06-03 的仓库更新。

如果第一篇介绍 `ParanoiaSkills`，重点是让大家看到一个能力：AI 可以把游戏录屏、PV、截图拆成有证据的设计诊断，而不是写一篇泛泛的观后感。

那么第二篇值得写，是因为这几天项目发生的变化已经不只是“又补了几个文档”。

它从一个能展示单点能力的 skill，变成了一套更完整的游戏设计 agent 工作台：

```text
一句话创意
-> 可验证的设计蓝图
-> 原型 / 录屏 / PV / 截图
-> 证据化体验诊断
-> 工作流继续演化、验证和回滚
```

这条链路一旦跑通，项目的性质就变了。

它不再只是“我有一个好用的游戏分析 prompt”，而是开始变成一套可安装、可迁移、可验证、可贡献的 Agent Skill 库。

这就是第二篇的重点：这几天到底做了哪些变化，新增了什么，优化了什么，以及为什么这些改变值得单独拿出来说。

## 一、新增了什么：从 1 个核心能力，扩展成 5 个公开基础 Skill

5 月 28 日之后，项目最大的变化，是公开 skill 的结构完整了。

现在仓库里有五个基础 skill：

```text
game-experience-analyzer
game-concept-architect
paranoia-ai-system-evolver
game-design-book-translator
game-design-source-curator
```

这五个 skill 分别覆盖三层工作：

| 层级 | Skill | 解决的问题 |
| --- | --- | --- |
| 设计生产 | `game-concept-architect` | 把一句话游戏创意变成可验证设计蓝图 |
| 设计生产 | `game-experience-analyzer` | 把截图、录屏、PV、视频链接变成证据化诊断 |
| 工作流治理 | `paranoia-ai-system-evolver` | 把 prompt、workflow、schema、eval 改动变成可控演化 |
| 知识资产 | `game-design-book-translator` | 把英文游戏设计资料翻译成专业中文设计文本 |
| 知识资产 | `game-design-source-curator` | 把文章、视频、作者、网站沉淀成长期知识库 |

这不是为了堆数量。

真正重要的是，五个 skill 让项目从“分析一个已有材料”，扩展到“支持一段完整的游戏设计工作流”。

以前你可以拿一段录屏来问：

```text
这个体验哪里有问题？
```

现在你还可以在更早的阶段问：

```text
这个一句话创意的设计核是什么？
哪些假设需要验证？
MVP 应该做什么，什么只是宣传概念？
```

也可以在工作流层继续问：

```text
这套分析流程怎么升级？
怎么加 eval？
什么情况必须人工确认？
改坏了怎么 rollback？
```

这就是第一类新增：项目补齐了从创意、分析、知识整理到 agent 工作流演化的基础能力。

## 二、新增的关键能力：Game Concept Architect

这次更新里，最值得单独讲的新 skill 是 `game-concept-architect`。

它的作用，是把一句话游戏创意扩展成完整但可验证的设计蓝图。

注意，不是把创意直接写成长篇 GDD。

普通 GDD 生成器很容易犯一个问题：你给它一句话，它立刻给你世界观、系统、角色、关卡、成长线、商业化、剧情章节。看起来很完整，但真正的设计核可能还是空的。

`game-concept-architect` 反过来工作。

它会先拆：

- concept seed 是什么？
- 玩家动词是什么？
- 玩家到底在做哪些会改变局面的动作？
- design nucleus 有哪些候选？
- 哪些假设还没有证据？
- 对外宣传承诺是什么？
- 前 10 分钟承诺是什么？
- 长期游玩承诺是什么？
- 哪些进 MVP，哪些进 Vertical Slice，哪些 Demo 后再做，哪些只保留宣传，哪些应该砍掉？

这套能力对独立游戏尤其重要。

因为独立团队最容易被“好点子”带着走：题材很好，氛围很好，脑内画面很好，但真正进入制作时，才发现核心玩家行为没有被验证，scope 早就失控了。

`game-concept-architect` 做的不是帮创意变长，而是帮创意变窄、变清楚、变可测。

这也是它值得成为第二篇重点的原因。

它让 `ParanoiaSkills` 不再只是在项目后段做复盘，而是开始介入设计前段：从“要不要做、怎么做、先验证什么”开始控制风险。

## 三、新增的闭环：Concept-to-Diagnosis Loop

比单个新 skill 更重要的，是两个 skill 之间形成了闭环。

现在项目里有一条很清楚的链路：

```text
game-concept-architect
-> 生成 player-promise-contract
-> 做出原型 / PV / 录屏 / 截图
-> game-experience-analyzer
-> 检查样本有没有兑现承诺
-> 回写下一轮 validation plan
```

这条链路可以叫 `Concept-to-Diagnosis Loop`。

它解决的是游戏设计里一个很常见的问题：

前期 pitch 说的是一套，实际原型呈现的是另一套；宣传片承诺的是一套，玩家前 10 分钟体验到的是另一套；设计文档里写得很热闹，但录屏里看不到玩家真的在做那些动作。

现在可以把“玩家承诺”变成一个贯穿前后的检查对象。

前面用 `game-concept-architect` 定义：

- 对外宣传承诺
- 前 10 分钟承诺
- 长期游玩承诺
- 核心循环
- scope gate
- validation plan

后面用 `game-experience-analyzer` 检查：

- 样本里有没有证据兑现这些承诺？
- 哪些承诺只是写在文档里，录屏或 PV 里看不到？
- 哪些判断样本根本不能证明？
- 下一轮最小验证应该补什么？

这条闭环，是第二篇最应该讲清楚的“质变”。

因为它让项目从“分析工具”变成“设计验证系统”。

## 四、优化了什么：Game Experience Analyzer 不再只是前期体验报告

`game-experience-analyzer` 是第一篇里最容易被看到的能力，但这几天它也做了明显升级。

它不再只是把一段录屏拆成前期体验复盘，而是扩展成多模式、多诊断包的游戏体验分析 skill。

现在它支持的输入更广：

- 截图
- 本地录屏
- PV / 预告片 / 宣传片
- 买量素材
- 商店页
- 视频链接

支持的分析方向也更多：

- 前期体验
- 玩法机制
- 游戏拆解
- 整体项目分析
- MDA
- 系统叙事融合
- 单机流程
- PV 热度预测
- 前瞻机会判断
- 品类策略
- 商业化打断
- UX/UI

更重要的是，它补了“诊断包”和“模式路由”。

也就是说，用户不必每次都手动指定完整结构。你说“帮我看这个 PV 有没有爆款潜力”，它应该进入 PV 热度诊断包；你说“拆这个游戏为什么成立”，它应该进入游戏拆解诊断包；你说“首小时为什么留不住”，它应该进入首小时留存诊断包。

这类优化看起来不像新增 banner 那么显眼，但对实际使用非常关键。

因为一个真正可用的 agent skill，不能只在 demo 输入下表现好。它必须知道不同任务之间的边界：

- 截图不能证明节奏和手感。
- PV 不能证明留存、销量和长期质量。
- 公开视频受访问权限、地区、登录态和工具能力影响。
- 没有样本证据的判断必须标 unknown 或 uncertain。

这次更新强化的就是这种边界感。

它让输出从“看起来很会分析”，更接近“能被项目决策使用”。

## 五、优化了什么：公开仓库开始有贡献边界和安全边界

这次更新另一个很重要但不那么显眼的部分，是 CONTRIBUTING、public/private boundary 和 showcase 规则。

`ParanoiaSkills` 是公开仓库，但它服务的场景很容易碰到真实项目：客户材料、未公开原型、内部路线图、投放策略、商业化假设、私有截图、工作室偏好。

如果不设边界，agent 很容易把一次私有会话里的东西沉淀进公共仓库。

所以这次补了很明确的规则：

- 用户可以在自己的私有环境里用 skill 处理真实项目。
- 但提交回公开仓库的 examples、assets、showcases、evals、docs，只能使用 synthetic、public 或 explicitly cleared material。
- 来源状态不清楚，就标 `needs_review`，不要当成 public material。
- 真实项目代号、客户信息、路线图、预算、档期、私有平台策略、本地路径和内部输出，都不能进公开仓库。

这不是形式主义。

对一个 agent workflow 项目来说，边界就是质量的一部分。

如果一个 skill 连“什么能公开，什么只能留在 private overlay”都分不清，那它越强，风险越大。

这次更新把公开基础 skill 和 private overlay 的关系讲清楚了：公开仓库存方法、模板、通用规则和 synthetic 示例；真实项目留在用户自己的环境中。

这个变化让项目更像一个可以被别人安全使用和贡献的开源项目，而不是作者自己的工作目录。

## 六、优化了什么：从仓库材料变成 10 分钟可试用入口

这几天还补了大量 public onboarding：

- `Try It in 10 Minutes`
- showcase index
- examples index
- GitHub About checklist
- issue templates
- release notes
- README 开头重写
- overview banner
- Star History
- adapter guidance
- contracts
- validation scripts

这些东西单独看都很小。

但合在一起，它们解决的是同一个问题：一个陌生人打开仓库，怎么在 10 分钟内知道自己该怎么开始？

现在新用户不需要先读完整项目结构。

他只需要判断自己手里是什么材料：

| 我手里有什么 | 先试哪个 skill |
| --- | --- |
| PV、录屏、截图、视频链接 | `game-experience-analyzer` |
| 一句话游戏创意 | `game-concept-architect` |
| prompt、workflow、schema、agent 规则 | `paranoia-ai-system-evolver` |

然后复制一个 skill 目录，触发一句最小 prompt，再看输出有没有样本边界、证据、unknown 和 validation plan。

这也是从“作者知道怎么用”到“陌生人也能开始用”的变化。

对外发布第二篇，真正要讲的是这个变化。

不是仓库多了一个 Markdown 文件，而是它开始有了产品入口。

## 七、优化了什么：验证脚本和 fallback 让 skill 更像工程资产

这次更新还补了仓库校验和 per-skill validation。

包括：

- `scripts/validate_repo.py`
- `scripts/validate_skill.py`
- JSON / YAML 解析检查
- PyYAML 缺失时的 fallback parser
- skill folder、`SKILL.md` frontmatter、`agents/openai.yaml` 的一致性检查
- release notes 和 changelog 入口

这些听起来偏工程，但它们决定了 skill 能不能长期维护。

一个 prompt 可以靠感觉复制。

一个 skill library 不行。

它需要知道：

- 文件路径有没有断？
- schema 能不能解析？
- YAML 缺库时能不能降级？
- skill 名和目录名是否一致？
- 新增模板有没有破坏仓库结构？

当项目开始有多个 skill、多种 templates、多份 eval、多种 host adapter 时，验证脚本就不是锦上添花，而是基础设施。

这也是第二篇值得写的原因之一：`ParanoiaSkills` 正在从“内容资产”变成“工程化的 agent workflow 资产”。

## 八、为什么这些改变值得发第二篇

如果只是新增一个小功能，不值得发第二篇。

如果只是 README 改得更好看，也不值得发第二篇。

这次值得写，是因为项目发生了四个层面的变化。

### 1. 能力边界变了

以前重点是：AI 能不能把游戏素材拆成证据化诊断。

现在重点变成：AI 能不能参与从创意、原型、诊断到工作流演化的一整段过程。

这是从单点能力到工作流能力。

### 2. 使用对象变了

以前更像给“想分析游戏体验的人”用。

现在同时服务三类人：

- 游戏设计师：分析录屏、PV、截图和体验问题。
- 独立开发者：把一句话创意变成可验证方案。
- agent workflow builder：把有用流程沉淀成可演化 skill。

这是从单一使用场景到多角色工作台。

### 3. 输出标准变了

以前重点是输出一份好的报告。

现在更强调：

- 样本边界
- evidence_id
- unsupported claims
- validation plan
- eval
- Human Gate
- rollback
- public/private boundary

这是从“写得像分析”到“能被复查和治理”。

### 4. 项目形态变了

以前它像一个作者维护的能力展示。

现在它开始有：

- release notes
- changelog
- adapter
- contracts
- issue templates
- showcase index
- contribution policy
- validation scripts
- 10 分钟试用入口

这是从个人工作流沉淀，到公开 skill library 的转变。

所以第二篇要发的不是“我又更新了”。

而是：这个项目已经进入了一个新的阶段。

## 九、如果你现在想试，可以从这三句开始

如果你手里有一段游戏录屏、PV 或截图：

```text
Use $game-experience-analyzer to diagnose this PV or gameplay recording into sample boundary, timestamped evidence, Hook/Loop/Link/Surprise diagnosis, issue cards, and validation recommendations.
```

如果你手里只有一句话游戏创意：

```text
Use $game-concept-architect to turn this one-line game idea into concept seed extraction, design nucleus options, player promise contract, core loop, scope gate, and prototype validation plan.
```

如果你想升级自己的 agent 工作流：

```text
Use $paranoia-ai-system-evolver to upgrade this workflow with VOI, OODA, eval checks, Human Gate, and rollback.
```

我的建议是，不要先把它当成“AI 能不能给我一个惊艳答案”的工具。

更好的试法是问它：

```text
你凭什么这么判断？
这个样本不能证明什么？
下一步最小验证是什么？
如果这个规则要长期复用，怎么防止它改坏旧行为？
```

这几个问题，才是 `ParanoiaSkills` 真正想解决的东西。

## 结尾

这几天的更新，表面上是新增 skill、补文档、加校验、做 release、整理 showcase。

但背后的变化更简单：

`ParanoiaSkills` 正在把游戏设计里的判断流程，做成 agent 可以安装、执行、复查和演化的工作流包。

它不承诺 AI 会突然变成完美游戏设计师。

它更关心另一件事：当 AI 参与游戏设计时，我们能不能让它少一点玄学，多一点证据；少一点一次性灵感，多一点可复用流程；少一点“我觉得”，多一点“我们怎么验证”。

这就是第二篇值得发的理由。

如果你也在用 AI 做游戏设计、竞品分析、独立游戏立项、设计知识整理或 agent workflow 建设，可以从 `game-experience-analyzer`、`game-concept-architect` 或 `paranoia-ai-system-evolver` 任意一个开始试。

也欢迎 star、提 issue、贡献 synthetic case。

star 越多，我会越优先补更好的公开 demo、adapter 和可复用 skill 模板。

## 附：5 月 28 日之后的更新摘要

- 2026-05-28：加入 `game-design-book-translator` 和 `game-design-source-curator`，并将系统演化 skill 重命名为 `Paranoia AI System Evolver`。
- 2026-05-29：发布 `game-experience-analyzer` 公开基础版，补充 demo、release note、英文 README 和证据化体验分析示例。
- 2026-05-30：加入 `game-concept-architect`，形成五 skill 架构；补充 CONTRIBUTING、LICENSE、adapters、contracts、CI 和仓库验证脚本。
- 2026-05-31：扩展游戏拆解、玩家动词、动作-目标对齐、诊断包、模式路由和 YAML fallback parser。
- 2026-06-01：补充整本书翻译工作流、翻译/润色脚本、global skill 同步脚本和仓库校验增强。
- 2026-06-03：补充 10 分钟试用、showcase index、GitHub About checklist、issue templates、v0.3.0 release draft、overview banner、Star History 和公开示例边界提醒。
