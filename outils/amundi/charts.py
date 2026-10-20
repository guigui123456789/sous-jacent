"""Graphiques SVG maison — règles de la charte : pas de quadrillage, pas de cadre,
étiquette de valeur au bout de la barre, unité dans le titre. Unités internes : 1 = 0,1 mm."""
NAVY = "#132A47"; CU = "#A8693E"; CU2 = "#D6A177"; SLATE = "#7E8494"; L1 = "#9DB0C8"
INK = "#262625"
GRAD = ["#132A47", "#3A5070", "#647793", "#8E9DB2", "#B5C1D0"]

def fr(v, d=1):
    if v is None: return ""
    s = f"{v:,.{d}f}".replace(",", " ").replace(".", ",")
    return s.replace("-", "−")

def _svg(w, h, body):
    return (f'<svg viewBox="0 0 {w*10} {h*10}" width="{w}mm" height="{h}mm" '
            f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')

def T(x, y, s, size=6.6, anchor="middle", fill=INK, weight=300, family="Inter", italic=False):
    st = ' font-style="italic"' if italic else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size*3.528:.1f}" text-anchor="{anchor}" '
            f'fill="{fill}" font-weight="{weight}" font-family="{family}"{st}>{s}</text>')

def columns(cats, vals, w=136, h=62, color=NAVY, hi=None, d=0, fmt=None, lab_every=1,
            hi_color=CU, vmax=None, txt=INK, base_label=True, neg_color=None):
    W, H = w*10, h*10
    top, bot = 40, 50
    n = len(cats); slot = W/n; bw = slot*0.62
    vmax = vmax or max(abs(v) for v in vals if v is not None)
    vmin = min(0, min(v for v in vals if v is not None))
    rng = vmax - vmin
    y0 = top + (H-top-bot) * (vmax/rng)
    sc = (H-top-bot)/rng
    out = []
    for i, (c, v) in enumerate(zip(cats, vals)):
        x = i*slot + (slot-bw)/2
        if v is None: continue
        col = hi_color if (hi and i in hi) else (neg_color if (neg_color and v < 0) else color)
        hgt = abs(v)*sc
        y = y0 - hgt if v >= 0 else y0
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{max(hgt,1):.1f}" fill="{col}"/>')
        lab = fmt(v) if fmt else fr(v, d)
        ly = (y - 9) if v >= 0 else (y + hgt + 24)
        out.append(T(x+bw/2, ly, lab, 5.6, fill=txt))
        if i % lab_every == 0 or i == n-1:
            out.append(T(x+bw/2, H-14, c, 5.6, fill=SLATE if txt == INK else txt))
    out.append(f'<line x1="0" y1="{y0:.1f}" x2="{W}" y2="{y0:.1f}" stroke="{txt if txt!=INK else "#000"}" stroke-width="1.8"/>')
    return _svg(w, h, "".join(out))

def hbars(items, w=90, h=None, color=NAVY, d=1, unit="", vmax=None, labw=40, txt=INK, hi=None, hi_color=CU):
    n = len(items); rowh = 62
    h = h or (n*rowh/10 + 2)
    W, H = w*10, h*10
    vmax = vmax or max(v for _, v in items)
    x0 = labw*10; avail = W - x0 - 120
    out = []
    for i, (lab, v) in enumerate(items):
        y = i*rowh + 8
        col = hi_color if (hi and i in hi) else color
        bw = max(v/vmax*avail, 2)
        out.append(T(0, y+34, lab, 6.4, anchor="start", fill=txt))
        out.append(f'<rect x="{x0}" y="{y+6}" width="{bw:.1f}" height="40" fill="{col}"/>')
        out.append(T(x0+bw+12, y+35, fr(v, d)+unit, 6.2, anchor="start", fill=txt))
    out.append(f'<line x1="{x0}" y1="0" x2="{x0}" y2="{H}" stroke="{txt if txt!=INK else "#000"}" stroke-width="1.4"/>')
    return _svg(w, h, "".join(out))

