#!/usr/bin/env python3
"""Validate JSON manifests in this repo."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ax402"

REQUIRED = [
    ROOT / ".cursor-plugin" / "marketplace.json",
    ROOT / ".claude-plugin" / "marketplace.json",
    ROOT / ".grok-plugin" / "marketplace.json",
    ROOT / ".agents" / "plugins" / "marketplace.json",
    ROOT / ".mcp.json",
    PLUGIN / "plugin.json",
    PLUGIN / "mcp.json",
    PLUGIN / ".mcp.json",
    PLUGIN / ".cursor-plugin" / "plugin.json",
    PLUGIN / ".claude-plugin" / "plugin.json",
    PLUGIN / ".grok-plugin" / "plugin.json",
    PLUGIN / ".codex-plugin" / "plugin.json",
]


def main() -> int:
    errors = 0
    for path in REQUIRED:
        if not path.is_file():
            print(f"missing {path.relative_to(ROOT)}", file=sys.stderr)
            errors += 1
            continue
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            print(f"invalid JSON {path.relative_to(ROOT)}: {exc}", file=sys.stderr)
            errors += 1
            continue
        if not isinstance(data, dict):
            print(f"not an object {path.relative_to(ROOT)}", file=sys.stderr)
            errors += 1

    skill = PLUGIN / "skills" / "ax402" / "SKILL.md"
    if not skill.is_file():
        print("missing skills/ax402/SKILL.md", file=sys.stderr)
        errors += 1

    logo = PLUGIN / "assets" / "logo.svg"
    if not logo.is_file():
        print("missing assets/logo.svg", file=sys.stderr)
        errors += 1

    if errors:
        print(f"{errors} error(s)", file=sys.stderr)
        return 1
    print(f"ok ({len(REQUIRED)} json files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
