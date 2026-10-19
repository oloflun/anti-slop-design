# -*- coding: utf-8 -*-
"""scaffold_entry.py fixture: run it into a temp catalogue, both directions.

The plan's own control is case 1: scaffold `aarke` in a temp dir and compare the
generated frontmatter against the existing entries/aarke/entry.md for `palette`
and `type`. Cases 2-5 are the house rule from performance.md ("both probes are
proven in both directions before they are trusted") applied to the slug guard
and the never-overwrite guard: a valid call that must succeed, and the invalid
slugs that must be refused with a non-zero exit.

    python tests/catalogue/test_scaffold_entry.py

Prints one line per case and asserts. No framework.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:                          # the script's own output is Swedish, ASCII-folded
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

REPO = Path(r"C:/Users/Anton L/anti-slop-design")
SCRIPT = REPO / "scripts" / "catalogue" / "scaffold_entry.py"
CAT = REPO / "design-catalogue"
sys.path.insert(0, str(REPO / "scripts" / "catalogue"))
from index import parse_frontmatter          # noqa: E402  the catalogue's parser

# only the three files scaffold_entry.py reads, so the fixture's dependencies
# are visible rather than "whatever happens to be in extract/"
EXTRACT_GLOBS = ("*-design-tokens.json", "*-motion-tokens.json", "*-design-language.md")


def run(*argv):
    r = subprocess.run([sys.executable, str(SCRIPT), *argv],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", cwd=str(REPO))
    return r.returncode, (r.stdout or ""), (r.stderr or "")


def temp_catalogue(tmp: Path, slug: str) -> Path:
    """A catalogue root holding nothing but <slug>/extract/, so the run cannot
    touch the real design-catalogue/ even if it tried."""
    dest = tmp / "design-catalogue" / "entries" / slug / "extract"
    dest.mkdir(parents=True)
    src = CAT / "entries" / slug / "extract"
    for pat in EXTRACT_GLOBS:
        for f in src.glob(pat):
            shutil.copy2(f, dest / f.name)
    return tmp / "design-catalogue"


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="scaffold-entry-"))
    try:
        # -- 1 the plan's control: aarke, temp dir, palette/type vs the real entry
        root = temp_catalogue(tmp, "aarke")
        code, out, err = run("aarke", "--origin", "raw-url", "--url", "https://aarke.com",
                             "--catalogue", str(root), "--json")
        assert code == 0, f"1 aarke: exit {code}\n{err}"
        made = json.loads(out)
        gen_path = Path(made["entry"])
        assert gen_path.is_file(), "1 aarke: no entry.md written"
        assert CAT.resolve() not in gen_path.resolve().parents, \
            "1 aarke: wrote into the real catalogue"

        gen, _ = parse_frontmatter(gen_path.read_text(encoding="utf-8"))
        real, _ = parse_frontmatter(
            (CAT / "entries" / "aarke" / "entry.md").read_text(encoding="utf-8"))

        gp = [h.upper() for h in gen["palette"]]
        rp = [h.upper() for h in real["palette"]]
        shared = [h for h in gp if h in rp]
        print("1 aarke palette")
        print(f"    generated: {gp}")
        print(f"    existing : {rp}")
        identical = gp == rp
        prefix = bool(gp) and rp[:len(gp)] == gp
        order_ok = shared == [h for h in rp if h in gp]
        print(f"    identical={identical}  generated-is-prefix={prefix}  "
              f"shared={len(shared)}/{len(rp)}  same order={order_ok}")
        assert shared, "1 aarke: no measured hex survived into the entry"
        assert order_ok, "1 aarke: shared hexes are in a different order"

        print("2 aarke type")
        print(f"    generated: {gen['type']}")
        print(f"    existing : {real['type']}")
        print(f"    measured : {gen['measured']}")
        # SCHEMA forbids inventing tokens; designlang resolved no family names
        # for aarke, so the only correct generated value is the empty list.
        assert gen["type"] == [], "2 aarke: invented a typeface designlang never named"
        assert "unresolved" in gen["measured"], "2 aarke: dropped labels not recorded"

        # -- 3 the rest of the contract on that same file
        assert gen["status"] == "pending", "3: status must be pending"
        assert gen["url"] == "https://aarke.com" and gen["origin"] == "raw-url"
        body = gen_path.read_text(encoding="utf-8")
        heads = re.findall(r"^##\s+(.+?)\s*$", body, re.M)
        want = ["Why it works", "What to borrow (principle)", "What to leave",
                "Signature move", "Motion", "Brief", "Image recipe", "Photo search",
                "Reference lock"]
        assert heads == want, f"3: H2 skeleton is {heads}"
        assert "| durations |" in body and "| easings |" in body, "3: no measured motion"
        print(f"3 skeleton  H2s in SCHEMA order ({len(heads)}), motion table prefilled, "
              f"status={gen['status']}")

        # -- 4 never overwrite: the same call again must refuse
        code2, _, err2 = run("aarke", "--origin", "raw-url", "--url", "https://aarke.com",
                             "--catalogue", str(root))
        assert code2 == 1, f"4: second run exited {code2}, expected 1"
        assert "finns redan" in err2, f"4: wrong refusal: {err2.strip()}"
        print(f"4 overwrite exit {code2}  {err2.strip().splitlines()[0][:90]}")

        # -- 5 no URL given: none is invented, and extract falls back
        root2 = tmp / "no-url"
        (root2 / "entries").mkdir(parents=True)
        code3, out3, err3 = run("mystery-site", "--origin", "raw-image",
                                "--catalogue", str(root2), "--json")
        assert code3 == 0, f"5: exit {code3}\n{err3}"
        g3, _ = parse_frontmatter(
            Path(json.loads(out3)["entry"]).read_text(encoding="utf-8"))
        assert g3["url"] == "" and g3["source_url"] == "" and g3["extract"] == "none", \
            f"5: {g3['url']!r} {g3['extract']!r}"
        assert g3["palette"] == [] and g3["type"] == []
        print(f"5 no-url    url={g3['url']!r} extract={g3['extract']!r} "
              f"palette={g3['palette']} type={g3['type']}")

        # -- 6 the other direction: slugs that MUST be refused, nothing created
        root3 = tmp / "bad"
        (root3 / "entries").mkdir(parents=True)
        for label, argv in (("--help", ["--origin", "raw-url", "--catalogue", str(root3),
                                        "--", "--help"]),
                            ("-h", ["--origin", "raw-url", "--catalogue", str(root3),
                                    "--", "-h"]),
                            ("Inte Kebab", ["Inte Kebab", "--origin", "raw-url",
                                            "--catalogue", str(root3)]),
                            ("Aarke", ["Aarke", "--origin", "raw-url",
                                       "--catalogue", str(root3)]),
                            ("trailing-", ["trailing-", "--origin", "raw-url",
                                           "--catalogue", str(root3)])):
            c, _, e = run(*argv)
            assert c != 0, f"6 {label!r}: exit {c} - a junk directory just became possible"
            print(f"6 slug {label!r} exit {c}  {e.strip().splitlines()[-1][:88]}")
        made_dirs = [p.name for p in (root3 / "entries").iterdir()]
        assert made_dirs == [], f"6: refused slugs still created {made_dirs}"

        # -- 7 bare --help is argparse's own flag: help text, exit 0, no directory
        root4 = tmp / "helpflag"
        (root4 / "entries").mkdir(parents=True)
        c7, o7, _ = run("--help")
        assert c7 == 0 and "--origin" in o7, "7: --help should print usage"
        assert [p.name for p in (root4 / "entries").iterdir()] == []
        print(f"7 bare --help exit {c7}, usage printed, no directory created")

        print("\nscaffold_entry: all seven cases behaved as specified.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
