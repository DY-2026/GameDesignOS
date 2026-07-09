# 发布与标签规范（Release & Versioning）

本仓库采用公开开源项目常见的 `SemVer + GitHub Release + 变更日志` 方式管理版本，避免“版本说明写了但标签没发”的情况。

## 版本规则（SemVer）

- `MAJOR.MINOR.PATCH`
- `MAJOR`：对公共能力、输入输出结构、核心行为有不兼容改动。
- `MINOR`：新增 skill、流程、公开能力、非破坏性行为提升。
- `PATCH`：修复错误、文档/校验脚本改进、兼容性细化。

## 新增正式 Skill 的发布检查

新增或正式接入一个 public skill 时，不要只改 skill 目录和 README。必须同步检查：

- `CHANGELOG.md` 是否新增对应版本段。
- `releases/vX.Y.Z.md` 是否新增 release note。
- README trio 的 skill 数量、Skill 表格、展示图和安装路径是否更新。
- `docs/try-it-in-10-minutes.md`、`docs/showcases/README.md` 是否补入口。
- `scripts/validate_repo.py` 是否把新 skill 纳入 required skills。
- release commit 完成后，Git tag 是否应该新增或更新到对应版本。

## Runtime / Workspace 发布检查

新增或改变 Runtime Foundation 时，还必须检查：

- `runtime/workspace-template/` 是否仍可独立复制。
- `runtime/workspace-template-v1/` 是否仍可独立复制。
- `game.designos.yaml` 与 workspace schema 是否同步。
- v0.8/v0.9 workspace 是否仍可兼容打开和校验。
- `contracts/README.md` 是否区分 skill-level 与 workspace-level contract。
- `docs/product/`、`docs/workflows/` 与 README trio 是否同步。
- `scripts/validate_repo.py` 是否覆盖新增必需路径与 workspace 约定。
- 是否明确兼容现有 skill 直接安装方式。
- 是否避免把 private workspace、客户材料或真实项目输出提交到公开仓库。

## 发布文件约定

- 发布说明文件放在 `releases/vX.Y.Z.md`
- 统一版本历史放在 `CHANGELOG.md`
- 根目录/仓库说明可从 `CHANGELOG.md` 引导到对应 release note

推荐的 release note 结构（参考流行开源项目）：

```md
# vX.Y.Z - Release Name

## Highlights
- 核心价值点

### Added
- 新增能力

### Changed
- 行为/流程变更

### Fixed
- 修复点

### Safety
- 合规与边界

### Validation
- 校验命令
```

## 推荐发布流程

1. 准备发布内容
   - 更新对应的 `releases/vX.Y.Z.md`
   - 更新 `CHANGELOG.md`
2. 运行仓库基础校验
   - `python scripts/validate_repo.py`
   - `python scripts/validate_skill.py game-concept-architect`
   - `python scripts/validate_skill.py game-experience-analyzer`
   - `python scripts/validate_skill.py game-experience-density-optimizer`
   - `python scripts/validate_skill.py game-design-proposal-writer`
3. 提交 release commit
   - `git commit -m "chore(release): prepare vX.Y.Z"`
4. 创建 Git tag（示例）
   - `git tag -a vX.Y.Z <commit> -m "Release vX.Y.Z"`
   - 如果是当前提交：`git tag -a v0.3.0 HEAD -m "Release v0.3.0"`
5. 推送到 GitHub
   - `git push origin main`
   - `git push origin vX.Y.Z`
6. 在 GitHub Release 页面创建对应 tag 的 Release，并粘贴 `releases/vX.Y.Z.md` 内容。

## 当前发布状态

- `v0.1.0`（已存在）
- `v0.2.0`（已存在）
- `v0.3.0`（已存在）
- `v0.4.0`（已补 tag：`game-experience-density-optimizer` 与 ED 实验基础）
- `v0.5.0`（已补 tag：contract layer、WOOP workflow governance 与 README 首屏刷新）
- `v0.6.0`（已存在 tag：新增 `game-design-proposal-writer`、ED experiment compiler、七 skill GitHub 首屏）
- `v0.6.1`（仓库校验修复与 README 版本同步）
- `v0.7.0`（已补 tag：GameDesignOS by Paranoia 公开品牌、GitHub URL、v7 README 封面和案例入口整理）
- `v0.8.0`（已补 tag：Runtime Foundation、Project Workspace、workspace contracts、Decision-to-Information 工作流与 VOI Decision Gate）
- `v0.9.0`（已补 tag：Local Runtime Prototype；`gamedesignos` CLI、workspace 初始化/状态/路由/创建/校验/打包/doctor、VOI 评估与 runtime 单测；GitHub Release 仍需按发布流程创建）
- `v1.0.0`（本地 tag 已补：Project-Ready GameDesignOS；Decision/Assumption/Evidence/Experiment/Gate/Workflow/Learning 主链路、v1 workspace、健康扫描、决策图与完整 runtime 行为测试；GitHub Release 仍需 maintainer 发布）
- `v1.1.0`（本地 tag 已补：RJR-AI Authority Layer；剩余判断权边界、GitHub About 定位、README trio、runtime/package 版本与 router/eval/validator 覆盖已同步；GitHub Release 仍需 maintainer 发布）
- `v1.2.0`（本地已准备 release note：Intent Work Order & Workflow Governance；AI 工作单、workflow-run.governance、Paranoia Checkpoint、runtime/package 版本与 tag backfill 已同步；Git tag/Release 仍需 release commit 后发布）

## 非目标约束

- `CHANGELOG.md` 记录全部公开变更；`releases/vX.Y.Z.md` 记录该版本详情。
- 不在仓库内保留“只改文档名、未同步 tag/发布入口”的半发布状态。
