#!/usr/bin/env python
"""Alunix r8 harness. A thin wrapper over tests/alunix-ab-r6/run.py, built the
way r7's wrapper is: r6 owns the engine (argv, spawn, stream-json pump,
meta.json), r8 owns its own paths and patches r6's module-level names. r6 is
never edited.

    python tests/alunix-r8/run.py build B [V3c K3 K4] [--round N]
                                 [--prompt-file PATH] [--resume] [--dry-run]
    python tests/alunix-r8/run.py probe B [--prompt-file PATH] [--dry-run]
    python tests/alunix-r8/run.py board [--dry-run]

What r8 changes, and why (plan § 7.2, § 7.4, § 10.7):

  * PORTS = {"V3c": 3301, "V3d": 3304, "K3": 3302, "K4": 3303}; DEFAULT_MODEL = claude-opus-5
    (every agent in r8 is Opus, builders included).
  * runs/<cell>/, not runs/<arm>/<cell>/: r8 has one arm (B, the chain on) and
    three concepts, so the arm segment is swallowed (see ArmlessRuns).
  * The builders' env gets DESIGN_HOOKS_FORCE_ARM=1. A headless builder never
    receives a UserPromptSubmit, so the design hooks would never arm and the
    route ledger, the reference floor and the Stop report would all stay
    silent - the exact measurement r8 exists to take (hooks/design_hook_lib.py
    armed(): anything but "", "0", "false" arms).
  * The builders' env gets SCROLLCRAFT_CHROME. scroll_verify.py / motion_probe
    fall back to Playwright's bundled headless shell otherwise, which crashes
    mid-screenshot on some pages.
  * The builders' argv gets --disallowed-tools with the Higgsfield MCP's
    generation tools. Only the lead generates material (F-009, plan § 10.7);
    a builder that tries anyway shows up as a denied tool call. It also drops
    whole MCP servers named in DROP_MCP_SERVERS, which is what keeps a fresh
    session's system prompt under the context ceiling (see that constant).
  * Per-round logs (--round N -> logs/round-N/) and a <arm>-<cell>.done marker
    next to each meta.json, so a /loop can wait on a file instead of a guess.

r6run.R6 and r6run.PLUGIN_SHIM are deliberately left alone: arm B reuses r6's
proven plugin-b shim (tests/alunix-ab-r6/plugin-b), whose hooks/ and agents/
junctions point at this repo, so T1-T5 land in the builder sessions directly.

There is no `reveal` subcommand: r8 runs one arm and three named concepts,
so there is nothing blinded to reveal.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

R8 = Path(__file__).resolve().parent
sys.path.insert(0, str(R8.parent / "alunix-ab-r6"))
import run as r6run  # noqa: E402

RUNS = R8 / "runs"
LOGS = R8 / "logs"
PROBES = LOGS / "probe"
BOARD = R8 / "board"
PROMPT_MD = R8 / "PROMPT.md"
CONCEPTS_MD = R8 / "concepts.md"
BRIEF_MD = R8 / "brief.md"

PORTS = {"V3c": 3301, "V3d": 3304, "K3": 3302, "K4": 3303}
DEFAULT_MODEL = "claude-opus-5"

BOARD_PORT = 4626
BOARD_PY = Path.home() / ".agents" / "skills" / "design" / "scripts" / "board.py"
ENGINE_ID = "r8"          # board cells are board/cells/<cell>-r8
BRIEF_FALLBACK = "Alunix r8"

FORCE_ARM_ENV = "DESIGN_HOOKS_FORCE_ARM"
CHROME_ENV = "SCROLLCRAFT_CHROME"
# Same candidates as skills/design/scripts/scroll_verify.py, same reason: a
# real Chrome, because the bundled headless shell has crashed mid-screenshot.
CHROME_CANDIDATES = (
    "C:/Program Files/Google/Chrome/Application/chrome.exe",
    "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/usr/bin/google-chrome", "/usr/bin/google-chrome-stable", "/usr/bin/chromium",
)

# The operations hooks/design_hook_lib.py's GEN_TOOL regex treats as generation
# (and hooks/hooks.json matches for the credit gate). Names come from there, not
# from guesswork. The provider's server segment is a UUID in this install (an
# account connector, so it is in no local config file); ALUNIX_HIGGSFIELD_MCP
# overrides it, comma-separated, if the connector id ever changes.
GEN_OPS = (
    "generate_image", "generate_video", "generate_audio", "generate_3d",
    "generate_image_batch", "generate_video_batch", "generate_audio_batch",
    "upscale_image", "upscale_video",
    "reframe", "remove_background", "outpaint_image", "motion_control",
)
HIGGSFIELD_MCP = ("cef36fd1-bedf-4056-ae8d-c1fde27b3553",)

# Whole MCP servers dropped from a builder's session, by bare server name — the
# CLI removes every tool the server exposes when it is named without a __tool
# suffix (measured 2026-09-21: 478 -> 266 tools, Vercel 212 -> 0).
#
# Vercel is here because its tool surface grew from 37 (r23) to 212 on
# 2026-09-21 and pushed a fresh session's system prompt past the context
# ceiling: the round died on "Prompt is too long" after two turns, before it
# had touched the page. No design round needs Vercel's API, and r23's builders
# ran fine without it mattering. Add a server here only with the same kind of
# measurement, and check the number against the last round that ran.
DROP_MCP_SERVERS = ("mcp__claude_ai_Vercel",)

DRY_RUN_PROMPT = (
    "(torrkoerning: ingen rundprompt angiven - en riktig runda koers med "
    "--prompt-file) Koncept {{KONCEPT}}, ut-mapp {{UT_MAPP}}, port {{PORT}}.\n"
)


# --------------------------------------------------------------------------- paths

class ArmlessRuns:
    """r6's cmd_build computes `out_dir = RUNS / arm / key`. r8 runs a single
    arm and the plan puts a cell's work in runs/<cell>/, so the arm segment is
    swallowed here rather than by forking r6's cmd_build."""

    def __init__(self, root: Path) -> None:
        self.root = root

    def __truediv__(self, _arm: str) -> Path:
        return self.root

    def __fspath__(self) -> str:
        return str(self.root)

    def __str__(self) -> str:
        return str(self.root)


