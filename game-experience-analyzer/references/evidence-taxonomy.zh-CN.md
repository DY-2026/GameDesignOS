# Evidence Taxonomy / 证据索引与事件分类

诊断报告里的重要判断必须引用 `evidence_id`。没有证据的内容只能写为假设、未知或验证项，不能伪装成观察事实。

## Evidence Index 字段定义

| 字段 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- |
| `evidence_id` | 是 | 全局唯一，格式建议 `E001`、`E002`。一个报告内不可重复。 | `E014` |
| `source_id` | 是 | 原始材料编号。 | `video_01`、`screenshot_03`、`steam_page` |
| `source_type` | 是 | `screenshot` / `video_file` / `video_url` / `trailer_pv` / `paid_creative` / `store_page` / `user_context` | `trailer_pv` |
| `timestamp` | 条件必填 | 视频材料的时间点；截图或页面可为 `null`。 | `00:00:06.200` |
| `time_range` | 否 | 连续事件的范围。 | `00:00:05-00:00:11` |
| `frame_id` | 否 | 抽帧编号或关键帧编号。 | `F012` |
| `image_id` | 条件必填 | 截图编号。 | `IMG_02` |
| `region` | 是 | 画面区域或页面区块。 | `top-right HUD`、`hero section` |
| `visible_text` | 否 | 可见 UI/字幕/页面文案。只记录会改变判断的文本。 | `Claim reward` |
| `observed_fact` | 是 | 只写可观察事实，不写推断。 | `玩家点击胜利结算后立即出现双倍奖励按钮` |
| `event_type` | 是 | 使用下方 taxonomy。 | `reward_claim` |
| `supports_judgment` | 是 | 该证据支撑哪个判断或问题卡。 | `商业化打断发生在首轮胜利反馈之前` |
| `confidence` | 是 | `0.0-1.0` 数字。低于 `0.6` 必须写不确定原因。 | `0.82` |
| `uncertainty_note` | 条件必填 | 遮挡、低清、链接不可访问、样本不足等。 | `字幕遮挡，按钮文案只能部分识别` |
| `extraction_method` | 否 | `direct_observation` / `frame_sample` / `ocr` / `page_metadata` / `user_provided` | `frame_sample` |

## 事件类型 Taxonomy

| `event_type` | 定义 | 典型证据 | 常见误用 |
| --- | --- | --- | --- |
| `hook_peak` | 最强吸引点、冲突点、奇观或玩法承诺出现。 | PV 第 2 秒出现巨大敌人和可控角色对峙。 | 把任何漂亮画面都当 hook。 |
| `feature_exposure` | 功能入口被看见，但未必解锁或使用。 | 主界面出现 `Guild` 按钮。 | 看到按钮就说已解锁。 |
| `feature_unlock` | 系统明确开放或提示解锁。 | 弹窗写 `Arena unlocked`。 | 把红点或灰按钮当解锁。 |
| `first_use` | 玩家首次实际使用某功能。 | 第一次进入抽卡界面并完成抽取。 | 只看见教程箭头就算首用。 |
| `reward_claim` | 玩家领取或被发放奖励。 | 点击领取金币、结算发放装备。 | 把奖励预览当领取。 |
| `failure_signal` | 失败、受挫、卡关、死亡、资源不足等信号出现。 | 战斗失败、按钮提示 `Not enough energy`。 | 把高难敌人展示都当失败。 |
| `confusion_signal` | 玩家可能不知道目标、路径或规则。 | 长时间停留、来回点错、多个入口无主次。 | 只因 UI 复杂就断言玩家困惑。 |
| `monetization_prompt` | 付费、广告、礼包、订阅、首充等请求出现。 | `Watch Ad x2`、`Starter Pack` 弹窗。 | 把普通商店入口都当强打断。 |
| `decision_point` | 玩家需要做有意义选择。 | 三选一奖励、路线分支、Build 取舍。 | 把确认按钮当决策。 |
| `shareable_moment` | 可截图、可复述、可二创、可争议传播的片段。 | 一句反差文案、强梗角色、奇观 Boss。 | 把普通过场都当传播点。 |
| `control_release` | 玩家获得自由操作窗口。 | 教程结束后可移动/战斗/探索。 | 把自动寻路阶段当自由控制。 |
| `loop_closure` | 核心动作到反馈、奖励、成长或下一轮目标形成闭环。 | 战斗 -> 掉落 -> 升级 -> 新关卡。 | 只看到战斗和奖励就说闭环，无下一轮目标。 |
| `access_blocked` | 链接、平台、权限、地区或工具导致内容不可读。 | 403、登录墙、视频下架、无法播放。 | 编造无法访问视频的时间轴。 |

## 置信度规则

| 范围 | 标签 | 使用规则 |
| --- | --- | --- |
| `0.85-1.0` | `high` | 画面、文案、时间点清楚，判断直接来自证据。 |
| `0.65-0.84` | `medium` | 证据清楚但需要轻微推断，或样本范围有限。 |
| `0.40-0.64` | `low` | 只能做弱判断，必须写 `uncertainty_note`。 |
| `<0.40` | `unsupported` | 不作为结论，只能进入 `key_unknowns` 或 `validation_plan`。 |

## 最小示例

```json
{
  "evidence_id": "E003",
  "source_id": "video_01",
  "source_type": "video_file",
  "timestamp": "00:07:18",
  "time_range": "00:07:12-00:07:25",
  "frame_id": "F128",
  "image_id": null,
  "region": "center modal",
  "visible_text": "Watch Ad x2",
  "observed_fact": "首轮胜利结算后，双倍奖励广告按钮位于默认视觉焦点。",
  "event_type": "monetization_prompt",
  "supports_judgment": "商业化请求早于玩家理解长期目标，可能打断首轮成就反馈。",
  "confidence": 0.88,
  "uncertainty_note": "",
  "extraction_method": "frame_sample"
}
```
