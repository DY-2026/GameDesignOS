from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import fitz

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from game_design_tools_translate import (  # noqa: E402
    BOOK_AUTHOR,
    BOOK_TITLE,
    DEFAULT_MODEL,
    build_units,
    call_minimax,
    extract_figures,
    figures_for_unit,
    inject_images,
    repetition_issues,
    split_text,
    validate_translation_output,
    write_json,
    write_text,
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_chapter_header(text: str) -> str:
    text = re.sub(r"^# .+?\n\n> PDF pages: .+?\n\n", "", text, count=1, flags=re.S)
    return text.strip()


def source_translation_pairs(root: Path, unit, source_chunk_chars: int) -> list[tuple[str, str]]:
    source = read(root / "work" / "extracted_text" / f"{unit.stem}.txt")
    chunk_dir = root / "work" / "chunk_translations" / unit.stem
    chunk_files = sorted(chunk_dir.glob("chunk-*.md"))

    if chunk_files:
        source_chunks = split_text(source, source_chunk_chars)
        if len(source_chunks) == len(chunk_files):
            return [(src, read(ch).strip()) for src, ch in zip(source_chunks, chunk_files)]

        combined_translation = "\n\n".join(read(ch).strip() for ch in chunk_files)
        if len(source) + len(combined_translation) <= 16000:
            return [(source, combined_translation)]

    chapter = root / "chapters" / f"{unit.stem}.md"
    return [(source, strip_chapter_header(read(chapter)))]


def group_pairs(pairs: list[tuple[str, str]], max_group_chars: int) -> list[list[tuple[str, str]]]:
    groups: list[list[tuple[str, str]]] = []
    current: list[tuple[str, str]] = []
    current_size = 0

    for pair in pairs:
        size = len(pair[0]) + len(pair[1])
        if current and current_size + size > max_group_chars:
            groups.append(current)
            current = []
            current_size = 0
        current.append(pair)
        current_size += size

    if current:
        groups.append(current)
    return groups


def format_group(group: list[tuple[str, str]]) -> tuple[str, str]:
    source_parts: list[str] = []
    translation_parts: list[str] = []
    for index, (source, translation) in enumerate(group, start=1):
        source_parts.append(f"### Segment {index} Source\n{source.strip()}")
        translation_parts.append(f"### Segment {index} Current Translation\n{translation.strip()}")
    return "\n\n".join(source_parts), "\n\n".join(translation_parts)


def expected_polished_chars(group: list[tuple[str, str]]) -> int:
    raw_chars = sum(len(translation) for _, translation in group)
    cjk_chars = sum(len(re.findall(r"[\u3400-\u9fff]", translation)) for _, translation in group)
    if cjk_chars:
        return min(raw_chars, int(cjk_chars * 1.55) + 400)
    return raw_chars


def clean_polish_output(content: str) -> str:
    content = content.strip()
    cleanup_patterns = [
        r"^\s*(?:[-*]\s*)?(?:#{1,6}\s*)?(?:\*\*)?\s*(?:以下为|下面是|精修后的|修订后的)?\s*Segment\s+\d+[^\n]*$",
        r"^\s*#{1,6}\s*Segment\s+\d+\s+(?:Source|Current Translation|Translation|中文译文|现有中文译文)\s*[:：]?\s*$",
        r"^\s*Segment\s+\d+\s+(?:Source|Current Translation|Translation|中文译文|现有中文译文)\s*[:：]?\s*$",
        r"^\s*#{1,6}\s*(?:英文原文|现有中文译文|Current Translation|精修后的中文译文|修订译文|精校译文)\s*[:：]?\s*$",
    ]
    for pattern in cleanup_patterns:
        content = re.sub(pattern, "", content, flags=re.I | re.M)
    return re.sub(r"\n{3,}", "\n\n", content).strip()


def polish_prompt(unit, source_group: str, translation_group: str, index: int, total: int) -> str:
    return f"""请以“出版级中文译审”的标准，依据英文原文审校并精修现有中文译文。

书名：{BOOK_TITLE}
作者：{BOOK_AUTHOR}
章节/单元：{unit.title}
当前组：{index}/{total}

硬性要求：
- 只输出精修后的中文 Markdown，不要解释工作过程。
- 以英文原文为准，修正误译、漏译、错译、术语漂移、英文腔和不自然中文。
- 不删节、不扩写、不总结，不加入原文没有的观点。
- 保留所有 Markdown 标题层级、列表、表格、页码标记、脚注编号、URL、游戏名、理论名和专有名词。
- 页面标记统一为 [[PDF 第 N 页]]；图片 Markdown 如果出现必须原样保留。
- 图注、表头、任务说明、步骤说明要处理成顺畅中文。
- 术语保持一致：praxeology=行动学（praxeology）；nudge=助推；behavioural game design=行为游戏设计；emotional game design=情感化游戏设计；affordance=可供性/行动暗示，按上下文选择；documentation=文档化/文档工作。
- 英文术语只在首次有必要时保留，避免堆括号和重复英文。
- Segment 只用于你理解输入结构；必须覆盖每个 Segment 的全部内容，但输出中不要保留 Segment 标题，也不要输出英文原文。

英文原文：

{source_group}

现有中文译文：

{translation_group}
"""


def retry_polish_prompt(unit, source_group: str, translation_group: str, index: int, total: int, issues: list[str]) -> str:
    segment_count = len(re.findall(r"^### Segment\s+\d+\s+Source", source_group, flags=re.M))
    return f"""请重新精修下面这组译文。上一版未通过质量检查：{'; '.join(issues)}。

要求：
- 只输出精修后的中文 Markdown。
- 必须覆盖本组全部 {segment_count} 个 Segment 的译文内容；不要概括、删节或只处理前半段。
- 不要保留任何 Segment 标题，不要重复英文短语，不要续写，不要输出解释。
- 以英文原文为准，保留页码标记、标题、列表、表格和 Markdown 结构。
- 当前单元：{unit.title}，组：{index}/{total}。

英文原文：

{source_group}

现有中文译文：

{translation_group}
"""


def validate_polish_output(content: str, translation_chars: int) -> list[str]:
    issues = validate_translation_output(content, max(translation_chars, 1))
    if re.search(r"^\s*.*\bSegment\s+\d+\b.*$", content, flags=re.I | re.M):
        issues.append("internal segment label leaked")
    if re.search(r"^\s*#{1,6}\s*(?:英文原文|现有中文译文|Current Translation|精修后的中文译文|修订译文|精校译文)\s*[:：]?\s*$", content, flags=re.I | re.M):
        issues.append("input heading leaked")
    min_chars = 20 if translation_chars < 120 else max(80, int(translation_chars * 0.45))
    if len(content) < min_chars:
        issues.append(f"polished output too short: {len(content)} for {translation_chars}")
    if len(content) > max(16000, int(translation_chars * 2.25) + 2000):
        issues.append(f"polished output too long: {len(content)} for {translation_chars}")
    issues.extend(repetition_issues(content))
    return list(dict.fromkeys(issues))


def bounded_tokens_for_polish(source_group: str, translation_group: str, max_completion_tokens: int) -> int:
    return min(max_completion_tokens, max(3000, int(len(translation_group) * 1.7) + 1600))


def polish_unit(
    root: Path,
    unit,
    figures,
    model: str,
    timeout: int,
    max_completion_tokens: int,
    source_chunk_chars: int,
    group_chars: int,
    force: bool,
) -> dict:
    out_path = root / "chapters_polished" / f"{unit.stem}.md"
    if out_path.exists() and not force:
        existing = strip_chapter_header(read(out_path))
        source_len = len(read(root / "work" / "extracted_text" / f"{unit.stem}.txt"))
        if not validate_polish_output(existing, source_len):
            return {"unit": unit.stem, "status": "skipped-existing", "groups": 0}

    pairs = source_translation_pairs(root, unit, source_chunk_chars)
    groups = group_pairs(pairs, group_chars)
    out_dir = root / "work" / "polish_chunks" / unit.stem
    meta_dir = root / "work" / "minimax_polish_runs" / unit.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    meta_dir.mkdir(parents=True, exist_ok=True)

    print(f"POLISH {unit.number:02d}: {unit.title} groups={len(groups)}", flush=True)
    outputs: list[str] = []
    metas: list[dict] = []

    for group_index, group in enumerate(groups, start=1):
        group_path = out_dir / f"group-{group_index:03d}.md"
        meta_path = meta_dir / f"group-{group_index:03d}.json"
        raw_translation_chars = sum(len(item[1]) for item in group)
        translation_chars = expected_polished_chars(group)

        if group_path.exists() and not force:
            existing = read(group_path).strip()
            issues = validate_polish_output(existing, translation_chars)
            if not issues:
                print(f"  group {group_index}/{len(groups)} skipped", flush=True)
                outputs.append(existing)
                if meta_path.exists():
                    metas.append(json.loads(read(meta_path)))
                continue
            print(f"  group {group_index}/{len(groups)} cached output failed validation: {'; '.join(issues)}", flush=True)

        source_group, translation_group = format_group(group)
        print(
            f"  group {group_index}/{len(groups)} source+translation chars={len(source_group) + len(translation_group)}",
            flush=True,
        )

        content = ""
        meta: dict = {}
        endpoint = ""
        issues: list[str] = []
        for attempt in range(1, 4):
            prompt = (
                retry_polish_prompt(unit, source_group, translation_group, group_index, len(groups), issues)
                if issues
                else polish_prompt(unit, source_group, translation_group, group_index, len(groups))
            )
            content, meta, endpoint = call_minimax(
                prompt,
                model=model,
                timeout=timeout,
                max_completion_tokens=bounded_tokens_for_polish(source_group, translation_group, max_completion_tokens),
            )
            content = clean_polish_output(content)
            issues = validate_polish_output(content, translation_chars)
            if not issues:
                break
            print(f"    validation failed attempt {attempt}/3: {'; '.join(issues)}", flush=True)
            time.sleep(min(12, attempt * 3))
        if issues:
            raise RuntimeError(f"Polish failed validation for {unit.stem} group {group_index}: {'; '.join(issues)}")

        write_text(group_path, content)
        run_meta = {
            **meta,
            "endpoint": endpoint,
            "unit": unit.title,
            "unit_stem": unit.stem,
            "group_index": group_index,
            "group_total": len(groups),
            "source_chars": sum(len(item[0]) for item in group),
            "translation_chars": raw_translation_chars,
            "expected_polished_chars": translation_chars,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        write_json(meta_path, run_meta)
        outputs.append(content.strip())
        metas.append(run_meta)
        time.sleep(0.8)

    body = "\n\n".join(part.strip() for part in outputs if part.strip())
    body = inject_images(body, figures_for_unit(figures, unit))
    header = f"# {unit.title}\n\n> PDF pages: {unit.start_page}-{unit.end_page}\n\n"
    write_text(out_path, header + body)
    return {"unit": unit.stem, "status": "polished", "groups": len(groups), "meta": metas}


def regenerate_combined(root: Path) -> None:
    parts = [
        f"# {BOOK_TITLE} 中文精校版\n",
        "> 状态：MiniMax API 初译后，依据英文原文进行二轮中文精修。仍建议公开使用前做人工终审与授权确认。  \n"
        "> 使用边界：个人学习 / 内部研究；公开传播或商业使用前需自行确认授权。\n",
    ]
    for chapter in sorted((root / "chapters_polished").glob("*.md")):
        content = read(chapter).strip().replace("../assets/", "assets/")
        parts.append("\n\n---\n\n" + content)
    write_text(root / "00-全书精校版.md", "\n".join(parts))


def build_good_sentence_notes(root: Path, model: str, timeout: int, max_completion_tokens: int) -> None:
    excerpts: list[str] = []
    for chapter in sorted((root / "chapters_polished").glob("*.md")):
        text = strip_chapter_header(read(chapter))
        compact = re.sub(r"\s+", " ", text)[:1200]
        excerpts.append(f"## {chapter.stem}\n{compact}")

    prompt = f"""请基于下面这本游戏设计书的中文精校译文摘取“英文好句摘要与译法”文档。

书名：{BOOK_TITLE}

版权边界：
- 不要复制长英文原句。
- 英文触发词只用 1-3 个词的短语，最多 36 个。
- 主要内容必须是中文观点摘要、译法点评和设计讨论用途。

输出 Markdown：
# 英文好句摘要与译法

然后给一个表格，列为：章节、英文触发词、中文好句摘要、可借鉴的写法、可用于哪类设计讨论。
总计 24-36 行。

中文精校译文摘录：

{chr(10).join(excerpts)}
"""
    content, meta, endpoint = call_minimax(prompt, model=model, timeout=timeout, max_completion_tokens=max_completion_tokens)
    issues = repetition_issues(content)
    if issues:
        raise RuntimeError(f"Good sentence notes failed validation: {'; '.join(issues)}")
    write_text(root / "03-英文好句摘要与译法.md", content)
    write_json(root / "work" / "good_sentence_notes_run.json", {**meta, "endpoint": endpoint, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")})


def write_quality_report(root: Path, units, polish_results: list[dict]) -> None:
    polished = sorted((root / "chapters_polished").glob("*.md"))
    combined = root / "00-全书精校版.md"
    combined_text = read(combined) if combined.exists() else ""
    asset_count = len(list((root / "assets").glob("fig-*.png")))
    chapter_refs = re.findall(r"!\[[^\]]*\]\(\.\./assets/fig-[^)]+\.png\)", "\n".join(read(p) for p in polished))
    combined_refs = re.findall(r"!\[[^\]]*\]\(assets/fig-[^)]+\.png\)", combined_text)
    forbidden_patterns = [
        "I am an AI",
        "as an AI",
        "作为 AI",
        "作为AI",
        "---TRANSLATION---",
        "---NEW_TERMS---",
        "无法翻译",
        "```",
    ]
    warnings = [pattern for pattern in forbidden_patterns if pattern.lower() in combined_text.lower()]
    repetition = repetition_issues(combined_text)
    total_groups = sum(int(item.get("groups") or 0) for item in polish_results)
    cached_groups = len(list((root / "work" / "polish_chunks").glob("*/group-*.md")))

    report = f"""# 质量门报告

## 本轮状态

- 文本状态：已生成 `chapters_polished/` 与 `00-全书精校版.md`，精校章节 {len(polished)}/{len(units)}。
- 图片状态：保留并回填 PDF 图像资产。
- 英文好句：{'已生成 `03-英文好句摘要与译法.md`。' if (root / '03-英文好句摘要与译法.md').exists() else '尚未生成。'}
- 授权边界：个人学习 / 内部研究；公开传播、出版或商业使用前必须确认授权。

## 自动检查

- 精校章节数：{len(polished)} / {len(units)}。
- 本次进程精校 API group 数：{total_groups}。
- 累计已缓存精校 group 数：{cached_groups}。
- 图片资产数：{asset_count}。
- 分章图片引用数：{len(chapter_refs)}。
- 合并版图片引用数：{len(combined_refs)}。
- 模型分隔符 / AI 自称 / 代码块残留：{len(warnings)}。
- 命中模式：{', '.join(warnings) if warnings else '无'}。
- 英文短语重复风险：{', '.join(repetition) if repetition else '无'}。

## 仍需人工判断

- 图内英文标签尚未逐张中文化重绘；目前是原图裁切回填。
- PDF 抽取可能造成表格、脚注和断词错位，关键表格与图注建议终审对照原书。
- “出版级”在这里指中文译文质量目标，不代表具备公开出版授权。
"""
    write_text(root / "audit" / "质量门报告.md", report)


def update_readme(root: Path, units) -> None:
    readme = root / "README.md"
    text = read(readme)
    text = re.sub(
        r"状态：.*",
        f"状态：初译 27/27；二轮精校 {len(list((root / 'chapters_polished').glob('*.md')))}/{len(units)}",
        text,
        count=1,
    )
    additions = [
        "- 精校分章：`chapters_polished/`。",
        "- 合并精校版：`00-全书精校版.md`。",
        "- 英文好句摘要：`03-英文好句摘要与译法.md`。",
    ]
    for line in additions:
        if line not in text:
            text += "\n" + line
    write_text(readme, text)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Polish Game Design Tools translation against source chunks.")
    parser.add_argument("--pdf", required=True)
    parser.add_argument("--root", required=True)
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--max-completion-tokens", type=int, default=16000)
    parser.add_argument("--source-chunk-chars", type=int, default=2600)
    parser.add_argument("--group-chars", type=int, default=11000)
    parser.add_argument("--start-order", type=int, default=1)
    parser.add_argument("--max-units", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-good-sentences", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(args.root).resolve()
    pdf = Path(args.pdf).resolve()
    doc = fitz.open(pdf)
    units = build_units(doc)
    figures = extract_figures(root, doc, units, force=False)
    selected = [unit for unit in units if unit.number >= args.start_order]
    if args.max_units:
        selected = selected[: args.max_units]

    results: list[dict] = []
    for unit in selected:
        results.append(
            polish_unit(
                root=root,
                unit=unit,
                figures=figures,
                model=args.model,
                timeout=args.timeout,
                max_completion_tokens=args.max_completion_tokens,
                source_chunk_chars=args.source_chunk_chars,
                group_chars=args.group_chars,
                force=args.force,
            )
        )
        regenerate_combined(root)
        write_quality_report(root, units, results)
        update_readme(root, units)

    regenerate_combined(root)
    if not args.skip_good_sentences:
        build_good_sentence_notes(root, args.model, args.timeout, args.max_completion_tokens)
    write_quality_report(root, units, results)
    update_readme(root, units)
    print(f"Done polishing: {root}", flush=True)


if __name__ == "__main__":
    main()
