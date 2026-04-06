#!/usr/bin/env python3
"""Fix: nav buttons → card style. Run from ~/Desktop/verdict-index/"""

with open('index.html', 'r') as f:
    html = f.read()

old_css = """.quick-nav{display:flex;flex-wrap:wrap;gap:.75rem;padding:2rem 0 2.5rem;border-bottom:1px solid var(--divider);margin-bottom:2.5rem;}.qn-btn{font-family:var(--mono);font-size:.78rem;letter-spacing:.08em;color:var(--navy);padding:.7rem 1.3rem;border:1.5px solid var(--divider);text-decoration:none;transition:all .15s;white-space:nowrap;}.qn-btn:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}.qn-primary{background:var(--navy);color:var(--white);border-color:var(--navy);font-weight:500;}.qn-primary:hover{background:var(--navy-light);border-color:var(--navy-light);}"""

new_css = """.quick-nav{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem;padding:2rem 0 2.5rem;border-bottom:1px solid var(--divider);margin-bottom:2.5rem;}.qn-btn{font-family:var(--mono);font-size:.75rem;letter-spacing:.06em;color:var(--navy);padding:1.1rem 1rem;background:var(--ice);border:1.5px solid var(--divider);text-decoration:none;transition:all .2s;text-align:center;display:flex;align-items:center;justify-content:center;}.qn-btn:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;transform:translateY(-2px);box-shadow:0 4px 12px rgba(27,42,74,.15);}.qn-primary{background:var(--navy);color:var(--white);border-color:var(--navy);font-weight:500;font-size:.8rem;}.qn-primary:hover{background:var(--navy-light);border-color:var(--navy-light);transform:translateY(-2px);box-shadow:0 4px 12px rgba(27,42,74,.25);}@media(max-width:600px){.quick-nav{grid-template-columns:1fr 1fr;}}"""

if old_css in html:
    html = html.replace(old_css, new_css)
    print("  ✓ Nav buttons → card style")
else:
    print("  ✗ CSS not found")

with open('index.html', 'w') as f:
    f.write(html)
print("  ✓ index.html saved")
print("\n✓ Done. git add . && git commit && git push")
