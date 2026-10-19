---
title: "Nico Menezes - Webflow developer"
url: https://www.nicomenezes.com/
source_url: https://www.nicomenezes.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: inline-image-bio-dev-folio
dna: "Webflow developer x a bio with inline images and full-bleed project cards"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio: 'NICO MENEZES' huge on white, a bio sentence with small inline images ('a brazilian [photo] Webflow Developer [logo] who builds [screen] websites'), full-bleed dark project panels (ARCA with a chrome sculpture, AWARDCO with a dot map, UNCAGED with a dancer) that slide over each other with a name and 'About more', 'SEE ALL PROJECTS' over a tilted grid, 'ABILITIES' with a service grid and a black 'LET'S CHAT' footer."
mode: read
traits: ["inline images in the bio sentence", "full-bleed project panels sliding over", "tilted project grid", "huge grotesk name", "black footer with underline", "side tab"]
palette: ["#FFFFFF", "#1B1C17", "#3D4451", "#2D3034", "#889095"]
type: ["Nohemi", "Generalsans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Inline images inside the bio sentence make an intro both readable and visual.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Put small images inline in the bio sentence

## What to leave

- Generic abilities grid

## Signature move

'a brazilian [photo] Webflow Developer [logo]' with inline images.

## Motion

Intro: white (~1 s), the name rises. Wheel (Lenis, Flip): the name scrolls off; bio words fade from grey; project panels slide over each other; the tilted grid scrolls; ability columns slide; the footer underline draws.

Measured (`motion/probe.json`): GSAP 3.12.5/3.15.0; 9 ScrollTriggers; Lenis; 3 video; smoothed scroll (median 169 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio: 'NICO MENEZES' huge on white, a bio sentence with small inline images ('a brazilian [photo] Webflow Developer [logo] who builds [screen] websites'), full-bleed dark project panels (ARCA with a chrome sculpture, AWARDCO with a dot map, UNCAGED with a dancer) that slide over each other with a name and 'About more', 'SEE ALL PROJECTS' over a tilted grid, 'ABILITIES' with a service grid and a black 'LET'S CHAT' footer. Type: Nohemi, Generalsans.
Ground and ink from the measured palette (#FFFFFF, #1B1C17, #3D4451). Motion carries the page through
'a brazilian [photo] Webflow Developer [logo]' with inline images. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography

## Reference lock

Primary reference/direction: Nico Menezes - Webflow developer — A developer folio: 'NICO MENEZES' huge on white, a bio sentence with small inline images ('a brazilian [photo] Webflow Developer [logo] who builds [screen] websites'), full-bleed dark project panels (ARCA with a chrome sculpture, AWARDCO with a dot map, UNCAGED with a dancer) that slide over each other with a name and 'About more', 'SEE ALL PROJECTS' over a tilted grid, 'ABILITIES' with a service grid and a black 'LET'S CHAT' footer.
Preserve (3-5 traits): inline images in the bio sentence; full-bleed project panels sliding over; tilted project grid; huge grotesk name; black footer with underline.
Borrow only (1-2): Put small images inline in the bio sentence
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography
Reject: Generic abilities grid
Token commitments: palette #FFFFFF, #1B1C17, #3D4451, #2D3034, #889095; type Nohemi, Generalsans; engine GSAP + Lenis linked (never vendored).
