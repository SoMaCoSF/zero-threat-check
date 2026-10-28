# Zero Threat Check

Offline, read-only known-threat checker for mercenary spyware indicators, CISA Known Exploited Vulnerabilities, hidden deleted-photo/Face Unlock caches, and pre-installed MDM/rogue-certificate fraud patterns.

Designed as an **Agent Skill** that can be extended by harvesting capabilities from other security tools (MVT, AndroidQF, YARA, future sources) without rewriting the core.

A clean result is never proof the device is safe. Always surface evidence grades, coverage gaps, and limits.

## Features

- Offline IOC matching (domains, hashes, process names, paths, certificates)
- CISA KEV catalog ingestion and local inventory cross-check
- Mobile evidence: iPhone backups + AndroidQF
- Hidden cache checks (iOS PhotoData/Thumbnails, Android Face Unlock frames)
- Hidden MDM / rogue root certificate / always-on VPN indicators
- Structured JSON reports with evidence grades
- Logging
- Simple TUI
- Localhost dashboard
- Extensible reader/module registry

## Quick Start

```bash
git clone https://github.com/SoMaCoSF/zero-threat-check.git
cd zero-threat-check
pip install -e .
zero-threat-check --describe
zero-threat-check update --kev
zero-threat-check scan --kev-inventory
zero-threat-check dashboard
# open http://127.0.0.1:8765
```

## Project Layout

```
skill/                  # Agent skill (SKILL.md + references + evals)
src/zero_threat_check/  # Python package (CLI, TUI, dashboard, logging)
docs/                   # Architecture, usage, extending
```

## Architecture

See [docs/architecture.md](docs/architecture.md).

## Extending

See [docs/extending.md](docs/extending.md) and skill/references/capability-harvest.md.

## Safety

Consent required. Read-only. No network during scans. Never contact indicators. Prefer Access Now / Amnesty for findings.
