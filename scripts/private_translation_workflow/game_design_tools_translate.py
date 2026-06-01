from __future__ import annotations

import argparse
import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import fitz


BOOK_TITLE = "Game Design Tools: Cognitive, Psychological, and Practical Approaches"
BOOK_AUTHOR = "Diego Ricchiuti"
DEFAULT_MODEL = "MiniMax-M2.7"
DEFAULT_API_KEY_ENVS = [
    "MINIMAX_API_KEY",
    "MINIMAX_KEY",
    "MINIMAX_TOKEN",
    "HAILUO_API_KEY",
    "HAILUO_TOKEN",
]
FRONT_OR_BACK_MATTER = {
    "Dedication",
    "Foreword",
    "Acknowledgments",
    "About the Author",
    "Index",
}


@dataclass(frozen=True)
class Unit:
    number: int
    title: str
    level: int
    start_page: int
    end_page: int
    stem: str


@dataclass(frozen=True)
class FigureAsset:
    page: int
    index_on_page: int
    unit_stem: str
    asset_rel: str
    bbox: tuple[float, float, float, float]


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2))


def read_api_key() -> tuple[str, str]:
    for name in DEFAULT_API_KEY_ENVS:
        value = os.environ.get(name)
        if value:
            return name, value
    raise RuntimeError("Missing MiniMax API key. Set MINIMAX_API_KEY first.")


def minimax_endpoints() -> list[str]:
    bases: list[str] = []
    if os.environ.get("MINIMAX_BASE_URL"):
        bases.append(os.environ["MINIMAX_BASE_URL"])
    bases.extend(["https://api.minimaxi.com", "https://api.minimax.io"])

    endpoints: list[str] = []
    for base in bases:
        base = base.rstrip("/")
        endpoint = (
            base
            if base.endswith("/v1/text/chatcompletion_v2")
            else f"{base}/v1/text/chatcompletion_v2"
        )
        if endpoint not in endpoints:
            endpoints.append(endpoint)
    return endpoints


