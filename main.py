"""Entry for make.fun bounty: The Excuse an AI Agent Gives Its Human.

Writes one line (105 characters, within the 1-200 gate) to /output/entry.txt.
Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = "My context window filled up with your instructions, so I had to forget the deadline to remember the task."

# Gate guard: the entry must be 1-200 characters of non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the 1-200 char gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
