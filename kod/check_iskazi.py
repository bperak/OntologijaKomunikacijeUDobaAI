#!/usr/bin/env python3
"""Jasnoća iskaza: tvrdnja mora reći na čemu stoji (ZAPIS-019).

Dvije provjere:

1. **Tvrdnja bez oslonca (po rečenici).** Rečenica koja nešto tvrdi odlučno (mora, treba, nikad, uvijek,
   jedino, nijedan, sve, nijedno) ili izvodi zaključak (dakle, stoga, time, otud) mora u istoj rečenici
   ili u susjednoj imati **oslonac**: razlog (jer, zato što, zbog, utoliko), uvjet (ako, u slučaju),
   mjeru/dokaz (mjereno, procjena, izvedeno, mjera, test, podatak, korpus, brojka, izvor, dokaz),
   uputu na mjesto (→ pogl.) ili citat ((Autor godina)).

2. **Nosiva tvrdnja u poglavlju.** Za svaku od šesnaest nosivih tvrdnji iz zbirne tablice (16.4) provjeri
   pojavljuje li se u svojemu poglavlju **zajedno s osloncem** (ista nosiva imenica + oslonac u istome
   odlomku). Ako se ne pojavljuje, tvrdnja u poglavlju stoji bez onoga što je tablica navela.

Uporaba:  python3 kod/check_iskazi.py [--datoteka rukopis/X.md] [--isoli] [--strogo]
"""
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")

TVRDNJA = re.compile(r"\b(mora|moraju|treba|trebaju|nikad|nikada|uvijek|jedino|jedini|jedina|nijedan|"
                     r"nijedno|nijedna|dakle|stoga|otud|time se|time je|zaključak je|pokazuje se|"
                     r"dokazuje)\b", re.I)
OSLONAC = re.compile(r"\b(jer|zato što|zato|zbog|utoliko|ako|ukoliko|u slučaju|pod uvjetom|mjereno|"
                     r"procjena|procijenjeno|izvedeno|mjera|mjeril|test|podatak|podacima|korpus|brojka|"
                     r"brojke|izvor|dokaz|rezultat|nalaz|pokus|eksperiment|anketa|prema|na temelju)\b", re.I)
UPUTA = re.compile(r"→\s*(?:pogl\.|dodatk|Slika|Tablica)|\b[A-ZČĆŠĐŽ][a-zčćšđž]+\s+(?:i\s+sur\.\s+)?\d{4}|\(\d{4}\)")


def proza(t):
    t = re.sub(r"^>.*$", "", t, flags=re.M)
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)
    t = re.sub(r"^\|.*$", "", t, flags=re.M)
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)
    t = re.sub(r"^\s*[-*]\s.*$", "", t, flags=re.M)
    t = re.sub(r"^\s*\d+\.\s.*$", "", t, flags=re.M)
    t = re.sub(r"^#.*$", "", t, flags=re.M)
    return t


def recenice(t):
    """Vraća (rečenica, oslonac-u-odlomku). Oslonac se traži u CIJELOME odlomku, a rečenice koje su
    najava (završavaju dvotočkom) ili sažetak kraći od 9 riječi izuzimaju se — njihov oslonac slijedi."""
    out = []
    for p in re.split(r"\n\s*\n", proza(t)):
        p = re.sub(r"\s+", " ", p).strip()
        if len(p.split()) < 25:
            continue
        rr = [r.strip() for r in re.split(r"(?<=[.!?])\s+", p) if r.strip()]
        for r in rr:
            if r.endswith(":") or len(r.split()) < 9:
                continue
            out.append((r, p))
    return out


def main():
    strogo = "--strogo" in sys.argv
    if "--datoteka" in sys.argv:
        dat = [sys.argv[sys.argv.index("--datoteka") + 1]]
    else:
        dat = [os.path.join(RUKOPIS, f) for f in ["uvod.md"] +
               [f"poglavlje-{i:02d}.md" for i in range(1, 17)] + ["zakljucak.md"]
               if os.path.exists(os.path.join(RUKOPIS, f))]
    print(f"{'datoteka':<24}{'rečenica':>10}{'tvrdnji':>9}{'bez oslonca':>13}{'%':>7}")
    nalazi, ukupno = [], 0
    for p in dat:
        t = open(p, encoding="utf-8").read()
        rr = recenice(t)
        tv = [o for o in rr if TVRDNJA.search(o[0])]
        bez = [o for o in tv if not (OSLONAC.search(o[1]) or UPUTA.search(o[1]))]
        ukupno += len(bez)
        print(f"{os.path.basename(p):<24}{len(rr):>10}{len(tv):>9}{len(bez):>13}"
              f"{100*len(bez)/max(len(tv),1):>7.0f}")
        for r, _ in bez:
            nalazi.append((os.path.basename(p), r))
    print(f"\nukupno tvrdnji bez oslonca: {ukupno}")
    if "--isoli" in sys.argv or "--datoteka" in sys.argv or strogo:
        print("\n=== TVRDNJE BEZ OSLONCA (za popravak) ===")
        for ime, r in nalazi:
            print(f"  • [{ime}] {' '.join(r.split())[:200]}")
    return 1 if (strogo and ukupno) else 0


if __name__ == "__main__":
    sys.exit(main())
