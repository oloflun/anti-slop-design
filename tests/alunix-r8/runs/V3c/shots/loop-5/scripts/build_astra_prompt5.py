"""Builds the Astra (codex) prompt for loop 5 and the ordered -i image list.
Usage: python build_astra_prompt4.py <probe-summary.txt>  (the loop-5 probe table, pasted in)"""
import sys
from pathlib import Path

ROOT = Path("C:/Users/Anton L/anti-slop-design")
CELL = ROOT / "tests/alunix-r8/runs/V3c"
SHOTS = CELL / "shots/loop-5"
OUT = Path(__file__).with_name("astra5-prompt.txt")
IMGS = Path(__file__).with_name("astra5-images.txt")
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
WHOLE-PAGE loop (Fas C, round 5 of max 6; round 6 is the last). REVIEW ONLY: return findings, never a patch, never
a rewritten file. You are read-only.

This round decides whether the loop is finished. The exit condition is: you answer `ship`
with ZERO material_fixes, the architect ticks every H-row in HELHET.md section 3 except the
Q30 rows, and the smoothness gate is green both directions. So be exact: a finding you can
verify in the file or in an image with a line number or an image number and region is a
material fix; a taste remark is not, and an unverifiable one is not. If you find nothing
material, say `ship` and put what you checked in `fidelity` and `keep`. If you find
something material, say `fix` and it must be reproducible.

## Target
File to review (read it in full yourself, one HTML file with inline CSS and JS, R10 state,
md5 d3491b4a):
  tests/alunix-r8/runs/V3c/index.html
The page's own shim (may be edited by the builder; the engine may not):
  tests/alunix-r8/runs/V3c/scroll/sc-smooth.js
Brief and decision ledger (device table, authored silence, the builder's R9 rows and the
"Fynd, dokumenterade men inte lösta i R9" table at the end of the ledger):
  tests/alunix-r8/runs/V3c/BRIEF.md
The whole-page reference floor you review against (ALSO pasted in full below; the
architect's loop-3 ticks refer to the R8 state and are being re-ticked now against R9):
  tests/alunix-r8/runs/V3c/HELHET.md
Your own loop-4 report and how each of your three findings was judged (all three taken,
all three built in R10, all three verified by the architect this round):
  tests/alunix-r8/runs/V3c/reviews/loop-4-astra.md
What R10 built (three plans 042, 043, 044), its per-plan numbers, its gate, and the gaps it
names honestly at the end:
  tests/alunix-r8/runs/V3c/NOTES.md, section "## R10"
The plans themselves, if you need the intended mechanism:
  tests/alunix-r8/runs/V3c/plans/042-*.md, 043-*.md, 044-*.md
The vendored scroll engine, reference only, never edited:
  tests/alunix-r8/runs/V3c/scroll/scrollcraft.js, scrollcraft.css
Repo root is the working directory. All paths are relative to it.

## Already known for round 5. Every item below was re-measured by the architect THIS round,
## not taken on the builder's word. Say if your read differs, with an image number or a line.
K13. The document height is now constant (plan 042). The two declarations that reserved
    760 px for .price (content-visibility:auto, contain-intrinsic-size:auto 760px) are gone.
    Measured: scrollHeight 10 582 px at load and in the band at 1440 (11 326 at 390), and
    the engine's cached act top for #process equals the DOM top (5 340 = 5 340 at 1440,
    6 152 = 6 152 at 390) in every one of 21 preview loads, with no resize needed. The
    consequence you named in loop 4 (your image 77: the drawing 297 px behind the prose at
    the process entry) is gone: see the process-1440 frame 2 attached here, where the
    contour is whole and the glyph drawn beside step 01's paragraph.
K14. ?preview=process-0N at 390 is no longer a race (plan 042). 21 loads (steps 01 to 07,
    three loads each), read at 1, 2, 4 and 8 s: 20 of 21 landed --sc-ps within 0.0001 of
    --eN; one landed 0.2400 against --e1 0.2450 (k1 = 0.971) and stayed there for 8 s. A
    follow-up of 8 further loads of step 01 gave 8/8 exact with stroke-dashoffset 0 on both
    drawn paths. At 1440: 7/7.
K15. The Calyx reveal now has an opening (plan 043). It was a no-op in R9, your loop-4
    fix 2. Measured with --rv forced: wrapper background visible 100.0 / 74.9 / 50.0 /
    0.1 per cent at --rv 0 / 0.25 / 0.5 / 1, .rv has overflow:clip, the iframe's own box
    stays at top 40 in all four states (pixel-still), identity at 1. Hoerai's iris in the
    same run: 99.9 / 44.9 / 12.0 per cent dark.
