#!/usr/bin/env python3
"""CLI entry point."""
import argparse
import json
from pathlib import Path
from .logging_setup import setup_logging
from .readers import READERS
from .readers.android_face_cache import scan as scan_android
from .readers.ios_mdm import scan as scan_ios
from .readers.ios_photo_cache import scan as scan_ios_photo
from .readers.browser_host import scan as scan_browser
from .readers.kev_inventory import scan as scan_kev
from .update import update_kev

log = setup_logging()

def describe():
    return {
        "name": "zero-threat-check",
        "version": "0.3.0",
        "capabilities": list(READERS.keys()),
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
    results.append(scan_android(root))
    results.append(scan_ios(root))
    results.append(scan_ios_photo(root))
    results.append(scan_browser(root))
    results.append(scan_kev())
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
    p.add_argument("--mirror", action="store_true", help="Use GitHub mirror for KEV update")
    args = p.parse_args()

    if args.describe or not args.command:
        print(json.dumps(describe(), indent=2))
        return

    log.info("command=%s", args.command)
    if args.command == "update":
        try:
            out = update_kev(mirror=args.mirror)
            print(json.dumps(out, indent=2))
        except Exception as e:
            print(json.dumps({"ok": False, "error": str(e)}, indent=2))
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
