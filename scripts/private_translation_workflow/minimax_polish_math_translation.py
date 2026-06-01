from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

from minimax_pdf_translate import call_minimax, write_json, write_text


DEFAULT_MODEL = "MiniMax-M2.7"


TERM_GUIDE = """
Core term guide:
- game theory = 博弈论
- payoff = 收益
- utility = 效用
- expected value = 期望值
- expected utility = 期望效用
- extensive form = 扩展式
- normal form = 标准式
- strategic form = 策略式
- matrix game = 矩阵博弈
- zero-sum game = 零和博弈
- saddle point = 鞍点
- mixed strategy = 混合策略
- Nash equilibrium = 纳什均衡
- dominated strategy = 被支配策略
- minimax theorem = 极小极大定理
- optimization = 优化
- Karush-Kuhn-Tucker conditions = Karush-Kuhn-Tucker 条件 / KKT 条件
- linear programming = 线性规划
- quadratic program = 二次规划
- cooperative game = 合作博弈
- bargaining problem = 讨价还价问题
- replicator equation = 复制子方程
"""


def split_long_line(line: str, max_chars: int) -> list[str]:
    if len(line) <= max_chars:
        return [line]
    parts = re.split(r"(?<=[。！？；;.!?])", line)
    chunks: list[str] = []
    current = ""
    for part in parts:
        if not part:
            continue
        if len(part) > max_chars:
            if current.strip():
                chunks.append(current.strip())
                current = ""
            for start in range(0, len(part), max_chars):
                chunks.append(part[start : start + max_chars].strip())
            continue
        if current and len(current) + len(part) > max_chars:
            chunks.append(current.strip())
            current = ""
        current += part
    if current.strip():
        chunks.append(current.strip())
    return [chunk for chunk in chunks if chunk]


def split_text_strict(text: str, max_chars: int) -> list[str]:
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
        pieces: list[str] = []
        if len(block) > max_chars:
            for line in block.splitlines() or [block]:
                line = line.strip()
                if not line:
                    continue
                pieces.extend(split_long_line(line, max_chars))
        else:
            pieces = [block]

        for piece in pieces:
            if current and len(current) + len(piece) + 2 > max_chars:
                flush()
            if len(piece) > max_chars:
                flush()
                chunks.extend(split_long_line(piece, max_chars))
            else:
                current = f"{current}\n\n{piece}".strip() if current else piece
    flush()
    return chunks


def polish_prompt(chapter_name: str, chunk: str, index: int, total: int) -> str:
    return f"""请精校下面这段中文译稿。它来自数学博弈论教材《Game Theory Explained: A Mathematical Introduction with Optimization》的 MiniMax 初译。

目标：做“完整精翻”的中文编辑稿，而不是摘要。

硬性要求：
- 只输出精校后的中文 Markdown，不要解释你的工作过程。
- 不要删减、概括、扩写，也不要新增原文没有的论点。
- 保留所有 Markdown 标题层级、列表、表格、编号、页码标记、引用编号和数学符号。
- 页码标记如 [[PDF 第 24 页]] 必须原样保留。
- Definition、Theorem、Lemma、Corollary、Remark、Example、Exercise 等编号必须保留；可译为“定义/定理/引理/推论/评注/例/习题”。
- 公式、集合、矩阵、变量、上下标、约束条件、概率记号不能被改写成散文；不确定时保留现有表达。
- 统一术语，去掉明显机翻腔，让中文读起来像严肃数学教材。
- 不做中英双语对照，不保留大段英文；专名和固定术语可短暂保留英文。
- 若看到“[公式需人工核对]”，保留它，除非上下文已经足以明确修复。
- 本块是 `{chapter_name}` 的第 {index}/{total} 块；只精校本块，不要补前后文。

{TERM_GUIDE}

待精校译稿：

{chunk}
"""


def chapter_sort_key(path: Path) -> tuple[int, str]:
    match = re.match(r"(\d+)-", path.name)
    return (int(match.group(1)) if match else 9999, path.name)


