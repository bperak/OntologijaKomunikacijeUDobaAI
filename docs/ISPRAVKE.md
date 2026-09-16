# ISPRAVKE — evidencija ispravljenih tvrdnji

Ova datoteka vodi **svaku tvrdnju koja je iznesena javno, a kasnije se pokazala netočnom ili nepotpunom**.
Pravilo knjige: pogreška se ne briše — bilježi se (što je pisalo, što je točno, odakle to znamo, gdje je ispravljeno).
Datum u zagradi = datum provjere na primarnom izvoru.

---

## ISPRAVAK-001 · 14. 9. 2026. · METR-ov vremenski horizont

- **Pisalo je:** METR-ov vremenski horizont za frontier model u veljači 2026. iznosi ~13–14,5 h. (izlaganje IUC Dubrovnik, 11. 9. 2026., slajd 16)
- **Točno je:** prvotna METR-ova procjena za **Claude Opus 4.6** (20. 2. 2026.) bila je **~14,5 h**, ali je METR **3. 3. 2026. ispravio bug** u svom modeliranju i vrijednost spustio na **~12 h**.
- **Uz to:** METR uz graf navodi: *„Measurements above 16 hrs are unreliable with our current task suite."* **Claude Mythos** (ožujak 2026.) ocijenjen je na **16+ h** — što je gornja granica skupa zadataka, a ne novi plato.
- **Izvor:** METR (2025), arXiv:2503.14499 (NeurIPS 2025); METR-ova napomena uz graf (2026.); A. Cotra (METR), *I underestimated AI capabilities (again)*, 3. 3. 2026.
- **Posljedica za tekst:** horizont se navodi kao **~12 h (nakon ispravka, 3. 3. 2026.)**, a svako navođenje brojke iznad 16 h mora nositi napomenu o nepouzdanosti mjerenja.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`metr_horizon_2026`, novi `metr_unreliable_above`)

## ISPRAVAK-002 · 14. 9. 2026. · Strop GPQA

- **Pisalo je:** strop GPQA („nesporno točni" odgovori) ≈ **90 %**. (izlaganje, slajd 17)
- **Točno je:** strop je **~80 %** (zavisi od podskupa); GPQA je **zasićen 11/2025** (Gemini 3 Pro @ 93,8 %), a **Anthropic ga prestaje izvještavati od 6/2026**.
- **Izvor:** A. D. Thompson, *Mapping IQ, MMLU, MMLU-Pro, GPQA, HLE*, LifeArchitect.ai (ažurirano 4. 8. 2026.); Rein et al. (2023), arXiv:2311.12022.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina H) · `data/fakti.csv` (`gpqa_ceiling` = 80, uz novi `mmlu_ceiling` 91 i `mmlu_pro_ceiling` 90 za kontekst)

## ISPRAVAK-003 · 14. 9. 2026. · Strop HLE (nepotpuna tvrdnja)

- **Pisalo je:** strop HLE = **25,6 %**. (izlaganje, slajd 17)
- **Nepotpuno je:** postoje **dva izvora s različitim vrijednostima** — **~51,3 %** (FutureHouse, 7/2025) i **25,6 %** (Alibaba, 2/2026, arXiv:2602.13964v2). HLE je **gotovo zasićen 12/2025** (GPT-5.2 @ 50 %).
- **Izvor:** Thompson (2026), *Mapping*; HLE (2026), *Nature* 649:1139–1146, DOI 10.1038/s41586-025-09962-4.
- **Posljedica za tekst:** nikad se ne navodi jedan strop kao jedini — navode se **oba, s izvorom i datumom**.
- **Ispravljeno u:** `referencije/REFERENCE_BASE.md` (skupina G) · `data/fakti.csv` (`hle_ceiling` = 51.3 + napomena o Alibabi)

---

## Zašto ovo postoji

Knjiga tvrdi da se razine razlučuju **po vrsti dokaza**, a ne po uvjerljivosti izvora. Ako autor ne bilježi vlastite ispravke, tvrdnja o razlučivanju razina nije vjerodostojna. Zato:

1. **Brojka bez datuma i vrste (mjereno / procjena) nije brojka.**
2. **Ako se dvije mjerne vrijednosti razilaze, navode se obje** — čitatelj dobiva stanje spora, ne autorov izbor.
3. **Ispravak se objavljuje, ne skriva.** Ova datoteka je javna.

## ISPRAVAK-004 — tekst izvan okvira na ploči `fig_omlcc_s1` i potpisi koji su citirali taj tekst

- **Što je pisalo:** na prvoj ploči ljestvice (`fig_omlcc_s1.png`) tekst zaglavlja nedovršenih
  domena glasio je „PSYCHOLOGICAL — reveal on the next click · mental facts · Searle 1995" i
  **prelazio je desni rub panela za 19 px** (tinta do x = 1888, panel do x = 1869). Potpisi
  slika 2.2 i 2.3 citirali su taj tekst („reveal on the next click").
- **Što je točno:** tekst je skraćen na „PSYCHOLOGICAL · mental facts · Searle 1995" (isto kao
  u otkrivenim pločama), pa prekoračenje iznosi **0 px** (mjereno: tinta do x = 1869 = rub
  panela). Nedovršene domene ostaju vidljive kao prigušeni stupci s brojevima 09–16.
