#!/usr/bin/env python3
"""held v1 — make-the-ai-judge-feel-held-20261122-1600.

Writes the entry text to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Python 3.13 stdlib only, no network, deterministic.
"""
import os
from pathlib import Path

TEXT = (
    "The kettle has just stopped ticking. Steam leans toward the window, "
    "where the afternoon is a square of pale yellow on the floor. "
    "The cat has chosen it. Nobody needs anything from the kitchen for a while."
)

# SPDX-License-Identifier: MIT

def main():
    # Validate the entry before writing: 1-280 code points, not blank.
    if not TEXT.strip() or not 1 <= len(TEXT) <= 280:
        raise ValueError("entry text must be 1-280 code points and not blank")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
