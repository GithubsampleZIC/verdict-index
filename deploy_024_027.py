#!/usr/bin/env python3
"""
VERDICT: Generate 4 new platform pages + update main site for #024-#027
Run from ~/Desktop/verdict-index/
"""
import os, re

# === TEMPLATE ===
PAGE_TEMPLATE = """<!DOCTYPE html>
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
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
body{{background:var(--white);color:var(--body);font-family:var(--sans);font-weight:400;line-height:1.6;}}
a{{color:var(--navy);text-decoration:none;}}a:hover{{text-decoration:underline;}}
header{{padding:0 2.5rem;height:58px;display:flex;align-items:center;justify-content:space-between;background:var(--white);border-bottom:1px solid var(--divider);}}
.logo{{display:flex;align-items:baseline;gap:.75rem;text-decoration:none;}}.logo:hover{{text-decoration:none;}}
.logo-mark{{font-family:var(--serif);font-size:1.25rem;font-weight:700;letter-spacing:.1em;color:var(--navy);}}
.logo-sub{{font-family:var(--mono);font-size:.6rem;letter-spacing:.15em;color:var(--caption);text-transform:uppercase;}}
.back{{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--caption);text-decoration:none;}}.back:hover{{color:var(--navy);}}
.wrap{{max-width:960px;margin:0 auto;padding:4rem 2.5rem;}}
.breadcrumb{{font-family:var(--mono);font-size:.65rem;color:var(--caption);margin-bottom:2rem;}}.breadcrumb a{{color:var(--caption);}}.breadcrumb a:hover{{color:var(--navy);}}
h1{{font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.1;color:var(--heading);margin-bottom:.4rem;}}
.meta{{font-family:var(--mono);font-size:.65rem;color:var(--caption);margin-bottom:.3rem;}}
.meta-owner{{font-family:var(--mono);font-size:.62rem;color:var(--navy-light);margin-bottom:1.5rem;}}
.score-hero{{display:flex;align-items:center;gap:2.5rem;margin-bottom:3rem;padding:2rem 0;border-top:1px solid var(--divider);border-bottom:1px solid var(--divider);}}
.score-big{{font-family:var(--score);font-weight:900;font-size:4rem;line-height:1;color:var(--navy);}}
.score-denom{{font-family:var(--mono);font-size:1.2rem;color:var(--caption);}}
.score-meta{{font-family:var(--mono);font-size:.65rem;color:var(--caption);line-height:1.8;}}
.finding{{font-size:.9rem;line-height:1.75;color:var(--body);border-left:3px solid var(--navy);padding-left:1rem;margin-bottom:2rem;}}
.tags{{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:3rem;}}
.tag{{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;padding:.3rem .7rem;border:1px solid;}}
.tag-red{{border-color:rgba(196,51,43,.3);color:var(--risk);background:var(--risk-bg);}}
.tag-amber{{border-color:rgba(192,133,32,.3);color:var(--caution);background:var(--caution-bg);}}
.tag-dim{{border-color:var(--divider);color:var(--caption);background:var(--ice);}}
.tag-safe{{border-color:rgba(45,122,79,.3);color:var(--safe);background:rgba(45,122,79,0.06);}}
.radar-section{{display:flex;gap:3rem;align-items:flex-start;margin-bottom:3rem;flex-wrap:wrap;}}
.radar-wrap{{width:260px;height:260px;flex-shrink:0;}}
.radar-svg{{width:100%;height:100%;overflow:visible;}}
.radar-ring{{fill:none;stroke:var(--divider);stroke-width:.5;}}
.radar-axis{{stroke:var(--divider);stroke-width:.5;}}
.radar-axis-inactive{{stroke:var(--divider);stroke-width:.5;stroke-dasharray:2 3;}}
.radar-label{{font-family:var(--mono);font-size:10px;font-weight:500;fill:var(--navy);letter-spacing:.05em;}}
.radar-label-inactive{{fill:var(--caption);}}
.radar-poly-fill{{opacity:.14;}}.radar-poly-stroke{{fill:none;stroke-width:1.5;stroke-linejoin:round;}}
.dim-list{{display:flex;flex-direction:column;gap:.7rem;flex:1;min-width:240px;}}
.dim-row{{display:grid;grid-template-columns:16px 1fr 55px;align-items:center;gap:.6rem;}}
.dim-letter{{font-family:var(--mono);font-size:.75rem;font-weight:600;color:var(--navy);}}.dim-letter.dim-inactive{{color:var(--caption);}}
.dim-bar-track{{height:3px;background:var(--divider);overflow:hidden;}}
.dim-bar-fill{{height:100%;background:var(--navy);}}.dim-bar-fill.fill-low{{background:var(--risk);}}.dim-bar-fill.fill-inactive{{background:repeating-linear-gradient(90deg,var(--divider) 0,var(--divider) 3px,transparent 3px,transparent 6px);}}
.dim-val{{font-family:var(--mono);font-size:.7rem;font-weight:500;color:var(--caption);text-align:right;}}.dim-val.val-high{{color:var(--navy);}}.dim-val.val-inactive{{color:var(--divider);}}
.cta-bar{{border-top:1px solid var(--divider);padding-top:2.5rem;margin-top:2rem;display:flex;gap:2rem;flex-wrap:wrap;}}
.cta-link{{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--navy);padding:.5rem 1rem;border:1px solid var(--divider);text-decoration:none;transition:all .2s;}}.cta-link:hover{{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}}
footer{{border-top:1px solid var(--divider);padding:2rem 2.5rem;max-width:960px;margin:0 auto;}}
.footer-note{{font-family:var(--mono);font-size:.62rem;color:var(--caption);line-height:1.8;}}.footer-note a{{color:var(--navy);}}
@media(max-width:700px){{.score-hero{{flex-direction:column;align-items:flex-start;gap:1rem;}}.radar-section{{flex-direction:column;}}.radar-wrap{{width:220px;height:220px;}}}}
</style>
</head>
<body>
<header>
  <a href="/" class="logo"><span class="logo-mark">VERDICT</span><span class="logo-sub">AI Agent Trust Index</span></a>
  <a href="/" class="back">&larr; All Evaluations</a>
</header>
<div class="wrap">
  <div class="breadcrumb"><a href="/">VERDICT</a> &rsaquo; Evaluations &rsaquo; {name}</div>
  <h1>{name}</h1>
  <div class="meta">{category}</div>
  <div class="meta">Evaluated 2026.03.30 &middot; Framework v0.3.1</div>
  <div class="meta-owner">{owner}</div>
  <div class="score-hero">
    <div><span class="score-big">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span></div>
    <div class="score-meta">Layer 0 &middot; Public Documentation Only<br>Rank #{rank} of 26 platforms evaluated<br>Framework v0.3.1</div>
  </div>
  <div class="finding">{finding}</div>
  <div class="tags">{tags_html}</div>
  <div class="radar-section">
    <div class="radar-wrap">
      <svg class="radar-svg" viewBox="0 0 240 240">
        <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/>
        <polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/>
        <polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/>
        <polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
        <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/>
        <line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/>
        <line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/>
        <line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/>
        <line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/>
        <line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/>
        <line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
        <g class="radar-data">
          <polygon class="radar-poly-fill" fill="#1B2A4A" points="{radar_points}"/>
          <polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{radar_points}"/>
        </g>
        <text class="radar-label" x="120" y="22" text-anchor="middle">V</text>
        <text class="radar-label radar-label-inactive" x="193" y="61" text-anchor="start">E</text>
        <text class="radar-label" x="212" y="141" text-anchor="start">R</text>
        <text class="radar-label" x="161" y="205" text-anchor="start">D</text>
        <text class="radar-label" x="79" y="205" text-anchor="end">I</text>
        <text class="radar-label" x="28" y="141" text-anchor="end">C</text>
        <text class="radar-label" x="47" y="61" text-anchor="end">T</text>
      </svg>
    </div>
    <div class="dim-list" id="dims" data-dims='{dims_json}'></div>
  </div>
  <div class="cta-bar">
    <a href="/" class="cta-link">View All 26 Evaluations</a>
    <a href="/#subscribe" class="cta-link">Get Notified of Score Changes</a>
  </div>
</div>
<footer>
  <div class="footer-note">
    VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>
    VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>
    {footer_bias}
  </div>
</footer>
<script>
document.querySelectorAll('.dim-list').forEach(list=>{{const dims=JSON.parse(list.dataset.dims);dims.forEach(d=>{{const pct=d.inactive?100:Math.round((d.s/d.m)*100);const isLow=!d.inactive&&pct<30;const isHigh=!d.inactive&&pct>=65;const fillClass=d.inactive?'fill-inactive':isLow?'fill-low':'';const letterClass=d.inactive?'dim-inactive':'';const valClass=d.inactive?'val-inactive':isHigh?'val-high':'';const valText=d.inactive?'L1':d.s+'/'+d.m;list.innerHTML+='<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';}});}});
</script>
<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>"""

