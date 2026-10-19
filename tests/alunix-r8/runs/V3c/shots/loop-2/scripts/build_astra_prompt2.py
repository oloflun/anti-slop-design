"""Builds the Astra (codex) prompt for loop-2 and the ordered -i image list."""
from pathlib import Path

ROOT = Path("C:/Users/Anton L/anti-slop-design")
CELL = ROOT / "tests/alunix-r8/runs/V3c"
SHOTS = CELL / "shots/loop-2"
OUT = Path(__file__).with_name("astra2-prompt.txt")
IMGS = Path(__file__).with_name("astra2-images.txt")

groups = [
    ("slices-1440", sorted((SHOTS / "slices-1440").glob("*.png")),
     "full-page slice {i} at 1440x900, scrollY = {i}*900"),
    ("slices-390", sorted((SHOTS / "slices-390").glob("*.png")),
     "full-page slice {i} at 390x844, scrollY = {i}*844"),
    ("preview-1440", [SHOTS / "preview" / f"preview-1440-{m}.png" for m in
      ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]],
     "?preview={m} at 1440x900 (formed state, shim frozen)"),
    ("preview-390", [SHOTS / "preview" / f"preview-390-{m}.png" for m in
      ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]],
     "?preview={m} at 390x844"),
    ("flip-1440", sorted((SHOTS / "flip-1440").glob("*.png")),
     "hero card, --flip forced to {f} at 1440x900 (12 steps 0 to 1)"),
    ("flip-390", sorted((SHOTS / "flip-390").glob("*.png")),
     "hero card, --flip forced to {f} at 390x844"),
    ("process-1440", sorted((SHOTS / "process-1440").glob("*.png")),
     "#process act, frame {i} of 12 through its visible life at 1440x900 (from top-vh to bottom)"),
    ("process-390", sorted((SHOTS / "process-390").glob("*.png")),
     "#process act, frame {i} of 12 at 390x844"),
]

lines, paths, n = [], [], 0
for name, files, desc in groups:
    for j, f in enumerate(files):
        n += 1
        stem = f.stem
        if name.startswith("preview"):
            d = desc.format(m=stem.split("-", 2)[2])
        elif name.startswith("flip"):
            d = desc.format(f=int(stem[-3:]) / 100)
        else:
            d = desc.format(i=j)
        lines.append(f"{n:3d}. {f.name}  -  {d}")
        paths.append(str(f))

helhet = (CELL / "HELHET.md").read_text(encoding="utf-8")

