# Priority Capability Modules

Implement and ingest in this order.

## 1. CISA KEV Local Inventory Cross-Check
Match installed software / extensions against current KEV. Surface due dates, required actions, ransomware flag. Never claim exploitation.

## 2. Mobile Evidence + Hidden Cache / MDM
- iPhone backups + AndroidQF
- iOS PhotoData/Thumbnails deleted-photo cache
- Android Face Unlock / front-camera system caches (`/data/system/users/0/faceunlock/cache` and related)
- Hidden MDM profiles, rogue root certificates, always-on VPN tunnels

## 3. Browser + Host IOC Depth
History, cookies, HSTS, autostart, hosts, DNS (no-admin).

## 4. Optional Pattern / YARA
Published binary rules. Gap if engine missing.

## 5. Indicator Update + Verification Pipeline
Explicit refresh with hash checks. Scan path stays network-blocked.

Each module registers in `--describe`, reports grades and gaps, and cites sources.
