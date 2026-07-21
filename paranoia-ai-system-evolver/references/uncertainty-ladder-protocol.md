# UL（Uncertainty Ladder，不确定性阶梯）工程协议

> Copyright (c) 2026 @Paranoia. All rights reserved.

本文件的完整中文主说明见 `references/uncertainty-ladder-protocol.zh-CN.md`。默认执行、字段定义、六阶段 gate、失败归因、迁移验证与 Human Gate 均以该中文主文件为准。

```text
建立模型 -> 拆分动作 -> 受控组合 -> 暴露失败 -> 诊断瓶颈
-> 针对训练 -> 增加复杂度 -> 迁移验证 -> 更新模型
```

核心约束：VOI 选择最值得消除的未知；UL 每轮只释放少量主要未知；OODA 执行单轮；Eval 判断能否升级；RJR-AI 与 Human Gate 限制权限和真实后果。机器状态对象统一为 `ul_state`，阶段统一为 `UL-L0`～`UL-L5`。若失败无法归因，状态必须是 `confounded` 并退回更受控环境，不得继续叠加长期规则。
