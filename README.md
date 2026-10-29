# Zero Threat Check

Offline, read-only known-threat checker for mercenary spyware indicators, CISA Known Exploited Vulnerabilities, hidden deleted-photo/Face Unlock caches, and pre-installed MDM/rogue-certificate fraud patterns.

Designed as an **Agent Skill** that can be extended by harvesting capabilities from other security tools without rewriting the core.

A clean result is never proof the device is safe.

## Features

- **Working readers**: Android Face Unlock hidden cache + iOS MDM/configuration profile
- Offline IOC matching (planned)
- CISA KEV cross-check (planned)
- Structured JSON reports with evidence grades and gaps
- Logging
- TUI that can run real scans
- Localhost dashboard (http://127.0.0.1:8765)
- Extensible reader registry

## Quick Start

```bash
git clone https://github.com/SoMaCoSF/zero-threat-check.git
cd zero-threat-check
pip install -e .
zero-threat-check --describe
zero-threat-check scan --phone /path/to/extracted/tree/or/backup
zero-threat-check tui
zero-threat-check dashboard
```

## Project Layout

```
skill/                  # Agent skill
src/zero_threat_check/
  readers/              # android_face_cache.py, ios_mdm.py
  cli.py / tui.py / dashboard.py
docs/                   # architecture, cli-usage, android-face-cache, …
```

## Key Docs

- [docs/cli-usage.md](docs/cli-usage.md)
- [docs/architecture.md](docs/architecture.md)
- [docs/android-face-cache.md](docs/android-face-cache.md)
- [skill/references/priority-modules.md](skill/references/priority-modules.md)

## Safety

Consent required. Read-only. No network during scans. Never contact indicators. Prefer Access Now / Amnesty for findings.