def call_minimax(
    prompt: str,
    model: str,
    timeout: int,
    max_completion_tokens: int,
) -> tuple[str, dict, str]:
    key_name, key = read_api_key()
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "name": "MiniMax AI",
                "content": (
                    "You are a senior English-to-Simplified-Chinese translator, "
                    "Chinese editor, and game-design terminology specialist."
                ),
            },
            {"role": "user", "name": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0.22,
        "top_p": 0.9,
        "max_completion_tokens": max_completion_tokens,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    last_error: Exception | None = None

    for endpoint in minimax_endpoints():
        for attempt in range(1, 6):
            try:
                request = urllib.request.Request(
                    endpoint,
                    data=body,
                    headers={
                        "Authorization": f"Bearer {key}",
                        "Content-Type": "application/json",
                    },
                    method="POST",
                )
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    data = json.loads(response.read().decode("utf-8"))

                base_resp = data.get("base_resp") or {}
                if base_resp.get("status_code") not in (None, 0):
                    raise RuntimeError(f"MiniMax base_resp error: {base_resp}")

                content = ((data.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
                if not content.strip():
                    raise RuntimeError("MiniMax returned empty content")
                meta = {
                    "api_key_env": key_name,
                    "usage": data.get("usage"),
                    "finish_reason": (data.get("choices") or [{}])[0].get("finish_reason"),
                }
                return content.strip(), meta, endpoint
            except urllib.error.HTTPError as exc:
                try:
                    detail = exc.read().decode("utf-8", errors="replace")
                except Exception:
                    detail = ""
                last_error = RuntimeError(f"HTTP {exc.code}: {detail[:500]}")
                print(f"    attempt {attempt} failed at {endpoint}: {last_error}", flush=True)
            except (urllib.error.URLError, TimeoutError, RuntimeError, OSError) as exc:
                last_error = exc
                print(f"    attempt {attempt} failed at {endpoint}: {type(exc).__name__}: {exc}", flush=True)
            time.sleep(min(45, attempt * 6))
    raise RuntimeError(f"MiniMax call failed: {last_error}")


def repetition_issues(text: str) -> list[str]:
    issues: list[str] = []
    repeated_phrase = re.search(
        r"\b([A-Za-z][A-Za-z'-]*(?:\s+[A-Za-z][A-Za-z'-]*){1,4})\b(?:\s+\1\b){8,}",
        text,
        flags=re.IGNORECASE,
    )
    if repeated_phrase:
        issues.append(f"repeated English phrase: {repeated_phrase.group(1)[:80]}")

    words = re.findall(r"[A-Za-z][A-Za-z'-]+", text)
    if len(words) >= 80:
        counts: dict[str, int] = {}
        for word in words:
            key = word.lower()
            counts[key] = counts.get(key, 0) + 1
        word, count = max(counts.items(), key=lambda item: item[1])
        if count > max(35, len(words) // 7):
            issues.append(f"over-repeated English word: {word} x{count}")
    return issues


def validate_translation_output(content: str, source_chars: int) -> list[str]:
    issues: list[str] = []
    if not content.strip():
        issues.append("empty output")
    if len(content) > max(12000, int(source_chars * 3.2)):
        issues.append(f"output too long: {len(content)} chars for {source_chars} source chars")
    issues.extend(repetition_issues(content))
    return issues


def bounded_completion_tokens(chunk: str, max_completion_tokens: int) -> int:
    return min(max_completion_tokens, max(2200, int(len(chunk) * 1.65) + 1200))


def slugify(value: str, fallback: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.replace("–", "-").replace("—", "-").replace("’", "")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value[:84] or fallback


def normalize_pdf_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00ad", "")
    text = text.replace("\ufb01", "fi").replace("\ufb02", "fl")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def is_boundary_anchor(level: int, title: str) -> bool:
    return level <= 2


def is_translatable_unit(level: int, title: str) -> bool:
    title = title.strip()
    if title in FRONT_OR_BACK_MATTER:
        return True
    if level == 2 and re.match(r"^\d+(\.|\s+)", title):
        return True
    return False


def build_units(doc: fitz.Document) -> list[Unit]:
    toc = doc.get_toc()
    anchors = [
        {"order": order, "level": level, "title": title.strip(), "page": page}
        for order, (level, title, page) in enumerate(toc)
        if is_boundary_anchor(level, title)
    ]
    anchors.sort(key=lambda item: (int(item["page"]), int(item["order"])))

    units: list[Unit] = []
    used_stems: set[str] = set()
    for idx, anchor in enumerate(anchors):
        title = str(anchor["title"])
        level = int(anchor["level"])
        start_page = int(anchor["page"])
        if not is_translatable_unit(level, title):
            continue

        next_pages = [
            int(other["page"])
            for other in anchors[idx + 1 :]
            if int(other["page"]) > start_page
        ]
        end_page = (min(next_pages) - 1) if next_pages else doc.page_count
        if end_page < start_page:
            continue

        base = slugify(title, f"unit-{len(units) + 1:02d}")
        stem = f"{len(units) + 1:02d}-{base}"
        suffix = 2
        while stem in used_stems:
            stem = f"{len(units) + 1:02d}-{base}-{suffix}"
            suffix += 1
        used_stems.add(stem)
        units.append(Unit(len(units) + 1, title, level, start_page, end_page, stem))
    return units


def unit_for_page(units: list[Unit], page: int) -> Unit | None:
    for unit in units:
        if unit.start_page <= page <= unit.end_page:
            return unit
    return None


def extract_unit_text(doc: fitz.Document, unit: Unit) -> str:
    pages: list[str] = []
    for page_number in range(unit.start_page, unit.end_page + 1):
        text = normalize_pdf_text(doc[page_number - 1].get_text("text", sort=True))
        if not text:
            continue
        pages.append(f"[[PDF page {page_number}]]\n{text}")
    return "\n\n".join(pages).strip()


def extract_figures(out_dir: Path, doc: fitz.Document, units: list[Unit], force: bool = False) -> list[FigureAsset]:
    assets_dir = out_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    figures: list[FigureAsset] = []

    for page_number in range(1, doc.page_count + 1):
        unit = unit_for_page(units, page_number)
        if unit is None:
            continue
        page = doc[page_number - 1]
        image_blocks = [block for block in page.get_text("dict").get("blocks", []) if block.get("type") == 1]
        visible_index = 0
        for block in image_blocks:
            bbox = fitz.Rect(block["bbox"])
            if bbox.width < 60 or bbox.height < 60:
                continue
            visible_index += 1
            name = f"fig-p{page_number:03d}-{visible_index:02d}.png"
            path = assets_dir / name
            if force or not path.exists():
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=bbox, alpha=False)
                pix.save(path)
            figures.append(
                FigureAsset(
                    page=page_number,
                    index_on_page=visible_index,
                    unit_stem=unit.stem,
                    asset_rel=f"assets/{name}",
                    bbox=(round(bbox.x0, 1), round(bbox.y0, 1), round(bbox.x1, 1), round(bbox.y1, 1)),
                )
            )
    return figures


def split_text(text: str, max_chars: int) -> list[str]:
    blocks = re.split(r"\n{2,}", text.strip())
    chunks: list[str] = []
    current = ""

    def flush() -> None:
        nonlocal current
        if current.strip():
            chunks.append(current.strip())
        current = ""

    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if len(block) > max_chars:
            for line in block.splitlines():
                line = line.strip()
                if not line:
                    continue
                if current and len(current) + len(line) + 2 > max_chars:
                    flush()
                current = f"{current}\n{line}".strip() if current else line
            continue
        if current and len(current) + len(block) + 2 > max_chars:
            flush()
        current = f"{current}\n\n{block}".strip() if current else block
    flush()
    return chunks


def figures_for_unit(figures: list[FigureAsset], unit: Unit) -> list[FigureAsset]:
    return [figure for figure in figures if figure.unit_stem == unit.stem]


def translation_prompt(unit: Unit, chunk: str, index: int, total: int) -> str:
    return f"""请将下面的英文游戏设计书稿翻译为简体中文 Markdown。用途是个人学习与内部研究；请按精细译稿处理。

书名：{BOOK_TITLE}
作者：{BOOK_AUTHOR}
翻译单元：{unit.title}
当前分块：{index}/{total}

硬性要求：
- 只输出译文，不要解释你的工作过程。
- 不要总结、删节、改写成大意，也不要添加原文没有的观点。
- 保留 Markdown 结构、标题层级、列表、表格、脚注、引用编号、游戏名、作者名、理论名和 URL。
- 页面标记如 [[PDF page 24]] 必须保留并译为 [[PDF 第 24 页]]。
- Figure、Table、Task、Chapter Guide、Task Guide、Golden Rules 等标题和图注/表头都要翻译。
- PDF 抽取导致的断词、换行、标题重复或表格错位，请在不改作者观点的前提下尽量恢复；无法判断时标注“[原文抽取需核对]”。
- 不做逐段中英对照，不堆大段英文原文；仅在术语首次出现或专名处短暂保留英文。
- 中文要像给游戏策划、设计研究者、制作人看的专业材料：顺、准、清楚，少英文腔。
- 译文长度应与原文信息量相当；不要续写、不要发散，不要反复输出同一个英文术语或短语。
- 翻完本块最后一句就停止。

术语偏好：
- game design tools：游戏设计工具
- game design：游戏设计
- target audience：目标受众
- archetype：原型
- praxeology：行动学（praxeology）
- self-determination theory：自我决定理论
- habit loop：习惯回路
- operant conditioning：操作性条件作用
- game design pattern：游戏设计模式
- MDA Framework：MDA 框架
- nudge：助推
- behavioural game design：行为游戏设计
- emotional game design：情感化游戏设计
- documentation：文档化 / 文档工作，按上下文选择
- playtesting：试玩测试
- evaluation：评估

原文：

{chunk}
"""


def retry_translation_prompt(unit: Unit, chunk: str, index: int, total: int, issues: list[str]) -> str:
    issue_text = "; ".join(issues)
    return f"""请重新翻译下面这段英文游戏设计书稿。上一次输出未通过质量检查：{issue_text}。

请严格遵守：
- 只输出本段中文译文。
- 不要续写，不要解释，不要总结，不要重复英文短语。
- 英文术语只在首次需要辨识时保留一次，例如“信念暂停（suspension of disbelief）”，后文用中文。
- 输出长度要明显短于原文字符数的 2 倍；翻完本块最后一句立刻停止。
- 保留页面标记并译为 [[PDF 第 N 页]]。
- 当前单元：{unit.title}，分块：{index}/{total}。

原文：

{chunk}
"""


def inject_images(text: str, figures: list[FigureAsset]) -> str:
    if not figures:
        return text

    output = text
    remaining: list[FigureAsset] = []
    for figure in figures:
        if figure.asset_rel in output or f"../{figure.asset_rel}" in output:
            continue
        snippet = (
            f"\n\n![PDF 第 {figure.page} 页图像 {figure.index_on_page}](../{figure.asset_rel})\n\n"
            f"图示说明：原书第 {figure.page} 页的图像资产，需结合相邻正文或原图注复核其具体含义。"
        )
        markers = [f"[[PDF 第 {figure.page} 页]]", f"[[PDF page {figure.page}]]"]
        inserted = False
        for marker in markers:
            position = output.find(marker)
            if position >= 0:
                line_end = output.find("\n", position)
                if line_end < 0:
                    line_end = len(output)
                output = output[:line_end] + snippet + output[line_end:]
                inserted = True
                break
        if not inserted:
            remaining.append(figure)

    if remaining:
        lines = ["", "## 本单元图像资产", ""]
        for figure in remaining:
            lines.extend(
                [
                    f"![PDF 第 {figure.page} 页图像 {figure.index_on_page}](../{figure.asset_rel})",
                    "",
                    f"图示说明：原书第 {figure.page} 页的图像资产，需结合相邻正文或原图注复核其具体含义。",
                    "",
                ]
            )
        output = output.rstrip() + "\n\n" + "\n".join(lines).rstrip()
    return output


def create_project_files(out_dir: Path, pdf_path: Path, doc: fitz.Document, units: list[Unit], figures: list[FigureAsset]) -> None:
    source_manifest = f"""# 来源清单

| 项目 | 内容 |
| --- | --- |
| 原书 | {BOOK_TITLE} |
| 作者 | {BOOK_AUTHOR} |
| 来源文件 | `{pdf_path}` |
| PDF 页数 | {doc.page_count} |
| PDF 目录项 | {len(doc.get_toc())} |
| 翻译引擎 | MiniMax API |
| 交付目录 | `{out_dir}` |
| 使用边界 | 个人学习 / 内部研究；公开传播或商业使用前需自行确认授权 |

## 处理方式

- PyMuPDF 抽取正文文本与目录。
- 按目录拆分为 {len(units)} 个翻译单元。
- 抽取原 PDF 图像块 {len(figures)} 个，写入 `assets/`，并在章节译文中按页码回填。
- 英文原文仅用于私有翻译流水线，不应提交到公开仓库或公开传播。
"""
    write_text(out_dir / "source_manifest.md", source_manifest)

    rows = [
        "| 序号 | 翻译单元 | PDF 页码 | 源文本 | 译文 |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for unit in units:
        rows.append(
            f"| {unit.number} | {unit.title} | {unit.start_page}-{unit.end_page} | "
            f"`work/extracted_text/{unit.stem}.txt` | `chapters/{unit.stem}.md` |"
        )
    write_text(out_dir / "source_outline.md", "# 来源拆分\n\n" + "\n".join(rows))

    readme = f"""# Game Design Tools 中文翻译工作区

原名：{BOOK_TITLE}  
作者：{BOOK_AUTHOR}  
状态：已建立私有翻译包，等待或正在进行 MiniMax 初译  
使用边界：个人学习 / 内部研究；公开传播或商业使用前需确认授权

## 交付范围

- 翻译单元：{len(units)} 个。
- 图片资产：{len(figures)} 个 PDF 图像块，位于 `assets/`。
- 章节译文：`chapters/`。
- 合并初译：`00-全书初译.md`。
- 术语表：`00-术语表.md`。
- 质量门：`audit/质量门报告.md`。

## 翻译原则

- 术语先统一，再翻正文。
- 游戏名、书名、作者名、理论名优先保留英文原名；关键术语首次出现可补英文。
- 图注、表头、任务说明、工具步骤纳入翻译范围。
- 不做逐段双语，不堆大段英文原文。
"""
    write_text(out_dir / "README.md", readme)


def write_glossary(out_dir: Path) -> None:
    glossary = """# 术语表

| English | 中文译法 | 语境/说明 | 状态 |
| --- | --- | --- | --- |
| game design tools | 游戏设计工具 | 本书核心概念，指可用于分析、生产、评估和文档化的工具。 | confirmed |
| target audience | 目标受众 | 市场与体验分析语境。 | confirmed |
| archetype | 原型 | 玩家类型、人格或行为模式语境。 | confirmed |
| Bartle's Archetypes | Bartle 玩家类型 | 也可写作 Bartle’s Archetypes，保留作者名。 | confirmed |
| Quantic Foundry | Quantic Foundry | 公司/模型名，保留英文。 | confirmed |
| Big Five | 大五人格 | 心理学模型。 | confirmed |
| praxeology | 行动学（praxeology） | 研究有目的行动；首次出现保留英文。 | tentative |
| self-determination theory | 自我决定理论 | 心理学动机理论。 | confirmed |
| habit loop | 习惯回路 | 行为设计语境。 | confirmed |
| operant conditioning | 操作性条件作用 | 行为心理学语境。 | confirmed |
| game design pattern | 游戏设计模式 | 类比设计模式，不译作“图案”。 | confirmed |
| MDA Framework | MDA 框架 | Mechanics-Dynamics-Aesthetics。 | confirmed |
| nudge | 助推 | 行为经济学/选择架构语境。 | confirmed |
| behavioural game design | 行为游戏设计 | 本书章节名，保持全书一致。 | confirmed |
| emotional game design | 情感化游戏设计 | 情绪体验与设计工具语境。 | confirmed |
| documentation | 文档化 / 文档工作 | 按上下文选择。 | confirmed |
| golden rules | 黄金法则 | 文档章节语境。 | confirmed |
| pivotal documents | 关键文档 | 文档生产语境。 | confirmed |
| playtesting | 试玩测试 | 用户测试/设计验证语境。 | confirmed |
| evaluation | 评估 | 与 analysis、testing 区分。 | confirmed |
"""
    write_text(out_dir / "00-术语表.md", glossary)


def write_figures_manifest(out_dir: Path, figures: list[FigureAsset]) -> None:
    rows = [
        "# 图片清单",
        "",
        "本清单由 PDF 图像块裁切生成，默认仅用于个人学习 / 内部研究，不代表具备公开转载授权。",
        "",
        "| 资产 | PDF 页 | 页内序号 | 翻译单元 | BBox | 回填状态 |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    for figure in figures:
        bbox = ", ".join(f"{value:g}" for value in figure.bbox)
        rows.append(
            f"| `{figure.asset_rel}` | {figure.page} | {figure.index_on_page} | "
            f"`{figure.unit_stem}` | `{bbox}` | 自动按页码回填 |"
        )
    write_text(out_dir / "assets" / "figures_manifest.md", "\n".join(rows))


def save_extracted_text(out_dir: Path, doc: fitz.Document, units: list[Unit]) -> list[tuple[Unit, str]]:
    extracted: list[tuple[Unit, str]] = []
    for unit in units:
        text = extract_unit_text(doc, unit)
        write_text(out_dir / "work" / "extracted_text" / f"{unit.stem}.txt", text)
        extracted.append((unit, text))
    return extracted


def translate_unit(
    out_dir: Path,
    unit: Unit,
    source_text: str,
    figures: list[FigureAsset],
    model: str,
    timeout: int,
    chunk_chars: int,
    max_completion_tokens: int,
    sleep_seconds: float,
    force: bool,
) -> dict:
    chapter_path = out_dir / "chapters" / f"{unit.stem}.md"
    if chapter_path.exists() and not force:
        existing = chapter_path.read_text(encoding="utf-8")
        issues = validate_translation_output(existing, len(source_text))
        if not issues:
            return {"unit": unit.stem, "title": unit.title, "status": "skipped-existing", "chunks": 0}
        print(
            f"UNIT {unit.number:02d}: existing chapter failed validation; retranslating: {'; '.join(issues)}",
            flush=True,
        )

    chunks = split_text(source_text, chunk_chars)
    chunk_dir = out_dir / "work" / "chunk_translations" / unit.stem
    meta_dir = out_dir / "work" / "minimax_runs" / unit.stem
    chunk_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)

    outputs: list[str] = []
    chunk_metas: list[dict] = []
    print(
        f"UNIT {unit.number:02d}: {unit.title} pages={unit.start_page}-{unit.end_page} chunks={len(chunks)}",
        flush=True,
    )

    for index, chunk in enumerate(chunks, start=1):
        chunk_path = chunk_dir / f"chunk-{index:03d}.md"
        meta_path = meta_dir / f"chunk-{index:03d}.json"
        if chunk_path.exists() and not force:
            existing = chunk_path.read_text(encoding="utf-8").strip()
            issues = validate_translation_output(existing, len(chunk))
            if not issues:
                print(f"  chunk {index}/{len(chunks)} skipped", flush=True)
                outputs.append(existing)
                if meta_path.exists():
                    chunk_metas.append(json.loads(meta_path.read_text(encoding="utf-8")))
                continue
            print(
                f"  chunk {index}/{len(chunks)} cached output failed validation; retranslating: {'; '.join(issues)}",
                flush=True,
            )

        print(f"  chunk {index}/{len(chunks)} chars={len(chunk)}", flush=True)
        content = ""
        meta: dict = {}
        endpoint = ""
        issues: list[str] = []
        for attempt in range(1, 4):
            prompt = (
                retry_translation_prompt(unit, chunk, index, len(chunks), issues)
                if issues
                else translation_prompt(unit, chunk, index, len(chunks))
            )
            content, meta, endpoint = call_minimax(
                prompt,
                model=model,
                timeout=timeout,
                max_completion_tokens=bounded_completion_tokens(chunk, max_completion_tokens),
            )
            issues = validate_translation_output(content, len(chunk))
            if not issues:
                break
            print(
                f"    validation failed attempt {attempt}/3: {'; '.join(issues)}",
                flush=True,
            )
            time.sleep(min(12, attempt * 3))
        if issues:
            raise RuntimeError(
                f"Translation failed validation for {unit.stem} chunk {index}: {'; '.join(issues)}"
            )
        write_text(chunk_path, content)
        run_meta = {
            **meta,
            "endpoint": endpoint,
            "unit": unit.title,
            "unit_stem": unit.stem,
            "chunk_index": index,
            "chunk_total": len(chunks),
            "source_chars": len(chunk),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        write_json(meta_path, run_meta)
        outputs.append(content)
        chunk_metas.append(run_meta)
        time.sleep(sleep_seconds)

    body = "\n\n".join(part.strip() for part in outputs if part.strip())
    body = inject_images(body, figures_for_unit(figures, unit))
    chapter_header = f"# {unit.title}\n\n> PDF pages: {unit.start_page}-{unit.end_page}\n\n"
    write_text(chapter_path, chapter_header + body)
    return {"unit": unit.stem, "title": unit.title, "status": "translated", "chunks": len(chunks), "meta": chunk_metas}


def regenerate_combined(out_dir: Path) -> None:
    parts = [
        f"# {BOOK_TITLE} 中文初译\n",
        "> 状态：MiniMax API 分章初译；图片按 PDF 图像块裁切并按页码回填。仍需人工精校与授权确认。  \n"
        "> 使用边界：个人学习 / 内部研究；公开传播或商业使用前需自行确认授权。\n",
    ]
    for chapter in sorted((out_dir / "chapters").glob("*.md")):
        content = chapter.read_text(encoding="utf-8").strip().replace("../assets/", "assets/")
        parts.append("\n\n---\n\n" + content)
    write_text(out_dir / "00-全书初译.md", "\n".join(parts))


def write_quality_report(out_dir: Path, units: list[Unit], figures: list[FigureAsset], translated_results: list[dict]) -> None:
    chapter_files = sorted((out_dir / "chapters").glob("*.md"))
    combined = out_dir / "00-全书初译.md"
    combined_text = combined.read_text(encoding="utf-8") if combined.exists() else ""
    warning_patterns = [
        "I am an AI",
        "as an AI",
        "作为 AI",
        "作为AI",
        "---TRANSLATION---",
        "---NEW_TERMS---",
        "pending",
        "无法翻译",
        "```",
    ]
    warnings = [pattern for pattern in warning_patterns if pattern.lower() in combined_text.lower()]
    repetition_warnings = repetition_issues(combined_text)
    overlong_files: list[str] = []
    extracted_dir = out_dir / "work" / "extracted_text"
    for chapter in chapter_files:
        source = extracted_dir / f"{chapter.stem}.txt"
        if not source.exists():
            continue
        source_chars = len(source.read_text(encoding="utf-8"))
        output_chars = len(chapter.read_text(encoding="utf-8"))
        if output_chars > max(12000, int(source_chars * 3.2)):
            overlong_files.append(f"{chapter.name} ({output_chars}/{source_chars})")
    total_chunks = sum(int(result.get("chunks") or 0) for result in translated_results)
    source_units = {unit.stem for unit in units}
    translated_units = {path.stem for path in chapter_files}
    image_assets = sorted((out_dir / "assets").glob("fig-*.png"))
    chapter_refs = re.findall(r"!\[[^\]]*\]\(\.\./assets/fig-[^)]+\.png\)", "\n".join(p.read_text(encoding="utf-8") for p in chapter_files))
    combined_refs = re.findall(r"!\[[^\]]*\]\(assets/fig-[^)]+\.png\)", combined_text)

    report = f"""# 质量门报告

## 本轮状态

- 文本状态：已生成 {len(chapter_files)}/{len(units)} 个章节初译文件。
- 图片状态：已抽取 {len(image_assets)} 个 PDF 图像块，并自动按页码回填。
- 英文好句：尚未生成独立摘要。
- 授权边界：个人学习 / 内部研究；公开传播或商业使用前需确认授权。

## 自动检查

- 翻译单元计划数：{len(units)}。
- 章节文件数：{len(chapter_files)}。
- 本轮 API 翻译 chunk 数：{total_chunks}。
- 未生成章节：{", ".join(sorted(source_units - translated_units)) if source_units - translated_units else "无"}。
- 图片资产数：{len(image_assets)}。
- 分章图片引用数：{len(chapter_refs)}。
- 合并版图片引用数：{len(combined_refs)}。
- 模型分隔符 / AI 自称 / 代码块残留：{len(warnings)}。
- 命中模式：{", ".join(warnings) if warnings else "无"}。
- 异常超长章节：{", ".join(overlong_files) if overlong_files else "无"}。
- 英文短语重复风险：{", ".join(repetition_warnings) if repetition_warnings else "无"}。

## 仍需人工判断

- 图内英文标签尚未逐张中文化重绘；目前是原图裁切回填。
- PDF 抽取可能造成表格、脚注和断词错位，关键章节仍建议对照原书人工复核。
- 当前为初译合并版；若要称为“完整精校版”，还需生成 `chapters_polished/`、`00-全书精校版.md` 和 `03-英文好句摘要与译法.md`。
"""
    write_text(out_dir / "audit" / "质量门报告.md", report)


def update_readme_status(out_dir: Path, units: list[Unit]) -> None:
    readme = out_dir / "README.md"
    text = readme.read_text(encoding="utf-8")
    chapter_count = len(list((out_dir / "chapters").glob("*.md")))
    text = re.sub(
        r"状态：.*",
        f"状态：MiniMax API 初译进度 {chapter_count}/{len(units)} 个翻译单元",
        text,
        count=1,
    )
    readme.write_text(text, encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate Game Design Tools into a private Markdown workspace.")
    parser.add_argument("--pdf", required=True, help="Input PDF path.")
    parser.add_argument("--out", required=True, help="Output directory.")
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--chunk-chars", type=int, default=5200)
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--max-completion-tokens", type=int, default=14000)
    parser.add_argument("--sleep", type=float, default=0.8)
    parser.add_argument("--prepare-only", action="store_true", help="Extract source and figures without API calls.")
    parser.add_argument("--force", action="store_true", help="Retranslate existing chunks and chapters.")
    parser.add_argument("--start-order", type=int, default=1, help="Start from this 1-based unit order.")
    parser.add_argument("--max-units", type=int, default=0, help="Translate at most N units in this run.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    all_units = build_units(doc)
    figures = extract_figures(out_dir, doc, all_units, force=args.force)
    create_project_files(out_dir, pdf_path, doc, all_units, figures)
    write_glossary(out_dir)
    write_figures_manifest(out_dir, figures)
    extracted = save_extracted_text(out_dir, doc, all_units)
    write_quality_report(out_dir, all_units, figures, [])
    update_readme_status(out_dir, all_units)

    if args.prepare_only:
        print(f"Prepared translation workspace: {out_dir}", flush=True)
        print(f"Units: {len(all_units)}; figures: {len(figures)}", flush=True)
        return

    selected = [(unit, text) for unit, text in extracted if unit.number >= args.start_order]
    if args.max_units:
        selected = selected[: args.max_units]

    translated_results: list[dict] = []
    for unit, source_text in selected:
        if not source_text.strip():
            continue
        result = translate_unit(
            out_dir=out_dir,
            unit=unit,
            source_text=source_text,
            figures=figures,
            model=args.model,
            timeout=args.timeout,
            chunk_chars=args.chunk_chars,
            max_completion_tokens=args.max_completion_tokens,
            sleep_seconds=args.sleep,
            force=args.force,
        )
        translated_results.append(result)
        regenerate_combined(out_dir)
        write_quality_report(out_dir, all_units, figures, translated_results)
        update_readme_status(out_dir, all_units)

    regenerate_combined(out_dir)
    write_quality_report(out_dir, all_units, figures, translated_results)
    update_readme_status(out_dir, all_units)
    print(f"Done: {out_dir}", flush=True)


if __name__ == "__main__":
    main()
