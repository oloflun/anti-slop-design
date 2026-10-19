# 004 — "Efter"-etiketten går utanför vyporten och klipper den låsta bildtexten under 640 px

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: funktionsfel i typen (F-007-avvikelse, s1 vid 320–414; följdfel av plan 003)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K4/index.html`), en breddregel

## Problem

Läst som pixlar i `tests/alunix-r8/review/r3/K4-fold-390.png`: raden under
`Efter` renderas

```
Exempelsida: Calyx,
florist i Stockholr        ← sista tecknen ligger utanför vyporten
```

Strängen `Exempelsida: Calyx, florist i Stockholm` står i `PRODUCT.md` §
Låst copy. En ofullständig rendering av låst copy är samma felklass som K3:s
plan 002 och åtgärdas på samma grund: **ingen bokstav får försvinna.**
Bevakaren såg det och bad om en mätning före domen (`NOTES.md` § Bevakarens
observationer, punkt 1); mätningen gjordes inte, och den behövs inte längre —
felet är räknat ur koden och är strukturellt, inte marginellt.

Det är ett **direkt följdfel av plan 003**, och orsaken är att etikettens bredd
är en andel av scenen medan sömmen har flyttat sig:

```css
/* tests/alunix-r8/runs/K4/index.html:497 — current, i @media (max-width: 640px) */
  .tag { top: auto; bottom: calc(100% - var(--head-h) + 10px); width: 44%; }
  .tag--before { right: calc(100% + 12px); }
  .tag--after  { left: 12px; }
```

`.tag--after` börjar 12 px till höger om sömmen och är 44 % av scenen bred.
Överskottet är därför `SPLIT_START·W + 12 + 0,44·W − W = 0,025·W + 12`, alltså
**positivt vid varje bredd**: 21,8 px vid 390, 20,0 px vid 320, 22,4 px vid 414.
Etiketten hängde utanför vyporten redan vid `--split-start` 0,5 (då med 7 px);
0,585 gjorde spillet stort nog att äta upp ett tecken. Plan 003:s steg 4
kontrollerade bara `Före`-etiketten, som får **mer** plats när sömmen flyttar
höger. `Efter` får mindre. Det var mitt fel i planen, inte byggarens i utförandet.

Vid `?preview=after` renderas samma rad komplett på två rader
(`review/r3/K4-after-390.png`), vilket bekräftar att strängen och radbrytningen
är rätt och att det bara är den tillgängliga bredden vid ps = 0 som saknas.

## Target

Etiketternas bredd härleds ur den plats som faktiskt finns på deras egen sida om
sömmen, inte ur en fast andel av scenen. Etiketterna byter varken grad,
register, ankare eller offset.

| Mätpunkt (ps = 0, `?preview=split`) | Målvärde |
|---|---|
| `.tag--after` `getBoundingClientRect().right` | ≤ `innerWidth − 8` px vid 320, 375, 390, 414, 639 |
| `.tag--before` `getBoundingClientRect().left` | ≥ `8` px vid samma fem bredder |
| Antal tecken i den renderade raden under `Efter` | **39**, ordagrant, vid varje bredd |
| Radernas antal i `.tag--after` under 640 px | ≤ **3** |
| Etikettblockets underkant → bandets överkant | ≥ **10** px, oförändrat (plan 001) |
| Etiketternas offset från sömmen | `12` px under 640, `20` px vid ≥ 640, **oförändrat** |
| Grad, vikt, `letter-spacing`, färg | **oförändrade** |

Samma tre kontroller ska hålla vid ps = 0,42 och ps = 1,0, alltså när sömmen har
flyttat sig: en etikett som ryms vid folden men spiller mitt i akten är inte löst.

Riktningen, inte receptet: den tillgängliga bredden på `efter`-sidan är
`(1 − --split)·100% − 2 × offset`, och på `före`-sidan `--split·100% − 2 × offset`.
Väljer du i stället att låta wrappern spänna sidan och etiketten fylla den, är
det lika bra — det som mäts är talen ovan.

## Repo conventions to follow

- `--split-start` bor på **ett** ställe och läses av de fyra som behöver den
  (`@property` initial-value, `targetFrom()`, `--d`-normeringen, `MODES`).
  Lägg inte till en femte kopia av talet i en breddregel; läs `--split`.
- Mätta tal skrivs som en kommentar bredvid regeln, i samma stil som
  `index.html:411`.
- Etiketterna är underkantsankrade mot bandet sedan plan 001 (mätt: 22 px
  överlapp vid 320 med toppankring). Behåll ankringen.
- Motorn och `sc-smooth.js` rörs aldrig.

## Steps

1. Mät och skriv ut `getBoundingClientRect().right` för `.tag--after` och
   `.left` för `.tag--before` vid 320, 375, 390, 414 och 639, vid ps = 0.
   Det är utgångsläget och det ska stå i `NOTES.md` bredvid utfallet.
2. Byt breddregeln så att båda etiketterna härleds ur `--split`.
3. Mät om de tio talen. Alla ska klara § Target.
4. Upprepa mätningen vid ps = 0,42 och ps = 1,0.
5. Räkna tecknen i den renderade raden under `Efter` vid varje bredd:
   `textContent.trim().length === 39` och `scrollWidth === clientWidth` på
   radens egen låda.
6. Skriv in ändringen och talen i `NOTES.md`, och en rad i `BRIEF.md` §
   decision ledger med `PRODUCT.md` § Låst copy som Source rule.

## Boundaries

- Korta INTE strängen, förkorta inte, sätt inte `text-overflow: ellipsis`, lägg
  inte till `title=` som ersättning för synlig text.
- Sänk INTE graden, ändra inte `letter-spacing`, byt inte snitt och ändra inte
  färgen för att vinna plats. Det är bredden som är fel, inte typen.
- Ändra INTE etiketternas offset från sömmen (12 / 20 px).
- Ändra INTE `--split-start`. Sömmens läge är avgjort i plan 003 och prövat mot
  pixlar; den här planen rör bara etiketterna.
- Rör INTE `sites/calyx.html` eller `sites/before-ai-slop.html`.
- Lägg INTE till en bakgrundsplatta, en ram eller en toning bakom etiketten för
  att göra den läsbar. Etiketterna står på papperet.

## Verification

- **Mekaniskt**:
  - De tio måtten i § Target vid ps = 0, plus samma vid ps = 0,42 och 1,0.
  - Teckenräkningen i steg 5: `39` vid alla fem bredder.
  - Överflödessvep vid 320, 375, 390, 414, 768, 1440: `scrollWidth == clientWidth`.
  - `motion_probe` på `--sc-ps` och `--split`, hjul `20:120`: oförändrat mot
    R3 (`max_step 0,86 %` respektive `1,62 %`, `staircase 0`).
- **Feel check**: ladda vid 390 × 844 och vid 320 × 568 och läs i pixlar:
  - hela raden `Exempelsida: Calyx, florist i Stockholm` syns, sista tecknet med
    luft till vyportens kant;
  - `Före`-etiketten står kvar högerställd mot sömnen med sin egen luft åt vänster;
  - de två etiketterna läser fortfarande som ett par, med samma avstånd till
    sömmen på var sin sida;
  - båda står minst 10 px fritt från bandet de namnger.
- **Done when**: skärmbilder vid 320 och 390 vid ps = 0 visar båda etiketterna
  hela, teckenräkningen `39` står i `NOTES.md`, och de tio måtten är utskrivna.
