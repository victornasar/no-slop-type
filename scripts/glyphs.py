#!/usr/bin/env python3
"""Report which `scripts` tags a font family earns, from its real character table.

Usage: python3 scripts/glyphs.py path/to/Font-Regular.otf path/to/Font-Italic.otf ...

Pass every style of one family: a letter only counts if all styles have it. Reads OTF and TTF
(not WOFF2). Standard library only.
"""
import struct
import sys

WESTERN = "ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖØÙÚÛÜÝàáâãäåæçèéêëìíîïñòóôõöøùúûüýÿßŒœ"
CENTRAL = "ĄąĆćČčĎďĐđĘęĚěŁłŃńŇňŐőŘřŚśŠšŤťŮůŰűŹźŻżŽž"

SCRIPTS = {
    "latin": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?()-",
    "latin-ext": WESTERN + CENTRAL,
    "cyrillic": "".join(chr(c) for c in [*range(0x410, 0x450), 0x401, 0x451]),
    "greek": "".join(chr(c) for c in [*range(0x391, 0x3A2), *range(0x3A3, 0x3AA), *range(0x3B1, 0x3CA)]),
    "vietnamese": "ĂăÂâĐđÊêÔôƠơƯư" + "".join(chr(c) for c in range(0x1EA0, 0x1EFA)),
    "hebrew": "".join(chr(c) for c in range(0x5D0, 0x5EB)),
}


def codepoints(path):
    with open(path, "rb") as fh:
        b = fh.read()
    tables = {}
    for i in range(struct.unpack(">H", b[4:6])[0]):
        tag, _, offset, _ = struct.unpack(">4sIII", b[12 + 16 * i:28 + 16 * i])
        tables[tag] = offset
    cmap = tables[b"cmap"]
    found = set()
    for i in range(struct.unpack(">H", b[cmap + 2:cmap + 4])[0]):
        sub = cmap + struct.unpack(">I", b[cmap + 8 + 8 * i:cmap + 12 + 8 * i])[0]
        fmt = struct.unpack(">H", b[sub:sub + 2])[0]
        if fmt == 4:
            count = struct.unpack(">H", b[sub + 6:sub + 8])[0] // 2
            ends = struct.unpack(f">{count}H", b[sub + 14:sub + 14 + 2 * count])
            starts = struct.unpack(f">{count}H", b[sub + 16 + 2 * count:sub + 16 + 4 * count])
            for start, end in zip(starts, ends):
                if start != 0xFFFF:
                    found |= set(range(start, end + 1))
        elif fmt == 12:
            for k in range(struct.unpack(">I", b[sub + 12:sub + 16])[0]):
                start, end, _ = struct.unpack(">III", b[sub + 16 + 12 * k:sub + 28 + 12 * k])
                found |= set(range(start, end + 1))
    return found


def coverage(chars):
    """{tag: missing characters} for a set of code points."""
    return {tag: "".join(c for c in letters if ord(c) not in chars) for tag, letters in SCRIPTS.items()}


def earned(chars):
    return [tag for tag, missing in coverage(chars).items() if not missing]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    common = set.intersection(*(codepoints(p) for p in sys.argv[1:]))
    print("scripts:", earned(common))
    for tag, missing in coverage(common).items():
        if missing:
            shown = missing if len(missing) <= 40 else f"{len(missing)} characters"
            print(f"  {tag}: missing {shown}")


if __name__ == "__main__":
    main()
