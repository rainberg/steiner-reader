#!/usr/bin/env python3
"""Position GA279 images by exact PDF page positions."""

import pdfplumber
import psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"

# Lecture page starts from PDF scan
LEC_PAGES = {
    1: 4, 2: 19, 3: 40, 4: 57, 5: 72, 6: 88, 7: 102,
    8: 114, 9: 128, 10: 140, 11: 155, 12: 169, 13: 189,
    14: 200, 15: 213, 16: 223, 17: 238, 18: 310
}

conn = psycopg2.connect(DB)
cur = conn.cursor()

# Get GA279 lecture IDs from DB
cur.execute("""
    SELECT l.id, l.order_index, COUNT(s.id)
    FROM lectures l
    JOIN paragraphs p ON p.lecture_id = l.id
    JOIN sentences s ON s.paragraph_id = p.id
    WHERE l.book_id = (SELECT id FROM books WHERE ga_number='GA279')
    GROUP BY l.id, l.order_index
    ORDER BY l.order_index
""")
lec_data = {r[1]: (r[0], r[2]) for r in cur.fetchall()}  # order_index -> (id, sent_count)

# Scan PDF for images and their pages
with pdfplumber.open('/opt/steiner-reader/uploads/GA279.pdf') as pdf:
    # Build list of (page_number, image_count) per page
    page_images = []
    for i, page in enumerate(pdf.pages):
        imgs = page.images
        if imgs:
            page_images.append((i + 1, len(imgs)))

# Map each image instance to a lecture and fractional position
img_positions = []  # (lec_order, fraction)
for pg, count in page_images:
    # Find which lecture this page belongs to
    lec_order = 1
    for l in sorted(LEC_PAGES.keys()):
        if pg >= LEC_PAGES[l]:
            lec_order = l
    # Fractional position within lecture
    start = LEC_PAGES[lec_order]
    end = LEC_PAGES.get(lec_order + 1, 310)
    frac = max(0, min(1, (pg - start) / max(1, end - start)))
    for _ in range(count):
        img_positions.append((lec_order, frac))

# Now match to DB images (ordered by order_index, which reflects PDF order)
cur.execute("""
    SELECT li.id, l.order_index
    FROM lecture_images li
    JOIN lectures l ON li.lecture_id = l.id
    WHERE l.book_id = (SELECT id FROM books WHERE ga_number='GA279')
    ORDER BY l.order_index, li.order_index, li.id
""")
db_images = cur.fetchall()

if len(db_images) != len(img_positions):
    print(f"WARNING: DB has {len(db_images)} images but PDF found {len(img_positions)} image instances!")
    print("Using DB count, truncating/duplicating positions as needed.")

total = 0
for i, (img_id, lec_order) in enumerate(db_images):
    if i < len(img_positions):
        lec_o, frac = img_positions[i]
        if lec_o != lec_order:
            print(f"  Image {img_id}: PDF says lec {lec_o} but DB has lec {lec_order} — using DB lecture")
            lec_o = lec_order
    else:
        lec_o = lec_order
        frac = 0.5  # fallback

    # Get sentence at this fractional position
    lec_id, sent_count = lec_data.get(lec_o, (None, 0))
    if not lec_id or sent_count == 0:
        continue

    target_pos = int(frac * sent_count)
    if target_pos >= sent_count:
        target_pos = sent_count - 1

    # Find the sentence at this position
    cur.execute("""
        SELECT s.id FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
        LIMIT 1 OFFSET %s
    """, (lec_id, target_pos))
    row = cur.fetchone()
    if row:
        cur.execute(
            "UPDATE lecture_images SET after_sentence_id = %s WHERE id = %s",
            (row[0], img_id)
        )
        total += 1

conn.commit()
print(f"GA279: {total} images positioned by PDF page location")
cur.close()
conn.close()
