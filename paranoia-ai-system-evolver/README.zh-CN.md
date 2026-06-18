# Paranoia AI System Evolver

**所属项目:** [GameDesignOS by Paranoia](../README.zh-CN.md)

**语言:** [简体中文](./README.zh-CN.md) | [English](./README.en.md)

> Copyright (c) 2026 Paranoia. Licensed under the MIT License.

这是 `GameDesignOS` 里的受控系统演化 skill。它负责升级 prompt、memory、RAG、tool routing、workflow、schema、eval 与 skill，同时用 VOI 决策门阻止 FOMO 调研、AI 分支爆炸和高结构低价值输出。

## 这个 Skill 做什么

它组合了：

- WOOP harness protocol：把任务目标、验收、失败模式和 if-then 恢复协议写进控制面；
- VOI 决策门：先定义决策、选项、默认行动和决策边界，再判断哪些信息值得获取；
- EVPI / EVPPI / EVSI：区分完全信息上界、目标不确定性和具体样本/实验的价值；
- 模型压缩与因果中介：用更短、可干预、可验证的 operating model 替代补丁堆积；
- Orient-first OODA：用现实反馈刷新地图，而不是追求反应速度；
- Evals、Human Gate、versioning 与 rollback：让候选改动可验证、可审批、可逆。

## VOI 的新增硬规则

```text
没有决策对象，不启动无限调研。
没有 current_default_action，不能计算行动变化。
所有合理信号都不改变行动，当前决策 VOI 接近于零。
EVPI 是价值上界，EVSI 是具体样本或实验的价值。
净 VOI 必须扣除获取、延迟、注意力、隐私和污染成本。
达到停止条件就拍板，不用更多研究替代行动。
```

## 包内容

```text
SKILL.md
agents/openai.yaml
references/value-of-information-playbook.md
references/value-of-information-playbook.zh-CN.md
references/value-of-information-playbook.en.md
references/evolution-loop-playbook.md
references/evolution-loop-playbook.zh-CN.md
references/evolution-loop-playbook.en.md
references/woop-harness-protocol.md
references/woop-harness-protocol.zh-CN.md
references/woop-harness-protocol.en.md
references/model-compression-playbook.md
references/model-compression-playbook.zh-CN.md
references/model-compression-playbook.en.md
references/eval-versioning-playbook.md
references/eval-versioning-playbook.zh-CN.md
references/eval-versioning-playbook.en.md
templates/voi_decision_gate.md
templates/voi_decision_gate.zh-CN.md
templates/voi_decision_gate.en.md
templates/evolution_proposal.md
templates/evolution_proposal.zh-CN.md
templates/evolution_proposal.en.md
templates/ooda_voi_state.md
templates/ooda_voi_state.zh-CN.md
templates/ooda_voi_state.en.md
evals/voi-decision-gate-cases.md
evals/voi-decision-gate-cases.en.md
quick_validate.py
```

## 推荐提示词

```text
使用 $paranoia-ai-system-evolver，先写出当前决策、选项、默认行动和决策边界，再用 VOI/EVPI/EVSI 判断哪些搜索、追问、日志、实验或 AI 分支值得做。把最终系统改动整理成带 WOOP、OODA、eval、Human Gate 和 rollback 的候选提案。
```

## 在 GameDesignOS 里的边界

- 领域 skill 仍负责概念、体验诊断、ED 实验和策划案；本 skill 负责系统改动与显式 VOI 审计。
- VOI 不把所有学习都判为无用，而是区分 `decision_information`、`model_learning` 和 `information_consumption`。
- 高风险概率、损益、资金和生产判断不能只靠高/中/低启发式。
- 真实项目材料、私有数据和客户信息留在 private workspace。

## 维护规则

- `SKILL.md` 保持轻量，完整方法放在 `references/`。
- 改动后运行 `python scripts/validate_skill.py paranoia-ai-system-evolver` 与 `python paranoia-ai-system-evolver/quick_validate.py paranoia-ai-system-evolver`。
- `target_layer: skill` 必须运行行为回归，检查是否减少低 VOI 分支且没有增加无意义前置文本。
- 全局安装、长期记忆写入、生产发布和长期规则提升都属于 Human Gate。
