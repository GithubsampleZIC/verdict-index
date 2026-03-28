#!/usr/bin/env python3
"""
VERDICT Individual Page Converter — Old Dark Theme → New Light Theme
Usage: python3 convert_pages.py <input_dir_or_file> [output_dir]

Processes all index.html files in subdirectories, or a single file.
Preserves all unique content (titles, meta, scores, radar data, etc.)
while replacing the design system.
"""

import re
import sys
import os

NEW_CSS = """<style>
:root {
  --white:#FFFFFF;--ice:#F5F6F8;--navy:#1B2A4A;--navy-light:#2A3D66;
  --heading:#1A1A2E;--body:#4A5060;--caption:#6B7280;
  --risk:#C4332B;--risk-bg:rgba(196,51,43,0.06);
  --caution:#C08520;--caution-bg:rgba(192,133,32,0.06);
  --safe:#2D7A4F;--safe-bg:rgba(45,122,79,0.06);
  --neutral:#D0D4DC;--divider:#E2E5EB;
  --serif:'Source Serif 4',Georgia,serif;--sans:'Libre Franklin',-apple-system,sans-serif;--mono:'JetBrains Mono',monospace;--score:'Merriweather',Georgia,serif;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--white);color:var(--body);font-family:var(--sans);font-weight:400;line-height:1.6;-webkit-font-smoothing:antialiased;}
a{color:var(--navy);text-decoration:none;}
a:hover{text-decoration:underline;}

header{padding:0 3rem;height:64px;display:flex;align-items:center;justify-content:space-between;background:var(--white);border-bottom:1px solid var(--divider);}
.logo{display:flex;align-items:baseline;gap:.75rem;text-decoration:none;}
.logo:hover{text-decoration:none;}
.logo-mark{font-family:var(--serif);font-size:1.3rem;font-weight:700;letter-spacing:.1em;color:var(--navy);}
.logo-divider{width:1px;height:18px;background:var(--divider);align-self:center;}
.logo-sub{font-family:var(--sans);font-size:.8rem;font-weight:500;letter-spacing:.08em;color:var(--caption);text-transform:uppercase;}
.back{font-family:var(--sans);font-size:.8rem;font-weight:500;color:var(--caption);text-decoration:none;}
.back:hover{color:var(--navy);text-decoration:none;}

.wrap{max-width:960px;margin:0 auto;padding:4rem 3rem;}
.breadcrumb{font-family:var(--mono);font-size:.8rem;color:var(--caption);margin-bottom:2rem;}
.breadcrumb a{color:var(--caption);}
.breadcrumb a:hover{color:var(--navy);}

h1{font-family:var(--serif);font-size:clamp(2rem,4vw,3rem);font-weight:700;line-height:1.1;color:var(--heading);margin-bottom:.4rem;}
.meta{font-family:var(--sans);font-size:.8rem;color:var(--caption);margin-bottom:.3rem;}
.meta-owner{font-family:var(--mono);font-size:.8rem;color:var(--navy);margin-bottom:1.5rem;}

.score-hero{display:flex;align-items:center;gap:2.5rem;margin-bottom:3rem;padding:2rem 0;border-top:1px solid var(--divider);border-bottom:1px solid var(--divider);}
.score-big{font-family:var(--score);font-weight:900;font-size:4rem;line-height:1;color:var(--navy);font-variant-numeric:tabular-nums;}
.score-denom{font-family:var(--score);font-size:1.2rem;color:var(--caption);font-weight:400;}
.score-meta{font-family:var(--sans);font-size:.8rem;color:var(--caption);line-height:1.8;}

.finding{font-size:.9rem;line-height:1.75;color:var(--body);border-left:3px solid var(--navy);padding-left:1rem;margin-bottom:2rem;}

.tags{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:3rem;}
.tag{font-family:var(--mono);font-size:.8rem;font-weight:500;letter-spacing:.04em;padding:.25rem .6rem;border:1px solid;}
.tag-red{border-color:rgba(196,51,43,0.25);color:var(--risk);background:var(--risk-bg);}
.tag-amber{border-color:rgba(192,133,32,0.25);color:var(--caution);background:var(--caution-bg);}
.tag-dim{border-color:var(--divider);color:var(--caption);background:var(--ice);}
.tag-warn{border-color:rgba(192,133,32,0.25);color:var(--caution);background:var(--caution-bg);}

.radar-section{display:flex;gap:3rem;align-items:flex-start;margin-bottom:3rem;flex-wrap:wrap;}
.radar-wrap{width:260px;height:260px;flex-shrink:0;}
.radar-svg{width:100%;height:100%;overflow:visible;}
.radar-ring{fill:none;stroke:var(--divider);stroke-width:.5;}
.radar-axis{stroke:var(--divider);stroke-width:.5;}
.radar-axis-inactive{stroke:var(--neutral);stroke-width:.5;stroke-dasharray:2 3;}
.radar-label{font-family:var(--mono);font-size:10px;font-weight:600;fill:var(--navy);letter-spacing:.05em;}
.radar-label-inactive{fill:var(--neutral);}
.radar-poly-fill{opacity:.10;}
.radar-poly-stroke{fill:none;stroke-width:1.5;stroke-linejoin:round;}

.dim-list{display:flex;flex-direction:column;gap:.7rem;flex:1;min-width:240px;}
.dim-row{display:grid;grid-template-columns:16px 1fr 56px;align-items:center;gap:.6rem;}
.dim-letter{font-family:var(--mono);font-size:.8rem;font-weight:600;color:var(--navy);}
.dim-letter.dim-inactive{color:var(--neutral);}
.dim-bar-track{height:3px;background:var(--ice);overflow:hidden;border-radius:1px;}
.dim-bar-fill{height:100%;background:var(--navy);border-radius:1px;}
.dim-bar-fill.fill-low{background:var(--risk);}
.dim-bar-fill.fill-inactive{background:repeating-linear-gradient(90deg,var(--neutral) 0,var(--neutral) 3px,transparent 3px,transparent 6px);}
.dim-val{font-family:var(--mono);font-size:.8rem;color:var(--navy);text-align:right;font-variant-numeric:tabular-nums;font-weight:500;}
.dim-val.val-high{color:var(--navy);font-weight:500;}
.dim-val.val-inactive{color:var(--neutral);font-weight:400;}

.cta-bar{border-top:1px solid var(--divider);padding-top:2.5rem;margin-top:2rem;display:flex;gap:1rem;flex-wrap:wrap;}
.cta-link{font-family:var(--sans);font-size:.8rem;font-weight:600;letter-spacing:.04em;color:var(--navy);padding:.5rem 1rem;border:1px solid var(--divider);text-decoration:none;transition:all .2s;}
.cta-link:hover{background:var(--navy);color:var(--white);text-decoration:none;border-color:var(--navy);}

footer{border-top:1px solid var(--divider);padding:2rem 3rem;max-width:960px;margin:0 auto;}
.footer-note{font-family:var(--sans);font-size:.8rem;color:var(--caption);line-height:1.8;}
.footer-note a{color:var(--navy);}

@media(max-width:700px){
  header{padding:0 1.5rem;}
  .wrap{padding:3rem 1.5rem;}
  .score-hero{flex-direction:column;align-items:flex-start;gap:1rem;}
  .radar-section{flex-direction:column;}
  .radar-wrap{width:220px;height:220px;}
  footer{padding:2rem 1.5rem;}
}
</style>"""

