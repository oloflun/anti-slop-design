"""Builds the Astra (codex) prompt for loop 4 and the ordered -i image list.
Usage: python build_astra_prompt4.py <probe-summary.txt>  (the loop-4 probe table, pasted in)"""
import sys
from pathlib import Path

ROOT = Path("C:/Users/Anton L/anti-slop-design")
CELL = ROOT / "tests/alunix-r8/runs/V3c"
SHOTS = CELL / "shots/loop-4"
OUT = Path(__file__).with_name("astra4-prompt.txt")
IMGS = Path(__file__).with_name("astra4-images.txt")
probe = Path(sys.argv[1]).read_text(encoding="utf-8") if len(sys.argv) > 1 else "(probe table not available)"

groups = [
    ("slices-1440", sorted((SHOTS / "slices-1440").glob("*.png")),
     "full-page slice {i} at 1440x900, scrollY = {i}*900, reached by plain scrollTo (no injected sampler: plan 035 is built), 3 s settle"),
    ("slices-390", sorted((SHOTS / "slices-390").glob("*.png")),
     "full-page slice {i} at 390x844, scrollY = {i}*844, plain scrollTo, 3 s settle"),
    ("preview-1440", [SHOTS / "preview" / f"preview-1440-{m}.png" for m in
      ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]],
     "?preview={m} at 1440x900 (formed state, shim frozen, load + 2 s)"),
    ("preview-390", [SHOTS / "preview" / f"preview-390-{m}.png" for m in
      ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]],
     "?preview={m} at 390x844"),
    ("flip-1440", sorted((SHOTS / "flip-1440").glob("*.png")),
     "hero card, --flip forced to {f} at 1440x900 (12 steps 0 to 1)"),
    ("flip-390", sorted((SHOTS / "flip-390").glob("*.png")),
     "hero card, --flip forced to {f} at 390x844"),
    ("process-1440", sorted((SHOTS / "process-1440").glob("*.png")),
     "#process act, frame {i} of 12 through its visible life at 1440x900 (from top-vh to bottom, 700 ms settle)"),
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
WHOLE-PAGE loop (Fas C, round 4 of max 6). REVIEW ONLY: return findings, never a patch, never
a rewritten file. You are read-only.

This round decides whether the loop is finished. The exit condition is: you answer `ship`
with ZERO material_fixes, the architect ticks every H-row in HELHET.md section 3 except the
Q30 rows, and the smoothness gate is green both directions. So be exact: a finding you can
verify in the file or in an image with a line number or an image number and region is a
material fix; a taste remark is not, and an unverifiable one is not. If you find nothing
material, say `ship` and put what you checked in `fidelity` and `keep`. If you find
something material, say `fix` and it must be reproducible.

## Target
File to review (read it in full yourself, one HTML file with inline CSS and JS, R9 state,
md5 909916d1):
  tests/alunix-r8/runs/V3c/index.html
The page's own shim (may be edited by the builder; the engine may not):
  tests/alunix-r8/runs/V3c/scroll/sc-smooth.js
Brief and decision ledger (device table, authored silence, the builder's R9 rows and the
"Fynd, dokumenterade men inte lösta i R9" table at the end of the ledger):
  tests/alunix-r8/runs/V3c/BRIEF.md
