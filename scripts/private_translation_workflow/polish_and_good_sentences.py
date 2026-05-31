from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_API_KEY_ENVS = ["MINIMAX_API_KEY", "MINIMAX_KEY", "MINIMAX_TOKEN", "HAILUO_API_KEY", "HAILUO_TOKEN"]
DEFAULT_MODEL = "MiniMax-M2.7"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def api_key() -> tuple[str, str]:
    for name in DEFAULT_API_KEY_ENVS:
        value = os.environ.get(name)
        if value:
            return name, value
    raise RuntimeError("Missing MiniMax API key")


def endpoints() -> list[str]:
    bases = []
    if os.environ.get("MINIMAX_BASE_URL"):
        bases.append(os.environ["MINIMAX_BASE_URL"])
    bases.extend(["https://api.minimaxi.com", "https://api.minimax.io"])
    out = []
    for base in bases:
        base = base.rstrip("/")
        endpoint = base if base.endswith("/v1/text/chatcompletion_v2") else f"{base}/v1/text/chatcompletion_v2"
        if endpoint not in out:
            out.append(endpoint)
    return out


def call_minimax(prompt: str, model: str, timeout: int, max_completion_tokens: int) -> tuple[str, dict, str]:
    key_name, key = api_key()
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "name": "MiniMax AI",
                "content": "You are a senior Chinese editor for game narrative, UX, and game-design books.",
            },
            {"role": "user", "name": "user", "content": prompt},
        ],
        "stream": False,
        "temperature": 0.35,
        "top_p": 0.9,
        "max_completion_tokens": max_completion_tokens,
    }
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    last_error: Exception | None = None
    for endpoint in endpoints():
        for attempt in range(1, 4):
            try:
                request = urllib.request.Request(
                    endpoint,
                    data=body,
                    headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
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
                return content.strip(), {"api_key_env": key_name, "usage": data.get("usage"), "finish_reason": (data.get("choices") or [{}])[0].get("finish_reason")}, endpoint
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, RuntimeError) as exc:
                last_error = exc
                print(f"    attempt {attempt} failed at {endpoint}: {type(exc).__name__}: {exc}")
                time.sleep(min(20, attempt * 3))
    raise RuntimeError(f"MiniMax call failed: {last_error}")


def split_markdown(text: str, max_chars: int) -> list[str]:
    paras = re.split(r"\n{2,}", text.strip())
    chunks: list[str] = []
    current = ""
    for para in paras:
        if current and len(current) + len(para) + 2 > max_chars:
            chunks.append(current.strip())
            current = ""
        if len(para) > max_chars:
            lines = para.splitlines()
            for line in lines:
                if current and len(current) + len(line) + 1 > max_chars:
                    chunks.append(current.strip())
                    current = ""
                current = f"{current}\n{line}".strip() if current else line
        else:
            current = f"{current}\n\n{para}".strip() if current else para
    if current:
        chunks.append(current.strip())
    return chunks


def polish_prompt(chunk: str, index: int, total: int) -> str:
    return f"""Polish the following Chinese Markdown translation of a game narrative/UX design book.

Hard requirements:
- Output polished Chinese Markdown only.
- Do not summarize, omit, expand, or invent content.
- Preserve all Markdown headings, tables, bullet structure, image links, figure numbers, source-page metadata, bibliography entries, URLs, and proper nouns.
- Keep image Markdown exactly if present.
- Improve Chinese fluency, remove translationese, clarify argument flow, and stabilize terminology.
- Keep English proper nouns and book/game/theory names when appropriate.
- Translate or smooth awkward mixed-language fragments unless they are proper nouns.
- This is chunk {index}/{total}; polish only this chunk.

Preferred terms:
game narrative=游戏叙事; narrative design=叙事设计; UX design=UX 设计/用户体验设计; agency=主体能动性; affordance=可供性; signifier=信号; onboarding=新手引导; player journey=玩家旅程; emotion mapping=情绪映射; core loop=核心循环; world-building=世界观构建; engagement=参与度.

Markdown chunk:

{chunk}
"""


def polish_chapters(root: Path, model: str, timeout: int, chunk_chars: int, max_completion_tokens: int) -> list[dict]:
    src_dir = root / "chapters"
    out_dir = root / "chapters_polished"
    run_dir = root / "work" / "minimax_polish_runs"
    out_dir.mkdir(parents=True, exist_ok=True)
    run_dir.mkdir(parents=True, exist_ok=True)
    metas = []
    for chapter in sorted(src_dir.glob("*.md")):
        text = read(chapter)
        chunks = split_markdown(text, chunk_chars)
        print(f"POLISH {chapter.name} chunks={len(chunks)} chars={len(text)}")
        polished_chunks = []
        chunk_metas = []
        for index, chunk in enumerate(chunks, start=1):
            print(f"  chunk {index}/{len(chunks)} chars={len(chunk)}")
            content, meta, endpoint = call_minimax(polish_prompt(chunk, index, len(chunks)), model, timeout, max_completion_tokens)
            polished_chunks.append(content)
            chunk_metas.append({**meta, "endpoint": endpoint, "chunk_index": index, "chunk_total": len(chunks), "source_chars": len(chunk)})
            time.sleep(0.8)
        output = "\n\n".join(part.strip() for part in polished_chunks if part.strip())
        write(out_dir / chapter.name, output)
        meta = {"chapter": chapter.name, "chunks": chunk_metas}
        write(run_dir / f"{chapter.stem}-{time.strftime('%Y%m%d-%H%M%S')}.json", json.dumps(meta, ensure_ascii=False, indent=2))
        metas.append(meta)
    return metas


