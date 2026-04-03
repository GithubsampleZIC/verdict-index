#!/usr/bin/env python3
"""
VERDICT: Deploy #041-#043 (Devin, Cursor, Manus AI)
Full card re-sort. Run from ~/Desktop/verdict-index/
"""
import os, re

# ============================================================
# STEP 1: CREATE 3 INDIVIDUAL PAGES
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
  <div class="score-hero"><div><span class="score-big">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span></div><div class="score-meta">Layer 0 &middot; Public Documentation Only<br>Rank #{rank} of 43 platforms evaluated<br>Framework v0.3.1</div></div>
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
  <div class="cta-bar"><a href="/" class="cta-link">View All 43 Evaluations</a><a href="/#subscribe" class="cta-link">Get Notified of Score Changes</a></div>
</div>
<footer><div class="footer-note">VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports.</div></footer>
<script>document.querySelectorAll('.dim-list').forEach(list=>{{const dims=JSON.parse(list.dataset.dims);dims.forEach(d=>{{const pct=d.inactive?100:Math.round((d.s/d.m)*100);const isLow=!d.inactive&&pct<30;const isHigh=!d.inactive&&pct>=65;const fillClass=d.inactive?'fill-inactive':isLow?'fill-low':'';const letterClass=d.inactive?'dim-inactive':'';const valClass=d.inactive?'val-inactive':isHigh?'val-high':'';const valText=d.inactive?'L1':d.s+'/'+d.m;list.innerHTML+='<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';}});}});</script>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}}'></script>
</body></html>"""

pages = [
    {"slug":"devin","name":"Devin","title":"Devin Security Review — VERDICT Score: 62/85",
     "meta_desc":"Independent security evaluation of Devin by Cognition AI. Score: 62/85 (#3 in index). SOC 2 Type II + FedRAMP High. D:12/15. Zero CVEs. Highest-scoring AI coding agent. Framework v0.3.1.",
     "category":"AI Coding Agent · Proprietary Cloud SaaS","owner":"Cognition AI · USA · $10.2B Valuation",
     "score":62,"rank":3,"eval_date":"2026.04.03",
     "finding":"Highest-scoring AI coding agent and highest-scoring startup in the index. SOC 2 Type II + SOC 1 + FedRAMP High aligned. D:12/15 — default no-training, Enterprise zero-retention. VPC deployment. Zero CVEs. Goldman Sachs, Palantir among customers.",
     "tags_html":'<span class="tag tag-safe">SOC 2 Type II + FedRAMP High</span>\n    <span class="tag tag-safe">D: 12/15 · Default No-Training</span>\n    <span class="tag tag-dim">0 CVEs · VPC Deploy</span>\n    <span class="tag tag-dim">$10.2B · Closed Source</span>',
     "dims_json":'[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":17,"m":20,"high":true},{"l":"D","s":12,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":7,"m":10,"high":true},{"l":"T","s":8,"m":10,"high":true}]',
     "radar_points":"120.0,80.4 120.0,120.0 179.7,133.6 145.0,171.9 98.2,165.4 70.9,131.2 75.0,84.1"},
    {"slug":"cursor","name":"Cursor","title":"Cursor Security Review — VERDICT Score: 47/85",
     "meta_desc":"Independent security evaluation of Cursor by Anysphere. Score: 47/85. SOC 2 Type II. 3 MCP CVEs (structural pattern). Privacy Mode zero-retention. $29.3B valuation. Framework v0.3.1.",
     "category":"AI Coding Agent / IDE · Proprietary","owner":"Anysphere Inc. · San Francisco · $29.3B Valuation",
     "score":47,"rank":16,"eval_date":"2026.04.03",
     "finding":"Most widely adopted AI IDE ($29.3B, $1B+ ARR). SOC 2 Type II. Privacy Mode: zero-retention + no training. 3 MCP CVEs (CVSS 8.6 highest) — structural trust model pattern. 94+ inherited Chromium CVEs. Workspace Trust disabled by default.",
     "tags_html":'<span class="tag tag-safe">SOC 2 Type II</span>\n    <span class="tag tag-safe">Privacy Mode · Zero Retention</span>\n    <span class="tag tag-red">3 MCP CVEs · Structural Pattern</span>\n    <span class="tag tag-amber">Workspace Trust Off · Chromium CVEs</span>',
     "dims_json":'[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":8,"m":20},{"l":"D","s":11,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":5,"m":10},{"l":"T","s":6,"m":10}]',
     "radar_points":"120.0,84.0 120.0,120.0 148.1,126.4 142.9,167.6 98.2,165.4 84.9,128.0 86.2,93.1"},
    {"slug":"manus-ai","name":"Manus AI","title":"Manus AI Security Review — VERDICT Score: 35/85",
     "meta_desc":"Independent security evaluation of Manus AI. Score: 35/85. Meta-acquired ($2B+). Browser Operator: full browser remote control (Mindgard analysis). Sandbox VM isolation. Zero CVEs. Framework v0.3.1.",
     "category":"Autonomous Browser Agent · Proprietary Cloud SaaS","owner":"Butterfly Effect (Meta-acquired) · Singapore",
     "score":35,"rank":34,"eval_date":"2026.04.03",
     "finding":"Meta-acquired ($2B+) autonomous browser agent. Sandbox VMs with Zero Trust isolation. Zero CVEs. Browser Operator analyzed by Mindgard as 'full browser remote control' — debugger/cookies/all_urls privileges. Complex jurisdiction: China team, Singapore entity, Meta parent.",
     "tags_html":'<span class="tag tag-dim">Meta Acquired · $2B+</span>\n    <span class="tag tag-dim">Sandbox VM · Zero CVEs</span>\n    <span class="tag tag-red">Browser Operator: Full Control</span>\n    <span class="tag tag-amber">No Certifications · No SECURITY.md</span>',
     "dims_json":'[{"l":"V","s":8,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":4,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":3,"m":10,"low":true}]',
     "radar_points":"120.0,91.2 120.0,120.0 169.1,131.2 128.3,137.3 113.8,133.0 91.9,126.4 103.1,106.5"},
]

for p in pages:
    os.makedirs(p["slug"], exist_ok=True)
    with open(os.path.join(p["slug"], "index.html"), 'w') as f:
        f.write(PAGE_TPL.format(**p))
    print(f"  ✓ {p['slug']}/index.html ({p['score']}/85, #{p['rank']})")

# ============================================================
# STEP 2: INSERT 3 NEW CARDS + FULL RE-SORT
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

new_cards = [
    make_card("Devin 62","devin","devin","Devin","AI Coding Agent · Cloud SaaS","Cognition AI · $10.2B","Evaluated 2026.04.03 · Framework v0.3.1",
        "SOC 2 Type II + FedRAMP High. D:12/15 default no-training. Zero CVEs. VPC deploy. Highest coding agent.",
        '<span class="tag tag-safe">SOC 2 Type II + FedRAMP</span>\n            <span class="tag tag-safe">D: 12/15 · No Training</span>\n            <span class="tag tag-dim">0 CVEs · $10.2B</span>',
        '[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":17,"m":20,"high":true},{"l":"D","s":12,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":7,"m":10,"high":true},{"l":"T","s":8,"m":10,"high":true}]',
        "120.0,80.4 120.0,120.0 179.7,133.6 145.0,171.9 98.2,165.4 70.9,131.2 75.0,84.1",62),
    make_card("Cursor 47","cursor","cursor","Cursor","AI Coding IDE · Proprietary","Anysphere · $29.3B","Evaluated 2026.04.03 · Framework v0.3.1",
        "SOC 2 Type II. Privacy Mode zero-retention. 3 MCP CVEs (structural). $29.3B, $1B+ ARR.",
        '<span class="tag tag-safe">SOC 2 Type II · Privacy Mode</span>\n            <span class="tag tag-red">3 MCP CVEs · CVSS 8.6</span>\n            <span class="tag tag-amber">Workspace Trust Off</span>',
        '[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":8,"m":20},{"l":"D","s":11,"m":15,"high":true},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":5,"m":10},{"l":"T","s":6,"m":10}]',
        "120.0,84.0 120.0,120.0 148.1,126.4 142.9,167.6 98.2,165.4 84.9,128.0 86.2,93.1",47),
    make_card("Manus AI 35","manus-ai","manus-ai","Manus AI","Autonomous Browser Agent · Cloud","Butterfly Effect (Meta) · Singapore","Evaluated 2026.04.03 · Framework v0.3.1",
        "Meta-acquired ($2B+). Sandbox VMs. Zero CVEs. Browser Operator: full browser control (Mindgard). No certifications.",
        '<span class="tag tag-dim">Meta · $2B+ · Zero CVEs</span>\n            <span class="tag tag-red">Browser Operator: Full Control</span>\n            <span class="tag tag-amber">No Certifications</span>',
        '[{"l":"V","s":8,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":4,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":4,"m":10},{"l":"T","s":3,"m":10,"low":true}]',
        "120.0,91.2 120.0,120.0 169.1,131.2 128.3,137.3 113.8,133.0 91.9,126.4 103.1,106.5",35),
]

# Extract, deduplicate, add new, sort
card_pattern = re.compile(r'(\n    <!-- (.+?) (\d+) -->\n    <a class="eval-card".*?</a>)', re.DOTALL)
matches = list(card_pattern.finditer(html))
print(f"\n  Found {len(matches)} existing cards")

seen = set()
cards = []
for m in matches:
    name = m.group(2)
    score = int(m.group(3))
    if name not in seen:
        seen.add(name)
        cards.append({'html': m.group(1), 'name': name, 'score': score})

for nc in new_cards:
    nm = re.search(r'<!-- (.+?) (\d+) -->', nc)
    if nm:
        name = nm.group(1)
        score = int(nm.group(2))
        if name not in seen:
            seen.add(name)
            cards.append({'html': nc, 'name': name, 'score': score})
            print(f"  + Added: {name} ({score})")

cards.sort(key=lambda c: (-c['score'], c['name'].lower()))

print(f"\n  Final sorted order ({len(cards)} cards):")
for i, c in enumerate(cards):
    print(f"    #{i+1}: {c['name']} ({c['score']}/85)")

first_start = matches[0].start()
last_end = matches[-1].end()
html = html[:first_start] + ''.join(c['html'] for c in cards) + html[last_end:]

# Hero stat 40 → 43
html = html.replace('<span class="stat-num">40<span> / 100</span></span>',
                     '<span class="stat-num">43<span> / 100</span></span>')
print("\n  ✓ Hero stat: 40 → 43")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

# ============================================================
# STEP 3: SITEMAP
# ============================================================
new_urls = """  <url><loc>https://getverdict.fyi/devin/</loc><lastmod>2026-04-03</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/cursor/</loc><lastmod>2026-04-03</lastmod><priority>0.8</priority></url>
  <url><loc>https://getverdict.fyi/manus-ai/</loc><lastmod>2026-04-03</lastmod><priority>0.8</priority></url>
