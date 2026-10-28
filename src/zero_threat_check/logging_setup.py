import logging
from pathlib import Path

LOG_DIR = Path.home() / ".local" / "share" / "zero-threat-check" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        handlers=[
            logging.FileHandler(LOG_DIR / "zero-threat-check.log"),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger("zero_threat_check")