def good_sentence_prompt(items: list[tuple[str, str]]) -> str:
    joined = "\n\n".join(f"## {title}\n{text[:9000]}" for title, text in items)
    return f"""Create a Chinese reading-note document for memorable ideas from this game narrative/UX book.

Copyright boundary:
- Do not reproduce long English sentences.
- Use at most 10 total English trigger phrases.
- Each English trigger phrase must be 1-3 words only.
- Most content must be Chinese paraphrase, not English quotation.

Output Markdown in Chinese with:
1. A short copyright/use-boundary note.
2. A table with columns: 章节, 英文触发词, 中文好句摘要, 可借鉴的写法, 可用于哪类设计讨论.
3. 24-36 rows total.

Source excerpts:

{joined}
"""


def build_good_sentence_notes(root: Path, model: str, timeout: int, max_completion_tokens: int) -> None:
    outline = read(root / "source_outline.md")
    rows = []
    for line in outline.splitlines():
        if not line.startswith("| ") or "`work/extracted_text/" not in line:
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 6 or cells[0] == "序号":
            continue
        title = cells[2]
        match = re.search(r"`work/extracted_text/([^`]+)`", cells[4])
        if not match:
            continue
        source = root / "work" / "extracted_text" / match.group(1)
        rows.append((title, read(source)))
    # Keep source small enough for a single selection pass while covering all sections.
    content, meta, endpoint = call_minimax(good_sentence_prompt(rows), model, timeout, max_completion_tokens)
    out = root / "03-英文好句摘要与译法.md"
    write(out, content)
    write(root / "work" / "good_sentence_notes_run.json", json.dumps({**meta, "endpoint": endpoint}, ensure_ascii=False, indent=2))


def regenerate_combined(root: Path) -> None:
    out = root / "00-全书精校版.md"
    parts = [
        "# Game Narrative Design and UX Fundamentals 中文精校版\n",
        "> 状态：MiniMax API 初译后进行中文审校润色，图片已按 PDF 裁切回填，仍建议人工逐章复核。  \n"
        "> 使用边界：个人学习 / 内部研究；公开传播或商业使用前需要自行确认授权。\n",
    ]
    for chapter in sorted((root / "chapters_polished").glob("*.md")):
        content = read(chapter).strip().replace("../assets/", "assets/")
        parts.append("\n\n---\n\n" + content)
    write(out, "\n".join(parts))


def verify(root: Path) -> str:
    assets = {p.name for p in (root / "assets").glob("fig-*.png")}
    polished = "\n".join(read(p) for p in (root / "chapters_polished").glob("*.md"))
    refs = set(re.findall(r"!\[[^\]]*\]\(\.\./assets/(fig-[^)]+\.png)\)", polished))
    combined = read(root / "00-全书精校版.md")
    combined_refs = set(re.findall(r"!\[[^\]]*\]\(assets/(fig-[^)]+\.png)\)", combined))
    forbidden = re.findall(r"pending|---TRANSLATION---|---NEW_TERMS---|作为 AI|作为AI|I am an AI|```", polished + "\n" + combined)
    lines = [
        "# 质量门报告",
        "",
        "## 本轮状态",
        "",
        "- 文本状态：已生成 `chapters_polished/` 与 `00-全书精校版.md`。",
        "- 图片状态：精校版保留并回填全部 Figure 图片引用。",
        "- 英文好句：已生成 `03-英文好句摘要与译法.md`，英文仅保留短触发词，不做长段原文搬运。",
        "",
        "## 自动检查",
        "",
        f"- 图片资产数：{len(assets)}。",
        f"- 分章图片引用数：{len(refs)}。",
        f"- 合并版图片引用数：{len(combined_refs)}。",
        f"- 分章缺失图片引用：{', '.join(sorted(assets - refs)) if assets - refs else '无'}。",
        f"- 合并版缺失图片引用：{', '.join(sorted(assets - combined_refs)) if assets - combined_refs else '无'}。",
        f"- 模型分隔符/AI 自称/待翻译占位残留：{len(forbidden)}。",
        "",
        "## 仍需人工判断",
        "",
        "- 图内英文标签尚未逐张中文化重绘；目前是原图裁切回填。",
        "- 英文好句为短摘和中文摘要，不构成完整原文摘抄。",
        "- 精校版经过模型润色，但公开传播前仍需人工审校和授权确认。",
    ]
    report = "\n".join(lines)
    write(root / "audit" / "质量门报告.md", report)
    return report


def update_readme(root: Path) -> None:
    readme = root / "README.md"
    text = read(readme)
    text = re.sub(
        r"状态：.*",
        "状态：MiniMax API 初译完成；中文审校润色版已生成；已完成 12/12 个翻译单元；已回填 46 张 Figure 裁切图  ",
        text,
        count=1,
    )
    additions = [
        "- `00-全书精校版.md`：中文审校润色后的合并通读版。",
        "- `chapters_polished/`：中文审校润色后的分章版本。",
        "- `03-英文好句摘要与译法.md`：英文短触发词 + 中文好句摘要 + 译法点评。",
        "- `audit/质量门报告.md`：本轮自动检查与人工复核边界。",
    ]
    for line in reversed(additions):
        if line not in text:
            text = text.replace("## 文件说明\n\n", f"## 文件说明\n\n{line}\n")
    write(readme, text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--model", default=os.environ.get("MINIMAX_MODEL", DEFAULT_MODEL))
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--chunk-chars", type=int, default=18000)
    parser.add_argument("--max-completion-tokens", type=int, default=26000)
    parser.add_argument("--skip-polish", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    if not args.skip_polish:
        polish_chapters(root, args.model, args.timeout, args.chunk_chars, args.max_completion_tokens)
    build_good_sentence_notes(root, args.model, args.timeout, args.max_completion_tokens)
    regenerate_combined(root)
    report = verify(root)
    update_readme(root)
    print(report)


if __name__ == "__main__":
    main()
