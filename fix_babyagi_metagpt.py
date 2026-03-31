#!/usr/bin/env python3
"""Fix: insert BabyAGI and MetaGPT cards after Langflow in index.html"""

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

babyagi = card("BabyAGI 24","babyagi","babyagi","BabyAGI","Experimental Autonomous Agent · OSS (MIT)","Yohei Nakajima · Individual","Evaluated 2026.03.31 · Framework v0.3.1",
    "First popular autonomous agent (2023). Experimental only. Self-building agent, no containment. I/C/T: all 0.",
    '<span class="tag tag-dim">MIT · 22.2k Stars</span>\n            <span class="tag tag-red">I/C/T: All 0/10</span>\n            <span class="tag tag-amber">Not for Production</span>',
    '[{"l":"V","s":8,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":14,"m":20},{"l":"D","s":2,"m":15,"low":true},{"l":"I","s":0,"m":10,"low":true},{"l":"C","s":0,"m":10,"low":true},{"l":"T","s":0,"m":10,"low":true}]',
    "120.0,91.2 120.0,120.0 169.1,131.2 124.2,128.7 120.0,120.0 120.0,120.0 120.0,120.0",24)

metagpt = card("MetaGPT 23","metagpt","metagpt","MetaGPT","Multi-Agent Dev Framework · OSS (MIT)","DeepWisdom · Shenzhen, China","Evaluated 2026.03.31 · Framework v0.3.1",
    "66k stars, ICLR 2024. Two CVSS 9.8 RCEs unpatched. Vendor unresponsive. D: 0/15. Four CVEs in 12 months.",
    '<span class="tag tag-red">2x CVSS 9.8 · Unpatched</span>\n            <span class="tag tag-red">Vendor Unresponsive</span>\n            <span class="tag tag-red">D: 0/15</span>\n            <span class="tag tag-dim">MIT · 66k Stars</span>',
    '[{"l":"V","s":11,"m":20},{"l":"E","s":0,"m":15,"inactive":true},{"l":"R","s":4,"m":20,"low":true},{"l":"D","s":0,"m":15,"low":true},{"l":"I","s":2,"m":10,"low":true},{"l":"C","s":5,"m":10},{"l":"T","s":1,"m":10,"low":true}]',
    "120.0,80.4 120.0,120.0 134.0,123.2 120.0,120.0 113.8,133.0 84.9,128.0 114.4,115.5",23)

# Debug: find what Langflow marker looks like
import re
# Search for any Langflow comment pattern
matches = list(re.finditer(r'<!-- Langflow.*?-->', html))
for m in matches:
    print(f"  Found marker: '{m.group()}' at position {m.start()}")

# Try to find the last eval-card closing tag
# Look for Langflow card and find the </a> after it
for m in matches:
    pos = m.start()
    close_a = html.find('</a>', pos)
    if close_a != -1:
        insert_pos = close_a + len('</a>')
        html = html[:insert_pos] + '\n' + babyagi + metagpt + html[insert_pos:]
        print(f"  ✓ BabyAGI + MetaGPT inserted after Langflow card")
        break
else:
    # Fallback: find the last </a> before the eval-grid closing div
    print("  ! Langflow marker not found. Trying fallback...")
    # Find the last eval-card
    last_card = html.rfind('</a>\n')
    if last_card != -1:
        insert_pos = last_card + len('</a>')
        html = html[:insert_pos] + '\n' + babyagi + metagpt + html[insert_pos:]
        print(f"  ✓ BabyAGI + MetaGPT inserted at end of cards (fallback)")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")
print("\nDone. git add . && git commit && git push")
