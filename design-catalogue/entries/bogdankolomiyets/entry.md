---
title: "Bogdan Kolomiyets"
url: https://bogdankolomiyets.com/
source_url: https://bogdankolomiyets.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: yes-script-designer-folio
dna: "Independent designer folio x condensed caps and red script 'Yes!'"
register: editorial print
grammar: chaptered editorial
lane: "A designer folio whose portrait cuts through 'WEBSITES THAT MAKE CLIENTS SAY 'YES!'', the 'Yes!' in a red handwritten script, then projects (Nodeck, Estelle, Kivra) on black with hanging images on threads, a big 'ABOUT' with a polaroid, and testimonial cards stacked like letters."
mode: persuade
traits: ["condensed caps with red script word", "portrait cut-out over the headline", "images hanging on threads", "polaroid photo", "stacked testimonial cards", "beige and black alternation"]
palette: ["#1A1A18", "#F2F0ED", "#6C4941", "#C0AA9F", "#E6E7C1"]
type: ["PP Neue Montreal", "Lektorat", "Tentang Nanti One"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The single red script 'Yes!' is the voice of the whole page and returns in the final CTA; project images hang on thin threads like mobiles, so each case feels like an object presented rather than a screenshot.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One handwritten script word in colour as the recurring voice
- Hang project images on threads so they sway in
- Stack testimonials as tilted letters

## What to leave

- Cookie popup on every frame
- Busy type mixes

## Signature move

Project images hanging on thin threads, swaying into place.

## Motion

Intro: portrait and headline with the script 'Yes!' writing in (~1.5 s). Scroll (Lenis, video, SplitText): mission line with video intro; black 'What saying yes looks like' with projects whose images drop in on threads; 'SEE ALL'; 'ABOUT' with a polaroid; testimonials stacking; FAQ; 'READY TO HEAR MORE "YES"?'.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 1 video; split text; smoothed scroll (median 140 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a designer folio whose portrait cuts through 'WEBSITES THAT MAKE CLIENTS SAY "YES!"', the 'Yes!' in a red handwritten script, then projects (Nodeck, Estelle, Kivra) on black with hanging images on threads, a big 'ABOUT' with a polaroid, and testimonial cards stacked like letters. Type: PP Neue Montreal, Lektorat, Tentang Nanti One.
Ground and ink from the measured palette (#1A1A18, #F2F0ED, #6C4941). Motion carries the page through
project images hanging on thin threads, swaying into place. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product mockups and lifestyle photos, warm

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product mockups and lifestyle photos, warm

## Reference lock

Primary reference/direction: Bogdan Kolomiyets — A designer folio whose portrait cuts through 'WEBSITES THAT MAKE CLIENTS SAY "YES!"', the 'Yes!' in a red handwritten script, then projects (Nodeck, Estelle, Kivra) on black with hanging images on threads, a big 'ABOUT' with a polaroid, and testimonial cards stacked like letters.
Preserve (3-5 traits): condensed caps with red script word; portrait cut-out over the headline; images hanging on threads; polaroid photo; stacked testimonial cards.
Borrow only (1-2): One handwritten script word in colour as the recurring voice; Hang project images on threads so they sway in
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product mockups and lifestyle photos, warm
Reject: Cookie popup on every frame; Busy type mixes
Token commitments: palette #1A1A18, #F2F0ED, #6C4941, #C0AA9F, #E6E7C1; type PP Neue Montreal, Lektorat, Tentang Nanti One; engine GSAP + Lenis linked (never vendored).
