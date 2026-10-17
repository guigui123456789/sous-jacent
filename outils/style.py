CSS = r"""
:root{
  --eggshell:#DCE6E6; --cream:#FAF7F2; --navy:#0E1F35; --navy2:#122236;
  --ink:#13263B; --gold:#B4913C; --gold-l:#C9A24B; --terre:#9A5B3A;
  --soft:#6F7F86; --rule:#BCCBCB; --rule-c:#DDD6CA;
}
@page{ size:A4; margin:0; }
*{ box-sizing:border-box; }
html,body{ margin:0; padding:0; }
body{
  font-family:Inter,Helvetica,Arial,sans-serif;
  color:var(--ink); background:#8e9a9a;
  -webkit-font-smoothing:antialiased; font-size:9.6pt;
}
.page{
  position:relative; width:210mm; height:297mm; overflow:hidden;
  background:var(--cream); margin:0 auto 6mm; page-break-after:always;
  padding:26mm 22mm 18mm;
}
.page:last-child{ page-break-after:auto; }
.page.egg{ background:var(--eggshell); }
.page.navy{ background:var(--navy); color:#EDE8DF; }
.page.cream{ background:var(--cream); }

/* --- typographie --- */
.serif{ font-family:'Latin Modern Roman','TeX Gyre Termes',Georgia,serif; }
h1,h2,h3,.kpi-v,.quote,.lead,.chapno{ font-family:'Latin Modern Roman','TeX Gyre Termes',Georgia,serif; font-weight:400; }
.eyebrow{
  font-size:7.6pt; letter-spacing:.20em; text-transform:uppercase;
  color:var(--soft); margin:0 0 7mm;
}
.page.navy .eyebrow{ color:#9FB2C2; }
.rule-v{ width:3px; height:12mm; background:var(--ink); opacity:.55; margin:0 0 7mm; }
.page.navy .rule-v{ background:var(--gold-l); opacity:.9; }
.ctr{ text-align:center; }
.ctr .rule-v{ margin:0 auto 7mm; }
h1{ font-size:30pt; line-height:1.1; letter-spacing:.005em; margin:0 0 6mm; }
h2{ font-size:19pt; line-height:1.18; margin:0 0 5mm; letter-spacing:.005em; }
h3{ font-size:11.4pt; margin:7mm 0 2.5mm; letter-spacing:.01em; }
.page.navy h1,.page.navy h2{ color:var(--gold-l); }
p{ line-height:1.62; margin:0 0 3.6mm; text-align:justify; hyphens:auto; }
.lead{ font-size:13pt; line-height:1.5; font-style:italic; text-align:left; }
.small{ font-size:8.2pt; color:var(--soft); line-height:1.5; }
.note{ font-size:7.8pt; color:var(--soft); line-height:1.5; text-align:left; }
b,strong{ font-weight:600; }
em{ font-style:italic; }
.srcline{ font-size:7.4pt; color:var(--soft); margin-top:2.5mm; font-style:italic; }

/* --- pied de page --- */
.foot{
  position:absolute; left:22mm; right:22mm; bottom:10mm;
  display:flex; justify-content:space-between; align-items:baseline;
  font-size:7pt; color:var(--soft); letter-spacing:.02em;
}
.foot b{ color:var(--ink); font-weight:600; }
.page.navy .foot{ color:#8FA2B2; } .page.navy .foot b{ color:#D9E2EA; }

/* --- couverture --- */
.cover{ display:flex; flex-direction:column; align-items:center; justify-content:center; padding-top:0; }
.cover .brand{ font-size:21pt; border-top:1.1px solid var(--ink); border-bottom:1.1px solid var(--ink); padding:2.2mm 6mm; }
.cover .mg{ font-size:8pt; letter-spacing:.04em; margin-top:3.5mm; color:var(--soft); text-align:center; line-height:1.5; }
.cover .emblem{ margin:30mm 0 26mm; opacity:.9; }
.cover .t1{ font-size:19pt; } .cover .t2{ font-size:12.4pt; margin-top:2mm; }

/* --- KPI --- */
.kpis{ display:grid; grid-template-columns:1fr 1px 1fr; row-gap:13mm; margin-top:10mm; }
.kpi{ text-align:center; padding:0 6mm; }
.kpi-v{ font-size:34pt; line-height:1; letter-spacing:-.01em; }
.kpi-v.sm{ font-size:27pt; }
.kpi-l{ font-size:8pt; color:var(--ink); margin-top:3mm; line-height:1.45; }
.vsep{ background:var(--rule); width:1px; }
.hr-strong{ border:0; border-top:1.4px solid var(--ink); margin:0 0 6mm; }
.hr-thin{ border:0; border-top:1px solid var(--rule); margin:6mm 0; }
.page.cream .hr-thin{ border-color:var(--rule-c); }

/* --- tableaux --- */
table{ width:100%; border-collapse:collapse; font-size:8.3pt; margin:3mm 0 2mm; }
caption{ caption-side:top; text-align:left; font-size:8.6pt; font-weight:600; padding-bottom:2mm; }
th{ font-weight:600; text-align:right; padding:1.7mm 2mm; border-bottom:1px solid var(--ink); font-size:7.9pt; }
th:first-child{ text-align:left; }
td{ text-align:right; padding:1.5mm 2mm; border-bottom:.6px solid var(--rule); }
.page.cream td{ border-bottom-color:var(--rule-c); }
td:first-child{ text-align:left; }
tr.total td{ font-weight:600; border-top:1px solid var(--ink); border-bottom:none; }
tbody tr:nth-child(even){ background:rgba(19,38,59,.035); }
table.plain tbody tr:nth-child(even){ background:none; }
.num{ font-variant-numeric:tabular-nums; }
td.hi,th.hi{ color:var(--terre); font-weight:600; }

/* --- encadre pedagogique --- */
.boxed{
  border-top:1.2px solid var(--gold); border-bottom:.8px solid var(--rule-c);
  padding:4mm 0 3.5mm; margin:6mm 0;
}
.boxed .t{ font-size:7.4pt; letter-spacing:.17em; text-transform:uppercase; color:var(--gold); margin-bottom:2.5mm; }
.boxed p{ font-size:8.5pt; line-height:1.55; margin-bottom:2mm; }
.boxed .f{ font-family:'Latin Modern Roman',serif; font-style:italic; font-size:9.6pt; text-align:center; margin:2.5mm 0; }

/* --- citation --- */
.quote{ font-size:13pt; line-height:1.48; font-style:italic; border-left:1px solid var(--rule); padding-left:6mm; margin:6mm 0; }
.page.navy .quote{ border-left-color:rgba(201,162,75,.6); }

/* --- chapitre --- */
.chapter{ position:relative; display:flex; flex-direction:column; height:100%; justify-content:center; padding-bottom:16mm; }
.chapno{ font-size:40pt; color:var(--gold-l); line-height:1; margin-bottom:6mm; }
.chaplist{ margin-top:14mm; border-top:1px solid rgba(201,162,75,.35); padding-top:5mm; }
.chaplist div{ font-size:9pt; color:#C8D3DD; padding:1.6mm 0; display:flex; gap:5mm; }
.chaplist span{ color:var(--gold-l); min-width:7mm; }
.colonnade{ position:absolute; left:50%; transform:translateX(-50%); bottom:-26mm; opacity:.11; pointer-events:none; }

/* --- deux colonnes --- */
.two{ display:grid; grid-template-columns:1fr 1fr; gap:9mm; }
.fig{ margin:5mm 0 3mm; }
.figcap{ font-size:7.6pt; color:var(--soft); line-height:1.45; margin-top:1.5mm; }
.toc div{ display:flex; align-items:baseline; gap:3mm; font-size:8.5pt; padding:1.15mm 0; border-bottom:.6px solid var(--rule); }
.toc .n{ color:var(--gold); min-width:9mm; font-family:'Latin Modern Roman',serif; }
.toc .d{ flex:1; border-bottom:.6px dotted transparent; }
.toc .p{ color:var(--soft); font-size:8.4pt; }
.toc .sec{ margin-top:3.4mm; font-size:7.6pt; letter-spacing:.18em; text-transform:uppercase; color:var(--soft); border:none; padding-bottom:1mm; }
.watermark{ position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); opacity:.07; }
"""

