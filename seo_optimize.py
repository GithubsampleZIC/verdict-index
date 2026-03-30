#!/usr/bin/env python3
"""
VERDICT SEO Optimization Script
Updates meta descriptions and titles for all 20 individual platform pages.
Run from ~/Desktop/verdict-index/
"""
import os
import re

# Optimized meta data for each platform
# Format: (dir_name, title, description)
pages = [
    ("vertex-ai",
     "Vertex AI Agent Builder Security Review — VERDICT Score: 65/85",
     "Independent security and privacy evaluation of Google Vertex AI Agent Builder. Score: 65/85 — highest in the VERDICT index. Container isolation, two cross-tenant incidents disclosed. Framework v0.3.1."),
    ("copilot-studio",
     "Microsoft Copilot Studio Security Review — VERDICT Score: 61/85",
     "Independent security evaluation of Microsoft Copilot Studio. Score: 61/85. EchoLeak CVE-2025-32711 (CVSS 9.3) — first zero-click prompt injection on a production AI system. Framework v0.3.1."),
    ("openai-assistants",
     "OpenAI Assistants API Security Review — VERDICT Score: 61/85",
     "Independent security evaluation of OpenAI Assistants API. Score: 61/85. Zero CVEs but used as C2 channel (SesameOp). Deprecation August 2026. Framework v0.3.1."),
    ("agentforce",
     "Salesforce Agentforce Security Review — VERDICT Score: 58/85",
     "Independent security evaluation of Salesforce Agentforce. Score: 58/85. ForcedLeak vulnerability (CVSS 9.4), 42-day patch window. Strong compliance documentation. Framework v0.3.1."),
    ("autogen",
     "AutoGen Security Review — VERDICT Score: 56/85",
     "Independent security evaluation of Microsoft AutoGen. Score: 56/85. Zero public CVEs, MSRC formal coverage since December 2025. Multi-agent orchestration framework. Framework v0.3.1."),
    ("pipedream",
     "Pipedream Security Review — VERDICT Score: 56/85",
     "Independent security evaluation of Pipedream. Score: 56/85. VM-isolated sandbox with zero public CVEs — strongest containment in the VERDICT index. Acquired by Workday. Framework v0.3.1."),
    ("bedrock-agents",
     "AWS Bedrock Agents Security Review — VERDICT Score: 55/85",
     "Independent security evaluation of AWS Bedrock Agents. Score: 55/85. DNS tunneling path classified as intended functionality. Strong compliance infrastructure. Framework v0.3.1."),
    ("activepieces",
     "Activepieces Security Review — VERDICT Score: 52/85",
     "Independent security evaluation of Activepieces. Score: 52/85. Only HIPAA-compliant platform in the index. Germany-hosted cloud, zero critical CVEs. Y Combinator backed. Framework v0.3.1."),
    ("langchain",
     "LangChain Security Review — VERDICT Score: 49/85",
     "Independent security evaluation of LangChain. Score: 49/85. LangGrinch CVE-2025-68664 (CVSS 9.3). SOC 2 Type II certified, $1.25B valuation. LiteLLM dependency exposure. Framework v0.3.1."),
    ("zapier",
     "Zapier Security Review — VERDICT Score: 48/85",
     "Independent security evaluation of Zapier. Score: 48/85. Two supply chain incidents in 2025 (npm SDK, repo breach) but strongest incident disclosure in the index. SOC 2 certified. Framework v0.3.1."),
    ("dify",
     "Dify Security Review — VERDICT Score: 46/85",
     "Independent security evaluation of Dify. Score: 46/85. React2Shell CVE-2025-55182 caused cryptominer infections. Strong transparency with 4 certifications. Structural SSRF issue persists. Framework v0.3.1."),
    ("make",
     "Make.com Security Review — VERDICT Score: 46/85",
     "Independent security evaluation of Make.com. Score: 46/85. Zero public CVEs under non-disclosure policy. ISO 27001 and SOC 2 certified. AI training use of data unconfirmed. Framework v0.3.1."),
    ("semantic-kernel",
     "Semantic Kernel Security Review — VERDICT Score: 46/85",
     "Independent security evaluation of Microsoft Semantic Kernel. Score: 46/85. No documented sandbox — plugins execute in-process. Microsoft Research project with MSRC coverage. Framework v0.3.1."),
    ("botpress",
     "Botpress Security Review — VERDICT Score: 45/85",
     "Independent security evaluation of Botpress. Score: 45/85. No documented sandbox for plugin execution. SOC 2 certified. Open-source chatbot and agent framework. Framework v0.3.1."),
    ("crewai",
     "CrewAI Security Review — VERDICT Score: 44/85",
     "Independent security evaluation of CrewAI. Score: 44/85. Uncrew vulnerability (CVSS 9.2) patched in 5 hours — fastest response in index. LiteLLM direct dependency. Andrew Ng backed. Framework v0.3.1."),
    ("llamaindex",
     "LlamaIndex Security Review — VERDICT Score: 41/85",
     "Independent security evaluation of LlamaIndex. Score: 41/85. RAG and agent framework. Limited public security documentation. Norwest Venture Partners backed. Framework v0.3.1."),
    ("coze",
     "Coze Security Review — VERDICT Score: 35/85",
     "Independent security evaluation of Coze (ByteDance). Score: 35/85. Terms of Service waive all confidentiality obligations. Parent company subject to China National Intelligence Law. Framework v0.3.1."),
    ("n8n",
     "n8n Security Review — VERDICT Score: 35/85",
     "Independent security evaluation of n8n. Score: 35/85. CISA KEV listed (CVE-2025-68613, CVSS 9.9). 12+ CVEs in trailing 12 months. Structural sandbox bypass pattern across 5+ CVEs. Framework v0.3.1."),
    ("flowise",
     "Flowise Security Review — VERDICT Score: 33/85",
     "Independent security evaluation of Flowise. Score: 33/85. Six CVEs in March 2026 cluster including two CVSS 9.8. Authentication not enforced by default. Acquired by Workday. Framework v0.3.1."),
    ("langflow",
     "Langflow Security Review — VERDICT Score: 30/85",
     "Independent security evaluation of Langflow. Score: 30/85 — lowest in the VERDICT index. CISA KEV listed (CVE-2025-3248, CVSS 9.8). Flodrix botnet exploitation. IBM acquired. Framework v0.3.1."),
]

updated = 0
skipped = 0

for dirname, new_title, new_desc in pages:
    filepath = os.path.join(dirname, "index.html")
    if not os.path.exists(filepath):
        print(f"  ✗ {filepath}: not found")
        skipped += 1
        continue

    with open(filepath, 'r') as f:
        content = f.read()

    original = content

    # Update <title>
    content = re.sub(
        r'<title>[^<]+</title>',
        f'<title>{new_title}</title>',
        content, count=1
    )

    # Update meta description
    content = re.sub(
        r'<meta name="description" content="[^"]+">',
        f'<meta name="description" content="{new_desc}">',
        content, count=1
    )

    # Update og:title
    content = re.sub(
        r'<meta property="og:title" content="[^"]+">',
        f'<meta property="og:title" content="{new_title}">',
        content, count=1
    )

    # Update og:description
    content = re.sub(
        r'<meta property="og:description" content="[^"]+">',
        f'<meta property="og:description" content="{new_desc}">',
        content, count=1
    )

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  ✓ {filepath}: updated")
        updated += 1
    else:
        print(f"  - {filepath}: no changes needed")

print(f"\nDone. {updated} updated, {skipped} skipped.")
