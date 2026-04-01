#!/usr/bin/env python3
"""
VERDICT: Deploy #037-#040 (AutoGPT, OpenHands, CAMEL-AI, SuperAGI)
Full card re-sort approach (learned from previous issues).
Run from ~/Desktop/verdict-index/
"""
import os, re

# ============================================================
# STEP 1: CREATE 4 INDIVIDUAL PAGES
# ============================================================

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
  <div class="meta">Evaluated {eval_date} &middot; Framework v0.3.1</div>
  <div class="meta-owner">{owner}</div>
  <div class="score-hero"><div><span class="score-big">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span></div><div class="score-meta">Layer 0 &middot; Public Documentation Only<br>Rank #{rank} of 40 platforms evaluated<br>Framework v0.3.1</div></div>
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
  <div class="cta-bar"><a href="/" class="cta-link">View All 40 Evaluations</a><a href="/#subscribe" class="cta-link">Get Notified of Score Changes</a></div>
</div>
<footer><div class="footer-note">VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports.</div></footer>
<script>document.querySelectorAll('.dim-list').forEach(list=>{{const dims=JSON.parse(list.dataset.dims);dims.forEach(d=>{{const pct=d.inactive?100:Math.round((d.s/d.m)*100);const isLow=!d.inactive&&pct<30;const isHigh=!d.inactive&&pct>=65;const fillClass=d.inactive?'fill-inactive':isLow?'fill-low':'';const letterClass=d.inactive?'dim-inactive':'';const valClass=d.inactive?'val-inactive':isHigh?'val-high':'';const valText=d.inactive?'L1':d.s+'/'+d.m;list.innerHTML+='<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';}});}});</script>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}}'></script>
</body></html>"""

pages = [
    {"slug":"autogpt","name":"AutoGPT","title":"AutoGPT Security Review — VERDICT Score: 36/85",
     "meta_desc":"Independent security evaluation of AutoGPT. Score: 36/85. T:10/10 (index highest). 6 security advisories including 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. Framework v0.3.1.",
     "category":"Autonomous AI Agent Platform · Source-Available (Polyform Shield + MIT)","owner":"Determinist Ltd · United Kingdom",
     "score":36,"rank":30,"eval_date":"2026.03.31",
     "finding":"Highest transparency score in the VERDICT index (T: 10/10). Six self-published security advisories with patches. Recurring SSRF pattern (3/6 advisories). Cross-user data leak via WebSockets (patched). 183k GitHub stars. $12M funded.",
     "tags_html":'<span class="tag tag-safe">T: 10/10 · Index Highest</span>\n    <span class="tag tag-red">6 Advisories · 2 Critical SSRF</span>\n    <span class="tag tag-red">Cross-User Data Leak</span>\n    <span class="tag tag-dim">183k Stars · $12M Funded</span>\n    <span class="tag tag-amber">Polyform Shield License</span>',
     "dims_json":'[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":4,"m":20,"low":true},{"l":"D","s":5,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":10,"m":10,"high":true}]',
     "radar_points":"120.0,84.0 120.0,120.0 134.0,123.2 130.4,141.6 110.6,139.5 91.9,126.4 63.7,75.1"},
    {"slug":"openhands","name":"OpenHands","title":"OpenHands (AllHands.ai) Security Review — VERDICT Score: 43/85",
     "meta_desc":"Independent security evaluation of OpenHands (formerly OpenDevin). Score: 43/85. Docker sandbox. HITL by default. D:1/15 — cloud service permits AI training on user code. Framework v0.3.1.",
     "category":"AI Coding Agent · Open Source (MIT)","owner":"All Hands AI, Inc. · Cambridge, MA",
     "score":43,"rank":22,"eval_date":"2026.04.01",
     "finding":"Docker-based sandbox for code execution. HITL enabled by default (opt-in for autonomous mode). D:1/15 — cloud privacy policy permits AI model training on user content including source code. Self-hosted deployment avoids cloud data concerns.",
     "tags_html":'<span class="tag tag-dim">MIT · 69.5k Stars</span>\n    <span class="tag tag-safe">Docker Sandbox · HITL Default</span>\n    <span class="tag tag-red">D: 1/15 · AI Training on User Code</span>\n    <span class="tag tag-amber">No SOC 2 · No GDPR DPA</span>',
     "dims_json":'[{"l":"V","s":13,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":12,"m":20},{"l":"D","s":1,"m":15,"low":true},{"l":"I","s":6,"m":10},{"l":"C","s":4,"m":10},{"l":"T","s":7,"m":10}]',
     "radar_points":"120.0,73.2 120.0,120.0 162.1,129.6 122.1,124.3 101.3,158.9 91.9,126.4 80.6,88.6"},
    {"slug":"camel-ai","name":"CAMEL-AI","title":"CAMEL-AI Security Review — VERDICT Score: 33/85",
     "meta_desc":"Independent security evaluation of CAMEL-AI. Score: 33/85. NeurIPS 2023 role-playing paradigm. Zero CVEs. SECURITY.md with 48-72h commitment. No containment model for role-playing. Framework v0.3.1.",
     "category":"Multi-Agent Research Framework · Open Source (Apache 2.0)","owner":"CAMEL-AI.org · UK (KAUST Origin)",
     "score":33,"rank":35,"eval_date":"2026.04.01",
     "finding":"Pioneered role-playing multi-agent paradigm (NeurIPS 2023). Zero CVEs. SECURITY.md with 48-72h response commitment, code scanning, Dependabot. No containment model for adversarial role assignment. Unfunded academic community.",
     "tags_html":'<span class="tag tag-dim">Apache 2.0 · NeurIPS 2023</span>\n    <span class="tag tag-dim">0 CVEs · SECURITY.md</span>\n    <span class="tag tag-amber">Role-Play Containment Risk</span>\n    <span class="tag tag-amber">No Privacy Policy · Unfunded</span>',
     "dims_json":'[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":1,"m":10,"low":true},{"l":"C","s":1,"m":10,"low":true},{"l":"T","s":4,"m":10}]',
     "radar_points":"120.0,80.4 120.0,120.0 169.1,131.2 124.2,128.7 116.9,126.5 113.0,121.6 97.5,102.0"},
    {"slug":"superagi","name":"SuperAGI","title":"SuperAGI Security Review — VERDICT Score: 21/85",
     "meta_desc":"Independent security evaluation of SuperAGI. Score: 21/85 (index lowest). Effectively unmaintained since mid-2024. Unpatched CVE-2024-9418 (plaintext password). No SECURITY.md. Framework v0.3.1.",
     "category":"Agent Management Platform · Open Source (MIT)","owner":"TransformErr Inc.",
     "score":21,"rank":40,"eval_date":"2026.04.01",
     "finding":"Effectively unmaintained since mid-2024. Unpatched CVE-2024-9418: API endpoint returns plaintext passwords enabling account takeover. No SECURITY.md. 17k stars but issues unanswered since 2025. Aging dependencies.",
     "tags_html":'<span class="tag tag-red">Unmaintained Since ~2024</span>\n    <span class="tag tag-red">Unpatched CVE · Plaintext Passwords</span>\n    <span class="tag tag-red">No SECURITY.md</span>\n    <span class="tag tag-dim">MIT · 17k Stars</span>',
     "dims_json":'[{"l":"V","s":7,"m":20,"low":true},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":5,"m":20,"low":true},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
     "radar_points":"120.0,94.8 120.0,120.0 137.6,124.0 124.2,128.7 113.8,133.0 98.9,124.8 108.7,111.0"},
]

for p in pages:
    os.makedirs(p["slug"], exist_ok=True)
    with open(os.path.join(p["slug"], "index.html"), 'w') as f:
        f.write(PAGE_TPL.format(**p))
    print(f"  ✓ {p['slug']}/index.html ({p['score']}/85, #{p['rank']})")

# ============================================================
# STEP 2: INSERT 4 NEW CARDS + FULL RE-SORT
# ============================================================

with open('index.html', 'r') as f:
    html = f.read()

SVG = """        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
          <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/><polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/><polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/><polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/><line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/><line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
          <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{pts}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{pts}"/></g>
          <text class="radar-label" x="120" y="22" text-anchor="middle">V</text><text class="radar-label radar-label-inactive" x="197" y="64" text-anchor="start">E</text><text class="radar-label" x="215" y="144" text-anchor="start">R</text><text class="radar-label" x="164" y="213" text-anchor="start">D</text><text class="radar-label" x="76" y="213" text-anchor="end">I</text><text class="radar-label" x="25" y="144" text-anchor="end">C</text><text class="radar-label" x="43" y="64" text-anchor="end">T</text>
        </svg></div>"""

def make_card(comment, href, platform, name, cat, owner, date, finding, tags, dims, pts, score):
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

# New cards to insert
new_cards_html = [
    make_card("AutoGPT 36","autogpt","autogpt","AutoGPT","Autonomous AI Agent · Source-Available","Determinist Ltd · UK","Evaluated 2026.03.31 · Framework v0.3.1",
        "T:10/10 (index highest). 6 advisories, 2 Critical SSRF. Recurring SSRF pattern. Cross-user data leak. 183k stars.",
        '<span class="tag tag-safe">T: 10/10 · Index Highest</span>\n            <span class="tag tag-red">6 Advisories · 2 Critical</span>\n            <span class="tag tag-red">Cross-User Data Leak</span>',
        '[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":4,"m":20,"low":true},{"l":"D","s":5,"m":15},{"l":"I","s":3,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":10,"m":10,"high":true}]',
        "120.0,84.0 120.0,120.0 134.0,123.2 130.4,141.6 110.6,139.5 91.9,126.4 63.7,75.1",36),
    make_card("OpenHands 43","openhands","openhands","OpenHands","AI Coding Agent · OSS (MIT)","All Hands AI · Cambridge, MA","Evaluated 2026.04.01 · Framework v0.3.1",
        "Docker sandbox. HITL by default. D:1/15 — cloud permits AI training on user code. 69.5k stars.",
        '<span class="tag tag-dim">MIT · Docker Sandbox</span>\n            <span class="tag tag-safe">HITL Default</span>\n            <span class="tag tag-red">D: 1/15 · AI Training Use</span>',
        '[{"l":"V","s":13,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":12,"m":20},{"l":"D","s":1,"m":15,"low":true},{"l":"I","s":6,"m":10},{"l":"C","s":4,"m":10},{"l":"T","s":7,"m":10}]',
        "120.0,73.2 120.0,120.0 162.1,129.6 122.1,124.3 101.3,158.9 91.9,126.4 80.6,88.6",43),
    make_card("CAMEL-AI 33","camel-ai","camel-ai","CAMEL-AI","Multi-Agent Research · OSS (Apache 2.0)","CAMEL-AI.org · UK (KAUST)","Evaluated 2026.04.01 · Framework v0.3.1",
        "NeurIPS 2023 role-playing paradigm. Zero CVEs. SECURITY.md 48-72h. No role-play containment model.",
        '<span class="tag tag-dim">Apache 2.0 · NeurIPS 2023</span>\n            <span class="tag tag-dim">0 CVEs · SECURITY.md</span>\n            <span class="tag tag-amber">Role-Play Containment Risk</span>',
        '[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":1,"m":10,"low":true},{"l":"C","s":1,"m":10,"low":true},{"l":"T","s":4,"m":10}]',
        "120.0,80.4 120.0,120.0 169.1,131.2 124.2,128.7 116.9,126.5 113.0,121.6 97.5,102.0",33),
    make_card("SuperAGI 21","superagi","superagi","SuperAGI","Agent Management · OSS (MIT)","TransformErr Inc.","Evaluated 2026.04.01 · Framework v0.3.1",
        "Unmaintained since ~2024. Unpatched CVE: plaintext passwords in API. No SECURITY.md. 17k stars.",
        '<span class="tag tag-red">Unmaintained · Unpatched CVE</span>\n            <span class="tag tag-red">Plaintext Passwords</span>\n            <span class="tag tag-dim">MIT · 17k Stars</span>',
        '[{"l":"V","s":7,"m":20,"low":true},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":5,"m":20,"low":true},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":2,"m":10,"low":true}]',
        "120.0,94.8 120.0,120.0 137.6,124.0 124.2,128.7 113.8,133.0 98.9,124.8 108.7,111.0",21),
]

# Extract existing cards
card_pattern = re.compile(
    r'(\n    <!-- (.+?) (\d+) -->\n    <a class="eval-card".*?</a>)',
    re.DOTALL
)
matches = list(card_pattern.finditer(html))
print(f"\n  Found {len(matches)} existing cards")

# Deduplicate existing
seen = set()
cards = []
for m in matches:
    name = m.group(2)
    score = int(m.group(3))
    if name not in seen:
        seen.add(name)
        cards.append({'html': m.group(1), 'name': name, 'score': score})

print(f"  Unique existing: {len(cards)}")

# Add new cards
for nc in new_cards_html:
    # Extract name and score from the card HTML
    nm = re.search(r'<!-- (.+?) (\d+) -->', nc)
    if nm:
        name = nm.group(1)
        score = int(nm.group(2))
        if name not in seen:
            seen.add(name)
            cards.append({'html': nc, 'name': name, 'score': score})
            print(f"  + Added: {name} ({score})")

# Sort: descending score, alphabetical name (case-insensitive for ties)
cards.sort(key=lambda c: (-c['score'], c['name'].lower()))

print(f"\n  Final sorted order ({len(cards)} cards):")
for i, c in enumerate(cards):
    print(f"    #{i+1}: {c['name']} ({c['score']}/85)")

# Replace card section
first_start = matches[0].start()
last_end = matches[-1].end()
new_html = ''.join(c['html'] for c in cards)
html = html[:first_start] + new_html + html[last_end:]

# Hero stat 36 → 40
html = html.replace('<span class="stat-num">36<span> / 100</span></span>',
                     '<span class="stat-num">40<span> / 100</span></span>')
print("\n  ✓ Hero stat: 36 → 40")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

# ============================================================
# STEP 3: SITEMAP
# ============================================================
new_urls = """  <url><loc>https://getverdict.fyi/autogpt/</loc><lastmod>2026-04-01</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/openhands/</loc><lastmod>2026-04-01</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/camel-ai/</loc><lastmod>2026-04-01</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/superagi/</loc><lastmod>2026-04-01</lastmod><priority>0.8</priority></url>
"""
with open('sitemap.xml','r') as f: s=f.read()
s=s.replace('</urlset>',new_urls+'</urlset>')
with open('sitemap.xml','w') as f: f.write(s)
print("  ✓ sitemap.xml: 4 URLs added")

# ============================================================
# STEP 4: UPDATE ALL EXISTING PAGES (rank + count → 40)
# ============================================================

# Full rank mapping: old_rank → new_rank for all 36 existing platforms
# Platforms 1-21: no rank change, only count update
# 22 Relevance AI → 23
# 23 Superagent → 24
# 24 LlamaIndex → 25
# 25 AG2 → 26
# 26 Rivet → 27
# 27 Phidata → 28
# 28 Letta → 29
# (AutoGPT NEW at 30)
# 29 Coze → 31
# 30 n8n → 32
# 31 Wordware → 33
# 32 Langroid → 34
# (CAMEL-AI NEW at 35)
# 33 Flowise → 36
# 34 Langflow → 37
# 35 BabyAGI → 38
# 36 MetaGPT → 39
# (SuperAGI NEW at 40)

no_rank_change = ["amazon-q-business","vertex-ai","copilot-studio","openai-assistants",
    "agentforce","dust","autogen","pipedream","bedrock-agents","activepieces",
    "voiceflow","langchain","watsonx-orchestrate","zapier","haystack",
    "composio","dify","make","semantic-kernel","botpress","crewai"]

rank_changes = {
    "relevance-ai":(22,23),"superagent":(23,24),"llamaindex":(24,25),
    "ag2":(25,26),"rivet":(26,27),"phidata":(27,28),"letta":(28,29),
    "coze":(29,31),"n8n":(30,32),"wordware":(31,33),
    "langroid":(32,34),"flowise":(33,36),"langflow":(34,37),
    "babyagi":(35,38),"metagpt":(36,39),
}

for dirname in no_rank_change:
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 36 platforms evaluated","of 40 platforms evaluated")
    c=c.replace("All 36 Evaluations","All 40 Evaluations")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        print(f"  ✓ {fp}: count→40")

for dirname,(old_r,new_r) in rank_changes.items():
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 36 platforms evaluated","of 40 platforms evaluated")
    c=c.replace("All 36 Evaluations","All 40 Evaluations")
    c=c.replace(f"Rank #{old_r} of",f"Rank #{new_r} of")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        print(f"  ✓ {fp}: #{old_r}→#{new_r}, count→40")

# Also update About and Methodology pages
for pg in ["about/index.html","methodology/index.html"]:
    if os.path.exists(pg):
        with open(pg,'r') as f: c=f.read()
        c=c.replace("36 Evaluations","40 Evaluations").replace(">36<",">40<")
        with open(pg,'w') as f: f.write(c)
        print(f"  ✓ {pg}: 36→40")

# Update comparison page
cp = "compare/n8n-vs-make/index.html"
if os.path.exists(cp):
    with open(cp,'r') as f: c=f.read()
    c=c.replace("Rank #30 of 36","Rank #32 of 40").replace("Rank #18 of 36","Rank #18 of 40")
    c=c.replace("All 36 Evaluations","All 40 Evaluations")
    with open(cp,'w') as f: f.write(c)
    print(f"  ✓ {cp}: ranks updated")

print("\n✓ Done. git add . && git commit && git push")
