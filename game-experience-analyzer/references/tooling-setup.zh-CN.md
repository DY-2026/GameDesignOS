# 工具检查、安装配置与降级策略

这个 skill 支持截图、本地录屏、视频链接三类来源。不同来源需要的工具不同。先检查工具，再决定完整分析还是降级分析。

## 工具分层

| 层级 | 工具/能力 | 用途 | 缺失时怎么降级 |
| --- | --- | --- | --- |
| 必需 | 图片查看/多模态识别 | 分析截图、封面、关键帧 | 无法看图时要求用户直接上传截图到当前对话 |
| 推荐 | `ffmpeg` | 本地录屏抽帧、按时间点取证 | 只能做元数据/封面/用户手动截图分析 |
| 推荐 | 浏览器访问 | 打开视频链接，确认页面、标题、封面、登录/权限限制 | 记录 `access_notes`，要求用户提供截图或本地录屏 |
| 推荐 | `yt-dlp` 或平台元数据接口 | 获取公开视频信息、可用流、字幕或下载片段 | 只做页面可见证据和封面弱诊断 |
| 可选 | OCR | 读取 UI 文案、按钮、奖励、弹窗 | 手动转写关键文案 |
| 可选 | ASR/字幕工具 | 提取解说、旁白、教程语音 | 只分析画面证据，语音判断标 `uncertain` |

## Windows 快速检查

```powershell
Get-Command ffmpeg -ErrorAction SilentlyContinue
Get-Command yt-dlp -ErrorAction SilentlyContinue
Get-Command python -ErrorAction SilentlyContinue
```

如果工具不存在，不要直接失败。先说明缺失工具会影响哪些结论，然后给安装引导。

## 安装建议

### ffmpeg

优先使用系统包管理器或可信发行包：

```powershell
winget install Gyan.FFmpeg
```

如果没有 `winget`，去 ffmpeg 官方网站或可信 Windows build 下载，解压后把 `bin` 目录加入 `PATH`。

### yt-dlp

适合公开视频链接。需要 Python 时：

```powershell
python -m pip install --user yt-dlp
```

也可以使用 `yt-dlp` 官方 release 的单文件程序，并把所在目录加入 `PATH`。

注意：不要用工具绕过登录、付费、地区、版权或平台权限限制。不可访问时记录限制并请求用户补充素材。

### OCR

轻量场景可以人工读图；需要批量处理时再安装：

- Tesseract OCR
- PaddleOCR
- 平台自带 OCR 或多模态识别能力

OCR 结果必须抽查。小字号、特效字、弹窗遮挡和竖屏压缩会导致误读。

### ASR / 字幕

如果视频有字幕，优先用字幕。没有字幕但语音会影响判断时，可使用 Whisper、剪映字幕、本地 ASR 或平台字幕导出。

没有 ASR 时，报告要写明“未分析语音/解说层”，不要把听不见的内容当事实。

## 视频链接处理流程

1. 打开链接，记录 `url`、访问日期、标题、作者、时长、封面、平台限制。
2. 如果平台有公开元数据接口，先取元数据，不直接下载整片。
3. 如果可合法访问播放流，用 `ffmpeg` 抽关键帧。长视频先抽样，不全量处理。
4. 如果平台限制访问，保留 `access_notes`，并请求用户提供本地录屏、截图或可访问片段。

B 站可尝试：

```text
https://api.bilibili.com/x/web-interface/view?bvid=<BV_ID>
https://api.bilibili.com/x/player/playurl?bvid=<BV_ID>&cid=<CID>&qn=16&fnval=16
```

接口结果只能证明元数据或可见流信息；真正设计判断仍要回到画面证据。

## 抽帧建议

首轮抽样：

```text
0s, 30s, 60s, 180s, 420s, 900s, 1500s, 后段
```

如果发现系统切换密集，再对对应窗口补抽：

```text
事件前 3 秒、事件点、事件后 3 秒
```

## 降级输出模板

当工具缺失或链接不可访问时，仍可输出：

```text
access_notes:
- 已能确认：
- 不能确认：
- 缺失工具/权限：
- 本次只能做：
- 建议补充素材：
```

不要把降级分析包装成完整时间轴分析。
