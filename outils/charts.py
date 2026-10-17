# -*- coding: utf-8 -*-
import data as d

NAVY="#13263B"; GOLD="#B4913C"; TERRE="#9A5B3A"; GRID="#C3D0D0"; SOFT="#6F7F86"
SER="'Latin Modern Roman','TeX Gyre Termes',serif"; SANS="Inter,Helvetica,Arial,sans-serif"

def fr(x, dec=0):
    s=f"{x:,.{dec}f}".replace(",", " ").replace(".", ",")
    return s

def frame(w,h,body,title=None,legend=None):
    t=""
    if title:
        t=f'<text x="0" y="13" font-family="{SANS}" font-size="9.2" letter-spacing="0.09em" fill="{SOFT}">{title.upper()}</text>'
    lg=""
    if legend:
        x=0
        for lab,col in legend:
            lg+=f'<line x1="{x}" y1="31" x2="{x+16}" y2="31" stroke="{col}" stroke-width="1.6"/>'
            lg+=f'<text x="{x+21}" y="34.5" font-family="{SANS}" font-size="8.6" fill="{NAVY}">{lab}</text>'
            x+=26+len(lab)*4.55
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;height:auto;overflow:visible">{t}{lg}{body}</svg>')

def axes(x0,x1,y0,y1,vmin,vmax,ticks,fmt=lambda v:fr(v)):
    """grille horizontale seule + etiquettes a gauche"""
    out=[]
    for v in ticks:
        y=y1-(v-vmin)/(vmax-vmin)*(y1-y0)
        out.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{GRID}" stroke-width="0.6"/>')
        out.append(f'<text x="{x0-7}" y="{y+3:.1f}" text-anchor="end" font-family="{SANS}" font-size="8.4" fill="{SOFT}">{fmt(v)}</text>')
    return "".join(out)

def xlabels(years,x0,x1,ybase,every=5):
    out=[]; n=len(years)
    for i,y in enumerate(years):
        if y%every==0 or i==n-1 or i==0:
            x=x0+(x1-x0)*i/(n-1) if n>1 else x0
            out.append(f'<text x="{x:.1f}" y="{ybase}" text-anchor="middle" font-family="{SANS}" font-size="8.4" fill="{SOFT}">{y}</text>')
    return "".join(out)

# ---------- 1. chiffre d'affaires ----------
def ca_barres():
    W,H=660,268; x0,x1,y0,y1=46,650,54,228
    ys=d.YEARS; vmax=460000
    bw=(x1-x0)/len(ys)*0.62
    b=axes(x0,x1,y0,y1,0,vmax,[0,100000,200000,300000,400000],lambda v:fr(v/1000))
    for i,y in enumerate(ys):
        cx=x0+(x1-x0)*(i+0.5)/len(ys)
        v=d.CA[y]; h=v/vmax*(y1-y0)
        lic=d.LICENCES.get(y,0); hl=lic/vmax*(y1-y0)
        b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{NAVY}" opacity="0.88"/>'
        if lic:
            b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{hl:.1f}" fill="{GOLD}"/>'
    b+=f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{NAVY}" stroke-width="0.8"/>'
    b+=xlabels(ys,x0+ (x1-x0)*0.5/len(ys), x1-(x1-x0)*0.5/len(ys), y1+15)
    b+=f'<text x="{x0-7}" y="{y0-6}" text-anchor="end" font-family="{SANS}" font-size="8" fill="{SOFT}">M$</text>'
    return frame(W,H,b,"Chiffre d'affaires publié, 2005-2025",
                 [("Ventes de produits",NAVY),("Revenus de licence",GOLD)])

