#!/usr/bin/env python3
"""One Star, Written in Sap — entry writer.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.
Gate: UTF-8 text, 1-279 characters, not only whitespace.
No network, no randomness, no files read: the text is fixed below.
"""

import os
import sys

REVIEW = (
    "One star. Gary watered me with flat Diet Coke for six months, "
    "then blamed my brown leaves on 'bad vibes' and moved me to "
    "the bathroom with no window."
)


def main() -> int:
    text = REVIEW.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 279:
        print(f"entry too long: {len(text)} chars", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
