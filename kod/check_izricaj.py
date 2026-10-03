#!/usr/bin/env python3
"""Izričaj: fraze koje ne tvrde ništa i pokazne zamjenice bez imenice (ZAPIS-022).

Autorova korekcija (3. 10. 2026.): „To nije jasno na što se odnosi i banalizira izričaj."
Povod je bila teza uvoda: „…preskače se ono što bi ih učinilo odlučivima — gdje to ontološki stoji?
Ova knjiga uzima to pitanje ozbiljno…"

Dvije provjere:

1. **FLOSKULE — fraza koja ne tvrdi ništa.** Popis izraza koji zvuče odlučno, a ne nose tvrdnju
   (uzeti ozbiljno, igra ključnu ulogu, na pragu…). Prag: 0 (iznimke se navode u `docs/ISPRAVKE.md`).

2. **POKAZNA ZAMJENICA U TVRDNJI.** Rečenica koja počinje pokaznom zamjenicom (To, Ovo, Ono, Time, Zato,
   Zbog toga, U tome…) ili je sadrži kao subjekt tvrdnje, a u prethodnoj rečenici nema imenice istoga roda
   koja bi joj bila antecedent — kandidat za „nije jasno na što se odnosi". Mjera je **sito**: ispisuje
   kandidate s kontekstom, presudu daje pregled.

Uporaba:  python3 kod/check_izricaj.py [--isoli] [--strogo]
"""
import glob
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")

FLOSKULE = [
    "uzeti ozbiljno", "uzima ozbiljno", "uzeti to ozbiljno", "shvatiti ozbiljno",
    "igra ključnu ulogu", "igraju ključnu ulogu", "ključna uloga", "od ključne važnosti",
    "nije slučajno", "nije ni čudo", "treba napomenuti", "važno je napomenuti", "vrijedi istaknuti",
    "na kraju krajeva", "u današnje vrijeme", "u današnjem svijetu", "mijenja pravila igre",
    "revolucionarno", "korak naprijed", "na pragu", "u suštini", "suštinski", "u srcu",
    "posve je jasno", "svima je jasno", "nema sumnje", "nesumnjivo je", "svakako treba",
    "duboko ukorijenjen", "tek je početak", "vrijeme će pokazati", "ostaje za vidjeti",
    "ne treba posebno isticati", "kao što svi znamo", "kao što je poznato",
]

POKAZNA = re.compile(r"^(To|Ovo|Ono|Time|Zato|Zbog toga|U tome|Pritom|Odatle|Otud|Iz toga)\b", re.I)
ZENSKI = re.compile(r"\b\w+(a|ost|ina|ija|nja|ska|čka)\b$")


def proza(t):
    t = re.sub(r"^>.*$", "", t, flags=re.M)
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)
    t = re.sub(r"^\|.*$", "", t, flags=re.M)
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)
    t = re.sub(r"^\s*[-*]\s.*$", "", t, flags=re.M)
    t = re.sub(r"^\s*\d+\.\s.*$", "", t, flags=re.M)
    return t


def recenice(t):
    out = []
    for p in re.split(r"\n\s*\n", proza(t)):
        p = re.sub(r"\s+", " ", p).strip()
        if len(p.split()) < 25:
            continue
        rr = [r.strip() for r in re.split(r"(?<=[.!?])\s+", p) if r.strip()]
        for i, r in enumerate(rr):
            out.append((r, rr[i - 1] if i else ""))
    return out


def datoteke():
    if "--datoteka" in sys.argv:
        return [sys.argv[sys.argv.index("--datoteka") + 1]]
    return ([os.path.join(RUKOPIS, f) for f in ["uvod.md"] +
             [f"poglavlje-{i:02d}.md" for i in range(1, 17)] + ["zakljucak.md"]] +
            [f for f in sorted(glob.glob(os.path.join(RUKOPIS, "dodaci/dodatak-*.md")))
             if os.path.basename(f)[8] not in ("B", "E", "G")])


def main():
    flos, pok = [], []
    print(f"{'datoteka':<40}{'floskule':>9}{'pokazna':>9}")
    for p in datoteke():
        t = open(p, encoding="utf-8").read()
        ime = os.path.basename(p)
        nf = 0
        for izraz in FLOSKULE:
            for m in re.finditer(re.escape(izraz), t, re.I):
                nf += 1
                flos.append((ime, izraz, " ".join(t[max(0, m.start() - 90):m.end() + 90].split())))
        np_ = 0
        IME = re.compile(r"\b[\wčćšđž]{4,}(?:a|e|i|o|u|ost|nost|ina|anje|enje|ija|logija|izam|stvo)\b", re.I)
        for r, preth in recenice(t):
            if POKAZNA.match(r) and len(r.split()) >= 9 and not IME.search(preth):
                np_ += 1
                pok.append((ime, r, preth))
        print(f"{ime:<40}{nf:>9}{np_:>9}")
    print(f"\nukupno floskula: {len(flos)} | pokaznih zamjenica u tvrdnjama (sito): {len(pok)}")
    if "--isoli" in sys.argv or "--strogo" in sys.argv:
        print("\n=== FLOSKULE ===")
        for ime, iz, k in flos:
            print(f"  • [{ime}] „{iz}\" … {k[:170]}")
        print("\n=== POKAZNA ZAMJENICA (prvih 40, za pregled) ===")
        for ime, r, preth in pok[:40]:
            print(f"  • [{ime}] {r[:150]}\n      ← {preth[:120]}")
    return 1 if ("--strogo" in sys.argv and len(flos)) else 0


if __name__ == "__main__":
    sys.exit(main())
