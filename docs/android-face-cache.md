# Android Face Unlock Hidden Cache

Observed pattern (2026): raw front-camera and IR frames retained in system caches outside Gallery / Recently Deleted.

## Paths of interest
- `/data/system/users/0/faceunlock/cache`
- Related Google Play Services / diagnostics caches

## Reader
`src/zero_threat_check/readers/android_face_cache.py`

Usage (on extracted tree or AndroidQF):
```python
from pathlib import Path
from zero_threat_check.readers.android_face_cache import scan
print(scan(Path("/path/to/extracted")))
```

## Notes
- Read-only.
- Presence of frames is graded moderate at most.
- Does not prove exfiltration.
- Always report gaps if paths are missing.
- Prefer full backup or AndroidQF over live device modification.
