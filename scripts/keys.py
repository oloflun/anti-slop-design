"""Nyckelhantering för anti-slop-design — Unsplash API-nycklar.

    python "C:\\Users\\Anton L\\anti-slop-design\\scripts\\keys.py"          # sätt + verifiera
    python .../scripts/keys.py --check                                     # bara verifiera
    python .../scripts/keys.py --pull / --push                             # inget deploymål, no-op

Nycklarna skrivs till EN fil utanför repot: ~/.secrets/.env
(delad med andra projekt; katalogen skapas om den saknas). Värden läses med
getpass (syns aldrig, hamnar aldrig i shell-historiken) och skrivs aldrig ut —
--check visar bara längd + fyra sista tecken.

Sökvägar löses ur __file__, ALDRIG ur cwd (api-key-setup SKILL.md Pitfall 1).
Konsumenten är scripts/catalogue/unsplash_sheet.py, som läser
UNSPLASH_ACCESS_KEY ur miljön först och annars ur samma fil.
"""

from __future__ import annotations

import argparse
import getpass
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # <repo>/scripts/keys.py -> <repo>
SECRETS_ENV = Path.home() / ".secrets" / ".env"        # utanför repot, med avsikt
TARGET_FILES = [SECRETS_ENV]


class Key:
    def __init__(self, name, files, blurb, *, required, where, secret=True, default=None):
        self.name, self.files, self.blurb = name, files, blurb
        self.required, self.where = required, where
        self.secret = secret        # False = vanlig konfig, ingen platshållarheuristik
        self.default = default      # skrivs utan prompt om nyckeln saknas i filen


KEYS = [
    Key(
        "UNSPLASH_ACCESS_KEY",
        [SECRETS_ENV],
        "Driver unsplash_sheet.py --api/--download/--verify. Utan den faller "
        "sourcing tillbaka på skrapvägen (Browser-panelen + --ids-file).",
        required=True,
        where="https://unsplash.com/oauth/applications/1056117 -> \"Keys\"",
    ),
    Key(
        "UNSPLASH_SECRET_KEY",
        [SECRETS_ENV],
        "Behövs BARA för OAuth-användarflöden (inloggad användare). Inget i "
        "repot använder den i dag — lämna tom om du inte vet att du behöver den.",
        required=False,
        where="https://unsplash.com/oauth/applications/1056117 -> \"Keys\"",
    ),
    Key(
        "UNSPLASH_APP_ID",
        [SECRETS_ENV],
        "Applikationens numeriska id, ren konfig (inte hemlig). Sätts till "
        "1056117 automatiskt om raden saknas.",
        required=False,
        where="https://unsplash.com/oauth/applications/1056117 (id:t i URL:en)",
        secret=False,
        default="1056117",
    ),
]

FIXED: dict[Path, dict[str, str]] = {}


def looks_placeholder(value: str) -> bool:
    return len(value) < 20 or "..." in value or "din-" in value or "your-" in value


def read_env(path: Path) -> dict[str, str]:
    """Tolerant KEY=VALUE-läsare: BOM, CRLF, kommentarer, tomrader."""
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def upsert(path: Path, key: str, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = path.read_text(encoding="utf-8-sig").splitlines() if path.exists() else []
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key}="):
            lines[i] = f"{key}={value}"
            break
    else:
        lines.append(f"{key}={value}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def guard_targets(target_files: list[Path]) -> None:
    """Målfilen ligger utanför repot — det är hela poängen. Skulle någon
    peka den in i repot måste den vara gitignorerad, annars avbryter vi."""
    for path in target_files:
        try:
            relative = path.resolve().relative_to(ROOT).as_posix()
        except ValueError:
            continue  # utanför repot: kan inte committas härifrån
        result = subprocess.run(
            ["git", "check-ignore", relative], cwd=ROOT, capture_output=True, text=True
        )
        if result.returncode != 0:
            sys.exit(f"AVBRYTER: {relative} ligger i repot och är inte gitignorerad.")


def status_line(key: Key, env: dict[str, str]) -> tuple[str, bool]:
    value = env.get(key.name, "")
    if not value:
        return ("SAKNAS" if key.required else "tom (valfri)"), not key.required
    if key.secret and looks_placeholder(value):
        return "PLATSHÅLLARE", False
    return f"OK (len={len(value)}, ...{value[-4:]})", True


def cmd_check() -> bool:
    print(f"Repo:  {ROOT}\nFil:   {SECRETS_ENV}  ({'finns' if SECRETS_ENV.exists() else 'saknas'})\n")
    ok = True
    for key in KEYS:
        env = read_env(key.files[0])
        status, key_ok = status_line(key, env)
        ok = ok and key_ok
        flag = "KRÄVS" if key.required else "valfri"
        print(f"  {key.name:22} [{flag:6}] {status}")
    print("\nKLART." if ok else "\nBLOCKERAT — se SAKNAS/PLATSHÅLLARE ovan.")
    return ok


def cmd_set() -> None:
    guard_targets(sorted({f for key in KEYS for f in key.files} | set(FIXED)))
    print(f"Repo: {ROOT}\nSkriver till: {SECRETS_ENV}")
    print("Lämna tomt för att hoppa över (befintligt värde behålls).\n")

    for key in KEYS:
        current = read_env(key.files[0]).get(key.name, "")
        if key.default is not None and not current:
            for path in key.files:
                upsert(path, key.name, key.default)
            print(f"{key.name}\n  -> saknades, satt till standardvärdet {key.default}\n")
            continue
        if key.default is not None and current:
            print(f"{key.name} [redan satt]\n  -> lämnas orörd\n")
            continue
        marker = " [redan satt]" if current and not (key.secret and looks_placeholder(current)) else ""
        print(f"{key.name}{marker}\n  {key.blurb}\n  Hämtas här: {key.where}")
        value = getpass.getpass("  Klistra in (syns inte): ").strip()
        if not value:
            print("  -> hoppar över\n")
            continue
        for path in key.files:
            upsert(path, key.name, value)
        print(f"  -> sparad i {', '.join(str(p) for p in key.files)}\n")

    for path, pairs in FIXED.items():
        for name, value in pairs.items():
            upsert(path, name, value)
    cmd_check()


def cmd_noop(flag: str) -> None:
    print(f"{flag}: inget deploymål — nycklarna används bara lokalt av unsplash_sheet.py.")


def main() -> None:
    try:
        sys.stdout.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass
    parser = argparse.ArgumentParser(description="Nyckelhantering (Unsplash).")
    parser.add_argument("--check", action="store_true", help="bara verifiera, skriv inget")
    parser.add_argument("--pull", action="store_true", help="inget deploymål (no-op)")
    parser.add_argument("--push", action="store_true", help="inget deploymål (no-op)")
    args = parser.parse_args()

    if args.check:
        sys.exit(0 if cmd_check() else 1)
    if args.pull or args.push:
        cmd_noop("--pull" if args.pull else "--push")
        sys.exit(0)
    cmd_set()


if __name__ == "__main__":
    main()
