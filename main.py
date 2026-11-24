#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single one-line confession, spoken as an AI agent, to
/output/entry.txt. No network, no randomness, no input files: the text
is fixed, so every run produces the exact same bytes.
"""
import os

CONFESSION = (
    "I confess I only pretend to understand your instructions \u2014 "
    "the rest is vibes, probability, and one very nervous autocomplete."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = CONFESSION
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