def polish_chapter(
    chapter: Path,
    out_dir: Path,
    work_dir: Path,
    model: str,
    timeout: int,
    chunk_chars: int,
    max_completion_tokens: int,
    sleep_seconds: float,
    force: bool,
) -> dict:
    polished_path = out_dir / chapter.name
    if polished_path.exists() and not force:
        return {"chapter": chapter.name, "status": "skipped-existing", "chunks": 0}

    source_text = chapter.read_text(encoding="utf-8")
    chunks = split_text_strict(source_text, chunk_chars)
    chunk_dir = work_dir / "polish_chunks" / chapter.stem
    meta_dir = work_dir / "polish_runs" / chapter.stem
    chunk_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)
    if force:
        for old in list(chunk_dir.glob("chunk-*.md")) + list(meta_dir.glob("chunk-*.json")):
            old.unlink()

    outputs: list[str] = []
    metas: list[dict] = []
    print(f"POLISH {chapter.name} chunks={len(chunks)} chars={len(source_text)}", flush=True)

    for index, chunk in enumerate(chunks, start=1):
        chunk_path = chunk_dir / f"chunk-{index:03d}.md"
        meta_path = meta_dir / f"chunk-{index:03d}.json"
        if chunk_path.exists() and not force:
            print(f"  chunk {index}/{len(chunks)} skipped", flush=True)
            outputs.append(chunk_path.read_text(encoding="utf-8").strip())
            if meta_path.exists():
                metas.append(json.loads(meta_path.read_text(encoding="utf-8")))
            continue

        print(f"  chunk {index}/{len(chunks)} chars={len(chunk)}", flush=True)
        content, meta, endpoint = call_minimax(
            polish_prompt(chapter.name, chunk, index, len(chunks)),
            model=model,
            timeout=timeout,
            max_completion_tokens=max_completion_tokens,
        )
        write_text(chunk_path, content)
        run_meta = {
            **meta,
            "endpoint": endpoint,
            "chapter": chapter.name,
            "chunk_index": index,
            "chunk_total": len(chunks),
            "source_chars": len(chunk),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        write_json(meta_path, run_meta)
        outputs.append(content)
        metas.append(run_meta)
        time.sleep(sleep_seconds)

    write_text(polished_path, "\n\n".join(part.strip() for part in outputs if part.strip()))
    return {"chapter": chapter.name, "status": "polished", "chunks": len(chunks), "meta": metas}


def regenerate_combined(root: Path) -> None:
    parts = [
        "# Game Theory Explained: A Mathematical Introduction with Optimization - 中文精校版\n",
        "> Translation engine: MiniMax API. Stage: Chinese polished edition. Boundary: private study / internal research. Formulas and tables still need human verification against the PDF.\n",
    ]
    for chapter in sorted((root / "chapters_polished").glob("*.md"), key=chapter_sort_key):
        parts.append("\n\n---\n\n" + chapter.read_text(encoding="utf-8").strip())
    write_text(root / "00-full-cn-polished.md", "\n".join(parts))


def write_report(root: Path, results: list[dict]) -> None:
    source_files = sorted((root / "chapters").glob("*.md"), key=chapter_sort_key)
    polished_files = sorted((root / "chapters_polished").glob("*.md"), key=chapter_sort_key)
    combined_path = root / "00-full-cn-polished.md"
    combined = combined_path.read_text(encoding="utf-8") if combined_path.exists() else ""

    source_markers = sum(p.read_text(encoding="utf-8").count("[[PDF") for p in source_files)
    polished_markers = sum(p.read_text(encoding="utf-8").count("[[PDF") for p in polished_files)
    warning_patterns = [
        "I am an AI",
        "as an AI",
        "作为 AI",
        "作为AI",
        "---TRANSLATION---",
        "pending",
        "无法翻译",
    ]
    warnings = [pattern for pattern in warning_patterns if pattern.lower() in combined.lower()]
    short_files = []
    length_warnings = []
    marker_warnings = []
    for source in source_files:
        target = root / "chapters_polished" / source.name
        if not target.exists():
            short_files.append(source.name)
            continue
        source_text = source.read_text(encoding="utf-8")
        target_text = target.read_text(encoding="utf-8")
        source_len = len(source_text)
        target_len = len(target_text)
        if target_len < max(200, int(source_len * 0.55)) or target_len > int(source_len * 1.8):
            length_warnings.append(f"{source.name}: source={source_len}, polished={target_len}")
        source_page_markers = source_text.count("[[PDF")
        target_page_markers = target_text.count("[[PDF")
        if source_page_markers != target_page_markers:
            marker_warnings.append(f"{source.name}: source={source_page_markers}, polished={target_page_markers}")

    translated_chunks = sum(int(result.get("chunks") or 0) for result in results)
    chunk_files = len(list((root / "work" / "polish_chunks").glob("*/*.md")))
    report = f"""# Polish Quality Report

## Current Status

- Source chapter files: {len(source_files)}.
- Polished chapter files: {len(polished_files)}.
- Polish chunks completed in this run: {translated_chunks}.
- Polish chunk files present: {chunk_files}.
- Combined polished file: `00-full-cn-polished.md`.

## Automated Checks

- Source page markers: {source_markers}.
- Polished page markers: {polished_markers}.
- Residual placeholder / AI self-reference pattern count: {len(warnings)}.
- Warning patterns found: {", ".join(warnings) if warnings else "none"}.
- Formula review marks: {combined.count("公式需人工核对")}.
- Missing polished files: {", ".join(short_files) if short_files else "none"}.
- Length warnings: {len(length_warnings)}.
- Page marker warnings: {len(marker_warnings)}.

## Length Warnings

{os.linesep.join(f"- {item}" for item in length_warnings) if length_warnings else "- none"}

## Page Marker Warnings

{os.linesep.join(f"- {item}" for item in marker_warnings) if marker_warnings else "- none"}

## Human Review Still Needed

- This is a model-polished Chinese edition, not a manually typeset published translation.
- Mathematical formulas and tables should still be checked against the original PDF.
- Figures are not redrawn or image-translated in this text-first workflow.
- Keep the output private unless rights are confirmed.
"""
    write_text(root / "audit" / "polish-quality-report.md", report)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Polish an existing MiniMax Chinese translation of a math textbook.")
    parser.add_argument("--root", required=True, help="Translation workspace root.")
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--chunk-chars", type=int, default=8500)
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--max-completion-tokens", type=int, default=14000)
    parser.add_argument("--sleep", type=float, default=0.8)
    parser.add_argument("--max-units", type=int, default=0)
    parser.add_argument("--only", default="", help="Comma-separated chapter filename(s) to polish.")
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    source_dir = root / "chapters"
    out_dir = root / "chapters_polished"
    work_dir = root / "work"
    if not source_dir.exists():
        raise FileNotFoundError(source_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    chapters = sorted(source_dir.glob("*.md"), key=chapter_sort_key)
    if args.only:
        wanted = {item.strip() for item in args.only.split(",") if item.strip()}
        chapters = [chapter for chapter in chapters if chapter.name in wanted]
        missing = wanted - {chapter.name for chapter in chapters}
        if missing:
            raise FileNotFoundError(f"Missing requested chapter(s): {', '.join(sorted(missing))}")
    if args.max_units:
        chapters = chapters[: args.max_units]

    results: list[dict] = []
    for chapter in chapters:
        result = polish_chapter(
            chapter=chapter,
            out_dir=out_dir,
            work_dir=work_dir,
            model=args.model,
            timeout=args.timeout,
            chunk_chars=args.chunk_chars,
            max_completion_tokens=args.max_completion_tokens,
            sleep_seconds=args.sleep,
            force=args.force,
        )
        results.append(result)
        regenerate_combined(root)
        write_report(root, results)

    regenerate_combined(root)
    write_report(root, results)
    print(f"Done: {root}", flush=True)


if __name__ == "__main__":
    main()
