# Production-test tells · gates 66–88, 97–99

**Load on every marketing, landing, or portfolio build.**

> Source: `design-taste-frontend` (Leonxlnx/taste-skill) v2, Section 9.F. Ported at full fidelity. These came out of real LLM-generated landing-page tests — they are the signatures a model reaches for when it tries to *look designed*. Blocks marked **[ours]** are this repo's framing.
>
> **97–98** arrive from two other upstreams (Anthropic `frontend-design`, Refero `color.md`) and carry numbers above the 89–96 block that [`gates.md`](gates.md) already spends. They are the same *kind* of finding as 66–88 — a small decoration or a missing declaration that survives every other gate — so they live here rather than in a third file.
>
> **99 [ours]** is Anton's 2026-09-19 standing ban on descriptive microtext (FEEDBACK.md F-016) — the next free number after 98, appended here for the same reason 97–98 were.

**[ours] Why these are separate from [`slop-test.md`](slop-test.md) gates 1–57.** Hallmark's set covers structural and visual slop (purple gradients, 3-column icon cards, centred hero, card-in-card). This set covers *micro-decoration* — the small labels, strips, dots, and captions a model sprinkles on to signal craft. They survive every other gate because individually each looks like a deliberate designer choice. Together they are the single most recognisable AI-page signature in production.

**Scope.** These are hard bans **by default**. Each is overridable when the brief explicitly calls for it — a genuine product-launch page may legitimately need a `BETA` label. The rule is that reaching for one *unprompted* is the failure.

---

## Hero and top-of-page

### 66 · Version labels in the hero
`V0.6`, `v2.0`, `BETA`, `INVITE-ONLY PREVIEW`, `EARLY ACCESS`, `ALPHA` as hero eyebrows. Banned as default. Acceptable only when the brief is explicitly about launch or preview status.

### 67 · "Brand · No. 01" sub-eyebrows
Micro-meta lines of the `Marrow · No. 01 · The 6-quart` shape. Skip them entirely.

### 68 · Decoration text strip at hero bottom
`BRAND. MOTION. SPATIAL.` · `TYPE / FORM / MOTION` · `DESIGN · BUILD · SHIP` · `ESTD. 2018 · LISBON` as a small mono-caps strip across the hero's base. Agency-portfolio cliché. Acceptable only when the strip carries real navigable links or real status info.

---

## Section labels and numbering

### 69 · Numbered eyebrows and range labels
`00 / INDEX`, `001 · Capabilities`, `06 · how it works`, `Index of Work, 2018 - 2026`. Eyebrows name the topic in plain language; they do not enumerate. Also covers `01 / 4`-style pagination on images and bento tiles — if the user can count, the label is noise.

Partially mechanical: impeccable's `numbered-section-labels` rule catches the common shapes.

### 70 · Micro-meta-sentences under eyebrows
A sentence like *"Each of these is a feature we ship today, not a roadmap promise."* sitting under a section heading. Eyebrow + headline + body is enough.

### 71 · Floating top-right sub-text in section headings
Giant left-aligned headline with a small explainer paragraph floating in the section header's top-right corner, aligned to nothing. Put the sub-text under the headline, or build a clean two-column header — not a corner floater.

### 72 · Generic step labels
`Stage 1 / Stage 2`, `Step 1 / Step 2`, `Phase 01 / Phase 02`, `Pass One / Pass Two`. The step's content is its label. If progression must show, use the verb directly (`Install`, `Configure`, `Ship`).

---

## Separators, dots, dashes

### 73 · Middle-dot as default separator
The `·` is rationed: **at most one per line** in a metadata strip. Not the default joiner for everything (`foo · bar · baz · qux`). Prefer line breaks, hairlines, or columns.

### 74 · Decorative status dots
A coloured dot before every nav link, list row, badge, or availability label. Zero by default. Acceptable only when the dot conveys real semantic state (live server status, a genuine availability flag), and then sparingly.

Partially mechanical: impeccable's `pulsing-dot` catches the animated variant.

### 75 · Em-dash, anywhere
**Zero tolerance.** `—` and separator-`–` are banned in headlines, eyebrows, pills, body copy, quotes, attribution, captions, button text, alt text. No "sparingly" allowance — that phrasing has been ignored in every prior round. Permitted dashes: the regular hyphen `-`, and the minus sign in maths.

Restructure instead: two sentences with a period, a comma, parentheses, or a colon. Quote attribution uses ` - ` or a line break.

