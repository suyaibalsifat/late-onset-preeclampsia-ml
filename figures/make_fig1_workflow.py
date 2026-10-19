import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Ellipse, Rectangle, Circle, Polygon, Wedge, FancyArrowPatch
plt.rcParams.update({"font.family": "Liberation Sans", "pdf.fonttype": 42, "font.size": 8})

fig, ax = plt.subplots(figsize=(6.5, 4.15)); ax.set_xlim(0, 100); ax.set_ylim(-5, 62); ax.axis("off")
NAVY, TEAL, ORANGE, GREEN, GREY = "#1f3b73", "#1b8a8f", "#d9822b", "#3c9a5f", "#5b6770"
W, H = 22.6, 28.0
xs = [0.2, 25.9, 51.6, 77.2]; ys = {1: 33, 2: 0.5}

def card(x, y, color, title, lines, tint):
    ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0.0,rounding_size=1.6", fc="white", ec=color, lw=1.6, zorder=2))
    ax.add_patch(FancyBboxPatch((x, y + H - 6.0), W, 6.0, boxstyle="round,pad=0.0,rounding_size=1.6", fc=color, ec=color, lw=1.6, zorder=3))
    ax.add_patch(Rectangle((x, y + H - 6.0), W, 3.0, fc=color, ec=color, zorder=3))
    ax.text(x + W / 2, y + H - 3.0, title, ha="center", va="center", color="white", fontsize=8.5, fontweight="bold", zorder=4)
    ax.add_patch(Circle((x + W / 2, y + 14.6), 5.8, fc=tint, ec="none", zorder=3))
    for i, t in enumerate(lines):
        ax.text(x + W / 2, y + 5.6 - i * 3.4, t, ha="center", va="center", fontsize=8, color="#222", zorder=4)

# ---- icons, each centred at (cx, cy) inside the tinted circle
def icon_database(cx, cy, c):
    w, h, e = 5.2, 1.5, 3.4
    for k, yy in enumerate([cy - 2.6, cy - 0.2, cy + 2.2]):
        ax.add_patch(Rectangle((cx - w / 2, yy), w, e * 0.55, fc=c, ec="none", zorder=5))
        ax.add_patch(Ellipse((cx, yy), w, h, fc=c, ec="white", lw=0.8, zorder=5))
    ax.add_patch(Ellipse((cx, cy + 2.2 + 1.9), w, h, fc=c, ec="white", lw=0.8, zorder=6))
def icon_people(cx, cy, c):
    for dx, s in [(-1.9, 0.85), (1.9, 0.85), (0, 1.1)]:
        ax.add_patch(Circle((cx + dx, cy + 1.6 * s + 0.6), 0.9 * s, fc=c, ec="white", lw=0.8, zorder=6 if dx == 0 else 5))
        ax.add_patch(Wedge((cx + dx, cy - 2.2 * s + 0.6), 1.8 * s * 1.15, 0, 180, fc=c, ec="white", lw=0.8, zorder=6 if dx == 0 else 5))
def icon_features(cx, cy, c):
    for i, hh in enumerate([2.0, 3.4, 2.6, 4.6]):
        ax.add_patch(Rectangle((cx - 4.2 + i * 2.2, cy - 3), 1.6, hh, fc=c, ec="none", zorder=5))
    xs_ = np.array([cx - 3.4, cx - 1.2, cx + 1.0, cx + 3.2]); ys_ = np.array([cy + 0.2, cy + 1.6, cy + 0.9, cy + 3.2])
    ax.plot(xs_, ys_, color=ORANGE, lw=1.8, zorder=6, marker="o", ms=3)
def icon_split(cx, cy, c):
    ax.add_patch(Rectangle((cx - 4.6, cy - 2.2), 6.6, 4.4, fc=c, ec="white", lw=0.8, zorder=5))
    ax.add_patch(Rectangle((cx + 2.3, cy - 2.2), 2.3, 4.4, fc=ORANGE, ec="white", lw=0.8, zorder=5))
    ax.text(cx - 1.3, cy, "80", color="white", fontsize=7, ha="center", va="center", fontweight="bold", zorder=6)
    ax.text(cx + 3.45, cy, "20", color="white", fontsize=6, ha="center", va="center", fontweight="bold", zorder=6)
def icon_funnel(cx, cy, c):
    ax.add_patch(Polygon([[cx - 4.6, cy + 3.4], [cx + 4.6, cy + 3.4], [cx + 0.9, cy - 0.4], [cx + 0.9, cy - 3.4], [cx - 0.9, cy - 2.2], [cx - 0.9, cy - 0.4]], closed=True, fc=c, ec="white", lw=0.8, zorder=5))
