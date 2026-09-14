# Mreža knjiga — kako tri knjige rade zajedno

**Svrha:** tri knjige nisu tri odvojena projekta, nego **jedna mreža s jasnom podjelom posla**. Ovaj dokument je ugovor o toj podjeli: što je čije, kako se međusobno citiraju i kako se linkovi ne raspadaju.

---

## 1. Tri čvora mreže i njihove uloge

| knjiga | pitanje na koje odgovara | vlasništvo (što je *kanonski* tamo) | status |
|---|---|---|---|
| **Komunikacija u doba umjetne inteligencije** (2025) | **ŠTO se dogodilo** | povijest komunikacijskih tehnologija · arhitektura i obuka LLM-a · promptanje, RAG, agentura · etički i društveni okvir | objavljena (ISBN 978-953-361-147-1) |
| **Data Science u kulturi** (u izradi) | **KAKO se mjeri** | podaci i FAIR · Python/Colab · pandas, statistika, vizualizacija · NLP, ugrađivanja, semantička pretraga, RAG u praksi · projektni i etički protokol | u izradi |
| **Razine i entiteti** (ova knjiga) | **GDJE to ontološki stoji** | sustavi i razine (OMLCC) · emergencija · jezik i komunikacija kao razine · vektorski prostor i model · novi entitet u sustavu · falsifikacijski program | radni rukopis v0.1 |

**Zašto podjela posla nije birokracija:** bez nje tri knjige ponavljaju isto (LLM osnove pojavljuju se u sve tri) i čitatelj ne zna gdje je što *konačno*. S njom svaka knjiga ima svoju razinu, a mreža daje put: **teorija → metoda → praksa**.

---

## 2. Pravilo vlasništva (jedno mjesto, mnogo uputa)

1. **Tema ima jednog vlasnika** — knjigu u kojoj je izložena najpotpunije (tablica gore).
2. Sve ostale knjige **ne objašnjavaju temu iznova**, nego upućuju: *„vidi: Perak 2025, pogl. 5"* ili *„pipeline je u Data Science u kulturi, pogl. 9"*.
3. **Izuzetak:** pojam koji je nužan za razumijevanje *ovog* teksta dobiva ovdje **jednu rečenicu** definicije i uputu — nikad više od jednog odlomka.
4. **Mjere i brojke** imaju vlasnika u `data/` (vidi točku 5) — nikad dvije verzije istog broja.
5. **Više od dva upućivanja po odjeljku = znak da je tekst prekratak** (objasni, ne upućuj).

---

## 3. Mreža pojmova: `pojmovnik/koncepti.yaml`

Jedan registar pojmova za sve tri knjige. Za svaki pojam: **id · naziv (HR/EN) · definicija (jedna rečenica) · kanonski izvor (knjiga + poglavlje) · srodni pojmovi · gdje se još pojavljuje**.

- Rječnik pojmova u svakoj knjizi **generira se** iz ovog registra (`kod/pojmovnik_build.py`) — ne piše se ručno tri puta.
- Kad se definicija promijeni, mijenja se **jednom**, a sve tri knjige dobiju istu.
- Skripta ispisuje i `pojmovnik/koncepti.csv` za provjeru (koji pojam gdje postoji).

## 4. Mreža uputa: pravilo sidra (anchor)

- Upute **nikad ne idu na broj stranice** (brojevi se mijenjaju izdanjem), nego na **stabilno sidro**:
  `https://github.com/bperak/OntologijaKomunikacijeUDobaAI/blob/main/rukopis/poglavlje-07.md#7-komunikacija-kao-razina-14--soccommunication`
- Za svaku knjigu postoji **kanonski URL** u `docs/CITIRANJE.md` i u `CITATION.cff`.
- U tekstu se koristi oznaka **↗** za uputu na drugu knjigu, **→** za uputu unutar iste knjige. Primjer:
  > *„Postupak izračuna je opisan u Data Science u kulturi (pogl. 9; ↗), a ovdje nas zanima što taj izračun ontološki znači (→ pogl. 10)."*

## 5. Mreža brojki: zajednička evidencija

Svaka brojka koja se pojavljuje u više knjiga mora biti u **jednoj evidenciji**: `data/fakti.csv` (brojka · izvor · datum · vrsta: *mjereno* ili *procjena* · poglavlja u kojima se navodi). Skripta `kod/check_fakti.py` upozorava ako knjiga navodi brojku koje nema u evidenciji ili ako se vrijednost razlikuje.

## 6. Automatska provjera mreže

- `kod/check_links.py` — provjerava da svaka uputa na drugu knjigu vodi na **postojeće sidro** i, uz `--http`, da URL odgovara (HEAD zahtjev).
- GitHub Action `.github/workflows/mreza.yml` — pokreće provjeru pri svakom commitu; **slomljena uputa ruši build**.

---

## 7. Što čitatelj dobiva (korist, ukratko)

| korist | kako se vidi |
|---|---|
| **jasan put** | jedan predgovor u svakoj knjizi: „kako čitati ovu knjigu uz druge dvije" (½ stranice) |
| **bez ponavljanja** | ista tema objašnjena jednom, ostalo su upute |
| **neproturječnost** | isti pojam = ista definicija; ista brojka = ista vrijednost |
| **citirana trojka** | svaka knjiga eksplicitno citira druge dvije (referenca u tekstu, ne samo u literaturi) → mreža citata i lakša vidljivost (CroRIS, Scholar) |
| **održivost** | „obnavljajuće knjige": jedna ispravka pojma ili brojke propagira se kroz sve tri |

## 8. Troškovi (pošteno)

| rizik | zaštita |
|---|---|
| upute se vremenom slome | automatska provjera u CI-u (točka 6) |
| tri knjige se počnu preklapati | pravilo vlasništva + revizija po poglavlju (točka 2) |
| previše uputa kvari čitanje | najviše 1–2 upute po odjeljku |
| vezanje uz verziju | sidra umjesto stranica; uz citat uvijek i verzija |

---

## 9. Iskrena napomena o granicama

Metafora „tri knjige su tri razine jedne mreže" je **heuristika za čitatelja**, ne tvrdnja ove knjige. Knjiga o ontološkim razinama ne smije vlastitu strukturu izdavati za dokaz svoje teorije — to bi bila kružna argumentacija. Mreža knjiga je *organizacijska odluka*; teorija se dokazuje u poglavljima 4, 6, 10, 14 i 16.
