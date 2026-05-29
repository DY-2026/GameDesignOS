# Game Design Source Curator

**父项目:** [ParanoiaSkills](../README.zh-CN.md)

**语言:** 简体中文 | [English](./README.en.md)

这是 `ParanoiaSkills` 里的一个可安装 skill，用于把零散的游戏设计来源沉淀成可维护的知识资产。

## 适用场景

- 长期收集高质量游戏设计资料
- 给网站、作者、UP 主、公众号或专栏建立来源档案
- 对文章、视频、复盘、方法论做证据门审核
- 把通过资料写入本地 `docs/` 知识库
- 做增量更新、去重、catalog、registry 和 update-history 维护
- 为通过资料补一张可验证的设计实验启发卡

## 结构

- `SKILL.md`：轻量入口，给 agent 判断何时加载与如何执行。
- `references/curation-workflow.zh-CN.md`：完整策展流程。
- `references/scoring-and-evidence-gates.zh-CN.md`：评分、证据门与平台边界。
- `templates/`：来源档案、catalog、资料卡、registry、更新历史模板。
- `agents/openai.yaml`：Codex UI 展示元数据。

## 同步规则

本目录是项目内可追踪副本。后续如果运行副本发生变化，请同步回本目录，并重新校验两边内容一致。

Copyright (c) 2026 @Paranoia. All rights reserved.
