#!/usr/bin/env python3
import re

filepath = '/sessions/affectionate-cool-johnson/mnt/Stitch_Claude_Co-work/stitch-website-v2/journal.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: X-Pac thumbnail (line 1073) - change from Unsplash to local image
# Find the X-Pac card and update its thumbnail
xpac_pattern = r'(<article class="acard fade-up" data-cat="engineering"[^>]*>)\s*<div class="acard-thumb">\s*<img src="https://images\.unsplash\.com/[^"]*" alt="[^"]*"'

xpac_replacement = r'\1\n          <div class="acard-thumb">\n            <img src="images/journal/materials-dsc01318.jpg" alt="Cordura fabric close-up"'

content = re.sub(xpac_pattern, xpac_replacement, content, count=1)

# Fix 2: Revert the FOB article thumbnail back to Unsplash
# The FOB article should keep its Unsplash (about shipping terms, so port image makes sense)
fob_pattern = r'(<article class="acard fade-up" data-cat="industry" data-page="1">)\s*<div class="acard-thumb">\s*<img src="images/journal/materials-dsc01318\.jpg" alt="Shipping containers at port"'

fob_replacement = r'\1\n          <div class="acard-thumb">\n            <img src="https://images.unsplash.com/photo-1537996051257-7f927591b74b?w=800&h=450&fit=crop&auto=format&q=80" alt="Shipping containers at port"'

content = re.sub(fob_pattern, fob_replacement, content, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Fixed journal.html thumbnails:")
print("  - X-Pac thumbnail updated to materials-dsc01318.jpg")
print("  - FOB article thumbnail reverted to Unsplash (shipping terms context)")
