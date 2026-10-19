# 016 · Kortbaksidans högra halva: ordmärkets A-glyf i hårlinje

- **Status**: TODO (R7, loop 1; radhänvisningar uppdaterade av arkitekten 2026-09-17 mot R6-läget)
- **Commit**: R6-läget av `runs/V3c/index.html`, md5 `424cdd46` (boardkopian `27b7db6d` är R4-läget och gäller inte längre)
- **Severity**: MEDIUM
- **Category**: Physicality (kortets två sidor), T-4, H-09
- **Estimated scope**: 1 fil, ~8 rader CSS, 1 SVG-element (path finns redan i filen)

## Problem

Baksidans innehåll fyller vänstra ~45 % och övre ~60 % av kortet; högra halvan och nedre
40 % är tom matt svart (`shots/fasA/v3c-preview/v3c-1440-back--fold.png`,
`v3c-flip/v3c-1440-flip-11-100.png`). Squint läser ett halvt tomt kort. Öppen fråga sedan
R2 och R3 utan dom; domen är nu: fyll högra halvan med samma objekt som framsidan bär,
ordmärkets A-glyf, men som kontur.

```css
/* index.html:399 - current */
  .face--back{transform:rotateY(180deg);background:var(--c-black);}
/* index.html:441-443 - current */
  .card-back{position:absolute;inset:0;display:flex;flex-direction:column;
    align-items:flex-start;justify-content:center;gap:0;
    padding:clamp(20px,5cqw,56px);}
```

Framsidans glyf: `index.html:986`, `<svg viewBox="80 400 827 1139" …><path fill="#ffffff" … d="M 430.020 513.250 …"/></svg>` (inline i `.logo-dock`).

## Target

Samma path, ritad som hårlinjekontur i `--frame-line`, 60 % av korthöjden, högerställd,
bakom texten i z-ordning, `aria-hidden`. Fylld fram, kontur bak: samma objekt, två sidor.
Ritad form, inte innehåll (gate 47/79).

```css
/* target, efter index.html:443 */
  /* T-4: ordmärkets glyf som kontur på baksidan. Samma path som logo-docken (rad 986),
     stroke i stället för fill. 60 % av korthöjden vid 16:9; under 640 (4:5) 34 % i nedre
     högra hörnet så att den aldrig korsar textkolumnen. */
  .card-glyph{position:absolute;right:clamp(20px,5cqw,56px);top:20%;height:60%;width:auto;
    z-index:0;pointer-events:none;}
  .card-glyph path{fill:none;stroke:var(--frame-line);stroke-width:6;stroke-linejoin:miter;}
  .card-back{z-index:1;}
  @media (max-width:640px){
    .card-glyph{top:auto;bottom:clamp(16px,5cqw,24px);height:34%;}
  }
```

`stroke-width:6` i viewBox-enheter (1 139 höga): vid 60 % av 504 px = 302 px hög glyf är
skalan 0,265, alltså 1,6 px stroke; vid 390 (4:5, ~422 px kort, 34 % = 143 px) 0,75 px.

```html
<!-- target, index.html:995-996: första barnet i .face--back, före .card-back -->
          <div class="face face--back" id="faceBack">
            <svg class="card-glyph" viewBox="80 400 827 1139" aria-hidden="true" focusable="false"><path d="M 430.020 513.250 … (identisk med rad 986)"/></svg>
            <div class="card-back">
```

Geometri vid 1440 (kort 896 x 504): glyf 302 hög, 219 bred, x från 621 till 840; textkolumnen
slutar vid ~400 (`card-mark` 80,6 px "ALUNIX"). Ingen överlappning. Vid 390 (kort ~338 x 422):
glyf 143 hög, 104 bred, x 214 till 318, y 255 till 398; textblocket är vertikalt centrerat
(~y 110 till 310) med `card-cta` som understa rad vid x 20 till ~140. Överlapp mäts i steg 4.

## Repo conventions to follow

- Pathen finns redan inline (rad 986, `#alunix-mark-path`) och som `#p-glyph` i processarket (rad 1252); kopiera `d` ordagrant, ingen ny
  asset (PRODUCT.md: logotypen får läggas inline).
- `--frame-line` (rad 137) är plåtens hårlinje och den enda kanten kortet har; glyfen delar
  den.
- `backface-visibility:hidden` på `.face` (rad 391) gäller glyfen som barn: den syns bara när
  baksidan är vänd fram.
- Ledgerrad finns: `BRIEF.md` § Arkitektens rader, "Kortbaksidans högra halva".

## Steps

1. Lägg CSS-blocket efter rad 443.
2. Lägg `<svg class="card-glyph">` före `.card-back` (rad 996), `d` kopierad från rad 986.
3. Kontrollera att `faceBack.inert` (`setFace`, rad 1406-1412) fortfarande gäller hela baksidan; glyfen är
   `aria-hidden` och `pointer-events:none`.
4. Mät överlapp vid 390x844 och 320x568 vid `?preview=back`: `getBoundingClientRect()` på
   `.card-glyph` mot `.card-mark`, `.card-services`, `.card-cta`; skärningsarea 0. Är den
   inte 0: sänk `height` till 28 % och mät om; skriv talen i NOTES.md.

## Boundaries

- Rör inte `.card-back`s innehåll, ordning eller typografi (plan 006 äger kickern).
- Ingen fill, ingen opacitet-animation: glyfen är statisk på kortet och vänds med det.
- Matchar inte raderna 399, 441-443, 986 eller 995-996: STOPPA.
- Loop 1 (2026-09-17): `preview/preview-1440-back.png` och `preview-390-back.png` bekräftar utgångsläget (högra halvan och nedre 40 % tomma); kortet är 896x504 vid 1440 och 324x405 vid 390 (`diag.json`, flip 1).

## Verification

- **Mekaniskt:** `contrast.py` på `.card-mark`, `.card-kicker`, `.card-services`, `.card-cta` mot `.face--back` oförändrat ≥ 4,5:1 (glyfen ligger inte under texten); `a11y_scan.py` 0 violations; `motion_probe.py --track ".plate-card:transform" --cpu 4`: p95 och rutor > 33 ms oförändrade mot en körning före ändringen (glyfen är ett statiskt SVG-barn på ett kompositerat lager).
- **Skärmbild:** `?preview=back` vid 1440 och 390 som bild: glyfen fyller högra halvan, texten orörd; `?preview=mid`: bara hårlinjen, glyfen syns inte (backface). Tolvstegs flip-sekvens: glyfen dyker upp med baksidan, inte före.
- **Done when:** H-09 bockad (innehåll eller ritad form på ≥ 60 % av bredd och höjd), överlapp 0 vid 390 och 320.
