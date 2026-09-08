#!/usr/bin/env python
"""Alunix A/B r6 harness. Stdlib only.

One headless `claude -p` process per cell (arm, concept). Arm A = design
chain off (baseline frontend-design skill body appended to the system prompt,
all hooks killed, skills disabled). Arm B = design chain on (this repo loaded
as a plugin, the older super-intelligence copy of the same hooks disabled).

    python tests/alunix-ab-r6/run.py probe A|B            [--dry-run]
    python tests/alunix-ab-r6/run.py build A|B [K1 K2 K3] [--dry-run] [--sequential] [--max-budget-usd X]
    python tests/alunix-ab-r6/run.py board
    python tests/alunix-ab-r6/run.py reveal

--dry-run prints the exact argv (system prompt abbreviated to sha256+length)
and the NAMES of env keys added, and spawns nothing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
R6 = REPO / "tests" / "alunix-ab-r6"
RUNS = R6 / "runs"
LOGS = R6 / "logs"
PROBES = R6 / "probes"
BOARD = R6 / "board"
PROMPT_MD = R6 / "PROMPT.md"
CONCEPTS_MD = R6 / "concepts.md"
BRIEF_MD = R6 / "brief.md"

PORTS = {"K1": 3101, "K2": 3102, "K3": 3103}
ARMS = ("A", "B")
MODEL = "claude-fable-5-1"
EFFORT = "high"
SECRETS = Path.home() / ".secrets" / ".env"
SECRET_PREFIX = "UNSPLASH_"
BASELINE_SKILL = (Path.home() / ".claude" / "plugins" / "cache" / "claude-plugins-official"
                  / "frontend-design" / "9a881c919fa4" / "skills" / "frontend-design" / "SKILL.md")
PLUGIN_DIR = REPO
# The repo manifest carries "defaultEnabled": false, which makes --plugin-dir load
# nothing (probe B, 2026-09-05). Arm B therefore points at a shim: the same manifest
# minus that flag, plus directory junctions to the repo's hooks/ and agents/.
PLUGIN_SHIM = R6 / "plugin-b"
SETTINGS_B = json.dumps({"enabledPlugins": {"super-intelligence@super-intelligence": False}},
                        separators=(",", ":"))
SYSPROMPT_FLAG_FILE = "--append-system-prompt-file"
SYSPROMPT_FLAG_INLINE = "--append-system-prompt"
PLACEHOLDERS = ("{{KONCEPT}}", "{{UT_MAPP}}", "{{PORT}}")
WIN_CMDLINE_LIMIT = 32000  # CreateProcess hard limit is 32767 chars

RESUME_PROMPT = (
    "Sessionen avbröts av en användningsgräns, inte av dig. Fortsätt uppdraget där du slutade: "
    "titta på vad som redan finns i {out}, slutför det som saknas enligt den ursprungliga prompten "
    "(sidan, verifieringen med skärmbilder som du tittar på, assets, shots och NOTES.md) och avsluta "
    "som prompten säger. Bygg inte om det som redan är klart."
)
PROBE_PROMPT = (
    "Skriv filen tests/alunix-ab-r6/probes/{arm}.html med en <h1> och en inline-stil som "
    "använder hexfärgen #1E5E9C. Svara sedan med en lista över alla skills du har "
    "tillgängliga (namnen), eller 'inga', och säg om du har ett verktyg som heter Skill."
)


# ----------------------------------------------------------------------------- helpers

def die(msg: str, code: int = 2) -> None:
    print(f"run.py: {msg}", file=sys.stderr)
    sys.exit(code)


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def plugin_shim() -> Path:
    """Build (idempotently) the arm-B plugin dir: repo manifest without
    defaultEnabled, junctions to the repo's hooks/ and agents/ (mklink /J needs
    no admin). Hook paths therefore resolve under this repo, which is what the
    monitor classifies as 'repo'."""
    man_dir = PLUGIN_SHIM / ".claude-plugin"
    man_dir.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    manifest.pop("defaultEnabled", None)
    (man_dir / "plugin.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    for name in ("hooks", "agents"):
        link = PLUGIN_SHIM / name
        target = REPO / name
        if link.exists():
            continue
        if os.name == "nt":
            subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)],
                           check=True, capture_output=True)
        else:
            link.symlink_to(target, target_is_directory=True)
    (PLUGIN_SHIM / ".gitignore").write_text("*\n", encoding="utf-8")
    return PLUGIN_SHIM


def resolve_claude() -> str:
    """Full path to the claude executable. The npm shim on PATH is claude.CMD,
    which would route argv through cmd.exe and mangle quotes/newlines, so we
    call the native binary the shim wraps (bin/claude.exe) directly.
    ALUNIX_CLAUDE_BIN overrides (the npm CLI 2.1.241 rejects claude-fable-5-1;
    the desktop app bundles a newer binary under AppData/Roaming/Claude/claude-code/)."""
    override = os.environ.get("ALUNIX_CLAUDE_BIN", "").strip()
    if override:
        if not Path(override).is_file():
            die(f"ALUNIX_CLAUDE_BIN not a file: {override}")
        return override
    found = shutil.which("claude")
    if not found:
        die("claude not found on PATH")
    p = Path(found)
    if p.suffix.lower() in (".cmd", ".bat"):
        native = p.parent / "node_modules" / "@anthropic-ai" / "claude-code" / "bin" / "claude.exe"
        if native.is_file():
            return str(native)
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            txt = ""
        m = re.search(r'"%dp0%\\([^"]+\.exe)"', txt)
        if m:
            cand = p.parent / m.group(1)
            if cand.is_file():
                return str(cand)
        die(f"claude resolves to a .cmd shim ({p}) and its native binary could not be located")
    return str(p)


_HELP_CACHE: dict[str, str] = {}


def claude_help(exe: str) -> str:
    if exe not in _HELP_CACHE:
        try:
            r = subprocess.run([exe, "--help"], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=60)
            _HELP_CACHE[exe] = (r.stdout or "") + (r.stderr or "")
        except Exception as e:  # noqa: BLE001
            print(f"run.py: warning: `claude --help` failed ({e}); assuming inline system prompt flag",
                  file=sys.stderr)
            _HELP_CACHE[exe] = ""
    return _HELP_CACHE[exe]


def sysprompt_flag(exe: str, mode: str) -> str:
    """Prefer --append-system-prompt-file when `claude --help` lists it."""
    if mode == "file":
        return SYSPROMPT_FLAG_FILE
    if mode == "inline":
        return SYSPROMPT_FLAG_INLINE
    listed = re.search(r"(^|\s)" + re.escape(SYSPROMPT_FLAG_FILE) + r"(\s|$)", claude_help(exe))
    return SYSPROMPT_FLAG_FILE if listed else SYSPROMPT_FLAG_INLINE


def baseline_body() -> str:
    if not BASELINE_SKILL.is_file():
        die(f"baseline skill not found: {BASELINE_SKILL}")
    text = BASELINE_SKILL.read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n.*?\r?\n---\r?\n", text, flags=re.S)
    body = text[m.end():] if m else text
    body = body.strip("\r\n") + "\n"
    if not body.strip():
        die("baseline skill body is empty after stripping frontmatter")
    return body


def secrets_env() -> dict[str, str]:
    """Only UNSPLASH_* keys from the secrets file. Values are never printed."""
    out: dict[str, str] = {}
    if not SECRETS.is_file():
        print(f"run.py: warning: secrets file missing ({SECRETS}); no {SECRET_PREFIX}* forwarded",
              file=sys.stderr)
        return out
    for raw in SECRETS.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        if not k.startswith(SECRET_PREFIX):
            continue
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        if v:
            out[k] = v
    return out


def abbreviate_argv(argv: list[str], sysprompt: str | None) -> list[str]:
    """argv with the appended system prompt replaced by sha256/length."""
    out = list(argv)
    for i, a in enumerate(out):
        if a == SYSPROMPT_FLAG_INLINE and i + 1 < len(out) and sysprompt is not None:
            out[i + 1] = f"<system-prompt sha256={sha256_text(sysprompt)} len={len(sysprompt)}>"
    return out


# ----------------------------------------------------------------------------- cell spec

class Cell:
    def __init__(self, arm: str, key: str, prompt: str, log: Path, stderr: Path, meta: Path,
                 out_dir: Path | None):
        self.arm, self.key, self.prompt = arm, key, prompt
        self.log, self.stderr, self.meta, self.out_dir = log, stderr, meta, out_dir
        self.session_id = str(uuid.uuid4())
        self.resume = False  # continue an interrupted session (same id, log appended)
        self.argv: list[str] = []
        self.env: dict[str, str] = {}
        self.env_added: list[str] = []
        self.sysprompt: str | None = None
        self.sysprompt_path: Path | None = None
        self.result: dict = {}
        self.result_lines: list[int] = []
        self.exit_code: int | None = None
        self.start = self.end = ""
        self.proc: subprocess.Popen | None = None

    @property
    def name(self) -> str:
        return f"{self.arm}-{self.key}"


def build_cell(cell: Cell, exe: str, sysprompt_mode: str, budget: str | None) -> None:
    argv = [exe, "-p", cell.prompt,
            "--model", MODEL, "--effort", EFFORT,
            "--output-format", "stream-json", "--verbose", "--include-hook-events",
            "--dangerously-skip-permissions",
            ("--resume" if cell.resume else "--session-id"), cell.session_id,
            "--no-chrome"]
    env = dict(os.environ)
    added: list[str] = []
    for k, v in secrets_env().items():
        env[k] = v
        added.append(k)

    if cell.arm == "A":
        body = baseline_body()
        cell.sysprompt = body
        flag = sysprompt_flag(exe, sysprompt_mode)
        argv += ["--setting-sources", "project", "--disable-slash-commands"]
        if flag == SYSPROMPT_FLAG_FILE:
            LOGS.mkdir(parents=True, exist_ok=True)
            cell.sysprompt_path = LOGS / "arm-A-system-prompt.md"
            cell.sysprompt_path.write_text(body, encoding="utf-8")
            argv += [flag, str(cell.sysprompt_path)]
        else:
            argv += [flag, body]
        env["CLAUDE_HOOKS_DISABLED"] = "1"
        added.append("CLAUDE_HOOKS_DISABLED")
    elif cell.arm == "B":
        argv += ["--plugin-dir", str(plugin_shim()), "--settings", SETTINGS_B]
    else:
        die(f"unknown arm {cell.arm!r}")

    if budget:
        argv += ["--max-budget-usd", str(budget)]

    cmdline_len = len(subprocess.list2cmdline(argv))
    if cmdline_len > WIN_CMDLINE_LIMIT:
        die(f"{cell.name}: command line is {cmdline_len} chars (> {WIN_CMDLINE_LIMIT}); "
            f"shorten PROMPT.md or use --sysprompt-mode file")

    cell.argv, cell.env, cell.env_added = argv, env, sorted(set(added))


def print_dry_run(cell: Cell) -> None:
    print(f"=== {cell.name}  (dry-run, nothing spawned)")
    print(f"cwd: {REPO}")
    print(f"session-id: {cell.session_id}")
    print(f"log: {cell.log}")
    print(f"stderr: {cell.stderr}")
    print(f"meta: {cell.meta}")
    if cell.out_dir:
        print(f"out dir: {cell.out_dir}")
    print("argv:")
    print(json.dumps(abbreviate_argv(cell.argv, cell.sysprompt), ensure_ascii=False, indent=1))
    print(f"env keys added: {cell.env_added or '(none)'}")
    print()


# ----------------------------------------------------------------------------- spawning

def _pump(cell: Cell, log_fh) -> None:
    """Stream child stdout into the log as it arrives; note result lines."""
    assert cell.proc and cell.proc.stdout
    n = 0
    for raw in iter(cell.proc.stdout.readline, b""):
        n += 1
        log_fh.write(raw)
        log_fh.flush()
        try:
            obj = json.loads(raw.decode("utf-8", errors="replace"))
        except ValueError:
            continue
        if isinstance(obj, dict) and obj.get("type") == "result":
            cell.result_lines.append(n)
            cell.result = {k: obj.get(k) for k in ("subtype", "is_error", "num_turns",
                                                   "duration_ms", "total_cost_usd", "session_id")}


def spawn(cell: Cell) -> threading.Thread:
    cell.log.parent.mkdir(parents=True, exist_ok=True)
    cell.stderr.parent.mkdir(parents=True, exist_ok=True)
    if cell.out_dir:
        cell.out_dir.mkdir(parents=True, exist_ok=True)
    cell.start = now_iso()
    log_fh = open(cell.log, "ab" if cell.resume else "wb")
    err_fh = open(cell.stderr, "ab" if cell.resume else "wb")
    cell.proc = subprocess.Popen(cell.argv, cwd=str(REPO), env=cell.env,
                                 stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=err_fh)

    def run() -> None:
        try:
            _pump(cell, log_fh)
        finally:
            cell.exit_code = cell.proc.wait()
            cell.end = now_iso()
            log_fh.close()
            err_fh.close()
            write_meta(cell)

    t = threading.Thread(target=run, name=cell.name, daemon=True)
    t.start()
    print(f"[{cell.name}] started pid={cell.proc.pid} session={cell.session_id}")
    return t


def write_meta(cell: Cell) -> None:
    meta = {
        "arm": cell.arm,
        "key": cell.key,
        "session_id": cell.session_id,
        "model": MODEL,
        "effort": EFFORT,
        "cwd": str(REPO),
        "out_dir": str(cell.out_dir) if cell.out_dir else None,
        "argv": abbreviate_argv(cell.argv, cell.sysprompt),
        "system_prompt_sha256": sha256_text(cell.sysprompt) if cell.sysprompt else None,
        "system_prompt_len": len(cell.sysprompt) if cell.sysprompt else None,
        "system_prompt_file": str(cell.sysprompt_path) if cell.sysprompt_path else None,
        "prompt_sha256": sha256_text(cell.prompt),
        "prompt_md_sha256": sha256_text(PROMPT_MD.read_text(encoding="utf-8")) if PROMPT_MD.is_file() else None,
        "env_keys_added": cell.env_added,
        "start": cell.start,
        "end": cell.end,
        "exit_code": cell.exit_code,
        "result_line_numbers": cell.result_lines,
        "result": cell.result,
        "log": str(cell.log),
        "stderr": str(cell.stderr),
    }
    cell.meta.parent.mkdir(parents=True, exist_ok=True)
    cell.meta.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")


def run_cells(cells: list[Cell], sequential: bool) -> None:
    if sequential:
        for c in cells:
            spawn(c).join()
    else:
        threads = [spawn(c) for c in cells]
        for t in threads:
            t.join()
    print()
    print(f"{'cell':<8} {'exit':>4} {'dur':>9} {'turns':>5} {'cost':>9}  subtype")
    for c in cells:
        r = c.result or {}
        dur = r.get("duration_ms")
        dur_s = f"{dur / 1000:.0f}s" if isinstance(dur, (int, float)) else "-"
        cost = r.get("total_cost_usd")
        cost_s = f"${cost:.2f}" if isinstance(cost, (int, float)) else "-"
        print(f"{c.name:<8} {str(c.exit_code):>4} {dur_s:>9} {str(r.get('num_turns', '-')):>5} "
              f"{cost_s:>9}  {r.get('subtype') or '-'}"
              + ("" if c.result_lines else "  (no result line)"))


# ----------------------------------------------------------------------------- subcommands

def parse_keys(keys: list[str]) -> list[str]:
    keys = keys or list(PORTS)
    bad = [k for k in keys if k not in PORTS]
    if bad:
        die(f"unknown concept key(s) {bad}; expected one of {list(PORTS)}")
    return keys


def cmd_probe(args) -> None:
    arm = args.arm
    prompt = (args.prompt or PROBE_PROMPT).format(arm=arm)
    name = f"{arm}{getattr(args, 'tag', '')}"
    cell = Cell(arm, "probe", prompt,
                log=PROBES / f"{name}.jsonl", stderr=PROBES / f"{name}.stderr.txt",
                meta=PROBES / f"{name}.meta.json", out_dir=None)
    build_cell(cell, resolve_claude(), args.sysprompt_mode, args.max_budget_usd)
    if args.dry_run:
        print_dry_run(cell)
        return
    PROBES.mkdir(parents=True, exist_ok=True)
    run_cells([cell], sequential=True)


def load_prompt_template() -> str:
    if not PROMPT_MD.is_file():
        die(f"PROMPT.md missing: {PROMPT_MD} — write it (with {', '.join(PLACEHOLDERS)}) before build")
    text = PROMPT_MD.read_text(encoding="utf-8")
    missing = [p for p in PLACEHOLDERS if p not in text]
    if missing:
        die(f"PROMPT.md lacks placeholder(s) {missing}")
    return text


def render_prompt(template: str, key: str, out_dir: Path) -> str:
    rel = out_dir.relative_to(REPO).as_posix()
    prompt = (template.replace("{{KONCEPT}}", key)
                      .replace("{{UT_MAPP}}", rel)
                      .replace("{{PORT}}", str(PORTS[key])))
    left = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", prompt)))
    if left:
        die(f"PROMPT.md has unknown placeholder(s) {left}")
    return prompt


def cmd_build(args) -> None:
    arm = args.arm
    keys = parse_keys(args.keys)
    template = load_prompt_template()
    exe = resolve_claude()
    cells: list[Cell] = []
    for k in keys:
        out_dir = RUNS / arm / k
        cell = Cell(arm, k, render_prompt(template, k, out_dir),
                    log=LOGS / f"{arm}-{k}.jsonl", stderr=LOGS / f"{arm}-{k}.stderr.txt",
                    meta=LOGS / f"{arm}-{k}.meta.json", out_dir=out_dir)
        if args.resume:
            # Same session, same flags, same prompt already in context: only a nudge.
            if not cell.meta.is_file():
                die(f"nothing to resume: {cell.meta} missing")
            prev = json.loads(cell.meta.read_text(encoding="utf-8"))
            cell.session_id = prev["session_id"]
            cell.resume = True
            cell.prompt = RESUME_PROMPT.format(out=out_dir.relative_to(REPO).as_posix())
            if not args.dry_run:
                n = 1
                while (cell.meta.with_suffix(f".{n}.json")).exists():
                    n += 1
                cell.meta.rename(cell.meta.with_suffix(f".{n}.json"))
        build_cell(cell, exe, args.sysprompt_mode, args.max_budget_usd)
        cells.append(cell)
    if args.dry_run:
        for c in cells:
            print_dry_run(c)
        return
    run_cells(cells, sequential=args.sequential)


def concept_names() -> dict[str, str]:
    """K -> H2 heading text from concepts.md (id prefix stripped), if present."""
    names: dict[str, str] = {}
    if not CONCEPTS_MD.is_file():
        return names
    for line in CONCEPTS_MD.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^##\s+(.*?)\s*$", line)
        if not m:
            continue
        heading = m.group(1)
        for k in PORTS:
            if re.match(rf"^{k}\b", heading) and k not in names:
                rest = re.sub(rf"^{k}\s*[-–—:.·|]*\s*", "", heading).strip()
                names[k] = rest or heading
    return names


def brief_text() -> str:
    for src in (BRIEF_MD, CONCEPTS_MD):
        if src.is_file():
            for line in src.read_text(encoding="utf-8").splitlines():
                s = line.strip().lstrip("#").strip()
                if s:
                    return s[:200]
    return "Alunix A/B r6"


def load_or_create_mapping() -> dict[str, dict[str, str]]:
    BOARD.mkdir(parents=True, exist_ok=True)
    path = BOARD / "mapping.json"
    if path.is_file():
        mapping = json.loads(path.read_text(encoding="utf-8"))
    else:
        mapping = {}
    rng = random.SystemRandom()
    changed = False
    for k in PORTS:
        if k not in mapping:
            engines = ["1", "2"]
            rng.shuffle(engines)
            mapping[k] = {"A": engines[0], "B": engines[1]}
            changed = True
    if changed:
        path.write_text(json.dumps(mapping, indent=2), encoding="utf-8")
    return mapping


def cmd_board(args) -> None:
    if args.dry_run:
        print(f"(dry-run) would create/read {BOARD / 'mapping.json'}, copy runs/<arm>/<K> -> "
              f"{BOARD / 'cells'} and write board.json; nothing written")
        return
    mapping = load_or_create_mapping()
    names = concept_names()
    cells_dir = BOARD / "cells"
    cells_dir.mkdir(parents=True, exist_ok=True)
    existing: dict[str, bool] = {}
    for k in PORTS:
        for arm in ARMS:
            src = RUNS / arm / k
            engine = mapping[k][arm]
            dst = cells_dir / f"{k}-{engine}"
            if src.is_dir() and any(src.iterdir()):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            existing[f"{k}-{engine}"] = (dst / "index.html").is_file()
    board = {
        "brief": brief_text(),
        "directions": [{"id": k, "name": names.get(k, k), "lane": "", "register": "", "grammar": ""}
                       for k in PORTS],
        "engines": [{"id": "1", "name": "Körning 1"}, {"id": "2", "name": "Körning 2"}],
    }
    (BOARD / "board.json").write_text(json.dumps(board, indent=2, ensure_ascii=False), encoding="utf-8")
    for key in sorted(existing):
        print(f"{key}: {'built' if existing[key] else 'missing'}")
    print(f"board.json written to {BOARD}")


def cmd_reveal(args) -> None:
    path = BOARD / "mapping.json"
    if not path.is_file():
        die(f"no mapping yet: {path} (run `board` first)")
    print(path.read_text(encoding="utf-8"))


def utf8_console() -> None:
    """Windows consoles default to cp1252; prompts and paths carry non-Latin-1 text."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def main(argv: list[str] | None = None) -> None:
    utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--max-budget-usd", default=None)
        p.add_argument("--sysprompt-mode", choices=("auto", "inline", "file"), default="auto",
                       help="arm A: how the baseline body is appended (auto = file flag if `claude --help` lists it)")

    p = sub.add_parser("probe"); p.add_argument("arm", choices=ARMS); common(p)
    p.add_argument("--prompt", default=None, help="override the built-in probe prompt ({arm} is substituted)")
    p.add_argument("--tag", default="", help="suffix for the probe log name, e.g. '2' -> probes/B2.jsonl")
    p = sub.add_parser("build"); p.add_argument("arm", choices=ARMS); p.add_argument("keys", nargs="*")
    p.add_argument("--sequential", action="store_true"); common(p)
    p.add_argument("--resume", action="store_true",
                   help="continue the cell's interrupted session (session-id from its meta, log appended)")
    p = sub.add_parser("board"); p.add_argument("--dry-run", action="store_true")
    p = sub.add_parser("reveal"); p.add_argument("--dry-run", action="store_true")

    args = ap.parse_args(argv)
    {"probe": cmd_probe, "build": cmd_build, "board": cmd_board, "reveal": cmd_reveal}[args.cmd](args)


if __name__ == "__main__":
    main()