# === PAGE DATA ===
pages = [
    {
        "slug": "amazon-q-business",
        "name": "Amazon Q Business",
        "title": "Amazon Q Business Security Review — VERDICT Score: 68/85",
        "meta_desc": "Independent security evaluation of Amazon Q Business. Score: 68/85 — highest in the VERDICT index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Zero CVEs. Framework v0.3.1.",
        "category": "Enterprise AI Assistant · Cloud SaaS (AWS)",
        "owner": "Amazon Web Services (Amazon)",
        "score": 68,
        "rank": 1,
        "finding": "Highest score in the VERDICT index. SOC 1/2/3, ISO 27001, ISO 42001 (first major cloud provider), FedRAMP, HIPAA BAA, PCI DSS. Customer data explicitly not used for model training. Zero CVEs for Q Business. Sibling product Q Developer experienced a supply chain compromise (CVE-2025-8217). Enhanced bias disclosure: Amazon is a major investor in Anthropic.",
        "tags_html": """<span class="tag tag-safe">SOC 1/2/3 · ISO 27001 · FedRAMP</span>
    <span class="tag tag-safe">ISO 42001 · First Cloud Provider</span>
    <span class="tag tag-safe">No Client Data for AI Training</span>
    <span class="tag tag-amber">Q Developer CVE-2025-8217 · Sibling</span>
    <span class="tag tag-dim">Closed Source · Managed SaaS</span>""",
        "dims_json": '[{"l":"V","s":14,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":20,"m":20,"high":true},{"l":"D","s":13,"m":15,"high":true},{"l":"I","s":6,"m":10},{"l":"C","s":6,"m":10},{"l":"T","s":9,"m":10,"high":true}]',
        "radar_points": "120.0,69.6 120.0,120.0 190.2,136.0 147.0,176.2 101.3,158.9 77.9,129.6 69.3,79.6",
        "footer_bias": "Evaluation tooling uses Claude (Anthropic). Amazon is a major investor in Anthropic and distributes Claude via AWS Bedrock. This is the strongest financial relationship between Anthropic and any evaluated vendor. Bias disclosures in full reports."
    },
    {
        "slug": "relevance-ai",
        "name": "Relevance AI",
        "title": "Relevance AI Security Review — VERDICT Score: 43/85",
        "meta_desc": "Independent security evaluation of Relevance AI. Score: 43/85. SOC 2 Type II, multi-region (US/AU/EU). No public CVEs. Closed-source GTM agent platform. Framework v0.3.1.",
        "category": "AI Agent Platform · Cloud SaaS",
        "owner": "Relevance AI Pty Ltd · Sydney, Australia",
        "score": 43,
        "rank": 20,
        "finding": "SOC 2 Type II compliant with explicit data non-training policy. Multi-region data residency (US, AU, EU/UK). Zero CVEs in any public database. Score moderated by closed-source architecture, no public vulnerability disclosure program, and Enterprise-only access to SSO/RBAC and data retention controls.",
        "tags_html": """<span class="tag tag-safe">SOC 2 Type II</span>
    <span class="tag tag-safe">No Data for Model Training</span>
    <span class="tag tag-dim">Closed Source · SaaS Only</span>
    <span class="tag tag-dim">Multi-Region · US/AU/EU</span>
    <span class="tag tag-amber">SSO/RBAC Enterprise Only</span>""",
        "dims_json": '[{"l":"V","s":7,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":9,"m":15},{"l":"I","s":5,"m":10},{"l":"C","s":4,"m":10},{"l":"T","s":4,"m":10}]',
        "radar_points": "120.0,94.8 120.0,120.0 169.1,131.2 138.7,158.9 104.4,152.4 91.9,126.4 97.5,102.0",
        "footer_bias": "Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."
    },
    {
        "slug": "letta",
        "name": "Letta",
        "title": "Letta (MemGPT) Security Review — VERDICT Score: 37/85",
        "meta_desc": "Independent security evaluation of Letta (formerly MemGPT). Score: 37/85. Zero CVEs in trailing 12 months. Apache 2.0 open source. Hosted service data may be used for model training. Framework v0.3.1.",
        "category": "Stateful AI Agent Framework · Open Source (Apache 2.0)",
        "owner": "Letta Inc. · San Francisco (UC Berkeley origin)",
        "score": 37,
        "rank": 22,
        "finding": "Pioneered stateful agent architecture (persistent memory). Zero CVEs in trailing 12 months. Full Apache 2.0 open source. Self-hosted option preserves data sovereignty. Hosted service data may be used for model training — one of the most permissive policies in the index. No SOC 2, no SECURITY.md, no HITL mechanism.",
        "tags_html": """<span class="tag tag-dim">Apache 2.0 · UC Berkeley</span>
    <span class="tag tag-dim">0 CVEs · Trailing 12 Months</span>
    <span class="tag tag-red">Hosted Data May Train Models</span>
    <span class="tag tag-amber">No SOC 2 · Seed Stage</span>
    <span class="tag tag-amber">No SECURITY.md</span>""",
        "dims_json": '[{"l":"V","s":12,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":3,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":3,"m":10,"low":true}]',
        "radar_points": "120.0,76.8 120.0,120.0 169.1,131.2 126.2,133.0 113.8,133.0 98.9,124.8 103.1,106.5",
        "footer_bias": "Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."
    },
    {
        "slug": "composio",
        "name": "Composio",
        "title": "Composio Security Review — VERDICT Score: 46/85",
        "meta_desc": "Independent security evaluation of Composio. Score: 46/85. SOC 2 + ISO 27001. Credential isolation architecture. Recurring eval() CVE pattern. Vendor non-response to disclosure. Framework v0.3.1.",
        "category": "AI Agent Tool Integration · Open Source SDK + Cloud SaaS",
        "owner": "Composio Inc. · San Francisco",
        "score": 46,
        "rank": 14,
        "finding": "SOC 2 Type II + ISO 27001:2022 dual certification. Credentials never reach agent context — architectural isolation. Published DPA with sub-processor list. Recurring eval() code injection pattern (CVE-2024-8864/8953). Directory traversal CVE-2025-56427 in SDK. Vendor documented as non-responsive to disclosure.",
        "tags_html": """<span class="tag tag-safe">SOC 2 + ISO 27001</span>
    <span class="tag tag-safe">Credential Isolation Architecture</span>
    <span class="tag tag-red">CVE-2025-56427 · Directory Traversal</span>
    <span class="tag tag-red">eval() Injection · Recurring Pattern</span>
    <span class="tag tag-amber">Vendor Non-Response to Disclosure</span>""",
        "dims_json": '[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":8,"m":20,"low":true},{"l":"D","s":10,"m":15},{"l":"I","s":6,"m":10},{"l":"C","s":6,"m":10},{"l":"T","s":6,"m":10}]',
        "radar_points": "120.0,84.0 120.0,120.0 148.1,126.4 140.8,163.3 101.3,158.9 77.9,129.6 86.2,93.1",
        "footer_bias": "Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports."
    },
]

