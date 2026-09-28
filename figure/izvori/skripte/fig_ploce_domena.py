#!/usr/bin/env python3
"""Slike I.2–I.4 — tri ploče: materijalna (1–8), psihološka (9–11), društvena (12–16).

Svaka kućica nosi ono što Dodatak I tvrdi za tu razinu:
  naziv i broj razine · entitet e_n · relaciju s arnošću · uvjet dopuštenosti ·
  učinak · gdje se čita u podacima · što bi razinu oborilo.
Strelice nose zakon sastavljanja κ_n (mreža razine n ↦ entitet razine n+1).

Slika ne tvrdi više od teksta: nema brojki, nema novih tvrdnji, nema referencije
(citiranje okvira: pogl. 2.1). Autorov prikaz.

Pokretanje: python3 fig_ploce_domena.py [izlazni_direktorij]
"""
import os
import sys
import textwrap

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

INK = '#1C2B4A'; INK2 = '#334463'; ACC = '#C0502E'; ACC2 = '#0F766E'
DEEP = '#8E3A20'; MUTED = '#5A6B80'; LINEC = '#D5DDE8'; FIELD = '#3B4A61'
MATC = INK2; PSYC = ACC2; SOCC = ACC


def sub(n: int) -> str:
    return str(n).translate(str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉'))


# razina → (naziv, entitet, relacija, arnost, uvjet dopuštenosti, učinak,
#           kako se čita, što bi je oborilo)
L = {
1: ('Existence', 'nosač x', 'jest / nije (unarna)', '1',
    'pripadnost domeni (x ∈ U)',
    'uvrštavanje u daljnje zapise',
    'egzistencijalni iskazi („postoji X”, „X ima”)',
    'ako se svaka tvrdnja o postojanju dade prevesti u tvrdnju o sastavu („postoji” = „ima dijelove”), L1 nije razina nego način govora'),
2: ('Emergence', 'nova cjelina e, niža mreža N', 'nastaje iz (N → e)', '2',
    'postoji zakon sastavljanja niže razine',
    'e dobiva svojstvo koje se ne pripisuje pojedinim dijelovima',
    'glagoli nastajanja i postajanja („nastaje”, „postaje”)',
    'ako se novost može izračunati prečicom (bez izvođenja), L2 je mjera, a ne razina'),
3: ('MaterialStructure', 'dio p, cjelina w', 'isPartOf (p, w)', '2',
    'pripadnost skupu dijelova',
    'p doprinosi sastavu w',
    'genitivne konstrukcije, „sastoji se od”, „dio” / „cjelina”',
    'ako su sva svojstva cjeline aditivna (zbroj svojstava dijelova), L3 opisuje zbroj, a ne uređenje'),
4: ('Spatial', 'figura f, tlo g', 'prostorna relacija (f, g; τ)', '2 + tip',
    'odnos prema tlu (figura–tlo)',
    'f dobiva položaj s obzirom na g',
    'prijedlozi i prilozi mjesta („u”, „na”, „iznad”), padeži mjesta',
    'ako se svi prostorni odnosi mogu svesti na svojstva strukture (L3) bez ostatka, L4 nije zasebna'),
5: ('Force', 'djelovatelj A, trpitelj B', 'djeluje na (A, B)', '2',
    'doseg',
    'promjena stanja trpitelja (ne nužno njegova gibanja)',
    'kauzativni glagoli, instrumentali, izrazi jakosti („pritisak”, „udar”)',
    'ako je sila uvijek samo opis gibanja, test razdvajanja spaja L5 i L6'),
6: ('Motion', 'tijelo m, putanja π', 'giba se duž (m, π)', '2',
    'mogućnost putanje',
    'promjena položaja',
    'glagoli kretanja s prijedlozima putanje, izrazi brzine i trajanja',
    'ako se gibanje može opisati kao niz stanja položaja bez novoga tipa svojstva, L6 je izvedenica L4'),
7: ('SequenceActivity', 'događaj d, niz Σ', 'prethodi / slijedi (d₁, d₂)', '2',
    'red (uređenje događaja)',
    'svojstva niza (ponavljanje, ritam) ne pripadaju pojedinom događaju',
    'vremenski veznici („zatim”, „prije”), glagolski vid, izrazi ponavljanja',
    'ako redoslijed nije ništa drugo do svojstvo trajanja pojedinih dijelova, L7 se svodi na L3–L6'),
8: ('InformationSystem', 'oznaka σ, stanje okoline s', 'nosi informaciju o (σ, s)', '2',
    'postoji razlikovanje (σ₁ ≠ σ₂ kad s₁ ≠ s₂)',
    'σ postaje upotrebljiva za daljnje odluke, i kad je nitko ne razumije',
    'znakovi, oznake, kodovi; „oznaka pokazuje”, „signal znači”',
    'ako je informacija samo struktura (svediva na L3–L7), L8 ne postoji i ljestvica se skraćuje'),
9: ('Perception', 'opažač q, objekt o', 'opaža (q, o)', '2',
    'usmjerenost (postoji razlika između toga da q prima razliku i da je ne prima)',
    'o postaje za q',
    'perceptivni glagoli („vidi”, „čuje”) s izraženim objektom',
    'ako se razlučivost može objasniti isključivo svojstvima oznake (L8) bez nositelja koji opaža, L9 se svodi na L8'),
10: ('Affect', 'doživljavatelj q, stanje α', 'doživljava (q, α)', '2',
    'stanje u koje sustav dolazi (ne usmjerenost)',
    'α mijenja spremnost na djelovanje',
    'emocionalni leksik i njegove mreže (→ pogl. 6.4)',
    'ako se afektivna svojstva mogu svesti na oznake bez nositelja (L8), afekt nije razina nego vrsta oznake'),
11: ('Cognition', 'mislitelj q, reprezentacija ρ', 'predočuje (q, ρ)', '2',
    'mogućnost pogreške (reprezentacija može ne odgovarati onome što predočuje)',
    'ρ ulazi u zaključivanje',
    'izrazi vjerovanja i mišljenja („misli da”), propozicijski sadržaji',
    'ako se sva svojstva reprezentacije daju opisati kao svojstva oznake (L8) u kontekstu (spor otvoren: Mitchell & Krakauer 2023), L11 je način opisa, a ne razina'),
12: ('SocIdentity', 'nositelj a, drugi b', 'prepoznaje kao (b, a, uloga)', '3',
    'trajnost kroz situacije (adresa koja nadživljava susret)',
    'a postaje adresabilan',
    'imena, titule, uloge, računi, ključevi (→ pogl. 14.1)',
    'ako se identitet svaki put uspostavlja izvana i ne postoji adresa koja nadživljava susret, riječ je o oznaci (L8)'),
13: ('SocBehaviourInteraction', 'sudionik a, sudionik b', 'uzvraća / suradi (a, b)', '2',
    'očekivanje uzvrata',
    'koordinirano ponašanje bez središnjega naredbodavca',
    'uzajamni izrazi, protokoli predaje zadatka, vremenska zbijenost (→ pogl. 14.2)',
    'ako se usklađenost uvijek svodi na jedan naredbeni lanac, L13 je raspored, a ne interakcija'),
14: ('SocCommunication', 'izvor S, primatelj H, artefakt c', 'adresira i daje da prepozna (S, H; c)', '3',
    'četiri člana: adresiranje, prepoznata namjera, zajednički artefakt, konvencija',
    'ishod ovisi o tome je li namjera prepoznata',
    'adresiranje, ispravci, preuzimanje obveze; dijaloški protokol (→ pogl. 13.5)',
    'ako se komunikacijski čin dade objasniti bez prepoznate namjere i obveze, L14 se svodi na L8 + L13'),
15: ('SocCulturalInstitution', 'pravilo R, kontekst C, nositelj a', 'broji kao (X, Y, C)', '3',
    'kolektivno priznanje',
    'deontički: prava, dužnosti i ovlast da se izrekne posljedica',
    '„vrijedi kao”, „ima pravo”, „dužan je”; zapisi o ispravku ili sankciji',
    'ako se institucionalne činjenice mogu opisati kao puki obrasci uporabe bez obveze i priznanja, L15 nije potrebna'),
16: ('CulturalModel', 'zajednica G, obrazac M, nositelj a', 'predaje / nasljeđuje (G, a; M)', '3',
    'višegeneracijski prijenos, mogućnost osporavanja i isključenja',
    'M se održava u mreži koja ga predaje, ne u pojedincu',
    'žanrovi, kanon, vrijednosti (→ pogl. 15.1, 15.4)',
    'ako se svaki od šest uvjeta prijenosa može ispuniti bez zajednice koja priznaje obrazac, L16 gubi razliku prema L6'),
}

# strelica između razine k i k+1 nosi zakon κ_k
ARROW = {
1: 'κ₁ → e₂{novost}',
2: 'κ₂ → e₃{sastav, čvrstoća}',
3: 'κ₃ → e₄{položaj, inkluzija}',
4: 'κ₄ → e₅{jakost, smjer}',
5: 'κ₅ → e₆{brzina, putanja}',
6: 'κ₆ → e₇{red, trajanje}',
7: 'κ₇ → e₈{razlika}',
8: 'κ₈ → e₉{razlučivost}',
9: 'κ₉ → e₁₀{valencija, pobuđenost}',
10: 'κ₁₀ → e₁₁{struktura reprezentacije}',
11: 'κ₁₁ → e₁₂{ime, uloga}',
12: 'κ₁₂ → e₁₃{uzajamnost}',
13: 'κ₁₃ → e₁₄{namjera, konvencija}',
14: 'κ₁₄ → e₁₅{status, ovlast}',
15: 'κ₁₅ → e₁₆{vrijednost, žanr}',
}

PANELS = [
    ('dijagram-I-2-materijalna-domena', 'MATERIJALNA DOMENA', 'razine 1–8 · κ₁–κ₇',
     list(range(1, 9)), MATC, 'dodatak I.3', None),
    ('dijagram-I-3-psiholoska-domena', 'PSIHOLOŠKA DOMENA', 'razine 9–11 · κ₈–κ₁₀',
     [9, 10, 11], PSYC, 'dodatak I.4',
     'ulaz iz materijalne domene: κ₈ (→ slika I.2)'),
    ('dijagram-I-4-drustvena-domena', 'DRUŠTVENA DOMENA', 'razine 12–16 · κ₁₁–κ₁₅',
     [12, 13, 14, 15, 16], SOCC, 'dodatak I.5',
     'ulaz iz psihološke domene: κ₁₁ (→ slika I.3); iznad 16 petlja se zatvara: κ₁₆ ↦ zajednica kao nositelj'),
]

NALAZI = []            # mjerni nalazi (prazno = sve unutar granica)
_texts = []            # (ploca, razina, vrsta, tekst, Text)
_cards = []            # (ploca, razina, x, y0, cw, ch)

W = 13.0
MARGIN = 0.34
GAP = 1.42
ROWGAP = 0.92
FS_FIELD = 6.0
FS_HDR = 7.8
FS_ENT = 6.5

def hl(fs: float) -> float:
    """Visina reda u inčima za zadanu veličinu fonta (vodeći prostor 1,30)."""
    return fs / 72.0 * 1.30


def wrap_chars(width_in: float, fs: float, faktor: float = 0.56) -> int:
    """Koliko znakova stane u širinu pri zadanoj veličini fonta (faktor se kalibrira mjerenjem)."""
    return max(12, int(width_in / (fs * faktor / 72.0)))


def card_layout(num, cw, col, faktor=0.56):
    """(tekst, veličina, boja, težina, stil, napredak_nakon) — jedno mjesto za mjerenje i crtanje."""
    name, ent, rel, arn, uvjet, ucinak, cita, obara = L[num]
    cols = wrap_chars(cw - 0.30, FS_FIELD, faktor)
    out = [(f'{num:02d}  {name}', FS_HDR, col, 'bold', 'normal', hl(FS_HDR) + 0.055),
           (f'e{sub(num)} = {ent}', FS_ENT, INK2, 'bold', 'italic', hl(FS_ENT) + 0.075)]
    for lbl, txt in (('RELACIJA', f'{rel} · arnost {arn}'),
                     ('UVJET', uvjet), ('UČINAK', ucinak),
                     ('ČITA SE', cita), ('OBARA GA', obara)):
        lines = textwrap.wrap(f'{lbl}: {txt}', cols)[:7]
        for i, ln in enumerate(lines):
            out.append((ln, FS_FIELD, FIELD, 'normal', 'normal',
                        hl(FS_FIELD) + (0.085 if i == len(lines) - 1 else 0.0)))
    return out


def build(panel, out_dir, faktor=0.56):
    fname, naslov, podnaslov, levels, col, ref, note = panel
    per_row = 4 if len(levels) >= 8 else 3
    rows = [levels[i:i + per_row] for i in range(0, len(levels), per_row)]
    cw = (W - 2 * MARGIN - (per_row - 1) * GAP) / per_row

    # visina kućice: najdulji sadržaj u ploči
    need = 0.0
    for lv in levels:
        need = max(need, 0.16 + sum(e[5] for e in card_layout(lv, cw, col, faktor)) + 0.16)
    ch = need

    H = 0.62 + len(rows) * ch + (len(rows) - 1) * ROWGAP + 0.52
    fig = plt.figure(figsize=(W, H), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])          # osi = cijelo platno → 1 jedinica = 1 inč
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis('off')

    ax.text(W / 2, H - 0.24, f'OMLCC — {naslov}', ha='center', va='center',
            fontsize=12.0, color=col, fontweight='bold')
    ax.text(W / 2, H - 0.46, podnaslov, ha='center', va='center',
            fontsize=8.6, color=INK2)

    _cards.clear(); _texts.clear()
    pos = {}
    for r, row in enumerate(rows):
        top = H - 0.62 - r * (ch + ROWGAP)
        y0 = top - ch
        for j, lv in enumerate(row):
            x = MARGIN + (j if r % 2 == 0 else per_row - 1 - j) * (cw + GAP)
            pos[lv] = (x, y0)

    # kućice
    for lv in levels:
        x, y0 = pos[lv]
        ax.add_patch(FancyBboxPatch((x, y0), cw, ch,
                                    boxstyle='round,pad=0,rounding_size=0.07',
                                    fc='white', ec=LINEC, lw=0.9, zorder=2))
        _cards.append((fname, lv, x, y0, cw, ch))
        ax.add_patch(FancyBboxPatch((x, y0), 0.055, ch,
                                    boxstyle='round,pad=0,rounding_size=0.02',
                                    fc=col, ec='none', zorder=3))
        lay = card_layout(lv, cw, col, faktor)
        cy = y0 + ch - 0.16 - hl(lay[0][1]) / 2
        for txt, fs, c, wt, st, adv in lay:
            _texts.append((fname, lv, 'kucica', txt,
                           ax.text(x + 0.15, cy, txt, ha='left', va='center', fontsize=fs,
                                   color=c, fontweight=wt, style=st, zorder=4)))
            cy -= adv
        if lv == levels[0] and lv == 1:
            ax.text(x + 0.15, y0 + 0.11, 'polazište: nema prethodne mreže — ni κ ni ε',
                    ha='left', va='center', fontsize=5.6, color=MUTED, style='italic', zorder=4)
        if lv == 16:
            ax.text(x + 0.15, y0 + 0.11, 'iznad: κ₁₆ ↦ zajednica kao nositelj (nije nova razina)',
                    ha='left', va='center', fontsize=5.6, color=col, style='italic', zorder=4)

    def chip(mx, my, txt):
        """Oznaka zakona κ na strelici: lomljena tako da ostane unutar razmaka među kućicama."""
        lijevo, _, desno = txt.partition(' → ')
        redci = [lijevo + ' →']
        redci += textwrap.wrap(desno, 20)[:2]
        _texts.append((fname, 0, 'chip', ' '.join(redci),
                       ax.text(mx, my, '\n'.join(redci), ha='center', va='center', fontsize=5.9,
                               color=ACC, fontweight='bold', zorder=6, linespacing=1.25,
                               bbox=dict(boxstyle='round,pad=0.20', fc='white', ec=ACC, lw=0.7))))

    # strelice unutar reda
    for r, row in enumerate(rows):
        for j in range(len(row) - 1):
            a, b = row[j], row[j + 1]
            xa, ya = pos[a]; xb, yb = pos[b]
            if r % 2 == 0:
                p0, p1 = (xa + cw, ya + ch / 2), (xb, yb + ch / 2)
            else:
                p0, p1 = (xa, ya + ch / 2), (xb + cw, yb + ch / 2)
            ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle='-|>', mutation_scale=10,
                                         lw=1.2, color=ACC, shrinkA=0, shrinkB=0, zorder=5))
            chip((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + 0.20, ARROW[a])
        # prijelaz u sljedeći red
        if r < len(rows) - 1:
            last, nxt = row[-1], rows[r + 1][0]
            xa, ya = pos[last]; xb, yb = pos[nxt]
            p0, p1 = (xa + cw / 2, ya), (xb + cw / 2, yb + ch)
            ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle='-|>', mutation_scale=10,
                                         lw=1.2, color=ACC, shrinkA=0, shrinkB=0, zorder=5))
            chip((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2, ARROW[last])

    foot = (f'Zakoni sastavljanja κ{sub(levels[0] - 1)}–κ{sub(levels[-1] - 1)}: mreža razine n daje entitet '
            'razine n+1 sa svojstvom koje na razini n nije postojalo. Svaka kućica: entitet razine, '
            f'relacija s arnošću, uvjet dopuštenosti, učinak, mjesto u podacima i što bi razinu oborilo. Autorov prikaz (→ {ref}).')
    ax.text(W / 2, 0.30, ' '.join(foot.split()), ha='center', va='center',
            fontsize=7.0, color=MUTED)
    if note:
        ax.text(W / 2, 0.14, note, ha='center', va='center', fontsize=7.0, color=col)

    # --- mjerenje: tekst u kućici, tekst u okviru kućice, chip u razmaku ---
    nalazi_ploce = []
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    dpi = fig.dpi
    kutije = {}
    for pl, lv, x, y0, cwid, chh in _cards:
        p0 = ax.transData.transform((x, y0)); p1 = ax.transData.transform((x + cwid, y0 + chh))
        kutije[lv] = (min(p0[0], p1[0]) / dpi, min(p0[1], p1[1]) / dpi,
                      max(p0[0], p1[0]) / dpi, max(p0[1], p1[1]) / dpi)
    for pl, lv, vrsta, txt, obj in _texts:
        bb = obj.get_window_extent(r)
        x0, y0, x1, y1 = bb.x0 / dpi, bb.y0 / dpi, bb.x1 / dpi, bb.y1 / dpi
        if vrsta == 'kucica':
            k = kutije[lv]
            if x0 < k[0] + 0.12 or x1 > k[2] - 0.06:
                nalazi_ploce.append(f'{pl} L{lv}: tekst izlazi vodoravno → „{txt[:60]}”')
            if y0 < k[1] + 0.05 or y1 > k[3] - 0.05:
                nalazi_ploce.append(f'{pl} L{lv}: tekst izlazi okomito → „{txt[:60]}”')
        else:
            for lv2, k in kutije.items():
                if x1 > k[0] and x0 < k[2] and y1 > k[1] and y0 < k[3]:
                    nalazi_ploce.append(f'{pl}: oznaka κ ulazi u kućicu L{lv2} → „{txt}”')

    NALAZI.extend(nalazi_ploce)
    for fmt in ('svg', 'png'):
        fig.savefig(os.path.join(out_dir, f'{fname}.{fmt}'), format=fmt,
                    facecolor='white', bbox_inches='tight', pad_inches=0.05)
    plt.close(fig)
    print(f'✔ {fname}.svg/.png   ({len(levels)} razina, kućica {cw:.2f} × {ch:.2f} in, '
          f'ploha {W:.1f} × {H:.2f} in, faktor {faktor})')
    return len(nalazi_ploce)


if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/agent/knjiga-emergencija/figure'
    for p in PANELS:
        NALAZI.clear()
        for f in (0.56, 0.53, 0.50, 0.47, 0.44):
            n = build(p, out, f)
            if n == 0:
                print(f'   mjerenje: 0 nalaza (faktor {f})')
                break
            print(f'   mjerenje: {n} nalaza s faktorom {f} → stanjujem tekst')
        else:
            print(f'   ⚠ {p[0]}: ni najmanji faktor nije prošao — treba ručno skratiti tekst')
    print()
    if NALAZI:
        print(f'⚠ mjernih nalaza: {len(NALAZI)}')
        for n in NALAZI[:40]:
            print('   -', n)
        sys.exit(1)
    print('✔ mjereno: sav tekst je unutar kućica, oznake κ ne ulaze u kućice')
