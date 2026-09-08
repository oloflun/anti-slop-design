"""Static server for verification: same as `python -m http.server 3103` from repo root,
but HTTP/1.1 with keep-alive. Chromium dropped large image responses from the stock
HTTP/1.0 server on this machine (ERR_CONNECTION_RESET / hangs)."""
import http.server, socketserver, sys, mimetypes
mimetypes.add_type("image/webp", ".webp")
class H(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"
    def log_message(self, *a): pass
class S(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True; allow_reuse_address = True
port = int(sys.argv[1]) if len(sys.argv) > 1 else 3103
S(("127.0.0.1", port), H).serve_forever()
