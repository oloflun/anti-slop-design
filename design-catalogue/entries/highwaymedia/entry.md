---
title: "Highway Media"
url: https://highwaymedia.se/webbyra-goteborg/
source_url: https://highwaymedia.se/webbyra-goteborg/
captured: 2026-09-15
origin: raw-url
raw: ""
extract: ok
category: portfolio
category2: "product-focused"
family: white-sheet-agency
dna: "Swedish full-service web agency sheet x rounded-card timeline process"
register: modern clean
grammar: chaptered editorial
lane: "A white sheet with a pink wordmark, a black grotesk headline and one offset photo, then case cards, a CMS pitch, a logo row, a vertical pink timeline that walks the work process in four phases, a support card, a named project leader and a footer that rides in on a rounded white sheet"
mode: persuade
traits: ["white ground, black grotesk 600, pink wordmark", "photo with an offset flat colour block behind it", "rounded 24px cards for cases, logos and support", "vertical timeline with a pink line and plum dots for the process", "pill CTA row in the header", "named project leader with portrait and phone", "rounded-top white sheet as footer", "chat widget and cookie card in every viewport"]
palette: ["#FFFFFF", "#624058", "#EC8AA3", "#232323", "#000000", "#495057", "#929292", "#656565", "#DEE2E6", "#CCCCCC", "#333333", "#FFE8EE"]
type: ["Inter", "Outfit", "Open Sans"]
measured: designlang (palette and type from highwaymedia-se-design-tokens.json; motion tokens from highwaymedia-se-design-language.md, feel smooth, scroll-linked). Grounds outside the token list (the green offset block behind the hero photo, the pale pink offer band on /tjanster/hemsida) are read off the captures, not measured.
kind: reference-style
source: claude
status: ready
---

## Why it works

The page is a white sheet and it never pretends otherwise. Everything that is not the
sheet is a rounded object placed on it: the hero photograph with a flat green block
offset behind it, three case cards in their own grounds, five customer logos in bordered
cards, a support card, and finally a footer that slides in as a second sheet with a
rounded top edge. Because every object shares the same 24 px corner, the page reads as
one material system even though its sections carry very different content. The grotesk
does the rest: one weight (600) for every heading from the 84 px H1 down to the 34 px
card title, so hierarchy is size alone, and a plain 20 px body in a second sans.

The process is the page's one structural device. "Så arbetar vi" is a vertical timeline,
a pink hairline with plum dots, one dot per phase (four phases on /tjanster/hemsida:
Uppstart och strategi, Design och utveckling, Innehåll, Lansering), each phase paired
with a 3D blob render on the right. In the capture the phase text had not revealed
(the reveal is scroll-triggered and the capture ran under a reduced-motion setting), so
the slices show the skeleton of the device rather than its words: the line, the dots and
the blobs carry the section even without copy, which is the skeleton test passed.

Colour is rationed by role. The plum (`#624058`) is the only filled button and the
timeline dot; the pink (`#EC8AA3`) is the wordmark, the breadcrumb's current page, the
timeline line and the case-card title; the green block behind the hero photo appears
once. Nothing else on the sheet is chromatic, so the three colours are legible as three
jobs. The read is offset by two persistent widgets, a chat bubble and a cookie card, that
sit in every viewport and compete with the hero for the lower-left corner.

## What to borrow (principle)

- **Name the phases of the work and give each one a fixed place on a line.** The
  timeline says "this is a sequence with a beginning and an end" before a word is read.
- **One corner radius for every object on the sheet**, so cards, photos and the footer
  read as one material.
- **One heading weight; hierarchy by size only.**
- **A named person as the contact**, not a form: the reader knows who answers.
- **A flat colour block offset behind the hero photograph** as the only depth device.

## What to leave

- Three equal case cards and five equal logo cards: the template rhythm TASTE § 5 counts
  at zero in Anton's own sources.
- The persistent chat widget and the cookie card that sit in the fold on every screen.
- Reveal-on-scroll that leaves the timeline empty when motion is gated by the OS
  setting: F-011 forbids the gate outright.
