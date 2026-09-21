# Typography

> **Diverges from upstream Hallmark: T6 port (2026-09-09).** This file has been
> extended with material ported from the upstream packages named in the design
> chain's v4 plan, sections 2.1 to 2.5. Every addition is traceable to a source
> file; where a port collided with a rule already in this file, the conflict is
> resolved in the text and the winner is named. Upstream is no longer the bar
> here, and `verify-design-system.py` records the divergence rather than
> treating it as drift.

Type carries the design. If the type is wrong, nothing else matters.

## Principles

- A page is a pairing, not a single font. Display face + body face, minimum. *Single-font pages are allowed only when the single font IS the design choice* — a true terminal aesthetic is monospace-everywhere on purpose; a Manifesto poster might be one display face on purpose. The default is a pairing.
- Commit to extremes. Weight 200 next to weight 800 reads as intentional. Weight 400 next to weight 600 reads as a default setting.
- Size steps should be ratios, not increments. Major third (1.25), perfect fourth (1.333), perfect fifth (1.5), or golden (1.618). Pick one and use it.
- Line-height changes with size. Tight for display (1.05–1.2), comfortable for body (1.5–1.65).
- Measure — line length — lives between 45 and 75 characters. Use `max-width: 65ch` as the default.

## The 2+1 rule — three faces is the ceiling

**A page may use at most three distinct font families.** One **display**, one **body**, and an optional **outlier** for a single typographic moment — wordmark, hero stat, pull quote, masthead — where the page wants exactly one note that doesn't sound like the rest. Four families is slop. Two is canonical. Three is the ceiling, used sparingly.

The pattern:

```css
:root {
  --font-display:  "Fraunces", ui-serif, Georgia, serif;       /* headings, hero */
  --font-body:     "Geist", ui-sans-serif, system-ui, sans;    /* prose, UI */
  --font-outlier:  "Geist Mono", ui-monospace, monospace;      /* wordmark + hero stat ONLY */
}
```

The outlier is a *register*, not a third surface. Rules:

- **Outlier appears in ≤ 2 places** on the whole page. Wordmark + hero stat. Or pull quote + masthead. Two slots, not five. If you find yourself reaching for it a third time, you don't have an outlier — you have a third body font, which is slop.
- **The outlier carries one role.** It tags a specific kind of content (the brand, the headline figure, the manifesto line). Once you know what it tags, every instance of that role uses it. Don't apply it to one button label and not another.
- **Mono counts as a face.** A page with Fraunces display, Geist body, and Geist Mono in code blocks is using three families. That's fine — code is the outlier role. Don't sneak in a fourth.
- **Same family at different weights is one family**, not two. Geist 400 + Geist 700 is one font; pairing it with Fraunces is two. Adding Geist Mono on top is three.

Two families is still the right answer for most pages. Three is for SaaS / brand-heavy / editorial-rich pages where the wordmark needs a different register than the body.

## Font selection procedure — four steps, every project

Ported from impeccable `reference/brand.md` § Font selection procedure. **Every project. Never skip.**

1. **Read the brief. Write three concrete brand-voice words.** Not "modern" or "elegant," but "warm and mechanical and opinionated" or "calm and clinical and careful." Physical-object words.
2. **List the three fonts you'd reach for by reflex.** If any appear in the reflex-reject list below, reject them; they are training-data defaults and they create monoculture.
3. **Browse a real catalog** (Google Fonts, Pangram Pangram, Future Fonts, Adobe Fonts, ABC Dinamo, Klim, Velvetyne) with the three words in mind. Find the font for the brand as a *physical object*: a museum caption, a 1970s terminal manual, a fabric label, a cheap-newsprint children's book, a concert poster, a receipt from a mid-century diner. Reject the first thing that "looks designy."
4. **Cross-check.** "Elegant" is not necessarily serif. "Technical" is not necessarily sans. "Warm" is not Fraunces. **If the final pick lines up with the original reflex, start over.**

Write the three words and the three rejected reflexes into `BRIEF.md`. A pick with no rejected reflexes behind it is a reflex that was never tested.

### Reflex-reject list

Training-data defaults. Look further:

> Fraunces · Newsreader · Lora · Crimson · Crimson Pro · Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne · IBM Plex Mono · IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans · DM Serif Display · DM Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans · Instrument Serif

impeccable `new-work.md` § 4 adds **Inter-as-display** to the same list and states the escape clause: *naming one of these faces anyway requires a reason no other face could satisfy, and a subject association is never that reason* — books wanting a serif, bookshops wanting hand-lettering, and tech wanting a mono are exactly the associations the list exists to break.

**The list applies to new design choices.** When the existing brand has already committed to a face as part of its identity, identity preservation wins; a variant on a shipping surface does not second-guess what is already live. The list is for greenfield decisions and departure-mode variants.

### Reflex-reject aesthetic lanes

