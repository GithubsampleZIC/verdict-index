#!/usr/bin/env python3
"""Add nav links to index.html header: About, Methodology, Q1 Report"""

with open('index.html', 'r') as f:
    html = f.read()

# Current header structure has the logo and possibly nothing else on the right
# We need to add nav links. Find the closing </header> and add nav before it.

# The header in the main page likely looks different from individual pages
# (individual pages have "← All Evaluations" link)
# Let's find the header and add a nav section

old_header_close = '</header>'

# Add a nav with links
nav_links = '''<nav style="display:flex;gap:1.5rem;align-items:center;">
      <a href="/about/" style="font-family:var(--mono);font-size:.7rem;letter-spacing:.05em;color:var(--caption);text-decoration:none;">About</a>
      <a href="/methodology/" style="font-family:var(--mono);font-size:.7rem;letter-spacing:.05em;color:var(--caption);text-decoration:none;">Methodology</a>
      <a href="/report/q1-2026/" style="font-family:var(--mono);font-size:.7rem;letter-spacing:.05em;color:var(--caption);text-decoration:none;">Q1 Report</a>
    </nav>'''

# Check if nav already exists
if '/about/' in html.split('</header>')[0]:
    print("  ! Nav links already exist in header. Skipping.")
else:
    # Insert nav before </header>
    html = html.replace(old_header_close, '  ' + nav_links + '\n  ' + old_header_close, 1)
    print("  ✓ Nav links added to main site header")

with open('index.html', 'w') as f:
    f.write(html)

print("Done. git add . && git commit && git push")