r6run.RUNS = ArmlessRuns(RUNS)
r6run.LOGS = LOGS
r6run.PROBES = PROBES
r6run.BOARD = BOARD
r6run.PROMPT_MD = PROMPT_MD
r6run.CONCEPTS_MD = CONCEPTS_MD
r6run.BRIEF_MD = BRIEF_MD
r6run.PORTS = PORTS


# --------------------------------------------------------------------------- builder cell

def find_chrome() -> str | None:
    for cand in CHROME_CANDIDATES:
        if Path(cand).exists():
            return cand
    return None


def higgsfield_servers() -> list[str]:
    override = [s.strip() for s in os.environ.get("ALUNIX_HIGGSFIELD_MCP", "").split(",") if s.strip()]
    return override or list(HIGGSFIELD_MCP)


def disallowed_tools() -> list[str]:
    ops = [f"mcp__{srv}__{op}" for srv in higgsfield_servers() for op in GEN_OPS]
    return ops + list(DROP_MCP_SERVERS)


_r6_build_cell = r6run.build_cell


def build_cell(cell, exe: str, sysprompt_mode: str, budget: str | None) -> None:
    """r6's cell, plus r8's env and the generation lock-out."""
    _r6_build_cell(cell, exe, sysprompt_mode, budget)
    added = list(cell.env_added)

    cell.env[FORCE_ARM_ENV] = "1"
    added.append(FORCE_ARM_ENV)

    chrome = os.environ.get(CHROME_ENV, "").strip() or find_chrome()
    if chrome:
        cell.env[CHROME_ENV] = chrome
        added.append(CHROME_ENV)
    else:
        print(f"run.py: warning: no installed Chrome found; {CHROME_ENV} not set "
              f"(scroll_verify/motion_probe will fall back to the bundled headless shell)",
              file=sys.stderr)

    # --disallowedTools/--disallowed-tools takes a variadic list (`<tools...>`,
    # verified against `claude --help`), so each name is its own argv element
    # and the flag goes last.
    cell.argv += ["--disallowed-tools", *disallowed_tools()]
    cell.env_added = sorted(set(added))

    n = len(subprocess.list2cmdline(cell.argv))
    if n > r6run.WIN_CMDLINE_LIMIT:
        r6run.die(f"{cell.name}: command line is {n} chars (> {r6run.WIN_CMDLINE_LIMIT}); "
                  f"shorten the round prompt or use --sysprompt-mode file")


