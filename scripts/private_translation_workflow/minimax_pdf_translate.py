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


DEFAULT_API_KEY_ENVS = [
    "MINIMAX_API_KEY",
    "MINIMAX_KEY",
    "MINIMAX_TOKEN",
    "HAILUO_API_KEY",
    "HAILUO_TOKEN",
]
DEFAULT_MODEL = "MiniMax-M2.7"


@dataclass(frozen=True)
class Unit:
    number: int
    title: str
    level: int
    start_page: int
    end_page: int
    stem: str


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


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2))


def slugify(value: str, fallback: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value[:90] or fallback


def normalize_pdf_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\u00ad", "")
    text = text.replace("ThisThisThisThis pagepagepagepage intentionallyintentionallyintentionallyintentionally leftleftleftleft blankblankblankblank", "")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def is_boundary_anchor(level: int, title: str) -> bool:
    if level == 1:
        return True
    if level == 2 and re.match(r"^(\d+\.|[A-Z]\.\d+)", title.strip()):
        return True
    return False


def is_translatable_unit(level: int, title: str) -> bool:
    title = title.strip()
    if title == "Contents":
        return False
    if title.startswith("Part "):
        return False
    if title.startswith("Appendix ") and level == 1:
        return False
    if level == 1:
        return title in {"Preface", "Acknowledgements", "About the Author", "References", "Index"}
    if level == 2:
        return bool(re.match(r"^(\d+\.|[A-Z]\.\d+)", title))
    return False


def build_units(doc: fitz.Document) -> list[Unit]:
    toc = doc.get_toc()
    anchors = [
        {"order": order, "level": level, "title": title.strip(), "page": page}
        for order, (level, title, page) in enumerate(toc)
        if is_boundary_anchor(level, title)
    ]
    anchors.sort(key=lambda item: (item["page"], item["order"]))

    units: list[Unit] = []
    for anchor in anchors:
        title = str(anchor["title"])
        level = int(anchor["level"])
        start_page = int(anchor["page"])
        if not is_translatable_unit(level, title):
            continue
        next_pages = [
            int(other["page"])
            for other in anchors
            if int(other["page"]) > start_page
        ]
        end_page = (min(next_pages) - 1) if next_pages else doc.page_count
        if end_page < start_page:
            continue
        stem = f"{len(units) + 1:02d}-{slugify(title, f'unit-{len(units) + 1:02d}')}"
        units.append(
            Unit(
                number=len(units) + 1,
                title=title,
                level=level,
                start_page=start_page,
                end_page=end_page,
                stem=stem,
            )
        )
    return units


def extract_unit_text(doc: fitz.Document, unit: Unit) -> str:
    pages: list[str] = []
    for page_number in range(unit.start_page, unit.end_page + 1):
        text = normalize_pdf_text(doc[page_number - 1].get_text("text", sort=True))
        if not text:
            continue
        pages.append(f"[[PDF page {page_number}]]\n{text}")
    return "\n\n".join(pages).strip()


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


def translation_prompt(unit: Unit, chunk: str, index: int, total: int) -> str:
    return f"""请将下面这段英文数学教材内容翻译为简体中文 Markdown。用途是个人学习与内部研究。

硬性要求：
- 只输出译文，不要解释你的工作过程。
- 不要总结、删节、改写成大意，也不要补写原文没有的内容。
- 保留章节号、小节号、Definition、Theorem、Lemma、Corollary、Remark、Example、Exercise 等编号。
- 数学符号、变量、集合、矩阵、公式、概率记号、约束条件、参考文献编号要尽量原样保留。
- 如果公式或表格因为 PDF 抽取导致排版破损，请尽量按上下文恢复；确实无法判断时，保留可见符号并标注“[公式需人工核对]”。
- 专名可保留英文，例如 Nash equilibrium、Karush-Kuhn-Tucker conditions，并在首次出现时给出中文译名。
- 页面标记如 [[PDF page 24]] 要保留，并译为 [[PDF 第 24 页]]。
- 不做中英双语对照，不保留大段英文原文；只在必要术语处短暂保留英文。
- 本段是《Game Theory Explained: A Mathematical Introduction with Optimization》的翻译单元“{unit.title}”第 {index}/{total} 块，只翻译本块。

原文：

{chunk}
"""


def call_minimax(prompt: str, model: str, timeout: int, max_completion_tokens: int) -> tuple[str, dict, str]:
    key_name, key = read_api_key()
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "name": "MiniMax AI",
                "content": (
                    "You are a senior English-to-Simplified-Chinese translator "
                    "and mathematical editor for game theory and optimization textbooks."
                ),
            },
            {"role": "user", "name": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0.2,
        "top_p": 0.9,
        "max_completion_tokens": max_completion_tokens,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    last_error: Exception | None = None

    for endpoint in minimax_endpoints():
        for attempt in range(1, 4):
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
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError) as exc:
                last_error = exc
                print(f"    attempt {attempt} failed at {endpoint}: {type(exc).__name__}: {exc}", flush=True)
                time.sleep(min(20, attempt * 3))
    raise RuntimeError(f"MiniMax call failed: {last_error}")


