"""Optional YARA pattern module stub.

Reports a gap unless yara-x or yara is importable and rules are present.
"""
from pathlib import Path
from . import register

@register("yara-patterns")
def scan(root: Path) -> dict:
    gaps = ["YARA engine not bundled; install yara-x and supply rules to enable"]
    return {
        "reader": "yara-patterns",
        "findings": [],
        "gaps": gaps,
        "note": "Optional. Scan path remains network-blocked."
    }
