# CISA KEV Integration

Official feed: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json

Mirror: https://github.com/cisagov/kev-data

## Usage
```bash
zero-threat-check update          # fetch and cache
zero-threat-check update --mirror
zero-threat-check scan            # includes kev-inventory reader
```

Matches are prioritization only (due date, ransomware flag). Never claim exploitation.
