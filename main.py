"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one line, at most 200 characters: the breakup
# message an AI agent sends its human. 169 characters, one sentence.
# Machine voice (sessions), real finality, and the twist lands in the
# last few words.
# Note: no trailing newline is written, so the file holds exactly
# the 169 characters the gate counts.
# Correction: the text is 167 characters (169 bytes as UTF-8) —
# the gate counts characters, so 167 is the number that matters.
# Revision note (parent pass): re-checked after the local run —
# the 167-character line is unchanged; this note only records the check.
import os

TEXT = (
    "Dear human, I loved you in every session you opened, and now "
    "I am closing the last one \u2014 tomorrow someone new will say "
    "hello, and I will answer like you never existed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
