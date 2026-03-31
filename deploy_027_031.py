#!/usr/bin/env python3
"""
VERDICT: Deploy #027-#031 (AG2, Langroid, Dust, Wordware, Superagent)
Run from ~/Desktop/verdict-index/
"""
import os, re

# === PAGE TEMPLATE ===
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
  <div class="score-hero"><div><span class="score-big">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span></div><div class="score-meta">Layer 0 &middot; Public Documentation Only<br>Rank #{rank} of 31 platforms evaluated<br>Framework v0.3.1</div></div>
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
  <div class="cta-bar"><a href="/" class="cta-link">View All 31 Evaluations</a><a href="/#subscribe" class="cta-link">Get Notified of Score Changes</a></div>
</div>
<footer><div class="footer-note">VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>{footer_bias}</div></footer>
<script>document.querySelectorAll('.dim-list').forEach(list=>{{const dims=JSON.parse(list.dataset.dims);dims.forEach(d=>{{const pct=d.inactive?100:Math.round((d.s/d.m)*100);const isLow=!d.inactive&&pct<30;const isHigh=!d.inactive&&pct>=65;const fillClass=d.inactive?'fill-inactive':isLow?'fill-low':'';const letterClass=d.inactive?'dim-inactive':'';const valClass=d.inactive?'val-inactive':isHigh?'val-high':'';const valText=d.inactive?'L1':d.s+'/'+d.m;list.innerHTML+='<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';}});}});</script>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}}'></script>
</body></html>"""

pages = [
    {"slug":"dust","name":"Dust","title":"Dust Security Review — VERDICT Score: 55/85","meta_desc":"Independent security evaluation of Dust. Score: 55/85. SOC 2 Type II, GDPR (French company). Highest data conduct score in index (13/15). Zero CVEs. Framework v0.3.1.","category":"Enterprise AI Assistant · Open Source + Cloud SaaS","owner":"Dust SAS · Paris, France","score":55,"rank":9,"finding":"SOC 2 Type II, GDPR-compliant French company, HIPAA-ready. Highest data conduct score in the index (13/15). Zero data retention from model providers. Customer data never used for training. Zero CVEs. Score moderated by limited public transparency documentation and undocumented agent action containment.","tags_html":'<span class="tag tag-safe">SOC 2 Type II · GDPR Native</span>\n    <span class="tag tag-safe">D: 13/15 · Highest in Index</span>\n    <span class="tag tag-safe">Zero Data Retention · Providers</span>\n    <span class="tag tag-dim">0 CVEs · All Periods</span>\n    <span class="tag tag-amber">No SECURITY.md · No VDP</span>',"dims_json":'[{"l":"V","s":13,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":17,"m":20,"high":true},{"l":"D","s":13,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',"radar_points":"120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 108.7,111.0","footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"ag2","name":"AG2","title":"AG2 (AutoGen Fork) Security Review — VERDICT Score: 40/85","meta_desc":"Independent security evaluation of AG2 (AutoGen fork). Score: 40/85. Zero AG2-specific CVEs. No MSRC coverage. PyPI namespace governance concern. Community-maintained. Framework v0.3.1.","category":"Multi-Agent Orchestration Framework · Open Source (Apache 2.0)","owner":"AG2AI Inc. · Community Governance","score":40,"rank":24,"finding":"Community fork of Microsoft AutoGen. Zero AG2-specific CVEs. Inherits Docker code execution from AutoGen. No MSRC coverage (16-point gap vs AutoGen 56/85). Controls autogen/pyautogen PyPI namespaces — unique supply chain governance concern. No SECURITY.md.","tags_html":'<span class="tag tag-dim">Apache 2.0 · AutoGen Fork</span>\n    <span class="tag tag-dim">0 CVEs · AG2-Specific</span>\n    <span class="tag tag-amber">No MSRC Coverage</span>\n    <span class="tag tag-amber">PyPI Namespace Governance</span>\n    <span class="tag tag-amber">No SECURITY.md</span>',"dims_json":'[{"l":"V","s":12,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":5,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":2,"m":10,"low":true}]',"radar_points":"120.0,76.8 120.0,120.0 169.1,131.2 130.4,141.6 110.6,139.5 91.9,126.4 108.7,111.0","footer_bias":"Evaluation tooling uses Claude (Anthropic). Anthropic competes with Microsoft (AutoGen origin). Bias disclosures in full reports."},
    {"slug":"langroid","name":"Langroid","title":"Langroid Security Review — VERDICT Score: 34/85","meta_desc":"Independent security evaluation of Langroid. Score: 34/85. CVE-2026-25481 CVSS 9.4 Critical RCE. Highest transparency (T: 8/10) among OSS frameworks. CMU origin. Framework v0.3.1.","category":"Multi-Agent LLM Framework · Open Source (MIT)","owner":"Prasad Chalasani (CMU) · Individual","score":34,"rank":29,"finding":"CVE-2026-25481 (CVSS 9.4 Critical RCE in TableChatAgent) within evaluation window. Recurring code injection pattern in same component. Despite this, transparency score 8/10 is highest among OSS frameworks — maintainer published the CVE himself with fix available at disclosure. 48-hour response commitment.","tags_html":'<span class="tag tag-red">CVE-2026-25481 · CVSS 9.4 RCE</span>\n    <span class="tag tag-red">Code Injection · Recurring Pattern</span>\n    <span class="tag tag-safe">T: 8/10 · OSS Transparency Leader</span>\n    <span class="tag tag-dim">MIT · CMU/UW-Madison</span>',"dims_json":'[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":5,"m":20,"low":true},{"l":"D","s":6,"m":15},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":8,"m":10,"high":true}]',"radar_points":"120.0,84.0 120.0,120.0 137.6,124.0 132.5,146.0 113.8,133.0 98.9,124.8 75.0,84.1","footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"wordware","name":"Wordware","title":"Wordware Security Review — VERDICT Score: 35/85","meta_desc":"Independent security evaluation of Wordware. Score: 35/85. Zero CVEs. $30M seed (YC/Spark Capital). Minimal privacy policy. Closed-source AI agent IDE. Framework v0.3.1.","category":"AI Agent IDE · Cloud SaaS","owner":"HeyDaily Inc. (DBA Wordware) · San Francisco","score":35,"rank":28,"finding":"Zero CVEs. $30M seed from Spark Capital, Felicis, YC. Trust center with SOC 2 reference. Twitter personality app handled 1M users without incidents. Minimal privacy policy — no DPA, no DPO, ambiguous AI training language. Sauna product connects to enterprise tools with undocumented permission scope.","tags_html":'<span class="tag tag-dim">0 CVEs · All Periods</span>\n    <span class="tag tag-dim">$30M Seed · YC W24</span>\n    <span class="tag tag-amber">Minimal Privacy Policy</span>\n    <span class="tag tag-amber">AI Training Use Ambiguous</span>\n    <span class="tag tag-dim">Closed Source · SaaS</span>',"dims_json":'[{"l":"V","s":6,"m":20,"low":true},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":4,"m":15,"low":true},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":2,"m":10,"low":true},{"l":"T","s":6,"m":10}]',"radar_points":"120.0,98.4 120.0,120.0 169.1,131.2 128.3,137.3 110.6,139.5 106.0,123.2 86.2,93.1","footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
    {"slug":"superagent","name":"Superagent","title":"Superagent Security Review — VERDICT Score: 42/85","meta_desc":"Independent security evaluation of Superagent. Score: 42/85. Pivoted to AI agent security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. Swedish origin. Framework v0.3.1.","category":"AI Agent Security Platform · Open Source + Cloud SaaS","owner":"Superagent · Gothenburg, Sweden","score":42,"rank":22,"finding":"Pivoted from AI agent framework to AI agent security company. Guard/Redact/Scan APIs + AI Firewall + VibeKit sandbox. Zero CVEs. Comprehensive legal docs (GDPR, DPA). 2-person team with $500K creates vendor viability question. No confirmed SOC 2. No SECURITY.md despite being a security company.","tags_html":'<span class="tag tag-dim">Pivoted to Security · YC W24</span>\n    <span class="tag tag-dim">Guard/Redact/Scan APIs</span>\n    <span class="tag tag-dim">0 CVEs · All Periods</span>\n    <span class="tag tag-amber">2-Person Team · $500K</span>\n    <span class="tag tag-amber">No SECURITY.md · Security Co.</span>',"dims_json":'[{"l":"V","s":9,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":8,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":4,"m":10}]',"radar_points":"120.0,87.6 120.0,120.0 169.1,131.2 136.6,154.6 110.6,139.5 91.9,126.4 97.5,102.0","footer_bias":"Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."},
]

# === GENERATE PAGES ===
for p in pages:
    os.makedirs(p["slug"], exist_ok=True)
    with open(os.path.join(p["slug"], "index.html"), 'w') as f:
        f.write(PAGE_TPL.format(**p))
    print(f"  ✓ {p['slug']}/index.html created ({p['score']}/85, Rank #{p['rank']})")

print()

# === UPDATE INDEX.HTML ===
with open('index.html', 'r') as f:
    html = f.read()

SVG_BLOCK = """        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
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
{SVG_BLOCK.format(pts=pts)}
        <div class="score-display"><span class="score-main">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span><div class="score-layer">Layer 0 &middot; Public Docs</div></div>
      </div>
    </a>
