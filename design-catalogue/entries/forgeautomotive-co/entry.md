---
title: "Forge Automotive"
url: https://forgeautomotive.co.uk/
source_url: https://forgeautomotive.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: ""
family: black-atelier-automotive
dna: "Bespoke car builder x slow cinematic editorial"
register: cinematic dark
grammar: chaptered editorial
lane: "A black page behind an ENTER gate where manifesto words come out of blur one by one, a stitched-leather close-up grows from a card to full bleed, and numbered principles and services pass as sticky text beside rising photographs."
mode: persuade
traits: ["entry gate", "words deblurring one by one", "card-to-full-bleed image growth", "numbered sticky slides 01/03", "text that fills from grey to white per word", "condensed serif display over small sans"]
palette: ["#000000", "#393939", "#181818", "#4F4F50"]
type: ["GeistSans", "editorial"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Everything is slowed to the pace of craft: the gate, then single words resolving out of blur, then a manifesto line that fills with light word by word as you read it. Images never just appear; a close-up of red stitching starts as a small card behind the heading and grows until it is the frame, which turns 'detail' into the subject of the page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: 12 Studio, Adam Roberts, Joe Ben Taylor).

## What to borrow (principle)

- Let one image grow from a card behind the headline to full bleed: the zoom is the transition into the next chapter
- Fill a statement from grey to ink word by word with scroll so the reader's pace sets the reveal
- Numbered sticky slides (01/03) for principles, each with its own image rising behind

## What to leave

- The ENTER gate adds a click before any content
- Very low-contrast grey text before it fills

## Signature move

A leather-stitching close-up that grows from a card behind the headline into the full frame.

## Motion

Gate: ENTER, then short white text on black, then 'For Those Who Refuse…' resolves word by word out of heavy blur (~2 s). Scroll (virtual, window stays at 0, Lenis): 'We Don't Modify Vehicles / We Build Them For You' centred; the stitching image grows from a card into full bleed as the heading splits apart; three numbered slides (Identity / Insight / Cohesion) with a photo card scaling in each; 'A vehicle should say something before it moves…' fills grey→white per word; Bodystyling / Interior / Wheels as sticky text left with a photo stack rising on the right.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a black page behind an ENTER gate where manifesto words come out of blur one by one, a stitched-leather close-up grows from a card to full bleed, and numbered principles and services pass as sticky text beside rising photographs. Type: GeistSans, editorial.
Ground and ink from the measured palette (#000000, #393939, #181818). Motion carries the page through
a leather-stitching close-up that grows from a card behind the headline into the full frame. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — macro close-ups of material (stitching, carbon, paint), low-key light, deep blacks, one warm accent

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: macro close-ups of material (stitching, carbon, paint), low-key light, deep blacks, one warm accent

## Reference lock

Primary reference/direction: Forge Automotive — A black page behind an ENTER gate where manifesto words come out of blur one by one, a stitched-leather close-up grows from a card to full bleed, and numbered principles and services pass as sticky text beside rising photographs.
Preserve (3-5 traits): entry gate; words deblurring one by one; card-to-full-bleed image growth; numbered sticky slides 01/03; text that fills from grey to white per word.
Borrow only (1-2): Let one image grow from a card behind the headline to full bleed: the zoom is the transition into the next chapter; Fill a statement from grey to ink word by word with scroll so the reader's pace sets the reveal
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: macro close-ups of material (stitching, carbon, paint), low-key light, deep blacks, one warm accent
Reject: The ENTER gate adds a click before any content; Very low-contrast grey text before it fills
Token commitments: palette #000000, #393939, #181818, #4F4F50; type GeistSans, editorial; engine GSAP + Lenis linked (never vendored).
