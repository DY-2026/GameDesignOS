# 发布与标签规范（Release & Versioning）

本仓库采用公开开源项目常见的 `SemVer + GitHub Release + 变更日志` 方式管理版本，避免“版本说明写了但标签没发”的情况。

## 版本规则（SemVer）

- `MAJOR.MINOR.PATCH`
- `MAJOR`：对公共能力、输入输出结构、核心行为有不兼容改动。
- `MINOR`：新增 skill、流程、公开能力、非破坏性行为提升。
- `PATCH`：修复错误、文档/校验脚本改进、兼容性细化。

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
- `v0.2.0`（建议从 `201b24d` 提交打 Tag）
- `v0.3.0`（本次提交完成后建议打在当前发布提交）

## 非目标约束

- `CHANGELOG.md` 记录全部公开变更；`releases/vX.Y.Z.md` 记录该版本详情。
- 不在仓库内保留“只改文档名、未同步 tag/发布入口”的半发布状态。
