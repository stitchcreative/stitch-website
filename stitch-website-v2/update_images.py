#!/usr/bin/env python3
import os
import re
import sys

# Image assignment mapping
IMAGE_ASSIGNMENTS = {
    # Factory & Supply Chain articles
    'journal-best-bag-factories.html': ('images/journal/factory-der03080.jpg', 'Factory floor with production'),
    'journal-evaluate-factory.html': ('images/journal/factory-der03317.jpg', 'Quality control review'),
    'journal-factory-relationship.html': ('images/journal/factory-der02530.jpg', 'Sam walking through factory'),
    'journal-meeting-supplier.html': ('images/journal/factory-der02834.jpg', 'Sewing line workers'),
    'journal-lead-times.html': ('images/journal/factory-der03237.jpg', 'Factory production floor'),
    'journal-supplier-certifications.html': ('images/journal/factory-bluesign-certification-e1684848133495.jpg', 'Bluesign certification'),
    'journal-supplier-code-of-conduct.html': ('images/journal/factory-img05210.jpg', 'Factory production'),
    'journal-qc-inspection.html': ('images/journal/factory-der03235.jpg', 'Sewing machine and hands'),
    'journal-china-vietnam-indonesia.html': ('images/journal/factory-der02713.jpg', 'Factory floor'),
    'journal-bluesign.html': ('images/journal/factory-textile-mill.jpg', 'Textile mill'),
    'journal-moq-negotiation.html': ('images/journal/factory-der04010.jpg', 'Factory team'),
    'journal-payment-terms.html': ('images/journal/factory-der03123.jpg', 'Factory floor'),

    # Materials & Construction articles
    'journal-xpac.html': ('images/journal/materials-dsc01318.jpg', 'Cordura fabric close-up'),
    'journal-ykk-sbs-riri.html': ('images/journal/materials-dsc01459.jpg', 'YKK zipper detail'),
    'journal-ykk-worth-4x.html': ('images/journal/materials-dsc01459.jpg', 'YKK zipper detail'),
    'journal-harness-system.html': ('images/journal/materials-bts1.jpg', 'Behind-the-scenes production'),
    'journal-pattern-pieces.html': ('images/journal/materials-bts2.jpg', 'Pattern pieces and production'),
    'journal-tech-packs.html': ('images/journal/materials-dsc07995.jpg', 'Water beading on fabric'),

    # Design & Strategy articles
    'journal-how-to-design-bag.html': ('images/journal/materials-reikasho-4944.jpg', 'Reika bag detail'),
    'journal-18-month-development.html': ('images/journal/factory-der02108.jpg', 'Factory development'),
    'journal-2026-trends.html': ('images/journal/materials-custom_resized_5a587124-97b6-4307-897a-ad117aee56e3.jpg', 'Product detail'),

    # Better terms article (added)
    'journal-better-terms.html': ('images/journal/factory-img_9327-2.jpg', 'Factory product inspection'),

    # Articles that KEEP Unsplash (NOT updated)
    # - journal-fob-exw-cif-ddp.html (keep Unsplash)
    # - journal-import-duties.html (keep Unsplash)
    # - journal-vietnam-gsp.html (keep Unsplash)
}