- The `→` suffix on `Se alla case` (gate 97) and the breadcrumb.
- Customer logos, a Google Partner badge and a named team member: PRODUCT.md § absences
  forbids all three for Alunix.

## Signature move

The process as a vertical timeline: a pink hairline runs down the left margin, a plum dot
marks each phase, and each phase owns one 3D render on the right, so the work reads as a
line the reader travels rather than four cards.

## Motion

Feel "smooth", scroll-linked. Durations 100 to 800 ms, `ease` on 34 of 36 transitions, one
`ease-out` and one custom `cubic-bezier(0.445, 0.05, 0.55, 0.95)`. One keyframe in use,
`infiniteScroll` (a `transform` marquee, used twice, the logo carousel on mobile). The
timeline phases are revealed on scroll; under a reduced-motion setting the reveal never
fired and the phase copy stayed hidden in the capture, which is the one thing this page
does with motion and the one thing it gets wrong for this design system. No parallax, no
pin, no scrub. (from designlang extract, plus the captured slices)

| kind | tokens |
|---|---|
| durations | instant 1ms · xs 100ms · sm 200ms · md 300ms · lg 600ms · xl 800ms |
| easings | ease-in-out `ease` · ease-out `cubic-bezier(0, 0.55, 0.45, 1)` · custom `cubic-bezier(0.445, 0.05, 0.55, 0.95)` |
| keyframes declared | `fa-spin` · `progress-bar-stripes` · `infiniteScroll` · `divider1` · `pathAnim-0..2` · `coworker_box_1..2` |

## Brief

Build a service page for a web agency on a plain white sheet: pink wordmark top left, a
pill CTA row top right, a breadcrumb, then a two-line black grotesk H1 with an H2 and a
short paragraph on the left and one photograph on the right with a flat colour block
offset behind it. Below: three case tiles on their own coloured grounds, a short CMS
pitch with the tool's logotype, a row of customer logos, and the page's device, a
vertical timeline that walks the work in four named phases with one render per phase.
Close with a support card beside a photo, a named project leader with phone and mail,
and a footer that arrives as a rounded white sheet.

## Image recipe

Documentary photograph of [SUBJECT] at a desk with the delivered website on the screen,
window light, neutral colour, cropped so the screen is readable; behind it a flat colour
block offset down and right by about a tenth of the frame. For the process, one abstract
3D render per phase on a plain field, never a screenshot.

## Photo search

Unsplash first, Pexels second.
- "person at desk website on monitor window light"
- "designer reviewing website on imac"
- "abstract 3d render soft shapes plain background"

## Reference lock

Primary reference/direction: Highway Media, a white agency sheet whose one device is a
vertical timeline that names the phases of the work.
Preserve (3-5 traits): white ground with black grotesk in one weight, hierarchy by size;
one corner radius on every object; a flat colour block offset behind the hero photo as
the only depth; the process as a line with a dot per named phase; a named human as the
contact.
Borrow only (1-2): the phase order Uppstart, Design och utveckling, Innehåll, Lansering as
a principle for any process description; the offset colour block behind a photograph.
Role rules: plum is the filled button and the timeline dot, nothing else; pink is the
wordmark, the current breadcrumb and the timeline line; the green block appears once.
Media strategy: photo:unsplash for people at work, generated 3D renders for the process
phases; never a screenshot drawn as chrome.
Reject: three equal cards for anything; logo rows and partner badges; persistent chat and
cookie widgets in the fold; motion gated behind a system setting; arrows appended to
link text.
Token commitments: bg `#FFFFFF`, ink `#232323`, ink-soft `#495057`, plum `#624058`
(button, timeline dot), pink `#EC8AA3` (wordmark, timeline line), pink-tint `#FFE8EE`
(one band); `Outfit` 600 for every heading, `Inter` 400 for body at 20px; radius 24px on
cards and photos; the process timeline is a 2px line with 24px dots.
