# Mindmap and Existing Proposal Input

本 reference 用于三类输入：一句话创意接续成案、脑图/xmind/系统设计图转策划案、已有策划案审核改进。

## 联网调研吸收点

| 来源 | 吸收规则 |
| --- | --- |
| Xmind 官方说明：支持导出 PNG、SVG、PDF、Excel、Word、OPML、TextBundle、PowerPoint、Markdown 等格式 | 如果用户提供 `.xmind` 难以直接解析，可要求或优先使用 Markdown、Word、Excel、OPML、PDF/PNG 导出；若文件可读，先保留层级再成案。 |
| Xmind 官方功能页：支持导入/导出 Markdown、OPML、Word、Excel、PowerPoint 等 | 脑图可以作为结构输入，但不是最终策划案；需要转成可执行文档结构。 |
| Unity Learn GDD 教程：GDD 用于记录设计决策、沟通愿景、指导开发 | 评审文档必须服务沟通和开发，不应只是设定堆叠或静态大纲。 |

## 一句话创意接续成案

当用户只有一句话创意，但目标是策划案：

1. 先调用 `game-concept-architect`。
2. 生成并提取：concept brief、player-promise-contract、core loop、scope gate、validation plan。
3. 再由本 skill 选择输出模式。
4. 在成案中标记：
   - `source_status: generated_this_turn`
   - `evidence_status: assumption`
   - `missing_external_evidence`
   - `next_validation_needed`

禁止直接把一句话扩写成完整世界观、系统表和商业承诺。

## 脑图 / xmind 读取规则

优先输入顺序：

1. Markdown / OPML / Word / Excel 导出。
2. 可解包的 `.xmind` 文件。
3. PDF / PNG / SVG 脑图截图。
4. 用户粘贴的文本层级。

处理 `.xmind` 时：

- 先判断是否能作为 ZIP 读取。
- 新版常见内容可能在 `content.json`，旧版可能在 `content.xml`。
- 如果有多 sheet，先列 sheet，再判断哪一个是主设计树。
- 保留 topic 层级、notes、markers、labels、relationships、attachments 的可见信息。
- 如果文件加密、损坏或只有图片，输出 `access_notes`，不要假装完整读取。

## 脑图到策划案的转换

先生成 `Mindmap Structure Inventory`：

| 层级 | 节点 | 可能含义 | 转换动作 |
| --- | --- | --- | --- |
| L1 | 主题/玩法/系统 | 文档章节或设计支柱 | 保留为 proposal spine 或章节 |
| L2 | 模块/循环/资源 | 系统责任或玩家行为 | 转成核心循环、资源流、scope |
| L3+ | 功能/规则/数值/内容 | 实现项或假设 | 分入 MVP / VS / Demo / Release / Cut |
| 关系线 | 依赖/冲突/互斥 | 风险或顺序 | 转成里程碑依赖和风险项 |
| 标记/优先级 | 星标/进度/负责人 | 已有项目管理信号 | 转成 owner、status、decision needed |

再生成 `Implementation Translation`：

- 玩家动词：节点背后的玩家行为是什么。
- 系统责任：每个系统到底改变什么状态。
- 资源流：产出、消耗、库存、门槛和反馈。
- Scope gate：哪些属于 MVP、Vertical Slice、Demo、Release、Post-launch、Cut。
- 验证项：每个关键假设怎么证明。
- 砍项理由：为什么某些节点暂不做。

## 已有策划案审核流程

先 review，后 rewrite。

### Review 维度

| 维度 | 检查问题 |
| --- | --- |
| 读者匹配 | 是给老板、制作人、发行、投资人、团队，还是自己整理？ |
| 决策请求 | 读完后需要批准什么、拒绝什么、投入什么？ |
| 玩家承诺 | 玩家为什么反复玩，是否在前 20% 出现？ |
| 核心循环 | 是否能独立读懂，而不是靠功能列表猜？ |
| 证据边界 | 哪些是事实、提供信息、推断、assumption、unknown？ |
| Scope | MVP/VS/Demo/Release 是否混成一团？ |
| 生产可行性 | 团队、周期、预算、工具链是否支撑内容承诺？ |
| 风险 | 风险是否有信号、缓解、验证和 owner？ |
| 外部 pitch | 是否有 proof of play、目标匹配、ask、budget、timeline？ |

### 改写要求

- 先写 `Revision Plan`，再写改写版。
- 保留原案中可用的玩家承诺、核心循环、证据和已经批准的限制。
- 删除或降级无法证明的大 scope、市场断言、收入承诺、愿望单承诺、发行兴趣承诺。
- 输出 `Change Log`：保留、重写、删除、待补证据。

## 输出块

脑图输入时追加：

```markdown
## Mindmap Structure Inventory
## Implementation Translation
## Scope Conversion
## Dependency and Risk Notes
```

已有策划案审核时追加：

```markdown
## Review Target
## Reader and Decision Fit
## Structure Diagnosis
## Evidence and Assumption Problems
## Scope and Production Risks
## Missing Proof / Missing Decisions
## Revision Plan
## Suggested Rewrite
## Change Log
## Remaining Unknowns
```
