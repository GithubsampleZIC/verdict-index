#!/usr/bin/env python3
"""Fix rank numbers in individual platform pages after alphabetical tiebreak reorder."""
import os

fixes = {
    "dify/index.html": ("Rank #12", "Rank #11"),
    "make/index.html": ("Rank #11", "Rank #12"),
    "coze/index.html": ("Rank #18", "Rank #17"),
    "n8n/index.html": ("Rank #17", "Rank #18"),
}

for path, (old, new) in fixes.items():
    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new)
            with open(path, 'w') as f:
                f.write(content)
            print(f"  ✓ {path}: {old} → {new}")
        else:
            print(f"  - {path}: '{old}' not found (may already be correct)")
    else:
        print(f"  ✗ {path}: file not found")

print("\nDone.")
