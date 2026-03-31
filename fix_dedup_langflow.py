#!/usr/bin/env python3
"""
Fix: deduplicate cards, restore Langflow, re-sort all 36 cards.
Run from ~/Desktop/verdict-index/
"""
import re

with open('index.html', 'r') as f:
    html = f.read()

# Extract all cards
card_pattern = re.compile(
    r'(\n    <!-- (.+?) (\d+) -->\n    <a class="eval-card".*?</a>)',
    re.DOTALL
)
matches = list(card_pattern.finditer(html))
print(f"Found {len(matches)} cards (expecting duplicates)")

# Deduplicate: keep first occurrence of each name
seen = set()
cards = []
for m in matches:
    full_html = m.group(1)
    name = m.group(2)
    score = int(m.group(3))
    if name not in seen:
        seen.add(name)
        cards.append({'html': full_html, 'name': name, 'score': score})
        print(f"  KEEP: {name} ({score}/85)")
    else:
        print(f"  SKIP duplicate: {name} ({score}/85)")

print(f"\nUnique cards: {len(cards)}")

# Check if Langflow is present
langflow_present = any(c['name'] == 'Langflow' for c in cards)
print(f"Langflow present: {langflow_present}")

if not langflow_present:
    print("  Restoring Langflow card...")
    SVG = """        <div class="radar-wrap"><svg class="radar-svg" viewBox="0 0 240 240">
          <polygon class="radar-ring" points="120,102 134.1,108.8 137.5,124 127.8,136.2 112.2,136.2 102.5,124 105.9,108.8"/><polygon class="radar-ring" points="120,84 148.1,97.6 155.1,128 135.6,152.4 104.4,152.4 84.9,128 91.9,97.6"/><polygon class="radar-ring" points="120,66 162.2,86.3 172.6,132 143.4,168.7 96.6,168.7 67.4,132 77.8,86.3"/><polygon class="radar-ring" points="120,48 176.3,75.1 190.2,136 151.2,184.9 88.8,184.9 49.8,136 63.7,75.1"/>
          <line class="radar-axis" x1="120" y1="120" x2="120" y2="48"/><line class="radar-axis radar-axis-inactive" x1="120" y1="120" x2="176.3" y2="75.1"/><line class="radar-axis" x1="120" y1="120" x2="190.2" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="151.2" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="88.8" y2="184.9"/><line class="radar-axis" x1="120" y1="120" x2="49.8" y2="136"/><line class="radar-axis" x1="120" y1="120" x2="63.7" y2="75.1"/>
          <g class="radar-data"><polygon class="radar-poly-fill" fill="#1B2A4A" points="{pts}"/><polygon class="radar-poly-stroke" stroke="#1B2A4A" points="{pts}"/></g>
          <text class="radar-label" x="120" y="22" text-anchor="middle">V</text><text class="radar-label radar-label-inactive" x="197" y="64" text-anchor="start">E</text><text class="radar-label" x="215" y="144" text-anchor="start">R</text><text class="radar-label" x="164" y="213" text-anchor="start">D</text><text class="radar-label" x="76" y="213" text-anchor="end">I</text><text class="radar-label" x="25" y="144" text-anchor="end">C</text><text class="radar-label" x="43" y="64" text-anchor="end">T</text>
        </svg></div>"""

    # Langflow radar points (from original: V=5/20, R=4/20, D=4/15, I=5/10, C=4/10, T=6/10)
    langflow_card = f"""
    <!-- Langflow 30 -->
    <a class="eval-card" href="/langflow/" data-platform="langflow">
      <div class="card-left">
        <div class="card-meta">
          <div class="platform-name">Langflow</div>
          <div class="platform-category">Visual AI Agent Builder · Open Source</div>
          <div class="platform-owner">IBM (DataStax Acquisition)</div>
          <div class="platform-date">Evaluated 2026.03.24 · Framework v0.3.1</div>
          <div class="key-finding">CISA KEV listed (CVE-2025-3248). IBM acquired via DataStax. 6 CVEs in March 2026 cluster. Auth not enforced across critical endpoints.</div>
          <div class="incident-tags"><span class="tag tag-red">CISA KEV · CVE-2025-3248</span>
            <span class="tag tag-red">6 CVEs · Mar 2026</span>
            <span class="tag tag-dim">IBM Acquired · Aug 2025</span></div>
        </div>
        <div class="dim-list" data-dims='[{{"l":"V","s":5,"m":20,"low":true}},{{"l":"E","s":0,"m":15,"inactive":true}},{{"l":"R","s":4,"m":20,"low":true}},{{"l":"D","s":4,"m":15,"low":true}},{{"l":"I","s":5,"m":10}},{{"l":"C","s":4,"m":10}},{{"l":"T","s":6,"m":10}}]'></div>
      </div>
      <div class="card-right">
{SVG.format(pts="120.0,102.0 120.0,120.0 134.0,123.2 128.3,137.3 104.4,152.4 91.9,126.4 86.2,93.1")}
        <div class="score-display"><span class="score-main">30</span><span class="score-denom">&thinsp;/&thinsp;85</span><div class="score-layer">Layer 0 &middot; Public Docs</div></div>
      </div>
    </a>"""

    cards.append({'html': langflow_card, 'name': 'Langflow', 'score': 30})
    print(f"  ✓ Langflow restored (30/85)")

# Sort: descending by score, then alphabetical by name for ties
cards.sort(key=lambda c: (-c['score'], c['name']))

print(f"\nFinal sorted order ({len(cards)} cards):")
for i, c in enumerate(cards):
    print(f"  #{i+1}: {c['name']} ({c['score']}/85)")

# Replace the card section
first_start = matches[0].start()
last_end = matches[-1].end()
new_cards_html = ''.join(c['html'] for c in cards)
html = html[:first_start] + new_cards_html + html[last_end:]

with open('index.html', 'w') as f:
    f.write(html)

print(f"\n✓ {len(cards)} unique cards sorted and saved")
print("Ready to: git add . && git commit && git push")
