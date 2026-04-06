#!/usr/bin/env python3
"""
VERDICT: Deploy Rankings + 2 Comparison Pages
Run from ~/Desktop/verdict-index/
"""
import os

# ============================================================
# SHARED CSS (extracted for reuse)
# ============================================================

SHARED_CSS = """
:root{--white:#FFFFFF;--ice:#F5F6F8;--navy:#1B2A4A;--navy-light:#2A3D66;--heading:#1A1A2E;--body:#4A5060;--caption:#6B7280;--risk:#C4332B;--risk-bg:rgba(196,51,43,0.06);--caution:#C08520;--caution-bg:rgba(192,133,32,0.06);--safe:#2D7A4F;--safe-bg:rgba(45,122,79,0.06);--divider:#E2E5EB;--serif:'Source Serif 4',Georgia,serif;--sans:'Libre Franklin',-apple-system,sans-serif;--mono:'JetBrains Mono',monospace;--score:'Merriweather',Georgia,serif;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}body{background:var(--white);color:var(--body);font-family:var(--sans);font-weight:400;line-height:1.6;}a{color:var(--navy);text-decoration:none;}a:hover{text-decoration:underline;}header{padding:0 2.5rem;height:58px;display:flex;align-items:center;justify-content:space-between;background:var(--white);border-bottom:1px solid var(--divider);}.logo{display:flex;align-items:baseline;gap:.75rem;text-decoration:none;}.logo:hover{text-decoration:none;}.logo-mark{font-family:var(--serif);font-size:1.25rem;font-weight:700;letter-spacing:.1em;color:var(--navy);}.logo-sub{font-family:var(--mono);font-size:.6rem;letter-spacing:.15em;color:var(--caption);text-transform:uppercase;}.back{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--caption);text-decoration:none;}.back:hover{color:var(--navy);}.wrap{max-width:960px;margin:0 auto;padding:3rem 2.5rem;}.breadcrumb{font-family:var(--mono);font-size:.65rem;color:var(--caption);margin-bottom:2rem;}.breadcrumb a{color:var(--caption);}.breadcrumb a:hover{color:var(--navy);}h1{font-family:var(--serif);font-size:clamp(1.8rem,3.5vw,2.5rem);font-weight:700;line-height:1.15;color:var(--heading);margin-bottom:.5rem;}h2{font-family:var(--serif);font-size:1.2rem;font-weight:600;color:var(--heading);margin:2.5rem 0 1rem;}.subtitle{font-family:var(--sans);font-size:.9rem;color:var(--body);line-height:1.7;margin-bottom:2rem;max-width:640px;}footer{border-top:1px solid var(--divider);padding:2rem 2.5rem;max-width:960px;margin:0 auto;}.footer-note{font-family:var(--mono);font-size:.62rem;color:var(--caption);line-height:1.8;}.footer-note a{color:var(--navy);}
.tier-label{font-family:var(--score);font-weight:900;font-size:1.6rem;color:var(--navy);width:40px;text-align:center;flex-shrink:0;}
.tier-section{margin-bottom:2rem;}
.tier-header{display:flex;align-items:center;gap:1rem;padding:.75rem 0;border-bottom:2px solid var(--navy);margin-bottom:.75rem;}
.tier-name{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--caption);}
.tier-count{font-family:var(--mono);font-size:.6rem;color:var(--caption);margin-left:auto;}
.rank-row{display:grid;grid-template-columns:32px 1fr 55px;align-items:center;gap:.75rem;padding:.5rem .5rem;border-bottom:1px solid var(--divider);text-decoration:none;transition:background .15s;}
.rank-row:hover{background:var(--ice);text-decoration:none;}
.rank-num{font-family:var(--mono);font-size:.7rem;color:var(--caption);text-align:right;}
.rank-info{display:flex;flex-direction:column;gap:.1rem;}
.rank-name{font-family:var(--sans);font-size:.85rem;font-weight:500;color:var(--heading);}
.rank-cat{font-family:var(--mono);font-size:.6rem;color:var(--caption);}
.rank-score{font-family:var(--score);font-weight:900;font-size:1.1rem;color:var(--navy);text-align:right;}
.cmp-table{width:100%;border-collapse:collapse;margin:1.5rem 0;}
.cmp-table th{font-family:var(--mono);font-size:.65rem;letter-spacing:.05em;text-transform:uppercase;color:var(--caption);text-align:left;padding:.6rem .5rem;border-bottom:2px solid var(--navy);font-weight:500;}
.cmp-table th.score-col{text-align:center;}
.cmp-table td{font-family:var(--sans);font-size:.8rem;color:var(--body);padding:.5rem;border-bottom:1px solid var(--divider);vertical-align:top;}
.cmp-table td.dim-label{font-family:var(--mono);font-size:.75rem;font-weight:600;color:var(--navy);}
.cmp-table td.score-cell{text-align:center;font-family:var(--mono);font-size:.8rem;font-weight:500;}
.cmp-table td.score-cell.high{color:var(--safe);font-weight:600;}
.cmp-table td.score-cell.low{color:var(--risk);font-weight:600;}
.cmp-table td.score-cell.mid{color:var(--caution);}
.cmp-total{font-family:var(--score);font-weight:900;font-size:1.1rem;color:var(--navy);}
.insight-box{background:var(--ice);border-left:3px solid var(--navy);padding:1rem 1.25rem;margin:1.5rem 0;font-size:.85rem;line-height:1.7;}
.cta-bar{border-top:1px solid var(--divider);padding-top:2rem;margin-top:2.5rem;display:flex;gap:1.5rem;flex-wrap:wrap;}
.cta-link{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--navy);padding:.5rem 1rem;border:1px solid var(--divider);text-decoration:none;transition:all .2s;}.cta-link:hover{background:var(--navy);color:var(--white);border-color:var(--navy);text-decoration:none;}
.tag{font-family:var(--mono);font-size:.55rem;letter-spacing:.08em;text-transform:uppercase;padding:.2rem .5rem;border:1px solid;display:inline-block;margin:.1rem .2rem .1rem 0;}
.tag-safe{border-color:rgba(45,122,79,.3);color:var(--safe);background:var(--safe-bg);}
.tag-red{border-color:rgba(196,51,43,.3);color:var(--risk);background:var(--risk-bg);}
.tag-amber{border-color:rgba(192,133,32,.3);color:var(--caution);background:var(--caution-bg);}
.tag-dim{border-color:var(--divider);color:var(--caption);background:var(--ice);}
@media(max-width:700px){.rank-row{grid-template-columns:28px 1fr 45px;}.cmp-table{font-size:.7rem;}}
"""

