"""Minimal TUI stub."""
def run():
    print("=== Zero Threat Check TUI ===")
    print("1. Describe")
    print("2. Update KEV")
    print("3. Scan (stub)")
    print("4. Exit")
    while True:
        c = input("> ").strip()
        if c == "1":
            from .cli import describe
            import json
            print(json.dumps(describe(), indent=2))
        elif c == "4":
            break
        else:
            print("Not implemented yet")
