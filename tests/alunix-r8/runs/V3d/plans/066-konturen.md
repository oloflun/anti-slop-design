# Plan 066 — konturen sluter sig om arket (Astra r21, material_fixes 1–2)

Två fynd, båda i `.tes-plane`s kontur. Inget annat rörs. Motorn, `scrollcraft.css` och
`sites/*` rörs aldrig.

## Fynd 1 — konturen är två vågräta streck, inte en rektangel

`box-shadow:inset` (`index.html:1189–1190`) målar vid `.tes-plane`s **egen border-box**
(x −5…vw+5), inte vid den `clip-path`-klippta synliga rektangeln — `clip-path` klipper bort
skuggans sidor i stället för att flytta dem. Kommentaren rad 1185–1188 hävdar motsatsen och
rättas i samma steg.

**Fix:** ett `::after` på `.tes-plane`, positionerat med `inset` som interpolerar med
SAMMA `--tx`-klocka och SAMMA `--pl-t/--pl-r/--pl-l`-tal som `clip-path` redan använder
(botten alltid 0, som planet självt), med `border` i stället för `box-shadow` så konturen
sitter på det INRE elementets egen krympande box, inte på det yttre elementets fasta box.
Ingen ny scroll-lyssnare, ingen JS-tillståndsmaskin.

| Target | Mätvärde | Mål |
|---|---|---|
| T1 | 2px ljus kolumn i PNG vid planets klippta vänster-/högerkant, `?preview=tes-till-ritning-2` och `-3`, 1920/1440/390 | inom ±1px |

## Fynd 2 — slutrektangeln landar +5 / −6px fel

`--pl-r = window.innerWidth − x4` och `--pl-l = x1` (`index.html:2538–2539`) mäter mot
`clientWidth`, men `.tes-plane` är CSS `100vw` (inkluderar rullningslistens bredd) och
`translateX(-50%)`-centrerad — dess EGEN vänsterkant sitter vid `-scrollbarWidth/2`, inte 0.

**Fix:** läs `.tes-plane`s egen `getBoundingClientRect()` en gång i `measureAct` och räkna
`--pl-l`/`--pl-r` mot DEN boxens kanter, inte mot `window.innerWidth`.

| Target | Mätvärde | Mål |
|---|---|---|
| T2 | `sideGapLeft`/`sideGapRight` vid `tes-till-ritning-4`, klippt kant mot `--x1`/`--x4`, 1920/1440/390 | ≤1px |

## Ordning

Fix 2 först (geometrin måste stämma innan konturen läggs ovanpå den), sedan fix 1. Verifiera
båda mot `plane21.py`-motsvarigheten (Astras skript i `shots/astra-r21/`, återanvänt) som
regressionsvakt: 0 träffar av text i/bakom konturen, `position:absolute` i varje bildruta,
`fixed` aldrig.