def icon_gears(cx, cy, c):
    def gear(x, y, r, n):
        ang = np.linspace(0, 2 * np.pi, 2 * n, endpoint=False); rr = np.where(np.arange(2 * n) % 2 == 0, r, r * 0.78)
        pts = np.c_[x + rr * np.cos(ang), y + rr * np.sin(ang)]
        ax.add_patch(Polygon(pts, closed=True, fc=c, ec="white", lw=0.8, zorder=5)); ax.add_patch(Circle((x, y), r * 0.35, fc="white", ec="none", zorder=6))
    gear(cx - 1.6, cy - 0.4, 3.2, 8); gear(cx + 2.9, cy + 2.2, 2.0, 6)
def icon_eval(cx, cy, c):
    ax.plot([cx - 4.4, cx - 4.4, cx + 4.4], [cy + 3.6, cy - 3, cy - 3], color=c, lw=1.6, zorder=5)
    for i, (hh, err) in enumerate([(3.4, 0.9), (5.2, 1.0), (4.0, 0.9)]):
        ax.add_patch(Rectangle((cx - 3.4 + i * 2.8, cy - 3), 1.8, hh, fc=c, ec="none", zorder=5))
        ax.plot([cx - 2.5 + i * 2.8] * 2, [cy - 3 + hh - err, cy - 3 + hh + err], color=ORANGE, lw=1.6, zorder=6)
def icon_explain(cx, cy, c):
    ax.add_patch(Circle((cx - 0.8, cy + 0.8), 3.0, fc="white", ec=c, lw=2.4, zorder=5))
    ax.plot([cx + 1.4, cx + 4.2], [cy - 1.4, cy - 4.0], color=c, lw=3, solid_capstyle="round", zorder=5)
    for i, hh in enumerate([1.4, 2.4, 1.8]):
        ax.add_patch(Rectangle((cx - 2.4 + i * 1.5, cy - 0.6), 1.0, hh, fc=ORANGE, ec="none", zorder=6))

cards = [
 (1, 0, NAVY, "1  Visit-level file", ["42,965 visit rows", "no woman identifier"], "#dfe6f3", icon_database),
 (1, 1, NAVY, "2  Rebuild women", ["11,767 women", "317 cases (2.7%)"], "#dfe6f3", icon_people),
 (1, 2, NAVY, "3  Features", ["27 measures × 5", "+ 67 static = 202"], "#dfe6f3", icon_features),
 (1, 3, ORANGE, "4  Split by woman", ["train 9,413", "test 2,354"], "#fbe9d6", icon_split),
 (2, 0, TEAL, "5  Fit on train only", ["impute, select, scale", "31 features kept"], "#d9eeef", icon_funnel),
 (2, 1, TEAL, "6  Models", ["13 classifiers + 8", "ensembles, tuned"], "#d9eeef", icon_gears),
 (2, 2, GREEN, "7  Test once", ["bootstrap CI,", "calibration"], "#dcefe3", icon_eval),
 (2, 3, GREEN, "8  Explain", ["SHAP (global)", "LIME (10 seeds)"], "#dcefe3", icon_explain),
]
for r, c, col, title, lines, tint, icon in cards:
    x, y = xs[c], ys[r]
    card(x, y, col, title, lines, tint)
    icon(x + W / 2, y + 14.6, col)

def arrow(p, q):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=9, lw=1.2, color=GREY, zorder=1))
for r in (1, 2):
    for c in range(3):
        arrow((xs[c] + W + 0.2, ys[r] + H / 2), (xs[c + 1] - 0.2, ys[r] + H / 2))
ymid = (ys[1] + ys[2] + H) / 2
ax.plot([xs[3] + W / 2] * 2, [ys[1] - 0.2, ymid], color=GREY, lw=1.2, zorder=1)
ax.plot([xs[3] + W / 2, xs[0] + W / 2], [ymid, ymid], color=GREY, lw=1.2, zorder=1)
arrow((xs[0] + W / 2, ymid), (xs[0] + W / 2, ys[2] + H + 0.2))
ax.add_patch(FancyBboxPatch((xs[0] - 0.9, ys[2] - 1.0), xs[1] - xs[0] + W + 1.8, H + 2.0, boxstyle="round,pad=0.0,rounding_size=2", fc="none", ec=TEAL, lw=1.2, ls=(0, (5, 3)), zorder=0))
ax.text(xs[0], -3.2, "Dashed frame: steps fitted on the training partition only", fontsize=8, color=TEAL, ha="left", va="center", style="italic")
fig.savefig("fig1_workflow.pdf", bbox_inches="tight"); fig.savefig("fig1_workflow.png", dpi=300, bbox_inches="tight")
