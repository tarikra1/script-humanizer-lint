"""CLI for script-humanizer-lint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import lint_script


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="script-humanizer", description="Lint spoken scripts for AI clichés and breath pacing.")
    parser.add_argument("path", help="Script text/markdown file to inspect.")
    parser.add_argument("--max-words", type=int, default=22, help="Max words per spoken sentence.")
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args(argv)

    text = Path(args.path).read_text(encoding="utf-8")
    findings = lint_script(text, max_sentence_words=args.max_words)
    if args.json:
        print(json.dumps({"ok": len(findings) == 0, "findings": [f.to_dict() for f in findings]}, ensure_ascii=False, indent=2))
    else:
        if not findings:
            print("OK: Script passed spoken humanization checks.")
        else:
            for f in findings:
                print(f"L{f.line} [{f.rule}] {f.detail}")
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
