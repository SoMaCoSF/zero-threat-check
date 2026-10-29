# Zero Threat Check

Offline, read-only known-threat checker for mercenary spyware indicators, CISA Known Exploited Vulnerabilities, hidden deleted-photo/Face Unlock caches, and pre-installed MDM/rogue-certificate fraud patterns.

A clean result is never proof the device is safe.

## Features (implemented)

- **Android Face Unlock hidden cache** reader
- **iOS MDM / configuration profile** reader
- **iOS PhotoData/Thumbnails** deleted-photo cache reader
- **CISA KEV inventory** cross-check (after `update`)
- **Browser + host** shallow presence checks
- Optional **YARA** stub (reports gap until engine + rules present)
- Structured JSON reports with grades and gaps
- Logging
- TUI and localhost dashboard
- Extensible reader registry
- Tests + CI

## Quick Start

```bash
git clone https://github.com/SoMaCoSF/zero-threat-check.git
cd zero-threat-check
pip install -e ".[test]"
zero-threat-check --describe
zero-threat-check update              # cache CISA KEV
zero-threat-check scan --phone /path/to/tree
zero-threat-check tui
zero-threat-check dashboard           # http://127.0.0.1:8765
pytest tests/ -q
```

## Project Layout

```
skill/references/     # priority-modules, kev, reporting, capability-harvest, …
src/zero_threat_check/
  readers/            # android_face_cache, ios_mdm, ios_photo_cache, kev_inventory, browser_host, yara_stub
  update.py           # explicit KEV fetch
  cli.py / tui.py / dashboard.py
docs/ examples/ tests/ .github/workflows/
```

## Safety

Consent required. Read-only. No network during scans. Never contact indicators. Prefer Access Now / Amnesty for findings.
