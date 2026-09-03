# Audit findings — planted.html (Florhuset Majorna)

1. Hero, `.hero .ctas` (two `.btn-primary` links) · Two identical filled accent buttons side by side ("Beställ bukett" / "Boka bröllopsmöte") give no primary/secondary hierarchy — the visitor can't tell which is the default action · major
2. Global accent usage (`--accent` on `.btn-primary`, `.badge-decorative`, `.dot-slut`, footer `h3`) · The single saturated accent appears only as fill on small controls (buttons, pill badge, status dot, footer labels) and never once at display scale (no giant price, drop cap, or glyph carries it) · major
3. "Veckans blomma" section, `.badge-decorative` vs `.cta-quiet` · The filled "★ Mest bokade" pill reads louder (color, weight, shape) than the actual conversion action below it, a plain underlined text link "Starta prenumeration →" — the loudest element on the block isn't the CTA · major
4. Ledger row 03, "Dahliabukett", `.dot-slut` · Sold-out state is carried by a bare 8px red dot with no adjacent text label ("Slutsåld" or similar) — meaning is color-only and easy to miss or misread as decoration · major
5. Bröllop / Prenumeration / Ateljékvällar sections (three `.flat-text` blocks in a row) · Three consecutive sections share identical anatomy — kicker, h2, one paragraph, no image, no ledger, same cream ground — reading as one repeated template block rather than three distinct sections · major
6. "Om ateljén" info-grid, three `.info-block` columns · The middle column heading "Öppettider" is set as a bold serif h3 while the flanking "Adress" and "Hitta hit" use small mono-caps kickers — the row's three parallel columns don't share a heading treatment, breaking the grid's symmetry · major
7. Hero and about-section `figcaption` (`--caption-grey` on `--cream`) · Caption text renders as pale grey on warm cream at 11px — contrast is close to the edge of legibility · major
8. Section padding scale (`.hero` 96px, `.ledger-section` 116px, `.flat-text-bröllop` 84px, `.flat-text-prenumeration` 120px, `.flat-text-ateljekvallar` 96px) · No shared vertical rhythm across sections — gaps feel arbitrary when scrolling down the page · minor
9. CTA styling overall (hero `.btn-primary` vs `.btn-text` / `.cta-quiet` used everywhere else) · Two unrelated CTA idioms coexist on one page — filled mono-caps rectangle buttons in the hero, typeset italic/underlined text links in every other section — with no visible rule for when each applies · minor
10. "Om ateljén" heading pair, `.about-section h2` (28px) vs `.about-section h3` (25px) · Adjacent heading levels sit within roughly 1.1× of each other, too close to read as a real hierarchy step, and it's made worse by the oversized "Öppettider" h3 next to it (see #6) · minor

7 major · 3 minor