HEADER = '<header><a href="/" class="logo"><span class="logo-mark">VERDICT</span><span class="logo-sub">AI Agent Trust Index</span></a><a href="/" class="back">&larr; All Evaluations</a></header>'
FOOTER = '<footer><div class="footer-note">VERDICT is not a certification authority. Scores are evaluations, not guarantees.<br>VERDICT by ZinovaCreation &middot; Est. 2026 &middot; Japan &middot; <a href="/">getverdict.fyi</a><br>Evaluation tooling uses Claude (Anthropic). Bias disclosures in full reports.</div></footer>'
CF = '<!-- Cloudflare Web Analytics --><script defer src=\'https://static.cloudflareinsights.com/beacon.min.js\' data-cf-beacon=\'{"token": "4dbc22ec4e18434e9bdbc01d644490c0"}\'></script>'

HEAD_COMMON = """<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;400;500;600;700&family=Libre+Franklin:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Merriweather:wght@400;700;900&display=swap" rel="stylesheet">"""

# ============================================================
# PAGE 1: /rankings/
# ============================================================

tiers = [
    ("S", "Institutional Grade", "65–85", [
        (1,"Amazon Q Business",68,"Enterprise AI Agent","Amazon (Anthropic inv.)","amazon-q-business"),
        (2,"Vertex AI Agent Builder",65,"Enterprise AI Agent","Google (Alphabet)","vertex-ai"),
    ]),
    ("A", "Enterprise Ready", "55–64", [
        (3,"Lovable",63,"AI App Builder","Lovable Labs AB · Sweden","lovable"),
        (4,"Devin",62,"AI Coding Agent","Cognition AI · $10.2B","devin"),
        (5,"Copilot Studio",61,"Enterprise AI Agent","Microsoft","copilot-studio"),
        (6,"OpenAI Assistants API",61,"Enterprise AI Agent","OpenAI","openai-assistants"),
        (7,"Agentforce",58,"Enterprise AI Agent","Salesforce","agentforce"),
        (8,"Windsurf",58,"AI Coding IDE","Cognition AI","windsurf"),
        (9,"Dust",57,"Enterprise AI Agent","Independent (Sequoia)","dust"),
        (10,"GitHub Copilot",57,"AI Coding Agent","GitHub (Microsoft)","github-copilot"),
        (11,"AutoGen",56,"Multi-Agent Framework","Microsoft Research","autogen"),
        (12,"Pipedream",56,"Workflow Automation","Workday","pipedream"),
        (13,"v0",56,"AI App Builder","Vercel · $3.25B","v0"),
        (14,"AWS Bedrock Agents",55,"Enterprise AI Agent","AWS","bedrock-agents"),
    ]),
    ("B", "Developing", "45–54", [
        (15,"Activepieces",52,"Workflow Automation","Independent (YC)","activepieces"),
        (16,"Voiceflow",52,"Conversational AI","Independent","voiceflow"),
        (17,"LangChain",49,"Agent Framework","Independent","langchain"),
        (18,"IBM watsonx Orchestrate",48,"Enterprise AI Agent","IBM","watsonx-orchestrate"),
        (19,"Replit",48,"AI Coding Agent / Cloud IDE","Independent · $1.16B","replit"),
        (20,"Zapier",48,"Workflow Automation","Independent","zapier"),
        (21,"Bolt.new",47,"AI App Builder","StackBlitz · $700M","bolt-new"),
        (22,"Cursor",47,"AI Coding IDE","Anysphere · $29.3B","cursor"),
        (23,"Haystack",47,"Agent Framework","Independent (deepset)","haystack"),
        (24,"Composio",46,"Agent Framework","Independent (YC)","composio"),
        (25,"Dify",46,"Visual Agent Builder","Independent","dify"),
        (26,"LangGraph",46,"Agent Orchestration","LangChain Inc.","langgraph"),
        (27,"Make.com",46,"Workflow Automation","Independent","make"),
        (28,"Semantic Kernel",46,"Agent Framework","Microsoft Research","semantic-kernel"),
        (29,"Botpress",45,"Visual Agent Builder","Independent","botpress"),
        (30,"CrewAI",44,"Multi-Agent Framework","Independent","crewai"),
    ]),
    ("C", "Foundational", "35–44", [
        (31,"OpenHands",43,"AI Coding Agent","Independent","openhands"),
        (32,"Relevance AI",43,"Agent Framework","Independent","relevance-ai"),
        (33,"Superagent",42,"Agent Framework","Independent (YC)","superagent"),
        (34,"LlamaIndex",41,"Agent Framework","Independent","llamaindex"),
        (35,"AG2",40,"Multi-Agent Framework","Community (AutoGen fork)","ag2"),
        (36,"Rivet",39,"Visual Agent Builder","Ironclad","rivet"),
        (37,"Phidata",38,"Agent Framework","Independent","phidata"),
        (38,"Letta",37,"Agent Framework","Independent","letta"),
        (39,"AutoGPT",36,"Autonomous Agent","Independent · UK","autogpt"),
        (40,"Coze",35,"Visual Agent Builder","ByteDance","coze"),
        (41,"Manus AI",35,"Browser Agent","Meta-acquired","manus-ai"),
        (42,"n8n",35,"Workflow Automation","Independent","n8n"),
        (43,"Wordware",35,"Agent Framework","Independent (YC)","wordware"),
    ]),
    ("D", "Early / At Risk", "21–34", [
        (44,"Langroid",34,"Agent Framework","Independent (CMU)","langroid"),
        (45,"CAMEL-AI",33,"Multi-Agent Research","CAMEL-AI.org · UK","camel-ai"),
        (46,"Flowise",33,"Visual Agent Builder","Workday","flowise"),
        (47,"Langflow",30,"Visual Agent Builder","IBM (Acquired)","langflow"),
        (48,"BabyAGI",24,"Autonomous Agent","Experimental","babyagi"),
        (49,"MetaGPT",23,"Multi-Agent Framework","DeepWisdom · China","metagpt"),
        (50,"SuperAGI",21,"Agent Management","TransformErr Inc.","superagi"),
    ]),
]