r6run.build_cell = build_cell


_r6_write_meta = r6run.write_meta


def write_meta(cell) -> None:
    """r6's meta.json, plus the .done marker the lead's /loop waits on
    (plan § 9.2: `.done`-fil + *.meta.json i logs/round-N/)."""
    _r6_write_meta(cell)
    # R1 (2026-09-10): two builders were cut by the account's usage limit and
    # still got a .done, because the stream's final record says subtype
    # "success" with is_error true. A loop that waits on .done must not read a
    # cut session as finished, so the marker is .failed in that case and the
    # lead's next step is `--resume`, not review.
    failed = bool((cell.result or {}).get("is_error")) or (cell.exit_code not in (0, None))
    marker = cell.meta.with_name(f"{cell.arm}-{cell.key}.{'failed' if failed else 'done'}")
    stale = cell.meta.with_name(f"{cell.arm}-{cell.key}.{'done' if failed else 'failed'}")
    if stale.exists():
        stale.unlink()
    marker.write_text(json.dumps({
        "cell": cell.name,
        "session_id": cell.session_id,
        "exit_code": cell.exit_code,
        "end": cell.end,
        "result": cell.result,
        "failed": failed,
        "meta": str(cell.meta),
    }, indent=2, ensure_ascii=False), encoding="utf-8")


r6run.write_meta = write_meta


# --------------------------------------------------------------------------- prompts

class RoundPrompt(str):
    """r6's resume path replaces the rendered prompt with
    `RESUME_PROMPT.format(out=runs/<cell>)`. r8's round prompts are per-cell
    templates, so `out` is used to recover the cell and the text is rendered
    through r6's own render_prompt() - a resumed round gets exactly the same
    substitution as a fresh one."""

    def format(self, *args, **kwargs) -> str:  # noqa: A003 (str API)
        out = kwargs.get("out")
        if out is None:
            return str(self)
        return r6run.render_prompt(str(self), Path(out).name, r6run.REPO / out)


def round_prompt_text(path: str) -> str:
    """Validate here as well as in r6's render_prompt, so the error names the
    round-prompt file rather than the PROMPT.md it stands in for."""
    text = Path(path).read_text(encoding="utf-8")
    missing = [p for p in r6run.PLACEHOLDERS if p not in text]
    if missing:
        r6run.die(f"{path} lacks placeholder(s) {missing}")
    unknown = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", text)) - set(r6run.PLACEHOLDERS))
    if unknown:
        r6run.die(f"{path} has unknown placeholder(s) {unknown}")
    return text


# --------------------------------------------------------------------------- subcommands

def cmd_probe(args) -> None:
    if args.prompt_file:
        args.prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    r6run.MODEL = args.model
    r6run.cmd_probe(args)


def carry_session_meta(args) -> None:
    """--resume in round N continues the session started in the newest earlier
    round: copy that round's meta into this round's log dir so r6's resume
    finds the session id where it looks."""
    re_round = re.compile(r"round-(\d+)$")
    earlier = sorted((d for d in LOGS.glob("round-*")
                      if d.is_dir() and (m := re_round.match(d.name)) and int(m.group(1)) < args.round),
                     key=lambda d: int(d.name.split("-")[1]))
    for k in (args.keys or list(PORTS)):
        dst = r6run.LOGS / f"{args.arm}-{k}.meta.json"
        if dst.exists():
            continue
        for d in reversed(earlier):
            src = d / f"{args.arm}-{k}.meta.json"
            if src.exists():
                r6run.LOGS.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                break


def cmd_build(args) -> None:
    if args.round is not None:
        r6run.LOGS = LOGS / f"round-{args.round}"

    text: str | None = None
    if args.prompt_file:
        text = round_prompt_text(args.prompt_file)
    elif args.dry_run and not PROMPT_MD.is_file():
        # The dry run exists to show argv, env and flags; the round prompt is
        # the architect's, written per round and passed with --prompt-file.
        print("run.py: no --prompt-file and no PROMPT.md; using a placeholder prompt "
              "for this dry run", file=sys.stderr)
        text = DRY_RUN_PROMPT
    if text is not None:
        r6run.load_prompt_template = lambda t=text: t
        r6run.RESUME_PROMPT = RoundPrompt(text)

    if args.resume and args.round is not None:
        carry_session_meta(args)

    r6run.MODEL = args.model
    r6run.cmd_build(args)


