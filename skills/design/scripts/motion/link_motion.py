#!/usr/bin/env python3
"""link_motion.py [project_dir] [--check] [--json]

Wires a project to the machine's ONE global GSAP + Lenis install
(%APPDATA%/npm/node_modules/{gsap,lenis}, see "Global GSAP + Lenis -
Architecture.txt" in anti-slop-design). Never installs, never copies the
libraries. Idempotent; safe to run on every design session.

  1. package.json      created ({"private": true}) when missing.
  2. dependencies      "gsap": "^<global>", "lenis": "^<global>" added when absent.
                       Measured 2026-10-02 (npm 11.6): a bare `npm link gsap lenis`
                       leaves the links *extraneous*, and the next `npm install <x>`
                       prunes both. With semver deps in package.json the links
                       survive every later install, and a deploy (Vercel) installs
                       the same version from the registry - no machine path leaks
                       into package.json the way `npm link --save` (file:../..) does.
  3. npm link gsap lenis  one command, only when node_modules/{gsap,lenis} do not
                       already resolve to the global install.
  4. gsap.js / smooth-scroll.js  copied from templates/ when the project has no
                       central GSAP file yet (searched in ., src, src/lib, lib, app/lib,
                       assets/js). Never overwritten.

Exit 0 when gsap and lenis both resolve to the global install afterwards, 1 otherwise.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATES = HERE / "templates"
GLOBAL = Path(os.environ.get("APPDATA", "")) / "npm" / "node_modules"
CENTRAL_DIRS = (".", "src", "src/lib", "lib", "app/lib", "assets/js", "js")
NO_WINDOW = 0x08000000 if os.name == "nt" else 0  # CREATE_NO_WINDOW: house rule, never flash a console


def global_version(name: str) -> str | None:
    try:
        return json.loads((GLOBAL / name / "package.json").read_text(encoding="utf-8"))["version"]
    except Exception:
        return None


def linked(root: Path, name: str) -> bool:
    p = root / "node_modules" / name
    try:
        return p.exists() and p.resolve() == (GLOBAL / name).resolve()
    except Exception:
        return False


def find_central(root: Path, stem: str) -> Path | None:
    for d in CENTRAL_DIRS:
        for ext in (".js", ".ts", ".mjs"):
            f = root / d / (stem + ext)
            if f.is_file():
                return f
    return None


def run(root: Path, check_only: bool = False) -> dict:
    root = root.resolve()
    st = {"root": str(root), "actions": [], "problems": []}
    versions = {n: global_version(n) for n in ("gsap", "lenis")}
    st["global"] = versions
    if not all(versions.values()):
        st["problems"].append(f"global install missing under {GLOBAL} (gsap={versions['gsap']}, lenis={versions['lenis']}); do NOT npm install, tell Anton")
        st["ok"] = False
        return st
    if root == Path.home().resolve() or root.parent == root:
        st["problems"].append("refusing to link the home directory or a drive root")
        st["ok"] = False
        return st

    pkg_path = root / "package.json"
    if not check_only:
        pkg = {}
        if pkg_path.exists():
            try:
                pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
            except Exception as e:
                st["problems"].append(f"package.json unreadable ({e}); left untouched")
                pkg = None
        else:
            pkg = {"name": root.name.lower().replace(" ", "-"), "private": True}
            st["actions"].append("created package.json")
        if pkg is not None:
            deps = pkg.setdefault("dependencies", {})
            dev = pkg.get("devDependencies", {})
            changed = False
            for n, v in versions.items():
                spec = deps.get(n) or dev.get(n)
                if spec is None:
                    deps[n] = "^" + v
                    changed = True
                elif not spec.lstrip("^~=v").startswith(v.split(".")[0] + "."):
                    st["problems"].append(f"package.json pins {n}@{spec}, global is {v}: left as is, decide before linking")
            if changed or not pkg_path.exists():
                pkg_path.write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")
                if changed:
                    st["actions"].append("added gsap/lenis semver deps to package.json")

        need = [n for n in versions if not linked(root, n)]
        pinned_elsewhere = any("pins" in p for p in st["problems"])
        if need and not pinned_elsewhere:
            npm = shutil.which("npm.cmd") or shutil.which("npm") or "npm"
            # ONE command for both: never `npm link a` then `npm link b` (older npm prunes a).
            r = subprocess.run([npm, "link", "gsap", "lenis", "--no-audit", "--no-fund"], cwd=root,
                               capture_output=True, text=True, timeout=60, creationflags=NO_WINDOW)
            if r.returncode != 0:
                st["problems"].append("npm link failed: " + (r.stderr or r.stdout).strip()[-300:])
            else:
                st["actions"].append("npm link gsap lenis")

        for stem in ("gsap", "smooth-scroll"):
            if find_central(root, stem) is None:
                shutil.copyfile(TEMPLATES / (stem + ".js"), root / (stem + ".js"))
                st["actions"].append(f"wrote {stem}.js from template")

    st["linked"] = {n: linked(root, n) for n in versions}
    st["central"] = {s: str(find_central(root, s) or "") for s in ("gsap", "smooth-scroll")}
    st["ok"] = all(st["linked"].values())
    return st


def summary(st: dict) -> str:
    if st.get("ok"):
        acts = "; ".join(st["actions"]) or "already linked"
        return (f"GSAP {st['global']['gsap']} + Lenis {st['global']['lenis']} linked from the global install ({acts}). "
                f"Central files: {st['central']['gsap'] or '-'}, {st['central']['smooth-scroll'] or '-'}.")
    return "GSAP/Lenis NOT linked: " + " | ".join(st["problems"] or ["unknown"])


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    st = run(Path(args[0] if args else "."), check_only="--check" in sys.argv)
    print(json.dumps(st, indent=1) if "--json" in sys.argv else summary(st))
    sys.exit(0 if st.get("ok") else 1)