Parallel to the font list, and the trap one tier deeper than picking a Fraunces. If a brief lands in one of these lanes without a register reason that *requires* it (a literal magazine, a literal terminal, a literal industrial signage system), it is the second-order reflex.

- **Editorial-typographic.** Display serif (often italic) + small mono labels + ruled separators + monochromatic restraint. Klim-influenced, magazine-cover affectation. By 2026 every Stripe-adjacent and Notion-adjacent brand has landed here. The fingerprint: three rule-separated columns, an italic Fraunces / Recoleta / Newsreader headline, lowercase track-spaced metadata, no imagery.

More lanes land here on the same cadence the font list updates; brutalist-utility and acid-maximalism join when they saturate, and entries leave when they fall back below saturation.

### Anti-reflexes worth defending against

From impeccable `reference/typography.md` § Anti-reflexes:

- A technical/utilitarian brief does NOT need a serif "for warmth." Most tech tools should look like tech tools.
- An editorial/premium brief does NOT need the same expressive serif everyone is using right now. Premium can be Swiss-modern, neo-grotesque, a literal monospace, or a quiet humanist sans.
- A children's product does NOT need a rounded display font. Kids' books use real type.
- A "modern" brief does NOT need a geometric sans. The most modern thing you can do is not use the font everyone else is using.

### Serif discipline

Ported from `design-taste-frontend` § 4.1. **"It feels creative / premium / editorial" is not a reason to reach for a serif** — the mental model *creative brief = serif* is the single most-tested AI tell in production rounds. A serif is acceptable when one of these is explicitly true:

- the brand brief literally names a serif face, **or**
- the aesthetic family is genuinely editorial / luxury / publication / manuscript / heritage / vintage **and** you can articulate why *this* serif fits *this* brand.

For everything else — creative agency, design studio, modern brand, premium consumer, portfolio, lifestyle — **default to a sans display**. Sans display faces are not "boring"; they are the default for the same reason black is the default in fashion.

**Fraunces and Instrument Serif are banned as defaults** (the two LLM-favourite display serifs). When a serif *is* justified, rotate from the pool and do not reuse the same serif on consecutive projects: PP Editorial New, GT Sectra Display, Cardinal Grotesque, Reckless Neue, Tiempos Headline, Recoleta, Cormorant Garamond, Playfair Display, EB Garamond, IvyPresto, Migra, Editorial Old, Saol Display, Söhne Breit Kursiv, Domaine Display, Canela, Schnyder, Tobias, NB Architekt, ITC Galliard.

**Emphasis inside a headline uses italic or bold of the same family.** Dropping a serif word into a sans headline (or the reverse) for visual interest is amateur. Same-family italic/bold is the move.

### Pairing and voice by genre

From `brand.md` § Pairing and voice — the shape depends on the brand:

- **Editorial / long-form / luxury:** display serif + sans body (a magazine shape).
- **Tech / dev tools / fintech:** one committed sans, usually; custom-tight tracking, strong weight contrast inside a single family.
- **Consumer / food / travel:** warmer pairings, often a humanist sans plus a script or display serif.
- **Creative studios / agencies:** rule-breaking welcome. Mono-only, display-only, or custom-drawn type as voice.

When pairing, contrast on more than one axis: serif + sans (structure), geometric + humanist (personality), condensed display + wide body (proportion). **Never pair two faces that are similar but not identical** — two geometric sans-serifs create tension without hierarchy.

**Vary across projects.** If the last brief was a serif-display landing page, this one isn't.

### How this resolves against the catalog below

**Explicit conflict.** The reflex-reject list names faces that § The font catalog and § Tone-based pairing patterns currently recommend by name: Fraunces, Newsreader, Instrument Serif, Cormorant Garamond, Playfair Display, Lora, Crimson Pro, Space Grotesk, Space Mono, IBM Plex Sans, IBM Plex Mono, Outfit, DM Serif Display, Inter Tight (as an Inter cut).

**The reflex-reject list wins on the *decision*; the catalog keeps its descriptive value.** Concretely:

- The catalog is a lookup for *what a face is and where it comes from*, not a shortlist to pick from. Its ordering carries no recommendation weight for a reflex-rejected row.
- A reflex-rejected row may still be chosen — but only out of step 3 (a real catalog browsed against three brand words) with the reason written down, and never because the subject suggested it.
- The tone-pairing table's "free baseline" column is read *past* its reflex-rejected entries. Read past Fraunces and Newsreader under Editorial, past Space Grotesk under Brutalist, past IBM Plex Sans under Technical, and so on, to the entries that survive.
- **The Hallmark defaults survive:** Geist, Geist Mono, The Future, Bricolage Grotesque, Cabinet Grotesk, Clash Display, Satoshi, Sentient, Erode, Tanker, Switzer, General Sans, JetBrains Mono, Commit Mono, Anton, Big Shoulders Display, Tomorrow, Bodoni Moda, EB Garamond, Cardo, Source Serif 4, Spectral are not on any reflex-reject list.
- **Superseded by this port:** § The discipline's naming of *Fraunces* as a first-rate free exemplar, and § Wordmark's *"Fraunces wordmark"* / *"Fraunces body"* pairings. Those pairings still work typographically; they are no longer the example to reach for.

