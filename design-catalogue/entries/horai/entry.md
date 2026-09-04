---
title: "Hōrai"
url: file:///C:/Users/Anton%20L/anti-slop-design/sites/horai.html
captured: 2026-09-03
family: lacquer-house
dna: "Kaiseki menu card x Roman inscriptional caps"
register: cinematic dark
grammar: chaptered editorial
lane: "Full-bleed dining photograph, then alternating cream menu leaves and near-black lacquer chapter panels, each menu a ruled row with a Roman numeral and a price, closing on a dark reservations spread"
mode: persuade
traits: ["alternating cream/lacquer panels", "Cinzel inscriptional caps", "Vollkorn body serif", "kanji section marks", "lacquer red accent", "Roman-numeral menu rows", "SEK prices set large", "word-by-word lede reveal", "fixed multiply grain"]
palette: ["#F8F1E8", "#F1E6D7", "#E5D9C8", "#241713", "#3D2F2B", "#77706B", "#A9000F", "#720000", "#2A5745"]
type: ["Cinzel", "Vollkorn", "Noto Serif JP"]
kind: example
source: claude
origin: example-site
extract: none
category: hospitality
category2: "editorial"
status: ready
---

## Why it works

The page is built as a restaurant's own printed matter: a cream menu leaf, then a
black lacquer card, then a cream leaf again. The alternation does the chaptering,
so the page needs no navigation and no scroll cues — you always know whether you
are reading the house talking (cream) or the house posing (lacquer).

Three typefaces, three jobs, no overlap. Cinzel — an inscriptional Roman capital —
is used only for names, numerals and prices, never for a sentence. Vollkorn sets
every sentence and nothing else. Noto Serif JP carries a single kanji per section
(家 house, 献 menus, 予約 reservations) as a section mark, not as decoration. The
kanji is the only thing on the page allowed to be purely graphic, and it earns it
by being the section's index.

Prices are the loudest type on the page. `1,480` and `2,180` are set in Cinzel at
display size in lacquer red with `SEK · PER GUEST` in tracked caps underneath. A
tasting-menu restaurant that hides its price loses the guest at the door; this one
makes the number the visual reward at the end of each row.

Restraint in the accent is what keeps it expensive-looking. Lacquer red `#A9000F`
appears on kanji, section titles, prices and one URL — perhaps eight elements on a
page of this length. Everything else is warm ink on warm paper, or cream on
near-black. There is no second accent and no gradient anywhere.

The menu rows are honest three-part records: numeral and name at the left, spec
line in tracked caps beneath (`世界 · NINE COURSES · THE HOUSE MENU`), service days
at the bottom, price at the right, hairline rule between rows. It reads as a card
you could hand to a guest, which is the point.

## What to borrow (principle)

- **Let alternating grounds do the chaptering.** Cream leaf / dark panel, repeated,
  replaces section headers, dividers and a nav bar all at once.
- **One face per job, enforced.** Inscriptional caps for names and numbers, a
  bookish serif for sentences, a third face for exactly one glyph per section. Never
  let the caps face set a sentence.
- **Set the price at display size.** The number, in the accent colour, with the
  currency and unit in small tracked caps beneath it, is the strongest close on the
  page.
- **One glyph as section index.** A single kanji (or any non-Latin mark) above each
  section title indexes the page memorably without a numbering system.
- **Cap the accent at a handful of elements.** One red, used on kanji, titles,
  prices and one link — nothing else gets colour.

## What to leave

- The fixed `mix-blend-mode: multiply` grain at 0.42 opacity — a full-screen
  composited layer for a texture that mostly just mutes the food photography, which
  is the one thing a restaurant page must keep appetising.
- Hero body copy set directly on the busy photograph at the right edge. In the
  capture it is unreadable — the plate behind it is bright and there is no scrim.
  Text over food photography needs a plate or a gradient, always.
- The blanket `document.querySelectorAll('article, figure, h2, h3')` reveal at 1.3s.
  In the middle of a long menu list it means half the rows are still faded when the
  reader arrives at them.
- The word-by-word lede fade (`.word { opacity: 0.18 }`). It is charming for one
  paragraph and it means that paragraph is unreadable for the first second — use it
  on the lede only, and never on anything a reader might scroll back to.

## Signature move

The menu row as a ledger line: Roman numeral · romanised name in inscriptional
caps · kanji and course count in tracked micro-caps · a paragraph of what the menu
actually is · service days · and the price alone at the far right in red at display
size, with a hairline rule closing the row. Three registers of type in one row,
each doing exactly one job, and the number winning.

## Brief

Build a dark-and-cream restaurant page that alternates full-width cream paper
leaves (`#F1E6D7`) with near-black lacquer panels (`#241713`), one alternation per
chapter, no nav beyond a fixed wordmark and a single outlined RESERVATIONS button.
Open on a full-bleed documentary photograph of a dining room with the restaurant
name set into it in cream inscriptional caps at ~14vw. Set all names, numerals and
prices in Cinzel with 0.03–0.06em tracking; set all sentences in Vollkorn at
1.15rem/1.75; put one kanji per section in Noto Serif JP above the section title.
Use exactly one accent, a lacquer red `#A9000F`, on kanji, section titles, prices
and one URL. Build the menu as ruled rows: Roman numeral, name, tracked micro-caps
spec line, description, service days, and the SEK price at the right at display
size in red. Close on a dark reservations spread split by a vertical hairline, with
the address in cream caps and a footer line that names the typefaces.

## Image recipe

Documentary interior and plate photography of [SUBJECT], shot available-light on
35mm, warm tungsten and candle sources, shallow depth of field, one plane crisp,
deep unlit background falling to near-black, muted warm colour with cream
highlights and no colour-cast correction, taken from a guest's seated eye level —
never overhead, never on white, no styling props, no strobe.

## Photo search

Unsplash first, Pexels second.
- "restaurant dining room candlelight documentary"
- "plated tasting menu dish natural light dark"
- "chef counter service warm interior"
- "izakaya interior wood slats evening"

## Reference lock

Primary reference/direction: Hōrai — alternating cream-leaf and lacquer-panel restaurant page, Cinzel + Vollkorn + one kanji, price set at display size.
Preserve (3-5 traits): alternation of cream `#F1E6D7` leaves and near-black `#241713` lacquer panels as the only chaptering device; Cinzel for names/numerals/prices and Vollkorn for all sentences, never crossed; one kanji per section as its index mark; menu rows as ruled ledger lines ending in a large red SEK price; lacquer red `#A9000F` as the only accent.
Borrow only (1-2): the full-bleed photographic overture with the name set into it; the footer line that names the typefaces.
Role rules: Cinzel never sets a sentence; Vollkorn never sets a label or a price; kanji appears once per section and never inside body copy; accent red on at most eight elements per page; tracked micro-caps capped at 11px and 0.18em.
Media strategy: photo:unsplash — available-light documentary interiors and plates, always captioned with menu and course number; never a bright white-background food shot.
Reject: fixed grain overlays; unscrimmed text over food photography; blanket scroll reveals on list rows; a second accent colour; any sans-serif; gradients.
Token commitments: paper `#F8F1E8`, paper-warm `#F1E6D7`, paper-deep `#E5D9C8`, lacquer `#241713`, lacquer-soft `#3D2F2B`, stone `#77706B`, red `#A9000F`, red-deep `#720000`, jade `#2A5745`; display `Cinzel`, body `Vollkorn`, mark `Noto Serif JP`; display tracking 0.03–0.06em, micro-caps tracking 0.18em, body 1.15rem/1.75.
