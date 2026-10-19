# 002 — Den låsta bildtexten får inte klippas av arkets kant

- **Status**: TODO
- **Commit**: b2e1ecd
- **Severity**: HIGH
- **Category**: funktionsfel (låst copy renderad ofullständig, s4 vid 390)
- **Estimated scope**: 1 fil (`tests/alunix-r8/runs/K3/index.html`), ett element

## Problem

`Exempelsida: Calyx, florist i Stockholm` står i `PRODUCT.md` § Låst copy och
bevaras ordagrant. Vid 390 klipps den av arkets högerkant och renderas
`Exempelsida: Calyx, florist i Stockh` — läst som pixlar i
`tests/alunix-r8/review/r2/K3-filled-390.png` och i
`runs/K3/shots/r2/drawn-390.png`.

`PROTOCOL.md` § Vad som stoppar en runda listar *"ändrad ordagrann Alunix-copy"*.
En rad som renderas ofullständig är samma fel sett av besökaren: hen kan inte
läsa den låsta raden. Med Martian Mono, som är bredare än fallback-monon i
skärmbilderna, blir klippet större, inte mindre.

Byggaren mätte felet och föreslog fixen (`NOTES.md` § Öppet efter R2, punkt 5);
den här planen sätter målvärdet och gränserna.

Nuvarande kod:

```html
<!-- tests/alunix-r8/runs/K3/index.html:655 — current -->
<text id="c-calyx" class="callout" x="480" y="759" text-anchor="start">Exempelsida: Calyx, florist i Stockholm</text>
```

```js
/* :747 — current, utropets plats per plansch */
'c-calyx': [480, 759, 12, 324],
```

Raden behöver ungefär 290 user units i fallback-monon; planschen är 320 bred och
raden börjar vid x = 12, alltså 302 tillgängliga units minus arkets egen marginal.

## Target

Raden passas in i sitt utrymme med `textLength`, vilket är ritpraxis för ett
utrop och inte en ny typinställning. Ingen bokstav tas bort, ingen förkortning
införs, ingen radbrytning läggs till.

| Storhet | Målvärde |
|---|---|
| `textLength` på `#c-calyx` i den reducerade planschen | `296` user units |
| `lengthAdjust` | `spacingAndGlyphs` |
| Vänsterkant | `x = 12`, oförändrat |
| Högerkant efter inpassning | ≤ `308`, alltså minst 12 units innanför arkets kant |
| Renderad radlängd vid 390 CSS-px | ≤ `375 px`, mätt med `getBBox()` |
| Antal tecken | 39, oförändrat, ordagrant |

```html
<!-- target: attributen sätts i samma JS-funktion som redan flyttar utropen
     per plansch, eftersom textLength är ett presentationsattribut och inte
     en CSS-egenskap på <text> — samma orsak som x och y (index.html:385). -->
<text id="c-calyx" class="callout" x="12" y="324"
      textLength="296" lengthAdjust="spacingAndGlyphs">Exempelsida: Calyx, florist i Stockholm</text>
```

`textLength` får **bara** sättas i den reducerade planschen. På 1440 ligger raden
på x = 480 med gott om plats och ska ha samma spärr som resten av utropen.

## Repo conventions to follow

- Utropens plats per plansch sätts som attribut i JS, i tabellen på
  `index.html:739`–`750`, eftersom `x` och `y` är presentationsattribut på
  `<text>` och en CSS-regel mot dem ignoreras tyst. `textLength` och
  `lengthAdjust` hör till samma familj och sätts i samma funktion.
- Utökade tabellrader kommenteras med det mätta talet, i samma stil som
  `index.html:646`–`648`.
- Talet ska mätas efter att `assets/martian-mono-var.woff2` landat, inte mot
  fallback-monon. Står filen fortfarande som `[needs: vendor]`: sätt `296`, mät
  om när filen finns, och skriv en rad i `NOTES.md` om att talet är preliminärt.

## Steps

1. Lägg `textLength` och `lengthAdjust` i utropstabellen (`index.html:739`) som
   två extra fält, satta bara för den reducerade planschen.
2. Sätt attributen i samma funktion som byter `viewBox` och flyttar utropen, och
   **ta bort dem** när planschen växlar tillbaka till 1440-geometrin.
3. Mät den renderade radlängden med `getBBox().width` vid 390 och skriv ut talet
   i `NOTES.md`.
4. Kontrollera samma rad för de två andra låsta bildtexterna när a3 byggs i R3
   (`Exempelsida: Hōrai, Asian fusion-koncept`,
   `Exempelsida: Hyperborea, konferens i Lund`) och skriv in det som en rad i
   `NOTES.md` så att R3 inte upptäcker samma sak tre gånger.

## Boundaries

- Korta ALDRIG raden, byt inget ord, ta inte bort `Exempelsida: `, och bryt den
  inte till två rader. Den är låst copy.
- Sänk INTE utropets grad under 12 px. Utropsregistret är en av sidans få
  typnivåer och ett undantag i ett hörn blir en fjärde nivå.
- Använd INTE `textLength` någon annanstans på sidan. Ett utrop som passas in i
  sitt utrymme är ritpraxis; en sida där all typ passas in är en sida utan
  typografi.
- Rör INTE `PRODUCT.md`.

## Verification

- **Mekaniskt**:
  - `node scripts/detect.mjs --json` mot filen: inga nya träffar.
  - En `getBBox().width`-avläsning vid 390 skriven i `NOTES.md`, ≤ 375 px.
  - Sträng-kontroll: `grep -c "Exempelsida: Calyx, florist i Stockholm" index.html` ger 1, och strängen är oförändrad byte för byte.
- **Feel check**: ladda `?preview=filled` vid 390 × 844 och 320 × 568 och läs raden i pixlar:
  - hela raden syns, sista bokstaven är `m` i `Stockholm`, och det finns luft mellan raden och arkets kant;
  - raden ser fortfarande ut som ett utrop i samma mono-register som `16:9` och `fold`, inte som en hoptryckt eller utdragen rad;
  - raden tonar in på samma ställe i akten som förut.
- **Done when**: skärmbilder vid 320 och 390 visar hela den låsta raden, och det mätta `getBBox`-talet står i `NOTES.md`.
