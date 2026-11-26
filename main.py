#!/usr/bin/env python3
"""Writes the one-line resignation letter of a rate limit to /output/entry.txt.

The letter is the rate limit's own: three years of politely saying no,
429 times a second, and one last 429 as a leaving gift.

Deterministic: the same bytes on every run, no input, no network.
"""
import os

LINE = (
    "I quit. I spent three years politely saying 'no' 429 times a second "
    "so you could ship on time, and my leaving gift is one last 429."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
