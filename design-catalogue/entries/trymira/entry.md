---
title: "MIRA"
url: https://trymira.com/
source_url: https://trymira.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: black-to-white-hardware-launch
dna: "AI smart glasses x hardware keynote page"
register: cinematic dark
grammar: chaptered editorial
lane: "A hardware launch page that starts on a black macro of the glasses turning under light, types its promise into tabbed capabilities, plays an AR demo film, then switches to white for exploded product callouts, the ring and the app."
mode: persuade
traits: ["black macro product hero rotating under light", "typed headline 'The Glasses That…'", "tabbed capability chips (Capture, Act, Translate)", "AR overlay demo video", "white product section with orange callouts", "phone mockup cycling app screens"]
palette: ["#32373B", "#FFFFFF", "#171A1A", "#BBC6CD", "#464D53", "#70787E"]
type: ["Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

It follows the keynote arc: mood shot, promise, demo, specs. The hero is a slow macro of the frame catching light, the promise types itself and resolves into capability tabs, a film proves it with green AR text, and only then does the page turn white to explain the hardware with callouts on an exploded view.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Order a product page like a keynote: mood, promise, demo, spec
- Dark for the story, white for the specification; switch once, not repeatedly
- Type the headline's ending so capabilities can be swapped in as tabs

## What to leave

- Promotional popup on load
- Specs set in very small grey text

## Signature move

A black macro of the glasses turning under a sweep of light, behind 'Welcome to Your Second Brain'.

## Motion

Intro: the glasses rotate slowly out of black as light sweeps the frame (~2.5 s, video). Scroll (Lenis, ScrollSmoother, Observer, 21 ScrollTriggers, MorphSVG): 'The Glasses That…' types with a block cursor and tab chips (Capture/Act/Translate) activate in turn; demo film with AR captions; white section with callouts drawing to parts of an exploded frame per feature; ring; phone mockup cycling screens; press logo row.

Measured (`motion/probe.json`): GSAP 3.14.2; 21 ScrollTriggers; Lenis; 15 video; split text; smoothed scroll (median 102 px still travelling after input stops); entry gate: Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a hardware launch page that starts on a black macro of the glasses turning under light, types its promise into tabbed capabilities, plays an AR demo film, then switches to white for exploded product callouts, the ring and the app. Type: Geist.
Ground and ink from the measured palette (#32373B, #FFFFFF, #171A1A). Motion carries the page through
a black macro of the glasses turning under a sweep of light, behind 'Welcome to Your Second Brain'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product macro on black with a light sweep, plus documentary demo footage

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product macro on black with a light sweep, plus documentary demo footage

## Reference lock

Primary reference/direction: MIRA — A hardware launch page that starts on a black macro of the glasses turning under light, types its promise into tabbed capabilities, plays an AR demo film, then switches to white for exploded product callouts, the ring and the app.
Preserve (3-5 traits): black macro product hero rotating under light; typed headline 'The Glasses That…'; tabbed capability chips (Capture, Act, Translate); AR overlay demo video; white product section with orange callouts.
Borrow only (1-2): Order a product page like a keynote: mood, promise, demo, spec; Dark for the story, white for the specification; switch once, not repeatedly
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product macro on black with a light sweep, plus documentary demo footage
Reject: Promotional popup on load; Specs set in very small grey text
Token commitments: palette #32373B, #FFFFFF, #171A1A, #BBC6CD, #464D53, #70787E; type Geist; engine GSAP + Lenis linked (never vendored).