prompt = f"""You are the fifth reviewer (Astra) on a hand-built Swedish agency marketing page, in the
WHOLE-PAGE loop (Fas C, round 2 of max 6). REVIEW ONLY: return findings, never a patch, never
a rewritten file. You are read-only.

## Target

File to review (read it in full yourself, one HTML file with inline CSS and JS, R7 state,
md5 d30355da):
  tests/alunix-r8/runs/V3c/index.html
Brief and decision ledger (device table, authored silence, the builder's R7 rows):
  tests/alunix-r8/runs/V3c/BRIEF.md
The whole-page reference floor you review against (ALSO pasted in full below; the
architect's loop-1 ticks are in it, they refer to the R6 state and are being re-ticked now):
  tests/alunix-r8/runs/V3c/HELHET.md
Your own loop-1 report and how each finding was judged (do not re-report what was taken):
  tests/alunix-r8/runs/V3c/reviews/loop-1-astra.md
What R7 built (eight plans 025, 017, 012, 013, 014, 015, 016, 026) and its gate numbers:
  tests/alunix-r8/runs/V3c/NOTES.md, section "## R7 (2026-09-17)"
The vendored scroll engine, reference only, never edited:
  tests/alunix-r8/runs/V3c/scroll/scrollcraft.js, scrollcraft.css, sc-smooth.js
Repo root is the working directory. All paths are relative to it.

## Already known for round 2 (verified by the lead and the architect; do not spend your
## budget re-finding them, but say if your read of the pixels or the code differs)

K1. The two iframes never wake up again once put to sleep: the IntersectionObserver
    observes the IFRAME, whose wrapper gets content-visibility:hidden (.is-asleep), and an
    element inside a content-visibility:hidden subtree has no box, so the observer reports
    it as not intersecting forever (index.html:1676-1688, .is-asleep at :639). Slices 4 and 5
    at 1440 and slice 4 to 6 at 390 show the Calyx and Horai frames as flat empty plates.
    The fix (observe the wrapper) is proven in-page and is plan 027.
K2. The ground drift after plan 017 A reads as a blue wash over the entire photograph
    (right-margin ground pixel (8,23,37) at the band vs (20,20,22) in the fold; chroma 29).
    H-19 asked for >= 12 RGB steps, not a colour cast. Measured alternative: tone layer at
    40 % instead of 62 % gives (12,22,31), delta 13, chroma 19. Plan 028.
K3. The giant headline at 6rem breaks the locked word as VARUMÄRK / E. (hyphens:auto has no
    Swedish dictionary in Chrome on Windows; the word is 601 px at 96 px in a 555 px column).
    Measured: 88 px at -0.04em is 542 px and holds; at 1280 the column is 480 px. Plan 029.
K4. Frame time. CDP attribution at 4x CPU, 100 px / 60 ms wheel: one --sc-ps write on
    section.hero costs 1.8 ms of style recalc (0.5 ms with .plate-card display:none), on
    #process 2.2 ms (0.7 ms with the sheet hidden), on #giant-section 2.0 ms (0.4 ms with
    the ledger hidden); a --sc-canvas write on :root costs 9 ms (0.24 ms when written on
    .ground instead). The engine writes --sc-p on every act every frame and --sc-canvas on
    :root every frame (scrollcraft.js:857, :983). Control fixture: 0.17 ms per write.
    The architect is writing the plan for this; if you see a cheaper cut in the code, name
    it with file:line and the mechanism.

Q30 (restacking the two-column band into five full-width acts) is an open question to the
owner. Do not propose the restack again; judge the band as two columns with 017's air and
offset.

## Attached images, in order (you cannot see file names, so here they are)

{chr(10).join(lines)}

Frame sequences: the flip frames force --flip on #plateCard with the shim frozen; the
#process frames are real scroll positions with a 700 ms settle, so a step's drawing may be
mid-way. The empty Calyx (beige) and Horai (black) plates in the slices are K1, not a capture
artefact this time.

## Invariants of this project. Do not violate them in your findings.

- Motion always plays (F-011). prefers-reduced-motion is DELIBERATELY not honoured on this
  project; a considered accessibility trade-off the owner confirmed after it was put to him,
  not an oversight. Suggesting a reduced-motion fallback, a static alternative, or an
  @media (prefers-reduced-motion) block is OUT OF SCOPE and will be discarded. Do not mention it.
- The scroll engine is never edited. scroll/scrollcraft.js and scroll/scrollcraft.css are
  vendored. Findings about them are reported, never fixed; the page-level shim
  scroll/sc-smooth.js is the sanctioned way around them (it may be edited: it is the page's).
- --sc-p is the RAW scroll position; --sc-ps is the SMOOTHED one. Anything that physically
  moves must read --sc-ps. A finding that says "use --sc-p for consistency" is backwards and
  will be discarded. Cue opacity may read --sc-p.
- No em dashes or en dashes (U+2010 to U+2015) in VISIBLE text (gate 75). Zero tolerance.
- Fifteen locked copy strings (PRODUCT.md) and the seven process paragraphs are NOT yours:
  a separate copy agent runs the copy gate after this loop. Do not propose wording, and do
  not propose a soft hyphen inside a locked string.
- sites/*.html (the three example sites inside the iframes) are untouchable references.
- New elements or colours are allowed (the owner said so), but each must be a concrete
  addition with a token name (never an inline hex) and the HELHET.md H-row it serves.
  Never "make it more premium".
- Review only, no patches.

## What is yours

CODE: logic, lifecycle, resource loading, arithmetic, state, DOM contracts. Listeners
never removed; observers and rAF loops that keep running; scroll maths that is
non-monotonic, clamps wrongly, or divides by zero; will-change left on; dead or
duplicated CSS/JS; a var() that references a custom property not defined on that
element; hard-coded values that contradict a token; SVG presentation attributes CSS
cannot set; anything that breaks between 900 and 1440 px; anything that would throw.
Especially this round: the cost of style recalculation per scroll frame (K4): which
selectors and which subtrees make a single custom-property write on an act expensive,
and what in this file (not the engine) can be cut.

PIXELS, WHOLE PAGE: with HELHET.md section 3 as the floor, read the 1440 slices and the
390 slices as one continuous page each. Then the previews and the frame sequences.

## The questions, answer every one with image numbers and regions

1. Do the parts cohere as one page after R7? Where does it still read as pages glued together?
2. Where does the rhythm break (a seam, a slit of raw ground, two equal blocks side by side,
   an empty screen the brief did not author)? Name image number and region.
3. Where is the balance wrong per screen (squint test: one dominant element per 1440 screen,
   no column carrying less weight than its width)? Per image.
4. Where does the motion stall, jump, or arrive late (the flip sequence, the process
   sequence, the previews vs the frames: does each ?preview=process-0N show ONLY step N's
   drawing)? Also: the footer rule (.close-rule) and the giant headline scale: do they read
   as motion in the frames, or are they invisible?
5. What is missing to reach the floor? Which H-rows (H-01 to H-35) are met, which are not,
   as far as the images and the code let you judge. One line per H-row you can judge.
6. New elements or colours you would add, each with a token name and its H-row.

## Output contract (exact; a script rejects anything else)

Line 1: exactly one word, the disposition: recapture | rebuild | fix | ship
Then exactly these five level-2 markdown headings, in this order, nothing else at level 2:

## persistence
(what survived from R7; how many findings you have and how confident)
## fidelity
(does the code do what BRIEF.md says; the H-row table from question 5; answers to 1 to 4)
## ceiling
(what the references named in HELHET.md section 1 still do better, one line each, or n/a)
## material_fixes
(AT MOST 8 items, a markdown list, most material first, each with file:line in
tests/alunix-r8/runs/V3c/index.html and a target value or expected behaviour, and for
pixel findings the image number and region; K1 to K4 count against the 8 only if you add
something to them)
## keep
(what is right and must survive the next round)

Plain text, no patches, no code blocks longer than three lines. Swedish or English, your
choice, but H-row ids and file:line exactly.

## HELHET.md, in full

{helhet}
"""
OUT.write_text(prompt, encoding="utf-8")
IMGS.write_text("\n".join(paths), encoding="utf-8")
print(f"prompt {len(prompt)} chars, {n} images -> {OUT.name}, {IMGS.name}")
