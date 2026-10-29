# CLI Usage

## Describe
```bash
zero-threat-check --describe
```

## Scan an extracted tree or backup
Runs both the Android Face Unlock cache reader and the iOS MDM/profile reader.
They report gaps when their paths are absent.

```bash
zero-threat-check scan --phone /path/to/extracted/android/or/ios/backup
# or
zero-threat-check scan --path /path/to/tree
```

Example output includes findings with grades (strong/moderate/weak) and gaps.

## TUI
```bash
zero-threat-check tui
```

## Dashboard
```bash
zero-threat-check dashboard
# http://127.0.0.1:8765
```

Always review the mandatory clean ≠ safe statement.