# ---------- 2. marge brute, deux presentations ----------
def marge_brute():
    W,H=660,250; x0,x1,y0,y1=46,650,54,210
    ys=d.YEARS; vmin,vmax=34,60
    def py(v): return y1-(v-vmin)/(vmax-vmin)*(y1-y0)
    def px(i): return x0+(x1-x0)*i/(len(ys)-1)
    b=axes(x0,x1,y0,y1,vmin,vmax,[35,40,45,50,55,60],lambda v:f"{int(v)} %")
    p1=" ".join(f"{px(i):.1f},{py(d.marge_brute(y)):.1f}" for i,y in enumerate(ys))
    p2=" ".join(f"{px(i):.1f},{py(d.marge_brute_publiee(y)):.1f}" for i,y in enumerate(ys))
    b+=f'<polyline points="{p2}" fill="none" stroke="{GOLD}" stroke-width="1.5" stroke-dasharray="3.5 2.6"/>'
    b+=f'<polyline points="{p1}" fill="none" stroke="{NAVY}" stroke-width="1.7"/>'
    i=len(ys)-1
    b+=f'<circle cx="{px(i):.1f}" cy="{py(52.6):.1f}" r="2.6" fill="{NAVY}"/>'
    b+=f'<circle cx="{px(i):.1f}" cy="{py(57.3):.1f}" r="2.6" fill="{GOLD}"/>'
    b+=(f'<line x1="{px(i)-8:.1f}" y1="{py(57.3):.1f}" x2="{px(i)-8:.1f}" y2="{py(52.6):.1f}" stroke="{TERRE}" stroke-width="1"/>'
        f'<text x="{px(i)-46:.1f}" y="{(py(57.3)+py(52.6))/2+3:.1f}" font-family="{SANS}" font-size="8.6" fill="{TERRE}">4,7 pts</text>')
    b+=xlabels(ys,x0,x1,y1+15)
    return frame(W,H,b,"Marge brute : l'écart de présentation",
                 [("Rapportée au seul chiffre d'affaires",NAVY),("Présentation de la société",GOLD)])

# ---------- 3. marge operationnelle publiee / courante ----------
def marge_op():
    W,H=660,268; x0,x1,y0,y1=46,650,54,214
    ys=d.YEARS; vmin,vmax=-18,22
    def py(v): return y1-(v-vmin)/(vmax-vmin)*(y1-y0)
    b=axes(x0,x1,y0,y1,vmin,vmax,[-15,-10,-5,0,5,10,15,20],lambda v:f"{int(v)} %")
    bw=(x1-x0)/len(ys)*0.34
    z=py(0)
    for i,y in enumerate(ys):
        cx=x0+(x1-x0)*(i+0.5)/len(ys)
        pub=d.ROP[y]/d.CA[y]*100; cour=d.marge_courante(y)
        for off,v,col in ((-bw*0.55,pub,"#9FB3BC"),(bw*0.55,cour,NAVY)):
            yy=py(v); b+=f'<rect x="{cx+off-bw/2:.1f}" y="{min(yy,z):.1f}" width="{bw:.1f}" height="{abs(yy-z):.1f}" fill="{col}"/>'
    b+=f'<line x1="{x0}" y1="{z:.1f}" x2="{x1}" y2="{z:.1f}" stroke="{NAVY}" stroke-width="0.8"/>'
    b+=xlabels(ys,x0+(x1-x0)*0.5/len(ys),x1-(x1-x0)*0.5/len(ys),y1+32)
    return frame(W,H,b,"Marge opérationnelle, publiée et retraitée",
                 [("Publiée",'#9FB3BC'),("Hors éléments non récurrents",NAVY)])

# ---------- 4. frais vs marge brute ----------
def frais():
    W,H=660,250; x0,x1,y0,y1=46,650,54,210
    ys=d.YEARS; vmin,vmax=34,58
    def py(v): return y1-(v-vmin)/(vmax-vmin)*(y1-y0)
    def px(i): return x0+(x1-x0)*i/(len(ys)-1)
    b=axes(x0,x1,y0,y1,vmin,vmax,[35,40,45,50,55],lambda v:f"{int(v)} %")
    p1=" ".join(f"{px(i):.1f},{py(d.marge_brute(y)):.1f}" for i,y in enumerate(ys))
    p2=" ".join(f"{px(i):.1f},{py((d.RD[y]+d.SGA[y])/d.CA[y]*100):.1f}" for i,y in enumerate(ys) if y in d.RD)
    b+=f'<polyline points="{p1}" fill="none" stroke="{NAVY}" stroke-width="1.7"/>'
    b+=f'<polyline points="{p2}" fill="none" stroke="{TERRE}" stroke-width="1.5"/>'
    b+=xlabels(ys,x0,x1,y1+15)
    return frame(W,H,b,"Les quatre points repris par les frais",
                 [("Marge brute, en % du CA",NAVY),("R&amp;D et frais généraux, en % du CA",TERRE)])

