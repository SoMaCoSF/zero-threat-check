"""Explicit update path for CISA KEV. Network allowed only here."""
import json
import urllib.request
from pathlib import Path
from datetime import datetime, timezone

KEV_URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
CACHE_DIR = Path.home() / ".local" / "share" / "zero-threat-check"
CACHE = CACHE_DIR / "kev.json"

def update_kev(mirror=False):
    url = KEV_URL if not mirror else "https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.json"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "zero-threat-check/0.2"})
    with urllib.request.urlopen(req, timeout=45) as resp:
        data = json.loads(resp.read().decode())
    if "vulnerabilities" not in data:
        raise ValueError("invalid KEV payload")
    CACHE.write_text(json.dumps(data))
    return {
        "ok": True,
        "source": url,
        "catalogVersion": data.get("catalogVersion"),
        "count": data.get("count"),
        "cached_at": datetime.now(timezone.utc).isoformat(),
        "path": str(CACHE)
    }