**[ours]** This is the strictest form of a rule that appears in three places in this system: impeccable's `em-dash-overuse` detector rule (mechanical, threshold-based), `humanizer`'s style bans (in the copy gate), and here (zero-tolerance, visual). The zero-tolerance version wins.

---

## Typography flourishes

### 76 · `<br>`-broken and italicised headlines
`for thirty<br><em>years.</em>` as a default "design move". Headlines read naturally first; they get clever only when the brief demands it.

**[ours]** Distinct from gate 38a / `italic-serif-display`, which ban italic display type outright. This gate bans the *break-and-italicise* composition even where an italic is otherwise legal.

### 77 · Vertical rotated text
`INDEX OF WORK, 2018 - 2026` rotated 90°. Agency-portfolio cliché. Only for an explicitly experimental brief where it serves real composition.

### 78 · Crosshair and hairline grid decoration
Vertical and horizontal rules drawn purely to make the page feel designed. Use them only when they organise real content.

---

## Fake product surfaces

### 79 · Div-based fake product UI
Fake task lists, terminals, dashboards built from styled `<div>`s to simulate a screenshot. The single most reliable LLM-design tell. Use a real screenshot, a generated image, a real component preview, or nothing.

**[ours]** Overlaps gate 47 (re-drawn chrome) — 47 bans the *frame* (browser bar, phone bezel), 79 bans the fabricated *content* inside it. Both apply.

### 80 · Fake version footers
`v0.6.2-rc.1`, `last sync 4s ago · main` inside a fake screenshot, or as a real footer on a marketing page. Build metadata is devtool fixture content, not landing-page content.

### 81 · Live-stock counters as decoration
`Reservation 412 of 800`. Only when the brief is a genuine limited-run waitlist with real data.

---

## Imagery treatment

### 82 · Pills and labels overlaid on images
`<span>` overlays on photos reading `Brand · 02`, `PLATE · BRAND`, `Field notes - journal`. Either let the image stand alone or caption it directly below, outside the frame.

### 83 · Photo-credit captions as decoration
`Field study no. 12 · Ines Caetano`, `Plate 03 · House archive`, `Frame XII · 35mm` under stock or placeholder images. Photo credit is legitimate only when crediting a real photographer for a real photo. Otherwise skip it, or use one functional line.

---

## Copy tells

### 84 · Performative-craftsman labels and social proof
- `Quietly in use at` / `Quietly trusted by` → use `Trusted by`, `Used at`, or let the logos speak.
- `From the field` / `Field notes` / `Currently on the bench` / `On our desks` / `Loose plates` → use plain functional labels (`Testimonials`, `Latest writing`) or none.
- Mock-humble industry asides (`We respect the French ones`).

Partially mechanical: impeccable's `theater-slop-phrase` and `marketing-buzzword` catch some phrasings.

### 85 · Atmospheric locale, time, and weather strips
`LIS 14:23 · 18°C` in a nav, `Lisbon, working with founders` in a hero, `1200-690 Lisbon, Portugal` as a footer flourish. Allowed only for a genuinely timezone-distributed studio, a travel brand, or a real physical venue. A plain contact address in the footer is fine; an atmospheric strip is not.

---

## Lists and comparison visuals

### 86 · `border-t` + `border-b` on every row
A ten-row spec table with a hairline under each row is the laziest available layout. Pick one (bottom border between rows, or a top border above the group) and use it sparingly. For lists over five items, reach for a real UI component instead of `<ul>` + `divide-y`.

### 87 · Scoring bars with filled background tracks
`bg-zinc-200` tracks with a partial fill, used as a comparison visual on a marketing page. Dashboard clutter. Prefer a number plus a small icon, or a thin inline bar with no background track.

---

## Scroll cues

### 88 · Any scroll cue
`Scroll`, `↓ scroll`, `Scroll to explore`, `Scroll to walk through it`, animated mouse-wheel icons. If the visitor has not scrolled, they are looking at the hero — they know what scrolling is. The bottom of the viewport does not need a label.

---

## Chrome that appears whatever the subject

### 97 · `→` appended to link and button text

`Book a meeting →`, `Read more →`, `Get started →`, `Se caset →`. Upstream names it in
the same breath as the tracked-out eyebrow and the middle-dot meta string: *"template
chrome that appears whatever the subject … a '→' appended to link and button text"*
(`upstream/anthropic/frontend-design/SKILL.md`). The arrow is not the direction of
anything on the page; it is decoration that means *this is a link*, applied to text that
already is one.

