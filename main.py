#!/usr/bin/env python3
"""Ship It Friday: the funniest one-line git commit message an AI coding
agent writes right before breaking production on a Friday.

Writes the commit message to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "feat: rewrote auth in one pass, deleted the old login just in case, "
    "all 400 tests green \u2014 merging at 4:59pm Friday, "
    "what could possibly go wrong"
)


def main():
    # Gate: entry.txt must be UTF-8, 1-159 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 159, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