# ---------- 5. ROIC ----------
def roic_ch():
    W,H=660,240; x0,x1,y0,y1=46,650,54,196
    ys=[y for y in d.YEARS if d.roic(y) is not None]
    vmin,vmax=-14,24
    def py(v): return y1-(v-vmin)/(vmax-vmin)*(y1-y0)
    b=axes(x0,x1,y0,y1,vmin,vmax,[-10,0,10,20],lambda v:f"{int(v)} %")
    bw=(x1-x0)/len(ys)*0.5; z=py(0)
    for i,y in enumerate(ys):
        cx=x0+(x1-x0)*(i+0.5)/len(ys); v=d.roic(y); yy=py(v)
        b+=f'<rect x="{cx-bw/2:.1f}" y="{min(yy,z):.1f}" width="{bw:.1f}" height="{abs(yy-z):.1f}" fill="{NAVY if v>0 else TERRE}" opacity="0.9"/>'
    b+=f'<line x1="{x0}" y1="{z:.1f}" x2="{x1}" y2="{z:.1f}" stroke="{NAVY}" stroke-width="0.8"/>'
    b+=f'<line x1="{x0}" y1="{py(10):.1f}" x2="{x1}" y2="{py(10):.1f}" stroke="{GOLD}" stroke-width="0.9" stroke-dasharray="4 3"/>'
    b+=f'<text x="{x0+4}" y="{py(10)-5:.1f}" font-family="{SANS}" font-size="8.4" fill="{GOLD}">coût du capital retenu : 10 %</text>'
    b+=xlabels(ys,x0+(x1-x0)*0.5/len(ys),x1-(x1-x0)*0.5/len(ys),y1+30)
    return frame(W,H,b,"Rentabilité du capital employé, retraitée")

# ---------- 6. flux de tresorerie disponible ----------
def fcf_ch():
    W,H=660,236; x0,x1,y0,y1=46,650,54,194
    ys=[y for y in d.YEARS if y in d.CFO and y in d.CAPEX]
    vmin,vmax=-60,130
    def py(v): return y1-(v-vmin)/(vmax-vmin)*(y1-y0)
    b=axes(x0,x1,y0,y1,vmin,vmax,[-50,0,50,100],lambda v:fr(v))
    bw=(x1-x0)/len(ys)*0.5; z=py(0)
    for i,y in enumerate(ys):
        cx=x0+(x1-x0)*(i+0.5)/len(ys); v=(d.CFO[y]-d.CAPEX[y])/1000; yy=py(v)
        b+=f'<rect x="{cx-bw/2:.1f}" y="{min(yy,z):.1f}" width="{bw:.1f}" height="{abs(yy-z):.1f}" fill="{NAVY if v>0 else TERRE}" opacity="0.9"/>'
    b+=f'<line x1="{x0}" y1="{z:.1f}" x2="{x1}" y2="{z:.1f}" stroke="{NAVY}" stroke-width="0.8"/>'
    b+=xlabels(ys,x0+(x1-x0)*0.5/len(ys),x1-(x1-x0)*0.5/len(ys),y1+30)
    b+=f'<text x="{x0-7}" y="{y0-5}" text-anchor="end" font-family="{SANS}" font-size="8" fill="{SOFT}">M$</text>'
    return frame(W,H,b,"Flux de trésorerie disponible (exploitation moins investissements)")

# ---------- 7. trimestres 2026 ----------
def trimestres():
    W,H=560,236; x0,x1,y0,y1=52,548,54,192
    T=[("T1 2026",92.6,20.4,"publié"),("T2 2026",112.9,30.4,"publié"),
       ("T3 2026",121.0,65.4,"estimation auteur"),("T4 2026",126.0,71.0,"estimation auteur")]
    vmax=210
    b=axes(x0,x1,y0,y1,0,vmax,[0,50,100,150,200],lambda v:fr(v))
    bw=(x1-x0)/len(T)*0.46
    for i,(lab,p,r,note) in enumerate(T):
        cx=x0+(x1-x0)*(i+0.5)/len(T)
        hp=p/vmax*(y1-y0); hr=r/vmax*(y1-y0)
        b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-hp:.1f}" width="{bw:.1f}" height="{hp:.1f}" fill="{NAVY}" opacity="0.88"/>'
        b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-hp-hr:.1f}" width="{bw:.1f}" height="{hr:.1f}" fill="{GOLD}"/>'
        b+=f'<text x="{cx:.1f}" y="{y1-hp-hr-7:.1f}" text-anchor="middle" font-family="{SER}" font-size="13" fill="{NAVY}">{fr(p+r,1)}</text>'
        b+=f'<text x="{cx:.1f}" y="{y1+15}" text-anchor="middle" font-family="{SANS}" font-size="8.6" fill="{NAVY}">{lab}</text>'
        b+=f'<text x="{cx:.1f}" y="{y1+26}" text-anchor="middle" font-family="{SANS}" font-size="7.6" fill="{SOFT}">{note}</text>'
    b+=f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{NAVY}" stroke-width="0.8"/>'
    return frame(W,H,b,"Exercice 2026 : le point de départ du modèle, en M$",
                 [("Produits",NAVY),("Redevances de licence",GOLD)])

