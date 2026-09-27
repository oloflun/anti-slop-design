#!/usr/bin/env python3
"""Run a browser-driving command while holding the machine-wide browser lock.

    python tests/alunix-r8/browser_lock.py -- python some_probe.py URL ...

Parallel reviewers each start Chromium; unserialized, they exhausted RAM and
crashed the machine (2026-09-25). Same lock file as showcase_probe.py's and
section_probe.py's single_flight(): %TEMP%/alunix-browser.lock.
"""
import os, subprocess, sys, time

LOCK = os.path.join(os.environ.get("TEMP", "/tmp"), "alunix-browser.lock")


def main():
    cmd = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    if not cmd:
        sys.exit(__doc__)
    deadline = time.time() + 3600
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode()); os.close(fd)
            break
        except FileExistsError:
            if time.time() - os.path.getmtime(LOCK) > 900:
                os.remove(LOCK); continue
            if time.time() > deadline:
                sys.exit("browser_lock: lock held too long")
            time.sleep(2)
    try:
        # the wrapped script must not try to take the same lock again
        env = dict(os.environ, ALUNIX_BROWSER_LOCK_HELD="1")
        sys.exit(subprocess.call(cmd, env=env))
    finally:
        if os.path.exists(LOCK):
            os.remove(LOCK)


if __name__ == "__main__":
    main()
