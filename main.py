"""Your Week in One Line — entry writer.

Writes the locked one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(with /output fallback). Stdlib only, deterministic, no trailing newline.
"""

import os

ENTRY = "This week: 252 contests, two wins, GTA 6 slid from #772 to #5,006 \u2014 the judge kept the receipt."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
