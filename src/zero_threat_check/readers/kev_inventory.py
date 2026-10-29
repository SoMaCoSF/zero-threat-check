"""CISA KEV local inventory cross-check.

Collects a best-effort local software inventory and matches against a cached KEV JSON.
Never claims exploitation — only prioritization by due date and ransomware flag.
"""
import json
import platform
import subprocess
from pathlib import Path
from . import register

CACHE = Path.home() / ".local" / "share" / "zero-threat-check" / "kev.json"

def collect_inventory():
    items = []
    sysname = platform.system().lower()
    if sysname == "windows":
        try:
            out = subprocess.check_output(
                ["reg", "query", "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall", "/s"],
                text=True, stderr=subprocess.DEVNULL, timeout=20
            )
            for line in out.splitlines():
                if "DisplayName" in line and "REG_" in line:
                    name = line.split("REG_", 1)[-1].strip().split(None, 1)[-1]
                    if name and len(name) > 2:
                        items.append({"name": name.strip(), "source": "uninstall"})
        except Exception:
            pass
    elif sysname == "darwin":
        apps = Path("/Applications")
        if apps.exists():
            items.extend({"name": p.stem, "source": "applications"} for p in apps.glob("*.app"))
    else:
        for cmd in (["dpkg", "-l"], ["rpm", "-qa"]):
            try:
                out = subprocess.check_output(cmd, text=True, stderr=subprocess.DEVNULL, timeout=15)
                for line in out.splitlines()[:300]:
                    parts = line.split()
                    if len(parts) >= 2:
                        items.append({"name": parts[1], "source": cmd[0]})
            except Exception:
                continue
    return items

@register("kev-inventory")
def scan(root: Path = None) -> dict:
    gaps = []
    matches = []
    if not CACHE.exists():
        gaps.append("no cached kev.json — run 'zero-threat-check update' first")
        return {"reader": "kev-inventory", "matches": [], "gaps": gaps, "inventory_count": 0}
    try:
        kev = json.loads(CACHE.read_text())
    except Exception as e:
        gaps.append(f"failed to read cache: {e}")
        return {"reader": "kev-inventory", "matches": [], "gaps": gaps, "inventory_count": 0}
    inv = collect_inventory()
    names = {i["name"].lower() for i in inv}
    for v in kev.get("vulnerabilities", []):
        product = (v.get("product") or "").lower()
        vendor = (v.get("vendorProject") or "").lower()
        if any(product and product in n or vendor and vendor in n for n in names):
            matches.append({
                "cveID": v.get("cveID"),
                "product": v.get("product"),
                "vendorProject": v.get("vendorProject"),
                "dueDate": v.get("dueDate"),
                "knownRansomwareCampaignUse": v.get("knownRansomwareCampaignUse"),
                "requiredAction": v.get("requiredAction"),
                "grade": "prioritization"
            })
    matches.sort(key=lambda m: m.get("dueDate") or "9999")
    return {
        "reader": "kev-inventory",
        "inventory_count": len(inv),
        "matches": matches[:50],
        "gaps": gaps,
        "note": "Matches are prioritization only, not proof of exploitation."
    }
