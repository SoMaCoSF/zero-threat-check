#!/usr/bin/env python3
"""CLI entry point."""
import argparse
import json
from .logging_setup import setup_logging

log = setup_logging()

def describe():
    return {
        "name": "zero-threat-check",
        "version": "0.1.0",
        "capabilities": [
            "kev-inventory",
            "mobile-evidence",
            "hidden-cache-mdm",
            "browser-host",
            "optional-patterns",
            "indicator-update",
        ],
        "scan_path": "network-blocked",
        "update_path": "explicit",
    }

def main():
    p = argparse.ArgumentParser(prog="zero-threat-check")
    p.add_argument("--describe", action="store_true")
    p.add_argument("command", nargs="?", choices=["update", "scan", "tui", "dashboard"])
    p.add_argument("--kev", action="store_true")
    p.add_argument("--kev-inventory", action="store_true")
    p.add_argument("--phone", type=str)
    args = p.parse_args()

    if args.describe or not args.command:
        print(json.dumps(describe(), indent=2))
        return

    log.info("command=%s", args.command)
    if args.command == "update":
        print("Update stub — implement fetch or call scripts/update_kev.py")
    elif args.command == "scan":
        print(json.dumps({"verdict": "stub", "note": "readers not yet implemented"}, indent=2))
    elif args.command == "tui":
        from .tui import run
        run()
    elif args.command == "dashboard":
        from .dashboard import run
        run()

if __name__ == "__main__":
    main()