## Banned defaults

The list below is the chain's **absolute** ban — a harder rule than the reflex-reject list above. A reflex-rejected face can be argued into the design with a written reason; a banned default is reached for only when the user insists on it by name.

These fonts are on-distribution for every LLM. Do not reach for them without a deliberate reason:

- **Sans-serif:** Inter, Roboto, Open Sans, Lato, Poppins, Source Sans, Nunito, Montserrat, Raleway, Work Sans, DM Sans, system-ui, Arial, Helvetica.
- **Serif:** Merriweather, Playfair Display (as body — banned as overused body serif; ok as display in moderation), Lora, Source Serif, Georgia-as-default.
- **Mono:** Courier New, Consolas-as-default, system mono.

If the user insists on one, do it. Otherwise pick from the allowlist below.

## The font catalog

Three sources, in priority order:

- **Google Fonts** — free, served via CDN, works everywhere. The default source.
- **Fontshare** (Indian Type Foundry) — free for commercial use, foundry-grade. The "you didn't know these were free" tier. Drop-in via `<link href="https://api.fontshare.com/v2/css?f=...">`.
- **Foundry-licensed** — Klim, Pangram Pangram, Production Type, Lineto, Colophon. Only when the user has confirmed they're licensed.

### Free display faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Fraunces** | Google | Variable serif, deeply expressive italic, optical-size axis | Editorial, Atelier, brand-heavy |
| **Newsreader** | Google | Roman serif with optical-size + italic | Editorial, magazine, long-form |
| **Instrument Serif** | Google | Tight contrast, italic available, smart for short heads | Brand, atelier, intimate editorial |
| **Cormorant Garamond** | Google | Classical, high contrast, luxury register | Luxury, fashion, fine arts |
| **EB Garamond** | Google | Honest classical Garamond, body-grade | Editorial body, longform reading |
| **Cardo** | Google | Scholarly serif, generous x-height | Reference, academic, slow reading |
| **Source Serif 4** | Google | Modern transitional, big OT family | SaaS marketing with serif tone |
| **DM Serif Display** | Google | Bracketed serif, high-contrast display | Headlines that need to feel printed |
| **Bodoni Moda** | Google | Modern Bodoni revival, dramatic | Fashion, editorial, luxury display |
| **Playfair Display** | Google | Use only as display; banned as body | Marketing display moments — sparingly |
| **Geist** | Google | Modern grotesque, geometric, 7 weights | Modern minimal, SaaS, dev tools |
| **Inter Tight** | Google | Tighter Inter — allowed *only* as a body fallback in technical themes; never as display | UI body in restrained themes |
| **Bricolage Grotesque** | Google | Variable display sans, bold weights, condensable | Brutal, playful, riso-bold |
| **Space Grotesk** | Google | Geometric grotesque, slightly quirky | Brutalist, technical |
| **Anton** | Google | Heavy condensed grotesque | Posters, manifestos |
| **Big Shoulders Display** | Google | Industrial condensed | Sports, manifestos, declarative |
| **Tomorrow** | Google | Variable optical condensed | Tech, atmospheric, near-future |
| **Outfit** | Google | Modern geometric (banned as default; use only when *picked* deliberately) | Restrained tech — sparingly |
| **General Sans** | Fontshare | Modern grotesque, Geist-adjacent | Modern minimal alternative to Geist |
| **Switzer** | Fontshare | Neutral sans, broad weight range | SaaS body, restrained |
| **Cabinet Grotesk** | Fontshare | Display grotesque, 9 weights | Editorial display, magazine |
| **Clash Display** | Fontshare | Ultra-condensed display | Posters, brand moments |
| **Satoshi** | Fontshare | Playful geometric sans | Playful, consumer |
| **Sentient** | Fontshare | Variable serif, soft contrast | Soft editorial, atmospheric |
| **Erode** | Fontshare | Distressed serif, hand-set feel | Riso, tactile-rebellion, brand-y |
| **Tanker** | Fontshare | Heavy condensed grotesque, pure display | One-word posters, mastheads |

### Free body faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Geist** | Google | The default modern body sans | Modern minimal, SaaS, atmospheric |
| **The Future** | (in repo) | Hallmark's own body workhorse | Default Hallmark tone |
| **Newsreader** | Google | Reading serif, optical-size aware | Editorial body, longform |
| **Source Serif 4** | Google | Body-grade serif | Editorial mid-weight |
| **EB Garamond** | Google | Classical body | Editorial slow reading |
| **Spectral** | Google | Slab-ish serif, screen-tuned | Long-form on screen |
| **Lora** | Google | Calligraphic serif, body-grade | Body — sparingly (over-used) |
| **Crimson Pro** | Google | Old-style body, generous | Editorial slow body |
| **IBM Plex Sans** | Google | Engineering sans, broad family | Technical body |
| **Switzer** | Fontshare | Neutral sans body | SaaS body, restrained |
| **General Sans** | Fontshare | Geist-adjacent body | Modern minimal body |