def board_serve_cmd() -> list[str]:
    return ["python", str(BOARD_PY), str(BOARD.relative_to(r6run.REPO).as_posix()),
            "--port", str(BOARD_PORT), "--fallback-root", ".", "--single"]


def board_json() -> dict:
    names = r6run.concept_names()
    brief = r6run.brief_text()
    if brief.startswith("Alunix A/B r6"):  # r6's own fallback string
        brief = BRIEF_FALLBACK
    return {
        "brief": brief,
        "directions": [{"id": k, "name": names.get(k, k), "lane": "", "register": "", "grammar": ""}
                       for k in PORTS],
        "engines": [{"id": ENGINE_ID, "name": "r8"}],
    }


def cmd_board(args) -> None:
    """One engine, three concepts, one cell at a time in full width. No blind
    A/B mapping: r8 compares concepts, not engines."""
    cells_dir = BOARD / "cells"
    if args.dry_run:
        print(f"(dry-run) would write {BOARD / 'board.json'} and copy "
              f"runs/<cell> -> {cells_dir}/<cell>-{ENGINE_ID}; nothing written")
        for k in PORTS:
            print(f"  {k}: {'built' if (RUNS / k / 'index.html').is_file() else 'missing'}")
        print(f"serve: {subprocess.list2cmdline(board_serve_cmd())}")
        print(f"launch.json: alunix-board-r8 - port {BOARD_PORT} - --fallback-root . - --single")
        print("  (one cell at a time, full width - never half-width; that was r5's mistake)")
        return
    cells_dir.mkdir(parents=True, exist_ok=True)
    for k in PORTS:
        src = RUNS / k
        if src.is_dir() and any(src.iterdir()):
            shutil.copytree(src, cells_dir / f"{k}-{ENGINE_ID}", dirs_exist_ok=True)
    (BOARD / "board.json").write_text(json.dumps(board_json(), indent=2, ensure_ascii=False),
                                      encoding="utf-8")
    for k in PORTS:
        built = (cells_dir / f"{k}-{ENGINE_ID}" / "index.html").is_file()
        print(f"{k}-{ENGINE_ID}: {'built' if built else 'missing'}")
    print(f"board.json written to {BOARD}")
    print(f"serve: {subprocess.list2cmdline(board_serve_cmd())}")


# --------------------------------------------------------------------------- cli

def main(argv: list[str] | None = None) -> None:
    r6run.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--max-budget-usd", default=None)
        p.add_argument("--sysprompt-mode", choices=("auto", "inline", "file"), default="auto",
                       help="arm A only: how the baseline body is appended")
        p.add_argument("--model", default=DEFAULT_MODEL)

    p = sub.add_parser("probe"); p.add_argument("arm", choices=r6run.ARMS); common(p)
    p.add_argument("--prompt", default=None, help="override the built-in probe prompt ({arm} is substituted)")
    p.add_argument("--prompt-file", default=None, help="file whose text overrides the probe prompt")
    p.add_argument("--tag", default="", help="suffix for the probe log name, e.g. '2' -> logs/probe/B2.jsonl")

    p = sub.add_parser("build"); p.add_argument("arm", choices=r6run.ARMS)
    p.add_argument("keys", nargs="*", help=f"cells to build (default: all of {list(PORTS)})")
    p.add_argument("--sequential", action="store_true"); common(p)
    p.add_argument("--resume", action="store_true",
                   help="continue the cell's session from an earlier round (session id from its meta)")
    p.add_argument("--round", type=int, default=None,
                   help="logs go to logs/round-N instead of logs/ directly")
    p.add_argument("--prompt-file", default=None,
                   help="the round prompt; must carry " + ", ".join(r6run.PLACEHOLDERS))

    sub.add_parser("board").add_argument("--dry-run", action="store_true")

    args = ap.parse_args(argv)
    {"probe": cmd_probe, "build": cmd_build, "board": cmd_board}[args.cmd](args)


if __name__ == "__main__":
    main()
