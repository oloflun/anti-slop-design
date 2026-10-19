"""Builds the Astra (codex) prompt for loop-3 and the ordered -i image list."""
from pathlib import Path

ROOT = Path("C:/Users/Anton L/anti-slop-design")
CELL = ROOT / "tests/alunix-r8/runs/V3c"
SHOTS = CELL / "shots/loop-3"
OUT = Path(__file__).with_name("astra3-prompt.txt")
IMGS = Path(__file__).with_name("astra3-images.txt")

groups = [
    ("slices-1440", sorted((SHOTS / "slices-1440").glob("*.png")),
     "full-page slice {i} at 1440x900, scrollY = {i}*900, reached by scrollTo (programmatic scroll)"),
    ("slices-390", sorted((SHOTS / "slices-390").glob("*.png")),
     "full-page slice {i} at 390x844, scrollY = {i}*844, reached by scrollTo"),
    ("slices-1440-fix", sorted((SHOTS / "slices-1440-fix").glob("*.png")),
     "SAME slice {i} at 1440x900 with the proposed latch fix (K5) injected, so the frames reveal as a wheel reader sees them"),
    ("slices-390-fix", sorted((SHOTS / "slices-390-fix").glob("*.png")),
     "SAME slice {i} at 390x844 with the proposed latch fix (K5) injected"),
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
        elif name.endswith("-fix"):
            d = desc.format(i=int(stem[-2:]))
        else:
            d = desc.format(i=j)
        lines.append(f"{n:3d}. {f.name}  -  {d}")
        paths.append(str(f))

helhet = (CELL / "HELHET.md").read_text(encoding="utf-8")

prompt = f"""You are the fifth reviewer (Astra) on a hand-built Swedish agency marketing page, in the
WHOLE-PAGE loop (Fas C, round 3 of max 6). REVIEW ONLY: return findings, never a patch, never
a rewritten file. You are read-only.

## Target

File to review (read it in full yourself, one HTML file with inline CSS and JS, R8 state,
md5 70214a22):
  tests/alunix-r8/runs/V3c/index.html
The page's own shim (may be edited by the builder; the engine may not):
  tests/alunix-r8/runs/V3c/scroll/sc-smooth.js
Brief and decision ledger (device table, authored silence, the builder's R8 rows):
  tests/alunix-r8/runs/V3c/BRIEF.md
The whole-page reference floor you review against (ALSO pasted in full below; the
architect's loop-2 ticks refer to the R7 state and are being re-ticked now against R8):
  tests/alunix-r8/runs/V3c/HELHET.md
Your own loop-2 report and how each finding was judged (all three were taken and built in R8):
  tests/alunix-r8/runs/V3c/reviews/loop-2-astra.md
What R8 built (eight plans 027, 028, 034, 031, 033, 029, 030, 032) and its gate numbers:
  tests/alunix-r8/runs/V3c/NOTES.md, section "## R8 (2026-09-17)" and "## R8, leadens pixelläsning"
The vendored scroll engine, reference only, never edited:
  tests/alunix-r8/runs/V3c/scroll/scrollcraft.js, scrollcraft.css
Repo root is the working directory. All paths are relative to it.

## Already known for round 3 (verified by the lead and the architect with measurements;
## do not spend your budget re-finding them, but say if your read differs)

K5. Plan 031's reveal latch is PATH DEPENDENT. readState (index.html ~1655-1685) samples the
    shim's lerped act value (acts[i].cur) only when a scroll event fires; the shim keeps
    lerping for ~30 frames after the last event but nobody samples it again. Measured at the
    same scrollY (Horai act --sc-ps 0.58): wheel 100 px/60 ms gives --rv 0.98; PageDown 0.21;
    window.scrollTo 0.00; smooth scrollTo 0.00. So slices 4 and 5 at 1440 (images 5, 6) and
    slices 4 to 6 at 390 show the Calyx and Horai wrappers fully clipped (raw ground where the
    frames should be): scrollTo capture = a keyboard or scrollbar reader. The fix (a rAF loop
    that keeps sampling while any reveal < 1 and its act is still moving toward --sc-p) was
    emulated in-page: all four scroll methods reach --rv 1. Images in the "-fix" groups are
    the same slices captured with that emulation, and are the ones to judge the band's
    balance from.
K6. Ground drift at 44 % (plan 029) still reads as a blue wash. Measured on the wood panel
    (mid-tone, 1440, thesis centred, pixel (720,180)): grayscale (128,128,128); at 44 %
    (112,132,150) chroma 38; 30 % chroma 26; 24 % chroma 21; 18 % chroma 16. H-19's floor
    was written on a near-black margin pixel (delta 12 RGB steps), and `mix-blend-mode:
    color` moves chroma in proportion to luminance, so that floor FORCES a wash on the
    mid-tones. The architect is rewriting H-19 on the mid-tone pixel and lowering the tone.
    Do not propose a different blend mode (multiply and soft-light were measured and
    rejected in loop 2).
K7. Frame time, loop 3 (control fixture 18.4 ms p95, 0 to 2 frames over 33 ms in every
    control run, machine never fully quiet): cpu 1, 100 px/60 ms: hero down p95 36.1 ms
    (19 frames > 33), up 18.4; #process down 32.1, up 18.5; #giant-section (band, 2700 to
    5500) 128 ms (22 frames); .price act (3873 to 5673, where both iframes mount) 143.7 ms
    (16 frames). cpu 4: hero down 89, up 54; process down 285, up 461. staircase 0 on every
    track in every run; max_step on --sc-ps 0.23 to 2.82 %. The band's cost is where the two
    live iframes (sites/calyx.html, sites/horai.html) are mounted and laid out inside the
    reader's scroll path, plus the engine's --sc-canvas write on :root (9 ms per changed
    value at cpu 1, measured loop 2; 0.24 ms if written on .ground instead). If you see a
    cheaper cut in THIS file (not the engine), name it with file:line and the mechanism.

Q30 (restacking the two-column band into five full-width acts) and Q31 (88 vs 96 px) are
open questions to the owner. Do not propose the restack again; judge the band as two
columns with 017's air and offset, and the giant headline at 88 px.

## Attached images, in order (you cannot see file names, so here they are)

{chr(10).join(lines)}

Frame sequences: the flip frames force --flip on #plateCard with the shim frozen; the
#process frames are real scroll positions with a 700 ms settle, so a step's drawing may be
mid-way. The empty Calyx and Horai regions in the plain slices are K5 (clipped wrappers), not
sleeping frames this time; the "-fix" slices show them revealed.

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
  will be discarded. Cue opacity may read --sc-p. The --sc-ps contract (LERP 0.16, DEAD
  0.0005, inherits:true on --sc-ps, staircase 0) is keep.
- No em dashes or en dashes (U+2010 to U+2015) in VISIBLE text (gate 75). Zero tolerance.
- Fifteen locked copy strings (PRODUCT.md) and the seven process paragraphs are NOT yours:
  a separate copy agent runs the copy gate after this loop. Do not propose wording, and do
  not propose a soft hyphen inside a locked string.
- sites/*.html (the three example sites inside the iframes) are untouchable references.
- The iframes are never transformed or faded after they are shown; reveal happens once, on
  the wrapper (PRODUCT.md). A wrapper keeps its content-visibility sleep (plan 027).
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
Especially this round: (a) is the K5 fix (a self-scheduling rAF sampler in readState, or a
subscription hook in sc-smooth.js) the right shape, and what else in this file samples a
lerped value only on scroll events (the same class of bug elsewhere: setFace, processPs,
the data-on groups)? (b) where do the band's frames go (K7): the iframe mount timing
(rootMargin 100 %, index.html ~1735-1790), the clip-path reveal repainting a live iframe
every frame, the --sc-canvas write on :root; which of these can this file move or cut?

PIXELS, WHOLE PAGE: with HELHET.md section 3 as the floor, read the 1440 slices and the
390 slices as one continuous page each (use the "-fix" slices for the band). Then the
previews and the frame sequences.

## The questions, answer every one with image numbers and regions

1. Do the parts cohere as one page after R8? Where does it still read as pages glued together?
2. Where does the rhythm break (a seam, a slit of raw ground, two equal blocks side by side,
   an empty screen the brief did not author)? Name image number and region.
3. Where is the balance wrong per screen (squint test: one dominant element per 1440 screen,
   no column carrying less weight than its width)? Per image. The band (fix slices 4 and 5
   at 1440): with both frames live, is it one authority per screen?
4. Where does the motion stall, jump, or arrive late (the flip sequence, the process
   sequence, the previews vs the frames: does each ?preview=process-0N show steps 01 to N
   and not N+1)? The price ledger's four rules (plan 033) and the footer rule: do they read
   as motion in the frames? The giant headline scale 0.92 to 1: visible or not?
5. What is missing to reach the floor? Which H-rows (H-01 to H-35) are met, which are not,
   as far as the images and the code let you judge. One line per H-row you can judge.
6. New elements or colours you would add, each with a token name and its H-row.

## Output contract (exact; a script rejects anything else)

Line 1: exactly one word, the disposition: recapture | rebuild | fix | ship
Then exactly these five level-2 markdown headings, in this order, nothing else at level 2:

## persistence
(what survived from R8; how many findings you have and how confident)
## fidelity
(does the code do what BRIEF.md says; the H-row table from question 5; answers to 1 to 4)
## ceiling
(what the references named in HELHET.md section 1 still do better, one line each, or n/a)
## material_fixes
(AT MOST 8 items, a markdown list, most material first, each with file:line in
tests/alunix-r8/runs/V3c/index.html or scroll/sc-smooth.js and a target value or expected
behaviour, and for pixel findings the image number and region; K5 to K7 count against the
8 only if you add something to them)
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
