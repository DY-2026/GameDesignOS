# GameDesignOS v1.0 本地 CLI

这里是 GameDesignOS 的可执行本地 runtime。

v1.0 的 CLI 不是自动写策划案的工具，而是一个确定性的项目操作层：它帮助真实游戏项目记录 Decision、Assumption、Evidence、Experiment、Gate、Workflow 和 Learning，并在进入承诺态前停到 Human Gate。

## 安装

在仓库根目录执行：

```bash
python -m pip install -e .
gamedesignos --version
```

## 快速开始

```bash
python -m gamedesignos "我想做一款修灯塔的策略游戏"
```

这条命令会自动推荐 skill。对项目型请求，它会把项目、第一条决策、第一条假设、三分钟验证实验和工作流一次准备好。之后先按终端输出做一次小测试，再记录观察。

## 主路径

```text
Decision Object
-> Assumption
-> VOI / Evidence / Scope / Experiment / Rollback Gate
-> Experiment Plan
-> Evidence Ledger
-> Experiment Result
-> Experiment Review
-> Human Gate
-> Learning candidate
```

## 兼容

- 默认新建 v1.0 workspace。
- 旧 v0.8/v0.9 workspace 仍可打开和校验。
- 如需创建旧模板，使用 `--workspace-version 0.8.0`。

完整命令见 [commands.md](./commands.md)。
