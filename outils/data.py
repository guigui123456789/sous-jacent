# -*- coding: utf-8 -*-
YEARS = list(range(2005, 2026))

CA = {2005:179351,2006:192047,2007:195827,2008:205368,2009:197959,2010:250733,
2011:252968,2012:218507,2013:199160,2014:225731,2015:220194,2016:200280,
2017:227830,2018:291220,2019:262977,2020:296576,2021:359364,2022:399079,
2023:405059,2024:359058,2025:407701}

GP = {2005:71407,2006:81836,2007:79009,2008:86285,2009:87594,2010:114520,
2011:106694,2012:91651,2013:81479,2014:97120,2015:99518,2016:91209,
2017:101656,2018:138971,2019:122966,2020:131447,2021:178200,2022:180559,
2023:204929,2024:183998,2025:259429}

ROP = {2005:3380,2006:-33182,2007:1071,2008:-1142,2009:4773,2010:29122,
2011:13686,2012:-2785,2013:-20467,2014:-14763,2015:-267,2016:-6314,
2017:-1360,2018:32059,2019:13821,2020:17368,2021:55602,2022:27201,
2023:51358,2024:-1310,2025:81828}

# elements non recurrents loges dans le resultat operationnel (signe = effet sur le ROP publie)
NR = {
 2005:[("Gain sur transactions judiciaires, net", "", 2250, "charges")],
 2006:[("Perte sur transaction judiciaire, net", "Ericsson", -37200, "charges")],
 2007:[("Gain sur transactions judiciaires, net", "", 1353, "charges")],
 2008:[("Gain sur transactions judiciaires, net", "", 177, "charges")],
 2009:[("Charges de restructuration", "", -4099, "charges"),
       ("Gain sur transactions judiciaires et autres, net", "", 846, "charges")],
 2012:[("Dépréciation d'écart d'acquisition", "filiale VJCL", -2012, "charges"),
       ("Gain sur transaction judiciaire", "assureurs", 1975, "charges")],
 2013:[("Charges de restructuration", "", -1361, "charges")],
 2014:[("Charges de restructuration et autres", "division Westcor", -2207, "charges")],
 2024:[("Provision pour litige", "SynQor", -19500, "charges")],
 2025:[("Règlement de litige de brevets encaissé", "partie non nommée", 45000, "produits")],
}

LICENCES = {2023:15872, 2024:46595, 2025:57384}

RD = {2009:31636,2010:35981,2011:38967,2012:38744,2013:39848,2014:41479,2015:41472,
2016:41848,2017:44924,2018:44286,2019:46588,2020:50916,2021:53114,2022:60594,
2023:67857,2024:68922,2025:78570}
RD.update({2005:29466,2006:31381,2007:30372,2008:31398})
SGA = {2009:47932,2010:49417,2011:54041,2012:55655,2013:60737,2014:68197,2015:58313,
2016:55675,2017:58092,2018:62224,2019:62557,2020:63163,2021:69484,2022:86264,
2023:85714,2024:96886,2025:99031}
SGA.update({2005:40811,2006:46437,2007:48919,2008:56206})

CFO = {2009:24798,2010:16894,2011:26407,2012:17238,2013:-4690,2016:544,2017:-2464,
2018:36171,2019:22211,2020:34742,2021:54444,2022:22939,2023:74528,2024:50842,2025:139548}
CAPEX = {2009:10643,2010:12103,2011:7466,2012:7396,2013:6179,2014:7128,2015:9090,
2016:8428,2017:12545,2018:18211,2019:12485,2020:28653,2021:47761,2022:63966,
2023:33452,2024:23602,2025:20318}

CAPITAUX = {2010:175031,2011:180945,2012:178352,2013:139176,2014:127772,2015:135031,
2016:130809,2017:136114,2018:183656,2019:205562,2020:350820,2021:423599,
2022:464088,2023:540869,2024:570071,2025:711557}
TRESO = {2008:22639,2009:40224,2010:49279,2011:71908,2012:84554,2013:56339,2014:55187,
2015:62980,2016:56170,2017:44230,2018:70557,2019:84668,2020:161742,2021:182418,
2022:190611,2023:242219,2024:277273,2025:402805}

def rop_courant(y):
    return ROP[y] - sum(m for _,_,m,_ in NR.get(y, []))

def marge_courante(y):
    return rop_courant(y) / CA[y] * 100

def marge_brute(y):
    """marge brute rapportee au seul chiffre d'affaires produit"""
    gp = GP[y] - sum(m for _,_,m,k in NR.get(y, []) if k == "produits")
    return gp / CA[y] * 100

def marge_brute_publiee(y):
    base = CA[y] + sum(m for _,_,m,k in NR.get(y, []) if k == "produits")
    return GP[y] / base * 100

# capital employe = capitaux propres + passifs - tresorerie (approx. capital employe net)
def capital_employe(y):
    if y not in CAPITAUX: return None
    return CAPITAUX[y] - TRESO.get(y, 0) + 0

def roic(y):
    """NOPAT / capital employe moyen, impot normatif 21 %"""
    ce0, ce1 = capital_employe(y-1), capital_employe(y)
    if ce0 is None or ce1 is None: return None
    ce = (ce0 + ce1) / 2
    if ce <= 0: return None
    return rop_courant(y) * 0.79 / ce * 100

# --- modele de valorisation (sceance du 16/10) ---
CA2026 = 639.8   # M$
CROISSANCE = [0.30,0.22,0.16,0.12,0.10,0.08,0.06,0.05,0.04]  # 2027-2035
MARGE_DEP, MARGE_NORM = 0.26, 0.33
IMPOT, ROTATION, WACC, G = 0.21, 2.6, 0.10, 0.03
ACTIONS = 46.0       # millions, dilue
TRESO_NETTE = 395.384  # M$
COURS = 202.40

def dcf(marge_norm=MARGE_NORM, wacc=WACC, rotation=ROTATION, croissance=None, g=G):
    cr = croissance if croissance is not None else CROISSANCE
    ca, va, ca_prec = CA2026, 0.0, CA2026
    n = len(cr)
    flux = []
    for i, c in enumerate(cr):
        ca = ca_prec * (1 + c)
        m = MARGE_DEP + (marge_norm - MARGE_DEP) * (i + 1) / n
        nopat = ca * m * (1 - IMPOT)
        reinv = (ca - ca_prec) / rotation
        fcf = nopat - reinv
        d = (1 + wacc) ** (i + 1)
        va += fcf / d
        flux.append((2026 + i + 1, ca, m, nopat, reinv, fcf, fcf / d))
        ca_prec = ca
    nopat_t = ca * marge_norm * (1 - IMPOT)
    reinv_t = ca * g / rotation
    vt = (nopat_t - reinv_t) * (1 + g) / (wacc - g)
    va_vt = vt / (1 + wacc) ** n
    ve = va + va_vt
    return dict(ve=ve, va_flux=va, va_vt=va_vt, vt=vt,
                par_action=(ve + TRESO_NETTE) / ACTIONS,
                part_vt=va_vt / ve * 100, flux=flux, ca_terminal=ca)
