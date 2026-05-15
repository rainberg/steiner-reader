#!/usr/bin/env python3
"""
Fix lecture image positions by matching #Bild markers in sentence text.
Cleans up #Bild markers from sentences and links images to the right sentences.

Usage: python3 scripts/fix_image_positions.py --dry-run
       python3 scripts/fix_image_positions.py
"""

import re
import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "Dd08120@"

# Pattern for #Bild markers: #Bild s. 95, #Bild s.95, Bild s. 20, etc.
BILD_PATTERN = re.compile(r'#?[Bb]ild\s*(s\.?\s*\d+)?')


def fix_lecture_images(cursor, lecture_id, dry_run=False):
    """Match images to sentences with #Bild references for one lecture."""
    # Get images ordered
    cursor.execute("""
        SELECT id, filename FROM lecture_images
        WHERE lecture_id = %s ORDER BY order_index, id
    """, (lecture_id,))
    images = list(cursor.fetchall())
    if not images:
        return 0, 0

    # Get sentences with #Bild markers, in text order
    cursor.execute("""
        SELECT s.id, s.text_de
        FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s AND s.text_de LIKE '%%#Bild%%'
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    bild_sentences = list(cursor.fetchall())

    matched = 0
    img_idx = 0

    for sent_id, text_de in bild_sentences:
        if img_idx >= len(images):
            break

        img_id, _ = images[img_idx]

        if not dry_run:
            # Link image to this sentence
            cursor.execute(
                "UPDATE lecture_images SET after_sentence_id = %s WHERE id = %s",
                (sent_id, img_id)
            )
            # Clean up #Bild marker from sentence
            cleaned = BILD_PATTERN.sub('', text_de).strip()
            cleaned = re.sub(r'\s+', ' ', cleaned)
            cursor.execute(
                "UPDATE sentences SET text_de = %s WHERE id = %s",
                (cleaned, sent_id)
            )

        img_idx += 1
        matched += 1

    return matched, len(images)


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Get all lectures with images
    cursor.execute("""
        SELECT DISTINCT l.id, l.title_de, b.ga_number
        FROM lecture_images li
        JOIN lectures l ON li.lecture_id = l.id
        JOIN books b ON l.book_id = b.id
        ORDER BY l.id
    """)
    lectures = cursor.fetchall()

    total_matched = 0
    total_images = 0
    fixed_lectures = 0

    for lec_id, title, ga in lectures:
        m, t = fix_lecture_images(cursor, lec_id, dry_run=args.dry_run)
        if m > 0:
            fixed_lectures += 1
            total_matched += m
            total_images += t
            print(f"  {ga} lect {lec_id} \"{title[:40]}\": matched {m}/{t} images", flush=True)

    if not args.dry_run and total_matched > 0:
        conn.commit()
        print(f"\nFixed {fixed_lectures} lectures: {total_matched}/{total_images} images linked.", flush=True)
    elif args.dry_run:
        print(f"\nDRY RUN: {fixed_lectures} lectures, {total_matched}/{total_images} images would be linked.", flush=True)
    else:
        print("No images matched.", flush=True)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
