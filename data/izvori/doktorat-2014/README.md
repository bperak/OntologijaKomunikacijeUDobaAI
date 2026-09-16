# Podaci izvuceni iz doktorskog rada (Perak 2014)

**Izvor:** Perak, B. (2014). *Opojmljivanje leksema strah u hrvatskome: sintaktičko-semantička analiza* (doktorski rad).
Filozofski fakultet Sveučilišta u Zagrebu. 474 str. PDF: https://github.com/bperak/doktorat-strah

**Metoda izvlačenja:** automatski, iz tekstualnog sloja PDF-a (PyMuPDF), uz normalizaciju naslijeđenog kodiranja
(č→ĉ, ć→Ċ, ž→ţ, š→ŝ u izvornom sloju). Skripta: `kod/izvuci_doktorat.py`. **Pomak stranica:** PDF stranica = tiskana + 24
(provjereno na trima uzorcima: PDF 269 → 245, PDF 328 → 304, PDF 393 → 369).

## Datoteke

| datoteka | sadržaj | redaka |
|---|---|---|
| `prijedlozne-konstrukcije.csv` | prijedložni izrazi s leksemom *strah* i brojem pojavnica (n) | 41 |
| `frekvencije-leksema.csv` | frekvencijske liste glagola i leksema uz *strah* | 49 |
| `emocije-nabrajanja.csv` | nabrajanja emocionalnih leksema u izvorniku (sirovi retci + izdvojeni leksemi) | 3 |
| `ishodisne-domene.csv` | parovi izraz + aktivirana ishodišna domena (iz tablica) | 50 |

## Ključne provjerene brojke (s izvornim stranicama)

| brojka | vrijednost | mjesto u izvorniku |
|---|---|---|
| korpus | Hrvatski nacionalni korpus, **131,8 Mw** | sažetak, str. 6 (PDF) |
| pojavnice leme *strah* | **14.875** | sažetak, str. 6 (PDF) |
| izraz *od straha* | **825** pojavnica (drugi po čestotnosti) | tiskana str. 304 |
| glagoli uz *od straha* | drhtati (62), umrijeti (61), tresti (39), trnuti (18), plakati (12), kriknuti (11), izbezumiti (10), bježati (9), razboljeti se (8), osloboditi (8), ukočiti (8) | tiskana str. 304 |
| konstrukcija s *miješati* | *miješati* (n=17), *prožeti* (n=6), *prodrijeti* (n=4) | tiskana str. 369 |

## Ograničenja (obavezno navesti u knjizi)

1. **Automatsko izvlačenje** može propustiti retke prelomljene preko stranica i tablice s višestupčanim slogom; svaka brojka koja ulazi u knjigu **provjerava se na navedenoj stranici** izvornika.
2. Kodiranje izvornika ima artefakte (npr. *iznenaćenje* mjesto *iznenađenje*); leksemi se u knjizi navode u normiranom obliku, a izvorni redak ostaje u CSV-u kao dokaz.
3. `ishodisne-domene.csv` je **parcijalan** popis (tablice su višestupčane) — koristi se kao ilustracija, ne kao potpun inventar.
4. Rad nije recenziran kao publikacija (doktorski rad); pri citiranju se navodi kao doktorski rad s mentorom i ustanovom.
