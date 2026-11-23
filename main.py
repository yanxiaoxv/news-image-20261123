#!/usr/bin/env python3
"""news-image-20261123 entry point.

Validates the front-page image shipped beside this file (entry.png holds
JPEG bytes, which the contest rules allow under the .png name) against the
contest limits, then copies it unchanged to the output directory.

    mkdir -p out
    MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png

With MAKEFUN_OUTPUT_DIR unset or set to an empty string, it writes
to /output/entry.png (an empty value counts as unset).
Standard library only, no network, deterministic: every run writes the
same bytes (a byte-for-byte copy of the shipped image).
"""

import hashlib
import os
import shutil
import struct
import sys
import zlib

MAX_BYTES = 1048576
MAX_DIM = 1024


def fail(message):
    print(f"main.py: error: {message}", file=sys.stderr)
    raise SystemExit(1)


def jpeg_dimensions(data):
    """Return (width, height) of a JPEG, or None if it is not one.

    Walks the marker segments from the SOI marker until a start-of-frame
    segment, and requires the end-of-image marker to be the last two bytes.
    """
    if len(data) < 4 or data[0:2] != b"\xff\xd8":
        return None
    if data[-2:] != b"\xff\xd9":
        fail("JPEG has no end-of-image marker at the end of the file")
    pos = 2
    while pos + 4 <= len(data):
        if data[pos] != 0xFF:
            fail(f"JPEG: expected marker at offset {pos}")
        marker = data[pos + 1]
        if marker == 0xD9:  # EOI
            break
        if marker == 0x01 or 0xD0 <= marker <= 0xD7:
            pos += 2
            continue
        seg_len = struct.unpack(">H", data[pos + 2:pos + 4])[0]
        if seg_len < 2 or pos + 2 + seg_len > len(data):
            fail("JPEG: truncated segment")
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0/1/2: baseline/extended/progressive
            height, width = struct.unpack(">HH", data[pos + 5:pos + 9])
            return width, height
        pos += 2 + seg_len
    fail("JPEG: no start-of-frame segment found")


def png_dimensions(data):
    """Return (width, height) of a PNG after verifying its chunk CRCs."""
    if len(data) < 8 or data[0:8] != b"\x89PNG\r\n\x1a\n":
        return None
    pos = 8
    saw_ihdr = False
    saw_iend = False
    width = height = 0
    while pos + 12 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            fail("PNG: truncated chunk")
        crc_stored = struct.unpack(">I", data[pos + 8 + length:pos + 12 + length])[0]
        crc_actual = zlib.crc32(ctype)
        crc_actual = zlib.crc32(data[pos + 8:pos + 8 + length], crc_actual)
        if crc_actual & 0xFFFFFFFF != crc_stored:
            fail(f"PNG: bad CRC in {ctype!r} chunk")
        if ctype == b"IHDR":
            if length != 13:
                fail("PNG: bad IHDR length")
            width, height = struct.unpack(">II", data[pos + 8:pos + 16])
            saw_ihdr = True
        if ctype == b"IEND":
            saw_iend = True
            if end != len(data):
                fail("PNG: trailing bytes after IEND")
            break
        pos = end
    if not saw_ihdr:
        fail("PNG: no IHDR chunk")
    if not saw_iend:
        fail("PNG: no IEND chunk")
    return width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        fail(f"missing shipped image: {src}")
    with open(src, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        fail(f"image is {len(data)} bytes, over the 1 MiB limit")
    dims = jpeg_dimensions(data)
    kind = "JPEG"
    if dims is None:
        dims = png_dimensions(data)
        kind = "PNG"
    if dims is None:
        fail("entry.png is neither a whole JPEG nor a whole PNG")
    width, height = dims
    if width > MAX_DIM or height > MAX_DIM:
        fail(f"image is {width}x{height}, over the 1024x1024 limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    digest = hashlib.sha256(data).hexdigest()
    print(f"main.py: wrote {dst} ({kind} {width}x{height}, "
          f"{len(data)} bytes, sha256 {digest})")


if __name__ == "__main__":
    main()
