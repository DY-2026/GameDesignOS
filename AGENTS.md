# GameDesignOS Agent 入口

这份文件给 Codex、Claude Code、OpenCode 等支持 `AGENTS.md` 的 agent 使用。目标是让用户拉取项目后，不需要先读完整 README，也不需要知道每个 skill 名字。

## 默认接法

当用户在这个仓库里随便发一句游戏设计、立项、体验分析、资料整理、翻译、工作流升级或策划案需求时，先走自然语言入口：

```bash
python -m gamedesignos ask "<用户原话>"
```

如果用户没有写 `ask`，也可以直接执行：

```bash
python -m gamedesignos "<用户原话>"
```

这个入口会做三件事：

- 推荐应该使用的 skill，并给出可审计的 `Use $skill-name ...` 提示词；
- `ask` 默认只做路由和状态审计；只有用户显式提供 `--destination` / `--workspace`，或明确调用 `start`，才创建或恢复 Project-Ready workspace。
- 给宿主 agent 一个明确的下一步执行线索。

默认 workspace 会放在公开仓库外侧的相邻目录，避免把真实项目资料写进本仓库。

## Agent 执行规则

`ask` 的输出不是最终答案，也不是让用户自己复制提示词。拿到推荐路线后，agent 要继续把事情办完：

- 如果需求已经明显属于某个 skill，agent 可以直接读取并调用该 skill，不必先让用户知道 skill 名。
- 如果只缺少输入材料或边界，agent 自己问最少的问题；用户补充后继续调用对应 skill。
- 如果使用了 `ask`，就把它当作路由和状态审计：按推荐 skill 读取 `SKILL.md`，必要时读取该 skill 指向的 reference/template，然后直接产出结果。
- 如果 `ask` 创建了 Project-Ready workspace，就把 workspace 当作长期项目记忆；后续产物写回对应的 decision、evidence、experiment、workflow 或 learning。
- 最终回复给用户的是本次任务的成果、下一步动作或需要确认的 Human Gate，不是“你可以使用某某 skill”。

## 什么时候用整个项目

用户想长期推进一个项目时，使用 GameDesignOS 项目模式：

```bash
python -m gamedesignos start "<项目名或一句话想法>"
```

它会自动准备第一条 Decision、Assumption、三分钟验证 Experiment、VOI Gate 和 Workflow Run。下一步只做终端输出里的那件事。

## 每个 Skill 单独怎么用

用户只想要一次性产出时，可以直接点名对应 skill；如果用户没有点名但意图已经明确，agent 自己选择并调用即可：

| 用户说法 | 单独使用 |
| --- | --- |
| 截图、录屏、PV、视频、商店页、试玩样本 | `Use $game-experience-analyzer ...` |
| 一句话游戏创意、玩法点子、核心循环、立项方向 | `Use $game-concept-architect ...` |
| 留存、首局、节奏、反馈、具身感、氛围、认知负荷、A/B、埋点 | `Use $game-experience-density-optimizer ...` |
| 商业策划案、独游设计案、pitch、GDD、vertical slice、决策 memo | `Use $game-design-proposal-writer ...` |
| prompt、workflow、schema、eval、router、memory、skill 改造 | `Use $paranoia-ai-system-evolver ...` |
| 英文游戏设计章节、术语表、长文翻译 | `Use $game-design-book-translator ...` |
| 文章、视频、作者、栏目、网站、知识库整理 | `Use $game-design-source-curator ...` |

如果不确定，先运行 `python -m gamedesignos ask "<用户原话>"`，用它的推荐路线；如果会触发 Human Gate、发布、删除、真实账号、长期规则升级或项目范围锁定，再停下来问用户确认。

## 安全边界

- 不把用户真实项目资料提交到公开仓库。
- 不替用户接受 Human Gate、发布承诺、删除资产或锁定项目范围。
- 不把一次实验结果直接升级成长期规则；先保持 candidate。
- 不做镜像覆盖、批量删除、强制迁移旧 workspace。
