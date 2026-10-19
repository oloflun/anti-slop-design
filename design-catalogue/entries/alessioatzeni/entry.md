---
title: "Alessio Atzeni - Creative Developer"
url: https://www.alessioatzeni.com/
source_url: https://www.alessioatzeni.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: monochrome-serif-dev-projects
dna: "Creative developer x serif titles over monochrome project screens and scattered letters"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio on black: a counter loader, letters of a sentence scattering like stars, 'Behind the Scenes' in serif over a faint giant word, the bio, achievements, 'Selected Projects 2017-2026', then monochrome desaturated site screenshots one after another (Manzetti, Two Way, L.G.R, Co.Re jewels, Kaos Store, Vis a Vis, Battistoni) with the name in serif and a round cursor, and 'The Lab'."
mode: read
traits: ["scattered letters as stars", "serif titles", "faint giant background words", "monochrome project screenshots", "round cursor", "counter loader"]
palette: ["#000000", "#4F4F4F", "#2C2C2C", "#8E8E8E", "#151515"]
type: ["OutfitPortfolio", "CormorantGaramondPortfolio"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Desaturating every project keeps a long list calm and consistent; the serif names carry it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Desaturate project screenshots to unify a list

## What to leave

- Very dark grey contrast

## Signature move

Monochrome site screenshots under serif project names.

## Motion

Intro: white counter 000 to 100 (~2 s), black page. Wheel: letters drift into words; the serif title scales in; the bio reveals by line; each project crossfades in grey with its name; 'The Lab' slides up.

Measured (`motion/probe.json`): GSAP 3.12.5; 8 pinned sections; Lenis; smoothed scroll (median 146 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio on black: a counter loader, letters of a sentence scattering like stars, 'Behind the Scenes' in serif over a faint giant word, the bio, achievements, 'Selected Projects 2017-2026', then monochrome desaturated site screenshots one after another (Manzetti, Two Way, L.G.R, Co.Re jewels, Kaos Store, Vis a Vis, Battistoni) with the name in serif and a round cursor, and 'The Lab'. Type: OutfitPortfolio, CormorantGaramondPortfolio.
Ground and ink from the measured palette (#000000, #4F4F4F, #2C2C2C). Motion carries the page through
monochrome site screenshots under serif project names. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots

## Reference lock

Primary reference/direction: Alessio Atzeni - Creative Developer — A developer folio on black: a counter loader, letters of a sentence scattering like stars, 'Behind the Scenes' in serif over a faint giant word, the bio, achievements, 'Selected Projects 2017-2026', then monochrome desaturated site screenshots one after another (Manzetti, Two Way, L.G.R, Co.Re jewels, Kaos Store, Vis a Vis, Battistoni) with the name in serif and a round cursor, and 'The Lab'.
Preserve (3-5 traits): scattered letters as stars; serif titles; faint giant background words; monochrome project screenshots; round cursor.
Borrow only (1-2): Desaturate project screenshots to unify a list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots
Reject: Very dark grey contrast
Token commitments: palette #000000, #4F4F4F, #2C2C2C, #8E8E8E, #151515; type OutfitPortfolio, CormorantGaramondPortfolio; engine GSAP + Lenis linked (never vendored).
