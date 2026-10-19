---
title: "Greater - Design Partner"
url: https://www.greaterstudio.com/
source_url: https://www.greaterstudio.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: agency-case-cards-curved-carousel
dna: "Design partnership studio x serif headline and a curved card carousel finale"
register: modern clean
grammar: chaptered editorial
lane: "A design agency: 'Your search for a design partner ends here' in a serif on pale pink with a hand emoji and badges, case cards with growth stats, big numbers ($800M+, 10+, 48+, 1000s), research articles, service cards, a testimonial, 'Rise above into forever' over a curved 3D carousel of work and a giant script 'Greater' wordmark footer."
mode: persuade
traits: ["serif headline on pale pink", "case cards with growth stats", "big number grid", "curved 3D work carousel", "giant script wordmark footer", "small orange tags"]
palette: ["#F7F2F1", "#202C4B", "#536164", "#B0A9A6", "#D4D09D"]
type: ["Perfectlynineties", "Spacemono", "Peridot PE Variable", "articulat-cf"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The curved carousel at the end is the one spatial moment that frames the CTA.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- End on a curved carousel of the work behind the CTA

## What to leave

- Generic agency content
- Small text

## Signature move

A curved 3D carousel of work behind 'Rise above into forever'.

## Motion

Intro: the hero with a cookie banner (rejected). Wheel (smoothed ~100 px): case cards rise; numbers count; articles slide; service cards stagger; the curved carousel rotates as you scroll; the script wordmark rises.

Measured (`motion/probe.json`): GSAP 3.12.7/3.12.5/3.12.5/3.12.2; 6 ScrollTriggers; WebGL canvas x1 (three.js); smoothed scroll (median 119 px still travelling after input stops); entry gate: Reject All. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a design agency: 'Your search for a design partner ends here' in a serif on pale pink with a hand emoji and badges, case cards with growth stats, big numbers ($800M+, 10+, 48+, 1000s), research articles, service cards, a testimonial, 'Rise above into forever' over a curved 3D carousel of work and a giant script 'Greater' wordmark footer. Type: Perfectlynineties, Spacemono, Peridot PE Variable, articulat-cf.
Ground and ink from the measured palette (#F7F2F1, #202C4B, #536164). Motion carries the page through
a curved 3D carousel of work behind 'Rise above into forever'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — case photography and UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: case photography and UI

## Reference lock

Primary reference/direction: Greater - Design Partner — A design agency: 'Your search for a design partner ends here' in a serif on pale pink with a hand emoji and badges, case cards with growth stats, big numbers ($800M+, 10+, 48+, 1000s), research articles, service cards, a testimonial, 'Rise above into forever' over a curved 3D carousel of work and a giant script 'Greater' wordmark footer.
Preserve (3-5 traits): serif headline on pale pink; case cards with growth stats; big number grid; curved 3D work carousel; giant script wordmark footer.
Borrow only (1-2): End on a curved carousel of the work behind the CTA
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: case photography and UI
Reject: Generic agency content; Small text
Token commitments: palette #F7F2F1, #202C4B, #536164, #B0A9A6, #D4D09D; type Perfectlynineties, Spacemono, Peridot PE Variable, articulat-cf; engine GSAP + Lenis linked (never vendored).
