# Changelog

All notable changes to ParanoiaSkills will be recorded here.

## [Unreleased]

### Added

- 待补充下一次发布内容。

### Changed

- 待补充下一次发布内容。

---

## [v0.3.0] - 2026-05-31

### Added

- game-experience-analyzer 新增 `game_dissection_diagnosis` 分析模式与完整拆解输出模板（game-dissection 报告）。
- game-concept-architect 新增 `player verb inventory`、`uncertainty calibration`、`system dynamics map`、`content flow plan`、`audience desire map` 与 `playable theme map` 模板与路由链路。
- 扩展 evals/negative cases/rubric，使技能更清晰拒绝“拍脑袋建议”和“直接迁移抄袭”类输出。
- 新增 release 文档与版本说明文件，补齐 v0.3 版本说明语义。

### Changed

- 将 `game-experience-analyzer` 的输出要求从单一经验审查扩展为“作品拆解 + 机制可迁移评估 + 证据归因”三层验证。
- `game-concept-architect` 的结果链路从 idea/seed 提升为“概念 -> 动词 -> 对齐 -> 不确定性 -> 动态 -> 流程 -> 受众 -> 可玩主题 -> 验证计划”的完整闭环。

### Fixed

- 统一了公开示例的边界说明（合规说明、可复用输出字段、结构化输出要求）。
- 修复了拆解报告在高层次机制复用讨论中缺少验收口径的问题。

### Documentation

- 重新组织 `releases/v0.3.0.md`，采用更接近开源项目的分段写法（Highlights / Added / Changed / Validation / Safety）。
- 新增 `CHANGELOG.md`，建立统一变更追踪入口。
- 新增 `releases/README.md`，定义标签策略、Release 步骤与 Git 操作清单。

### Safety

- 保留了公开素材边界：所有新增示例与文档不引入私有项目信息。

## [v0.2.0] - 2026-05-30

### Added

- 新增 `game-concept-architect`，完成五个核心 skills 的公开骨架。
- 引入 `adapters`、`contracts`、`CONTRIBUTING.md` 与仓库验证入口。

### Changed

- 将仓库组织从单一 skill preview 向 “设计产出 / 流程治理 / 知识资产” 分层结构迁移。
- 补充多项可验证的公开安全边界规则，增强案例与素材提交约束。

## [v0.1.0] - 2026-05-29

### Added

- 发布 `game-experience-analyzer` 公开可运行基础版本。
- 增加发布草案、安装指引与基础验收样例。

---

[Unreleased]: https://github.com/your-org/ParanoiaSkills/compare/v0.3.0...HEAD
[v0.3.0]: ./releases/v0.3.0.md
[v0.2.0]: ./releases/v0.2.0.md
[v0.1.0]: ./releases/v0.1.0.md