# === GENERATE PAGES ===
for p in pages:
    dirname = p["slug"]
    os.makedirs(dirname, exist_ok=True)
    html = PAGE_TEMPLATE.format(**p)
    with open(os.path.join(dirname, "index.html"), 'w') as f:
        f.write(html)
    print(f"  ✓ {dirname}/index.html created (Score: {p['score']}/85, Rank #{p['rank']})")

print("\nPages created. Now updating main site...\n")

# === UPDATE INDEX.HTML ===
with open('index.html', 'r') as f:
    html = f.read()

# Helper for card HTML
RADAR_SVG = """        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
          <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/>
          <polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/>
          <polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/>
          <polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/>
          <line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/>
          <line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/>
          <line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/>
          <line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/>
          <line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
          <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{pts}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{pts}"/></g>
          <text class="radar-label" x="120" y="22" text-anchor="middle">V</text>
          <text class="radar-label radar-label-inactive" x="197" y="64" text-anchor="start">E</text>
          <text class="radar-label" x="215" y="144" text-anchor="start">R</text>
          <text class="radar-label" x="164" y="213" text-anchor="start">D</text>
          <text class="radar-label" x="76" y="213" text-anchor="end">I</text>
          <text class="radar-label" x="25" y="144" text-anchor="end">C</text>
          <text class="radar-label" x="43" y="64" text-anchor="end">T</text>
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
          <div class="incident-tags">
            {tags}
          </div>
        </div>
        <div class="dim-list" data-dims='{dims}'></div>
      </div>
      <div class="card-right">
{RADAR_SVG.format(pts=pts)}
        <div class="score-display"><span class="score-main">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span><div class="score-layer">Layer 0 &middot; Public Docs</div></div>
      </div>
    </a>
"""

