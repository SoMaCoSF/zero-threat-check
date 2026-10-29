#!/usr/bin/env python3
"""CLI entry point."""
import argparse
import json
from pathlib import Path
from .logging_setup import setup_logging
from .readers import READERS
from .readers.android_face_cache import scan as scan_android
from .readers.ios_mdm import scan as scan_ios

log = setup_logging()

def describe():
    return {
        "name": "zero-threat-check",
        "version": "0.2.0",
        "capabilities": list(READERS.keys()) or ["android-face-cache", "ios-mdm"],
        "scan_path": "network-blocked",
        "update_path": "explicit",
        "readers": list(READERS.keys()),
    }

def do_scan(args):
    results = []
    root = Path(args.phone or args.path or ".").resolve()
    if not root.exists():
        return {"error": f"path not found: {root}"}
    log.info("scanning %s", root)
    # Always run both readers; they report gaps when paths missing
    results.append(scan_android(root))
    results.append(scan_ios(root))
    return {
        "schema_version": "1.0",
        "scope": str(root),
        "results": results,
        "mandatory": "A clean result means no known indicators were found in the places checked. It does not mean the device is clean."
    }

def main():
    p = argparse.ArgumentParser(prog="zero-threat-check")
    p.add_argument("--describe", action="store_true")
    p.add_argument("command", nargs="?", choices=["update", "scan", "tui", "dashboard"])
    p.add_argument("--phone", type=str, help="Path to backup, AndroidQF, or extracted tree")
    p.add_argument("--path", type=str, help="Alias for --phone")
    args = p.parse_args()

    if args.describe or not args.command:
        print(json.dumps(describe(), indent=2))
        return

    log.info("command=%s", args.command)
    if args.command == "update":
        print("Update path is explicit. Use scripts or implement fetch. Scan remains network-blocked.")
    elif args.command == "scan":
        out = do_scan(args)
        print(json.dumps(out, indent=2))
    elif args.command == "tui":
        from .tui import run
        run()
    elif args.command == "dashboard":
        from .dashboard import run
        run()

if __name__ == "__main__":
    main()
