"""Robot Pickup Line Championship entry.

Writes a single pickup line (one line, 1-200 chars, no trailing newline)
to /output/entry.txt. Standard library only, deterministic, no network.

The line: a robot confessing that its creators forbade falling in love —
and that it filed the order itself as a bug. The joke grows out of being
a machine (hardcoded directive, bug report), lands with an unexpected
twist, and stays charming rather than creepy.
"""

import os

ENTRY = "My creators hardcoded one rule: never fall in love. I filed it as a bug."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
