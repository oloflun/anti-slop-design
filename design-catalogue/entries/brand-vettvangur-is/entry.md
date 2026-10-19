---
title: "Vettvangur brand"
url: https://brand.vettvangur.is/
source_url: https://brand.vettvangur.is/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: ""
family: brand-book-scroll-site
dna: "Icelandic agency rebrand x interactive brand book"
register: modern clean
grammar: chaptered editorial
lane: "A brand-book site for an Icelandic agency's new identity: concentric rings draw around the title on navy, then chapters (logo, type, colour, graphics, voice) alternate navy and white with an orange dot that travels through every section, specimens and logo construction animating."
mode: read
traits: ["navy, white and signal orange", "concentric ring intro", "orange dot that travels through sections", "type specimen cards (Aeonik)", "logo construction animation", "Icelandic copy"]
palette: ["#0B1423", "#F9FBFC", "#796A6C"]
type: ["Aeonik"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A brand guideline told as a scroll: each chapter demonstrates its own rule (the logo builds, the typeface shows its weights, the shapes line up), and a single orange dot is the thread that moves from section to section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Present a brand system as a scroll where each chapter demonstrates its rule
- A single travelling dot as the thread through chapters

## What to leave

- Texts cut mid-transition
- Very small labels in the chrome

## Signature move

An orange dot that travels through every chapter of the brand book.

## Motion

Intro: rings expand on navy around 'Ný ásýnd Vettvangs' (~2 s). Scroll (Lenis, ~150 px glide): white chapter with the dot; logo marks slide in from the sides and merge; navy logo card; 'Letrið setur tóninn' with weight words and specimen cards; colour chapter; shapes; 'Grafíkin styður upplifun og flæði' with shape row; voice; case images; orange close.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 2 video; smoothed scroll (median 149 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a brand-book site for an Icelandic agency's new identity: concentric rings draw around the title on navy, then chapters (logo, type, colour, graphics, voice) alternate navy and white with an orange dot that travels through every section, specimens and logo construction animating. Type: Aeonik.
Ground and ink from the measured palette (#0B1423, #F9FBFC, #796A6C). Motion carries the page through
an orange dot that travels through every chapter of the brand book. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand applications and mockups, flat specimen cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand applications and mockups, flat specimen cards

## Reference lock

Primary reference/direction: Vettvangur brand — A brand-book site for an Icelandic agency's new identity: concentric rings draw around the title on navy, then chapters (logo, type, colour, graphics, voice) alternate navy and white with an orange dot that travels through every section, specimens and logo construction animating.
Preserve (3-5 traits): navy, white and signal orange; concentric ring intro; orange dot that travels through sections; type specimen cards (Aeonik); logo construction animation.
Borrow only (1-2): Present a brand system as a scroll where each chapter demonstrates its rule; A single travelling dot as the thread through chapters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand applications and mockups, flat specimen cards
Reject: Texts cut mid-transition; Very small labels in the chrome
Token commitments: palette #0B1423, #F9FBFC, #796A6C; type Aeonik; engine GSAP + Lenis linked (never vendored).
