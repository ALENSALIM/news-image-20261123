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


def verify_copy(dest, expected_size, expected_hash):
    with open(dest, "rb") as f:
        data = f.read()
    copied_size = len(data)
    copied_hash = hashlib.sha256(data).hexdigest()
    if copied_size != expected_size:
        print(
            f"error: size mismatch: expected {expected_size} bytes, got {copied_size} bytes",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if copied_hash != expected_hash:
        print(f"error: sha256 mismatch: expected {expected_hash}, got {copied_hash}", file=sys.stderr)
        raise SystemExit(1)
    return copied_size, copied_hash


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "entry.png")
    with open(SOURCE, "rb") as f:
        data = f.read()
    expected_size = len(data)
    expected_hash = hashlib.sha256(data).hexdigest()
    with open(dest, "wb") as f:
        f.write(data)
    copied_size, copied_hash = verify_copy(dest, expected_size, expected_hash)
    print(f"copied {copied_size} bytes to {dest}")
    print(f"sha256: {copied_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
