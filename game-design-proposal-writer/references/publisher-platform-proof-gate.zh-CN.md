# Publisher and Platform Proof Gate

本 reference 用于 `publisher_pitch_outline`、Steam/平台导向独游设计案、立项融资稿和对外 pitch。它把“看起来专业”改成“能被外部读者判断、追问和继续推进”。

## 使用前提

正式投递前必须重新检查目标发行方、平台或孵化器的当前页面。下面的公开来源只作为 2026-06-09 调研得到的样例证据，不是永久规则。

| 来源 | 这次吸收的方法 |
| --- | --- |
| Devolver Digital pitch form: https://pitch.devolverdigital.com/ | 需要 quick pitch、gameplay video、pitch deck URL；deck 应包含 demo 链接、financial roadmap 和向发行方请求什么。 |
| Akupara Games pitch page: https://www.akuparagames.com/pitch-a-game/ | 要 pitch deck、playable build、gameplay video；还要 overview、公司/团队介绍、理想合作方式、预算、目标平台、预计档期和 engine。 |
| Finji pitch page: https://finji.co/pitches.html | 发行方可能当前不签新项目，也可能只少量签约；pitch 需要先确认对方是否仍开放、是否符合 portfolio/timing。 |
| GDC / GFR Fund fundraising deck notes: https://media.gdcvault.com/gdcsummer2020/presentations/Tsutsui-Teppei-Skill-Building%20Series-How%20Game%20Studios%20Should%20Plan%20Fundraising%20-%20Learning%20Best%20Practices.pdf | deck 先有 narrative，正文保持简洁，更多视觉少文字；常见内容包括 team、previous titles、new game/product、why now、traction、monetization、competition、roadmap 和 round/ask。 |
| Steamworks store page docs: https://partner.steamgames.com/doc/store/page | Store page 要准备 description、trailer、screenshots 等必要项；发布 store page 会把素材放到公开服务器，未公布项目也可能被抓取或传播。 |
| Steamworks trailer docs: https://partner.steamgames.com/doc/store/trailer | trailer 需要分类；前两个有效 trailer 会排在 screenshots 前；microtrailer 来自商店页第一个可见视频。 |

## 六个证明门

### 1. 发行方匹配门

输出必须说明：

- 目标发行方/投资方/平台为什么可能适配这个项目。
- 对方 portfolio、偏好、档期、平台能力或服务能力与项目需求的对应关系。
- 当前是否开放收项目：`verified_current` / `needs_recheck` / `unknown`。
- 不适配的反例：至少写一个“不该投给谁/为什么”。

### 2. Proof of Play 门

对外 pitch 不应只靠概念图或世界观。至少列出：

- playable build / prototype / vertical slice / demo 的状态。
- gameplay video 或 GIF 的状态。
- 玩家反馈、试玩记录、愿望单、社区反馈、活动反馈或指标的状态。
- 没有 proof 时，明确写成 `missing`，并把下一步变成 proof-building plan。

### 3. Ask and Budget 门

外部读者需要知道“你到底要什么”。必须写清：

- ask 类型：funding、publishing、marketing、QA、localization、porting、platform featuring、feedback、partnership。
- 预算或资源请求是否有依据。
- 时间线是否支持预算请求。
- 若预算是空的，写 `budget model missing`，不要编数字。

### 4. Build Scope 门

pitch 中的 demo / vertical slice 必须证明项目独特性，而不是复刻正式版范围。

必须区分：

- `shown_now`: pitch/deck/video 已经能看到什么。
- `must_prove_next`: 下一阶段必须证明什么。
- `not_in_scope`: 这次不做什么。
- `later_release_scope`: 正式版才考虑什么。

### 5. Steam / Store Visibility 门

面向 Steam 或 PC 买断项目时，加入平台可见面检查：

- store-page promise 是否能在截图、trailer、capsule、tags 或 demo 中被看见。
- 第一个 trailer / video 是否能证明玩法，而不是只给氛围。
- screenshots 是否覆盖不同系统、场景或关键反馈。
- 发布 store page 是否会暴露未公开信息；如项目保密，先写 `publication_risk`。

### 6. Meeting Readiness 门

pitch 不是把 deck 读完。输出中要准备：

- 30 秒口头版：项目是什么、为什么现在、玩家做什么、你要什么。
- 5 分钟版：核心体验、证明材料、制作计划、风险和请求。
- 追问清单：预算、roadmap、team capacity、market evidence、platform plan、scope cut、IP/素材/AI 使用边界。

## 输出追加块

涉及发行、投资、平台、Steam 或孵化器时，在常规模板后追加：

```markdown
## Publisher / Platform Fit

| target | fit reason | current status | mismatch risk |
| --- | --- | --- | --- |

## Proof of Play

| proof item | current status | next action |
| --- | --- | --- |

## Ask, Budget, and Timeline

| ask | evidence | unknown / risk |
| --- | --- | --- |

## Submission Readiness

| material | status | owner | blocker |
| --- | --- | --- | --- |

## Recheck Before Submission

- target page / form:
- checked date:
- changed requirements:
- decision:
```

## 禁止过度承诺

- 不得写“发行一定感兴趣”“愿望单会增长”“Steam 算法会推荐”。
- 不得把未打开过的发行方页面写成当前开放。
- 不得用“预算合理”替代预算模型。
- 不得把 AI 生成的概念图当作 proof of play。
- 不得把 pitch deck 当成完整 GDD；deck 只服务外部判断，详细设计应放 appendix 或独立文档。