CSS += r"""
/* ====== photographie ====== */
.page.photo{ background:var(--navy); color:#EDE8DF; padding:0; }
.photo-bg{ position:absolute; inset:0; background-size:cover; background-position:center; }
.photo-veil{ position:absolute; inset:0;
  background:linear-gradient(180deg, rgba(10,24,42,.62) 0%, rgba(10,24,42,.78) 52%, rgba(8,19,34,.94) 100%); }
.photo-inner{ position:absolute; inset:0; padding:26mm 22mm 20mm; display:flex; flex-direction:column; justify-content:center; }
.page.photo .eyebrow{ color:#B3C4D3; }
.page.photo .rule-v{ background:var(--gold-l); opacity:.95; }
.page.photo h1{ color:var(--gold-l); font-size:33pt; }
.page.photo .quote{ border-left-color:rgba(201,162,75,.55); color:#E6E1D7; }
.page.photo .chaplist{ border-top:1px solid rgba(201,162,75,.38); }
.page.photo .chaplist div{ color:#D2DBE3; }
.page.photo .chaplist span{ color:var(--gold-l); }
.page.photo .foot{ color:#93A6B6; } .page.photo .foot b{ color:#DCE4EB; }
.mark{ position:absolute; top:20mm; right:22mm; }

/* ====== page vedette : photo en demi-fond perdu ====== */
.page.feature{ padding:0; background:var(--cream); display:flex; align-items:stretch; }
.feat-img{ flex:0 0 62mm; background-size:cover; background-position:center; }
.feat-body{ flex:1 1 auto; min-width:0; position:relative; padding:26mm 22mm 20mm 14mm; }
.page.feature .foot{ left:76mm; }

/* ====== panneau photo en tête de page ====== */
.panel{ position:relative; margin:0 0 7mm; height:62mm; background-size:cover; background-position:center;
  display:flex; align-items:flex-end; padding:7mm; }
.panel .pt{ font-family:'Latin Modern Roman',serif; font-size:27pt; color:#F0EBE1; line-height:1.1; }
.panel .pm{ position:absolute; top:6mm; right:6mm; }

/* ====== bande photo ====== */
.band{ height:34mm; background-size:cover; background-position:center; margin:6mm 0; }
.bandcap{ font-size:7.4pt; color:var(--soft); font-style:italic; margin-top:1.5mm; }

/* ====== couverture ====== */
.cover-mark{ margin-bottom:4mm; }
"""