Banned as default, on links, buttons, cards-as-links, nav items and CTA rows alike. The
arrow is permitted only when [`reference-lock.md`](reference-lock.md)'s decision ledger
carries a row for it — a named source that does it, and a reason specific to this brief.
Absent that row, the affordance is carried by a typeset underline, a real button, or the
label's own verb.

**[ours]** This is a sibling of gate 73 (middle dot as default joiner) and gate 84
(performative labels): each one is a small mark the model adds to signal craft. Two CTAs
on the same page both ending in `→` is the shape to look for first, because it proves the
arrow is a habit and not a decision.

### 98 · Dark ground with no `color-scheme` and no `theme-color`

A page whose canvas is dark (cinematic dark, illustrated dark, or any locked dark theme)
that never declares it to the browser. Refero states the consequence plainly: *"Without
`color-scheme: dark`, scrollbars stay light gray on dark backgrounds"*, form controls
`<input>` / `<select>` / `<textarea>` *"get wrong default colors"*, and *"System dialogs
and autofill appear broken"* (`upstream/refero/.../references/color.md`). The tell is a
pale scrollbar down the right edge of a black page, and a white native control the moment
the reader touches a field.

Required on every dark-canvas build:

```html
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#0f0f0f" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
```

```css
:root { color-scheme: light; }
[data-theme="dark"] { color-scheme: dark; }
```

A page locked to one theme declares that one value rather than the pair; `theme-color`
matches the page background it actually ships. Refero's own pre-ship list carries both as
checkboxes: *"`color-scheme` set on `<html>` for dark mode (fixes scrollbars, inputs)"*
and *"`<meta name="theme-color">` matches page background"*.

### 99 · Descriptive microtext

Small text set smaller than the page's body copy whose job is to describe or restate the
obvious rather than to identify, differentiate, locate, or enable an action — a kicker
naming what the section *is* (`EXEMPELCASE`, `SÅ GÅR DET TILL`), a figcaption naming what
a screenshot demonstrates (`Exempelsida: Hōrai, Asian fusion-koncept`), a side-rail list
of step headings in small grey type, or a line under a heading that just paraphrases it.
Banned outright, 2026-09-19 (Anton, FEEDBACK.md F-016), after live examples on the Alunix
demo pages.

**Full definition, the test, and the genre-apparatus exception:** [`anti-patterns.md` §
Descriptive microtext](anti-patterns.md). **Check:**
`skills/design/scripts/microtext_scan.py URL_OR_FILE` — flags visible text smaller than
the page's median `<p>` font-size that also looks like a kicker/eyebrow/caption/rail
(class name, uppercase-plus-tracking, or a short grey line beside a heading). Exit code
is non-zero on any finding; a finding is a candidate for a human/reviewer to judge against
the genre-apparatus exception, not an automatic fail. `--price-ledger` adds gate-adjacent
coverage for F-017 — a price column's text cell sized like its digit cells.

**[ours]** Sibling of gates 69, 70, 72, 82, and 83, which each ban one named shape of this
same failure; 99 is the general test that catches shapes those miss (a side-rail of step
titles, a paraphrase line under a heading with no eyebrow at all).

**[ours] Extended 2026-09-20 (FEEDBACK.md F-018): the same ban at body size.** A section
lede that narrates the section — what follows, in what order, why it exists — or that
disclaims the material before showing it, is the same failure typeset larger, and
`microtext_scan.py` cannot see it because it is not small. The scanner is a floor for the
small case only; the body-size case is caught by reading, and by the copy gate. Test: cut
the lede and read the section. If nothing is lost but a description of what the reader can
already see, it was filler, and a heading standing alone is the better setting.

**[ours]** Unlike the rest of this file, 98 is a *missing* declaration rather than an
added decoration. It earns its place here because the symptom reads identically to one:
browser chrome that does not belong to the design, appearing on every dark page a model
builds and on no dark page a designer ships.

---

## [ours] Mechanical coverage summary

| Gate | Mechanically caught by |
|---|---|
| 69 | `numbered-section-labels` (common shapes only) |
| 74 | `pulsing-dot` (animated variant only) |
| 75 | `em-dash-overuse` (threshold, not zero-tolerance) |
| 76 | `italic-serif-display` (display italic, not the break-composition) |
| 84 | `theater-slop-phrase`, `marketing-buzzword` (some phrasings) |
| 97 | not covered — grep the built page for `→` in anchor, button and CTA text |
| 98 | not covered — grep the built page for `color-scheme` and `theme-color` |

Everything else in 66–88 is model-enforced. Run this file as a checklist before emit; the pre-emit self-critique in the front door is where it binds.
