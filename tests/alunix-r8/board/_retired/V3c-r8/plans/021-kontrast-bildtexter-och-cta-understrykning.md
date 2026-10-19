# 021 · Kontrast: ramarnas bildtexter och kortets CTA-understrykning

- **Status**: TODO (R6)
- **Commit**: R5-läget av `runs/V3c/index.html`, md5 `fcbee8f1`
- **Severity**: HIGH (WCAG 1.4.3 och 1.4.11, a11y-rapportens två HIGH)
- **Category**: Accessibility (H-34)
- **Estimated scope**: 1 fil, 3 rader CSS
- **Källor**: design-a11y-reviewer fix 1 (`.frame-cap` 3,06:1, 50,1 % av ytan under 4,5:1
  vid scrollY 4000) och fix 2 (`.card-cta` understrykning `#1e5e9c` mot `#0b0c0e` 2,92:1)

## Problem

```css
/* index.html:580-581 - current */
  .frame-cap{line-height:1.5;padding:10px 2px 0;font-size:12px;
    letter-spacing:.02em;color:rgba(244,242,239,.86);}
/* index.html:443-446 - current (utdrag) */
  .card-cta{…;text-decoration:underline;
    text-underline-offset:5px;text-decoration-color:var(--c-accent);
    text-decoration-thickness:2px;…}
```

Bildtexten (12 px, 86 % vit) står på den fotografiska grunden, som driftar mot papper
under s5/s6; mätt sämsta lapp 3,06:1. Understrykningen är det enda som identifierar
`Boka ett möte` som länk och mäter 2,92:1 mot kortets grund (kravet 3:1 för icke-text).
BRIEF § rättelse 2 mätte samma par (2,93:1) för fokusringen och tog bort det där, men
lämnade det på sidans enda konverteringskontroll.

## Target

**A. Bildtexten på en yta med känd valör.** Bildtexten flyttas in i ramens egen wrapper
som en rad med papperets valör: `.frame-cap` får `background:var(--bg); color:var(--ink);
padding:10px 12px;` och ligger direkt under ramen utan mellanrum, som ett typsatt band i
samma bredd som ramen (TASTE § 2.3: hårlinjer och ton på ton, inte etikettrutor ovanpå
bilden; bandet ligger under, inte ovanpå). Kontrast `--ink` `#16140f` mot `#fdfbf4` =
17,9:1 oavsett grunddrift. Bandet får `border-top:1px solid var(--c-line-on-paper)` så det
läser som en bildtext i en katalog, inte som en knapp.

```css
/* target, index.html:580-581 */
  .frame-cap{line-height:1.5;padding:10px 12px;font-size:12px;letter-spacing:.02em;
    background:var(--bg);color:var(--ink);border-top:1px solid var(--c-line-on-paper);}
```

**B. Understrykningen i `currentColor`.** Accenten behåller sin plats som tesplåtens grund
och som måtten i arket; på kortet bär `currentColor` (17,5:1) understrykningen och accenten
lämnar kortet. Det sänker accentens frekvens på sidan från tre roller till två (tesplåten,
arkets mått) och raden i decision ledger uppdateras.

```css
/* target, index.html:445 */
    text-underline-offset:5px;text-decoration-color:currentColor;
/* target: hover/active (rad 447-449) byter till text-decoration-thickness:3px i stället
   för färg, eftersom färgen redan är full */
```

## Repo conventions to follow

- Ett värde per grund (house physics): bildtexten får en egen grund i stället för att
  jaga en färg som klarar alla grunddriftens stopp.
- Accentens frekvens skrivs som ett tal i ledgern (`BRIEF.md` § Role rules): efter 021
  och 020 är det två roller: tesplåtens grund (inklusive drift-målet) och arkets sanna
  mått.

## Steps

1. Byt rad 580-581.
2. Byt rad 445; skriv om `.card-cta:hover` och `:active` (rad 447-449) till tjocklek.
3. Mät: `contrast_over_media.py --url` vid scrollY 4000 och 4700 (1440): `.frame-cap`
   ≥ 4,5:1 mot ljusaste 5 %; `contrast.py`-metoden på `.card-cta`s understrykning: ≥ 3:1.
4. Ledgerrad i `BRIEF.md`: accentens frekvens två roller; källa a11y fix 1-2.

## Boundaries

- Ramarna, deras `inert` och `pointer-events` rörs inte.
- Bildtexternas strängar är låst copy (`Exempelsida: …`) och rörs inte.
- Matchar inte raderna 443-449 eller 580-581: STOPPA.

## Verification

- **Mekaniskt:** `a11y_scan.py` 0 violations; `contrast_over_media.py --url` på båda
  bildtexterna vid tre scrolldjup (p 0,2, 0,5, 0,9 för respektive ram) ≥ 4,5:1; kortets
  understrykning ≥ 3:1 mot `#0b0c0e`.
- **Skärmbilder:** s5 och s6 vid 1440 och 390: bildtextbandet under ramen läser som en
  katalograd, inte som en etikett över bilden; `?preview=back`: understrykningen vit.
- **Done when:** H-34 bockad för de fyra strängarna; a11y-rapportens två HIGH stängda.
