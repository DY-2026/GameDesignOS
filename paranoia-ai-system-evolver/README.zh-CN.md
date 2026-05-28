# Paranoia AI System Evolver

**所属项目:** [ParanoiaSkills](../README.zh-CN.md)

**语言:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 @Paranoia. All rights reserved.

这是 `ParanoiaSkills` 里的一个具体可安装 skill。它负责“AI 系统受控进化”这个能力，不代表整个技能库。

## 这个 Skill 做什么

它帮助 agent 改进 AI 系统，同时避免把一次成功案例直接提升成永久规则。它组合了：

- 模型压缩：判断 prompt、skill、agent、workflow 或 harness 是否用更短的核心模型解释更多真实任务。
- 因果中介：把最终结果拆成可观察、可干预、可验证的中间链路。
- VOI：判断哪些信息值得获取。
- OODA：维护紧凑的 Observe / Orient / Decide / Act 状态。
- Evals：检查结果质量、过程质量和进化风险。
- Human Gate：高影响改动必须人工确认。
- Rollback：每个被提升的改动都要可回滚。

## 包内容

```text
SKILL.md
agents/openai.yaml
references/evolution-loop-playbook.md
references/evolution-loop-playbook.zh-CN.md
references/evolution-loop-playbook.en.md
references/model-compression-playbook.md
references/model-compression-playbook.zh-CN.md
references/model-compression-playbook.en.md
references/eval-versioning-playbook.md
references/eval-versioning-playbook.zh-CN.md
references/eval-versioning-playbook.en.md
templates/evolution_proposal.md
templates/evolution_proposal.zh-CN.md
templates/evolution_proposal.en.md
templates/ooda_voi_state.md
templates/ooda_voi_state.zh-CN.md
templates/ooda_voi_state.en.md
quick_validate.py
```

## 推荐提示词

```text
使用 $paranoia-ai-system-evolver，把这个 AI workflow 问题整理成带模型压缩、因果中介、VOI、OODA、eval、Human Gate 和 rollback 的受控进化提案。
```

## 在 ParanoiaSkills 里的边界

- 根目录 README 负责整个 `ParanoiaSkills` 的目录、索引和管理规则。
- 本目录 README 只解释 `paranoia-ai-system-evolver` 这个 skill。
- `SKILL.md` 是 agent 入口，保持轻量。
- `references/` 是方法论，按需读取。
- `templates/` 是可复制表单。

## 维护规则

- `SKILL.md` 保持轻量，只做触发、工作流和按需读取路由。
- 长期方法论放在 `references/`。
- 可复制工作表单放在 `templates/`。
- 改动后先运行 `quick_validate.py`，再同步运行时副本并做一致性校验。
- `name`、文件夹名、`agents/openai.yaml` 和公开 README 的命名保持一致。
- 全局安装、长期记忆写入和生产影响改动都属于 Human Gate。
