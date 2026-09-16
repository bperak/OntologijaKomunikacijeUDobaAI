"""Cultural Complexity Lab — invented lockup (emblem + wordmark), transparent PNG."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
from PIL import Image

INK = '#1C2B4A'
ACC = '#C0502E'
ACC2 = '#0F766E'
MUTED = '#5A6B80'

W, H = 5.2, 1.3
fig = plt.figure(figsize=(W, H), dpi=300)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, W)
ax.set_ylim(0, H)
ax.axis('off')

# ---------------- emblem: a cultural network (nodes + relations) ----------
cx, cy, R = 0.66, 0.63, 0.44
ax.add_patch(Circle((cx, cy), R, fill=False, ec=INK, lw=1.9, zorder=2))
n = 9
ang = np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, n + 1)[:-1]
px = cx + R * np.cos(ang)
py = cy + R * np.sin(ang)
# ring relations
for i in range(n):
    j = (i + 1) % n
    ax.plot([px[i], px[j]], [py[i], py[j]], color=MUTED, lw=0.8, alpha=0.85, zorder=3)
# chords through the centre (structure, not just a ring)
for i in (0, 3, 6):
    ax.plot([px[i], cx], [py[i], cy], color=ACC2, lw=1.0, alpha=0.9, zorder=3)
ax.plot([px[1], px[6]], [py[1], py[6]], color=ACC, lw=1.2, zorder=3)
# centre: the shared core
ax.add_patch(Circle((cx, cy), 0.075, fc=INK, ec='none', zorder=4))
# nodes
for i in range(n):
    col = ACC if i == 1 else INK
    ax.add_patch(Circle((px[i], py[i]), 0.052, fc=col, ec='white', lw=0.7, zorder=5))

# ---------------- wordmark -------------------------------------------------
letters = '\u2009'
def spaced(txt):
    return '   '.join(letters.join(w) for w in txt.split(' '))

ax.text(1.42, 0.79, spaced('CULTURAL'), fontsize=15.5, fontweight='bold', color=INK,
        va='center', ha='left', family='DejaVu Sans')
ax.text(1.42, 0.50, spaced('COMPLEXITY LAB'), fontsize=15.5, fontweight='bold', color=INK,
        va='center', ha='left', family='DejaVu Sans')
ax.text(1.42, 0.235, 'language  ·  culture  ·  complexity', fontsize=8.6, color=ACC2,
        va='center', ha='left', family='DejaVu Sans', style='italic')
ax.plot([1.42, 4.98], [0.345, 0.345], color=ACC, lw=1.1, zorder=3)

fig.savefig('/tmp/logos/ccl_logo_raw.png', dpi=300, transparent=True)
plt.close(fig)

# trim transparent margin
im = Image.open('/tmp/logos/ccl_logo_raw.png').convert('RGBA')
bb = im.getchannel('A').getbbox()
im = im.crop(bb)
im.save('/tmp/logos/ccl_logo.png')
w, h = im.size
print(f'ccl_logo.png {w}x{h} ar={w/h:.2f}')

# square emblem-only variant (for footers)
fig = plt.figure(figsize=(1.4, 1.4), dpi=300)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, 1.4); ax.set_ylim(0, 1.4); ax.axis('off')
cx, cy, R = 0.7, 0.7, 0.5
ax.add_patch(Circle((cx, cy), R, fill=False, ec=INK, lw=2.4, zorder=2))
px = cx + R * np.cos(ang); py = cy + R * np.sin(ang)
for i in range(n):
    j = (i + 1) % n
    ax.plot([px[i], px[j]], [py[i], py[j]], color=MUTED, lw=1.0, alpha=0.85, zorder=3)
for i in (0, 3, 6):
    ax.plot([px[i], cx], [py[i], cy], color=ACC2, lw=1.2, zorder=3)
ax.plot([px[1], px[6]], [py[1], py[6]], color=ACC, lw=1.4, zorder=3)
ax.add_patch(Circle((cx, cy), 0.085, fc=INK, ec='none', zorder=4))
for i in range(n):
    ax.add_patch(Circle((px[i], py[i]), 0.060, fc=(ACC if i == 1 else INK), ec='white', lw=0.8, zorder=5))
fig.savefig('/tmp/logos/ccl_mark_raw.png', dpi=300, transparent=True)
plt.close(fig)
im = Image.open('/tmp/logos/ccl_mark_raw.png').convert('RGBA')
im = im.crop(im.getchannel('A').getbbox())
im.save('/tmp/logos/ccl_mark.png')
print('ccl_mark.png', im.size)
