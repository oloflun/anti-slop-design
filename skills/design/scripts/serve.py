#!/usr/bin/env python
"""Static file server for design verification. Stdlib only.

`python -m http.server` speaks HTTP/1.0 with no keep-alive. On Windows,
Chromium (Playwright and the design board's own iframes alike) drops large
responses from that server -- a big WebP screenshot or hero image comes back
as ERR_CONNECTION_RESET or just hangs. Nothing about the failure points at
the server; it looks like a broken build or a broken page. Every r6 builder
rediscovered this independently and wrote its own one-off fix (see
tests/alunix-ab-r6/runs/*/shots/serve.py) -- this is that fix, kept in one
place instead of copy-pasted per cell.

    python serve.py [--port 8000] [--root .]
"""
import argparse
import http.server
import mimetypes
import socketserver
import sys
from pathlib import Path

mimetypes.add_type("image/webp", ".webp")


class Handler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass  # quiet: this runs as a background subprocess


class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--root", default=".", help="directory to serve (default: cwd)")
    args = ap.parse_args()
    root = str(Path(args.root).resolve())

    def handler(*a, **kw):
        return Handler(*a, directory=root, **kw)

    httpd = Server(("127.0.0.1", args.port), handler)
    print(f"serving {root} at http://127.0.0.1:{args.port}")
    sys.stdout.flush()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
