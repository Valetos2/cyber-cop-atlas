#!/usr/bin/env python3
"""Build GitHub Pages from the owner's standalone Atlas 40 ZIP (no game ROMs needed)."""
from __future__ import annotations

import hashlib
import shutil
import stat
import sys
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "Cyber-Cop_Atlas40_full.zip"
DEST = ROOT / "_site"
MAX_TOTAL = 120 * 1024 * 1024
ALLOWED_SUFFIXES = {".html", ".png", ".json", ".csv", ".md", ".txt"}


def build() -> None:
    if not ARCHIVE.is_file():
        sys.exit("Missing Cyber-Cop_Atlas40_full.zip. Upload the Atlas 40 ZIP to the repository root.")

    with zipfile.ZipFile(ARCHIVE) as z:
        names = {i.filename for i in z.infolist() if not i.is_dir()}
        required = {"Cyber-Cop_Atlas.html", "Cyber-Cop_Atlas_en.html", "data.json", "cells.csv"}
        if missing := required - names:
            sys.exit(f"Archive missing required files: {sorted(missing)}")
        if z.testzip() is not None:
            sys.exit("Corrupt archive: ZIP CRC validation failed")
        if sum(i.file_size for i in z.infolist()) > MAX_TOTAL:
            sys.exit("Archive is unexpectedly large; stopping to prevent decompression bombs")

        if DEST.exists():
            shutil.rmtree(DEST)
        DEST.mkdir()
        for info in z.infolist():
            if info.is_dir():
                continue
            posix = PurePosixPath(info.filename)
            if (posix.is_absolute() or ".." in posix.parts or "\\" in info.filename
                    or info.filename.startswith(".") or posix.suffix.lower() not in ALLOWED_SUFFIXES
                    or stat.S_IFMT(info.external_attr >> 16) == stat.S_IFLNK):
                sys.exit(f"Unsafe or unexpected ZIP member: {info.filename}")
            target = DEST.joinpath(*posix.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(info))

    ru = DEST / "Cyber-Cop_Atlas.html"
    en = DEST / "Cyber-Cop_Atlas_en.html"
    for html_path, old, new in (
        (ru, "<title>Cyber-Cop — атлас 16 уровней</title>", "<title>Cyber-Cop Atlas 40 — 32 карты: Original + Mission Disk</title>"),
        (en, "<title>Cyber-Cop — 16-floor atlas</title>", "<title>Cyber-Cop Atlas 40 — 32 maps: Original + Mission Disk</title>"),
    ):
        contents = html_path.read_text(encoding="utf-8")
        if "data:image/png;base64," not in contents or "Cyber-Cop_Atlas" not in contents:
            sys.exit(f"{html_path.name} is not the expected standalone atlas")
        html_path.write_text(contents.replace(old, new), encoding="utf-8")

    (DEST / "index.html").write_bytes(ru.read_bytes())
    (DEST / ".nojekyll").write_text("", encoding="utf-8")
    downloads = DEST / "downloads"
    downloads.mkdir()
    shutil.copy2(ARCHIVE, downloads / ARCHIVE.name)
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    print(f"PASS: {len(names)} Atlas 40 files, index, RU/EN viewers, downloadable original ZIP")
    print(f"Atlas ZIP SHA-256: {digest}")
    print(f"GitHub Pages staging directory: {DEST}")


if __name__ == "__main__":
    build()
