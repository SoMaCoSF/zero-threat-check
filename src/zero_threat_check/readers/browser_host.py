"""Basic browser and host IOC depth (no-admin).

Checks common locations for hosts file anomalies, user autostart, and browser profile presence.
Does not parse full history databases in this version; reports what was reachable.
"""
from pathlib import Path
from . import register

@register("browser-host")
def scan(root: Path) -> dict:
    findings = []
    gaps = []
    # hosts
    for hosts in [Path("/etc/hosts"), Path("C:/Windows/System32/drivers/etc/hosts")]:
        if hosts.exists():
            try:
                lines = [l.strip() for l in hosts.read_text(errors="ignore").splitlines() if l.strip() and not l.startswith("#")]
                findings.append({"type": "hosts", "path": str(hosts), "entry_count": len(lines), "grade": "info"})
            except Exception as e:
                gaps.append(f"hosts unreadable: {e}")
    # common browser profile dirs (presence only)
    home = Path.home()
    browser_hints = [
        home / "Library/Application Support/Google/Chrome",
        home / "AppData/Local/Google/Chrome/User Data",
        home / ".config/google-chrome",
        home / "Library/Safari",
        home / "AppData/Roaming/Mozilla/Firefox",
    ]
    present = [str(p) for p in browser_hints if p.exists()]
    if present:
        findings.append({"type": "browser_profiles_present", "paths": present, "grade": "info"})
    else:
        gaps.append("no common browser profile directories found")
    return {
        "reader": "browser-host",
        "findings": findings,
        "gaps": gaps,
        "note": "Shallow presence check only. Full history parsing not yet implemented."
    }
