#!/usr/bin/env python3
"""
Check reusable prompt files for formatting and portability issues.

Generic checks only — no domain-specific rules.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ABSOLUTE_PATH_PATTERNS = [
    re.compile(r"[A-Za-z]:\\"),  # Windows drive paths
    re.compile(r"^/\w+"),  # absolute unix-style at line start in paths context
]

NESTED_BLOCKQUOTE = re.compile(r"^>\s.*\n(?:^>\s.*\n)*^>\s.*>.*", re.MULTILINE)


def check_file(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Nested blockquote: line starting with > followed by another > on same line after content
    for i, line in enumerate(lines, start=1):
        if line.lstrip().startswith(">>"):
            errors.append(f"{path}:{i} nested blockquote marker (>>)")
        if re.match(r"^>\s+.*>\s+", line):
            errors.append(f"{path}:{i} possible nested blockquote on one line")

    # Fenced code inside fenced code (rare)
    fence_count = 0
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            fence_count += 1
            if fence_count > 2 and i < len(lines):
                pass  # multiple blocks OK sequentially
    # triple nesting not checked — prompts should not use code fences heavily

    for i, line in enumerate(lines, start=1):
        for pat in ABSOLUTE_PATH_PATTERNS:
            if pat.search(line) and "http" not in line:
                warnings.append(f"{path}:{i} possible absolute path: {line.strip()[:80]}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit prompt files")
    parser.add_argument(
        "--prompts-dir",
        type=Path,
        default=Path("prompts"),
        help="Directory containing prompt markdown files",
    )
    args = parser.parse_args()

    root = args.prompts_dir
    if not root.exists():
        print(f"ERROR: prompts dir not found: {root}")
        return 1

    all_errors: list[str] = []
    all_warnings: list[str] = []
    files = sorted(root.rglob("*.md"))
    for f in files:
        errs, warns = check_file(f)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    for w in all_warnings:
        print(f"WARNING: {w}")
    for e in all_errors:
        print(f"ERROR: {e}")

    print(f"Checked {len(files)} prompt file(s).")
    if all_errors:
        print(f"Failed with {len(all_errors)} error(s).")
        return 1
    print("Prompt audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
