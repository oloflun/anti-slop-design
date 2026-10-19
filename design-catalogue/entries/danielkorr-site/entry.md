---
title: "Daniel Korr"
url: http://danielkorr.site/
source_url: http://danielkorr.site/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: capture-letterbox-photographer
dna: "Photographer folio x word with a photo in its gap"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A black photographer site with 'CAPTURE' in huge condensed type where a cropped portrait sits inside the missing letters, then work as image pairs over a dark red band and a closing '(LABS)' in brackets."
mode: persuade
traits: ["huge word with a photo replacing letters", "black ground with dark red bands", "image pairs with mono captions", "bracketed section words", "condensed grotesque"]
palette: ["#000000", "#44454A", "#78A4A1", "#306D87", "#D0D6D1", "#173542"]
type: ["Inconsolata", "Aguafina Script", "News Cycle"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The hero word 'CAPTURE' is missing its middle letters and a photo fills the hole, so the word and the medium are one object. Work then comes in pairs over a dark red band, like contact prints on a darkroom bench.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Thokozani Mavuso).

## What to borrow (principle)

- Remove letters from a hero word and put the photo in the gap
- Pair images over a single dark colour band as a darkroom metaphor

## What to leave

- Section words get letters knocked out during transitions and read as broken
- Thin mono captions

## Signature move

A portrait set inside the missing letters of 'CAPTURE'.

## Motion

Intro: 'CAPTURE' with the portrait in the gap (~1 s). Scroll (Lenis, ~150 px glide, SplitText): the word lifts and 'WORKS' assembles with missing letters filling in; image pairs (Weekend Times, Vogue, Netflix, Delhi Festival, editorial) slide up over a dark red band; '(LABS)' letters assemble.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 1 video; split text; smoothed scroll (median 150 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a black photographer site with 'CAPTURE' in huge condensed type where a cropped portrait sits inside the missing letters, then work as image pairs over a dark red band and a closing '(LABS)' in brackets. Type: Inconsolata, Aguafina Script, News Cycle.
Ground and ink from the measured palette (#000000, #44454A, #78A4A1). Motion carries the page through
a portrait set inside the missing letters of 'CAPTURE'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — fashion and editorial photography, high contrast, colour accents

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: fashion and editorial photography, high contrast, colour accents

## Reference lock

Primary reference/direction: Daniel Korr — A black photographer site with 'CAPTURE' in huge condensed type where a cropped portrait sits inside the missing letters, then work as image pairs over a dark red band and a closing '(LABS)' in brackets.
Preserve (3-5 traits): huge word with a photo replacing letters; black ground with dark red bands; image pairs with mono captions; bracketed section words; condensed grotesque.
Borrow only (1-2): Remove letters from a hero word and put the photo in the gap; Pair images over a single dark colour band as a darkroom metaphor
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: fashion and editorial photography, high contrast, colour accents
Reject: Section words get letters knocked out during transitions and read as broken; Thin mono captions
Token commitments: palette #000000, #44454A, #78A4A1, #306D87, #D0D6D1, #173542; type Inconsolata, Aguafina Script, News Cycle; engine GSAP + Lenis linked (never vendored).
