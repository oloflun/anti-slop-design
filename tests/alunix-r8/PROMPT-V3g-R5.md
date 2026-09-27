Alunix {{KONCEPT}}, runda 5 (smal). Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}. Samma regler: bara
headless, en webbläsare i taget, EFFECTS.md skyddad, ingen commit.

Leadens mätning av runda 4 med `tests/alunix-r8/click_scroll_probe.py` (skriver nu också vilken
bildruta som är längst), tre körningar:
- scrollkurvan är mjuk: 15 px efter 300 ms, framme efter 1,4 s. Bra;
- men **en bildruta tar 470–536 ms**, 400–800 ms efter klicket, och scrollen hoppar 280–650 px
  i den bildrutan. Det är det enda som gör övergången hård nu.

Trolig orsak, som du ska bekräfta mätt och inte gissat: Hōrais dokument har legat som
`display:none` och läggs ut och målas för första gången när det visas. `measureCase` läser sedan
ankarpositioner i det dokumentet och tvingar fram layouten synkront, mitt i scrollen.

Gör så här:
1. Mät först vad bildrutan innehåller. Använd CDP-tracing (`page.context.new_cdp_session` +
   `Tracing.start` med devtools.timeline) runt klicket, headless. Ange de tre största posterna
   (Layout, Paint, Script eller Decode, och i vilket dokument).
2. Rättning: efter förladdningen ska **båda** iframarna vara utlagda, målade och mätta **innan**
   något klick.
   - Den inaktiva ligger kvar i ramen med `visibility:hidden` eller `opacity:0` och
     `pointer-events:none`, aldrig `display:none`.
   - `measureCase` körs för båda i `load` + `document.fonts.ready` i iframen, och om vid resize.
   - Ett klick får bara skriva opacity/visibility och byta aktuellt case. Inga layoutläsningar.
   - Samma princip gäller panelen till höger. Den inaktiva panelen får inte ligga som
     `display:none` om det kostar layout vid bytet. Mät det.
3. **Krav:** ingen bildruta över 50 ms från klick till framkomst, i tre körningar av
   click_scroll_probe. Största steg ≤ 60 px. `section_probe` ska vara oförändrat grönt: 1 laddning
   per iframe, 0 refreshar, alla sektioner ≤ baslinjen `{{UT_MAPP}}/shots/lead-section-r4-1.json`.
4. Kontrollera att inget annat försämrats: mobil 390 med showcase_probe med bilder, läs
   `sheet.png`.

Skriv en R5-sektion i `RAPPORT.md` med tracing-fyndet, fixen och siffrorna före och efter.
