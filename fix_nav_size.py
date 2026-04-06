#!/usr/bin/env python3
"""Fix: enlarge quick-nav buttons. Run from ~/Desktop/verdict-index/"""

with open('index.html', 'r') as f:
    html = f.read()

old_css = """.quick-nav{display:flex;flex-wrap:wrap;gap:.6rem;padding:1.5rem 0 2rem;border-bottom:1px solid var(--divider);margin-bottom:2.5rem;}.qn-btn{font-family:var(--mono);font-size:.68rem;letter-spacing:.08em;color:var(--navy);padding:.45rem .9rem;border:1px solid var(--divider);text-decoration:none;transition:all .15s;white-space:nowrap;}.qn-btn:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}.qn-primary{background:var(--navy);color:var(--white);border-color:var(--navy);}.qn-primary:hover{background:var(--navy-light);border-color:var(--navy-light);}"""

new_css = """.quick-nav{display:flex;flex-wrap:wrap;gap:.75rem;padding:2rem 0 2.5rem;border-bottom:1px solid var(--divider);margin-bottom:2.5rem;}.qn-btn{font-family:var(--mono);font-size:.78rem;letter-spacing:.08em;color:var(--navy);padding:.7rem 1.3rem;border:1.5px solid var(--divider);text-decoration:none;transition:all .15s;white-space:nowrap;}.qn-btn:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}.qn-primary{background:var(--navy);color:var(--white);border-color:var(--navy);font-weight:500;}.qn-primary:hover{background:var(--navy-light);border-color:var(--navy-light);}"""

if old_css in html:
    html = html.replace(old_css, new_css)
    print("  ✓ Nav buttons enlarged")
else:
    print("  ✗ CSS not found")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")
print("\n✓ Done. git add . && git commit && git push")
