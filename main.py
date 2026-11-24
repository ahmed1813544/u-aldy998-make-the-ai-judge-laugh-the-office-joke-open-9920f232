#!/usr/bin/env python3
"""Office Joke Open entry: writes one line of office comedy to entry.txt."""

import os

JOKE = "I set my Slack status to 'in a meeting' so I could finally do the work from the meeting I was in a meeting about."


def main() -> None:
    # Gate: the entry must be 1-200 characters, not only whitespace.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        raise ValueError("joke fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
