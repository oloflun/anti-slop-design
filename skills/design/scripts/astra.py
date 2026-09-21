"""Ask Codex for an independent review of a screenshot set: prompt in, verdict out.

Replaces the `Agent(codex-review)` wrapper, whose Opus sub-agent re-did the
measurement work before asking the question. One round cost **305,000 Opus
tokens** — and inside that, the actual Codex call was *one* request: 24 images
in, **6.3 kB of text out**, billed to the OpenAI quota. The verdict costs almost
nothing; the wrapper was the whole expense.

This drives `codex exec` straight from the shell, read-only, with the images
attached and the prompt fed on stdin. It never opens a browser and never edits
the page: screenshots come from a capture script, the prompt comes from you, and
the answer is written to a file.

    python scripts/astra.py PROMPT.md "shots/r24/*.png" reviews/r24-codex.txt

Two failure modes are refused by construction, and both matter:

- **An empty response is an error, not "no findings."** A silent Codex is
  indistinguishable from a clean page if you let it be, so a reply under
  `MIN_REPLY_CHARS` exits non-zero.
- **More than `MAX_IMAGES` images is a hard stop.** Past ~28 the answer turns to
  sludge, so the selection is narrowed, never padded.

What you must not drop along with the wrapper: the wrapper checked every Codex
finding against the file and the pixels before releasing it, and most findings
died there. **The verdict is a draft, never a finding.** Nothing here does that
verification for you.
"""
import argparse
import glob
import subprocess
import sys
from pathlib import Path

# Both are passed on every run because a local default must not decide the depth
# of a verdict: ~/.codex/config.toml ships reasoning effort `low`, which is not
# the level these reviews were asked for.
MODEL = "gpt-6-astra"
REASONING_EFFORT = "medium"

# r21 attached 24 images. Past ~28 the answer stops being a review and becomes a
# blur. The cap is a stop, not a target — narrow the selection, never pad it.
MAX_IMAGES = 28

# A reply shorter than this is a silent failure, not a clean bill of health.
MIN_REPLY_CHARS = 200

EXAMPLES = """\
    python scripts/astra.py PROMPT.md "shots/r24/*.png" reviews/r24-codex.txt
    python scripts/astra.py prompt.md "shots/r24/s*.png" out/r24.md
"""


def build_command(images: list[str]) -> list[str]:
    cmd = [
        "codex", "exec",
        "-m", MODEL,
        "-c", f'model_reasoning_effort="{REASONING_EFFORT}"',
        # Read-only: the reviewer reads the code and the pixels, it never edits
        # the build. Stated on the command line rather than left to the config
        # default, so no later config change can silently widen it.
        "--sandbox", "read-only",
        # The cell under review is usually untracked scratch work.
        "--skip-git-repo-check",
    ]
    for p in images:
        cmd += ["-i", p]
    cmd += ["-"]  # "-" tells codex to read the prompt from stdin
    return cmd


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Ask Codex to review a screenshot set; write the answer to a file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EXAMPLES,
    )
    ap.add_argument("prompt_file", help="file holding the review prompt")
    ap.add_argument("image_glob", help='glob for the images to attach, e.g. "shots/*.png"')
    ap.add_argument("out_file", help="where the answer is written; parent dirs are created")
    args = ap.parse_args()

    images = sorted(glob.glob(args.image_glob))
    if not images:
        sys.exit(f"astra.py: no images match {args.image_glob}")
    if len(images) > MAX_IMAGES:
        sys.exit(f"astra.py: {len(images)} images, the cap is {MAX_IMAGES} "
                 f"— narrow the selection")

    prompt = Path(args.prompt_file).read_text(encoding="utf-8")

    print(f"codex {MODEL}/{REASONING_EFFORT}, {len(images)} images", flush=True)
    r = subprocess.run(build_command(images), input=prompt,
                       capture_output=True, text=True, encoding="utf-8")

    # Written before any guard, so a failed run still leaves what Codex said on
    # disk to be read. An empty file is itself evidence that it said nothing.
    reply = r.stdout or ""
    out = Path(args.out_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(reply, encoding="utf-8")
    print(f"{len(images)} images, {len(reply)} chars -> {out.resolve()}")

    if r.returncode != 0:
        sys.stderr.write((r.stderr or "")[-2000:] + "\n")
        sys.exit(r.returncode)
    if len(reply) < MIN_REPLY_CHARS:
        sys.exit(f"astra.py: reply is {len(reply)} chars, under {MIN_REPLY_CHARS} "
                 f"— a silent Codex is an error, not \"no findings\"")


if __name__ == "__main__":
    main()
