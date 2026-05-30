---
name: game-design-source-curator
description: "Use when curating game design sources into a durable local knowledge base: source research, candidate screening, evidence-gated review, canonical ingestion, incremental updates, source catalogs, HTML archives, and design inspiration cards. Do not use for one-off summaries, casual recommendations, general news browsing, or translation-only tasks without knowledge-base ingestion."
metadata:
  short-description: 游戏设计资料策展、审核、入库与增量更新
---

# Game Design Source Curator

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

把到处看到的文章、视频、作者、专栏和网站，变成一套可持续维护的游戏设计知识资产。

## 核心目标

目标不是收藏链接，而是沉淀可追踪、可复查、可复用的知识库条目。每轮执行至少交付：

- 来源是否值得长期跟踪
- 本轮新增候选、拒收和正式入库条目
- 关键证据、评分、置信度和拒收理由
- 与现有方法论、项目、案例或专题资料的连接点
- 每条通过资料对应的设计实验启发
- 本轮是否只是当前轮次扫描，不要暗示已经具备后台自动监控能力

## 触发条件

优先使用本 skill：

- 用户要持续收集高质量游戏设计资料，并沉淀到本地 `docs/`
- 用户提到“帮我盯这个网站 / 作者 / UP 主 / 公众号 / 专栏”
- 用户要求按标准审核后再入库，而不是见文就收
- 用户要求做增量更新，而不是每次从头全量重跑
- 用户希望把新资料和既有方法论、案例、项目资料串起来
- 用户希望顺手获得可用于设计实践的启发或实验卡

默认不使用本 skill：

- 只总结一篇文章或一条视频
- 只做一次性推荐，不要求落库
- 只浏览泛行业资讯、新闻、发行动态
- 只想要作者清单，不要求审核和入库
- 只做翻译，不做策展与知识沉淀

## 快速工作流

1. **Observe：确认任务模式。** 在来源研究、首轮建档、候选审核、标准入库、增量更新、批量巡检中选一个主模式。
2. **VOI 门：只收集会改变决策的信息。** 先做 URL 标准化、去重、元数据提取、规则门和短读；只有 shortlist 才深读。
3. **Orient：对齐库内规范。** 先读 `AGENTS.md`、`README.md`、已有 `registry.json`、目标来源 `source-profile.md`、`catalog.md`、已有 item 和 `update-history.md`。
4. **Decide：状态推进必须有证据。** 只看标题、摘要、简介、章节、可见字幕片段时最多推进到 `shortlisted`；未深读不得进入 `accepted`。
5. **Act：落盘到既有结构。** 优先沿用仓库现有目录；无规范时使用 `docs/research/curated-game-design/` 默认结构。
6. **Evaluate：完成输出门。** 检查 catalog、registry、update-history、HTML 归档、知识链接和灵感发芽是否同步完成。

## 默认状态

- `discovered`：已发现，尚未初筛
- `shortlisted`：短读后值得深读
- `candidate`：有潜力，但证据不足或价值尚未确认
- `needs-manual-review`：正文、字幕或核心证据不可得，需要人工补证据
- `rejected`：未通过规则门或最终审核
- `accepted`：完成深读并通过正式收录判定
- `ingested`：已写入 canonical 文档并完成 catalog / registry 更新
- `duplicate`：与库内已有资料重复或高度重合

## 默认落盘结构

先遵守仓库现有规范。若无现成规范，使用：

```text
docs/research/curated-game-design/
  registry.json
  inbox.md
  update-history.md
  websites/
    <source-slug>/
      source-profile.md
      catalog.md
      items/
      original-html/
      bilingual-html/
  creators/
    <platform>-<creator-slug>/
      source-profile.md
      catalog.md
      items/
      original-html/
      bilingual-html/
  attachments/
```

HTML 归档是正式入库的必要层：中文资料至少保存可本地阅读的 HTML；非中文资料必须生成带图双语 HTML，并保留关键术语原文。

## 按需读取

- 完整策展流程、任务模式、低 token 工作流、增量和幂等规则：`references/curation-workflow.zh-CN.md`
- 审核硬门槛、评分系统、证据上限和平台边界：`references/scoring-and-evidence-gates.zh-CN.md`
- 来源档案、catalog、registry、资料卡和更新历史模板：`templates/`

## 输出门

完成一轮来源研究、入库或增量更新后，按顺序确认：

1. `catalog.md` 已更新或说明为何无变化
2. `registry.json` 已更新或说明为何无变化
3. `update-history.md` 已追加本轮记录
4. 通过条目已生成 canonical 文档与必要 HTML 归档
5. 通过条目已连接到现有方法论、项目或案例；无锚点时明确写“当前库内暂无直接对应条目”
6. 每条通过资料都有“灵感发芽”实验卡
7. 只有实际新增 canonical 文档或结构变动时才刷新 wiki

## 不要做

- 不要见文就收、短读即入库、或把营销稿和高质量复盘放在同一层级
- 不要忽略去重、证据门、平台现实边界和置信度
- 不要把非中文资料整篇生硬直译，或丢失关键专名原文
- 不要把超长原文 HTML 塞进 Markdown 主体
- 不要在没有实际新增时刷新整套 wiki
- 不要承诺后台持续监控，除非当前环境已经明确创建并验证调度器