tier_rows = ""
for letter, name, score_range, platforms in tiers:
    rows = ""
    for rank, pname, score, cat, owner, slug in platforms:
        rows += f'    <a class="rank-row" href="/{slug}/"><span class="rank-num">#{rank}</span><div class="rank-info"><span class="rank-name">{pname}</span><span class="rank-cat">{cat} · {owner}</span></div><span class="rank-score">{score}</span></a>\n'
    tier_rows += f"""  <div class="tier-section">
    <div class="tier-header"><span class="tier-label">{letter}</span><span class="tier-name">{name} · {score_range}</span><span class="tier-count">{len(platforms)} platforms</span></div>
{rows}  </div>
"""

rankings_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
<title>AI Agent Platform Rankings — VERDICT Trust Index</title>
<meta name="description" content="50 AI agent platforms ranked by security, privacy, and compliance. Tier-based evaluation from S (Institutional Grade) to D (At Risk). Independent evaluation, no vendor sponsorships.">
<meta property="og:title" content="AI Agent Platform Rankings — VERDICT">
<meta property="og:description" content="50 AI agent platforms ranked by security, privacy, and compliance. S through D tiers.">
<meta property="og:url" content="https://getverdict.fyi/rankings/">
<link rel="canonical" href="https://getverdict.fyi/rankings/">
<style>{SHARED_CSS}</style>
</head>
<body>
{HEADER}
<div class="wrap">
  <div class="breadcrumb"><a href="/">VERDICT</a> &rsaquo; Rankings</div>
  <h1>AI agent platform rankings</h1>
  <div class="subtitle">50 platforms evaluated on security, privacy, and compliance using public data only. Scored out of 85 (Layer 0, Framework v0.3.1). Tiers reflect meaningful capability boundaries, not arbitrary groupings. Updated April 2026.</div>
{tier_rows}
  <div class="insight-box">Tied scores are sorted alphabetically. Scores reflect public documentation as of the evaluation date. Platforms may improve or decline as documentation and security posture evolve. Full methodology at <a href="/methodology/">getverdict.fyi/methodology</a>.</div>
  <div class="cta-bar"><a href="/" class="cta-link">View All Evaluations</a><a href="/compare/coding-agents/" class="cta-link">Coding Agents Compared</a><a href="/compare/ai-app-builders/" class="cta-link">AI App Builders Compared</a><a href="/methodology/" class="cta-link">Methodology</a></div>
