"""patch_astra5.py: turn build_astra_prompt5.py (a copy of loop 4's builder) into loop 5's:
new context files, new "already known" block (each item re-measured by the architect this
round), new round-specific code questions."""
from pathlib import Path

p = Path(__file__).with_name("build_astra_prompt5.py")
s = p.read_text(encoding="utf-8")

s = s.replace("WHOLE-PAGE loop (Fas C, round 4 of max 6)",
              "WHOLE-PAGE loop (Fas C, round 5 of max 6; round 6 is the last)")
s = s.replace("R9 state,\nmd5 909916d1):", "R10 state,\nmd5 d3491b4a):")

old_ctx = s[s.index("Your own loop-3 report"):s.index("The vendored scroll engine")]
new_ctx = """Your own loop-4 report and how each of your three findings was judged (all three taken,
all three built in R10, all three verified by the architect this round):
  tests/alunix-r8/runs/V3c/reviews/loop-4-astra.md
What R10 built (three plans 042, 043, 044), its per-plan numbers, its gate, and the gaps it
names honestly at the end:
  tests/alunix-r8/runs/V3c/NOTES.md, section "## R10"
The plans themselves, if you need the intended mechanism:
  tests/alunix-r8/runs/V3c/plans/042-*.md, 043-*.md, 044-*.md
"""
s = s.replace(old_ctx, new_ctx)

old_known = s[s.index("## Already known for round 4"):s.index("## Loop-4 probe table")]
new_known = """## Already known for round 5. Every item below was re-measured by the architect THIS round,
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

"""
s = s.replace(old_known, new_known)
s = s.replace("## Loop-4 probe table", "## Loop-5 probe table")

# round-specific code questions replace R9's
old_q = s[s.index("Especially this round: (a) latchTick"):s.index("PIXELS, WHOLE PAGE:")]
new_q = """Especially this round, and only these, because R10 touched exactly three places:
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
"""
s = s.replace(old_q, new_q)
p.write_text(s, encoding="utf-8")
print("patched, len", len(s))
