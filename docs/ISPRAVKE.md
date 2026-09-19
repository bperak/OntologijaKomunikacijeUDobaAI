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

## ISPRAVAK-009 — tri figure ispod tiskarske rezolucije zamijenjene vektorskim dijagramima

- **Što je bilo:** tri PNG figure bile su ispod granice za tisak (~1800 px za 150 mm pri 300 dpi):
  `fig_razine` (891 × 832), `fig_emerg_hijerarhija` (873 × 437), `fig_voda` (952 × 672). U tisku
  bi bile mutne, a skaliranje rastra ne pomaže.
- **Što je točno:** sve tri zamijenjene su **vektorskim dijagramima** (SVG + PNG ~2000 px):
  `dijagram-1-5-slojevi-stvarnosti` (Slika 1.2), `dijagram-3-3-emergentna-hijerarhija`
  (Slika 3.1) i `dijagram-3-4-voda` (Slika 3.2). Stare PNG datoteke **uklonjene** su iz repoa,
  a potpisi prepisani prema onome što se na novim slikama stvarno vidi (npr. Slika 1.2 sada
  nosi i zaglavlja ljestvica — Hartmann 1940 te Novikoff 1945 · Feibleman 1954 — kojih na
  staroj slici nije bilo, pa se nije znalo čija je koja ljestvica).
- **Napomena o kriteriju:** vektorski dijagram nema „rezoluciju"; mjerilo je sada **veličina
  teksta na stranici** (traženo ≥ 8 pt pri širini 150 mm). Izmjereno za sve dijagrame:
  8,2–28 pt.

## ISPRAVAK-010 — četiri nova dijagrama ondje gdje je tekst tražio sliku

- **Dodano:** Slika 4.2 (`dijagram-4-5-vrste-dokaza`, trijaža mjereno/procjena/izvedeno),
  Slika 7.1 (`dijagram-7-5-pet-uvjeta`, pet uvjeta komunikacijskoga čina), Slika 8.1
  (`dijagram-8-1-statusna-funkcija`, X broji kao Y u kontekstu C) i Slika 14.1
  (`dijagram-14-6-funkcionalno-intrinzicno`, funkcionalno i intrinzično po razinama 12–16).
- **Zašto:** to su mjesta na kojima čitatelj mora držati nekoliko odnosa istodobno (trijaža,
  pet kumulativnih uvjeta, tri mjesta formule, dvije vrste prisutnosti kroz pet razina) —
  upravo ondje slika radi posao koji rečenica radi sporije.
- **Provjera:** svaki dijagram pregledan je vizualno (`model.supports_vision` uključen) i
  izmjeren (`check_figure_overflow.py`); vrijednosti u Slici 14.1 prepisane su iz tablice 14.6.

## ISPRAVAK-011 — rukopis je o sebi tvrdio nešto netočno (pogl. 16)

- **Što je bilo:** na kraju 16. poglavlja, u bloku „Otvoreno za provjeru u ovoj datoteci", stajale su
  dvije tvrdnje koje su u međuvremenu postale netočne: (3) da poglavlje 9 **nema** odjeljak
  „Kako bismo znali da griješimo" i (4) da u rukopisu **nema** poglavlja 4 i 15, pa se upute na 4.x i
  15.x odnose na plan, a ne na tekst.
- **Što je točno (17. 9. 2026.):** poglavlje 9 **ima** taj odjeljak, a poglavlja 4 (7.113 riječi) i 15
  (6.488 riječi) **postoje** i dovršena su.
- **Kako je ispravljeno:** tvrdnje nisu obrisane nego prepisane kao **riješene stavke** s datumom, uz
  uputu na ovaj zapis. Razlog je isti kao i za sve ostale ispravke: pogreška se ne briše, jer brisanje
  skriva i samu činjenicu da je rukopis jedno vrijeme bio nepotpun.
