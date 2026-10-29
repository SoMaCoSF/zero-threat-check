"""iOS Spotlight PhotoData/Thumbnails cache checker.

Looks for retained copies of deleted photos in PhotoData/Thumbnails.
Read-only. Grade is moderate at most.
"""
from pathlib import Path
from . import register

@register("ios-photo-cache")
def scan(root: Path) -> dict:
    findings = []
    gaps = []
    candidates = list(root.rglob("PhotoData/Thumbnails")) + list(root.rglob("*/PhotoData/Thumbnails"))
    if not candidates:
        gaps.append("PhotoData/Thumbnails not found")
    for p in candidates:
        if not p.is_dir():
            continue
        files = list(p.rglob("*"))
        media = [f for f in files if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".heic", ".mov", ".mp4"}]
        findings.append({
            "path": str(p),
            "file_count": len(files),
            "media_like_count": len(media),
            "grade": "moderate" if media else "unknown",
            "note": "Spotlight cache may retain previously deleted photos. Presence is not proof any app read them."
        })
    return {
        "reader": "ios-photo-cache",
        "findings": findings,
        "gaps": gaps,
        "mandatory": "A clean result does not prove the device is safe."
    }
