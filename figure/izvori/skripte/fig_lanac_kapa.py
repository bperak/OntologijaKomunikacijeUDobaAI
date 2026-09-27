#!/usr/bin/env python3
"""Slika I.1 — lanac zakona sastavljanja (κ₁–κ₁₅) u OMLCC-u.

Prikazuje ono što Dodatak I tvrdi: svaka razina ima zakon sastavljanja
κ_n : N_n ↦ e_{n+1}{p} — mreža razine n daje entitet razine n+1 sa svojstvom
koje na razini n nije postojalo. Lanac je "zmijski": prvi stupac 1–8 odozgo
prema dolje, drugi stupac 9–16 odozdo prema gore.

Slika NE tvrdi više od teksta: ne nosi brojke, ne prikazuje nove tvrdnje i ne
sadrži referenciju (citiranje okvira: pogl. 2.1).

Pokretanje:  python3 fig_lanac_kapa.py [izlazni_direktorij]
"""
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.ft2font import FT2Font
from matplotlib import font_manager

INK = '#1C2B4A'; INK2 = '#334463'; ACC = '#C0502E'; ACC2 = '#0F766E'
SOFT = '#EEF2F8'; MUTED = '#5A6B80'; LINEC = '#D5DDE8'; DEEP = '#8E3A20'

# postoji li znak ₙ (U+2099) u zadanome fontu? ako ne, piše se obično slovo n
_font_path = font_manager.findfont('DejaVu Sans')
_has_sub_n = FT2Font(_font_path).get_char_index(ord('ₙ')) != 0
SUB_N = 'ₙ' if _has_sub_n else 'n'


def sub(n: int) -> str:
    """Broj kao indeks (1 → ₁, 16 → ₁₆)."""
    tab = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
    return str(n).translate(tab)


# (razina, naziv, entitet koji razina daje, svojstvo, boja)
LEVELS = [
    (1, 'Existence', 'nosač', 'prisutnost', INK2),
    (2, 'Emergence', 'nova cjelina', 'novost', INK2),
    (3, 'MaterialStructure', 'strukturirana cjelina', 'sastav, čvrstoća', INK2),
    (4, 'Spatial', 'tijelo s položajem', 'položaj, inkluzija', INK2),
    (5, 'Force', 'djelovatelj', 'jakost, smjer', INK2),
    (6, 'Motion', 'tijelo u gibanju', 'brzina, putanja', INK2),
    (7, 'SequenceActivity', 'slijed', 'red, trajanje', INK2),
    (8, 'InformationSystem', 'oznaka', 'razlika', ACC2),
    (9, 'Perception', 'opažaj', 'razlučivost', ACC2),
    (10, 'Affect', 'afektivno stanje', 'valencija, pobuđenost', ACC2),
    (11, 'Cognition', 'pojam', 'struktura reprezentacije', ACC2),
    (12, 'SocIdentity', 'nositelj uloge', 'ime, uloga', ACC),
    (13, 'SocBehaviourInteraction', 'sudionik', 'uzajamnost', ACC),
    (14, 'SocCommunication', 'komunikacijski čin', 'namjera, konvencija', ACC),
    (15, 'SocCulturalInstitution', 'statusna funkcija', 'status, ovlast', ACC),
    (16, 'CulturalModel', 'kulturni model', 'vrijednost, žanr', DEEP),
]

