---
title: "Picnic"
url: https://trypicnic.com
source_url: https://trypicnic.com
captured: 2026-09-04
origin: raw-url
raw: raw/191d835149f44b93-trypicnic-com.webp
extract: ok
category: product-focused
category2: consumer-brand
family: checkered-lunch-hero
dna: "Office-delivery SaaS x checkered picnic-blanket food photography"
register: warm photographic
grammar: split stage
lane: "One full-bleed overhead picnic-spread photo carries the whole hero with a serif claim and orange italic accent word, then the page drops to a plain cream ledger of logos and numbered solutions"
mode: persuade
traits: ["full-bleed overhead food photo hero", "serif display with italic accent word", "single orange accent", "logo wall of restaurant brands", "numbered solution list with hairline rules", "circular video-still callout", "cream ledger below fold", "sticky orange sign-up card"]
palette: ["#F7F6F2", "#F74C24", "#6D3E25", "#E5D3CA", "#52170D", "#EA8D71"]
type: ["P22 Mackinac Pro", "Inter", "Inter Display"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero is carried entirely by one photograph — an overhead, warm-lit picnic-blanket
spread of pizza, strawberries and drinks — with white and orange serif type set directly
onto it. The headline mixes roman and italic within one sentence ("50+ restaurants
delivered to your **office**"), and the italic word is the only one carrying the brand's
orange, so the accent colour and the emphasis device are the same move: colour marks the
one word the sentence turns on.

Below the fold the page changes register completely, from photographic warmth to a plain
cream ledger: a restaurant logo wall in mixed display faces (each brand keeps its own
identity), then a numbered list of business solutions separated by hairline rules, each
with an orange kicker and a "Learn more" link. The restraint here is what makes the hero
photo feel earned rather than decorative — the page proves the claim (50+ real restaurant
brands) immediately after making it, in the same orange the hero used for emphasis.

A circular, cropped video-still sits beside the solutions list rather than another
rectangular card, breaking the grid just enough to read as a genuine interruption (a
"how it works" moment) without introducing a new colour or typeface. The whole page runs
on exactly two registers — photographic hero, ruled ledger — and one accent colour moves
between both.

The copy voice makes the same move from broad to specific as the layout: it opens in "we"
framing for the company's claims, then shifts to direct "you" address at the point of
conversion, mirroring how the page moves from a shared hero photo to a personal CTA (from
designlang extract).

## What to borrow (principle)

- **Mix roman and italic within one headline sentence and let the italic carry the
  accent colour.** Emphasis and colour become the same signal instead of two competing
  ones.
- **Follow a photographic hero immediately with proof in the same accent colour.** A logo
  wall or number, coloured to match the hero's one accent, reads as continuation, not a
  new section.
- **Use a circular crop to break a rectangular grid once.** One non-rectangular element
  (a video still, a photo) reads as an intentional pause, not inconsistency, if it's the
  only one.
- **Let each partner logo keep its own type and colour in a wall.** It signals real
  variety of real brands rather than a homogenised "as seen in" strip.

## What to leave

- The sticky orange sign-up card overlapping the hero's bottom-right corner (both
  captures) crops into the photograph and competes with the primary CTA in the centre —
  worth demoting to a scroll-triggered or footer placement.
- Hairline rules under each numbered solution are the same weight as the section's other
  rules, so the numbered list doesn't visually separate from surrounding content at a
  glance; a slightly heavier rule or indent would help.
- The "Order" vs "Request Picnic" button pair uses the same orange for one filled and one
  outlined button — close enough in weight that the primary action isn't obviously
  primary.

## Signature move

The italic accent word inside a mixed-case serif headline, set in the brand's one orange
directly over the hero photograph — emphasis, colour and voice collapse into a single
typographic gesture instead of three separate decisions.

## Motion

Feel reads as smooth rather than mixed — the most cohesive rhythm of this batch — and the
page is scroll-linked. Durations run a clean short-to-long ladder, 140/180/300/500ms,
mostly riding a standard `ease-out` deceleration with a `linear` curve reserved for a
handful of transitions; no spring or overshoot curves appear anywhere. The curated keyframe
list shows two structural moves repeated across the page: an `enter` opacity fade (a
per-section reveal on scroll) and an eight-times-repeated `scroll` slide-x transform, almost
certainly the auto-scrolling restaurant logo wall described in Why it works. The fuller
keyframe set adds bespoke touches beyond that summary: a `pd-font-pulse` scale-up-and-back
on a small chip or badge (desktop and mobile variants), a generic opacity `pulse`, a
`splat-fade-out` for a decorative graphic, and a `nav-modal-enter`/`nav-modal-exit` pair
that wipes the mobile nav in and out via `clip-path` inset from the right edge rather than a
simple fade or slide — the circular video-still's play affordance itself carries no
recorded keyframe, so its click behaviour stays unconfirmed. (from designlang extract)

| token | value | used for |
|---|---|---|
| xs | 140ms | fastest hover/colour transitions |
| sm | 180ms | transform hovers |
| md | 300ms | mid-length transitions |
| lg | 500ms | slower transform moves |
| ease-out | `ease-out` | most transitions (91 uses) |
| linear | `linear` | a subset of transitions (27 uses) |

## Brief

Build an office-food-delivery landing page anchored on one full-bleed, warm overhead
photograph of a real food spread. Set the headline in a serif that mixes roman and italic
within one sentence, with the italic word carrying the single brand accent colour (a warm
orange-red) directly over the photo in white/orange type. Below the fold, drop to a plain
cream ledger: a restaurant-logo wall (each logo keeps its own typeface), then a numbered,
hairline-ruled list of business solutions with orange kickers and "Learn more" links.
Break the rectangular grid once with a circular photo or video-still element beside the
list. Keep the accent orange consistent between hero italic, kickers and primary buttons;
introduce no second accent colour anywhere on the page.

## Image recipe

Overhead documentary photograph of [SUBJECT] — a shared meal, a checkered picnic spread,
office lunch containers — shot from directly above, warm natural or warm artificial light,
saturated true-to-life food colour, some motion (hands reaching, chopsticks mid-bite),
checkered or textured linen visible at the edges, no studio product-shot lighting.

## Photo search

Unsplash first, Pexels second.
- "overhead picnic spread checkered blanket"
- "office lunch shared meal overhead"
- "pizza box strawberries flatlay warm light"
- "coworkers eating lunch together overhead"

## Reference lock

Primary reference/direction: Picnic — full-bleed overhead food-photo hero with a mixed
roman/italic serif headline, cream ledger of proof below.
Preserve (3-5 traits): one full-bleed warm overhead food photograph carrying the entire
hero; headline mixing roman and italic in one sentence, italic word carrying the sole
accent colour; a real-brand logo wall immediately below the hero as proof; numbered,
hairline-ruled solution list with orange kickers; exactly one accent colour used
everywhere (hero italic, kickers, buttons).
Borrow only (1-2): the circular crop for the video-still/how-it-works element; the pill-
shaped location/order search bar over the hero photo.
Role rules: italic serif is reserved for the one emphasis word per headline, never used
for body copy; orange never appears twice as both a filled and outlined button without
clear weight difference; logo wall entries keep native brand typography, never
normalised to one face.
Media strategy: photo:unsplash — warm, saturated, overhead real-food photography with
visible human presence (hands, motion); never a sterile product-only flatlay.
Reject: a second accent colour; centred, static (non-mixed-style) headlines; card
shadows or rounded rectangles in the ledger section; a logo wall normalised to one
typeface.
Token commitments: bg `#F7F6F2`, accent `#F74C24`, accent-soft `#EA8D71`, ink-warm
`#6D3E25`, ink-deep `#52170D`, tint `#E5D3CA`; display `P22 Mackinac Pro` (hero serif),
body/UI `Inter` / `Inter Display`; headline mixes roman and italic in one line, body and
labels stay upright; hairline rules at consistent weight throughout the ledger.
