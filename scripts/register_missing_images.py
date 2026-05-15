#!/usr/bin/env python3
"""Register disk images missing from lecture_images table, assign to lectures, position by source."""

import os, re, psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
IMG_BASE = "/opt/steiner-reader/images"

conn = psycopg2.connect(DB)
cur = conn.cursor()

# Get existing DB images
cur.execute("SELECT b.ga_number, li.filename FROM lecture_images li JOIN lectures l ON li.lecture_id = l.id JOIN books b ON l.book_id = b.id")
db_images = {}
for ga, fn in cur.fetchall():
    db_images.setdefault(ga, set()).add(fn)

# Get book_id -> ga_number mapping
cur.execute("SELECT id, ga_number FROM books")
books = {ga: bid for bid, ga in cur.fetchall()}

# Get all image files on disk
total_new = 0
for ga_dir in sorted(os.listdir(IMG_BASE)):
    path = os.path.join(IMG_BASE, ga_dir)
    if not os.path.isdir(path) or not ga_dir.startswith("GA"):
        continue
    if ga_dir not in books:
        continue

    book_id = books[ga_dir]
    disk_files = sorted(f for f in os.listdir(path) if f.endswith(('.png','.jpg','.jpeg')))
    db_files = db_images.get(ga_dir, set())
    new_files = [f for f in disk_files if f not in db_files]

    if not new_files:
        continue

    # Get lectures for this book, sorted
    cur.execute(
        "SELECT id, order_index FROM lectures WHERE book_id = %s AND level = 'lecture' ORDER BY order_index",
        (book_id,)
    )
    lectures = cur.fetchall()
    if not lectures:
        continue

    # Distribute new images across lectures based on filename order
    n_imgs = len(new_files)
    n_lecs = len(lectures)

    for i, filename in enumerate(new_files):
        lec_idx = int(i * n_lecs / n_imgs) if n_imgs >= n_lecs else i % n_lecs
        if lec_idx >= n_lecs:
            lec_idx = n_lecs - 1
        lec_id = lectures[lec_idx][0]

        # Try to extract page number from filename
        pg = re.search(r'p(\d+)|_p(\d+)|page(\d+)', filename)
        page_num = int(pg.group(1) or pg.group(2) or pg.group(3)) if pg else 0

        cur.execute(
            "INSERT INTO lecture_images (lecture_id, filename, page_number, order_index) VALUES (%s,%s,%s,%s)",
            (lec_id, filename, page_num, i)
        )
        total_new += 1

    print(f"{ga_dir}: {len(new_files)} new images registered")

conn.commit()
print(f"\nTotal new images registered: {total_new}")
cur.close()
conn.close()