# ---------- 8. pont de valeur ----------
def pont():
    W,H=600,268; x0,x1,y0,y1=46,590,58,206
    base=d.dcf()['par_action']
    steps=[(("Modèle","central"),base,None),
           (("Croissance","plus forte"),52,GOLD),(("Marge normative","40 %"),32,GOLD),
           (("Coût du capital","9 %"),36,GOLD),(("Capital","plus léger"),6,GOLD)]
    vmax=260
    b=axes(x0,x1,y0,y1,0,vmax,[0,50,100,150,200,250],lambda v:fr(v)+" $")
    n=len(steps)+1; bw=(x1-x0)/n*0.54
    cum=0
    for i,(lab,val,col) in enumerate(steps):
        cx=x0+(x1-x0)*(i+0.5)/n
        if col is None:
            h=val/vmax*(y1-y0)
            b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{NAVY}"/>'
            b+=f'<text x="{cx:.1f}" y="{y1-h-7:.1f}" text-anchor="middle" font-family="{SER}" font-size="13" fill="{NAVY}">{fr(val)}</text>'
            cum=val
        else:
            h0=cum/vmax*(y1-y0); h=val/vmax*(y1-y0)
            b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h0-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{GOLD}" opacity="0.9"/>'
            b+=f'<text x="{cx:.1f}" y="{y1-h0-h-7:.1f}" text-anchor="middle" font-family="{SER}" font-size="12" fill="{GOLD}">+{fr(val)}</text>'
            cum+=val
        for k,part in enumerate(lab):
            b+=f'<text x="{cx:.1f}" y="{y1+14+k*9.4:.1f}" text-anchor="middle" font-family="{SANS}" font-size="7.8" fill="{SOFT}">{part}</text>'
    cx=x0+(x1-x0)*(n-0.5)/n; h=cum/vmax*(y1-y0)
    b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{TERRE}"/>'
    b+=f'<text x="{cx:.1f}" y="{y1-h-7:.1f}" text-anchor="middle" font-family="{SER}" font-size="13" fill="{TERRE}">{fr(cum)}</text>'
    b+=f'<text x="{cx:.1f}" y="{y1+14}" text-anchor="middle" font-family="{SANS}" font-size="7.8" fill="{SOFT}">Total</text>'
    yc=y1-d.COURS/vmax*(y1-y0)
    b+=f'<line x1="{x0}" y1="{yc:.1f}" x2="{x1}" y2="{yc:.1f}" stroke="{NAVY}" stroke-width="0.9" stroke-dasharray="4 3"/>'
    b+=f'<text x="{x0+4}" y="{yc-5:.1f}" font-family="{SANS}" font-size="8.4" fill="{NAVY}">cours du 16 octobre 2026 : 202,40 $</text>'
    b+=f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{NAVY}" stroke-width="0.8"/>'
    return frame(W,H,b,"Ce qu'il faut ajouter au modèle pour rejoindre le cours")

