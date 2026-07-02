# GameDesignOS Product

This directory defines the product boundary and evolution path of GameDesignOS.

> 中文摘要：这里描述 GameDesignOS 为什么存在、它由哪些层组成、v0.8.0 的 MVP 边界、v0.9.0 的本地 runtime 原型、v1.0.0 如何演进为 Project-Ready 的游戏设计操作系统，以及 v1.1.0 如何补上 RJR-AI 剩余判断权边界。

## Documents

- [Product Vision](./vision.md): why GameDesignOS exists and what problem it solves.
- [System Architecture](./architecture.md): Skill Kernel, Contract Layer, Project Workspace, Runtime Interface, and governance.
- [v0.8.0 MVP Definition](./mvp-definition.md): scope, non-goals, success criteria, and acceptance gates.
- [v0.9.0 Definition](./v0.9.0-definition.md): executable local runtime boundary, commands, success criteria, and release gate.
- [v1.0 Development Plan](./v1.0-development-plan.md): Project-Ready GameDesignOS 的开发计划、门禁、验收标准和 rollback。
- [Roadmap](./roadmap.md): the path from Runtime Foundation to a project-ready operating system with explicit RJR-AI authority boundaries.

## Product Test

GameDesignOS should help a designer:

1. preserve evidence and assumptions;
2. route work to the smallest suitable skill;
3. save outputs as durable project assets;
4. make human decisions with explicit risks and rollback conditions;
5. retain what the project learned across iterations.

If a feature produces more text but does not improve one of these five outcomes, it is not automatically a GameDesignOS feature.