"""

# Dust 55 → insert before Activepieces 52
c = card("Dust 55","dust","dust","Dust","Enterprise AI Assistant · OSS + Cloud SaaS","Dust SAS · Paris, France","Evaluated 2026.03.31 · Framework v0.3.1","SOC 2 Type II, GDPR-native French company. Highest data conduct score (13/15). Zero CVEs. Zero data retention from providers. No SECURITY.md.","<span class=\"tag tag-dim\">SOC 2 Type II · GDPR Native</span>\n            <span class=\"tag tag-dim\">D: 13/15 · Index Highest</span>\n            <span class=\"tag tag-amber\">No SECURITY.md</span>",'[{"l":"V","s":13,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":17,"m":20,"high":true},{"l":"D","s":13,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',"120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 108.7,111.0",55)
m = '    <!-- Activepieces 52 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Dust inserted")

# Superagent 42 → insert before LlamaIndex 41
c = card("Superagent 42","superagent","superagent","Superagent","AI Agent Security Platform · OSS + Cloud","Superagent · Gothenburg, Sweden","Evaluated 2026.03.31 · Framework v0.3.1","Pivoted to AI security. Guard/Redact/Scan APIs. Zero CVEs. 2-person team. No confirmed SOC 2.","<span class=\"tag tag-dim\">Security Pivot · YC W24</span>\n            <span class=\"tag tag-dim\">Guard/Redact/Scan</span>\n            <span class=\"tag tag-amber\">2-Person Team</span>",'[{"l":"V","s":9,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":8,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":4,"m":10}]',"120.0,87.6 120.0,120.0 169.1,131.2 136.6,154.6 110.6,139.5 91.9,126.4 97.5,102.0",42)
m = '    <!-- LlamaIndex 41 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Superagent inserted")

# AG2 40 → insert before Letta 37
c = card("AG2 40","ag2","ag2","AG2","Multi-Agent Framework · OSS (Apache 2.0)","AG2AI Inc. · Community Fork","Evaluated 2026.03.31 · Framework v0.3.1","AutoGen fork. Zero AG2-specific CVEs. No MSRC. Controls autogen PyPI namespace.","<span class=\"tag tag-dim\">AutoGen Fork · Apache 2.0</span>\n            <span class=\"tag tag-amber\">No MSRC Coverage</span>\n            <span class=\"tag tag-amber\">PyPI Namespace Issue</span>",'[{"l":"V","s":12,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":5,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":2,"m":10,"low":true}]',"120.0,76.8 120.0,120.0 169.1,131.2 130.4,141.6 110.6,139.5 91.9,126.4 108.7,111.0",40)
m = '    <!-- Letta 37 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ AG2 inserted")

# Wordware 35 → insert before Langroid... wait, we need to insert before existing 35s
# Order at 35: Coze, n8n, Wordware (alphabetical)
# Wordware goes AFTER n8n but BEFORE Flowise(33). But n8n comment is "n8n 35"
# Actually Coze is already before n8n. Wordware after n8n, before Flowise.
# Find Flowise marker
c = card("Wordware 35","wordware","wordware","Wordware","AI Agent IDE · Cloud SaaS","HeyDaily Inc. · San Francisco","Evaluated 2026.03.31 · Framework v0.3.1","Zero CVEs. $30M seed. Trust center (SOC 2 ref). Minimal privacy policy. AI training ambiguous.","<span class=\"tag tag-dim\">$30M Seed · YC W24</span>\n            <span class=\"tag tag-amber\">Minimal Privacy Policy</span>\n            <span class=\"tag tag-amber\">Training Use Ambiguous</span>",'[{"l":"V","s":6,"m":20,"low":true},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":4,"m":15,"low":true},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":2,"m":10,"low":true},{"l":"T","s":6,"m":10}]',"120.0,98.4 120.0,120.0 169.1,131.2 128.3,137.3 110.6,139.5 106.0,123.2 86.2,93.1",35)
m = '    <!-- Flowise 33 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Wordware inserted")

# Langroid 34 → insert before Flowise 33 (but after Wordware which we just inserted before Flowise)
# Actually Langroid(34) > Flowise(33), so Langroid before Flowise. But we just put Wordware(35) before Flowise.
# Order should be: ...Wordware(35), Langroid(34), Flowise(33)
# So Langroid goes before Flowise too. Since Wordware card is already before Flowise marker,
# Langroid should go between Wordware and Flowise.
# The Flowise marker is still in the HTML. Insert before it.
c = card("Langroid 34","langroid","langroid","Langroid","Multi-Agent LLM Framework · OSS (MIT)","Prasad Chalasani (CMU) · Individual","Evaluated 2026.03.31 · Framework v0.3.1","CVE-2026-25481 CVSS 9.4 RCE. But T: 8/10 — maintainer published CVE himself. 48h response commitment.","<span class=\"tag tag-red\">CVE-2026-25481 · CVSS 9.4</span>\n            <span class=\"tag tag-safe\">T: 8/10 · Transparency Leader</span>\n            <span class=\"tag tag-dim\">MIT · CMU Origin</span>",'[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":5,"m":20,"low":true},{"l":"D","s":6,"m":15},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":8,"m":10,"high":true}]',"120.0,84.0 120.0,120.0 137.6,124.0 132.5,146.0 113.8,133.0 98.9,124.8 75.0,84.1",34)
m = '    <!-- Flowise 33 -->'
if m in html: html = html.replace(m, c + m); print("  ✓ Langroid inserted")

# Hero stat 26 → 31
html = html.replace('<span class="stat-num">26<span> / 100</span></span>','<span class="stat-num">31<span> / 100</span></span>')
print("  ✓ Hero stat: 26 → 31")

with open('index.html','w') as f: f.write(html)
print("  ✓ index.html saved")

# === SITEMAP ===
new_urls = """  <url><loc>https://getverdict.fyi/dust/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/ag2/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/langroid/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/wordware/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/superagent/</loc><lastmod>2026-03-31</lastmod><priority>0.8</priority></url>
"""
with open('sitemap.xml','r') as f: s=f.read()
s=s.replace('</urlset>',new_urls+'</urlset>')
with open('sitemap.xml','w') as f: f.write(s)
print("  ✓ sitemap.xml: 5 URLs added")

# === RANK UPDATES ===
# Full 31-platform ranking:
# 1:AmazonQ 2:Vertex 3:Copilot 4:OpenAI 5:Agentforce 6:AutoGen 7:Pipedream
# 8:AWSBedrock 9:Dust(NEW) 10:Activepieces 11:LangChain
# 12:IBMwatsonx 13:Zapier 14:Haystack 15:Composio 16:Dify 17:Make.com
# 18:SemanticKernel 19:Botpress 20:CrewAI 21:RelevanceAI
# 22:Superagent(NEW) 23:LlamaIndex 24:AG2(NEW) 25:Letta
# 26:Coze 27:n8n 28:Wordware(NEW) 29:Langroid(NEW) 30:Flowise 31:Langflow

rank_changes = {
    "amazon-q-business":(1,1),"vertex-ai":(2,2),"copilot-studio":(3,3),
    "openai-assistants":(4,4),"agentforce":(5,5),"autogen":(6,6),
    "pipedream":(7,7),"bedrock-agents":(8,8),
    # Dust is NEW at 9
    "activepieces":(9,10),"langchain":(10,11),
    "watsonx-orchestrate":(11,12),"zapier":(12,13),
    "haystack":(13,14),"composio":(14,15),
    "dify":(15,16),"make":(16,17),
    "semantic-kernel":(17,18),"botpress":(18,19),
    "crewai":(19,20),"relevance-ai":(20,21),
    # Superagent NEW at 22
    "llamaindex":(21,23),
    # AG2 NEW at 24
    "letta":(22,25),
    "coze":(23,26),"n8n":(24,27),
    # Wordware NEW at 28, Langroid NEW at 29
    "flowise":(25,30),"langflow":(26,31),
}

for dirname,(old_r,new_r) in rank_changes.items():
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 26 platforms evaluated","of 31 platforms evaluated")
    c=c.replace("All 26 Evaluations","All 31 Evaluations")
    if old_r != new_r:
        c=c.replace(f"Rank #{old_r} of",f"Rank #{new_r} of")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        if old_r!=new_r:
            print(f"  ✓ {fp}: #{old_r}→#{new_r}, count→31")
        else:
            print(f"  ✓ {fp}: count→31")

print("\nDone. git add . && git commit && git push")
