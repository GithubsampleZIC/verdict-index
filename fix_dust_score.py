#!/usr/bin/env python3
"""
VERDICT: Dust score correction 55→57 (T dimension 2→4)
Vendor-reported: VDP (HackerOne), security.txt, SECURITY.md confirmed.
Run from ~/Desktop/verdict-index/
"""
import os, re

# === 1. UPDATE dust/index.html ===
fp = "dust/index.html"
with open(fp, 'r') as f:
    c = f.read()

# Score 55 → 57
c = c.replace('<span class="score-big">55</span>', '<span class="score-big">57</span>')
# Rank #9 → #6
c = c.replace('Rank #9 of 31', 'Rank #6 of 31')
# T dimension: s:2,m:10,"low":true → s:4,m:10
c = c.replace('"T","s":2,"m":10,"low":true', '"T","s":4,"m":10')
# Radar points: T changed from 4/10 fraction
# Old: 120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 108.7,111.0
# New: 120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 97.5,102.0
c = c.replace(
    "120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 108.7,111.0",
    "120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 97.5,102.0"
)
# Update meta description
c = c.replace("Score: 55/85", "Score: 57/85")
# Update OG title
c = c.replace("VERDICT Score: 55/85", "VERDICT Score: 57/85")
# Update finding text to reflect VDP
c = c.replace(
    "Score moderated by limited public transparency documentation and undocumented agent action containment.",
    "Vulnerability disclosure program (HackerOne) and SECURITY.md confirmed. Score moderated by undocumented agent action containment."
)
# Update tags: remove No SECURITY.md tag, add VDP tag
c = c.replace(
    '<span class="tag tag-amber">No SECURITY.md · No VDP</span>',
    '<span class="tag tag-safe">VDP · HackerOne + SECURITY.md</span>'
)

with open(fp, 'w') as f:
    f.write(c)
print(f"  ✓ {fp}: Score 55→57, Rank #9→#6, T:2→4, radar updated, tags updated")

# === 2. UPDATE index.html — move Dust card and update score ===
with open('index.html', 'r') as f:
    html = f.read()

# Step 2a: Find and extract the Dust card
# The card starts with "    <!-- Dust 55 -->" and ends before the next "    <!-- " card comment
dust_start = html.find('    <!-- Dust 55 -->')
if dust_start == -1:
    print("  ✗ Dust card not found!")
else:
    # Find the next card after Dust
    next_card = html.find('\n    <!-- ', dust_start + 10)
    dust_card = html[dust_start:next_card]

    # Remove the card from current position
    html = html[:dust_start] + html[next_card:]

    # Update the card content
    dust_card = dust_card.replace('<!-- Dust 55 -->', '<!-- Dust 57 -->')
    dust_card = dust_card.replace('<span class="score-main">55</span>', '<span class="score-main">57</span>')
    dust_card = dust_card.replace('"T","s":2,"m":10,"low":true', '"T","s":4,"m":10')
    dust_card = dust_card.replace(
        "120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 108.7,111.0",
        "120.0,73.2 120.0,120.0 179.7,133.6 147.0,176.2 98.2,165.4 98.9,124.8 97.5,102.0"
    )
    # Update finding and tags on main card
    dust_card = dust_card.replace("No SECURITY.md", "VDP (HackerOne)")

    # Insert before AutoGen (currently <!-- AutoGen 56 -->)
    autogen_marker = '    <!-- AutoGen 56 -->'
    insert_pos = html.find(autogen_marker)
    if insert_pos != -1:
        html = html[:insert_pos] + dust_card + '\n' + html[insert_pos:]
        print("  ✓ Dust card moved: #9 → #6 (before AutoGen)")
    else:
        print("  ✗ AutoGen marker not found!")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

# === 3. UPDATE affected individual page ranks ===
rank_updates = {
    "autogen": (6, 7),
    "pipedream": (7, 8),
    "bedrock-agents": (8, 9),
}

for dirname, (old_r, new_r) in rank_updates.items():
    fp = os.path.join(dirname, "index.html")
    if not os.path.exists(fp):
        continue
    with open(fp, 'r') as f:
        c = f.read()
    c = c.replace(f"Rank #{old_r} of", f"Rank #{new_r} of")
    with open(fp, 'w') as f:
        f.write(c)
    print(f"  ✓ {fp}: Rank #{old_r} → #{new_r}")

print("\nDone. git add . && git commit && git push")