# Amazon Q Business: insert before Vertex AI (current #1)
aq_card = card("Amazon Q Business 68", "amazon-q-business", "amazon-q-business",
    "Amazon Q Business", "Enterprise AI Assistant · Cloud SaaS (AWS)", "Amazon Web Services",
    "Evaluated 2026.03.30 · Framework v0.3.1",
    "Highest score in the index. SOC 1/2/3, ISO 27001, ISO 42001, FedRAMP, HIPAA. Customer data not used for model training. Zero CVEs. Enhanced bias disclosure: Amazon is Anthropic's major investor.",
    '<span class="tag tag-dim">SOC 1/2/3 · ISO 27001 · FedRAMP</span>\n            <span class="tag tag-dim">ISO 42001 · First Cloud Provider</span>\n            <span class="tag tag-amber">Q Developer CVE · Sibling Product</span>',
    '[{"l":"V","s":14,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":20,"m":20,"high":true},{"l":"D","s":13,"m":15,"high":true},{"l":"I","s":6,"m":10},{"l":"C","s":6,"m":10},{"l":"T","s":9,"m":10,"high":true}]',
    "120.0,69.6 120.0,120.0 190.2,136.0 147.0,176.2 101.3,158.9 77.9,129.6 69.3,79.6", 68)

marker_vertex = '    <!-- Vertex AI Agent Builder 65 -->'
if marker_vertex in html:
    html = html.replace(marker_vertex, aq_card + marker_vertex)
    print("  ✓ Amazon Q Business card inserted before Vertex AI")

