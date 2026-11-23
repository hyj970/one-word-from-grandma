"""One Word From Grandma — make.fun bounty entry.

The single word a grandma would text about AI.
"""

import os

WORD = "THINGAMAJIG"


def output_path() -> str:
    """Resolve the entry file path from $MAKEFUN_OUTPUT_DIR (default /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
