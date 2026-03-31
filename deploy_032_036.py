#!/usr/bin/env python3
"""
VERDICT: Deploy #032-#036 (Phidata/Agno, MetaGPT, Rivet, BabyAGI, Voiceflow)
Run from ~/Desktop/verdict-index/
"""
import os

# === PAGE TEMPLATE (compressed) ===
PAGE_TPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://getverdict.fyi/{slug}/">
<meta property="og:type" content="article">
<link rel="canonical" href="https://getverdict.fyi/{slug}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;400;500;600;700&family=Libre+Franklin:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Merriweather:wght@400;700;900&display=swap" rel="stylesheet">
<style>
:root{{--white:#FFFFFF;--ice:#F5F6F8;--navy:#1B2A4A;--navy-light:#2A3D66;--heading:#1A1A2E;--body:#4A5060;--caption:#6B7280;--risk:#C4332B;--risk-bg:rgba(196,51,43,0.06);--caution:#C08520;--caution-bg:rgba(192,133,32,0.06);--safe:#2D7A4F;--divider:#E2E5EB;--serif:'Source Serif 4',Georgia,serif;--sans:'Libre Franklin',-apple-system,sans-serif;--mono:'JetBrains Mono',monospace;--score:'Merriweather',Georgia,serif;}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}body{{background:var(--white);color:var(--body);font-family:var(--sans);font-weight:400;line-height:1.6;}}a{{color:var(--navy);text-decoration:none;}}a:hover{{text-decoration:underline;}}header{{padding:0 2.5rem;height:58px;display:flex;align-items:center;justify-content:space-between;background:var(--white);border-bottom:1px solid var(--divider);}}.logo{{display:flex;align-items:baseline;gap:.75rem;text-decoration:none;}}.logo:hover{{text-decoration:none;}}.logo-mark{{font-family:var(--serif);font-size:1.25rem;font-weight:700;letter-spacing:.1em;color:var(--navy);}}.logo-sub{{font-family:var(--mono);font-size:.6rem;letter-spacing:.15em;color:var(--caption);text-transform:uppercase;}}.back{{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--caption);text-decoration:none;}}.back:hover{{color:var(--navy);}}.wrap{{max-width:960px;margin:0 auto;padding:4rem 2.5rem;}}.breadcrumb{{font-family:var(--mono);font-size:.65rem;color:var(--caption);margin-bottom:2rem;}}.breadcrumb a{{color:var(--caption);}}.breadcrumb a:hover{{color:var(--navy);}}h1{{font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.1;color:var(--heading);margin-bottom:.4rem;}}.meta{{font-family:var(--mono);font-size:.65rem;color:var(--caption);margin-bottom:.3rem;}}.meta-owner{{font-family:var(--mono);font-size:.62rem;color:var(--navy-light);margin-bottom:1.5rem;}}.score-hero{{display:flex;align-items:center;gap:2.5rem;margin-bottom:3rem;padding:2rem 0;border-top:1px solid var(--divider);border-bottom:1px solid var(--divider);}}.score-big{{font-family:var(--score);font-weight:900;font-size:4rem;line-height:1;color:var(--navy);}}.score-denom{{font-family:var(--mono);font-size:1.2rem;color:var(--caption);}}.score-meta{{font-family:var(--mono);font-size:.65rem;color:var(--caption);line-height:1.8;}}.finding{{font-size:.9rem;line-height:1.75;color:var(--body);border-left:3px solid var(--navy);padding-left:1rem;margin-bottom:2rem;}}.tags{{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:3rem;}}.tag{{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;padding:.3rem .7rem;border:1px solid;}}.tag-red{{border-color:rgba(196,51,43,.3);color:var(--risk);background:var(--risk-bg);}}.tag-amber{{border-color:rgba(192,133,32,.3);color:var(--caution);background:var(--caution-bg);}}.tag-dim{{border-color:var(--divider);color:var(--caption);background:var(--ice);}}.tag-safe{{border-color:rgba(45,122,79,.3);color:var(--safe);background:rgba(45,122,79,0.06);}}.radar-section{{display:flex;gap:3rem;align-items:flex-start;margin-bottom:3rem;flex-wrap:wrap;}}.radar-wrap{{width:260px;height:260px;flex-shrink:0;}}.radar-svg{{width:100%;height:100%;overflow:visible;}}.radar-ring{{fill:none;stroke:var(--divider);stroke-width:.5;}}.radar-axis{{stroke:var(--divider);stroke-width:.5;}}.radar-axis-inactive{{stroke:var(--divider);stroke-width:.5;stroke-dasharray:2 3;}}.radar-label{{font-family:var(--mono);font-size:10px;font-weight:500;fill:var(--navy);letter-spacing:.05em;}}.radar-label-inactive{{fill:var(--caption);}}.radar-poly-fill{{opacity:.14;}}.radar-poly-stroke{{fill:none;stroke-width:1.5;stroke-linejoin:round;}}.dim-list{{display:flex;flex-direction:column;gap:.7rem;flex:1;min-width:240px;}}.dim-row{{display:grid;grid-template-columns:16px 1fr 55px;align-items:center;gap:.6rem;}}.dim-letter{{font-family:var(--mono);font-size:.75rem;font-weight:600;color:var(--navy);}}.dim-letter.dim-inactive{{color:var(--caption);}}.dim-bar-track{{height:3px;background:var(--divider);overflow:hidden;}}.dim-bar-fill{{height:100%;background:var(--navy);}}.dim-bar-fill.fill-low{{background:var(--risk);}}.dim-bar-fill.fill-inactive{{background:repeating-linear-gradient(90deg,var(--divider) 0,var(--divider) 3px,transparent 3px,transparent 6px);}}.dim-val{{font-family:var(--mono);font-size:.7rem;font-weight:500;color:var(--caption);text-align:right;}}.dim-val.val-high{{color:var(--navy);}}.dim-val.val-inactive{{color:var(--divider);}}.cta-bar{{border-top:1px solid var(--divider);padding-top:2.5rem;margin-top:2rem;display:flex;gap:2rem;flex-wrap:wrap;}}.cta-link{{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--navy);padding:.5rem 1rem;border:1px solid var(--divider);text-decoration:none;transition:all .2s;}}.cta-link:hover{{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}}footer{{border-top:1px solid var(--divider);padding:2rem 2.5rem;max-width:960px;margin:0 auto;}}.footer-note{{font-family:var(--mono);font-size:.62rem;color:var(--caption);line-height:1.8;}}.footer-note a{{color:var(--navy);}}@media(max-width:700px){{.score-hero{{flex-direction:column;align-items:flex-start;gap:1rem;}}.radar-section{{flex-direction:column;}}.radar-wrap{{width:220px;height:220px;}}}}
</style>
</head>
<body>
<header><a href="/" class="logo"><span class="logo-mark">VERDICT</span><span class="logo-sub">AI Agent Trust Index</span></a><a href="/" class="back">&larr; All Evaluations</a></header>
<div class="wrap">
  <div class="breadcrumb"><a href="/">VERDICT</a> &rsaquo; Evaluations &rsaquo; {name}</div>
  <h1>{name}</h1>
  <div class="meta">{category}</div>
  <div class="meta">Evaluated 2026.03.31 &middot; Framework v0.3.1</div>
  <div class="meta-owner">{owner}</div>
  <div class="score-hero"><div><span class="score-big">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span></div><div class="score-meta">Layer 0 &middot; Public Documentation Only<br>Rank #{rank} of 36 platforms evaluated<br>Framework v0.3.1</div></div>
  <div class="finding">{finding}</div>
  <div class="tags">{tags_html}</div>
  <div class="radar-section">
    <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
        <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/><polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/><polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/><polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
        <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/><line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/><line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
        <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{radar_points}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{radar_points}"/></g>
        <text class="radar-label" x="120" y="22" text-anchor="middle">V</text><text class="radar-label radar-label-inactive" x="193" y="61" text-anchor="start">E</text><text class="radar-label" x="212" y="141" text-anchor="start">R</text><text class="radar-label" x="161" y="205" text-anchor="start">D</text><text class="radar-label" x="79" y="205" text-anchor="end">I</text><text class="radar-label" x="28" y="141" text-anchor="end">C</text><text class="radar-label" x="47" y="61" text-anchor="end">T</text>
    </svg></div>
    <div class="dim-list" id="dims" data-dims='{dims_json}'></div>
  </div>
  <div class="cta-bar"><a href="/" class="cta-link">View All 36 Evaluations</a><a href="/#subscribe" class="cta-link">Get Notified of Score Changes</a></div>
</div>
<footer><div class="footer-note">VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>{footer_bias}</div></footer>
<script>document.querySelectorAll('.dim-list').forEach(list=>{{const dims=JSON.parse(list.dataset.dims);dims.forEach(d=>{{const pct=d.inactive?100:Math.round((d.s/d.m)*100);const isLow=!d.inactive&&pct<30;const isHigh=!d.inactive&&pct>=65;const fillClass=d.inactive?'fill-inactive':isLow?'fill-low':'';const letterClass=d.inactive?'dim-inactive':'';const valClass=d.inactive?'val-inactive':isHigh?'val-high':'';const valText=d.inactive?'L1':d.s+'/'+d.m;list.innerHTML+='<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';}});}});</script>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}}'></script>
</body></html>"""

pages = [
    {"slug":"voiceflow","name":"Voiceflow","title":"Voiceflow Security Review — VERDICT Score: 52/85",
     "meta_desc":"Independent security evaluation of Voiceflow. Score: 52/85. SOC 2 + ISO 27001 + GDPR. I: 8/10 highest among conversational AI. Zero CVEs. Canadian company. Framework v0.3.1.",
     "category":"Conversational AI Agent Platform · Cloud SaaS","owner":"Voiceflow Inc. · Toronto, Canada",
     "score":52,"rank":11,
     "finding":"Triple certification: SOC 2 (Type 1, moving to Type 2) + ISO 27001 + GDPR. Highest I dimension (8/10) among conversational AI platforms — SSO/SAML, SCIM, RBAC, audit logs. HIPAA-aligned with PII redaction. Zero CVEs. V4: public cloud, VPC, or on-premise deployment options.",
     "tags_html":'<span class="tag tag-safe">SOC 2 + ISO 27001 + GDPR</span>\n    <span class="tag tag-safe">I: 8/10 · Conv. AI Highest</span>\n    <span class="tag tag-dim">0 CVEs · All Periods</span>\n    <span class="tag tag-dim">Closed Source · Canadian</span>\n    <span class="tag tag-amber">SOC 2 Type 1 · Not Yet Type 2</span>',
     "dims_json":'[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":10,"m":15},{"l":"I","s":8,"m":10,"high":true},{"l":"C","s":4,"m":10},{"l":"T","s":6,"m":10}]',
     "radar_points":"120.0,84.0 120.0,120.0 169.1,131.2 140.8,163.3 95.0,171.9 91.9,126.4 86.2,93.1",
     "footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"phidata","name":"Phidata (Agno)","title":"Phidata (Agno) Security Review — VERDICT Score: 38/85",
     "meta_desc":"Independent security evaluation of Phidata/Agno. Score: 38/85. Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON. Framework v0.3.1.",
     "category":"Multi-Agent Framework + AgentOS · Open Source (MPL 2.0)","owner":"Phidata Inc.",
     "score":38,"rank":27,
     "finding":"Zero CVEs. Self-hosted architecture: all agent data in user's own database. HITL and runtime approval as architectural primitives. Telemetry enabled by default (model usage to api.phidata.com). No privacy policy on agno.com. No SECURITY.md.",
     "tags_html":'<span class="tag tag-dim">MPL 2.0 · Self-Hosted</span>\n    <span class="tag tag-dim">0 CVEs · All Periods</span>\n    <span class="tag tag-safe">HITL · Architecture Primitive</span>\n    <span class="tag tag-red">Telemetry Default ON</span>\n    <span class="tag tag-amber">No Privacy Policy · No SECURITY.md</span>',
     "dims_json":'[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":3,"m":15,"low":true},{"l":"I","s":5,"m":10},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
     "radar_points":"120.0,80.4 120.0,120.0 169.1,131.2 126.2,133.0 104.4,152.4 98.9,124.8 108.7,111.0",
     "footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"rivet","name":"Rivet","title":"Rivet Security Review — VERDICT Score: 39/85",
     "meta_desc":"Independent security evaluation of Rivet by Ironclad. Score: 39/85. Zero CVEs. Local-first visual AI IDE. Corporate-backed ($3.2B+ Ironclad). MIT open source. Framework v0.3.1.",
     "category":"Visual AI Agent IDE · Open Source (MIT)","owner":"Ironclad Inc. · San Francisco",
     "score":39,"rank":26,
     "finding":"Visual AI programming environment backed by Ironclad ($3.2B+ CLM company). Zero CVEs. Local-first: all data processing on user's machine. Graphs stored as Git-controllable YAML. No SECURITY.md despite well-resourced corporate backer. Plugin system sandboxing undocumented.",
     "tags_html":'<span class="tag tag-dim">MIT · Ironclad ($3.2B+)</span>\n    <span class="tag tag-dim">0 CVEs · Local-First</span>\n    <span class="tag tag-dim">Visual Builder · YAML Graphs</span>\n    <span class="tag tag-amber">No SECURITY.md</span>\n    <span class="tag tag-amber">Plugin Sandbox Undocumented</span>',
     "dims_json":'[{"l":"V","s":14,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":5,"m":15},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":2,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
     "radar_points":"120.0,69.6 120.0,120.0 169.1,131.2 130.4,141.6 113.8,133.0 106.0,123.2 108.7,111.0",
     "footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"babyagi","name":"BabyAGI","title":"BabyAGI Security Review — VERDICT Score: 24/85",
     "meta_desc":"Independent security evaluation of BabyAGI. Score: 24/85. Experimental, not for production. Self-building agent with no containment. I/C/T all 0/10. Historical significance as first popular autonomous agent. Framework v0.3.1.",
     "category":"Experimental Autonomous Agent · Open Source (MIT)","owner":"Yohei Nakajima · Individual (VC)",
     "score":24,"rank":35,
     "finding":"Historical origin of the autonomous AI agent movement (March 2023, 22.2k stars). Explicitly not for production use. Self-building agent executes arbitrary LLM-generated code with no sandboxing. I, C, T dimensions all score 0/10 — unique in the index. Zero CVEs.",
     "tags_html":'<span class="tag tag-dim">MIT · Experimental Only</span>\n    <span class="tag tag-dim">22.2k Stars · Historical</span>\n    <span class="tag tag-red">I/C/T: All 0/10</span>\n    <span class="tag tag-red">Self-Building · No Sandbox</span>\n    <span class="tag tag-amber">Not for Production Use</span>',
     "dims_json":'[{"l":"V","s":8,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":0,"m":10,"low":true},{"l":"C","s":0,"m":10,"low":true},{"l":"T","s":0,"m":10,"low":true}]',
     "radar_points":"120.0,91.2 120.0,120.0 169.1,131.2 124.2,128.7 120.0,120.0 120.0,120.0 120.0,120.0",
     "footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"metagpt","name":"MetaGPT","title":"MetaGPT Security Review — VERDICT Score: 23/85",
     "meta_desc":"Independent security evaluation of MetaGPT by DeepWisdom. Score: 23/85. Four CVEs including two CVSS 9.8 Critical RCEs unpatched. Vendor unresponsive to disclosures. 66k stars. Framework v0.3.1.",
     "category":"Multi-Agent Software Development Framework · Open Source (MIT)","owner":"DeepWisdom · Shenzhen, China",
     "score":23,"rank":36,
     "finding":"66k GitHub stars and ICLR 2024 publication. Four CVEs in trailing 12 months including two CVSS 9.8 Critical RCEs (deserialization + code injection) — all unpatched. Vendor documented as unresponsive to multiple disclosure attempts. D dimension 0/15. No privacy policy, no certifications.",
     "tags_html":'<span class="tag tag-red">2x CVSS 9.8 RCE · Unpatched</span>\n    <span class="tag tag-red">4 CVEs · 12 Months</span>\n    <span class="tag tag-red">Vendor Unresponsive</span>\n    <span class="tag tag-red">D: 0/15</span>\n    <span class="tag tag-dim">MIT · 66k Stars · ICLR 2024</span>',
     "dims_json":'[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":4,"m":20,"low":true},{"l":"D","s":0,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":5,"m":10},{"l":"T","s":1,"m":10,"low":true}]',
     "radar_points":"120.0,80.4 120.0,120.0 134.0,123.2 120.0,120.0 113.8,133.0 84.9,128.0 114.4,115.5",
     "footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
]

# === GENERATE PAGES ===
for p in pages:
    os.makedirs(p["slug"], exist_ok=True)
    with open(os.path.join(p["slug"], "index.html"), 'w') as f:
        f.write(PAGE_TPL.format(**p))
    print(f"  ✓ {p['slug']}/index.html ({p['score']}/85, #{p['rank']})")
print()

# === UPDATE INDEX.HTML ===
with open('index.html', 'r') as f:
    html = f.read()

SVG = """        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
          <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/><polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/><polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/><polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/><line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/><line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
          <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{pts}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{pts}"/></g>
          <text class="radar-label" x="120" y="22" text-anchor="middle">V</text><text class="radar-label radar-label-inactive" x="197" y="64" text-anchor="start">E</text><text class="radar-label" x="215" y="144" text-anchor="start">R</text><text class="radar-label" x="164" y="213" text-anchor="start">D</text><text class="radar-label" x="76" y="213" text-anchor="end">I</text><text class="radar-label" x="25" y="144" text-anchor="end">C</text><text class="radar-label" x="43" y="64" text-anchor="end">T</text>
        </svg></div>"""

def card(comment, href, platform, name, cat, owner, date, finding, tags, dims, pts, score):
    return f"""
    <!-- {comment} -->
    <a class="eval-card" href="/{href}/" data-platform="{platform}">
      <div class="card-left">
        <div class="card-meta">
          <div class="platform-name">{name}</div>
          <div class="platform-category">{cat}</div>
          <div class="platform-owner">{owner}</div>
          <div class="platform-date">{date}</div>
          <div class="key-finding">{finding}</div>
          <div class="incident-tags">{tags}</div>
        </div>
        <div class="dim-list" data-dims='{dims}'></div>
      </div>
      <div class="card-right">
{SVG.format(pts=pts)}
        <div class="score-display"><span class="score-main">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span><div class="score-layer">Layer 0 &middot; Public Docs</div></div>
      </div>
    </a>
