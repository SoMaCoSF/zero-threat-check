"""Localhost dashboard for Zero Threat Check."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, timezone

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            body = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Zero Threat Check</title>
<style>
body{font-family:system-ui;margin:2rem;background:#0f1115;color:#e6e6e6}
a{color:#6cb6ff} .card{background:#1a1d24;padding:1rem;margin:1rem 0;border-radius:8px}
.badge{display:inline-block;padding:0.2rem 0.5rem;border-radius:4px;background:#2a2f3a}
</style></head><body>
<h1>Zero Threat Check</h1>
<p>Offline known-threat scanner — local dashboard</p>
<div class="card"><h2>Actions</h2>
<ul>
<li><a href="/describe">Describe capabilities</a></li>
<li><a href="/status">Status</a></li>
<li><a href="/docs">Architecture notes</a></li>
</ul></div>
<div class="card"><h2>Safety</h2>
<p class="badge">Clean ≠ Safe</p>
<p>Read-only. Network blocked during scans. Consent required.</p></div>
</body></html>""".encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/describe":
            from .cli import describe
            data = json.dumps(describe(), indent=2).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)
        elif self.path == "/status":
            status = {
                "ok": True,
                "time": datetime.now(timezone.utc).isoformat(),
                "mode": "local-only",
                "scan_path": "network-blocked"
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(status, indent=2).encode())
        elif self.path == "/docs":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"See docs/architecture.md and skill/references/ in the repo.\n")
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8765):
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Dashboard at http://127.0.0.1:{port}")
    server.serve_forever()
