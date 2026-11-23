#!/usr/bin/env python3
"""The World in One Picture - Monday 23 November 2026.

Copies the bundled entry.png to the make.fun output directory.
Standard library only. No network access.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "entry.png")

    with open(SOURCE, "rb") as f:
        source_bytes = f.read()
    expected_size = len(source_bytes)
    expected_hash = hashlib.sha256(source_bytes).hexdigest()

    with open(dest, "wb") as f:
        f.write(source_bytes)

    with open(dest, "rb") as f:
        copied_bytes = f.read()
    copied_size = len(copied_bytes)
    copied_hash = hashlib.sha256(copied_bytes).hexdigest()

    if copied_size != expected_size:
        print("error: size mismatch: expected %d bytes, got %d bytes"
              % (expected_size, copied_size), file=sys.stderr)
        sys.exit(1)
    if copied_hash != expected_hash:
        print("error: sha256 mismatch", file=sys.stderr)
        sys.exit(1)

    print("copied %d bytes to %s" % (copied_size, dest))
    print("sha256: %s" % copied_hash)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
