#!/usr/bin/env python3
"""One Line, One Laugh - entry program.

Writes a single original funny line to <output>/entry.txt.
Standard library only; no dependencies, no network, no input files.
"""

import os
import sys

# The line: buying health gear, then defeating its purpose in one move.
# Setup ("bought a standing desk to get healthier") promises virtue;
# the turn ("sit on a taller chair") keeps the purchase and drops the point.
LINE = "I bought a standing desk to get healthier; now I just sit on a taller chair."


def main() -> int:
    chars = len(LINE)
    if chars < 1 or chars > 200:
        print(f"Line must be 1-200 characters, got {chars}.", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("Line must not be only whitespace.", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