CSS += r"""
/* ====== filigrane de propriété ====== */
.filigrane{
  position:absolute; inset:0; pointer-events:none; overflow:hidden; z-index:5;
  display:flex; align-items:center; justify-content:center;
}
.filigrane .bloc{
  transform:rotate(-30deg); text-align:center; white-space:nowrap;
  color:var(--ink); opacity:.105;
}
.filigrane .mot{
  font-family:'Latin Modern Roman',serif; font-size:54pt;
  letter-spacing:.10em; line-height:1;
}
.filigrane .url{
  font-family:Inter,Helvetica,Arial,sans-serif; font-size:9.6pt;
  letter-spacing:.44em; text-transform:uppercase; margin-top:3.5mm;
  padding-left:.44em;
}
.page.navy .filigrane .bloc,.page.photo .filigrane .bloc{ color:#D7E2EE; opacity:.11; }
.page.photo .photo-inner,.page.feature .feat-body{ position:relative; z-index:6; }

/* ====== rendu papier : aucun liseré entre les pages ====== */
@media print{
  body{ background:#fff; }
  .page{ margin:0 !important; box-shadow:none !important; }
}
.copyright{
  border-top:1.2px solid var(--gold); padding-top:3.5mm; margin-top:5mm;
}
.copyright .t{ font-size:7.4pt; letter-spacing:.17em; text-transform:uppercase; color:var(--gold); margin-bottom:2.5mm; }
.copyright p{ font-size:8.2pt; line-height:1.55; margin-bottom:2mm; }
"""