NEW_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;400;500;600;700&family=Libre+Franklin:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Merriweather:wght@400;700;900&display=swap" rel="stylesheet">'

NEW_HEADER = """<header>
  <a href="/" class="logo">
    <span class="logo-mark">VERDICT</span>
    <span class="logo-divider"></span>
    <span class="logo-sub">AI Agent Trust Index</span>
  </a>
  <a href="/" class="back">← All Evaluations</a>
</header>"""

NEW_SCRIPT = """<script>
document.querySelectorAll('.dim-list').forEach(list => {
  const dims = JSON.parse(list.dataset.dims);
  dims.forEach(d => {
    const pct = d.inactive ? 100 : Math.round((d.s / d.m) * 100);
    const isLow = !d.inactive && pct < 30;
    const fillClass = d.inactive ? 'fill-inactive' : isLow ? 'fill-low' : '';
    const letterClass = d.inactive ? 'dim-inactive' : '';
    const valClass = d.inactive ? 'val-inactive' : '';
    const valText = d.inactive ? 'L1' : d.s+'/'+d.m;
    list.innerHTML += '<div class="dim-row"><span class="dim-letter '+letterClass+'">'+d.l+'</span><div class="dim-bar-track"><div class="dim-bar-fill '+fillClass+'" style="width:'+(d.inactive?'100':pct)+'%"></div></div><span class="dim-val '+valClass+'">'+valText+'</span></div>';
  });
});
</script>"""


def convert_page(content):
    # 1. Replace font link
    content = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=DM.*?" rel="stylesheet">',
        NEW_FONTS,
        content
    )

    # 2. Replace entire <style> block
    content = re.sub(
        r'<style>.*?</style>',
        NEW_CSS,
        content,
        flags=re.DOTALL
    )

    # 3. Replace header
    content = re.sub(
        r'<header>.*?</header>',
        NEW_HEADER,
        content,
        flags=re.DOTALL
    )

    # 4. Replace radar colors
    content = content.replace('fill="#c9a24a"', 'fill="#1B2A4A"')
    content = content.replace('stroke="#c9a24a"', 'stroke="#1B2A4A"')

    # 5. Replace JS (remove val-high logic)
    content = re.sub(
        r'<script>\s*document\.querySelectorAll\(\'.dim-list\'\).*?</script>',
        NEW_SCRIPT,
        content,
        flags=re.DOTALL
    )

    return content


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = convert_page(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  ✓ {filepath}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 convert_pages.py <path>")
        print("  path can be a single .html file or a directory containing platform folders")
        sys.exit(1)

    path = sys.argv[1]
    count = 0

    if os.path.isfile(path):
        process_file(path)
        count = 1
    elif os.path.isdir(path):
        for entry in sorted(os.listdir(path)):
            subdir = os.path.join(path, entry)
            index_file = os.path.join(subdir, 'index.html')
            if os.path.isdir(subdir) and os.path.isfile(index_file):
                process_file(index_file)
                count += 1
    else:
        print(f"Error: {path} not found")
        sys.exit(1)

    print(f"\nDone. {count} file(s) converted.")


if __name__ == '__main__':
    main()