def create_project_files(out_dir: Path, pdf_path: Path, doc: fitz.Document, units: list[Unit]) -> None:
    source_manifest = f"""# Source Manifest

| Item | Value |
| --- | --- |
| Original title | Game Theory Explained: A Mathematical Introduction with Optimization |
| Author | Christopher Griffin |
| Source file | `{pdf_path}` |
| PDF pages | {doc.page_count} |
| Translation engine | MiniMax API |
| Output boundary | Private study / internal research |
| Output directory | `{out_dir}` |

Note: This project keeps extracted text and translations in a private temporary directory. Do not publish the full translation without confirming rights.
"""
    write_text(out_dir / "source_manifest.md", source_manifest)

    rows = [
        "| No. | Unit | PDF pages | Source text | Translation |",
        "| ---: | --- | ---: | --- | --- |",
    ]
    for unit in units:
        rows.append(
            f"| {unit.number} | {unit.title} | {unit.start_page}-{unit.end_page} | "
            f"`work/extracted_text/{unit.stem}.txt` | `chapters/{unit.stem}.md` |"
        )
    write_text(out_dir / "source_outline.md", "# Source Outline\n\n" + "\n".join(rows))

    readme = f"""# Game Theory Explained Chinese Translation Workspace

Original: Game Theory Explained: A Mathematical Introduction with Optimization
Author: Christopher Griffin
Status: MiniMax translation workspace prepared
Boundary: private study / internal research

Main outputs:
- `chapters/`: translated units.
- `00-full-cn-translation.md`: combined Chinese translation.
- `source_manifest.md` and `source_outline.md`: source and progress map.
- `audit/quality-report.md`: automated checks and remaining human-review notes.
- `work/`: extracted text, chunk translations, and MiniMax run metadata.

The translation is generated from PDF text extraction, so formulas, tables, references, and index entries should be manually checked before serious use.
"""
    write_text(out_dir / "README.md", readme)


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
    model: str,
    timeout: int,
    chunk_chars: int,
    max_completion_tokens: int,
    sleep_seconds: float,
    force: bool,
) -> dict:
    chapter_path = out_dir / "chapters" / f"{unit.stem}.md"
    if chapter_path.exists() and not force:
        return {"unit": unit.stem, "status": "skipped-existing", "chunks": 0}

    chunks = split_text(source_text, chunk_chars)
    chunk_dir = out_dir / "work" / "chunk_translations" / unit.stem
    meta_dir = out_dir / "work" / "minimax_runs" / unit.stem
    chunk_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)

    outputs: list[str] = []
    chunk_metas: list[dict] = []
    print(f"UNIT {unit.number:02d}: {unit.title} pages={unit.start_page}-{unit.end_page} chunks={len(chunks)}", flush=True)

    for index, chunk in enumerate(chunks, start=1):
        chunk_path = chunk_dir / f"chunk-{index:03d}.md"
        meta_path = meta_dir / f"chunk-{index:03d}.json"
        if chunk_path.exists() and not force:
            print(f"  chunk {index}/{len(chunks)} skipped", flush=True)
            outputs.append(chunk_path.read_text(encoding="utf-8").strip())
            if meta_path.exists():
                chunk_metas.append(json.loads(meta_path.read_text(encoding="utf-8")))
            continue

        print(f"  chunk {index}/{len(chunks)} chars={len(chunk)}", flush=True)
        content, meta, endpoint = call_minimax(
            translation_prompt(unit, chunk, index, len(chunks)),
            model=model,
            timeout=timeout,
            max_completion_tokens=max_completion_tokens,
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

    chapter_header = f"# {unit.title}\n\n> PDF pages: {unit.start_page}-{unit.end_page}\n\n"
    write_text(chapter_path, chapter_header + "\n\n".join(part.strip() for part in outputs if part.strip()))
    return {"unit": unit.stem, "status": "translated", "chunks": len(chunks), "meta": chunk_metas}


def write_glossary(out_dir: Path) -> None:
    glossary = """# Terms Glossary

| English | Chinese | Note |
| --- | --- | --- |
| game theory | 博弈论 | 研究策略互动的数学理论 |
| payoff | 收益 | 也可译作支付或效用，本文按语境处理 |
| utility | 效用 | 决策理论中的偏好数值表示 |
| expected value | 期望值 | 概率论基础概念 |
| expected utility | 期望效用 | von Neumann-Morgenstern 框架 |
| extensive form | 扩展式 | 博弈树表示 |
| normal form | 标准式 | 也称 strategic form |
| strategic form | 策略式 | 与 normal form 相关 |
| matrix game | 矩阵博弈 | 双人博弈常见表示 |
| saddle point | 鞍点 | 零和博弈中的均衡条件 |
| mixed strategy | 混合策略 | 策略上的概率分布 |
| Nash equilibrium | 纳什均衡 | 核心均衡概念 |
| dominated strategy | 被支配策略 | 可被其他策略严格或弱支配 |
| minimax theorem | 极小极大定理 | 零和博弈基础定理 |
| optimization | 优化 | 与均衡求解相连 |
| Karush-Kuhn-Tucker conditions | Karush-Kuhn-Tucker 条件 | 常简称 KKT 条件 |
| linear programming | 线性规划 | 优化问题类型 |
| quadratic program | 二次规划 | 优化问题类型 |
| cooperative game | 合作博弈 | 关注联盟与收益分配 |
| bargaining problem | 讨价还价问题 | Nash bargaining problem |
| replicator equation | 复制子方程 | 演化博弈常用动力系统 |
"""
    write_text(out_dir / "00-terms-glossary.md", glossary)


def regenerate_combined(out_dir: Path) -> None:
    parts = [
        "# Game Theory Explained: A Mathematical Introduction with Optimization - 中文初译\n",
        "> Translation engine: MiniMax API. Boundary: private study / internal research. Formulas and tables need manual verification.\n",
    ]
    for chapter in sorted((out_dir / "chapters").glob("*.md")):
        parts.append("\n\n---\n\n" + chapter.read_text(encoding="utf-8").strip())
    write_text(out_dir / "00-full-cn-translation.md", "\n".join(parts))


def write_quality_report(out_dir: Path, units: list[Unit], translated_results: list[dict]) -> None:
    chapter_files = sorted((out_dir / "chapters").glob("*.md"))
    combined = out_dir / "00-full-cn-translation.md"
    combined_text = combined.read_text(encoding="utf-8") if combined.exists() else ""
    warning_patterns = [
        "I am an AI",
        "as an AI",
        "---TRANSLATION---",
        "pending",
        "无法翻译",
    ]
    warnings = [pattern for pattern in warning_patterns if pattern.lower() in combined_text.lower()]
    total_chunks = sum(int(result.get("chunks") or 0) for result in translated_results)

    report = f"""# Quality Report

## Current Status

- Translation engine: MiniMax API.
- Units planned: {len(units)}.
- Unit files present: {len(chapter_files)}.
- MiniMax chunks translated in this run: {total_chunks}.
- Combined file: `00-full-cn-translation.md`.
- Glossary file: `00-terms-glossary.md`.

## Automated Checks

- Residual placeholder / AI self-reference pattern count: {len(warnings)}.
- Warning patterns found: {", ".join(warnings) if warnings else "none"}.
- Source extraction method: PyMuPDF text extraction.

## Human Review Still Needed

- Mathematical formulas and tables should be checked against the PDF.
- Figures are not redrawn or image-translated in this text-first run.
- References and index entries may need manual style cleanup.
- The output is for private study / internal research; confirm rights before any public distribution.
"""
    write_text(out_dir / "audit" / "quality-report.md", report)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Translate a PDF book with MiniMax into a private Markdown workspace.")
    parser.add_argument("--pdf", required=True, help="Input PDF path.")
    parser.add_argument("--out", required=True, help="Output directory.")
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--chunk-chars", type=int, default=6500)
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--max-completion-tokens", type=int, default=12000)
    parser.add_argument("--sleep", type=float, default=0.8)
    parser.add_argument("--max-units", type=int, default=0, help="For testing: translate only the first N units.")
    parser.add_argument("--prepare-only", action="store_true", help="Extract and create project files without API calls.")
    parser.add_argument("--force", action="store_true", help="Retranslate existing chunks and chapters.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = Path(args.pdf).expanduser().resolve()
    out_dir = Path(args.out).expanduser().resolve()
    if not pdf_path.exists():
        raise FileNotFoundError(pdf_path)

    out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    units = build_units(doc)
    if args.max_units:
        units = units[: args.max_units]

    create_project_files(out_dir, pdf_path, doc, units)
    extracted = save_extracted_text(out_dir, doc, units)
    write_glossary(out_dir)

    if args.prepare_only:
        write_quality_report(out_dir, units, [])
        print(f"Prepared translation workspace: {out_dir}", flush=True)
        return

    translated_results: list[dict] = []
    for unit, source_text in extracted:
        if not source_text.strip():
            continue
        translated_results.append(
            translate_unit(
                out_dir=out_dir,
                unit=unit,
                source_text=source_text,
                model=args.model,
                timeout=args.timeout,
                chunk_chars=args.chunk_chars,
                max_completion_tokens=args.max_completion_tokens,
                sleep_seconds=args.sleep,
                force=args.force,
            )
        )
        regenerate_combined(out_dir)
        write_quality_report(out_dir, units, translated_results)

    regenerate_combined(out_dir)
    write_quality_report(out_dir, units, translated_results)
    print(f"Done: {out_dir}", flush=True)


if __name__ == "__main__":
    main()
