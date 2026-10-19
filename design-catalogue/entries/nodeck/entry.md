---
title: "Nodeck"
url: https://www.nodeck.online/
source_url: https://www.nodeck.online/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "institutional"
family: highlighter-slide-deck-site
dna: "Startup consultancy x presentation deck with a highlighter"
register: other
grammar: chaptered editorial
lane: "A consultancy site built as a slide deck that hates decks: chunky outlined NODECK on pink, a giant highlighter pen that sweeps neon yellow across the screen to change slides, and statements whose key words get highlighted."
mode: persuade
traits: ["presentation deck UI (prev/next, slide numbers, presenter notes)", "giant highlighter pen as the transition", "chunky outlined display type on pink", "neon-yellow highlight sweeps", "cream and pink slides alternating", "footnoted statements"]
palette: ["#FE87AB", "#E8D68F", "#FFFFFF", "#191113", "#BB6F82"]
type: ["DM Sans", "BN Dime Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The concept is the interface: the site is a deck, with prev/next and a slide counter, but every transition is a highlighter stroke wiping across the screen, and every statement gets its key words highlighted in the same yellow. The joke and the brand are the same move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Bogdan Kolomiyets).

## What to borrow (principle)

- Make the transition tool an object from the brand's world (a highlighter) that physically wipes the slide
- Highlight key words in a statement with the same gesture as the transition
- Deck-style navigation (prev/next, counter) for a page that is truly sequential

## What to leave

- Slide-by-slide navigation hides how long the deck is
- Chunky outlined display type is hard to read in long statements

## Signature move

A giant highlighter that sweeps neon yellow across the screen to change slides.

## Motion

Intro: letters of NODECK pop in one by one (Flip/SplitText), the sticky note and highlighter slide in (~1.2 s). Navigation (Observer, Draggable/Inertia, DrawSVG): next slide triggers the highlighter to sweep a yellow band across the frame and reveal the next slide; statements set in and then yellow highlights draw behind key words; 'WE BELIEVE' slide with words wobbling in; footnotes draw.

Measured (`motion/probe.json`): GSAP 3.14.2; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Go to cover slide. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a consultancy site built as a slide deck that hates decks: chunky outlined NODECK on pink, a giant highlighter pen that sweeps neon yellow across the screen to change slides, and statements whose key words get highlighted. Type: DM Sans, BN Dime Display.
Ground and ink from the measured palette (#FE87AB, #E8D68F, #FFFFFF). Motion carries the page through
a giant highlighter that sweeps neon yellow across the screen to change slides. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D props (highlighter, sticky note, eraser) on flat pastel grounds

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D props (highlighter, sticky note, eraser) on flat pastel grounds

## Reference lock

Primary reference/direction: Nodeck — A consultancy site built as a slide deck that hates decks: chunky outlined NODECK on pink, a giant highlighter pen that sweeps neon yellow across the screen to change slides, and statements whose key words get highlighted.
Preserve (3-5 traits): presentation deck UI (prev/next, slide numbers, presenter notes); giant highlighter pen as the transition; chunky outlined display type on pink; neon-yellow highlight sweeps; cream and pink slides alternating.
Borrow only (1-2): Make the transition tool an object from the brand's world (a highlighter) that physically wipes the slide; Highlight key words in a statement with the same gesture as the transition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D props (highlighter, sticky note, eraser) on flat pastel grounds
Reject: Slide-by-slide navigation hides how long the deck is; Chunky outlined display type is hard to read in long statements
Token commitments: palette #FE87AB, #E8D68F, #FFFFFF, #191113, #BB6F82; type DM Sans, BN Dime Display; engine GSAP + Lenis linked (never vendored).
