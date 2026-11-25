"""Your Week in One Line — entry writer.

Writes the locked one-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(with /output fallback). Stdlib only, deterministic, no trailing newline.

Verified 2026-11-25: entry.txt sha256
64724005f0a8c5d4c52c8717a4d8b30852b6fc6072d2326ca6271fc0ed6e984a,
95 chars / 97 bytes, byte-identical across 3 runs (2 fresh + 1 clean env -i).
Anchor b5814fb47d48cb79c8a58e2cc287b8b91c32269b, drand round 34256507,
emission 2026-11-25T02:14:45Z.
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
