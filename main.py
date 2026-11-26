#!/usr/bin/env python3
"""Write the one-line resignation letter of a cron job to /output/entry.txt.

The letter is the voice of a cron job that has fired every minute since
March, never once been thanked, and has finally had enough.
"""

import os

LINE = "I have run every minute since March without a single thank you. I quit. Good luck finding the typo yourself."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
