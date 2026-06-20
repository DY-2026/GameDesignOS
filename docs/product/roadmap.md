# GameDesignOS Roadmap

路线图按能力门推进，不承诺空泛日期。一个阶段只有在上一层有可评审案例、稳定契约和回归覆盖后，才进入下一阶段。

## v0.8.0 — Runtime Foundation

主题：从 skill 包走向项目 workspace。

交付：

- 产品愿景与系统架构；
- workspace template 和 manifest；
- decision-information 与 workspace-level contracts；
- decision-to-information 路线和四条核心生产 workflow；
- workspace-aware adapters；
- planned CLI surface；
- validation 和 release integration。

退出门：

- 一个 synthetic project 能被 coherent 地表示成 workspace assets；
- 现有 skills 保持向后兼容；
- repository validation 通过。

## v0.9.0 — Local Runtime Prototype

已交付命令：

```text
gamedesignos init <project>
gamedesignos status
gamedesignos voi <decision-id>
gamedesignos route <task>
gamedesignos new <asset-type>
gamedesignos validate
gamedesignos pack
gamedesignos doctor
```

已交付行为：

- 从模板初始化 workspace；
- 检查 manifest、asset index、accepted decisions 和 current default actions；
- 排序候选信息动作并执行 research stop rule；
- 推荐最小合适 skill；
- 创建 contract-shaped artifact stubs；
- 校验 workspace 结构和引用；
- 生成可评审 pack。

## v1.0.0 — Project-Ready GameDesignOS

详细计划：[v1.0-development-plan.md](./v1.0-development-plan.md)。

v1.0 的目标不是更多命令，而是让真实游戏项目可以连续使用 GameDesignOS 管理完整周期：

```text
想法 -> 假设 -> 证据 -> 实验 -> 决策 -> 复盘 -> 下一轮演化
```

已交付能力：

- v1 workspace structure，默认决策优先目录；
- core models：Decision、Assumption、Evidence、Experiment、Learning、GateResult；
- v1 CLI 分组：`decision`、`assumption`、`evidence`、`experiment`、`workflow`；
- Decision Graph inspect 与 Mermaid export；
- VOI、Evidence、Scope、Experiment、Commitment、Rollback gates；
- Project Health Scan 和 Next Best Action；
- `gamedesignos ask` / `gamedesignos "<一句话>"` 自然语言入口；
- `gamedesignos start` 一键项目入口；
- v0.8/v0.9 workspace 兼容；
- public/private source-status pack 边界。

v1.0 主命令：

```text
gamedesignos ask
gamedesignos "<一句话>"
gamedesignos start
gamedesignos decision new/list/inspect/accept/reject/supersede
gamedesignos assumption new/list/validate
gamedesignos evidence add/list/inspect
gamedesignos experiment plan/result/review
gamedesignos gate run
gamedesignos workflow list/start/status/next/validate
gamedesignos health
gamedesignos next
gamedesignos graph export/inspect
```

退出门：

- 一个真实私有项目可以跨多轮迭代使用 GameDesignOS，而不需要重建上下文；
- accepted decisions、superseded assets、evidence boundaries 和 rollback history 可追踪；
- public/private material boundaries 可操作；
- 行为测试覆盖无 Decision 阻止 research、高影响无 rollback 阻断承诺、未复盘 experiment 不可支撑接受决策、public-synthetic 不导出 private evidence。

## Later Exploration

只有 v1.0 foundation 稳定后再探索：

- game-engine adapters；
- playtest / telemetry connectors；
- visual asset graph；
- multi-agent orchestration；
- team permissions 与 review roles；
- reusable studio overlays；
- optional local knowledge retrieval。

这些不是承诺，只是候选。只有当用户证据表明它们改善设计决策的收益大于系统复杂度时，才进入开发。

## 优先级规则

未来工作按这个公式排序：

```text
positive net VOI
x decision value
x frequency of use
x reuse across projects
x evidence quality
÷ implementation and governance cost
```

不要因为 agent 能生成新表面，就把它加入系统。