fig, ax = plt.subplots(figsize=(13.0, 7.4), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis('off')

BW, BH = 38.0, 8.2
X1, X2 = 4.0, 58.0
TOP, STEP = 88.0, 10.4


def y_of(col: int, i: int) -> float:
    """i = 0..7 (redak u stupcu); prvi stupac odozgo, drugi odozdo."""
    if col == 1:
        return TOP - i * STEP - BH
    return TOP - (7 - i) * STEP - BH


def box(x, y, num, name, ent, prop, col):
    ax.add_patch(FancyBboxPatch((x, y), BW, BH, boxstyle='round,pad=0,rounding_size=1.0',
                                fc='white', ec=LINEC, lw=1.0, zorder=2))
    ax.add_patch(FancyBboxPatch((x, y), 2.6, BH, boxstyle='round,pad=0,rounding_size=1.0',
                                fc=col, ec='none', zorder=3))
    ax.text(x + 4.0, y + BH * 0.66, f'{num:02d}  {name}', ha='left', va='center',
            fontsize=9.0, color=col, fontweight='bold', zorder=4)
    ax.text(x + 4.0, y + BH * 0.24, f'e{sub(num)} = {ent}  ·  {{{prop}}}',
            ha='left', va='center', fontsize=7.0, color=MUTED, style='italic', zorder=4)


def arrow(x0, y0, x1, y1, label, rad=0.0):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=11,
                                 lw=1.3, color=ACC, shrinkA=0, shrinkB=0,
                                 connectionstyle=f'arc3,rad={rad}', zorder=3))
    ax.text((x0 + x1) / 2 + 1.6, (y0 + y1) / 2, label, ha='left', va='center',
            fontsize=8.2, color=ACC, fontweight='bold', zorder=4,
            bbox=dict(boxstyle='round,pad=0.16', fc='white', ec='none'))


# --- prvi stupac: razine 1–8 (odozgo prema dolje) ---
for i, (num, name, ent, prop, col) in enumerate(LEVELS[:8]):
    box(X1, y_of(1, i), num, name, ent, prop, col)
for i in range(7):
    y0 = y_of(1, i); y1 = y_of(1, i + 1)
    arrow(X1 + BW / 2, y0, X1 + BW / 2, y1 + BH, f'κ{sub(i + 1)}')

# --- prijelaz 8 → 9 (vodoravno pri dnu) ---
y_low = y_of(1, 7) + BH / 2
arrow(X1 + BW, y_low, X2, y_low, f'κ{sub(8)}', rad=-0.10)

# --- drugi stupac: razine 9–16 (odozdo prema gore) ---
for i, (num, name, ent, prop, col) in enumerate(LEVELS[8:]):
    box(X2, y_of(2, i), num, name, ent, prop, col)
for i in range(7):
    y0 = y_of(2, i) + BH; y1 = y_of(2, i + 1)
    arrow(X2 + BW / 2, y0, X2 + BW / 2, y1, f'κ{sub(i + 9)}')

# --- zaglavlje i podnožje ---
ax.text(50, 97.4, 'OMLCC — lanac zakona sastavljanja: κ₁–κ₁₅',
        ha='center', va='center', fontsize=12.4, color=ACC, fontweight='bold')
ax.text(50, 93.4, 'svaka razina: mreža  →  emergentni entitet  →  mreža sljedeće razine',
        ha='center', va='center', fontsize=8.6, color=INK2)
ax.text(50, 4.6, f'κ{SUB_N} : N{SUB_N} ↦ e(n+1){{p}}   —   mreža razine n daje entitet razine n+1 '
                 'sa svojstvom koje na razini n nije postojalo',
        ha='center', va='center', fontsize=8.6, color=INK2)
ax.text(50, 1.6, 'Smjer: 1–8 odozgo prema dolje, 9–16 odozdo prema gore. Iznad 16 petlja se zatvara '
                 '(κ₁₆ ↦ zajednica kao nositelj). Autorov prikaz (→ dodatak I.1).',
        ha='center', va='center', fontsize=7.8, color=MUTED)

fig.savefig(os.path.join(os.sys.argv[1] if len(sys.argv) > 1 else '/home/agent/knjiga-emergencija/figure',
                         'dijagram-I-1-lanac-kapa.svg'), format='svg',
            facecolor='white', bbox_inches='tight', pad_inches=0.06)
out = sys.argv[1] if len(sys.argv) > 1 else '/home/agent/knjiga-emergencija/figure'
fig.savefig(os.path.join(out, 'dijagram-I-1-lanac-kapa.png'), format='png',
            facecolor='white', bbox_inches='tight', pad_inches=0.06)
print('subscript ₙ available:', _has_sub_n)
print('saved', os.path.join(out, 'dijagram-I-1-lanac-kapa.png'), 'and .svg')
