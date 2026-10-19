---
title: "Make Design"
url: https://makedesign.tech/
source_url: https://makedesign.tech/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: gold-coil-proptech
dna: "Real-estate design tool x gold coiled sphere"
register: cinematic dark
grammar: chaptered editorial
lane: "A proptech product page that counts 22 → 82, sets a gold coiled sphere as the mark, shows interior customisation as cards beside renders, then turns light where the sphere becomes silver and gold to mark each benefit, closing on a black disc 'SCHEDULE A DEMO'."
mode: persuade
traits: ["number loader", "gold coiled sphere mark", "dark interior render cards", "light chapter with metal sphere", "benefit callout chips around the sphere", "black disc CTA"]
palette: ["#0C0A0A", "#F5F2EB", "#252122", "#5C564D", "#F0D376", "#AB9E79"]
type: ["Led Counter", "Neue Haas"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One object (a coiled metal sphere) is the brand: gold on dark for the product chapters, silver and gold on light for the benefits, and finally a black disc for the CTA, so the chapters are told by the same object changing material.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: ADELT).

## What to borrow (principle)

- Change the material of one recurring object per chapter
- Place benefit chips around a central object instead of a list

## What to leave

- Headline letters scattered during the intro
- Busy render cards

## Signature move

A coiled metal sphere that turns from gold to silver to a black CTA disc.

## Motion

Intro: white with '22 → 55 → 82' bottom-left (~2 s). Scroll (Lenis, ~145 px glide, 20 ScrollTriggers, SplitText): dark hero with the gold sphere and scattered title letters resolving; sphere shrinks to the corner; feature cards for real-world data, interior customisation, estimation, furniture purchase; light chapter where the sphere rotates with benefit chips; sphere turns black for 'SCHEDULE A DEMO'.

Measured (`motion/probe.json`): GSAP 3.15.0/3.11.3; 20 ScrollTriggers; Lenis; 4 video; split text; smoothed scroll (median 148 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a proptech product page that counts 22 → 82, sets a gold coiled sphere as the mark, shows interior customisation as cards beside renders, then turns light where the sphere becomes silver and gold to mark each benefit, closing on a black disc 'SCHEDULE A DEMO'. Type: Led Counter, Neue Haas.
Ground and ink from the measured palette (#0C0A0A, #F5F2EB, #252122). Motion carries the page through
a coiled metal sphere that turns from gold to silver to a black CTA disc. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior renders, metal 3D object

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior renders, metal 3D object

## Reference lock

Primary reference/direction: Make Design — A proptech product page that counts 22 → 82, sets a gold coiled sphere as the mark, shows interior customisation as cards beside renders, then turns light where the sphere becomes silver and gold to mark each benefit, closing on a black disc 'SCHEDULE A DEMO'.
Preserve (3-5 traits): number loader; gold coiled sphere mark; dark interior render cards; light chapter with metal sphere; benefit callout chips around the sphere.
Borrow only (1-2): Change the material of one recurring object per chapter; Place benefit chips around a central object instead of a list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior renders, metal 3D object
Reject: Headline letters scattered during the intro; Busy render cards
Token commitments: palette #0C0A0A, #F5F2EB, #252122, #5C564D, #F0D376, #AB9E79; type Led Counter, Neue Haas; engine GSAP + Lenis linked (never vendored).
