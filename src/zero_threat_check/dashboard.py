"""Minimal localhost dashboard."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b"""<html><body>
            <h1>Zero Threat Check</h1>
            <p>Local dashboard (stub)</p>
            <ul>
              <li><a href="/describe">Describe</a></li>
              <li><a href="/status">Status</a></li>
            </ul>
            </body></html>"""
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/describe":
            from .cli import describe
            data = json.dumps(describe()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()

def run(port=8765):
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"Dashboard at http://127.0.0.1:{port}")
    server.serve_forever()
