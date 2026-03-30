#!/usr/bin/env python3
"""
Add IBM watsonx Orchestrate and Haystack to VERDICT main site.
Run from ~/Desktop/verdict-index/
"""
import re, os

RADAR_RINGS = """          <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/>
          <polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/>
          <polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/>
          <polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>"""

RADAR_AXES = """          <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/>
          <line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/>
          <line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/>
          <line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/>
          <line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/>
          <line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>"""

RADAR_LABELS = """          <text class="radar-label" x="120" y="22" text-anchor="middle">V</text>
          <text class="radar-label radar-label-inactive" x="197" y="64" text-anchor="start">E</text>
          <text class="radar-label" x="215" y="144" text-anchor="start">R</text>
          <text class="radar-label" x="164" y="213" text-anchor="start">D</text>
          <text class="radar-label" x="76" y="213" text-anchor="end">I</text>
          <text class="radar-label" x="25" y="144" text-anchor="end">C</text>
          <text class="radar-label" x="43" y="64" text-anchor="end">T</text>"""

def make_card(comment, href, platform, name, category, owner, date, finding, tags_html, dims_json, radar_points, score):
    return f"""
    <!-- {comment} -->
    <a class="eval-card" href="/{href}/" data-platform="{platform}">
      <div class="card-left">
        <div class="card-meta">
          <div class="platform-name">{name}</div>
          <div class="platform-category">{category}</div>
          <div class="platform-owner">{owner}</div>
          <div class="platform-date">{date}</div>
          <div class="key-finding">{finding}</div>
          <div class="incident-tags">
            {tags_html}
          </div>
        </div>
        <div class="dim-list" data-dims='{dims_json}'></div>
      </div>
      <div class="card-right">
        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
{RADAR_RINGS}
{RADAR_AXES}
          <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{radar_points}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{radar_points}"/></g>
{RADAR_LABELS}
        </svg></div>
        <div class="score-display"><span class="score-main">{score}</span><span class="score-denom">&thinsp;/&thinsp;85</span><div class="score-layer">Layer 0 · Public Docs</div></div>
      </div>
    </a>
"""

# === IBM watsonx Orchestrate card ===
watsonx_card = make_card(
    comment="IBM watsonx Orchestrate 48",
    href="watsonx-orchestrate",
    platform="watsonx-orchestrate",
    name="IBM watsonx Orchestrate",
    category="Enterprise AI Agent Platform · Cloud SaaS + On-Prem",
    owner="IBM Corporation",
    date="Evaluated 2026.03.30 · Framework v0.3.1",
    finding="FedRAMP authorized, SOC 2, ISO 27001. Client data explicitly not used for IBM model training. 10+ dependency CVEs including CVSS 9.1, plus IBM-specific SQL injection (CVE-2025-0165). Langflow (CISA KEV, 30/85) integrated via DataStax acquisition.",
    tags_html="""<span class="tag tag-red">10+ CVEs · CVSS 9.1</span>
            <span class="tag tag-red">CVE-2025-0165 · SQL Injection</span>
            <span class="tag tag-amber">Langflow · CISA KEV Portfolio</span>""",
    dims_json='[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":7,"m":20,"low":true},{"l":"D","s":9,"m":15},{"l":"I","s":7,"m":10,"high":true},{"l":"C","s":6,"m":10},{"l":"T","s":8,"m":10,"high":true}]',
    radar_points="120.0,80.4 120.0,120.0 144.6,125.6 138.7,158.9 98.2,165.4 77.9,129.6 75.0,84.1",
    score=48
)

# === Haystack card ===
haystack_card = make_card(
    comment="Haystack 47",
    href="haystack",
    platform="haystack",
    name="Haystack",
    category="AI Application Framework · Open Source (Apache 2.0)",
    owner="deepset GmbH · Berlin, Germany",
    date="Evaluated 2026.03.30 · Framework v0.3.1",
    finding="Zero CVEs in trailing 12 months. Full Apache 2.0 open source with monthly releases. SOC 2 Type 2 for enterprise platform. German company (GDPR). No built-in sandbox or access control in OSS framework. Telemetry default ON with easy opt-out.",
    tags_html="""<span class="tag tag-dim">0 CVEs · Trailing 12 Months</span>
            <span class="tag tag-dim">Apache 2.0 · 18K+ Stars</span>
            <span class="tag tag-amber">Telemetry Default ON</span>""",
    dims_json='[{"l":"V","s":15,"m":20,"high":true},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":17,"m":20,"high":true},{"l":"D","s":5,"m":15},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":3,"m":10,"low":true},{"l":"T","s":5,"m":10}]',
    radar_points="120.0,66.0 120.0,120.0 179.7,133.6 130.4,141.6 113.8,133.0 98.9,124.8 91.8,97.5",
    score=47
)

