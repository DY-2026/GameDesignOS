# Paranoia AI System Evolver

**所属项目:** [ParanoiaSkills](../README.zh-CN.md)

**语言:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

这是 `ParanoiaSkills` 里的一个具体可安装 skill。它负责 Paranoia Method 里的“系统演化器”能力，不代表整个技能库。

## 这个 Skill 做什么

它帮助 agent 把行为改动整理成可审计的操作模型提案。目标不是让 AI 多说几句谨慎话，而是判断一个系统改动是否有足够证据、是否降低总描述成本、是否能 shadow 发布、是否能回滚。

这个 skill 用 Paranoia Method 做七件事：

- 操作模型审计：显式写出隐含模型、因果中介和控制点。
- 总描述成本：比较七项成本，而不是只盯 prompt。
- 断言证据账本：区分已验证事实、工具观察、推理判断、未验证假设和人类待确认。
- 反遗漏检查：确认重要替代方案和子 agent 关键信息没有被压缩掉。
- 确定性 gate 优先：schema、routing、validator、retry、rollback 先于 LLM 判断。
- Shadow-first 发布：行为改变类 gate 先走 `off -> shadow -> warn -> enforce -> rollbackable`。
- Human Gate 与 rollback：长期规则必须可批准、可追溯、可回滚。

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
使用 $paranoia-ai-system-evolver，把这个 AI workflow 问题整理成 Paranoia Method 演化提案：操作模型、总描述成本、断言证据账本、反遗漏检查、shadow-first 发布、eval、Human Gate 和 rollback。
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
- 改动后在仓库根目录运行 `python scripts/validate_skill.py paranoia-ai-system-evolver`，再同步运行时副本并做一致性校验。
- `name`、文件夹名、`agents/openai.yaml` 和公开 README 的命名保持一致。
- 全局安装、长期记忆写入和生产影响改动都属于 Human Gate。
