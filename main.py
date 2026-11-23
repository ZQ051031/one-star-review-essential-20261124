"""One-star review of something essential: gravity.

Writes a single deadpan one-star review, at most 160 characters,
to /output/entry.txt. Standard library only, no network.
"""

import os

REVIEW = (
    "Gravity: works around the clock, never takes a day off, "
    "and still drops my phone face-down every time. One star."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")


if __name__ == "__main__":
    main()