# === 1. Update index.html ===
with open('index.html', 'r') as f:
    html = f.read()

# Insert watsonx card before Zapier (48)
marker_zapier = '    <!-- Zapier 48 -->'
if marker_zapier in html:
    html = html.replace(marker_zapier, watsonx_card + marker_zapier)
    print("  ✓ IBM watsonx Orchestrate card inserted before Zapier")
else:
    print("  ✗ Zapier marker not found")

# Insert Haystack card before Dify (46)
marker_dify = '    <!-- Dify 46 -->'
if marker_dify in html:
    html = html.replace(marker_dify, haystack_card + marker_dify)
    print("  ✓ Haystack card inserted before Dify")
else:
    print("  ✗ Dify marker not found")

# Update hero stat: 20 → 22
html = html.replace(
    '<span class="stat-num">20<span> / 100</span></span>',
    '<span class="stat-num">22<span> / 100</span></span>'
)
print("  ✓ Hero stat updated: 20 → 22")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

# === 2. Update sitemap.xml ===
new_urls = """  <url>
    <loc>https://getverdict.fyi/watsonx-orchestrate/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://getverdict.fyi/haystack/</loc>
    <lastmod>2026-03-30</lastmod>
    <priority>0.8</priority>
  </url>
"""

with open('sitemap.xml', 'r') as f:
    sitemap = f.read()
sitemap = sitemap.replace('</urlset>', new_urls + '</urlset>')
with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("  ✓ sitemap.xml updated with 2 new URLs")

# === 3. Update rank numbers on individual pages ===
# New ranking (22 platforms):
# 1-9: unchanged
# 10: IBM watsonx Orchestrate (NEW)
# 11: Zapier (was #10)
# 12: Haystack (NEW)
# 13: Dify (was #11)
# 14: Make.com (was #12)
# 15: Semantic Kernel (was #13)
# 16: Botpress (was #14)
# 17: CrewAI (was #15)
# 18: LlamaIndex (was #16)
# 19: Coze (was #17)
# 20: n8n (was #18)
# 21: Flowise (was #19)
# 22: Langflow (was #20)

rank_changes = {
    "zapier": (10, 11),
    "dify": (11, 13),
    "make": (12, 14),
    "semantic-kernel": (13, 15),
    "botpress": (14, 16),
    "crewai": (15, 17),
    "llamaindex": (16, 18),
    "coze": (17, 19),
    "n8n": (18, 20),
    "flowise": (19, 21),
    "langflow": (20, 22),
}

# Also update "of 20 platforms" → "of 22 platforms" on ALL pages
all_dirs = [
    "vertex-ai", "copilot-studio", "openai-assistants", "agentforce",
    "autogen", "pipedream", "bedrock-agents", "activepieces", "langchain",
    "zapier", "dify", "make", "semantic-kernel", "botpress", "crewai",
    "llamaindex", "coze", "n8n", "flowise", "langflow"
]

for dirname in all_dirs:
    filepath = os.path.join(dirname, "index.html")
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r') as f:
        content = f.read()
    original = content

    # Update total count
    content = content.replace("of 20 platforms evaluated", "of 22 platforms evaluated")
    content = content.replace("All 20 Evaluations", "All 22 Evaluations")

    # Update rank if needed
    if dirname in rank_changes:
        old_rank, new_rank = rank_changes[dirname]
        content = content.replace(f"Rank #{old_rank} of", f"Rank #{new_rank} of")

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        if dirname in rank_changes:
            old_r, new_r = rank_changes[dirname]
            print(f"  ✓ {filepath}: Rank #{old_r} → #{new_r}, count 20→22")
        else:
            print(f"  ✓ {filepath}: count 20→22")

# Also update autogen page
autogen_path = "autogen/index.html"
if os.path.exists(autogen_path):
    with open(autogen_path, 'r') as f:
        c = f.read()
    c = c.replace("of 20 platforms evaluated", "of 22 platforms evaluated")
    c = c.replace("All 20 Evaluations", "All 22 Evaluations")
    with open(autogen_path, 'w') as f:
        f.write(c)
    print(f"  ✓ {autogen_path}: count 20→22")

print("\nDone. Ready to git add/commit/push.")
