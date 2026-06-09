# Proposal Intake Router

本 reference 用于判断用户真正需要哪一种策划案，而不是默认输出一份臃肿 GDD。

## 先判断读者

策划案不是写给所有人的。读者决定章节密度、证据要求和语言风格。

| 读者 | 他们真正关心 | 文档重点 |
| --- | --- | --- |
| 老板/管理层 | 为什么值得投入，风险是否可控 | 一句话定位、机会、成本、里程碑、Go/No-Go |
| 制作人 | 能不能做，先做什么，怎么验证 | 核心循环、scope、团队资源、排期、风险 |
| 主策/系统策划 | 设计是否自洽，系统是否回连循环 | 玩家动词、核心循环、关键系统、验证标准 |
| 发行/投资人 | 卖点是否清晰，demo 能否证明，团队是否可信 | pitch、目标玩家、差异化、证明材料、请求 |
| 独立团队成员 | 要做什么，不做什么，为什么这样做 | 创作命题、设计支柱、vertical slice、制作边界 |
| 自己整理 | 方向是否清楚，下一步怎么走 | assumption、scope、风险、下一步动作 |

## 再判断文档场景

| 用户请求 | 默认模式 | 不要输出 |
| --- | --- | --- |
| 一句话创意 + 写策划案 / 立项案 / pitch | `game-concept-architect` -> `commercial_product_proposal` / `indie_design_dossier` | 直接把一句话扩写成完整案，不标注 assumption |
| 商业游戏策划案 / 产品方案 / 立项案 | `commercial_product_proposal` | 纯世界观设定集、没有商业和生产边界的长 GDD |
| 独游设计案 / Steam 方案 / 小团队 GDD | `indie_design_dossier` | 套用手游商业化模板、承诺大内容量 |
| 老板只看一页 / 会前判断 | `one_page_decision_memo` | 章节齐全但结论淹没的方案 |
| 给发行 / 投资人 / 孵化器 | `publisher_pitch_outline` | 内部系统细节过多、没有 demo proof |
| 做 Demo / first playable / vertical slice | `vertical_slice_design_doc` | 正式版完整功能规划 |
| xmind / 脑图 / 玩法系统图 / 系统设计大纲 -> 策划案 | 根据读者选择成案模式，并追加 mindmap structure inventory | 把节点顺序原样贴成正文 |
| 审核 / 改进 / 重写已有策划案或 GDD | `proposal_review_and_rewrite` | 只润色语言，不处理证据、scope 和决策问题 |

## 输入材料分级

| 材料状态 | 处理方式 |
| --- | --- |
| 只有一句话创意，且只是判断方向 | 先用 `game-concept-architect`，不直接写策划案 |
| 只有一句话创意，但明确要策划案 | 自动先走 `game-concept-architect`，再由本 skill 成案 |
| 有 concept brief / player promise | 可以写 proposal spine，但生产和商业仍需 assumption ledger |
| 有 xmind / 脑图 / OPML / Markdown 大纲 / 系统图 | 先做结构清点，再转成 scope、里程碑、验证项和风险 |
| 有已有策划案 / GDD / pitch | 先做 review 和 revision plan，再按需改写 |
| 有竞品调研 / source notes | 可以建立 reference boundary 和 evidence ledger |
| 有录屏 / issue cards / ED handoff | 可以把真实体验问题写进风险和验证计划 |
| 有团队/预算/周期 | 可以写较具体的 milestone gate |
| 有发行/投资目标 | 使用外部读者语言，减少内部术语 |
| 有 playable build / demo / gameplay video | 可以写 proof of play；若没有，只能写 proof-building plan |
| 有目标发行方/平台 | 读取 `publisher-platform-proof-gate.zh-CN.md`，检查 fit、ask、预算、素材和投递前 recheck |

## 三个优先澄清问题

只有当答案会改变文档方向时才问。最多问三个。

1. 这份文档给谁看？内部老板/制作人/发行/投资人/团队/自己？
2. 目标平台和商业模式是否已定？
3. 团队规模、周期、预算或当前阶段是什么？

用户要求继续时，不要卡住。用 `assumption draft` 继续推进。
