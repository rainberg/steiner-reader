#!/usr/bin/env python3
"""
Position all unlinked lecture images proportionally within their lectures.
Images are distributed evenly among sentences, preserving their order.

Usage: python3 scripts/position_all_images.py --dry-run
       python3 scripts/position_all_images.py
"""

import argparse
import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "Dd08120@"


def position_images_in_lecture(cursor, lecture_id, dry_run=False):
    """Distribute unlinked images evenly among sentences in a lecture."""
    # Get unlinked images for this lecture
    cursor.execute("""
        SELECT id, filename FROM lecture_images
        WHERE lecture_id = %s AND after_sentence_id IS NULL
        ORDER BY order_index, id
    """, (lecture_id,))
    images = cursor.fetchall()
    if not images:
        return 0

    # Get sentences for this lecture, sorted
    cursor.execute("""
        SELECT s.id FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    sentences = cursor.fetchall()
    if not sentences:
        return 0

    total_sents = len(sentences)
    total_imgs = len(images)

    if total_imgs >= total_sents:
        # More images than sentences: 1 image per sentence from the start
        matches = list(zip([s[0] for s in sentences[:total_imgs]], [i[0] for i in images]))
    else:
        # Distribute evenly: image i goes after sentence at position
        # floor((i+1) * total_sents / (total_imgs + 1))
        matches = []
        for i, (img_id, _) in enumerate(images):
            pos = int((i + 1) * total_sents / (total_imgs + 1))
            if pos >= total_sents:
                pos = total_sents - 1
            sent_id = sentences[pos][0]
            matches.append((sent_id, img_id))

    if not dry_run:
        for sent_id, img_id in matches:
            cursor.execute(
                "UPDATE lecture_images SET after_sentence_id = %s WHERE id = %s",
                (sent_id, img_id)
            )

    return len(matches)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    # Get all lectures with unlinked images
    cursor.execute("""
        SELECT l.id, l.title_de, b.ga_number, COUNT(li.id) as unlinked
        FROM lecture_images li
        JOIN lectures l ON li.lecture_id = l.id
        JOIN books b ON l.book_id = b.id
        WHERE li.after_sentence_id IS NULL
        GROUP BY l.id, l.title_de, b.ga_number
        ORDER BY b.ga_number, MIN(l.order_index)
    """)
    lectures = cursor.fetchall()

    total = 0
    fixed = 0
    for lec_id, title, ga, unlinked in lectures:
        n = position_images_in_lecture(cursor, lec_id, dry_run=args.dry_run)
        if n > 0:
            total += n
            fixed += 1
            print(f"  {ga} lect {lec_id} \"{title[:45]}\": {n} images positioned", flush=True)

    if not args.dry_run and total > 0:
        conn.commit()
        print(f"\nFixed {fixed} lectures: {total} images positioned.", flush=True)
    elif args.dry_run:
        print(f"\nDRY RUN: {fixed} lectures, {total} images would be positioned.", flush=True)
    else:
        print("No unlinked images found.", flush=True)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
