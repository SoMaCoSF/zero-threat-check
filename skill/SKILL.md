---
name: known-threat-check
description: "Run offline known-threat checks for mercenary spyware indicators and CISA KEV on authorized local evidence, and ingest new capability modules. Use when asked to scan for spyware, check for known exploited vulnerabilities, update indicators, interpret findings, or extend the checker with harvested capabilities."
type: workflow
lifecycle: active
---

# Known Threat Check — Offline Indicator + KEV Scanner

Offline, read-only check for published mercenary spyware indicators and CISA Known Exploited Vulnerabilities on authorized local evidence. Designed so new capabilities can be harvested from other tools and ingested as modules.

A clean result is never proof the device is safe.

## Core Workflow

1. Locate trusted local tool.
2. Run --describe.
3. Select and confirm scope (authorized evidence only).
4. Update indicators only when explicitly requested.
5. Run the check (network blocked).
6. Interpret with grades and gaps. Never claim clean.
7. Extend via capability harvest.

See references/ for full contracts, KEV, hidden cache/MDM, and harvest pattern.
