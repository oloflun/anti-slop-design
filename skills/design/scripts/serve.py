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


import ctypes
import os
import threading
from ctypes import wintypes


def claude_desktop_owner_handle():
    """Hold the launching Desktop process, so detached previews cannot pin MSIX.

    Standalone/CLI launches retain their existing lifetime. Windows process
    creation times prevent following a recycled parent PID into an unrelated app.
    """
    if os.name != 'nt':
        return None
    k = ctypes.WinDLL('kernel32', use_last_error=True)
    class Entry(ctypes.Structure):
        _fields_ = [('size', wintypes.DWORD), ('usage', wintypes.DWORD),
                    ('pid', wintypes.DWORD), ('heap', ctypes.c_size_t),
                    ('module', wintypes.DWORD), ('threads', wintypes.DWORD),
                    ('parent', wintypes.DWORD), ('priority', wintypes.LONG),
                    ('flags', wintypes.DWORD), ('exe', wintypes.WCHAR * 260)]
    k.CreateToolhelp32Snapshot.argtypes = [wintypes.DWORD, wintypes.DWORD]
    k.CreateToolhelp32Snapshot.restype = wintypes.HANDLE
    k.Process32FirstW.argtypes = [wintypes.HANDLE, ctypes.POINTER(Entry)]
    k.Process32NextW.argtypes = [wintypes.HANDLE, ctypes.POINTER(Entry)]
    k.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    k.OpenProcess.restype = wintypes.HANDLE
    k.CloseHandle.argtypes = [wintypes.HANDLE]
    k.QueryFullProcessImageNameW.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)]
    k.GetProcessTimes.argtypes = [wintypes.HANDLE] + [ctypes.POINTER(wintypes.FILETIME)] * 4
    snapshot = k.CreateToolhelp32Snapshot(2, 0)
    if snapshot == ctypes.c_void_p(-1).value:
        return None
    parents = {}
    try:
        entry = Entry()
        entry.size = ctypes.sizeof(entry)
        ok = k.Process32FirstW(snapshot, ctypes.byref(entry))
        while ok:
            parents[entry.pid] = entry.parent
            ok = k.Process32NextW(snapshot, ctypes.byref(entry))
    finally:
        k.CloseHandle(snapshot)
    pid, seen, child_created = os.getpid(), set(), None
    while pid and pid not in seen:
        seen.add(pid)
        handle = k.OpenProcess(0x100000 | 0x1000, False, pid)
        if not handle:
            return None
        keep = False
        try:
            times = [wintypes.FILETIME() for _ in range(4)]
            if not k.GetProcessTimes(handle, *(ctypes.byref(t) for t in times)):
                return None
            created = (times[0].dwHighDateTime << 32) | times[0].dwLowDateTime
            if child_created is not None and created > child_created:
                return None
            child_created = created
            path, size = ctypes.create_unicode_buffer(32768), wintypes.DWORD(32768)
            if k.QueryFullProcessImageNameW(handle, 0, path, ctypes.byref(size)):
                name = path.value.lower()
                if '\\windowsapps\\claude_' in name and name.endswith('\\claude.exe'):
                    keep = True
                    return handle
        finally:
            if not keep:
                k.CloseHandle(handle)
        pid = parents.get(pid, 0)
    return None


def watch_owner(server, handle):
    """Stop serving as soon as the owning Claude Desktop process exits."""
    if handle is None:
        return
    def watch():
        k = ctypes.WinDLL('kernel32', use_last_error=True)
        k.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
        k.CloseHandle.argtypes = [wintypes.HANDLE]
        try:
            if k.WaitForSingleObject(handle, 0xFFFFFFFF) == 0:
                server.shutdown()
        finally:
            k.CloseHandle(handle)
    threading.Thread(target=watch, name='claude-preview-owner', daemon=True).start()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--root", default=".", help="directory to serve (default: cwd)")
    args = ap.parse_args()
    owner_handle = claude_desktop_owner_handle()
    root = str(Path(args.root).resolve())

    def handler(*a, **kw):
        return Handler(*a, directory=root, **kw)

    httpd = Server(("127.0.0.1", args.port), handler)
    print(f"serving {root} at http://127.0.0.1:{args.port}")
    sys.stdout.flush()
    try:
        watch_owner(httpd, owner_handle)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
