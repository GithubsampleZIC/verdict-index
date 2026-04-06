#!/usr/bin/env python3
"""
VERDICT: Add navigation strip to index.html
Inserts between hero/stats section and first eval card.
Run from ~/Desktop/verdict-index/
"""

with open('index.html', 'r') as f:
    html = f.read()

# The navigation strip HTML
nav_strip = """
    <!-- Quick Navigation -->
    <div class="quick-nav">
      <a href="/rankings/" class="qn-btn qn-primary">Full Rankings</a>
      <a href="/compare/coding-agents/" class="qn-btn">Coding Agents</a>
      <a href="/compare/ai-app-builders/" class="qn-btn">AI App Builders</a>
      <a href="/compare/n8n-vs-make/" class="qn-btn">n8n vs Make</a>
      <a href="/methodology/" class="qn-btn">Methodology</a>
    </div>

"""

# CSS for the nav strip
nav_css = """.quick-nav{display:flex;flex-wrap:wrap;gap:.6rem;padding:1.5rem 0 2rem;border-bottom:1px solid var(--divider);margin-bottom:2.5rem;}.qn-btn{font-family:var(--mono);font-size:.68rem;letter-spacing:.08em;color:var(--navy);padding:.45rem .9rem;border:1px solid var(--divider);text-decoration:none;transition:all .15s;white-space:nowrap;}.qn-btn:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}.qn-primary{background:var(--navy);color:var(--white);border-color:var(--navy);}.qn-primary:hover{background:var(--navy-light);border-color:var(--navy-light);}
"""

# Insert CSS before </style>
html = html.replace('</style>', nav_css + '</style>', 1)
print("  ✓ Nav CSS added")

# Insert nav strip before the first eval card
marker = '    <!-- Amazon Q Business 68 -->'
if marker in html:
    html = html.replace(marker, nav_strip + marker, 1)
    print("  ✓ Nav strip inserted before first card")
else:
    print("  ! First card marker not found — trying regex")
    import re
    m = re.search(r'\n    <!-- .+? \d+ -->\n    <a class="eval-card"', html)
    if m:
        html = html[:m.start()] + '\n' + nav_strip + html[m.start():]
        print("  ✓ Nav strip inserted (regex fallback)")
    else:
        print("  ✗ FAILED: Could not find insertion point")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")

print("\n✓ Done. git add . && git commit && git push")