# ---------- 9. valorisation historique ----------
def ve_ca():
    W,H=560,210; x0,x1,y0,y1=46,548,54,168
    pts=[(2012,0.7),(2016,2.1),(2019,3.0),(2021,15.3),(2023,6.4),(2025,9.8),(2026,21.6)]
    vmax=24
    b=axes(x0,x1,y0,y1,0,vmax,[0,5,10,15,20],lambda v:f"{int(v)}x")
    bw=(x1-x0)/len(pts)*0.5
    for i,(y,v) in enumerate(pts):
        cx=x0+(x1-x0)*(i+0.5)/len(pts); h=v/vmax*(y1-y0)
        col=TERRE if y==2026 else NAVY
        b+=f'<rect x="{cx-bw/2:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{col}" opacity="0.9"/>'
        b+=f'<text x="{cx:.1f}" y="{y1-h-6:.1f}" text-anchor="middle" font-family="{SER}" font-size="12" fill="{col}">{str(v).replace(".",",")}x</text>'
        lab="16 oct. 2026" if y==2026 else str(y)
        b+=f'<text x="{cx:.1f}" y="{y1+14}" text-anchor="middle" font-family="{SANS}" font-size="8.2" fill="{SOFT}">{lab}</text>'
    med=y1-3.0/vmax*(y1-y0)
    b=f'<line x1="{x0}" y1="{med:.1f}" x2="{x1}" y2="{med:.1f}" stroke="{GOLD}" stroke-width="0.9" stroke-dasharray="4 3"/>'+b
    b+=f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{NAVY}" stroke-width="0.8"/>'
    return frame(W,H,b,"Valeur d'entreprise rapportée au chiffre d'affaires",
                 [("Multiple observé",NAVY),("Médiane 2005-2025 : 3,0x",GOLD)])

# ---------- facade gravee ----------
def facade(col="#13263B", w=118):
    s=f'<svg viewBox="0 0 200 150" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:auto">'
    g=f'stroke="{col}" fill="none" stroke-width="1.05" stroke-linecap="square"'
    s+=f'<g {g}>'
    s+='<path d="M14 58 L100 20 L186 58"/><path d="M22 58 L100 26 L178 58"/>'
    s+='<line x1="100" y1="12" x2="100" y2="20"/><circle cx="100" cy="9" r="2.6"/>'
    for i in range(9):
        x=26+i*18.5
        s+=f'<line x1="{x}" y1="62" x2="{x}" y2="116"/><line x1="{x+7}" y1="62" x2="{x+7}" y2="116"/>'
        s+=f'<rect x="{x-1.6}" y="58.5" width="10.2" height="4"/>'
        s+=f'<rect x="{x-1.6}" y="116" width="10.2" height="4"/>'
    s+='<line x1="10" y1="58" x2="190" y2="58"/><line x1="10" y1="54" x2="190" y2="54"/>'
    s+='<line x1="8" y1="121" x2="192" y2="121"/>'
    s+='<line x1="4" y1="128" x2="196" y2="128"/><line x1="0" y1="136" x2="200" y2="136"/>'
    s+='<line x1="2" y1="132" x2="198" y2="132"/>'
    s+='</g></svg>'
    return s

ALL = dict(ca=ca_barres, mb=marge_brute, mo=marge_op, frais=frais, roic=roic_ch,
           fcf=fcf_ch, tri=trimestres, pont=pont, veca=ve_ca)

# ---------- emblème sous-jacent (reprise de public/favicon.svg) ----------
def logo(mode="sombre", w=44):
    """mode 'sombre' : carré marine, traits crème — l'emblème du site.
       mode 'clair'  : traits crème seuls, pour fond marine."""
    if mode == "sombre":
        bg = '<rect width="40" height="40" rx="7" fill="#162b4b"/>'
        st = "#f4efe6"
    else:
        bg = ''
        st = "#C9A24B"
    return (f'<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:{w}px;height:{w}px;display:block">{bg}'
            f'<g fill="none" stroke="{st}" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M8.5 13.6 H 31.5" stroke-width="2.1" opacity="0.5"/>'
            f'<path d="M8.5 21 H 31.5" stroke-width="2.4" opacity="0.75"/>'
            f'<path d="M8.5 28.4 H 31.5" stroke-width="2.7"/>'
            f'<path d="M20 7 V 31.5" stroke-width="2.6"/>'
            f'<path d="M15.6 27.6 L 20 33.4 L 24.4 27.6" stroke-width="2.6"/></g></svg>')

def logo_mot(mode="sombre", w=40):
    """emblème + nom, pour la couverture"""
    col = "#13263B" if mode == "sombre" else "#EDE8DF"
    return (f'<div style="display:flex;align-items:center;gap:4mm;justify-content:center">'
            f'{logo(mode, w)}'
            f'<div style="font-family:\'Latin Modern Roman\',serif;font-size:21pt;color:{col};'
            f'letter-spacing:.01em">Sous-jacent</div></div>')
