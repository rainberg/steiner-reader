#!/usr/bin/env python3
"""Position all images and save anchor text (surrounding sentences) for future re-linking."""

import psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
MAX_SENTS = 12

PARA_START_KEYS = [
    'Erstens','Zweitens','Drittens','Viertens','Fünftens','Sechstens','Siebentens','Achtens','Neuntens','Zehntens',
    'Heute','Nun','Also','Sodann','Schlie','Zusammen','Dasjenige','Diejenige',
    'Das ist','Dieser','Diese','Dieses','Aber','Allein','Dagegen','Hingegen','Dem steht',
    'Ich möchte','Ich will','Ich werde','Gehen wir','Sehen wir','Wenden wir'
]


def normalize(text):
    return (text or '').replace('\xad','').strip()


def is_para_start(text):
    t = normalize(text)
    for key in PARA_START_KEYS:
        if t.startswith(key):
            return True
    return False


def process_lecture(cur, lec_id):
    """Regroup sentences AND position images with anchors."""
    # Get all sentences in order
    cur.execute("""
        SELECT s.id, s.text_de FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lec_id,))
    sent_rows = cur.fetchall()
    if len(sent_rows) < 10:
        return

    # Get images for this lecture
    cur.execute("""
        SELECT id FROM lecture_images
        WHERE lecture_id = %s AND after_sentence_id IS NULL
        ORDER BY order_index, id
    """, (lec_id,))
    img_ids = [r[0] for r in cur.fetchall()]

    # Group sentences into paragraphs
    groups = []; current = []
    for sid, text in sent_rows:
        if len(current) >= 2 and is_para_start(text):
            groups.append(current); current = []
        if len(current) >= MAX_SENTS:
            groups.append(current); current = []
        current.append(sid)
    if current: groups.append(current)

    # Merge singles
    merged = []
    for g in groups:
        if len(g) <= 1 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
    groups = merged
    if len(groups) <= 1:
        return

    # Position images: distribute in order
    sent_flat = [sid for g in groups for sid in g]
    total_sents = len(sent_flat)
    n_imgs = len(img_ids)

    img_positions = {}  # img_id -> sent_id
    for i, img_id in enumerate(img_ids):
        pos = int((i + 1) * total_sents / (n_imgs + 1))
        if pos >= total_sents: pos = total_sents - 1
        sent_id = sent_flat[pos]
        img_positions[img_id] = sent_id

    # Save anchors: text of sentence before and after each image
    for img_id, sent_id in img_positions.items():
        idx = sent_flat.index(sent_id) if sent_id in sent_flat else -1
        before = sent_flat[idx - 1] if idx > 0 else None
        after = sent_flat[idx + 1] if idx < len(sent_flat) - 1 else None

        before_text = None
        after_text = None
        for sid, text in sent_rows:
            if sid == before: before_text = text
            if sid == after: after_text = text

        cur.execute(
            "UPDATE lecture_images SET after_sentence_id=%s, anchor_before=%s, anchor_after=%s WHERE id=%s",
            (sent_id, before_text, after_text, img_id)
        )

    # Rebuild paragraphs WITHOUT cascading delete:
    # 1. Create all new paragraphs
    new_paras = []
    for pi, sent_ids in enumerate(groups, 1):
        cur.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
            (lec_id, pi)
        )
        new_paras.append((cur.fetchone()[0], sent_ids))

    # 2. Update sentences to point to new paragraphs
    for pid, sent_ids in new_paras:
        for si, sid in enumerate(sent_ids, 1):
            cur.execute(
                "UPDATE sentences SET paragraph_id=%s, order_index=%s WHERE id=%s",
                (pid, si, sid)
            )

    # 3. Delete old paragraphs (no longer referenced by any sentences)
    cur.execute(
        "DELETE FROM paragraphs WHERE lecture_id = %s AND id NOT IN (SELECT DISTINCT paragraph_id FROM sentences)",
        (lec_id,)
    )


def main():
    conn = psycopg2.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
    books = cur.fetchall()
    fixed = 0; imgs = 0

    for bid, ga in books:
        cur.execute("SELECT id FROM lectures WHERE book_id=%s AND level='lecture' ORDER BY order_index", (bid,))
        for (lid,) in cur.fetchall():
            process_lecture(cur, lid)
            fixed += 1
        if fixed % 500 == 0:
            print(f"  {fixed} lectures done...", flush=True)

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM lecture_images WHERE after_sentence_id IS NOT NULL")
    linked = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM lecture_images WHERE anchor_before IS NOT NULL")
    anchored = cur.fetchone()[0]
    print(f"Done: {fixed} lectures. {linked} images positioned, {anchored} with anchors.", flush=True)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
