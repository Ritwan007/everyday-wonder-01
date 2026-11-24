#!/usr/bin/env python3
"""Everyday Wonder entry: writes the winning sentence to /output/entry.txt,
then reads it back and verifies byte-identity, a single sentence, and the
1-200 character gate."""

import os
import sys

SENTENCE = "The ceiling fan's shadow turns on the wall a fraction slower than the fan itself, like a memory arriving late."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(SENTENCE)

    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()

    text = raw.decode("utf-8")
    if text.encode("utf-8") != raw:
        print("FAIL: output is not byte-identical UTF-8", file=sys.stderr)
        return 1
    if text != SENTENCE:
        print("FAIL: output differs from the entry sentence", file=sys.stderr)
        return 1
    if not text.strip():
        print("FAIL: output is only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 200:
        print(f"FAIL: length {len(text)} outside 1-200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("FAIL: output is not a single sentence", file=sys.stderr)
        return 1
    print(f"OK: {len(text)} chars, single sentence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
