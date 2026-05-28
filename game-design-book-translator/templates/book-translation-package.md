Copyright (c) 2026 @Paranoia. All rights reserved.

# Book Translation Package Template

用于整本书、连续章节或需要长期维护的游戏设计翻译项目。

## 推荐目录

```text
translated-book/
  README.md
  source_manifest.md
  00-术语表.md
  01-前言与目录.md
  02-Chapter-1-title.md
  03-Chapter-2-title.md
  audit/
    审校记录.md
  assets/
    fig-1-1.png
    fig-1-2.png
```

## README.md

```md
# 书名中文工作名

原名：Original Title
作者：Author Name
状态：术语表 / 第 1 章 / 图像回填 / 审校中
使用边界：个人学习 / 内部研究 / 公开文章草稿 / 待确认授权

## 交付范围

- 已翻译章节：
- 待处理章节：
- 图片处理状态：
- 术语表状态：
- 待确认授权或来源：

## 翻译原则

- 术语先统一，再翻正文。
- 游戏名、书名、作者名、产品名优先保留英文原名。
- 图注、表头、流程图标签纳入翻译范围。
- 关键英文原句只少量行内保留。
```

## source_manifest.md

```md
# 来源清单

| 项目 | 内容 |
| --- | --- |
| 原书/文章 |  |
| 作者 |  |
| 版本/年份 |  |
| 来源文件/URL |  |
| 处理方式 | PDF / OCR / Markdown / 图片 |
| 传播边界 | 个人学习 / 内部研究 / 公开前需确认授权 |

## 待确认

- [ ] 页码或章节来源是否完整：
- [ ] 图片来源是否完整：
- [ ] 是否允许公开传播：
```

## 00-术语表.md

```md
# 术语表

| English | 中文译法 | 语境/说明 | 状态 |
| --- | --- | --- | --- |
| core loop | 核心循环 | 指反复驱动玩家行动的循环。 | confirmed |
| agency | 主体能动性 | Game Studies 语境慎用“自由度”。 | tentative |
| feedback loop | 反馈循环 | 系统设计语境。 | confirmed |
```

## Chapter 文件

```md
# Chapter 1 中文标题

> 原标题：Original Chapter Title

## 小节标题

中文正文。必要时调整语序、拆分长句，让论证关系符合中文阅读习惯。

如果某句确实值得保留英文，可写成：“中文译句（original English）。”

图 1.1：中文图注。

![图 1.1 中文化说明](assets/fig-1-1.png)

图示说明：说明这张图在本节论证中的作用。
```

## audit/审校记录.md

```md
# 审校记录

## 本轮检查

- 术语一致性：
- 图注/表格完整性：
- 专有名词：
- 英文原句保留比例：
- 中文可读性：
- 来源与授权边界：

## 待回填

- [ ] 缺图：
- [ ] 待确认术语：
- [ ] 需要原文复核：
- [ ] 需要授权确认：
```