def lines(cats, series, w=136, h=60, ymin=None, ymax=None, ticks=None, d=1, lab_every=1,
          txt=INK, end_labels=True, legend=True, fmt=None):
    W, H = w*10, h*10
    left, right, top, bot = 70, 230, 40, 55
    allv = [v for _, vs, _ in series for v in vs if v is not None]
    ymin = min(allv) if ymin is None else ymin
    ymax = max(allv) if ymax is None else ymax
    n = len(cats)
    X = lambda i: left + i*(W-left-right)/(n-1)
    Y = lambda v: top + (H-top-bot)*(1-(v-ymin)/(ymax-ymin))
    out = []
    for t in (ticks or []):
        out.append(T(left-14, Y(t)+8, fmt(t) if fmt else fr(t, 0), 5.4, anchor="end", fill=SLATE))
    for i, c in enumerate(cats):
        if i % lab_every == 0 or i == n-1:
            out.append(T(X(i), H-16, c, 5.4, fill=SLATE if txt == INK else txt))
    out.append(f'<line x1="{left}" y1="{H-bot+6}" x2="{W-right}" y2="{H-bot+6}" stroke="{"#000" if txt==INK else txt}" stroke-width="1.4"/>')
    for name, vs, col in series:
        pts = [(X(i), Y(v)) for i, v in enumerate(vs) if v is not None]
        path = " ".join(f"{'M' if k==0 else 'L'}{x:.1f},{y:.1f}" for k, (x, y) in enumerate(pts))
        out.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="5"/>')
        for x, y in pts:
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{col}"/>')
        # first & last value
        iv = [(i, v) for i, v in enumerate(vs) if v is not None]
        (i0, v0), (i1, v1) = iv[0], iv[-1]
        out.append(T(X(i0), Y(v0)-14, fmt(v0) if fmt else fr(v0, d), 5.6, fill=col))
        if end_labels:
            out.append(T(X(i1)+16, Y(v1)+7, (fmt(v1) if fmt else fr(v1, d)) + (f"  {name}" if legend else ""), 5.8, anchor="start", fill=col))
    return _svg(w, h, "".join(out))

def stacked(cats, series, w=136, h=66, txt=INK, lab_every=1):
    """series: list of (name, values, color). Positives empilés vers le haut, négatifs vers le bas."""
    W, H = w*10, h*10
    top, bot = 30, 50
    n = len(cats); slot = W/n; bw = slot*0.6
    pos = [sum(max(s[1][i], 0) for s in series) for i in range(n)]
    neg = [sum(min(s[1][i], 0) for s in series) for i in range(n)]
    vmax, vmin = max(pos), min(neg)
    sc = (H-top-bot)/(vmax-vmin); y0 = top + vmax*sc
    out = []
    for i, c in enumerate(cats):
        x = i*slot + (slot-bw)/2; up = y0; dn = y0
        for name, vs, col in series:
            v = vs[i]
            if v >= 0:
                hgt = v*sc; up -= hgt
                out.append(f'<rect x="{x:.1f}" y="{up:.1f}" width="{bw:.1f}" height="{hgt:.1f}" fill="{col}"/>')
            else:
                hgt = -v*sc
                out.append(f'<rect x="{x:.1f}" y="{dn:.1f}" width="{bw:.1f}" height="{hgt:.1f}" fill="{col}"/>'); dn += hgt
        tot = sum(s[1][i] for s in series)
        out.append(T(x+bw/2, up-9, fr(tot, 0), 5.4, fill=txt))
        if i % lab_every == 0 or i == n-1:
            out.append(T(x+bw/2, H-14, c, 5.4, fill=SLATE))
    out.append(f'<line x1="0" y1="{y0:.1f}" x2="{W}" y2="{y0:.1f}" stroke="#000" stroke-width="1.6"/>')
    return _svg(w, h, "".join(out))

def legend(items, txt=INK):
    return '<div style="font-size:6.2pt;margin-top:1.5mm;color:%s">' % txt + " ".join(
        f'<span style="display:inline-block;width:1.8mm;height:1.8mm;background:{c};margin:0 1.2mm 0 3mm;vertical-align:0"></span>{n}'
        for n, c in items) + "</div>"
