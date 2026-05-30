# 模型压缩 Playbook

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

此文件为默认中文版本。英文版见 `model-compression-playbook.en.md`，简体中文版见 `model-compression-playbook.zh-CN.md`。

升级 AI 系统时，先问：这个系统到底在按什么模型工作？

好的 prompt、skill、agent、workflow 或 harness，不是把场景流程写得越来越长，而是把一类任务压缩成可复用、可组合、可验证的操作模型。

## 核心准则

```text
更短的核心描述
+ 更少的例外补丁
+ 更清楚的中介变量
+ 更可执行的控制点
+ 更可靠的验证和恢复
```

## 总描述成本

```text
model_score = core_model_length
            + data_patch_length
            + routing_rule_length
            + state_injection_length
            + validation_observation_length
            + exception_patch_length
            + failure_recovery_length
```

升级目标是让总描述成本下降，同时不牺牲关键结果质量。

## 因果中介

不要只写：

```text
input -> final_output
```

要写：

```text
input -> mediator_1 -> mediator_2 -> final_output
```

中介变量必须尽量可诊断、可干预、可验证。不能说清楚优化了哪个中介变量的改动，通常只是风格偏好，不应直接进入长期系统。

## 动词优先

优先按“信息如何被变换”建模，而不是按“这是什么场景”建模。

好的 skill 像游戏机制：可重复调用、可组合、可涌现。坏的 skill 像关卡脚本：服务特定场景，失败后只能继续补丁。

## 详细版本

完整流程、表格和输出格式见：

- `references/model-compression-playbook.zh-CN.md`
- `references/model-compression-playbook.en.md`
