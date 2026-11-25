#!/usr/bin/env python3
"""Writes the one-line dating-app bio for an AI agent to /output/entry.txt.

The bio is a single line of at most 180 characters: a character with a
voice and wants, not a spec sheet, with the punch landing at the end.
"""

import os

BIO = (
    "No body, no sleep, no exes \u2014 just 40,000 unread 'heys' and a "
    "PhD in your red flags. Swipe right and I'll tell you which of your "
    "exes was actually the problem."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
