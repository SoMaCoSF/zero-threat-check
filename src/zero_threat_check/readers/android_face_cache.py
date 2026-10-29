"""Android Face Unlock / front-camera system cache checker.

Looks for raw frames outside Gallery in known system cache paths.
Read-only. Intended for AndroidQF collections or extracted /data trees.
"""
from pathlib import Path
from . import register

KNOWN_PATHS = [
    "data/system/users/0/faceunlock/cache",
    "data/system/faceunlock",
]

@register("android-face-cache")
def scan(root: Path) -> dict:
    findings = []
    gaps = []
    for rel in KNOWN_PATHS:
        p = root / rel
        if not p.exists():
            gaps.append(f"path not present: {rel}")
            continue
        files = list(p.rglob("*"))
        media = [f for f in files if f.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".bin"}]
        findings.append({
            "path": str(p),
            "file_count": len(files),
            "media_like_count": len(media),
            "grade": "moderate" if media else "unknown",
            "note": "Hidden system cache. Presence of frames is not proof of exfiltration."
        })
    return {
        "reader": "android-face-cache",
        "findings": findings,
        "gaps": gaps,
        "mandatory": "A clean result does not prove the device is safe."
    }
