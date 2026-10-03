#!/usr/bin/env python3
"""Provjera uvođenja pojmova (ZAPIS-017).

Pojmovi se čitaju iz popisa „### Ključni pojmovi" svakoga poglavlja (knjiga sama kaže koji su joj
pojmovi važni). Za svaki se traži PRVA UPORABA u čitateljskom redu (uvod → predgovor → pogl. 1–16 →
zaključak) i uspoređuje s poglavljem koje ga uvodi. Ako se pojam rabi prije toga poglavlja, čitatelj ga
susreće prije objašnjenja — to je nalaz.

Poklapanje je strogo: cijeli pojam, dopušten je nastavak samo na POSLJEDNJOJ riječi (padež), a aparat
(popis ključnih pojmova, literatura, blok-citati, tablice, slike, kod) ne broji se kao uporaba.

Uporaba:  python3 kod/check_pojmovi.py [--strogo]
"""
import os
import re
import sys

KOR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUKOPIS = os.path.join(KOR, "rukopis")
RED = [("uvod", 0), ("predgovor", 0)] + [(f"poglavlje-{i:02d}", i) for i in range(1, 17)] + [("zakljucak", 99)]


def bez_aparata(t):
    t = re.sub(r"### Ključni pojmovi.*?(?=\n#|\Z)", "", t, flags=re.S)
    t = re.sub(r"### Literatura poglavlja.*?(?=\n#|\Z)", "", t, flags=re.S)
    t = re.sub(r"^>.*$", "", t, flags=re.M)      # teza
    t = re.sub(r"^!\[.*$", "", t, flags=re.M)    # slike
    t = re.sub(r"^\|.*$", "", t, flags=re.M)     # tablice
    t = re.sub(r"^```.*?^```", "", t, flags=re.M | re.S)  # kod
    return t


def pojmovi():
    """{pojam: poglavlje koje ga uvodi} iz popisa ključnih pojmova."""
    out = {}
    for ime, br in RED:
        p = os.path.join(RUKOPIS, ime + ".md")
        if not os.path.exists(p):
            continue
        m = re.search(r"### Ključni pojmovi\s*\n+([^\n]+)",
                      open(p, encoding="utf-8").read())
        if not m:
            continue
        for x in m.group(1).split("·"):
            x = re.sub(r"[\*_]", "", x).strip()
            x = re.sub(r"\s*\([^)]*\)\s*", " ", x).strip()
            x = re.sub(r"\s*[—-].*$", "", x).strip()          # „pojam — objašnjenje"
            if 4 <= len(x) <= 60 and x.lower() not in out:
                out[x.lower()] = (x, br)
    return out


def uzorak(pojam):
    """Strogi uzorak: sve riječi pojma, nastavak dopušten samo na posljednjoj."""
    rijeci = [re.escape(w) for w in pojam.split()]
    return re.compile(r"\b" + r"\W+".join(rijeci[:-1] + [rijeci[-1] + r"\w{0,4}"]) + r"\b", re.I)


def main():
    strogo = "--strogo" in sys.argv
    tekstovi = {}
    for ime, br in RED:
        p = os.path.join(RUKOPIS, ime + ".md")
        if os.path.exists(p):
            tekstovi[ime] = (br, bez_aparata(open(p, encoding="utf-8").read()))
    P = pojmovi()
    nalazi = []
    for kljuc, (naziv, kan) in sorted(P.items(), key=lambda k: k[1][1]):
        if kan == 0 or kan == 99:
            continue
        for ime, (br, t) in tekstovi.items():
            if br == 0 or br == 99:
                continue
            m = uzorak(naziv).search(t)
            if m:
                if br < kan:
                    nalazi.append((naziv, kan, ime,
                                   " ".join(t[max(0, m.start() - 130):m.start() + 150].split())))
                break
    print(f"pojmova u popisima: {len(P)} · RANO upotrijebljenih: {len(nalazi)}\n")
    for n, k, ime, rec in nalazi:
        print(f"• {n}   (uvodi se u pogl. {k}; prva uporaba: {ime})\n    …{rec}…\n")
    return 1 if (nalazi and strogo) else 0


if __name__ == "__main__":
    sys.exit(main())