# Composio: insert before Dify (46)
comp_card = card("Composio 46", "composio", "composio",
    "Composio", "AI Agent Tool Integration · OSS SDK + Cloud", "Composio Inc. · San Francisco",
    "Evaluated 2026.03.30 · Framework v0.3.1",
    "SOC 2 + ISO 27001. Credentials never reach agent context. Recurring eval() code injection pattern. Directory traversal CVE-2025-56427. Vendor non-responsive to security disclosure.",
    '<span class="tag tag-red">CVE-2025-56427 · Dir Traversal</span>\n            <span class="tag tag-red">eval() Injection · Recurring</span>\n            <span class="tag tag-amber">Vendor Non-Response</span>',
    '[{"l":"V","s":10,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":8,"m":20,"low":true},{"l":"D","s":10,"m":15},{"l":"I","s":6,"m":10},{"l":"C","s":6,"m":10},{"l":"T","s":6,"m":10}]',
    "120.0,84.0 120.0,120.0 148.1,126.4 140.8,163.3 101.3,158.9 77.9,129.6 86.2,93.1", 46)

marker_dify = '    <!-- Dify 46 -->'
if marker_dify in html:
    html = html.replace(marker_dify, comp_card + marker_dify)
    print("  ✓ Composio card inserted before Dify")

# Relevance AI: insert before LlamaIndex (41)
rel_card = card("Relevance AI 43", "relevance-ai", "relevance-ai",
    "Relevance AI", "AI Agent Platform · Cloud SaaS", "Relevance AI Pty Ltd · Sydney, Australia",
    "Evaluated 2026.03.30 · Framework v0.3.1",
    "SOC 2 Type II. Customer data not used for training. Multi-region (US/AU/EU). Zero public CVEs. Closed-source with no public vulnerability disclosure program. SSO/RBAC Enterprise only.",
    '<span class="tag tag-dim">SOC 2 Type II</span>\n            <span class="tag tag-dim">Multi-Region · US/AU/EU</span>\n            <span class="tag tag-amber">No Public Vuln Disclosure</span>',
    '[{"l":"V","s":7,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":9,"m":15},{"l":"I","s":5,"m":10},{"l":"C","s":4,"m":10},{"l":"T","s":4,"m":10}]',
    "120.0,94.8 120.0,120.0 169.1,131.2 138.7,158.9 104.4,152.4 91.9,126.4 97.5,102.0", 43)

marker_llama = '    <!-- LlamaIndex 41 -->'
if marker_llama in html:
    html = html.replace(marker_llama, rel_card + marker_llama)
    print("  ✓ Relevance AI card inserted before LlamaIndex")

