#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261125.

Copies the bundled front-page image (entry.png) to the output directory.
Standard library only; no network access; deterministic: the same bytes
are written on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard against a truncated copy: the output must be byte-identical
    # to the bundled image, otherwise the run is not deterministic.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        print("error: copied file size differs from bundled entry.png",
              file=sys.stderr)
        return 1
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
