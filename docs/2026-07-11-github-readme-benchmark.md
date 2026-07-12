# GameDesignOS GitHub 首页对标记录（2026-07-11）

## 决策问题

如何让第一次进入仓库的读者在 5 秒内理解 GameDesignOS 的价值，并在 30 秒内找到可信 proof 与最短启动路径？

## 公开样本

| 项目 | 2026-07-11 页面可见 stars | 首屏做法 | 可迁移模式 |
| --- | ---: | --- | --- |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 104k | 极短定位、视觉 demo、任务案例、随后进入 Quickstart | 先展示“能完成什么”，再解释技术结构 |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 80.4k | 一句产品定义、兼容对象、状态 badge、主视觉 proof | 一句话承诺与产品截图/主视觉紧邻 |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 68.8k | 鲜明心智模型、输入输出承诺、快速安装 | 用一个可复述模型代替功能清单 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 59.6k | 一句定义、明确状态、立即安装与 Hello World | 状态边界必须比营销承诺更醒目 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 55.3k | 清晰主张、两类核心原语、社区 proof、Getting Started | 首屏只保留最重要的两三个结构概念 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 37k | 极简一句话、可信采用者、单行安装、Why 列表 | 先给承诺与安装，再展开架构 |

Stars 只用于确认这些 README 经历过大规模公开访问，不代表设计质量的因果证明。

## GameDesignOS 当前问题

1. 首屏先解释版本、资产数量和内部术语，用户结果出现得太晚。
2. CTA 数量过多，第一次访问者不知道应先看 Quick Start、Skill、Runtime 还是 Case。
3. 旧主视觉同时承载标题、版本、模块、流程和多个仪表盘，小尺寸下信息竞争严重。
4. “AI 游戏设计 OS”范围太宽，缺少可复述的独占承诺。

## 本轮迁移

- 核心承诺：**Turn AI output into game design decisions you can verify.**
- 中文承诺：**把 AI 输出变成可验证的游戏设计决策。**
- 首屏顺序：主视觉 → 一句话承诺 → 边界说明 → 4 个主链接 → 可信 badge → 转化链 → Quick Start。
- 新视觉只表达一个关系：碎片化 AI 输出 → 决策核心 → 可审计项目资产。
- GitHub About 描述聚焦 `reviewable decisions + contracts + Human Gates + rollback`。

## 不迁移的做法

- 不复制其他项目的品牌图形、配色、文案或截图。
- 不使用未经证明的“production standard”“trusted by”或用户规模声明。
- 不把 stars、模块数量或版本号当成核心价值。
- 不为了更像热门仓库而隐藏 local-first、Human Gate、public/private boundary 与 rollback。

## 后续观察指标

- README 首屏到 Quick Start 的滚动距离；
- Quick Start 是否无需阅读架构章节即可理解；
- issue / discussion 中“这个项目到底做什么”的重复提问是否下降；
- GitHub traffic 中 README 到案例、工作流和安装入口的点击是否提升；
- 新用户能否准确复述“AI 输出 → 可验证决策”。