- **Zašto je i sadržajno bolje:** „reveal on the next click" uputa je za predavanje (klik), a
  knjiga se ne klika — u tiskanoj slici takva uputa nema smisla.
- **Gdje je ispravljeno:** `figure/fig_omlcc_s1.png` (ponovno izrađeno iz
  `figure/izvori/fig_omlcc_stage.py`), potpisi slika 2.2 i 2.3 u `rukopis/poglavlje-02.md`.
- **Kako je nađeno:** neovisni vizualni pregled 19 figura (3 subagenta) + vlastito mjerenje
  tinte prema rubu panela. Ostalih 18 figura: bez prelijevanja i bez pokvarenih znakova.

## ISPRAVAK-005 — vlastiti pretvarač dijagrama spajao je razlomljene natpise u jedan red

- **Što je bilo:** alat `kod/mermaid_render.py` prevodio je Mermaidov `<foreignObject>` u SVG
  `<text>`, ali je **više redova natpisa spajao u jedan** — natpis je postao širi od kućice i
  tekst je izlazio iz okvira (uočio Benedikt na poslanim slikama).
- **Što je točno:** svaki `<p>` (i svaki `<br/>`) sada je **zaseban** `<text>` uz okomito
  centriranje; PNG za pregled traži se od poslužitelja (crta ga isti Chromium koji je mjerio
  okvire), a SVG za tisak ima ugrađenu sigurnosnu marginu od 8 %.
- **Dokaz:** alat `kod/check_figure_overflow.py` — mjeri prelijevanje pikselima i **provjeren je
  kontrolnim slikama** (tekst unutra → bez nalaza; preko desnoga ruba → nalaz; ispod ruba →
  nalaz; oznaka brida podalje → bez nalaza). Rezultat: 4/4 dijagrama čisto i u Chromiumovu i u
  tiskarskom putu (SVG → resvg).
- **Gdje je ispravljeno:** `kod/mermaid_render.py`, `figure/dijagram-*.svg|png`,
  novi alat `kod/check_figure_overflow.py`.

## ISPRAVAK-006 — iz natpisa dijagrama nestajale su strelice (→) i srednja točka (·)

- **Što je bilo:** filtar koji je iz Mermaid izvora uklanjao emoji bio je napisan kao popis
  **dopuštenih** raspona znakova; sve izvan njih se brisalo. Strelice (`→`, kategorija Sm),
  srednja točka (`·`, Po) i znak `×` (Sm) **nisu** bili u dopuštenome, pa je u dijagramu 13.1
  natpis „Čovjek → agent" ispao kao „Čovjek agent" — tvrdnja je promijenila smisao.
- **Što je točno:** filtar sada uklanja **samo prave emoji** (Unicode kategorija `So`),
  varijacijske selektore i nevidljive spojnike; interpunkcija, strelice i matematički znakovi
  ostaju. Provjera: u 13.1 sada stoje tri natpisa s `→`, u 12.1 dva s `·`.
- **Gdje je ispravljeno:** `kod/mermaid_render.py` (filtar `EMOJI`) i ponovno izrađeni
  `figure/dijagram-*.svg|png`.

## ISPRAVAK-007 — naslovi skupina preklapali su se s okvirima (13.1) i prekratki lomovi

- **Što je bilo:** u dijagramu 13.1 `subgraph` naslovi („Čovjek do agenta", „Agent do čovjeka",
  „Agent do agenta") **preklapali su se s okvirima** čvorova; u 12.1 i 12.4 natpisi su se lomili
  u 5–7 redaka, a slike su bile 4:1 stripovi — na 150 mm širine tekst bi ispao oko 5 pt.
- **Što je točno:** 13.1 više ne rabi `subgraph` (tri konfiguracije su čvorovi u mreži),
  12.4 je prebačen u uspravno stablo, lomovi natpisa kontroliraju se zapisom `%% wrap: N` u
  izvoru dijagrama. Izmjereno: tekst sada 8,5–17 pt na 150 mm (prije ~5 pt), bez stripova.
- **Kako je nađeno:** vlastitim pregledom slika nakon uključivanja `model.supports_vision`
  (→ ISPRAVAK-008); mjerilo prelijevanja te stvari **ne vidi** jer tekst nije izlazio iz okvira.

## ISPRAVAK-008 — Hermes je vision prosljeđivao lokalnom modelu iako glavni model ima vision

- **Što je bilo:** `auxiliary.vision` bio je postavljen na `custom:gemma4`
  (`gemma-4-26b-a4b-nvfp4`), a `model.supports_vision` nije bio deklariran — pa je svaki
  `vision_analyze` išao na lokalni Gemma 4 i vraćao **opis u tekstu**, umjesto da sliku priloži
  glavnome modelu. Posljedica: tri pogrešne prosudbe o figurama („pokvaren znak" = glava
  strelice) i prešućeni stvarni kvarovi (preklapanje naslova, nestale strelice).
- **Dokaz da glavni model ima vision:** slika poslana izravno na `deepseek-flash`
  (`/v1/chat/completions`, `image_url`) vraća točan odgovor („7391" i „donjoj").
- **Što je točno:** `hermes config set model.supports_vision true` (kopija configa:
  `config.yaml.prije-vision.bak`). Sada `vision_analyze` prilaže sliku izravno.
- **Napomena:** promjena vrijedi za nove sesije; u tekućoj je već stupila na snagu.
