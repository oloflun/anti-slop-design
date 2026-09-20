"""Astra utan wrapper: skicka bilder + prompt rakt till Codex, skriv svaret till fil.

Ersätter Agent(codex-review), vars Opus-wrapper kostade ~300k tokens per runda för att
göra om mätarbetet innan den frågade Codex en (1) gång. Domen kostar nästan ingenting.

    python astra.py PROMPT.md "runs/V3d/shots/r24/*.png" runs/V3d/reviews/r24-codex.txt

Bilder tas med ett eget capture-skript, inte här. Codex körs read-only.
"""
import glob
import subprocess
import sys
from pathlib import Path

MODEL = "gpt-6-astra"
EFFORT = "medium"
MAX_IMGS = 28  # r21 skickade 24; över ~30 blir svaret grötigt


def main():
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    prompt_file, pattern, out_file = sys.argv[1:]

    imgs = sorted(glob.glob(pattern))
    if not imgs:
        sys.exit(f"inga bilder matchar {pattern}")
    if len(imgs) > MAX_IMGS:
        sys.exit(f"{len(imgs)} bilder, taket är {MAX_IMGS} — snäva in urvalet")

    prompt = Path(prompt_file).read_text(encoding="utf-8")

    cmd = ["codex", "exec", "-m", MODEL, "-c", f'model_reasoning_effort="{EFFORT}"',
           "--skip-git-repo-check"]
    for p in imgs:
        cmd += ["-i", p]
    cmd += ["-"]

    print(f"codex {MODEL}/{EFFORT}, {len(imgs)} bilder", flush=True)
    r = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8")

    out = Path(out_file)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(r.stdout or "", encoding="utf-8")

    print(f"exit {r.returncode}, {len(r.stdout or '')} tecken -> {out}")
    if r.returncode != 0:
        print((r.stderr or "")[-2000:], file=sys.stderr)
        sys.exit(r.returncode)
    # Ett tomt svar är ett tyst fel, inte "inga fynd".
    if len(r.stdout or "") < 200:
        sys.exit("svaret är för kort för att vara en granskning")


if __name__ == "__main__":
    main()