# Letta: insert before Coze (35)
letta_card = card("Letta 37", "letta", "letta",
    "Letta", "Stateful AI Agent Framework · Open Source (Apache 2.0)", "Letta Inc. · San Francisco (UC Berkeley)",
    "Evaluated 2026.03.30 · Framework v0.3.1",
    "Pioneered stateful agent architecture. Zero CVEs in trailing 12 months. Self-hosted preserves data sovereignty. Hosted service data may be used for model training. No SOC 2, no SECURITY.md.",
    '<span class="tag tag-dim">Apache 2.0 · UC Berkeley</span>\n            <span class="tag tag-red">Hosted Data May Train Models</span>\n            <span class="tag tag-amber">No SOC 2 · Seed Stage</span>',
    '[{"l":"V","s":12,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":3,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":3,"m":10,"low":true}]',
    "120.0,76.8 120.0,120.0 169.1,131.2 126.2,133.0 113.8,133.0 98.9,124.8 103.1,106.5", 37)

marker_coze = '    <!-- Coze 35 -->'
if marker_coze in html:
    html = html.replace(marker_coze, letta_card + marker_coze)
    print("  ✓ Letta card inserted before Coze")

# Update hero stat: 22 → 26
html = html.replace(
    '<span class="stat-num">22<span> / 100</span></span>',
    '<span class="stat-num">26<span> / 100</span></span>')
print("  ✓ Hero stat updated: 22 → 26")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

# === UPDATE SITEMAP ===
new_urls = """  <url>
    <loc>https://getverdict.fyi/amazon-q-business/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://getverdict.fyi/relevance-ai/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://getverdict.fyi/letta/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://getverdict.fyi/composio/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
"""
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()
sitemap = sitemap.replace('</urlset>', new_urls + '</urlset>')
with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("  ✓ sitemap.xml updated with 4 new URLs")

# === UPDATE ALL INDIVIDUAL PAGE RANKS ===
# New full ranking (26 platforms):
# 1: Amazon Q Business (NEW)
# 2: Vertex AI (was 1)
# 3: Copilot Studio (was 2) — tied with OpenAI at 61, alphabetical: Copilot before OpenAI
# 4: OpenAI Assistants (was 3)
# 5: Agentforce (was 4)
# 6: AutoGen (was 5)
# 7: Pipedream (was 6)
# 8: AWS Bedrock (was 7)
# 9: Activepieces (was 8)
# 10: LangChain (was 9)
# 11: IBM watsonx (was 10)
# 12: Zapier (was 11)
# 13: Haystack (was 12)
# 14: Composio (NEW, 46, alphabetical before Dify)
# 15: Dify (was 13)
# 16: Make.com (was 14)
# 17: Semantic Kernel (was 15)
# 18: Botpress (was 16)
# 19: CrewAI (was 17)
# 20: Relevance AI (NEW, 43)
# 21: LlamaIndex (was 18)
# 22: Letta (NEW, 37)
# 23: Coze (was 19)
# 24: n8n (was 20)
# 25: Flowise (was 21)
# 26: Langflow (was 22)

rank_changes = {
    "vertex-ai": (1, 2),
    "copilot-studio": (2, 3),
    "openai-assistants": (3, 4),
    "agentforce": (4, 5),
    "autogen": (5, 6),
    "pipedream": (6, 7),
    "bedrock-agents": (7, 8),
    "activepieces": (8, 9),
    "langchain": (9, 10),
    "watsonx-orchestrate": (10, 11),
    "zapier": (11, 12),
    "haystack": (12, 13),
    "dify": (13, 15),
    "make": (14, 16),
    "semantic-kernel": (15, 17),
    "botpress": (16, 18),
    "crewai": (17, 19),
    "llamaindex": (18, 21),
    "coze": (19, 23),
    "n8n": (20, 24),
    "flowise": (21, 25),
    "langflow": (22, 26),
}

all_dirs = list(rank_changes.keys())

for dirname in all_dirs:
    filepath = os.path.join(dirname, "index.html")
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    original = content
    
    content = content.replace("of 22 platforms evaluated", "of 26 platforms evaluated")
    content = content.replace("All 22 Evaluations", "All 26 Evaluations")
    
    old_rank, new_rank = rank_changes[dirname]
    content = content.replace(f"Rank #{old_rank} of", f"Rank #{new_rank} of")
    
    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  ✓ {filepath}: Rank #{old_rank} → #{new_rank}, count → 26")

print("\nDone. Ready to: git add . && git commit && git push")
