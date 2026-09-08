#!/usr/bin/env python
"""Alunix A/B r7 harness. Thin wrapper over r6's run.py: same subcommands and
spawn/argv logic, r7's own runs/logs/probes/board paths, a 2-concept PORTS map
(K1/K2 only), a --model flag (default claude-sonnet-5, r6 is pinned to fable),
and per-round logs (--round N) plus file-based resume/probe prompts
(--prompt-file) for build/probe.

    python tests/alunix-ab-r7/run.py probe A|B [--dry-run] [--prompt-file PATH]
    python tests/alunix-ab-r7/run.py build A|B [K1 K2] [--dry-run] [--round N]
                                     [--prompt-file PATH] [--resume]
    python tests/alunix-ab-r7/run.py board
    python tests/alunix-ab-r7/run.py reveal

r6run.R6 / r6run.PLUGIN_SHIM are deliberately left untouched: arm B reuses
r6's own plugin-b shim (tests/alunix-ab-r6/plugin-b), which is computed at
r6's import time from r6's own file location, not from whoever imports it.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

R7 = Path(__file__).resolve().parent
sys.path.insert(0, str(R7.parent / "alunix-ab-r6"))
import run as r6run  # noqa: E402

RUNS = R7 / "runs"
LOGS = R7 / "logs"
PROBES = R7 / "probes"
BOARD = R7 / "board"
PROMPT_MD = R7 / "PROMPT.md"
CONCEPTS_MD = R7 / "concepts.md"
BRIEF_MD = R7 / "brief.md"
PORTS = {"K1": 3201, "K2": 3202}
DEFAULT_MODEL = "claude-sonnet-5"

r6run.RUNS = RUNS
r6run.LOGS = LOGS
r6run.PROBES = PROBES
r6run.BOARD = BOARD
r6run.PROMPT_MD = PROMPT_MD
r6run.CONCEPTS_MD = CONCEPTS_MD
r6run.BRIEF_MD = BRIEF_MD
r6run.PORTS = PORTS


def cmd_probe(args) -> None:
    if args.prompt_file:
        args.prompt = Path(args.prompt_file).read_text(encoding="utf-8")
    r6run.MODEL = args.model
    r6run.cmd_probe(args)


def cmd_build(args) -> None:
    r6run.LOGS = LOGS / f"round-{args.round}" if args.round is not None else LOGS
    if args.prompt_file:
        # r6 applies .format(out=...) to the resume prompt; escape literal braces.
        r6run.RESUME_PROMPT = (Path(args.prompt_file).read_text(encoding="utf-8")
                               .replace("{", "{{").replace("}", "}}").replace("{{out}}", "{out}"))
    if args.prompt_file:
        args.resume = True
    if args.resume and args.round is not None:
        # Continue the session from the newest earlier round: copy its meta into
        # this round's log dir so r6's resume finds the session id there.
        import shutil, re
        RE_ROUND = re.compile(r'round-(\d+)$')
        for k in (args.keys or list(r6run.PORTS)):
            dst = r6run.LOGS / f"{args.arm}-{k}.meta.json"
            if dst.exists():
                continue
            prev = sorted((d for d in LOGS.glob("round-*") if d.is_dir()
                           and (m := RE_ROUND.match(d.name)) and int(m.group(1)) < args.round),
                          key=lambda d: int(d.name.split("-")[1]))
            for d in reversed(prev):
                src = d / f"{args.arm}-{k}.meta.json"
                if src.exists():
                    r6run.LOGS.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                    break
    r6run.MODEL = args.model
    r6run.cmd_build(args)


def main(argv: list[str] | None = None) -> None:
    r6run.utf8_console()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--max-budget-usd", default=None)
        p.add_argument("--sysprompt-mode", choices=("auto", "inline", "file"), default="auto",
                       help="arm A: how the baseline body is appended (auto = file flag if `claude --help` lists it)")
        p.add_argument("--model", default=DEFAULT_MODEL)

    p = sub.add_parser("probe"); p.add_argument("arm", choices=r6run.ARMS); common(p)
    p.add_argument("--prompt", default=None, help="override the built-in probe prompt ({arm} is substituted)")
    p.add_argument("--prompt-file", default=None, help="file whose text overrides the probe prompt")
    p.add_argument("--tag", default="", help="suffix for the probe log name, e.g. '2' -> probes/B2.jsonl")

    p = sub.add_parser("build"); p.add_argument("arm", choices=r6run.ARMS); p.add_argument("keys", nargs="*")
    p.add_argument("--sequential", action="store_true"); common(p)
    p.add_argument("--resume", action="store_true",
                   help="continue the cell's interrupted session (session-id from its meta, log appended)")
    p.add_argument("--round", type=int, default=None,
                   help="logs go to logs/round-N instead of logs/ directly")
    p.add_argument("--prompt-file", default=None,
                   help="file whose text becomes the resume prompt; implies --resume")

    sub.add_parser("board").add_argument("--dry-run", action="store_true")
    sub.add_parser("reveal").add_argument("--dry-run", action="store_true")

    args = ap.parse_args(argv)
    {"probe": cmd_probe, "build": cmd_build,
     "board": r6run.cmd_board, "reveal": r6run.cmd_reveal}[args.cmd](args)


if __name__ == "__main__":
    main()
