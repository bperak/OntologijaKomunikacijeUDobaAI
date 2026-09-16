#!/usr/bin/env python3
"""Emergent hierarchy figure (OMLCC principle) for slide 7 - compact horizontal ladder."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch

INK='#1C2B4A'; INK2='#334463'; ACC='#C0502E'; ACC2='#0F766E'; SOFT='#EEF2F8'; MUTED='#5A6B80'; LINEC='#D5DDE8'

fig, ax = plt.subplots(figsize=(4.7, 2.35), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(0, 50); ax.axis('off')

def box(x, y, w, h, text, fc=SOFT, ec=None, tc=INK, fs=8.6, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.6",
                                fc=fc, ec=(ec or 'none'), lw=1.2, zorder=2))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', color=tc, fontsize=fs,
            fontweight=('bold' if bold else 'normal'), zorder=3, linespacing=1.35)

def arrow(x1, y1, x2, y2, color=LINEC, lw=1.6):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='-|>', mutation_scale=11, color=color, lw=lw, zorder=1))

ax.text(50, 46.5, 'Emergent hierarchy (OMLCC principle)', ha='center', fontsize=9.5, color=ACC, fontweight='bold')

# level 3 (top): emergent entity
box(30, 33, 40, 9, 'EMERGENT ENTITY\n+ new properties', fc='white', ec=ACC, tc=ACC, fs=8.6, bold=True)

# level 2: relations + relation properties
box(14, 19, 30, 8.5, 'RELATIONS\n+ relation properties', fc='white', ec=ACC2, tc=ACC2, fs=8.2, bold=True)
box(56, 19, 30, 8.5, 'RELATIONS\n+ relation properties', fc='white', ec=ACC2, tc=ACC2, fs=8.2, bold=True)

# level 1: entities + properties
for i, x in enumerate((4, 38, 70)):
    box(x, 5.5, 26, 8.5, f'ENTITY {i+1}\n+ properties', fc=SOFT, ec=LINEC, tc=INK2, fs=8.0)

arrow(17, 14.2, 40, 32.5); arrow(50, 14.2, 50, 32.5); arrow(83, 14.2, 60, 32.5)
ax.text(50, 1.5, 'each higher level: new entities and properties (not a sum of the parts)',
        ha='center', fontsize=7.8, color=MUTED, style='italic')
fig.tight_layout(); fig.savefig('/home/agent/iuc-dubrovnik-2026/fig_emerg_hijerarhija.png',
                                facecolor='white', bbox_inches='tight', pad_inches=0.07)
print('saved fig_emerg_hijerarhija.png')
