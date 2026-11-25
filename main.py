"""One Line of Earned Pride.

Writes a single original line of text to /output/entry.txt:
a quiet, earned moment of pride for a real person in a concrete
scene. Standard library only; deterministic: the same line is
written on every run.
"""

import os
import sys

LINE = (
    "After eleven failed batches, Mara finally pulled a loaf from the "
    "oven that sang when she tapped its crust, and she just stood "
    "there, flour on her cheek, listening."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Self-checks against the competition gate: UTF-8 text, 1 to 240
    # characters, not only whitespace, and a single line.
    if not (1 <= len(LINE) <= 240):
        print(f"entry is {len(LINE)} characters, must be 1-240", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    LINE.encode("utf-8")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {OUTPUT_PATH}")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
