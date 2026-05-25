<p align="center">
  <img src="./assets/voi-ooda-system-evolver-hero.png" alt="ParanoiaSkills skill library hero" width="100%">
</p>

# ParanoiaSkills

**语言:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

ParanoiaSkills 是 @Paranoia 的公开技能库，用来整体管理可复用、可安装的 Codex / Agent skills。

这里的重点不是把一个 skill 写得很大，而是把多个 skill 当成一个可维护的技能库来管理：

```text
根目录 README：介绍整个 ParanoiaSkills。
每个 skill 目录：介绍一个具体可安装 skill。
SKILL.md：给 agent 加载的轻量入口。
references/：按需读取的方法论和规则。
templates/：可直接复制使用的工作表单。
```

## Skill 目录

| Skill | 用途 | 包目录 |
| --- | --- | --- |
| VOI-OODA AI System Evolver | 用 VOI、OODA、eval、Human Gate、版本管理和 rollback 受控升级 AI 系统 | [`voi-ooda-ai-system-evolver/`](./voi-ooda-ai-system-evolver/) |

## 当前结构

```text
ParanoiaSkills/
├── README.md
├── README.zh-CN.md
├── README.en.md
├── assets/
│   └── voi-ooda-system-evolver-hero.png
└── voi-ooda-ai-system-evolver/
    ├── SKILL.md
    ├── README.md
    ├── README.zh-CN.md
    ├── README.en.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── evolution-loop-playbook.md
    │   ├── evolution-loop-playbook.zh-CN.md
    │   ├── evolution-loop-playbook.en.md
    │   ├── eval-versioning-playbook.md
    │   ├── eval-versioning-playbook.zh-CN.md
    │   └── eval-versioning-playbook.en.md
    └── templates/
        ├── evolution_proposal.md
        ├── evolution_proposal.zh-CN.md
        ├── evolution_proposal.en.md
        ├── ooda_voi_state.md
        ├── ooda_voi_state.zh-CN.md
        └── ooda_voi_state.en.md
```

## 总体管理规则

- 根目录只讲整个 `ParanoiaSkills`：定位、目录、索引和治理规则。
- 具体 skill 的介绍、安装提示和方法论入口放在各自目录里。
- 每个 skill 的 `SKILL.md` 保持轻量，只放触发条件、核心流程和按需读取路径。
- 长文方法论放 `references/`，可复制表单放 `templates/`。
- 每新增一个 skill，都要同步更新根 README 的 Skill 目录。
- 每个公开 skill 至少保持 `README.md`、`README.zh-CN.md`、`README.en.md` 三个入口。
- `SKILL.md` frontmatter `name`、文件夹名、`agents/openai.yaml` 默认提示保持一致。

## 当前 Skill

### VOI-OODA AI System Evolver

目录：[`voi-ooda-ai-system-evolver/`](./voi-ooda-ai-system-evolver/)

用于升级 AI 系统、Agent workflow、Codex skill、prompt、memory、RAG、tool routing、schema、eval set 或反馈闭环。它强调：

- VOI：哪些信息值得获取。
- OODA：如何在任务中持续校准地图。
- Evals：哪些改动有资格留下。
- Human Gate：哪些动作必须人工确认。
- Rollback：如何把升级变成可回退行为。

## 版权

Copyright (c) 2026 @Paranoia. All rights reserved.