def update_article_image(filepath):
    """Update hero image in article HTML file"""
    filename = os.path.basename(filepath)

    if filename not in IMAGE_ASSIGNMENTS:
        return False, f"No image assignment for {filename}"

    new_image_path, alt_text = IMAGE_ASSIGNMENTS[filename]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Error reading {filename}: {e}"

    # Look for Unsplash image URLs in various contexts
    # Common patterns: src="https://images.unsplash.com/..." or data-src, or in picture/img tags
    unsplash_pattern = r'(src|data-src)=["\']https://images\.unsplash\.com/[^"\']*["\']'

    if not re.search(unsplash_pattern, content):
        return False, f"No Unsplash image found in {filename}"

    # Replace the Unsplash URL with local image path
    # We need to be careful to replace in the first occurrence (hero image)
    updated_content = re.sub(
        unsplash_pattern,
        f'src="{new_image_path}"',
        content,
        count=1
    )

    # Also update alt text - look for alt attribute near the image
    # This is a bit tricky as alt text might be in a different tag
    alt_pattern = r'alt=["\'][^"\']*["\']'

    # Find the position of our newly updated src
    src_pos = updated_content.find(f'src="{new_image_path}"')
    if src_pos > 0:
        # Look backward from src to find the img tag start
        img_start = updated_content.rfind('<img', 0, src_pos)
        if img_start == -1:
            img_start = updated_content.rfind('<source', 0, src_pos)

        if img_start >= 0:
            # Look forward from src to find the closing >
            tag_end = updated_content.find('>', src_pos)
            if tag_end > 0:
                tag_content = updated_content[img_start:tag_end+1]

                # Check if there's an alt attribute
                if 'alt=' in tag_content:
                    # Replace existing alt
                    new_tag = re.sub(
                        r'alt=["\'][^"\']*["\']',
                        f'alt="{alt_text}"',
                        tag_content
                    )
                else:
                    # Add alt attribute before closing >
                    new_tag = tag_content.rstrip('>').rstrip() + f' alt="{alt_text}">'

                updated_content = updated_content[:img_start] + new_tag + updated_content[tag_end+1:]

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True, f"Updated {filename} with {new_image_path}"
    except Exception as e:
        return False, f"Error writing {filename}: {e}"

def update_journal_index():
    """Update journal.html index page thumbnails"""
    filepath = '/sessions/affectionate-cool-johnson/mnt/Stitch_Claude_Co-work/stitch-website-v2/journal.html'

    if not os.path.exists(filepath):
        return False, "journal.html not found"

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return False, f"Error reading journal.html: {e}"

    # Define which thumbnails to update
    # Looking for X-Pac thumbnail to replace with materials-dsc01318.jpg
    # FOB/EXW, import-duties, vietnam-gsp keep Unsplash

    # We need to find the thumbnail for X-Pac article and replace it
    xpac_unsplash = r'(?:journal-xpac\.html[^}]*?src=["\']https://images\.unsplash\.com/[^"\']*["\']|src=["\']https://images\.unsplash\.com/[^"\']*["\'][^}]*?journal-xpac\.html)'

    # More targeted approach: find article references and update their thumbnails
    # For X-Pac article thumbnail
    if 'journal-xpac.html' in content:
        # Find the context around the xpac link and update nearby image
        xpac_pattern = r'(<article[^>]*?class="[^"]*card[^"]*"[^>]*>.*?journal-xpac\.html.*?</article>)'

        def replace_xpac_image(match):
            article_section = match.group(1)
            # Replace Unsplash in this section with materials image
            updated = re.sub(
                r'src=["\']https://images\.unsplash\.com/[^"\']*["\']',
                'src="images/journal/materials-dsc01318.jpg"',
                article_section,
                count=1
            )
            return updated

        updated_content = re.sub(xpac_pattern, replace_xpac_image, content, flags=re.DOTALL)
        content = updated_content

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, "Updated journal.html with X-Pac thumbnail"
    except Exception as e:
        return False, f"Error writing journal.html: {e}"

def main():
    base_dir = '/sessions/affectionate-cool-johnson/mnt/Stitch_Claude_Co-work/stitch-website-v2'

    print("=" * 70)
    print("UPDATING ARTICLE IMAGES")
    print("=" * 70)

    articles_updated = 0
    articles_skipped = 0

    # Update articles with local images
    for filename in sorted(IMAGE_ASSIGNMENTS.keys()):
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            success, message = update_article_image(filepath)
            status = "✓" if success else "✗"
            print(f"{status} {message}")
            if success:
                articles_updated += 1
            else:
                articles_skipped += 1
        else:
            print(f"✗ File not found: {filename}")
            articles_skipped += 1

    print("\n" + "=" * 70)
    print("UPDATING JOURNAL INDEX")
    print("=" * 70)

    success, message = update_journal_index()
    status = "✓" if success else "✗"
    print(f"{status} {message}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Articles updated: {articles_updated}")
    print(f"Articles with issues: {articles_skipped}")
    print("\nNote: The following articles KEEP Unsplash images:")
    print("  - journal-fob-exw-cif-ddp.html")
    print("  - journal-import-duties.html")
    print("  - journal-vietnam-gsp.html")

if __name__ == '__main__':
    main()