- **Uz to:** `check_fakti.py --strict` upozorio je na brojku **300 dimenzija** (fastText cc.hr.300) u
  potpisu slike 10.2 koje nije bilo u evidenciji; dodan je zapis `fasttext_hr_dim` u `data/fakti.csv`.
  Alat `check_lit.py` proširen je tako da provjerava i dijelove rukopisa **bez** popisa literature
  (uvod, zaključak, predgovor, studija slučaja) — u smjeru citat → baza.

## ISPRAVAK-012 — bibliografski podaci provjereni na primarnim izvorima (17. 9. 2026.)

**Što je bilo:** baza referenci navodila je četiri protokola (MCP, A2A, AP2, x402) i šest izvještaja
(GreyNoise, Tenable, Chroma, Knight, t-SNE/UMAP, Perak & Ban Kirigin 2023) **bez punih bibliografskih
podataka**, s oznakom ❓. Uz to je popis literature poglavlja 5 sadržavao **„Perak 2018, 2019"** —
radove kojih nema (OMLCC je izlaganje 2017a; 2017b, kako stoji i u odjeljku K baze).

**Što je utvrđeno (provjereno na primarnim izvorima, ne preko posrednika):**

| jedinica | utvrđeno |
|---|---|
| Anthropic 2024 (MCP) | *Introducing the Model Context Protocol*, spec. rev. 2024-11-05, objavljeno 25. 11. 2024. |
| Google 2025 (A2A) | *Announcing the Agent2Agent Protocol (A2A)*, Google Developers Blog, 9. 4. 2025. |
| Google 2025 (AP2) | *Powering AI commerce with the new Agent Payments Protocol (AP2)*, Google Cloud Blog, 16. 9. 2025. |
| Coinbase 2025 (x402) | *Introducing x402*, Coinbase Developer Platform, 6. 5. 2025. |
| Knight 2025 | *Levels of Autonomy for AI Agents*, **autori Feng, McDonald i Zhang**, 25-15 Knight First Amend. Inst., 28. 7. 2025.; pet razina autonomije |
| Chroma 2025 | Hong, Troynikov i Huber, *Context Rot*, Chroma Technical Report, 14. 7. 2025. |
| GreyNoise 2026 | *Agents Gone Wild…*, 9. 9. 2026. (potvrđene i brojke: 395 organizacija, 440 instanci, 48 zemalja) |
| Tenable 2026 | Research Special Operations, *The Agentic AI threat cluster…*, 14. 8. 2026. |
| t-SNE | van der Maaten & Hinton 2008, *JMLR* 9(86): 2579–2605 |
| UMAP | McInnes, Healy i Melville 2018, arXiv:1802.03426 (DOI 10.48550/arXiv.1802.03426) |
| Perak & Ban Kirigin 2023 | *Natural Language Engineering* 29(3): 584–614, DOI 10.1017/S1351324922000274 (Crossref) |

**Što je ispravljeno u rukopisu:**
1. poglavlje 5 — popis literature: „Perak 2014, 2018, 2019, 2025, 2026" → **„Perak 2014 · Perak 2025 · Perak 2026 · Perak, OMLCC - izlaganja 2017a; 2017b"**;
2. poglavlje 10 — t-SNE i UMAP više se ne navode samo imenom: dodani su citati i oba rada u popis;
3. poglavlja 3, 6 i 4 — ukinute napomene da se „puni podaci preuzimaju iz autorove bibliografije" (podaci su sada u bazi);
4. poglavlja 12 i 14 — ❓ blokovi skraćeni: riješene stavke (bibliografije, Knight) premještene u „Zatvoreno", ostaju samo one koje nisu bibliografske (vrsta brojke; nalazi o odsutnosti).

**Što ostaje otvoreno:** tipološka replikacija ljestvice (pogl. 2), nalazi o odsutnosti (pogl. 11, 14, 15, 16) i Perak 2025 (naslov i izdanje iz autorove bibliografije).
