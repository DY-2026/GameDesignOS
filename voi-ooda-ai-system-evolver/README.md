# Paranoia Skill

> 一个面向 **AI 系统持续进化** 的实战型方法论仓库：用 **VOI + OODA + Evals + Human Gate + Rollback**，让你的系统“会变强”，但不“失控变异”。

## 1. 项目定位

**Paranoia Skill**（原 VOI-OODA AI System Evolver）是一个可落地的“系统进化操作系统”，用于升级你的：

- Prompt 设计
- Agent Workflow
- 记忆系统（Memory）
- 检索增强（RAG）
- Tool Routing
- 结构化 Schema
- Evals 与发布门禁

它不是训练新模型，而是把“AI 变好”变成可验证、可回滚、可审计的工程过程。

---

## 2. 核心价值

### 2.1 为什么不是“多试几次提示词”

大多数团队会在问题出现时“临时补丁”：改一段 prompt、加一条规则、换一个模型，然后祈祷别出回归。

Paranoia Skill 提供的不是补丁，而是**受控进化闭环**：

1. **VOI（Value of Information）**：先判断是否值得继续搜集信息。
2. **OODA**：持续 Observe / Orient / Decide / Act，避免盲动。
3. **Evals**：所有改动先过评测，再决定留不留。
4. **Human Gate**：高风险动作必须人工确认。
5. **Rollback**：任何升级都能快速撤回。

### 2.2 适合谁

- AI 产品团队（Agent、Copilot、自动化工作流）
- 提示词工程师 / AI 应用工程师
- 需要稳定上线与合规审计的企业团队

---

## 3. 仓库结构

```text
agents/openai.yaml                 # Agent 展示信息与默认调用提示
references/evolution-loop-playbook.md
references/eval-versioning-playbook.md
templates/evolution_proposal.md    # 进化提案模板
templates/ooda_voi_state.md        # OODA+VOI 状态模板
SKILL.md                           # 技能入口说明
```

---

## 4. 方法论亮点（可对外传播）

- **先算信息价值，再行动**：减少无效检索、无效实验。
- **任务 OODA + 元 OODA 双循环**：今天解决问题，明天升级系统。
- **候选态（candidate）机制**：避免一次“偶然有效”污染全局策略。
- **评测驱动版本化**：让“升级”变成有证据的发布行为。

---

## 5. 图片生成介绍（用于对外发布）

Paranoia Skill 同时适合生成项目传播用视觉素材（封面图、流程图草图、宣传配图）的提示词与工作流编排。

### 5.1 可生成的视觉内容

- **项目封面图**：如「AI 指挥舱 / OODA 战情室」风格主视觉
- **流程海报**：VOI → OODA → Evals → Human Gate → Rollback
- **社媒配图**：发布更新日志、版本迭代、评测结果
- **演示图说明**：把复杂架构转换为可读的视觉说明

### 5.2 推荐图片生成流程

1. 在 OODA 的 **Orient** 阶段先定义视觉目标（品牌风格、受众、渠道）。
2. 用 VOI 判断是否需要补充素材信息（竞品视觉、品牌色、尺寸规范）。
3. 先生成 **candidate 图片**，不要直接用作最终发布。
4. 用评估清单检查：可读性、准确性、版权风险、品牌一致性。
5. 通过 Human Gate 后再进入正式发布资产库。

### 5.3 对外话术建议

你可以这样描述：

> “Paranoia Skill 不只帮助 AI 系统做决策进化，也能把复杂方法论转换成可传播的视觉资产，并通过评测与人工门禁确保素材质量与一致性。”

---

## 6. 快速开始

1. 阅读 `SKILL.md` 了解原则与输出要求。
2. 使用 `templates/evolution_proposal.md` 提交一次候选改动。
3. 使用 `templates/ooda_voi_state.md` 跑一轮短 OODA。
4. 参考 `references/*` 建立你自己的评测与版本门禁。

---

## 7. 发布级承诺

Paranoia Skill 强调以下发布标准：

- 变更前有假设，变更后有证据。
- 高风险能力有人类审批。
- 所有关键规则可版本化、可追溯、可回滚。

这让它非常适合作为企业级 AI 系统治理与持续优化的公开项目基础。
