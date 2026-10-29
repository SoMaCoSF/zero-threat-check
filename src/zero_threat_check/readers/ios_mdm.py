"""iOS configuration profile / MDM checker.

Looks for .mobileconfig files and common backup indicators of MDM,
rogue certificates, and always-on VPN payloads in an extracted
iPhone backup or filesystem tree. Read-only.
"""
from pathlib import Path
from . import register

MDM_KEYWORDS = ("RemoteManagement", "DeviceManagement", "com.apple.mdm", "MDM")
VPN_KEYWORDS = ("VPN", "WireGuard", "AlwaysOnVPN", "com.apple.vpn.managed")
CERT_KEYWORDS = ("Certificate", "Root", "Trust")

@register("ios-mdm")
def scan(root: Path) -> dict:
    findings = []
    gaps = []
    configs = list(root.rglob("*.mobileconfig")) + list(root.rglob("*Profile*"))
    if not configs:
        gaps.append("no .mobileconfig or Profile files found in tree")
    for p in configs:
        try:
            text = p.read_text(errors="ignore")
        except Exception:
            continue
        flags = []
        if any(k.lower() in text.lower() for k in MDM_KEYWORDS):
            flags.append("mdm")
        if any(k.lower() in text.lower() for k in VPN_KEYWORDS):
            flags.append("vpn")
        if any(k.lower() in text.lower() for k in CERT_KEYWORDS):
            flags.append("certificate")
        grade = "strong" if "mdm" in flags and ("vpn" in flags or "certificate" in flags) else (
            "moderate" if flags else "weak"
        )
        findings.append({
            "path": str(p),
            "flags": flags,
            "grade": grade,
            "note": "Profile content matched known MDM/VPN/cert markers. Verify install date and whether it appears in Settings > General > VPN & Device Management."
        })
    return {
        "reader": "ios-mdm",
        "findings": findings,
        "gaps": gaps,
        "mandatory": "A clean result does not prove the device is safe. Check live Settings for Supervision and MDM."
    }
