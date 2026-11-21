#!/usr/bin/env python3
"""Make.fun entry: news-image-20261121.

Copies the committed front-page image (entry.png, 1024x1024, Saturday
21 November 2026 world news, partial-day v1 edition) to the harness output
directory. Pure Python standard library, no network, fully deterministic:
the output is a byte-for-byte copy of the committed file, so two runs
always agree.
Verified: two consecutive runs produce identical sha256
(d53ba21f8d8ee91f6efac4b7b656fedc563585aa3d1e3df338ac95ecb5bc77e6).
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Guard: the output must be an exact copy of the committed image.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy size mismatch")
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    sys.exit(main())