"""

# Voiceflow 52 → before LangChain 49 (after Activepieces 52, alphabetical)
c = card("Voiceflow 52","voiceflow","voiceflow","Voiceflow","Conversational AI · Cloud SaaS","Voiceflow Inc. · Toronto, Canada","Evaluated 2026.03.31 · Framework v0.3.1",
    "SOC 2 + ISO 27001 + GDPR. I: 8/10 highest conv. AI. HIPAA-aligned. PII redaction. Zero CVEs.",
    '<span class="tag tag-dim">SOC 2 + ISO 27001 + GDPR</span>\n            <span class="tag tag-dim">I: 8/10 · Conv. AI Highest</span>\n            <span class="tag tag-amber">SOC 2 Type 1</span>',
    '[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":10,"m":15},{"l":"I","s":8,"m":10,"high":true},{"l":"C","s":4,"m":10},{"l":"T","s":6,"m":10}]',
    "120.0,84.0 120.0,120.0 169.1,131.2 140.8,163.3 95.0,171.9 91.9,126.4 86.2,93.1",52)
m = '    <!-- LangChain 49 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Voiceflow inserted")

# Rivet 39 → before AG2 40? No, Rivet is 39, goes before Phidata 38 which goes before Letta 37
# Actually: AG2(40) > Rivet(39) > Phidata(38) > Letta(37)
# Insert Rivet before Phidata, and Phidata before Letta
# But we need to insert both. Insert Rivet before Letta first, then Phidata before Letta
# Actually: insert in reverse score order before Letta marker

# Phidata 38 → before Letta 37
c = card("Phidata 38","phidata","phidata","Phidata (Agno)","Multi-Agent Framework · OSS (MPL 2.0)","Phidata Inc.","Evaluated 2026.03.31 · Framework v0.3.1",
    "Zero CVEs. Self-hosted data sovereignty. HITL as architecture primitive. Telemetry default ON.",
    '<span class="tag tag-dim">MPL 2.0 · Self-Hosted</span>\n            <span class="tag tag-red">Telemetry Default ON</span>\n            <span class="tag tag-amber">No SECURITY.md</span>',
    '[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":3,"m":15,"low":true},{"l":"I","s":5,"m":10},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
    "120.0,80.4 120.0,120.0 169.1,131.2 126.2,133.0 104.4,152.4 98.9,124.8 108.7,111.0",38)
m = '    <!-- Letta 37 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Phidata inserted")

# Rivet 39 → before Phidata 38 (which we just inserted before Letta)
c = card("Rivet 39","rivet","rivet","Rivet","Visual AI Agent IDE · OSS (MIT)","Ironclad Inc. · San Francisco","Evaluated 2026.03.31 · Framework v0.3.1",
    "Ironclad ($3.2B+) backed. Local-first. Zero CVEs. YAML graphs + Git. No SECURITY.md.",
    '<span class="tag tag-dim">MIT · Ironclad ($3.2B+)</span>\n            <span class="tag tag-dim">Local-First · Zero CVEs</span>\n            <span class="tag tag-amber">No SECURITY.md</span>',
    '[{"l":"V","s":14,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":5,"m":15},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":2,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
    "120.0,69.6 120.0,120.0 169.1,131.2 130.4,141.6 113.8,133.0 106.0,123.2 108.7,111.0",39)
m = '    <!-- Phidata 38 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Rivet inserted")

# BabyAGI 24 → before MetaGPT. But MetaGPT doesn't exist yet.
# Both go after Langflow (30). Insert MetaGPT after Langflow, then BabyAGI before MetaGPT.
# Find end of Langflow card - look for the closing </a> after Langflow
# Actually, simpler: find the section closing div after the last card
# Let's insert before the closing of the evaluations section

# First insert MetaGPT at the very end (before section close)
# Find the last card's closing tag area. Look for <!-- Langflow 30 --> card
# Insert both after the Langflow card block

# Strategy: find Langflow card end, insert BabyAGI then MetaGPT after it
# But we need markers. Let's find a reliable end marker.
# The cards section ends with </div> that closes the eval-grid.
# Let's look for a pattern after the last card.

# Alternative: insert before Flowise (33), which puts them at wrong position
# BabyAGI(24) and MetaGPT(23) go AFTER Langflow(30)
# We need to append after the last card.

# Find the Langflow card's closing </a> tag and insert after it
langflow_marker = '    <!-- Langflow 30 -->'
langflow_pos = html.find(langflow_marker)
if langflow_pos != -1:
    # Find the closing </a> of the Langflow card
    next_close = html.find('</a>', langflow_pos)
    if next_close != -1:
        insert_after = next_close + len('</a>')
        # BabyAGI card
        babyagi_card = card("BabyAGI 24","babyagi","babyagi","BabyAGI","Experimental Autonomous Agent · OSS (MIT)","Yohei Nakajima · Individual","Evaluated 2026.03.31 · Framework v0.3.1",
            "First popular autonomous agent (2023). Experimental only. Self-building agent, no containment. I/C/T: all 0.",
            '<span class="tag tag-dim">MIT · 22.2k Stars</span>\n            <span class="tag tag-red">I/C/T: All 0/10</span>\n            <span class="tag tag-amber">Not for Production</span>',
            '[{"l":"V","s":8,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":0,"m":10,"low":true},{"l":"C","s":0,"m":10,"low":true},{"l":"T","s":0,"m":10,"low":true}]',
            "120.0,91.2 120.0,120.0 169.1,131.2 124.2,128.7 120.0,120.0 120.0,120.0 120.0,120.0",24)
        # MetaGPT card
        metagpt_card = card("MetaGPT 23","metagpt","metagpt","MetaGPT","Multi-Agent Dev Framework · OSS (MIT)","DeepWisdom · Shenzhen, China","Evaluated 2026.03.31 · Framework v0.3.1",
            "66k stars, ICLR 2024. Two CVSS 9.8 RCEs unpatched. Vendor unresponsive. D: 0/15. Four CVEs in 12 months.",
            '<span class="tag tag-red">2x CVSS 9.8 · Unpatched</span>\n            <span class="tag tag-red">Vendor Unresponsive</span>\n            <span class="tag tag-red">D: 0/15</span>\n            <span class="tag tag-dim">MIT · 66k Stars</span>',
            '[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":4,"m":20,"low":true},{"l":"D","s":0,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":5,"m":10},{"l":"T","s":1,"m":10,"low":true}]',
            "120.0,80.4 120.0,120.0 134.0,123.2 120.0,120.0 113.8,133.0 84.9,128.0 114.4,115.5",23)
        html = html[:insert_after] + '\n' + babyagi_card + metagpt_card + html[insert_after:]
        print("  ✓ BabyAGI + MetaGPT inserted after Langflow")

# Hero stat 31 → 36
html = html.replace('<span class="stat-num">31<span> / 100</span></span>','<span class="stat-num">36<span> / 100</span></span>')
print("  ✓ Hero stat: 31 → 36")

with open('index.html','w') as f: f.write(html)
print("  ✓ index.html saved")

# === SITEMAP ===
new_urls = """  <url><loc>https://getverdict.fyi/voiceflow/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/phidata/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/rivet/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/babyagi/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/metagpt/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
"""
with open('sitemap.xml','r') as f: s=f.read()
s=s.replace('</urlset>',new_urls+'</urlset>')
with open('sitemap.xml','w') as f: f.write(s)
print("  ✓ sitemap.xml: 5 URLs added")

# === RANK UPDATES ===
# 36-platform ranking changes from 31-platform:
# 1-10: no rank change (Amazon Q through Activepieces)
# NEW: Voiceflow at 11
# 11→12: LangChain
# 12→13: IBM watsonx
# 13→14: Zapier
# 14→15: Haystack
# 15→16: Composio
# 16→17: Dify
# 17→18: Make.com
# 18→19: Semantic Kernel
# 19→20: Botpress
# 20→21: CrewAI
# 21→22: Relevance AI
# 22→23: Superagent
# 23→24: LlamaIndex
# 24→25: AG2
# NEW: Rivet at 26
# NEW: Phidata at 27
# 25→28: Letta
# 26→29: Coze
# 27→30: n8n
# 28→31: Wordware
# 29→32: Langroid
# 30→33: Flowise
# 31→34: Langflow
# NEW: BabyAGI at 35
# NEW: MetaGPT at 36

rank_changes = {
    "langchain":(11,12),"watsonx-orchestrate":(12,13),"zapier":(13,14),
    "haystack":(14,15),"composio":(15,16),"dify":(16,17),
    "make":(17,18),"semantic-kernel":(18,19),"botpress":(19,20),
    "crewai":(20,21),"relevance-ai":(21,22),"superagent":(22,23),
    "llamaindex":(23,24),"ag2":(24,25),
    "letta":(25,28),"coze":(26,29),"n8n":(27,30),
    "wordware":(28,31),"langroid":(29,32),"flowise":(30,33),"langflow":(31,34),
}

# Pages with no rank change but need count update
no_rank_change = ["amazon-q-business","vertex-ai","copilot-studio","openai-assistants",
    "agentforce","dust","autogen","pipedream","bedrock-agents","activepieces"]

for dirname in no_rank_change:
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 31 platforms evaluated","of 36 platforms evaluated")
    c=c.replace("All 31 Evaluations","All 36 Evaluations")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        print(f"  ✓ {fp}: count→36")

for dirname,(old_r,new_r) in rank_changes.items():
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 31 platforms evaluated","of 36 platforms evaluated")
    c=c.replace("All 31 Evaluations","All 36 Evaluations")
    c=c.replace(f"Rank #{old_r} of",f"Rank #{new_r} of")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        print(f"  ✓ {fp}: #{old_r}→#{new_r}, count→36")

print("\nDone. git add . && git commit && git push")
