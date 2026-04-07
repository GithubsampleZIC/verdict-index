#!/usr/bin/env python3
"""
VERDICT fix_manus_ai.py
========================
Fixes 3 factual errors in the Manus AI card in index.html:

1. platform-owner: "Butterfly Effect (Meta) · Singapore"
                -> "Butterfly Effect Pte. Ltd. · Singapore"

2. key-finding:   "Meta-acquired ($2B+). Sandbox VMs..."
                -> "Butterfly Effect Pte. Ltd. ($500M+ funding). Sandbox VMs..."

3. incident-tag:  "Meta · $2B+ · Zero CVEs"
                -> "$500M+ · Zero CVEs"

Reason: Butterfly Effect Pte. Ltd. (Singapore-registered) is an
independent company and has NOT been acquired by Meta or any other
company. The previous text was a factual error.

Usage (from ~/Desktop/verdict-index/):
    python3 fix_manus_ai.py

Creates:
    index.html (modified in place)
    index.html.backup (safety backup of original)
"""

import shutil
import sys
from pathlib import Path

INDEX = Path("index.html")
BACKUP = Path("index.html.backup")

# Exact string replacements — must match current file precisely
REPLACEMENTS = [
    (
        '<div class="platform-owner">Butterfly Effect (Meta) · Singapore</div>',
        '<div class="platform-owner">Butterfly Effect Pte. Ltd. · Singapore</div>',
    ),
    (
        '<div class="key-finding">Meta-acquired ($2B+). Sandbox VMs. Zero CVEs. Browser Operator: full browser control (Mindgard). No certifications.</div>',
        '<div class="key-finding">Butterfly Effect Pte. Ltd. ($500M+ funding). Sandbox VMs. Zero CVEs. Browser Operator: full browser control (Mindgard). No certifications.</div>',
    ),
    (
        '<span class="tag tag-dim">Meta · $2B+ · Zero CVEs</span>',
        '<span class="tag tag-dim">$500M+ · Zero CVEs</span>',
    ),
]


def main():
    if not INDEX.exists():
        print(f"ERROR: {INDEX} not found in current directory.")
        print("Please run this script from ~/Desktop/verdict-index/")
        sys.exit(1)

    # Read
    with open(INDEX, "r", encoding="utf-8") as f:
        content = f.read()

    # Backup
    shutil.copy(INDEX, BACKUP)
    print(f"[1/3] Backup created: {BACKUP}")

    # Verify all source strings exist before modifying
    print("\n[2/3] Verifying source strings...")
    missing = []
    for old, new in REPLACEMENTS:
        if old not in content:
            missing.append(old[:60] + "...")

    if missing:
        print("ERROR: The following source strings were not found:")
        for m in missing:
            print(f"  - {m}")
        print("\nThe file may have already been modified, or the structure has changed.")
        print("Backup file preserved at:", BACKUP)
        sys.exit(2)

    print("      All 3 source strings verified.")

    # Apply replacements
    print("\n[3/3] Applying fixes...")
    for i, (old, new) in enumerate(REPLACEMENTS, 1):
        content = content.replace(old, new)
        # Show concise diff
        old_short = old.replace('<div class="platform-owner">', "").replace('<div class="key-finding">', "").replace('<span class="tag tag-dim">', "")[:70]
        new_short = new.replace('<div class="platform-owner">', "").replace('<div class="key-finding">', "").replace('<span class="tag tag-dim">', "")[:70]
        print(f"      Fix {i}: {old_short.split('<')[0]}")
        print(f"           -> {new_short.split('<')[0]}")

    # Write
    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n[DONE] {INDEX} updated.")
    print(f"       Backup: {BACKUP}")
    print(f"\nNext: review with 'git diff index.html', then commit.")


if __name__ == "__main__":
    main()
