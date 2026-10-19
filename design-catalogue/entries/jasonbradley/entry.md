---
title: "Jason Bradley"
url: https://jasonbradley.co/
source_url: https://jasonbradley.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: fullbleed-film-thumbstrip
dna: "Design technologist folio x full-bleed film with thumbnail strip"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A folio of full-bleed project films: a black intro opens on a sunset silhouette, and each wheel step cuts to the next film while a strip of thumbnails along the bottom shows where you are."
mode: experience
traits: ["full-bleed looping project films", "thumbnail strip as position indicator", "tiny centred name and role", "credits in small type at right", "varied campaign photography"]
palette: ["#E5E5E5", "#C9C7C4", "#A9A8A6", "#010103", "#111720", "#4E4D44"]
type: ["ReworkText", "UniversNextPro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Like a reel with a timeline: the frame is always full, the bottom strip of thumbnails is the index and the progress at once, and the active thumb lifts. The intro frames the first film rising out of black with only the name visible.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Bruno Arizio, Jason Bradley).

## What to borrow (principle)

- A thumbnail strip along the bottom as both index and progress for a reel
- Open the first film by raising it out of black under a tiny name

## What to leave

- Wheel-only; no overview without the strip
- Very small credits text over busy footage

## Signature move

A sunset silhouette film rising out of black under a tiny name, then a wheel that cuts film to film over a live thumbnail strip.

## Motion

Intro: 'JASON BRADLEY / DESIGN TECHNOLOGIST' tiny on black, the sunset film rises from the bottom and fills the frame (~1.5 s). Wheel (virtual, Lenis, SplitText): each step cuts to the next full-bleed film; the active thumbnail in the bottom strip highlights; credits at right swap per project.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; 20 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Close. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a folio of full-bleed project films: a black intro opens on a sunset silhouette, and each wheel step cuts to the next film while a strip of thumbnails along the bottom shows where you are. Type: ReworkText, UniversNextPro.
Ground and ink from the measured palette (#E5E5E5, #C9C7C4, #A9A8A6). Motion carries the page through
a sunset silhouette film rising out of black under a tiny name, then a wheel that cuts film to film over a live thumbnail strip. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign films with strong colour and light, varied subjects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign films with strong colour and light, varied subjects

## Reference lock

Primary reference/direction: Jason Bradley — A folio of full-bleed project films: a black intro opens on a sunset silhouette, and each wheel step cuts to the next film while a strip of thumbnails along the bottom shows where you are.
Preserve (3-5 traits): full-bleed looping project films; thumbnail strip as position indicator; tiny centred name and role; credits in small type at right; varied campaign photography.
Borrow only (1-2): A thumbnail strip along the bottom as both index and progress for a reel; Open the first film by raising it out of black under a tiny name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign films with strong colour and light, varied subjects
Reject: Wheel-only; no overview without the strip; Very small credits text over busy footage
Token commitments: palette #E5E5E5, #C9C7C4, #A9A8A6, #010103, #111720, #4E4D44; type ReworkText, UniversNextPro; engine GSAP + Lenis linked (never vendored).
