# Extending Zero Threat Check

Follow the harvest pattern. Document the capability, implement a reader, register it, add tests.

1. Identify artifacts, indicator types, grades, and gaps.
2. Create a reader under `src/zero_threat_check/readers/`.
3. Register it so `--describe` exposes it.
4. Keep the scan path network-blocked.
5. Update `skill/references/` and add fixtures.
6. Cite every indicator source.

See `skill/references/capability-harvest.md` and `skill/references/priority-modules.md`.
