---
title: "What Matters (Agency)"
url: https://www.whatmattersagency.com
source_url: https://www.whatmattersagency.com
captured: 2026-09-04
origin: raw-url
raw: raw/4ebe6f8853825f81-www-whatmattersagency-com.webp
extract: ok
category: portfolio
category2: hospitality
family: overhead-feast-agency-poster
dna: "Overhead hospitality feast photography x condensed black poster claims"
register: warm photographic
grammar: typographic poster
lane: "A giant white condensed headline sits over an overhead photo of hands sharing a dessert, then the page drops to white for a client-logo wall and a black condensed manifesto statement with one photo wedged mid-sentence"
mode: persuade
traits: ["overhead candid dining photograph", "oversized condensed white headline", "yellow pill CTA in nav", "parenthetical qualifier in small caps", "client logo wall in native typography", "black condensed manifesto statement", "small photo wedged inside a headline", "outlined secondary CTA"]
palette: ["#FFFFFF", "#050505", "#FEF073", "#6C6B6A", "#5A92E7", "#312821"]
type: ["Denim Ink", "Neue Haas Display", "Inter"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The hero photograph — an overhead, candid shot of two people's hands sharing a plated
dessert at a dark restaurant table — is doing the same job EXAMPLE and Picnic use
elsewhere in this set: proving the agency's category (hospitality) before a single word is
read. The huge condensed white headline "WHAT MATTERS" sits directly on the photo with a
small parenthetical qualifier, "(AGENCY)", set at a fraction of the size beside it —
enough to clarify the wordmark is also the company name without diluting its scale as a
headline.

A single yellow pill CTA in the top-right nav is the only saturated colour on the entire
page; everything else is white, black, or drawn from the warm, dark-red tones of the food
photography itself. This restraint means the CTA is never competing with anything for
attention — there's exactly one coloured shape on the page at any time.

Below the fold, the page states its positioning as three short, stacked, ultra-bold
condensed lines ("CREATIVE-FIRST. HOSPITALITY FOCUSED. SYSTEMS ENABLED.") with a single
small photograph wedged directly into the gap between two lines via a bracketed
down-arrow — a smaller, quieter cousin of the wedged-photo device seen in the EXAMPLE
entry. Client logos, kept in each brand's own native typography, sit above this statement
as a plain, unstyled wall — proof arrives before the pitch is even fully stated.

## What to borrow (principle)

- **Let one candid, category-appropriate photograph state your specialism before your
  headline does.** An overhead hospitality photo says "we work in restaurants" faster
  than a sentence could.
- **Reserve your one accent colour for a single small UI element** (here, the nav CTA)
  when the rest of the page draws its warmth entirely from photography.
- **Wedge a small photograph into the gap of a stacked manifesto statement** rather than
  running it as a separate image block — it keeps the claim and its proof in one visual
  unit.
- **Show a client-logo wall in each brand's native typography, unstyled**, above your own
  positioning statement — proof precedes pitch.

## What to leave

- This entry's images are derived from the archived raw capture, not a fresh render — the
  live site returned HTTP 200 but did not complete the capture pipeline within budget, so
  treat exact copy and layout as approximate.
- The "(AGENCY)" qualifier's small size next to the massive headline risks being missed
  entirely on a quick scan — worth testing whether first-time visitors correctly parse the
  company name.
- Stacking three ultra-bold condensed manifesto lines at full viewport width with no
  supporting copy between them is a high-commitment device; it depends entirely on the
  three lines being genuinely differentiated claims, not filler.

## Signature move

The wedged manifesto photo: a single small photograph sits inside the vertical gap of a
three-line stacked bold statement, marked by a bracketed arrow, so the image reads as
supporting evidence for the middle claim specifically rather than a generic illustration
of the whole paragraph.

## Motion

Motion feel is mixed and the page is scroll-linked. Durations run a full micro-to-macro
ramp from a 20ms `instant` step up to a 420ms `lg` step. Easing is more varied than most
entries in this set: a standard decelerate curve (`ease-out`) handles light touches, a
"custom" family of three steep, front-loaded cubics (all control points stay within 0–1,
so none are true spring/overshoot curves, but they read as snappier than a plain ease)
carries the bulk of the transitions at 275 uses, and a plain `linear` covers continuous
motion. Keyframe use is narrow — only `translateXCursor`, a horizontal slide to -100%,
consistent with a custom cursor-follow or marquee element; a `spin` (360° rotation) exists
in the stylesheet but isn't logged as in-use. The raw transitions do show one explicit
choreography pattern: seven `transform 0.5s` rules share the same custom cubic-bezier but
each adds an incremental 0.02s delay (0.02s → 0.14s), a classic staggered-reveal for a list
of items entering in sequence (from designlang extract).

| kind | name/family | value |
|---|---|---|
| duration | `instant` | 20ms |
| duration | `xs` | 100ms |
| duration | `sm` | 160ms |
| duration | `md` | 260ms |
| duration | `lg` | 420ms |
| easing | ease-out | `cubic-bezier(0.165, 0.84, 0.44, 1)` |
| easing | custom | `cubic-bezier(0.625, 0.05, 0, 1)` |
| easing | custom | `cubic-bezier(0.75, 0, 0.25, 1)` |
| easing | custom | `cubic-bezier(0.625, 0.5, 0, 1)` |
| easing | ease-in-out | `ease` |
| easing | linear | `linear` |

## Brief

Build a hospitality-focused content/creative-agency landing page opening on one full-
bleed, candid overhead photograph of shared dining (hands, food, a set table) with a
massive condensed white headline set directly on the photo, paired with a small
parenthetical qualifier clarifying the company type. Reserve one saturated accent colour
for a single small CTA element only. Below the fold, show a client-logo wall in each
brand's own native typography, unstyled and ungridded beyond simple horizontal spacing.
Follow with the agency's positioning stated as three short, stacked, ultra-bold condensed
lines at large scale, with one small supporting photograph wedged into the gap between two
of the lines via a simple bracketed arrow mark.

## Image recipe

Overhead candid photograph of [SUBJECT] — a shared restaurant meal, hands reaching for
food, a plated dessert or dish — shot from directly above, warm ambient restaurant
lighting (candlelight, low warm bulbs), true-to-life saturated warm tones, genuine motion
and gesture (cutlery mid-use, hands overlapping), no studio food-photography lighting.

## Photo search

Unsplash first, Pexels second.
- "overhead restaurant table hands sharing food"
- "candid dining hands dessert warm light"
- "bartender at work restaurant candid"
- "restaurant table overhead ambient lighting"

## Reference lock

Primary reference/direction: What Matters (Agency) — overhead dining photo hero with a
massive condensed headline, black manifesto statement with a wedged photo.
Preserve (3-5 traits): one full-bleed candid overhead hospitality photograph carrying a
massive condensed white headline with a small parenthetical qualifier; exactly one
saturated accent colour, reserved for a single small CTA; a client-logo wall shown in
each brand's native typography, unstyled; a stacked, ultra-bold condensed manifesto
statement with one small photo wedged into its gap via a simple arrow mark.
Borrow only (1-2): the outlined secondary CTA style ("LEARN ABOUT US"); the small
bracketed down-arrow as a wedge-photo marker.
Role rules: the accent colour never appears on more than one element per screen; the
manifesto statement's stacked lines stay condensed and bold, never mixed with a lighter
weight; client logos are never normalised to one typeface.
Media strategy: photo:unsplash — warm, candid, overhead hospitality/dining photography
with genuine ambient restaurant lighting; never a staged, evenly-lit food-styling shot.
Reject: a second accent colour; a normalised (single-typeface) client-logo wall; a
manifesto statement broken into more than three lines; illustrated or iconographic
substitutes for the wedged photo.
Token commitments: bg `#FFFFFF`, hero-warm-dark `#301414`, warm-mid `#8D5A43`, warm-tan
`#AE836A`, ink-warm `#60544B`, stone `#C9C3BA`; condensed bold grotesque for headlines and
manifesto lines, plain sans for nav/body/captions; one accent colour reserved for the
primary nav CTA only.