### Free mono / outlier faces

| Family | Source | Voice | Best for |
| --- | --- | --- | --- |
| **Geist Mono** | Google | Geist's mono companion | Default Hallmark mono, code, captions |
| **JetBrains Mono** | Google | Engineering mono, ligatures | Code, terminal, technical |
| **IBM Plex Mono** | Google | Engineering mono, broad family | Technical body-grade |
| **Commit Mono** | Google | Tighter mono, modern | Code, modern terminal |
| **Space Mono** | Google | Quirky, slightly retro | Playful tech, riso |

### Tone-based pairing patterns

Each tone gets two rows: a **free baseline** (Google Fonts / Fontshare; works out of the box) and a **paid upgrade** (foundry licences required; only when the user has confirmed the budget and the licence). The free row is the default. **Never name a paid font in code without confirming the user is licensed** — the demo will fall back to system-default and look broken to the user.

| Tone | Tier | Display | Body | Outlier |
| --- | --- | --- | --- | --- |
| **Editorial** | Free | Fraunces · Newsreader · EB Garamond · Instrument Serif · Cabinet Grotesk | IBM Plex Sans · Switzer · Source Serif 4 | JetBrains Mono · Geist Mono · Erode (display moment) |
| | *Paid* | *Tiempos Headline · Söhne Breit · Reckless Display · Migra · Tobias* | *Söhne · Haffer · Untitled Sans* | *Söhne Mono · GT America Mono* |
| **Technical** | Free | JetBrains Mono · Geist Mono · Geist (700) · Commit Mono | Geist · IBM Plex Sans · Switzer | Tomorrow · Cabinet Grotesk (wordmark) |
| | *Paid* | *Berkeley Mono · Söhne Mono · GT Pressura · ABC Diatype Mono* | *Söhne · Untitled Sans · ABC Diatype* | *Berkeley Mono · GT Pressura Mono* |
| **Brutalist** | Free | Bricolage Grotesque (800) · Anton · Tanker · Big Shoulders Display | Geist · Switzer | Space Grotesk (numerals) · Geist Mono |
| | *Paid* | *Druk · Monument Extended · NaN Jaune · Migra · ABC Pressura* | *Söhne Breit · GT America* | *GT America Mono* |
| **Soft** | Free | Geist · Bricolage Grotesque (500) · Sentient · Newsreader | Geist · Crimson Pro · Switzer | Geist Mono · Satoshi (label) |
| | *Paid* | *Söhne · GT Pressura · Pangaia · Tobias* | *Söhne · Halyard Text · Satoshi* | *Söhne Mono · GT Maru Mono* |
| **Luxury** | Free | Cormorant Garamond · Fraunces · Cardo · DM Serif Display · Bodoni Moda | EB Garamond · Crimson Pro · Source Serif 4 | (rare; small caps from display family) |
| | *Paid* | *Canela · Tiempos Headline · GT Super · Domaine Display · Migra* | *Tiempos Text · Suisse Int'l · Domaine Text* | *(rarely used at this tier)* |
| **Playful** | Free | Bricolage Grotesque · Fraunces (italic) · Satoshi · Newsreader (italic) · Sentient | Geist · Newsreader · Satoshi | Geist Mono · Space Mono |
| | *Paid* | *Clash Display · Cabinet Grotesk · Migra · Tobias · Pangaia* | *Satoshi · Plus Jakarta Sans · GT Maru* | *Space Mono · GT Maru Mono* |
| **Austere** | Free | system-ui · Inter Tight (regular) · Geist (400) · Switzer (regular) | system-ui · Geist · Switzer | system-ui mono · Geist Mono |
| | *Paid* | *ABC Diatype · ABC Monument Grotesk · Söhne (regular) · ABC Pressura* | *ABC Diatype · Söhne* | *ABC Diatype Mono · Söhne Mono* |
| **Atmospheric** | Free | Geist (600) · Sentient · Tomorrow · Bricolage Grotesque | Geist (400) · Switzer | Geist Mono · JetBrains Mono |
| | *Paid* | *Söhne · GT Pressura · ABC Diatype* | *Söhne · ABC Diatype* | *Berkeley Mono · Söhne Mono* |
| **Workshop** *(Hallmark's own theme)* | Free | The Future · Geist · Cabinet Grotesk | The Future · Switzer | The Future Mono · Geist Mono |
| | *Paid* | *Avenir Next · GT Walsheim* | *Söhne · GT Walsheim* | *Berkeley Mono* |

**The discipline.** Default to the free pairings. They're not consolation prizes; Geist, Bricolage Grotesque, Cabinet Grotesk, Sentient, Clash Display, and JetBrains Mono are first-rate faces in 2026. (*Fraunces stood in this sentence until the reflex-reject port; it is still a fine face, it is no longer the one to name as the exemplar. See § How this resolves against the catalog below.*) The paid upgrades exist for two cases: (a) the user has explicitly confirmed they're licensed, or (b) the user is asking for a specific named foundry voice (e.g., "make it look like Klim", "I want Söhne"). Reach for Tier 2 only then; otherwise the free row is the right answer. Treat the free row as canon, the paid row as a *cited* alternative.

## Wordmark / logo typography

The wordmark in the navbar and footer **may use a different display face than the body**. On tone-rich themes (Editorial, Atelier, Specimen) it **should** — collapsing the wordmark into the body family flattens the visual hierarchy and the page reads as un-branded.

```css
:root {
  --display:       "Geist", system-ui, sans-serif;     /* body + display */
  --font-wordmark: "Fraunces", Georgia, serif;         /* logo only */
}
.wordmark {
  font-family: var(--font-wordmark);
  font-weight: 600;
  letter-spacing: -0.015em;
}
```

Recommended pairings (free baseline first):

- **Geist body → Fraunces wordmark, IBM Plex Mono wordmark, or Bricolage Grotesque (heavy) wordmark**
- **Fraunces body → Geist Mono wordmark, Inter Tight wordmark**
- **System-ui body → JetBrains Mono wordmark, Newsreader wordmark**
- **Inter Tight body → Fraunces wordmark, EB Garamond wordmark**

When to use the same family for both:

- **Editorial · Letter · Manifesto · Long Document** can collapse to a single family because the body voice carries the brand. The wordmark in these contexts is small, grounded, and earns its weight by being typeset rather than decorated.

When to use a contrasting family:

- **Bento Grid · Stat-Led · Workbench · Marquee Hero** — these archetypes lean visually generic (geometric grids, big numbers, browser-frame mockups) and need the wordmark to do the typographic differentiation work the body can't.

**Avoid the same-family collapse on a SaaS page.** A Geist-only page where the wordmark is also Geist 600 reads as un-designed; the wordmark in Fraunces SemiBold over a Geist body costs nothing and adds the one typographic register that says *this is a brand*.

## Scale

Pick a ratio. The default for Hallmark work is **1.25** (major third). Build the scale from a 16px body, then clamp display sizes for responsive.

```css
:root {
  --text-xs:   0.64rem;   /* 10.24px */
  --text-sm:   0.8rem;    /* 12.8px  */
  --text-base: 1rem;      /* 16px    */
  --text-md:   1.25rem;   /* 20px    */
  --text-lg:   1.5625rem; /* 25px    */
  --text-xl:   1.9531rem; /* 31.25px */
  --text-2xl:  2.4414rem;
  --text-3xl:  3.0518rem;
  --text-4xl:  3.8147rem;
  --text-display: clamp(2.75rem, 5vw + 1rem, 5.25rem);
}
```

**Display max — keep it ≤ 5.5rem (88 px).** Above that, hero headlines crowd themselves on 1280–1440 px viewports and require multi-line wrapping that almost always reads as drama, not gravity. Even on Manifesto / Brutal display-heavy themes, cap at 6rem (96 px). The exception is a single-line, single-word display (e.g. a stat) that occupies ≤ 12 ch — it can grow to 7rem. **Default emit format is `clamp(2.75rem, 5vw + 1rem, 5.25rem)`.**

### Hero headline sizing — match size to copy length

Count characters in the rendered hero `h1`. Pick the cap by bucket — the rule applies on top of any per-theme `--text-display` clamp:

| Headline length | Size cap | Notes |
| --- | --- | --- |
| **≤ 20 chars** (e.g. *"Limitless"*, *"Made not generated"*) | full `--text-display`; single-word can grow to 7rem | Display-heavy themes only |
| **21–50 chars** (the default sweet spot) | `--text-display` | If it wraps past 2 lines at 414 px, step down to `--text-display-s` |
| **51–90 chars** | cap at `--text-display-s` | Strongly consider splitting into eyebrow + headline |
| **> 90 chars** | rewrite shorter, or cap at `--text-4xl` with tighter leading | A 100-char headline at display size is the single most reliable AI tell |

**Aggressive-display themes step down one rung when headline > 50 chars.** Brutal, Riso, and Manifesto clamp `--text-display` at 6.5–9rem — that ceiling is for ≤ 50-char statements only. Past 50 chars, route them to `--text-display-s` automatically. **When you write the headline yourself (no user-supplied copy), aim for ≤ 7 words and ≤ 50 chars from the start** — imperative or nominal phrase, never a gerund opener.

Use no more than five sizes on a single page. If you need more hierarchy, use weight and colour, not another size.

**The failure this prevents** is too many sizes sitting too close together — 14, 15, 16, 18 px — which reads as muddy hierarchy rather than as a fine gradation. Fewer sizes with more contrast between them, every time.

### Vertical rhythm — line-height is the base unit

From impeccable `reference/typography.md` § Vertical Rhythm: **the body line-height is the base unit for all vertical spacing.** Body text at `line-height: 1.5` on `16px` type is 24px, so spacing values are multiples of 24px. Text and space then share a mathematical foundation, and the harmony is subconscious rather than argued for.

refero `typography.md` § 7 gives the same rule one rung finer — `line-height × 0.5` is the *minimum* step, so the 24px line-height above yields a 12 / 24 / 48 / 72 ladder:

```css
:root {
  --space-xs: 12px;   /* 0.5 × line-height */
  --space-sm: 24px;   /* 1   × line-height */
  --space-md: 48px;   /* 2   × line-height */
  --space-lg: 72px;   /* 3   × line-height */
}
```

**Spacing matters more than font size.** Two designs with the same faces and different spacing look like different products. Fix the spacing before touching the type. (The chain's 4-pt spacing scale lives in [`layout-and-space.md`](layout-and-space.md); this is the rule that ties it to the type scale rather than leaving the two unrelated.)

**Paragraph rhythm:** pick either space between paragraphs OR first-line indentation. Never both. Screen work usually wants space; editorial long-form can justify indent-only.

### Fluid or fixed, and bounding the clamp

- **Fluid `clamp()`** for headings and display on marketing and content pages, where text dominates and has to breathe across viewports. The middle term (`5vw + 1rem`) controls the scaling rate; the `rem` offset keeps it from collapsing on small screens *and* keeps browser zoom working.
- **Fixed `rem` scales** for app UI, dashboards, and data-dense surfaces. No major product design system (Material, Polaris, Primer, Carbon) uses fluid type in product UI — fixed scales give container layouts their spatial predictability. **Body text stays fixed even on marketing pages**; the size difference across viewports is too small to be worth it.
- **Bound the clamp: `max-size ≤ ~2.5 × min-size`.** Wider ratios break zoom and reflow behaviour and make large viewports feel like the page is shouting.
- **Scale container width and font-size together**, so the effective measure stays in band at every viewport. A heading that widens faster than its container drifts out of the comfortable measure at the top end.

## Weights

- Body: one weight (typically 400 or 350). Bold for emphasis only.
- Headings: a weight that contrasts the body by at least 300 units. If body is 400, headings are 700 or 200 — not 500 or 600.
- Never synthesise. Load the weight you need; don't rely on `font-weight: bold` against a single-weight file.

## Required features

- `font-display: swap` on every web font.
- Match fallback metrics with `size-adjust`, `ascent-override`, `descent-override`, `line-gap-override` to prevent CLS.
- Tabular numbers on any data display: `font-variant-numeric: tabular-nums;`.
- Oldstyle figures for body copy where the face supports them: `font-variant-numeric: oldstyle-nums;`.
- Proper typographic punctuation: `" " — … ‘ ’`. Never straight quotes, never `--` or `...`.
- **Underline offset and thickness are set, not inherited** (`text-underline-offset`, `text-decoration-thickness`). Along with selection colour, caret colour, focus ring and scrollbar — see [`color.md`](color.md) § Browser surfaces — these are the parts you did not draw that still carry the design, and the cheapest signal that a page was built rather than assembled. It is also the step that gets skipped most reliably.
- **The chosen face distinguishes `I`, `l`, `1` and `O`, `0`.** Check the specimen before committing; a face that fuses them is disqualified for anything that carries an identifier, a code, or a number a reader has to transcribe. **Fallbacks are declared in the same classification** as the face they stand in for — a grotesque falls back to a grotesque, not to a serif. (designpowers `ui-composition`.)

### Loading and layout shift

Fonts load late, text reflows, content jumps. The fix, ported from impeccable `reference/typography.md` § Web Font Loading, is four declarations and one decision:

```css
/* 1. Show text immediately */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-display: swap;
}

/* 2. Match the fallback's metrics so the swap doesn't move anything */
@font-face {
  font-family: 'CustomFont-Fallback';
  src: local('Arial');
  size-adjust: 105%;        /* scale to match x-height   */
  ascent-override: 90%;     /* match ascender height     */
  descent-override: 20%;    /* match descender depth     */
  line-gap-override: 10%;   /* match line spacing        */
}

body { font-family: 'CustomFont', 'CustomFont-Fallback', sans-serif; }
```

Tools like [Fontaine](https://github.com/unjs/fontaine) compute the four overrides automatically. Do not eyeball them.

- **`swap` vs `optional`.** `swap` shows fallback text immediately and FOUT-swaps when the web font arrives. `optional` uses the fallback if the web font misses a ~100 ms budget and avoids the shift entirely. Pick `optional` when zero layout shift matters more than seeing the branded face on a slow network.
- **Preload the critical weight only** — typically the regular body weight used above the fold. Preloading every weight costs more bandwidth than it saves.
- **Variable font at 3+ weights or styles.** One variable file usually beats three static weight files, gives fractional weight control, and pairs with `font-optical-sizing: auto`. At 1–2 weights, static is fine.

The metric-fallback block and the preload rule are the two CLS-decisive items here; they belong to the performance budget as much as to this file.

### OpenType and rendering polish

```css
/* Even out heading line lengths (the browser picks better break points) */
h1, h2, h3 { text-wrap: balance; }

/* Reduce orphans and ragged endings in prose */
article p { text-wrap: pretty; }

/* Variable faces: pick the right optical-size master automatically */
body { font-optical-sizing: auto; }

/* Numerals that have to line up */
.data-table, .price, .stat { font-variant-numeric: tabular-nums; }

/* Fractions, small caps for abbreviations, no ligatures in code */
.recipe-amount { font-variant-numeric: diagonal-fractions; }
abbr          { font-variant-caps: all-small-caps; }
code          { font-variant-ligatures: none; }
body          { font-kerning: normal; }
```

Check what your face actually supports at [Wakamai Fondue](https://wakamaifondue.com/) before relying on a feature.

### Wrapping, trimming and overflow

- **`balance` on short headings, captions, pull quotes and card titles. `pretty` on lead and body prose.** A single word on the last line of a hero title reads as accidental, not designed.
- **Do not apply either blindly** to nav, buttons, tables, badges, code, form controls, or dense UI labels. Browsers ignore `balance` past a few lines anyway, and evening out a whole paragraph wastes space and makes it harder to read.
- **Still inspect the actual break points.** If the wrapping is awkward after `balance`, the fix is the copy, the `max-width`, the size, or the leading — not more CSS. `text-wrap` is progressive enhancement; nothing breaks where it is unsupported.
- **`text-box` trims the reserved space fonts leave above and below the letters** — the reason text sits slightly low in buttons and badges. `text-box: trim-both cap alphabetic` trims both edges; `trim-start cap` and `trim-end alphabetic` trim one. Chromium 133+ and Safari 18.2+, not Firefox: progressive enhancement, unsupported browsers keep the default leading.
- **Overflow is handled, not hoped for:** `text-overflow: ellipsis` (with `overflow: hidden; white-space: nowrap`) for one line, `line-clamp` for several, `overflow-wrap: break-word` for URLs and IDs. Truncation hides content — where the hidden value matters, expose the full one.
- **Flex children need `min-width: 0` to truncate at all.** `flex: 1` alone will not do it; the child's min-content width holds the container open and the ellipsis never appears. This is the single most common reason a truncation rule "doesn't work".

### Tracking (letter-spacing)

Letter-spacing is the polish detail that separates refined from rough, and the one most reliably skipped. Without it: all-caps looks cramped and cheap, small text gets harder to read, and large headlines feel loose.

| Text type | Size | Value | Priority |
| --- | --- | --- | --- |
| Body text | 14–18 px | `0` | Default is fine |
| Small text | 11–13 px | `0.01em` – `0.02em` | **Required** |
| UI labels / buttons | any | `0.01em` – `0.03em` | **Required** |
| ALL CAPS | any | `0.06em` – `0.14em` | **Mandatory** |
| Large headings | 32 px+ | `0` to `-0.02em` | Recommended |
| Display | 48 px+ | `-0.02em` to `-0.03em` | Recommended |

**Always `em`, never `px`** — `em` scales with the font size, `px` does not, and a tracked label breaks the moment the size changes.

**Tighten only when** the size is 32 px+, it is a headline and not body, the weight isn't light, and the problem pairs (AV, WA, To) don't collide.

*Conflict resolved.* Three source ranges disagree on all-caps: refero `typography.md` § 8 says `0.06–0.10em` (mandatory), impeccable `reference/typography.md` says 5–12 % (`0.05–0.12em`), and this file's § Headings rules already said `0.08–0.14em`. **The mandatory floor is `0.06em`** — nothing all-caps ships below it, which is the strictest of the three floors. **The house range stays `0.08–0.14em`** for small caps and labels, because it is the chain's existing rule and no source forbids the top end. Real small caps set via `font-variant-caps` take the same treatment, slightly gentler.

## Body text rules

- Minimum 16px. Below 14px is accessibility-hostile.
- Line-height 1.5–1.65 on body copy, tighter (1.1–1.3) on display. **Floor for all-caps display heads (`text-transform: uppercase` on `.hero__display` / `.section__title` / `h1` / `h2`) is `1.0` — recommended `1.02–1.08`.** Below 1.0 the cap-tops of line N+1 collide with the baseline of line N (no descenders to cushion the gap); the comma + cap-D on a wrapped "PROMPT, / DIFFERENT" fuse into a single glyph blob. Condensed display faces (Anton, Inter Tight 900, Bebas Neue) make this worse. Gate 55 auto-fails the pattern.
- Measure 45–75 characters (`max-width: 65ch`).
- Never all-caps body copy. Never justified text without hyphenation. Never letter-spacing above 0.05em on body.
- **Serif body gets a slightly longer measure *and* slightly more line-height than a sans.** The two move together; lengthening the line without opening the leading is what makes a serif column feel dense. (anthropic `frontend-design`.)

### Measure by register — the one table

**This is the canonical measure table. Every other file in the chain points here.** Four numbers were circulating and reading as a contradiction; they were four different columns, not four opinions about one.

| Column | Measure | Where the number comes from |
| --- | --- | --- |
| Long-form prose, article body | **60–75 ch**, target `65–75 ch` | `design-verify/SKILL.md` § Type (`65–75ch`); interfaces `wrapping-and-punctuation.md` (60–75); anthropic `frontend-design` ("less than 80 characters") |
| General body copy — the default | **45–75 ch**, default `max-width: 65ch` | this file; `verbs/critique.md` § Readability; scroll-craft `taste.md` (`--sc-measure` is 62ch) |
| Typeset display columns in print / editorial registers | **36–58 ch** | `SKILL.md` craft floor § Display type |
| Compact UI — card descriptions, captions, list rows | **~45 ch** | refero `typography.md` § 9 |

**Hard limits either side:** below 45 ch prose fragments; above 85 ch the eye loses the start of the next line. A full-width paragraph on a 1600 px monitor is unreadable regardless of size.

**Line-height moves inversely with measure.** Narrow columns take tighter leading, wide columns need more: at 80+ characters use 1.6–1.7, at ~40 characters 1.4 is fine. A serif takes marginally less than a sans at the same measure.

### Light text on dark — compensate on three axes

**Not one axis, three.** Light type on a dark ground reads as lighter weight *and* tighter *and* more crowded than the same setting inverted, and fixing only the leading leaves it looking thin and blurry:

1. **Line-height** up by 0.05–0.1.
2. **Tracking** up by 0.01–0.02em.
3. **Weight** up one notch (regular → medium).

Dark-mode type set with light-mode metrics is the failure this prevents, and it is the reason an inverted section can look cheap while every measured value passes. Three sources state it identically — impeccable `reference/typography.md` § Readability & Measure, impeccable `reference/brand.md` § Scale (line-height +0.05–0.1), and scroll-craft `taste.md` § Typography — so it is not a preference.

The colour half of the same problem (re-inking an inverted subtree, muted tones needing a value per ground) is in [`color.md`](color.md).

## Headings rules

- Tight tracking on display sizes (`letter-spacing: -0.02em` to `-0.04em` depending on the face).
- Loose tracking on small caps / labels (`letter-spacing: 0.08em` to `0.14em`, `text-transform: uppercase`, use small caps if the face has them: `font-variant-caps: all-small-caps;`).
- Skip no levels. `h1` → `h2` → `h3`. Style them visually how you like, but keep semantic order.
- **Tracking tightens as size grows.** A face set at 6rem with default tracking reads loose and amateur. This is optical correction, not decoration — the same face needs a different value at 16 px and at 96 px, and shipping one value for both is the tell. (scroll-craft `taste.md` § Typography.)
- **Italic descender clearance is mandatory.** When italic is used in display type and the word contains `y g j p q`, `line-height: 1` clips the descender. Use **`1.1` minimum** and reserve space on the wrapping element (`padding-bottom` / `margin-bottom` of one step). Audit every italic word in a display headline before shipping — the clip is invisible at editing zoom and obvious at full size. (`design-taste-frontend` § 4.1.)

## Bans

- No Inter, no Roboto, no Open Sans. No system stack as the *only* stack.
- No gradient text on headings (`background-clip: text` with a gradient fill).
- No single-font pages.
- No all-caps paragraphs.
- No font-size below 14px for body copy, below 10px anywhere.
- No hard-synthesised bold or italic.
- **No more than three font families on a single page.** Display + body + one outlier is the ceiling. Four families = slop. Audit gate.
- No outlier face used in more than two slots. Wordmark + hero stat is the canonical pair; if you reach for a third slot, drop it back to the body face.
- **No more than four distinct text colours on a page** — primary, secondary, tertiary, and one more if a role genuinely needs it. More than four is either an unresolved hierarchy or a page assembled from several. Count the rendered values, not the token names. (refero `typography.md` § 13 Quick Test; `measure.py` already counts distinct sizes and can count these.)
- No all-caps set without tracking. `text-transform: uppercase` with default spacing is cramped and reads as unfinished; see § Tracking for the floor.
- No italic display word with a descender set at `line-height: 1`.
- No face picked by reflex. If the pick matches the reflex you wrote down in step 2, it isn't a pick.