"""
with open('sitemap.xml','r') as f: s=f.read()
s=s.replace('</urlset>',new_urls+'</urlset>')
with open('sitemap.xml','w') as f: f.write(s)
print("  ✓ sitemap.xml: 3 URLs added")

# ============================================================
# STEP 4: UPDATE ALL EXISTING PAGES (40→43)
# ============================================================

# Rank changes: Devin inserts at #3, Cursor at #16, Manus at #34
# Platforms 1-2: no rank change
no_rank_change_dirs = ["amazon-q-business","vertex-ai"]

# +1 shift (Devin at #3): ranks 3-14
shift1 = {
    "copilot-studio":(3,4),"openai-assistants":(4,5),"agentforce":(5,6),
    "dust":(6,7),"autogen":(7,8),"pipedream":(8,9),"bedrock-agents":(9,10),
    "activepieces":(10,11),"voiceflow":(11,12),"langchain":(12,13),
    "watsonx-orchestrate":(13,14),"zapier":(14,15),
}

# +2 shift (Devin + Cursor): ranks 15 onwards until Manus insertion
shift2 = {
    "haystack":(15,17),"composio":(16,18),"dify":(17,19),"make":(18,20),
    "semantic-kernel":(19,21),"botpress":(20,22),"crewai":(21,23),
    "openhands":(22,24),"relevance-ai":(23,25),"superagent":(24,26),
    "llamaindex":(25,27),"ag2":(26,28),"rivet":(27,29),"phidata":(28,30),
    "letta":(29,31),"autogpt":(30,32),"coze":(31,33),
}

# +3 shift (Devin + Cursor + Manus): after Manus at #34
shift3 = {
    "n8n":(32,35),"wordware":(33,36),"langroid":(34,37),
    "camel-ai":(35,38),"flowise":(36,39),"langflow":(37,40),
    "babyagi":(38,41),"metagpt":(39,42),"superagi":(40,43),
}

for dirname in no_rank_change_dirs:
    fp = os.path.join(dirname,"index.html")
    if not os.path.exists(fp): continue
    with open(fp,'r') as f: c=f.read()
    orig=c
    c=c.replace("of 40 platforms evaluated","of 43 platforms evaluated")
    c=c.replace("All 40 Evaluations","All 43 Evaluations")
    if c!=orig:
        with open(fp,'w') as f: f.write(c)
        print(f"  ✓ {fp}: count→43")

for shifts in [shift1, shift2, shift3]:
    for dirname,(old_r,new_r) in shifts.items():
        fp = os.path.join(dirname,"index.html")
        if not os.path.exists(fp): continue
        with open(fp,'r') as f: c=f.read()
        orig=c
        c=c.replace("of 40 platforms evaluated","of 43 platforms evaluated")
        c=c.replace("All 40 Evaluations","All 43 Evaluations")
        c=c.replace(f"Rank #{old_r} of",f"Rank #{new_r} of")
        if c!=orig:
            with open(fp,'w') as f: f.write(c)
            print(f"  ✓ {fp}: #{old_r}→#{new_r}, count→43")

# Update About, Methodology, comparison page
for pg in ["about/index.html","methodology/index.html"]:
    if os.path.exists(pg):
        with open(pg,'r') as f: c=f.read()
        c=c.replace("40 Evaluations","43 Evaluations").replace(">40<",">43<")
        with open(pg,'w') as f: f.write(c)
        print(f"  ✓ {pg}: 40→43")

cp = "compare/n8n-vs-make/index.html"
if os.path.exists(cp):
    with open(cp,'r') as f: c=f.read()
    c=c.replace("Rank #32 of 40","Rank #35 of 43").replace("Rank #18 of 40","Rank #20 of 43")
    c=c.replace("All 40 Evaluations","All 43 Evaluations")
    with open(cp,'w') as f: f.write(c)
    print(f"  ✓ {cp}: ranks updated")

print("\n✓ Done. git add . && git commit && git push")