</div>
{FOOTER}
{CF}
</body></html>"""

os.makedirs("rankings", exist_ok=True)
with open("rankings/index.html", "w") as f:
    f.write(rankings_html)
print("  ✓ rankings/index.html")

# ============================================================
# PAGE 2: /compare/coding-agents/
# ============================================================

coding_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
<title>AI Coding Agent Security Comparison — Devin vs Cursor vs Windsurf vs Copilot — VERDICT</title>
<meta name="description" content="Independent security comparison of 6 AI coding agents: Devin (62/85), Windsurf (58), GitHub Copilot (57), Replit (48), Cursor (47), OpenHands (43). Dimension-by-dimension analysis.">
<meta property="og:title" content="AI Coding Agent Security Comparison — VERDICT">
<meta property="og:url" content="https://getverdict.fyi/compare/coding-agents/">
<link rel="canonical" href="https://getverdict.fyi/compare/coding-agents/">
<style>{SHARED_CSS}</style>
</head>
<body>
{HEADER}
<div class="wrap">
  <div class="breadcrumb"><a href="/">VERDICT</a> &rsaquo; <a href="/rankings/">Rankings</a> &rsaquo; Coding Agents</div>
  <h1>AI coding agents compared</h1>
  <div class="subtitle">Six AI coding agents evaluated on security, privacy, and compliance. All scores are Layer 0 (public documentation only), Framework v0.3.1. Updated April 2026.</div>

  <table class="cmp-table">
    <thead><tr>
      <th>Dimension</th><th>Max</th>
      <th class="score-col"><a href="/devin/">Devin</a></th>
      <th class="score-col"><a href="/windsurf/">Windsurf</a></th>
      <th class="score-col"><a href="/github-copilot/">Copilot</a></th>
      <th class="score-col"><a href="/replit/">Replit</a></th>
      <th class="score-col"><a href="/cursor/">Cursor</a></th>
      <th class="score-col"><a href="/openhands/">OpenHands</a></th>
    </tr></thead>
    <tbody>
      <tr><td class="dim-label">V</td><td>20</td><td class="score-cell">11</td><td class="score-cell">10</td><td class="score-cell">12</td><td class="score-cell">10</td><td class="score-cell">10</td><td class="score-cell high">13</td></tr>
      <tr><td class="dim-label">R</td><td>20</td><td class="score-cell high">17</td><td class="score-cell">14</td><td class="score-cell high">17</td><td class="score-cell">14</td><td class="score-cell low">8</td><td class="score-cell">12</td></tr>
      <tr><td class="dim-label">D</td><td>15</td><td class="score-cell high">12</td><td class="score-cell high">12</td><td class="score-cell">7</td><td class="score-cell">6</td><td class="score-cell high">11</td><td class="score-cell low">1</td></tr>
      <tr><td class="dim-label">I</td><td>10</td><td class="score-cell high">7</td><td class="score-cell high">7</td><td class="score-cell high">7</td><td class="score-cell">5</td><td class="score-cell high">7</td><td class="score-cell">6</td></tr>
      <tr><td class="dim-label">C</td><td>10</td><td class="score-cell high">7</td><td class="score-cell">6</td><td class="score-cell">5</td><td class="score-cell">5</td><td class="score-cell">5</td><td class="score-cell">4</td></tr>
      <tr><td class="dim-label">T</td><td>10</td><td class="score-cell high">8</td><td class="score-cell high">9</td><td class="score-cell high">9</td><td class="score-cell high">8</td><td class="score-cell">6</td><td class="score-cell high">7</td></tr>
      <tr style="border-top:2px solid var(--navy)"><td class="dim-label">Total</td><td>85</td>
        <td class="score-cell"><span class="cmp-total">62</span></td>
        <td class="score-cell"><span class="cmp-total">58</span></td>
        <td class="score-cell"><span class="cmp-total">57</span></td>
        <td class="score-cell"><span class="cmp-total">48</span></td>
        <td class="score-cell"><span class="cmp-total">47</span></td>
        <td class="score-cell"><span class="cmp-total">43</span></td>
      </tr>
    </tbody>
  </table>

  <h2>Key differentiators</h2>
  <table class="cmp-table">
    <thead><tr><th>Feature</th><th>Devin</th><th>Windsurf</th><th>Copilot</th><th>Replit</th><th>Cursor</th><th>OpenHands</th></tr></thead>
    <tbody>
      <tr><td class="dim-label">Architecture</td><td>Cloud SaaS</td><td>Desktop IDE</td><td>IDE Extension</td><td>Cloud IDE</td><td>Desktop IDE</td><td>OSS Self-Host</td></tr>
      <tr><td class="dim-label">SOC 2 Type II</td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-safe">Yes (0 exc.)</span></td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-dim">No</span></td></tr>
      <tr><td class="dim-label">FedRAMP</td><td><span class="tag tag-safe">Aligned</span></td><td><span class="tag tag-safe">High</span></td><td><span class="tag tag-safe">Via Azure</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td></tr>
      <tr><td class="dim-label">Training default</td><td><span class="tag tag-safe">No (opt-in)</span></td><td><span class="tag tag-safe">ZDR default</span></td><td><span class="tag tag-red">Opt-in (Apr 26)</span></td><td><span class="tag tag-amber">Public=yes</span></td><td><span class="tag tag-amber">Privacy Mode</span></td><td><span class="tag tag-red">D:1/15</span></td></tr>
      <tr><td class="dim-label">Self-hosted</td><td><span class="tag tag-safe">VPC</span></td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-safe">Yes (OSS)</span></td></tr>
      <tr><td class="dim-label">CVEs (12mo)</td><td><span class="tag tag-safe">0</span></td><td><span class="tag tag-safe">0</span></td><td><span class="tag tag-safe">0</span></td><td><span class="tag tag-safe">0</span></td><td><span class="tag tag-red">3 (MCP)</span></td><td><span class="tag tag-amber">1</span></td></tr>
      <tr><td class="dim-label">IP Indemnity</td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-safe">Enterprise</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td><td><span class="tag tag-dim">No</span></td></tr>
      <tr><td class="dim-label">Price</td><td>$500/mo</td><td>$15-60/mo</td><td>$10-39/mo</td><td>$20-60/mo</td><td>$20/mo</td><td>Free (OSS)</td></tr>
    </tbody>
  </table>

  <div class="insight-box">The 15-point gap between Devin (62) and Cursor (47) is driven primarily by R dimension (17 vs 8) and C dimension (7 vs 5). Cursor's three MCP CVEs represent a structural trust model pattern. Windsurf outscores Cursor by 11 points despite both being VS Code forks — FedRAMP High accreditation, HIPAA readiness, and default zero-data-retention account for the difference.</div>

  <div class="cta-bar"><a href="/rankings/" class="cta-link">Full Rankings (50 Platforms)</a><a href="/compare/ai-app-builders/" class="cta-link">AI App Builders Compared</a><a href="/methodology/" class="cta-link">Methodology</a></div>
</div>
{FOOTER}
{CF}
</body></html>"""

