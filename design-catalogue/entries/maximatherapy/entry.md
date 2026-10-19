---
title: "Maxima Therapy"
url: https://maximatherapy.com/
source_url: https://maximatherapy.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "playful"
family: primary-shapes-child-therapy
dna: "Pediatric therapy practice x primary-colour shape illustration"
register: other
grammar: chaptered editorial
lane: "A children's therapy site in primary colours: 'SEE LIFE FROM A DIFFERENT ANGLE' tilts into place, shapes unfold into an illustrated landscape, service cards deal like playing cards, a huge 'learn' word tumbles, and photos of kids sit inside shape-built scenes."
mode: persuade
traits: ["primary red, blue, yellow, green shapes", "condensed caps headlines that tilt", "service cards dealt like a hand", "clouds drifting", "huge tumbling word", "photos framed by shape illustrations"]
palette: ["#FFF2B6", "#FBCB40", "#FEFCEF", "#9D99A1", "#C94444", "#FDDF82"]
type: ["ABC Diatype Rounded", "ABC Diatype Rounded Plus", "Robuck Rounded", "Robuck"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A sensitive service (therapy for neurodivergent children) is made warm and playful through children's-book shapes. The headline literally changes angle ('see life from a different angle'), and the service cards are dealt and shuffled like a game.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Anthony Morell, KOKI-KIKO, Louis Paquet, Nicolas Garnier).

## What to borrow (principle)

- Make the headline do what it says (tilt into place for 'different angle')
- Deal service cards like a hand of playing cards

## What to leave

- Busy compositions
- Small body text on yellow

## Signature move

'SEE LIFE FROM A DIFFERENT ANGLE' tilting into level.

## Motion

Intro: the headline appears tilted and rotates level with clouds drifting (~1.5 s). Scroll (Lenis, ~140 px glide, SplitText): geometric shapes unfold; 'Early Intervention' card; service cards (child development, speech, physical, occupational) deal and stack; statement; giant 'learn' letters tumble; photo of a child within shape scenery; 'THE FIRST YEARS MATTER MOST'; process steps; green 'ADAPTIVE SKILLS TRAINING'.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; split text; smoothed scroll (median 141 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a children's therapy site in primary colours: 'SEE LIFE FROM A DIFFERENT ANGLE' tilts into place, shapes unfold into an illustrated landscape, service cards deal like playing cards, a huge 'learn' word tumbles, and photos of kids sit inside shape-built scenes. Type: ABC Diatype Rounded, ABC Diatype Rounded Plus, Robuck Rounded, Robuck.
Ground and ink from the measured palette (#FFF2B6, #FBCB40, #FEFCEF). Motion carries the page through
'SEE LIFE FROM A DIFFERENT ANGLE' tilting into level. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — real photos of children at play combined with flat primary-colour shapes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: real photos of children at play combined with flat primary-colour shapes

## Reference lock

Primary reference/direction: Maxima Therapy — A children's therapy site in primary colours: 'SEE LIFE FROM A DIFFERENT ANGLE' tilts into place, shapes unfold into an illustrated landscape, service cards deal like playing cards, a huge 'learn' word tumbles, and photos of kids sit inside shape-built scenes.
Preserve (3-5 traits): primary red, blue, yellow, green shapes; condensed caps headlines that tilt; service cards dealt like a hand; clouds drifting; huge tumbling word.
Borrow only (1-2): Make the headline do what it says (tilt into place for 'different angle'); Deal service cards like a hand of playing cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: real photos of children at play combined with flat primary-colour shapes
Reject: Busy compositions; Small body text on yellow
Token commitments: palette #FFF2B6, #FBCB40, #FEFCEF, #9D99A1, #C94444, #FDDF82; type ABC Diatype Rounded, ABC Diatype Rounded Plus, Robuck Rounded, Robuck; engine GSAP + Lenis linked (never vendored).
