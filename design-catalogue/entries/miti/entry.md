---
title: "Miti Navi"
url: https://miti-navi.com/fr
source_url: https://miti-navi.com/fr
captured: 2026-09-04
origin: refero
extract: ok
category: luxury-craft
category2: "hospitality"
family: linen-arch-chapbook
dna: "Cathedral-arch yacht photography x monospaced editorial UI on unbleached linen"
register: warm photographic
grammar: gallery/catalog
lane: "A sand-linen page holds a full-bleed yacht photograph masked by a cathedral-arch clip-path beneath a three-cluster nav, with an oversized 180px serif headline and a persistent rotated side tab — every functional element rendered in a monospaced type that never once softens a corner"
mode: experience
traits: ["arch-masked hero, the sole soft shape on the page", "0px radius everywhere else, rigorously square", "one apricot underline, no filled buttons at all", "monospace for every UI role, serif for display only", "dark image-inset frames as prints behind glass", "rotated vertical side-tab as a persistent margin marker"]
palette: ["#e6dece", "#000e13", "#232323", "#999999", "#ffdead"]
type: ["Voyage", "GT Pressura Mono", "GTSectraDisplay"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/miti.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the
live capture. Linen `#e6dece` is not merely a background but the site's only
surface — cards, canvas and content blocks share the exact same value, so
nothing "lifts" off the page; the source states white or light-gray tints
are never introduced anywhere. Deep ink `#000e13` reserves itself for dark
photographic insets that function as "prints mounted behind glass," giving
the palette exactly two roles: warm paper, and the occasional dark window
into deeper space.

The typography inverts the usual mono/serif hierarchy seen elsewhere in this
catalogue: GT Pressura Mono, not a humanist sans, runs the entire functional
interface — nav, body, links, buttons — with tracking that widens
proportionally as size grows (0.71px at 10px up to 1.6px at 16px), giving
even body paragraphs a technical, spaced-out cadence. Voyage, a theatrical
high-contrast serif, is reserved exclusively for display at 46-180px and
banned below 46px, so the romantic curves of the brand voice never dilute
into small text.

Geometry stays absolutely square (0px radius on every card, tag, image and
button) with exactly one exception: the hero photograph itself, masked by a
custom arch clip-path that creates a cathedral-window silhouette. Because
that curve is the only soft shape anywhere on the site, it reads as a
genuine architectural gesture rather than a stylistic default — reinforced
by a system with no filled buttons at all, where every action is a plain
mono link marked only by a 1px apricot underline offset below the text.

## What to borrow (principle)

- **Let type tracking widen proportionally with size, not shrink.** GT
  Pressura Mono's 0.71px-to-1.6px curve keeps every size feeling
  consistently "spaced," rather than tight at large sizes and loose at
  small ones.
- **Reserve exactly one soft shape for one specific purpose.** A single
  arch clip-path on the hero photograph, with 0px radius everywhere else,
  makes that one curve read as an architectural signature, not decoration.
- **Run the entire functional UI in a monospace face.** Using mono for body
  copy as well as nav and buttons — not just for code or labels — gives an
  editorial site an unexpectedly technical, precise register.
- **Replace filled buttons with a single underline convention.** One
  1px accent-colour rule, offset below the text, as the system's only CTA
  style removes the temptation to invent multiple button treatments.
- **Frame dark photography in a dark inset, not a light card.** Setting
  secondary images inside a `#000e13` filled block (rather than the linen
  canvas) makes them read as windows or framed prints, adding weight where
  the flat linen system needs it.

## What to leave

- Zero filled buttons anywhere is a hard commercial constraint — a booking
  or contact flow needing a genuinely prominent action has no built-in
  pattern beyond an underlined link.
- The custom arch clip-path hero is a bespoke asset requiring careful
  responsive handling; a naive rebuild risks either losing the cathedral
  silhouette or clipping photography awkwardly at narrow viewports.
- Running body copy in a monospace face at 14px with 1.4px tracking is a
  legibility trade-off some readers find harder to scan at length than a
  humanist sans — appropriate for a low-text, photography-led site but risky
  for a copy-dense one.

## Signature move

The arched hero mask: a full-bleed yacht photograph clipped by a tall,
custom cathedral-window silhouette against the linen canvas — the single
soft, curved shape on an otherwise rigorously square-edged site.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked —
correcting the earlier "no motion tokens" read: shadowlessness and motion turn
out to be separate design decisions here. A single custom curve,
`cubic-bezier(0.82, 0, 0.36, 1)`, is used with striking consistency (102
uses) across four durations, from a quick 200ms up to a slow 1.6s — a
late-accelerating "held, then release" shape fitting for measured, editorial
reveals rather than snappy UI feedback. No keyframes are confirmed firing, so
this choreography lives entirely in property transitions. (observed in
capture) the live capture confirms the arch-masked hero and split
three-cluster navigation are present and match the structure closely; given
the flat, shadowless, printed-catalog register, interaction states most
plausibly still apply the documented apricot underline to active links,
riding that same custom curve rather than adding elevation.

| Token | Value | Easing |
|---|---|---|
| sm | 200ms | `cubic-bezier(0.82, 0, 0.36, 1)` |
| lg | 600ms | `cubic-bezier(0.82, 0, 0.36, 1)` |
| xl | 1s | `cubic-bezier(0.82, 0, 0.36, 1)` |
| xxl | 1.6s | `cubic-bezier(0.82, 0, 0.36, 1)` |

## Brief

Build a luxury yacht-builder site on a warm, editorial paper canvas. Set
linen `#e6dece` as the only surface colour across the entire site — no
white, no light gray, ever. Deep ink `#000e13` is reserved for dark
photographic insets only. Cap every card, image, tag and button at 0px
radius without exception. Run GT Pressura Mono for all functional text —
nav, body, links, buttons — with tracking widening from 0.71px at 10px to
1.6px at 16px; reserve Voyage, a theatrical serif, exclusively for display
headlines at 46-180px, never smaller. Open with a split three-cluster nav
(left links, centred wordmark, right links, no background) beneath a
full-bleed hero photograph masked by a custom arch clip-path — the only
curved shape on the page. Mark every interactive element with a single
1px apricot `#ffdead` underline offset below the text; no filled or
outlined buttons exist. Pin a narrow vertical side tab with rotated
uppercase text to the right viewport edge. Set secondary photography inside
dark `#000e13` inset frames, like prints behind glass. Keep 60px section
gaps and generous 30-60px outer gutters; no shadows anywhere.

## Image recipe

Documentary-naturalistic photograph of [SUBJECT] — a sailing yacht on open
water shot from astern or three-quarter angle, high-key natural daylight
with no colour grading beyond natural blue water and sky, coastline visible
in the background, no studio staging, presented full-bleed and masked by an
arch silhouette at the top edge for hero use, or set inside a dark inset
frame for secondary editorial use.

## Photo search

Unsplash first, Pexels second.
- "sailing yacht open water aerial astern"
- "sailboat mediterranean coastline natural light"
- "yacht deck teak detail natural light"
- "sailing vessel wake ocean documentary"

## Reference lock

Primary reference/direction: Miti Navi — linen-paper yacht chapbook, arch-
masked hero, monospaced editorial UI with a single apricot underline accent.
Preserve (3-5 traits): linen `#e6dece` as the site's only surface colour, no
white or light-gray tint anywhere; 0px radius on every element except the
one arch-masked hero photograph; GT Pressura Mono for all functional text
with tracking widening at larger sizes; Voyage reserved for display only
(46-180px), never below 46px; no filled buttons — every action is a plain
mono link with a single 1px apricot underline.
Borrow only (1-2): the arch clip-path hero mask; the rotated vertical
side-tab margin marker.
Role rules: apricot never becomes a fill or a large surface; Voyage never
sets body copy, nav or buttons; dark `#000e13` insets are reserved for
photography, never for text-only cards.
Media strategy: photo:unsplash — documentary-naturalistic yacht and coastal
photography, high-key natural light, no studio staging; no illustration.
Reject: any filled or outlined (non-underline) button; border-radius on any
element outside the hero arch; box-shadow or elevation; white or light-gray
surfaces; Voyage below 46px.
Token commitments: bg/card `#e6dece`, image-inset `#000e13`, ink `#232323`,
muted `#999999`, accent `#ffdead`, hard-black `#000000`; display Voyage 400
at 46-180px/leading 0.90-0.94; body GT Pressura Mono 400 at 10-16px/leading
1.4/0.71-1.6px tracking; radius 0px universal; page max-width 1200px,
section gap 60px.