K16. The drift handoff is continuous (plan 044). Your loop-4 fix 3 measured --sc-canvas
    rgb(18,63,104) at scrollY 3 600 and rgb(244,242,238) at 3 620. Now: 3 600
    rgb(18,63,104), 3 620 rgb(19,64,104), 3 700 rgb(35,76,114), 3 800 rgb(76,109,138),
    4 000 rgb(185,195,203); the wood mid-tone at (720,40) goes chroma 21, 20, 19, 15, 5
    over the same span. No step over 40 per channel per 20 px.
K17. Contrast is measured across the whole page this round, not only the fold
    (contrast_over_media.py --url, text hidden, brightest 5 per cent of the ground):
    1440 at scrollY 0, 3 300, 4 800, 5 400, 8 000, 9 700 = 61 strings, all pass, worst
    6.70:1 (the thesis strings on the blue plate, floor 4.5). 390 at 0, 2 900, 5 600,
    7 000, 10 400 = 41 strings, all pass except one known tool artefact: the card back's
    'SYSTEM' reads 2.28:1 at ?preview=front because the tool samples the BACK's DOM
    rectangle while the FRONT's light pool is what is painted there; at ?preview=back the
    same string measures 17.51:1, and the 390 slice 0 attached here shows no text over the
    photo at all.
K18. The reveal latch is still path independent after 043 (plan 035 kept): wheel, PageDown,
    scrollTo, smooth scrollTo and a resize-before-the-band all land --rv 1 on BOTH
    wrappers, with zero --rv writes three seconds after landing.
K19. Frame time. The architect re-measured the two windows whose single-run p95 moved
    against loop 4, three interleaved runs each with a clean control between them, plus an
    interleaved A/B of the .panel-thesis window with the two removed declarations
    re-injected (the R9 condition) against the page as built. Result: hero cpu 4 down
    median 280.1 ms (loop 4's declared floor: 333.8) and .panel-thesis cpu 1 median
    142.4 ms as built against 108.4 ms with R9's declarations back, the two spreads
    overlapping. Every other window is equal to or better than loop 4. So the image-time
    floor is held or beaten. What remains above the bar (p95 <= 20 ms, 0 frames over
    33 ms) is the declared architectural floor: the two live iframes' own paint and the
    engine's per-frame read, outside this file. Do not re-open it as a material fix unless
    you can name a cut IN THIS FILE with a line number and a mechanism.
K20. staircase is 0 on every contract track in every run, both directions, both cadences,
    both CPU settings. Two extra tracks reported staircase 1 on a first pass
    (.calyx-wrap:--rv and .horai-wrap:--rv); probed from BEFORE the reveal triggers instead
    of after, both gave staircase 0, twice over, so that flag was the probe's own settle
    plateau and not the page. .horai-wrap .rv:transform reads DEAD and that is correct and
    by design: Hoerai's device (BRIEF device table, row 6) is an iris, not a transform on
    .rv, so nothing moves there; that device's live track is .horai-wrap:--rv.
Q30 (restacking the two-column band into five full-width acts) and Q31 (88 vs 96 px) are
still open questions to the owner and not yours: judge the band as two columns with 017's
air and offset and the giant headline at 88 px. H-02, H-03 and H-08 (screen s03) hang on
Q30 and count as "waiting for the owner", not as open findings.

## Loop-5 probe table (motion_probe.py, control protocol; architect's own runs this round)
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
Especially this round, and only these, because R10 touched exactly three places:
(a) plan 042 removed content-visibility:auto and contain-intrinsic-size from .price. Is
    there anywhere else in the file that still assumes the old reserved height, or another
    element whose reserved size can desynchronise the engine's cached act tops the same
    way? Name the selector and the line.
(b) plan 043 rewrote the Calyx reveal: .calyx-wrap .rv got overflow:clip and the two
    transforms were inverted so the opening comes from the top. Check the arithmetic at
    every --rv and at both widths: is the product of the two transforms exactly identity
    at --rv 1, does the clip box cover the wrapper at every --rv, and is anything clipped
    that should not be? Does 036's Hoerai iris still hold with 043's change next to it?
(c) plan 044 added driftHand (the giant act's raw progress at the moment the thesis act's
    t reaches 1) and made leg 2 read driftSmooth((g - driftHand) / 0.35). Is driftHand
    measured at a moment that can be missed, re-measured on resize, or stale after a
    layout change? Is the colour monotone in BOTH scroll directions, and what happens if
    the reader starts mid-band (a deep link or a restored scroll position)?
(d) anything the three R10 plans broke that R10's own gate did not measure. R10 names its
    gaps at the end of NOTES section R10: no full cpu-4 motion matrix for all seven
    tracks, no repeated PageDown/PageUp walk, and the 1440 preview check not run in both
    directions. The architect has since run the cpu-4 matrix, the latch walk and the 390
    preview matrix; the 1440 preview check in both directions is still unrun.
(e) anything that would throw, leak a listener, keep a rAF loop alive, or break between
    900 and 1440 px.
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