os.makedirs("compare/coding-agents", exist_ok=True)
with open("compare/coding-agents/index.html", "w") as f:
    f.write(coding_html)
print("  ✓ compare/coding-agents/index.html")

# ============================================================
# PAGE 3: /compare/ai-app-builders/
# ============================================================

builders_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
{HEAD_COMMON}
<title>AI App Builder Security Comparison — Lovable vs v0 vs Bolt.new — VERDICT</title>
<meta name="description" content="Independent security comparison of 3 AI app builders: Lovable (63/85), v0 (56), Bolt.new (47). Data conduct, containment, and certification analysis.">
<meta property="og:title" content="AI App Builder Security Comparison — VERDICT">
<meta property="og:url" content="https://getverdict.fyi/compare/ai-app-builders/">
<link rel="canonical" href="https://getverdict.fyi/compare/ai-app-builders/">
<style>{SHARED_CSS}</style>
</head>
<body>
{HEADER}
<div class="wrap">
  <div class="breadcrumb"><a href="/">VERDICT</a> &rsaquo; <a href="/rankings/">Rankings</a> &rsaquo; AI App Builders</div>
  <h1>AI app builders compared</h1>
  <div class="subtitle">Three AI app builders evaluated on security, privacy, and compliance. All generate full-stack web applications from natural language prompts. Layer 0, Framework v0.3.1. Updated April 2026.</div>

  <table class="cmp-table">
    <thead><tr>
      <th>Dimension</th><th>Max</th>
      <th class="score-col"><a href="/lovable/">Lovable</a></th>
      <th class="score-col"><a href="/v0/">v0</a></th>
      <th class="score-col"><a href="/bolt-new/">Bolt.new</a></th>
    </tr></thead>
    <tbody>
      <tr><td class="dim-label">V</td><td>20</td><td class="score-cell">10</td><td class="score-cell high">13</td><td class="score-cell">12</td></tr>
      <tr><td class="dim-label">R</td><td>20</td><td class="score-cell high">17</td><td class="score-cell high">17</td><td class="score-cell high">17</td></tr>
      <tr><td class="dim-label">D</td><td>15</td><td class="score-cell high">13</td><td class="score-cell">8</td><td class="score-cell low">4</td></tr>
      <tr><td class="dim-label">I</td><td>10</td><td class="score-cell high">8</td><td class="score-cell">5</td><td class="score-cell low">3</td></tr>
      <tr><td class="dim-label">C</td><td>10</td><td class="score-cell high">7</td><td class="score-cell">6</td><td class="score-cell high">7</td></tr>
      <tr><td class="dim-label">T</td><td>10</td><td class="score-cell high">8</td><td class="score-cell high">7</td><td class="score-cell">4</td></tr>
      <tr style="border-top:2px solid var(--navy)"><td class="dim-label">Total</td><td>85</td>
        <td class="score-cell"><span class="cmp-total">63</span></td>
        <td class="score-cell"><span class="cmp-total">56</span></td>
        <td class="score-cell"><span class="cmp-total">47</span></td>
      </tr>
    </tbody>
  </table>

  <h2>Key differentiators</h2>
  <table class="cmp-table">
    <thead><tr><th>Feature</th><th>Lovable</th><th>v0</th><th>Bolt.new</th></tr></thead>
    <tbody>
      <tr><td class="dim-label">Origin</td><td>Sweden (EU)</td><td>USA</td><td>USA</td></tr>
      <tr><td class="dim-label">SOC 2 Type II</td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-safe">Yes (v0 in scope)</span></td><td><span class="tag tag-dim">No</span></td></tr>
      <tr><td class="dim-label">ISO 27001</td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-safe">Yes</span></td><td><span class="tag tag-dim">No</span></td></tr>
      <tr><td class="dim-label">GDPR / DPA</td><td><span class="tag tag-safe">EU native + DPO</span></td><td><span class="tag tag-safe">DPA + DPF</span></td><td><span class="tag tag-dim">No DPA</span></td></tr>
      <tr><td class="dim-label">Training policy</td><td><span class="tag tag-safe">No (explicit)</span></td><td><span class="tag tag-amber">Tiered opt-in/out</span></td><td><span class="tag tag-red">Not stated</span></td></tr>
      <tr><td class="dim-label">Security scanners</td><td><span class="tag tag-safe">4 automated</span></td><td><span class="tag tag-dim">None</span></td><td><span class="tag tag-dim">None</span></td></tr>
      <tr><td class="dim-label">Execution model</td><td>Cloud</td><td>Vercel Sandbox (VM)</td><td>WebContainers (browser)</td></tr>
      <tr><td class="dim-label">Open source</td><td><span class="tag tag-dim">Closed (gpt-engineer origin)</span></td><td><span class="tag tag-dim">Closed</span></td><td><span class="tag tag-safe">OSS core</span></td></tr>
      <tr><td class="dim-label">Valuation</td><td>$6.6B</td><td>$3.25B (Vercel)</td><td>$700M</td></tr>
    </tbody>
  </table>

  <div class="insight-box">All three share R: 17/20 (zero CVEs). The 16-point gap between Lovable (63) and Bolt.new (47) comes from D (+9), I (+5), and T (+4). Lovable's EU jurisdiction, explicit no-training policy, and four automated security scanners are the primary differentiators. Bolt.new's WebContainers provide the strongest architectural containment (C: 7/10, tied with Lovable) but lack formal documentation and certification.</div>

  <div class="cta-bar"><a href="/rankings/" class="cta-link">Full Rankings (50 Platforms)</a><a href="/compare/coding-agents/" class="cta-link">Coding Agents Compared</a><a href="/methodology/" class="cta-link">Methodology</a></div>
</div>
{FOOTER}
{CF}
</body></html>"""

os.makedirs("compare/ai-app-builders", exist_ok=True)
with open("compare/ai-app-builders/index.html", "w") as f:
    f.write(builders_html)
print("  ✓ compare/ai-app-builders/index.html")

# ============================================================
# STEP 2: UPDATE SITEMAP
# ============================================================
new_urls = """  <url><loc>https://getverdict.fyi/rankings/</loc><lastmod>2026-04-06</lastmod><priority>0.9</priority></url>
  <url><loc>https://getverdict.fyi/compare/coding-agents/</loc><lastmod>2026-04-06</lastmod><priority>0.9</priority></url>
  <url><loc>https://getverdict.fyi/compare/ai-app-builders/</loc><lastmod>2026-04-06</lastmod><priority>0.9</priority></url>
"""
with open('sitemap.xml','r') as f: s=f.read()
s=s.replace('</urlset>',new_urls+'</urlset>')
with open('sitemap.xml','w') as f: f.write(s)
print("  ✓ sitemap.xml: 3 URLs added (rankings, 2 comparisons)")

print("\n✓ Done. git add . && git commit && git push")
