"""Smoke check for the Unsplash API path in scripts/catalogue/unsplash_sheet.py.

    python tests/unsplash_api_smoke.py

No key (env or ~/.secrets/.env) -> prints "skipped: no key", exit 0.
With a key -> one GET /photos/random in-process; asserts HTTP 200 and that
both X-Ratelimit-* headers are present. Prints status + limit + remaining only.
Stdlib only. The key value is never printed.
"""
import importlib.util
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "catalogue" / "unsplash_sheet.py"


def load_module():
    spec = importlib.util.spec_from_file_location("unsplash_sheet", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    us = load_module()
    key = us.resolve_access_key()
    if not key:
        print("skipped: no key")
        return 0
    status, limit, remaining, tier, errors = us.verify(key)
    print(f"HTTP {status}   X-Ratelimit-Limit: {limit}   X-Ratelimit-Remaining: {remaining}   tier: {tier}")
    assert status == 200, f"expected HTTP 200, got {status}: {errors}"
    assert limit is not None, "X-Ratelimit-Limit header missing"
    assert remaining is not None, "X-Ratelimit-Remaining header missing"
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
