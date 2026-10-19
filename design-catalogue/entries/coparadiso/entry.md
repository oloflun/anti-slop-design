---
title: "CoParadiso"
url: https://www.coparadiso.com/
source_url: https://www.coparadiso.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "playful"
family: retro-tropical-coworking
dna: "Melbourne coworking space x 70s tropical sign-painting"
register: warm photographic
grammar: chaptered editorial
lane: "A coworking space branded as a tropical motel: yellow brush-script logo over a beach with a palm, a marquee of perks, photo collages of the space in warm 70s colour, rounded tab cards for membership types and stacked colour notes for testimonials."
mode: persuade
traits: ["brush script logo in yellow", "beach and palm hero", "perk marquee band in orange", "70s warm colour photos", "rounded tab cards", "stacked coloured note cards"]
palette: ["#EDDFCB", "#334A45", "#26241A", "#7B8277", "#5B4631", "#666156"]
type: ["fontBrushScript", "fontWindsor", "fontEurocine", "fontPitchSans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

An office rental becomes a holiday: motel-sign lettering, a palm over the beach, warm orange marquees. The photos of the actual space are graded and composed to match, so the joke never leaves the brand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Allan Pooley).

## What to borrow (principle)

- Borrow a whole period sign-language (70s motel) for a commercial space
- Stack testimonial notes in different colours like pinned memos

## What to leave

- Hero beach is unrelated to the real space
- Small mono body

## Signature move

A brush-script motel sign over a beach with a palm tree.

## Motion

Intro: blurred frame resolves into the beach with the sign (~1.5 s). Scroll (Lenis, ~135 px glide): marquee band slides; statement split; photo collage of the space slides in; dark green 'Experience the Ultimate Coworking Lifestyle' with tabbed cards (Hot Desking, Permanent, Private Studio); stacked notes fan out; 'Come Say Hi' card over a door photo; logo footer.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; smoothed scroll (median 140 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a coworking space branded as a tropical motel: yellow brush-script logo over a beach with a palm, a marquee of perks, photo collages of the space in warm 70s colour, rounded tab cards for membership types and stacked colour notes for testimonials. Type: fontBrushScript, fontWindsor, fontEurocine, fontPitchSans.
Ground and ink from the measured palette (#EDDFCB, #334A45, #26241A). Motion carries the page through
a brush-script motel sign over a beach with a palm tree. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — warm, retro-graded interior photos of the space; beach and palms

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: warm, retro-graded interior photos of the space; beach and palms

## Reference lock

Primary reference/direction: CoParadiso — A coworking space branded as a tropical motel: yellow brush-script logo over a beach with a palm, a marquee of perks, photo collages of the space in warm 70s colour, rounded tab cards for membership types and stacked colour notes for testimonials.
Preserve (3-5 traits): brush script logo in yellow; beach and palm hero; perk marquee band in orange; 70s warm colour photos; rounded tab cards.
Borrow only (1-2): Borrow a whole period sign-language (70s motel) for a commercial space; Stack testimonial notes in different colours like pinned memos
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: warm, retro-graded interior photos of the space; beach and palms
Reject: Hero beach is unrelated to the real space; Small mono body
Token commitments: palette #EDDFCB, #334A45, #26241A, #7B8277, #5B4631, #666156; type fontBrushScript, fontWindsor, fontEurocine, fontPitchSans; engine GSAP + Lenis linked (never vendored).
