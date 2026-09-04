---
title: "Amrit Palace"
url: https://amritpalace.com
source_url: https://amritpalace.com
captured: 2026-09-04
origin: refero
extract: ok
category: hospitality
category2: editorial
family: candlelit-parchment-menu
dna: "Fine-dining candlelight photography x whisper-weight serif editorial"
register: warm photographic
grammar: chaptered editorial
lane: "A dark, candlelit dining-room photograph carries a whisper-thin serif headline, then the page drops onto a warm parchment canvas of sharp-cornered, hairline-ruled editorial sections with a single saffron accent and a scrolling marquee of signature dishes"
mode: persuade
traits: ["115px weight-300 serif display", "0px radius everywhere except 3px buttons", "warm parchment canvas, no white", "single saffron accent, 2-3 uses per fold", "dark full-bleed candlelight photography", "hairline column-rule dividers", "27s linear dish marquee"]
palette: ["#d8cbb8", "#bfb4a3", "#b6ab9c", "#2c2c2c", "#292622", "#d49653"]
type: ["TT Ramillas Variable", "Satoshi"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Amrit Palace.md
raw: raw/c52b1d72d1cd4bd5-amritpalace-com.webp
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Warm parchment `#d8cbb8` replaces white as the base canvas everywhere, and
warm onyx `#2c2c2c` replaces pure black as the ink — the whole page runs a few
degrees warmer than a typical editorial site, which is what makes candlelit
photography feel continuous with the UI rather than pasted onto it. Saffron
`#d49653` is the one chromatic note, rationed to star ratings and one or two
decorative moments per fold; everything else in the system is a warm neutral.

Type performs a duet the md calls out explicitly: TT Ramillas Variable at weight
300 sings the display voice at extreme sizes (up to 115px, always uppercase, always
weight 300 — never bolded), while Satoshi at weight 500 handles every functional
line — nav, buttons, captions, the 199px hero wordmark. The serif never drops below
22px and the sans never exceeds 42px outside that one wordmark exception, so the
two faces never compete at the same size class.

Geometry reinforces the restraint: 0px radius on every card and section, 3px only
on buttons and tags, no shadows anywhere. Depth comes from tonal steps (parchment →
linen → walnut) and 1px hairline rules that behave like column rules in a printed
menu, not from elevation. Photography does the atmospheric work instead — full-
bleed, dark, candlelit table shots bookend the page before it opens onto the flat
parchment editorial spread.

## What to borrow (principle)

- **Warm every neutral by a few degrees.** Replacing white and black with parchment
  and warm onyx makes candlelit or golden-hour photography feel native to the page.
- **Ration the accent color to a literal count.** "No more than 2-3 times per fold"
  is a concrete, checkable rule that keeps a single accent from creeping into
  decoration.
- **Split radius into exactly two values.** 0px for structure, one small radius for
  interactive controls — nothing in between reads as decisive rather than fussy.
- **Use hairlines as column rules, not decoration.** A 1px divider that behaves like
  a typographic element (full-width, no padding logic) reads as editorial, not as
  UI chrome.
- **Reserve one motion device.** A single scrolling marquee, used once, gives the
  page its only kinetic personality without turning motion into wallpaper.

## What to leave

- Zero border-radius on every card is a hard commitment — any component borrowed
  from a softer system (rounded chips, pill tags) will visibly clash.
- The 115px uppercase serif headline needs real display weight in the chosen
  typeface; a serif without a genuine weight-300 cut will look thin and broken,
  not intentional.
- Full-bleed dark photography before any parchment content means the fold has no
  UI signifiers at all beyond the headline — risky outside a category where
  atmosphere alone is expected to sell the product.

## Signature move

The horizontal marquee of signature dish names, scrolling continuously at 27s
linear — the only extended motion the system permits, deployed once, and reserved
specifically for the menu's signature items rather than for generic content.

## Motion

(from designlang extract) Feel reads as responsive, and the page is scroll-linked —
content resolves relative to scroll position rather than firing purely on load.
Interactive transitions run on a single ease-out family, `cubic-bezier(0.25, 0.46,
0.45, 0.94)`, at two durations: a 350ms step for smaller state changes and 450ms for
larger reveals; the extract's broader transition log adds a 400ms variant on the
same curve, matching the 0.4s figure the Refero export's Motion Philosophy states
directly. The one keyframe confirmed in use is `marquee`, a slide-x transform
driving the horizontal scrolling dish-name band — the extract also carries a
video-player's own spin/fade/popup keyframes (from the embedded Plyr player), which
are library chrome, not page design. (observed in capture) the live capture
confirms a flat, non-parallax scroll: sections resolve as static parchment panels
beneath the dark hero, consistent with "turning pages of a printed menu, not a web
app."

| Token | Value | Easing |
|---|---|---|
| md (state change) | 350ms | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` |
| lg (reveal) | 450ms | `cubic-bezier(0.25, 0.46, 0.45, 0.94)` |
| marquee (signature) | 27s linear | `linear` |

## Brief

Build a fine-dining restaurant page. Canvas is warm parchment `#d8cbb8`, stepping to
linen `#bfb4a3` for secondary tone and warm onyx `#2c2c2c` / midnight `#292622` for
dark surfaces; saffron `#d49653` is the sole accent, used only for star ratings and
one or two decorative marks per screen. Open full-bleed on a dark, candlelit dining
photograph with a floating transparent nav and a TT Ramillas weight-300 uppercase
headline at up to 115px, flanked by small Satoshi meta labels ("Serving ___",
"Established ___"). Drop to the parchment canvas for editorial content: 0px-radius
sections divided by 1px hairline rules, generous 120-160px gaps, left-aligned copy
in Satoshi 500 at 14-15px. Use ghost-outlined buttons only (1px border, 3px radius,
uppercase Satoshi label) — no filled chromatic buttons. Include a testimonial row on
the parchment canvas and a horizontally scrolling marquee of signature dish names as
the one kinetic moment. Transitions run 0.4s ease.

## Image recipe

Documentary interior photograph of [SUBJECT] — a candlelit fine-dining table set
with glassware and linen, shot at table height with shallow depth of field, warm
amber practical lighting only (no flash, no cool fill), rich wood and copper tones
in the background falling into soft shadow, natural imperfection in the flame and
reflections retained, no styled overhead flat-lay.

## Photo search

Unsplash first, Pexels second.
- "candlelit restaurant table setting warm light"
- "fine dining interior moody amber light"
- "table setting glassware candle close up"
- "Indian cuisine plated dish dark background"

## Reference lock

Primary reference/direction: Amrit Palace — candlelit fine-dining hero into a warm
parchment editorial menu, whisper-weight uppercase serif display.
Preserve (3-5 traits): parchment `#d8cbb8` canvas with warm onyx `#2c2c2c` ink, no
pure white or black anywhere; TT Ramillas weight 300 uppercase for all display,
never bolded; 0px radius on every card/section, 3px only on buttons and tags; 1px
hairline dividers used as column rules; saffron `#d49653` rationed to 2-3 uses per
fold, reserved for ratings and single decorative marks.
Borrow only (1-2): the 199px Satoshi hero wordmark exception; the 27s linear dish
marquee.
Role rules: serif never appears below 22px, sans never exceeds 42px outside the
hero wordmark; no filled chromatic buttons, ghost/outline only; no shadows, no
gradients; body text left-aligned only, never centred.
Media strategy: photo:unsplash — dark, candlelit, table-height interior and dish
photography only; no illustration, no stock lifestyle smiling-diner shots.
Reject: rounded cards; a second accent colour; bold serif headings; centred body
copy; parallax or scroll-triggered reveals beyond the single marquee.
Token commitments: bg `#d8cbb8`, tone-1 `#bfb4a3`, hairline `#b6ab9c`, ink `#2c2c2c`,
ink-deep `#292622`, accent `#d49653`; display weight 300, uppercase, tracking
-0.03 to -0.04em, leading 0.8-0.9; body Satoshi 500 14-15px; radius 0px default, 3px
interactive; transitions 0.4s ease / cubic-bezier(0.25,0.46,0.45,0.94); page
max-width 1440px, section gap 120-160px.
