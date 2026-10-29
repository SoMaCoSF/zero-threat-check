"""Simple TUI that can run real scans."""
import json
from pathlib import Path

def run():
    print("=== Zero Threat Check TUI ===")
    print("1. Describe")
    print("2. Scan a path (Android cache + iOS MDM)")
    print("3. Exit")
    while True:
        c = input("> ").strip()
        if c == "1":
            from .cli import describe
            print(json.dumps(describe(), indent=2))
        elif c == "2":
            p = input("Path to backup/extracted tree: ").strip()
            if not p:
                continue
            from .cli import do_scan
            class A: pass
            a = A()
            a.phone = p
            a.path = None
            print(json.dumps(do_scan(a), indent=2))
        elif c == "3":
            break
        else:
            print("Unknown")
