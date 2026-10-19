# 037 · `?preview=process-0N` siktar om efter `load` och `fonts.ready`: det formade läget, inte ett läge från före typsnitten

- **Status**: TODO (R9, loop 3)
- **Commit**: R8-läget av `runs/V3c/index.html`, md5 `70214a22`
- **Severity**: HIGH (funktionsfel i det läge alla ramsekvenser, Astra-granskningar och F-007 mäter mot; H-30 faller vid 390 i preview 01 och vid 1440 i preview 02)
- **Category**: Funktion (lifecycle), H-30; Astra loop 3 fix 5, verifierad med mätning
- **Estimated scope**: 1 fil, ~10 rader JS (en funktion, två extra anrop)
- **Källor**: loop 3 `shots/loop-3/preview_check.json` (talen nedan), `preview/preview-1440-process-01.png` (glyfen delvis ritad), `preview-390-process-01.png` (glyfen delvis ritad), `preview-1440-process-02.png` (måttlinjen `#p-dim-width` saknas); Astra loop 3 bild 42, 43, 54, 55

## Problem

Previewkoden (rad 1858 till 1868) räknar målscrollen **en gång vid skripttid**: `measureAct()`
→ `stepAnchors[pi].yc` → `scrollTo(processTop + yc − vh/2)` (390: `y0 − sheetH`). Sedan
kommer `load` och `document.fonts.ready`, som båda dispatchar `resize` (rad 1529 till 1531)
→ `measureAct()` mäter om `--sN`/`--eN` med **de riktiga typsnittens** radbrytning, och
prosan i steg 01 växer eller krymper, så li 02 till 07 flyttar sig. Scrollpositionen står
kvar där den var, men fönstret den skulle träffa har flyttat sig:

| läge | scrollY | `--sc-ps` på `#process` efter 2 s | `--eN` | `--kN` | banor |
|---|---|---|---|---|---|
| 1440 process-01 | 5 489 | 0,2234 | 0,2232 | 1 | `#p-outline` 0, `#p-glyph` 0 (formad) |
| 1440 process-02 | 5 942 | 0,2566 | **0,3199** | **0,19** | `#p-dim-width` 1px (oritad), `#p-guides` 42 % |
| 390 process-01 | 6 723 → **6 461** efter relayout | 0,1894 | 0,2450 | **0,67** | `#p-glyph` 0,59 (delvis) |
| 390 process-02 | 6 865 | 0,3310 | 0,3311 | 1 | formad |

(`preview_check.py`, R8-läget; vid 390 flyttade dessutom själva scrollpositionen 262 px
när `plansch()`/typsnitten lade om arkets höjd, webbläsarens scroll anchoring.) Preview 01
vid 1440 råkar hålla eftersom li 01 ligger först och inte flyttas av sin egen prosa.

R8:s kontroll ("`on`-listan capped vid N, `#p-outline`/`#p-glyph` 0px i alla previews")
mätte steg 01:s banor i alla lägen, inte steg N:s egna `--kN`; därför syntes inte felet.

```js
/* index.html:1858-1868 - current: en gång, vid skripttid */
  if (mode && /^process-0[1-7]$/.test(mode) && process){
    var pi = parseInt(mode.slice(-2), 10) - 1;
    measureAct();
    ...
    window.scrollTo(0, processTop + target);
  }
```

## Target

Målscrollen räknas i en funktion `aimPreview()` som anropas vid skripttid **och** efter
varje ommätning: på `load` och på `document.fonts.ready`, efter `measureAct()` (samma
ordning som `relayout` → `measureAct` i dag: registrera `aimPreview` sist på båda
händelserna). Med `__scFreezeMotion` satt adopterar shimen råvärdet exakt, så en andra
`scrollTo` ger det formade läget utan lerp.

```js
/* target */
  function aimPreview(){
    if (!(mode && /^process-0[1-7]$/.test(mode) && process)) return;
    var pi = parseInt(mode.slice(-2), 10) - 1;
    measureAct();
    var mobilePrev = window.matchMedia('(max-width:1279px)').matches;
    var stickEl = process.querySelector('.process-stick');
    var sheetHPrev = mobilePrev && stickEl ? stickEl.getBoundingClientRect().height : 0;
    var target = mobilePrev ? stepAnchors[pi].y0 - sheetHPrev : stepAnchors[pi].yc - window.innerHeight / 2;
    window.scrollTo(0, processTop + target);
  }
  aimPreview();
  addEventListener('load', aimPreview);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(aimPreview);
```

## Repo conventions to follow

- `__scFreezeMotion` sätts som i dag (rad 1826); `previewFace` rörs inte.
- `measureAct()` är den enda mätaren av `--sN`/`--eN` (034 A: gridets överkant, inte sticky-rect).
- Ledgerrad i `BRIEF.md` § Byggarens rader, R9: "Previewlägena siktar om efter load och fonts.ready".

## Steps

1. Bryt ut blocket på rad 1858 till 1868 till `aimPreview()` enligt Target; anropa vid skripttid, på `load` och på `fonts.ready` (efter `relayout`-registreringarna på rad 1530 till 1531, så att `measureAct` redan körts när `aimPreview` kör; `aimPreview` anropar ändå `measureAct()` själv).
2. Mät (scratch `preview_check.py`, båda bredderna, N = 1 till 7, `wait_until="load"` + 2 s): `--sc-ps` på `#process` ≥ `--eN` och < `--s(N+1)`; `--kN` = 1 (uträknat); steg N:s sista bana (`#p-glyph` för 01, `#p-stations` för 02, `#p-lead-169` för 03, `#p-dim-row` för 04, `#p-live-img`/`#p-opening`-maskningen för 05, tonbytet `--k6` = 1 för 06, `#p-rev` för 07) `stroke-dashoffset: 0px`; `data-on` bara på 01 till N.
3. Previews i båda riktningarna (R8 § 2 punkt 8, som inte kördes): samma sida, scrolla från toppen in i `?preview=process-03`:s scrollY och från botten till samma: `--k3` = 1 båda gångerna.

## Boundaries

- Inget annat i previewkoden ändras (`front|mid|back|ledger|bleed` orörda).
- Matchar inte rad 1858 till 1868 eller 1529 till 1531: STOPPA.

## Verification

- **Mekaniskt:** steg 2 (28 kombinationer), steg 3.
- **Skärmbild:** `?preview=process-01` vid 1440 och 390 (`load` + 2 s): ramen och glyfen helt ritade (målbild `shots/r8/preview-process-05-1440.png`:s ram + glyf, i tomt ark); `?preview=process-02` vid 1440: hjälplinjer, måttlinjen `320 … 1440`:s bas (`#p-dim-width`) och stationerna ritade.
- **Feel check:** inget att känna; previews är stillbilder.
- **Done when:** H-30 bockad med tabellen; R8 § 2 punkt 8 körd i båda riktningarna.
