---
title: "SOHub"
url: https://sohub.digital/
source_url: https://sohub.digital/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: robot-arm-stacked-services
dna: "Digital agency x 3D robot arm and stacked service cards"
register: modern clean
grammar: chaptered editorial
lane: "An agency page where a 3D robotic arm peeks over a huge 'sohub' wordmark, cases sit in a two-column image grid, services are dark rounded cards that stack on top of each other one per scroll beat, and a mechanical capsule rises at the close."
mode: persuade
traits: ["3D robotic arm and machine props", "huge cropped wordmark", "grey highlighted word in each statement", "stacking dark rounded service cards", "two-column case grid", "pill controls"]
palette: ["#F1F5F9", "#D8E1E2", "#0D0F15", "#6C686E", "#3F2A60", "#B5BABD"]
type: ["Inter", "publicaPlay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Services arrive as a deck: each dark card slides up and lands on the one before, leaving only its title visible, so four services read as one tidy stack. 3D machine parts (an arm, a capsule) are the recurring props that make the agency feel engineered.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stack service cards on top of each other so earlier titles stay visible as tabs
- One grey-highlighted word per statement for emphasis
- Recurring 3D machine props as the brand's objects

## What to leave

- Generic case grid
- Many pill buttons in the chrome

## Signature move

Dark service cards stacking on top of each other, titles left showing like tabs.

## Motion

Intro: logo mark morphs on navy (~2 s), white page with the arm reaching over 'sohub'. Scroll (Lenis, ~150 px glide, 1 pin, SplitText): statement with grey word; case grid in two columns; statement; service cards (Brand Identities, Smart Development, Marketing Campaigns, 3D Visualization) slide up and stack; 'Don't be shy' with a robot chair; capsule rises over the wordmark footer.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; split text; smoothed scroll (median 151 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency page where a 3D robotic arm peeks over a huge 'sohub' wordmark, cases sit in a two-column image grid, services are dark rounded cards that stack on top of each other one per scroll beat, and a mechanical capsule rises at the close. Type: Inter, publicaPlay.
Ground and ink from the measured palette (#F1F5F9, #D8E1E2, #0D0F15). Motion carries the page through
dark service cards stacking on top of each other, titles left showing like tabs. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D industrial/robotic renders on light grey; campaign case images

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D industrial/robotic renders on light grey; campaign case images

## Reference lock

Primary reference/direction: SOHub — An agency page where a 3D robotic arm peeks over a huge 'sohub' wordmark, cases sit in a two-column image grid, services are dark rounded cards that stack on top of each other one per scroll beat, and a mechanical capsule rises at the close.
Preserve (3-5 traits): 3D robotic arm and machine props; huge cropped wordmark; grey highlighted word in each statement; stacking dark rounded service cards; two-column case grid.
Borrow only (1-2): Stack service cards on top of each other so earlier titles stay visible as tabs; One grey-highlighted word per statement for emphasis
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D industrial/robotic renders on light grey; campaign case images
Reject: Generic case grid; Many pill buttons in the chrome
Token commitments: palette #F1F5F9, #D8E1E2, #0D0F15, #6C686E, #3F2A60, #B5BABD; type Inter, publicaPlay; engine GSAP + Lenis linked (never vendored).
