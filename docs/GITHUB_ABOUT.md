# GitHub About Metadata

这份文件是 GitHub 仓库 About 区域的文案真源。修改公开仓库设置属于 Human Gate：先在这里评审，再由仓库维护者手动更新线上设置。

定位依据见 [2026-07-11 GitHub 首页对标记录](./2026-07-11-github-readme-benchmark.md)，执行检查见 [GitHub About Checklist](./github-about-checklist.md)。

## Description

```text
Local-first game design OS for AI agents: turn sessions into evidence, experiments, reviewable decisions, and durable project memory—with Human Gates and rollback.
```

这句话与 README 首屏的“AI output -> verifiable decisions”保持一致，先说用户得到什么，再说明 Human Gate 与 rollback；不写容易漂移的版本号、数量、stars 或未经证明的采用规模。

## Repository URL

```text
https://github.com/DY-2026/GameDesignOS
```

公开文章和历史链接已经依赖这个地址；除非用户明确接受链接迁移成本，否则不改仓库 URL。

## Display Name

- 项目短名：`GameDesignOS`
- 署名需要出现时：`GameDesignOS by Paranoia`

## Website

在有独立产品站或文档站前留空，不重复填写仓库自身 URL。

## Topics

```text
ai-agents
agent-skills
game-design
game-development
game-analysis
game-research
game-design-tools
indie-game
local-first
human-in-the-loop
decision-support
workflow-automation
python
```

Topics 只保留与当前公开能力直接相关的发现词；候选 skill、未来路线和尚未发布能力不进入这里。

## 2026-07-23 线上审计快照

状态：`needs_sync`

### facts

- 线上 Description 仍是旧文案：`Local-first OS for AI-assisted game design: turn AI-agent sessions into decisions, evidence, experiments, proposals, and durable project memory.`
- 线上 Website 是仓库自身的 `#readme` 链接，而本真源要求在没有独立站点时留空。
- 线上 Topics 仍是旧的 7 项集合，尚未同步上面的当前能力与发现词。
- 远端已有 `v0.1.0` 至 `v1.2.0` 共 13 个 tag，但 GitHub Releases 数量仍为 0。

### inference

- About 设置和正式 Release 页面尚未跟上仓库内已经完成的品牌、版本与 release-note 工作。

### needs_more_evidence

- 维护者完成线上设置后，需要重新打开公开仓库和 Release 页面读回验证；未读回前不得把状态改成 `synced`。
