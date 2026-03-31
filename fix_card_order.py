#!/usr/bin/env python3
"""
Fix card ordering in index.html — sort all eval-cards by score descending, then alphabetical for ties.
Run from ~/Desktop/verdict-index/
"""
import re

with open('index.html', 'r') as f:
    html = f.read()

# Find the section containing all eval cards
# Cards are between comment markers like <!-- Platform Score -->
# Each card starts with \n    <!-- and ends with </a>\n
# Find all card blocks

# Pattern: from "    <!-- XXXXX NNN -->" to the next "    <!-- " or end of cards section
card_pattern = re.compile(
    r'(\n    <!-- (.+?) (\d+) -->\n    <a class="eval-card".*?</a>)',
    re.DOTALL
)

matches = list(card_pattern.finditer(html))
print(f"Found {len(matches)} cards")

if len(matches) == 0:
    print("ERROR: No cards found!")
    exit(1)

# Extract cards with their metadata
cards = []
for m in matches:
    full_html = m.group(1)
    name = m.group(2)
    score = int(m.group(3))
    cards.append({
        'html': full_html,
        'name': name,
        'score': score,
        'start': m.start(),
        'end': m.end()
    })
    print(f"  Found: {name} ({score}/85)")

# Sort: descending by score, then alphabetical by name for ties
cards.sort(key=lambda c: (-c['score'], c['name']))

print(f"\nSorted order:")
for i, c in enumerate(cards):
    print(f"  #{i+1}: {c['name']} ({c['score']}/85)")

# Replace the card section
# Find the region from the first card to the last card
first_start = matches[0].start()
last_end = matches[-1].end()

# Build the new card section
new_cards_html = ''.join(c['html'] for c in cards)

# Replace
html = html[:first_start] + new_cards_html + html[last_end:]

with open('index.html', 'w') as f:
    f.write(html)

print(f"\n✓ All {len(cards)} cards sorted and saved to index.html")
print("Ready to: git add . && git commit && git push")
