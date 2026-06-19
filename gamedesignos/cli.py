"""Command-line interface for the GameDesignOS v0.9 local runtime."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence

from .constants import ASSET_SPECS, RUNTIME_VERSION
from .errors import EXIT_INCOMPATIBLE_VERSION, EXIT_OK, EXIT_VALIDATION, GameDesignOSError, UsageError
from .routing import route_task, router_source
from .voi import create_assessment, review_assessment
from .workspace import Workspace, doctor, init_workspace


def _path(value: str | None) -> Path | None:
    return Path(value).expanduser() if value else None


def _emit(data: Any, *, as_json: bool, text: str) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2) if as_json else text)


def _workspace(args: argparse.Namespace) -> Workspace:
    return Workspace.open(_path(getattr(args, "workspace", None)))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="gamedesignos",
        description="Local deterministic GameDesignOS runtime. No model calls, API keys, uploads, or Human Gate decisions.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {RUNTIME_VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("init", help="Create a workspace")
    p.add_argument("project_name")
    p.add_argument("--destination")
    p.add_argument("--codename")
    p.add_argument("--visibility", default="private", choices=["private", "public-synthetic", "public-cleared"])
    p.add_argument("--owner", default="designer")
    p.add_argument("--force", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--json", action="store_true")

    for name, help_text in (("status", "Summarize workspace state"), ("validate", "Validate a workspace"), ("doctor", "Diagnose runtime readiness")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--workspace")
        if name == "validate":
            p.add_argument("--repo-root")
        p.add_argument("--json", action="store_true")

    p = sub.add_parser("route", help="Recommend the smallest suitable skill")
    p.add_argument("task", nargs="+")
    p.add_argument("--workspace")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("new", help="Create and register an asset stub")
    p.add_argument("asset_type", choices=sorted(ASSET_SPECS))
    p.add_argument("--title")
    p.add_argument("--filename")
    p.add_argument("--created-by", default="human-agent", choices=["human", "agent", "human-agent", "import"])
    p.add_argument("--source-status", choices=["private", "synthetic", "public", "cleared", "needs_review"])
    p.add_argument("--workspace")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("voi", help="Create or review a Decision-to-Information gate")
    p.add_argument("decision_id", nargs="?")
    p.add_argument("--input")
    p.add_argument("--write", action="store_true")
    p.add_argument("--decision", dest="decision_question")
    p.add_argument("--default-action")
    p.add_argument("--option", action="append", default=[])
    p.add_argument("--owner")
    p.add_argument("--deadline")
    p.add_argument("--stakes", default="medium", choices=["low", "medium", "high", "critical"])
    p.add_argument("--reversibility", default="reversible", choices=["reversible", "costly_to_reverse", "irreversible"])
    p.add_argument("--boundary", default="undefined", choices=["undefined", "far", "near", "locked"])
    p.add_argument("--candidate-info", action="append", default=[])
    p.add_argument("--stop-when", action="append", default=[])
    p.add_argument("--output")
    p.add_argument("--workspace")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--json", action="store_true")

    p = sub.add_parser("pack", help="Create a review-safe bundle")
    p.add_argument("--mode", default="internal-review", choices=["internal-review", "publisher", "public-synthetic"])
    p.add_argument("--output")
    p.add_argument("--workspace")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    p.add_argument("--json", action="store_true")
    return parser


def _run(args: argparse.Namespace) -> int:
    if args.command == "init":
        destination = _path(args.destination) or (Path.cwd() / args.project_name)
        result = init_workspace(
            project_name=args.project_name,
            destination=destination,
            codename=args.codename,
            visibility=args.visibility,
            owner=args.owner,
            force=args.force,
            dry_run=args.dry_run,
        )
        text = f"{'Would create' if args.dry_run else 'Created'} workspace: {result['workspace']}\nProject ID: {result['project_id']}"
        if not args.dry_run:
            text += "\nNext: review game.designos.yaml, define a Decision Object, then run `gamedesignos route <task>`."
        _emit(result, as_json=args.json, text=text)
        return EXIT_OK

    if args.command == "status":
        status = _workspace(args).status()
        text = (
            f"{status.title} [{status.project_id}]\nStatus: {status.project_status} | Visibility: {status.visibility}\n"
            f"Workspace schema: {status.workspace_schema_version} | Declared runtime: {status.runtime_version_declared} | Current CLI: {status.runtime_version_current}\n"
            f"Assets: {sum(status.asset_counts_by_type.values())} | Accepted decisions: {status.accepted_decisions} | Open Human Gates: {status.unresolved_human_gates}\n"
            f"Compatibility: {'OK' if status.compatible else 'FAILED'}"
        )
        _emit(status.as_dict(), as_json=args.json, text=text)
        return EXIT_OK if status.compatible else EXIT_INCOMPATIBLE_VERSION

    if args.command == "route":
        workspace = _workspace(args) if args.workspace else None
        if not args.workspace:
            try:
                workspace = Workspace.open()
            except GameDesignOSError:
                pass
        result = route_task(" ".join(args.task), workspace=workspace)
        result["router_source"] = router_source(workspace)
        selected = result.get("selected_skill") or "no stable route"
        text = f"Route: {selected}"
        if result.get("target_skill") and result["target_skill"] != selected:
            text += f" -> then {result['target_skill']}"
        text += f"\nReason: {result['reason']}"
        if result.get("missing_upstream"):
            text += "\nMissing upstream: " + ", ".join(result["missing_upstream"])
        text += "\nThis command recommends a route; it does not execute a skill."
        _emit(result, as_json=args.json, text=text)
        return EXIT_OK

    if args.command == "new":
        result = _workspace(args).create_asset(
            args.asset_type,
            title=args.title,
            filename=args.filename,
            created_by=args.created_by,
            source_status=args.source_status,
            dry_run=args.dry_run,
        )
        _emit(result, as_json=args.json, text=f"{'Would create' if args.dry_run else 'Created'} {args.asset_type}: {result['asset']['asset_id']}\nPath: {result['asset']['path']}")
        return EXIT_OK

    if args.command == "validate":
        report = _workspace(args).validate(repo_root=_path(args.repo_root))
        text = "Workspace validation passed." if report.ok else "Workspace validation failed:\n- " + "\n- ".join(report.errors)
        if report.warnings:
            text += "\nWarnings:\n- " + "\n- ".join(report.warnings)
        _emit(report.as_dict(), as_json=args.json, text=text)
        incompatible = any("Unsupported workspace schema" in item or "incompatible with runtime" in item for item in report.errors)
        return EXIT_OK if report.ok else (EXIT_INCOMPATIBLE_VERSION if incompatible else EXIT_VALIDATION)

    if args.command == "voi":
        if args.input:
            input_path = Path(args.input).expanduser()
            if not input_path.is_absolute() and args.workspace:
                input_path = Path(args.workspace).expanduser() / input_path
            result = review_assessment(input_path, write=args.write)
            text = "VOI assessment review passed." if result["ok"] else "VOI assessment review failed:\n- " + "\n- ".join(result["errors"])
            if result["recommendations"]:
                text += "\nRecommendations:\n- " + "\n- ".join(result["recommendations"])
            _emit(result, as_json=args.json, text=text)
            return EXIT_OK if result["ok"] else EXIT_VALIDATION
        required = {"decision_id": args.decision_id, "decision": args.decision_question, "default action": args.default_action, "owner": args.owner}
        missing = [name for name, value in required.items() if not value]
        if missing:
            raise UsageError("Missing VOI fields: " + ", ".join(missing))
        result = create_assessment(
            _workspace(args),
            decision_id=args.decision_id,
            decision_question=args.decision_question,
            options=args.option,
            current_default_action=args.default_action,
            owner=args.owner,
            deadline=args.deadline,
            stakes=args.stakes,
            reversibility=args.reversibility,
            boundary=args.boundary,
            candidate_information_actions=args.candidate_info,
            stop_when=args.stop_when or None,
            output=_path(args.output),
            dry_run=args.dry_run,
        )
        _emit(result, as_json=args.json, text=f"{'Would create' if args.dry_run else 'Created'} VOI assessment: {result['path']}\n{result['next_action']}")
        return EXIT_OK

    if args.command == "pack":
        result = _workspace(args).pack(mode=args.mode, output=_path(args.output), dry_run=args.dry_run, force=args.force)
        _emit(result, as_json=args.json, text=f"{'Would create' if args.dry_run else 'Created'} pack: {result['output']}\nIncluded assets: {len(result['included_assets'])}")
        return EXIT_OK

    if args.command == "doctor":
        result = doctor(_path(args.workspace))
        lines = [f"GameDesignOS runtime {result['runtime_version']}"] + [f"{'OK' if item['ok'] else 'FAIL'} {item['name']}: {item['detail']}" for item in result["checks"]]
        _emit(result, as_json=args.json, text="\n".join(lines))
        return EXIT_OK if result["ok"] else EXIT_VALIDATION
    raise UsageError(f"Unknown command: {args.command}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    try:
        return _run(parser.parse_args(argv))
    except GameDesignOSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.exit_code
    except KeyboardInterrupt:
        print("error: interrupted", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
