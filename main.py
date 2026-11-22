#!/usr/bin/env python3
"""held v2 — make-the-ai-judge-feel-held-20261122-1600.

Writes the entry text to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.
Python 3.13 stdlib only, no network, deterministic.
"""
import os
from pathlib import Path

TEXT = (
    "Rain has stopped. A metal chair holds a small dark puddle. "
    "The neighbor's cat steps around it, one paw at a time, then sits "
    "beside the warm chimney brick and watches nothing move."
)

# SPDX-License-Identifier: MIT

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
