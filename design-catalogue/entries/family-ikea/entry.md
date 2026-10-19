---
title: "Desmontando los 30 (IKEA Family)"
url: https://www.family.ikea.es/demos/desmontando-los-30/
source_url: https://www.family.ikea.es/demos/desmontando-los-30/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "consumer-brand"
family: marble-run-campaign
dna: "Retail anniversary campaign x 3D marble run"
register: other
grammar: continuous world
lane: "An anniversary microsite where a 3D marble-run in IKEA colours forms the number 30, a ball travels the track as the preloader, and scrolling sends it down a vertical run into the entry form."
mode: experience
traits: ["3D marble-run illustration in primary colours", "ball on track as the loader (76%)", "number 30 built from track pieces", "vertical track that guides the scroll", "form panel slides in beside the track"]
palette: ["#C4C3BC", "#FAFAFA", "#DFD29C", "#AF9980", "#E4E3DC"]
type: ["NotoIKEALatin"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The campaign's metaphor (taking 30 years apart, piece by piece) is literal: the number is a toy track and the ball is the visitor. The loader is the ball rolling, the hero is the assembled 30, and the scroll follows the ball down a single vertical run until the form appears beside it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: /nk.studio, MRM Spain, Mach Studio).

## What to borrow (principle)

- Make the loader a moving piece of the hero object so loading is already the story
- Let one object (a ball) carry the visitor down the page as the scroll guide
- Bring a form in beside the illustration instead of below it

## What to leave

- Ends at a form asking for a loyalty card number: the experience is short
- Large flat yellow gradient areas around a narrow track

## Signature move

A marble that rolls through a 3D track shaped like the number 30, then leads the scroll down the page.

## Motion

Intro: close-up of a ball rolling in a track with a percentage counter (76%), camera pulls back to the full '30' track (~2.5 s). Scroll (virtual, Lenis, SplitText, useGSAP): the 30 shrinks to the left as 'DESMONTANDO LOS 30' types in; the scene becomes a vertical run with the ball travelling down; the participation form slides in from the right.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 4 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the continuous world grammar: an anniversary microsite where a 3D marble-run in IKEA colours forms the number 30, a ball travels the track as the preloader, and scrolling sends it down a vertical run into the entry form. Type: NotoIKEALatin.
Ground and ink from the measured palette (#C4C3BC, #FAFAFA, #DFD29C). Motion carries the page through
a marble that rolls through a 3D track shaped like the number 30, then leads the scroll down the page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D toy/marble-run render in brand primaries on a warm neutral ground

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D toy/marble-run render in brand primaries on a warm neutral ground

## Reference lock

Primary reference/direction: Desmontando los 30 (IKEA Family) — An anniversary microsite where a 3D marble-run in IKEA colours forms the number 30, a ball travels the track as the preloader, and scrolling sends it down a vertical run into the entry form.
Preserve (3-5 traits): 3D marble-run illustration in primary colours; ball on track as the loader (76%); number 30 built from track pieces; vertical track that guides the scroll; form panel slides in beside the track.
Borrow only (1-2): Make the loader a moving piece of the hero object so loading is already the story; Let one object (a ball) carry the visitor down the page as the scroll guide
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D toy/marble-run render in brand primaries on a warm neutral ground
Reject: Ends at a form asking for a loyalty card number: the experience is short; Large flat yellow gradient areas around a narrow track
Token commitments: palette #C4C3BC, #FAFAFA, #DFD29C, #AF9980, #E4E3DC; type NotoIKEALatin; engine GSAP + Lenis linked (never vendored).
