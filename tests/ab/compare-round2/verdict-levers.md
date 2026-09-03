# Runda 2 — spakarna (T12–T18) mot K1, samma florist-brief, blinda one-shots

Fold-mosaik: `compare-round2/folds-levers.png` (läst). Siffror: `README-round2-numbers.md`.

| Spak | Fold (mina ögon) | axe · overflow320 · dead · kontrast-under-media · detect | Beslut |
|---|---|---|---|
| K1 (v3) | fotoplansch, serif, koral-ord | 1 · 0 · 2 · 0 · 1 | baslinje |
| T12 worlds | bröllopsbåge-foto (nytt!), vit serif direkt på ljus bild = oläslig rubrik, röd knapp | 1 · 4 · 0 · 3 · 2 | förordet gav ny bild och ny stämning; utförandet bröt kontrast. IN som förord, med scrim-regel |
| T13 amplify | identisk med K1 i folden | 1 · 0 · 2 · 0 · 1 | UTE: tre dolda småsteg lyfter inget |
| T14 imagery pipeline | samma calyx-bukett som alla andra, vit serif på upptagen bild | 1 · 0 · 0 · **7** · 0 | pipelinen valde "bästa" bilden ur en pool på 19 → samma bild som resten. UTE tills poolen växer |
| T15 taste | samma bukett, tunn italic serif oläslig | 1 · 0 · 0 · 4 · 1 | UTE: taste-profilen landade i defaulten |
| T16 gpt-taste | samma bukett, fet grotesk + scrim (läsbart), pill-nav, bento | 1 · 0 · 0 · **16** · 0 | UTE: SaaS-slop-drag (pill, bento), 16 kontrastfynd i skivorna |
| T18 laws | foto under nav, hierarki-plan | 1 · **20** · 0 · 0 · 1 | UTE: lagarna ändrade inte utseendet, och 20 overflow-element vid 320 px |

**Rotorsak till likheten (bevisad av mosaiken):** (1) fotopoolen är 19 verifierade ID:n, fyra av dem blommor, så varje byggare landar på samma hero; (2) registertabellen säger florist → editorial print och house-physics belönar "fullbleed foto med typ över"; (3) serif-tvåton är reflex. Ingen av spakarna angriper de tre; breddkontraktet gör det (B1–B4, separat verdict).

**Åtgärder som går in i kedjan:** (a) worlds-förordet i Step 2b (varje Persuade-bygge skriver en style preamble före tokens); (b) registertabellen: kategoridefaulten är SISTA valet på Tier 3 — välj ur register × grammatik × värld-matrisen och säg varför inte defaulten; (c) bake-offens tre riktningar ska spänna tre register, tre grammatiker och tre världar, och fingerprint-gaten körs mot syskonen i sessionen, inte bara registret; (d) fotopoolen: Unsplash API-nyckel (gratis, Antons handpåläggning) så `photo-sources` kan söka på riktigt; tills dess är fotobyggen dömda att likna varandra; (e) typ-över-foto kräver plansch eller uppmätt scrim (contrast_over_media) — T12/T14/T15 föll alla där.