The whole-page reference floor you review against (ALSO pasted in full below; the
architect's loop-3 ticks refer to the R8 state and are being re-ticked now against R9):
  tests/alunix-r8/runs/V3c/HELHET.md
Your own loop-3 report and how each of your six findings was judged (all six taken, all
six built in R9):
  tests/alunix-r8/runs/V3c/reviews/loop-3-astra.md
What R9 built (seven plans 035, 036, 037, 039, 040, 038, 041), its per-plan numbers and its
gate; and the lead's pixel read that approved R9:
  tests/alunix-r8/runs/V3c/NOTES.md, section "## R9" and "## R9, leadens pixelläsning"
The plans themselves, if you need the intended mechanism:
  tests/alunix-r8/runs/V3c/plans/035-*.md to 041-*.md
The vendored scroll engine, reference only, never edited:
  tests/alunix-r8/runs/V3c/scroll/scrollcraft.js, scrollcraft.css
Repo root is the working directory. All paths are relative to it.

## Already known for round 4 (verified by the lead and the architect; say if your read differs)
K8. The reveal latch is no longer path dependent (plan 035): wheel, PageDown, scrollTo and
    smooth scrollTo all land --rv 1 on both wrappers; a resize before the band survives
    (the act object is resolved per tick). The slices attached this round are plain
    scrollTo captures and the frames are whole in them; there is no "-fix" group any more.
K9. The reveal no longer clips a live iframe (plan 036): the iris is border-radius:50% +
    scale(--rv) on an inner .rv box (a measured square, --rv-s) with the iframe
    counter-scaled; the Calyx pull-up is translateY on .rv with the iframe
    counter-translated. Price window at cpu 1 went 143.7 -> 35.6 ms p95 (median of 3).
    The giant window (2700 + 28 ticks) went 128 -> 106.6 ms median: the builder's stated
    <= 60 ms target was NOT reached there and the builder names #giant-section's own
    0.92 -> 1 scale (outside R9) as a suspect, unmeasured.
K10. The builder measured a regression in the hero, DOWN direction, cpu 1: p95 36 ms (R8)
    -> 70.6 ms with acts.filter() per tick -> 58.6 ms after replacing it with a for-loop
    (findAct). Hero UP is 18.5 ms. The builder attributes the remainder to latchTick now
    running every frame while ANY act is still lerping (035's architecture). The architect
    re-measures this round; the numbers are in the probe table below. If you can see in
    latchTick (index.html ~1620-1700) what per-frame work is avoidable, name it with the
    line and the mechanism; that is the most valuable code finding this round.
K11. Ground drift now at 24 % (plan 038) and written on .ground by the page (plan 041,
    kept with a measured 15 to 18 ms gain in the thesis and giant windows): wood pixel
    (720,180) at the thesis centred reads (119,130,140), chroma 21; fold chroma 0.
K12. ?preview=process-0N re-aims after load and fonts.ready (plan 037): 7/7 formed at 1440,
    6/7 at 390 (step 02 at 390 lands --sc-ps 0.2753 against --e2 0.3311, rooted in the
    engine's own isMobile() resize guard, scrollcraft.js line 1186; the engine is never
    edited, so this is reported as a known engine-bound limit, not a page bug).
Q30 (restacking the two-column band into five full-width acts) and Q31 (88 vs 96 px) are
still open questions to the owner and not yours: judge the band as two columns with 017's
air and offset and the giant headline at 88 px. H-02, H-03 and H-08 (screen s03) hang on
Q30 and count as "waiting for the owner", not as open findings.

## Loop-4 probe table (motion_probe.py, control protocol; architect's own runs this round)
{probe}

## Attached images, in order (you cannot see file names, so here they are)
{chr(10).join(lines)}

Frame sequences: the flip frames force --flip on #plateCard with the shim frozen; the
#process frames are real scroll positions with a 700 ms settle, so a step's drawing may be
mid-way. The slices are plain scrollTo with a 3 s settle at every position.

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
  Calyx's own nav overlapping its wordmark at 390 inside the frame is the reference site's,
  already reported, not a finding here.
- The iframes are never transformed or faded after they are shown; reveal happens once, on
  the wrapper (PRODUCT.md). During the reveal the content is pixel-still (transform x
  counter-transform = identity); after it both transforms are identity. A wrapper keeps its
  content-visibility sleep (plan 027).
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
Especially this round: (a) latchTick's per-frame cost and its stop condition (K10): does it
stop when nothing it owns can change, and what does it touch per frame that costs layout or
style? (b) the .rv geometry (measureFrames, --rv-s/--rv-w/--rv-h): any viewport where the
square does not cover the wrapper at --rv 1, or where the counter-scale distorts? (c)
aimPreview's three triggers + scroll listener + generation id: any leak, any loop that never
settles, anything that runs outside preview mode? (d) driftColor/applyDrift: the three stops
read from :root once; the t<1 / else switch against the engine's own loop order; any frame
where --sc-canvas jumps? (e) anything the seven R9 plans broke that the R9 gate did not
measure (the builder lists known gaps at the end of NOTES section R9: no cpu-4 matrix,
no full twelve-frame sweep of all six acts, 390 previews 04-07 not re-checked).
PIXELS, WHOLE PAGE: with HELHET.md section 3 as the floor, read the 1440 slices and the
390 slices as one continuous page each. Then the previews and the frame sequences.

## The questions, answer every one with image numbers and regions
1. Do the parts cohere as one page after R9? Where does it still read as pages glued together?
2. Where does the rhythm break (a seam, a slit of raw ground, two equal blocks side by side,
   an empty screen the brief did not author)? Name image number and region.
3. Where is the balance wrong per screen (squint test: one dominant element per 1440 screen,
   no column carrying less weight than its width)? Per image. The band (slices 4 and 5 at
   1440): with both frames live and whole, is it one authority per screen?
4. Where does the motion stall, jump, or arrive late (the flip sequence, the process
   sequence, the previews vs the frames: does each ?preview=process-0N show steps 01 to N
   and not N+1)? The process entry (slice 6 at 1440, process frame 1): is the outline whole
   while step 01 is read (plan 040)? The price ledger's rules and the footer rule: motion in
   the frames?
5. What is missing to reach the floor? Which H-rows (H-01 to H-35) are met, which are not,
   as far as the images, the probe table and the code let you judge. One line per H-row.
   For H-21/H-22/H-32 (frame time): given the probe table, is what remains the engine's
   floor outside this file (the shim's per-act write, the engine's read loop, the two live
   iframes' own paint), or is there a cut left in this file? Name it or say "architectural
   floor, accounted for".
6. New elements or colours you would add, each with a token name and its H-row; or "none".

## Output contract (exact; a script rejects anything else)
Line 1: exactly one word, the disposition: recapture | rebuild | fix | ship
Then exactly these five level-2 markdown headings, in this order, nothing else at level 2:
## persistence
(what survived from R9; how many findings you have and how confident)
## fidelity
(does the code do what BRIEF.md says; the H-row table from question 5; answers to 1 to 4)
## ceiling
(what the references named in HELHET.md section 1 still do better, one line each, or n/a)
## material_fixes
(AT MOST 8 items, a markdown list, most material first, each with file:line in
tests/alunix-r8/runs/V3c/index.html or scroll/sc-smooth.js and a target value or expected
behaviour, and for pixel findings the image number and region. If nothing is material,
write the single line "none" with no list items.)
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
