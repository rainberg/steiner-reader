#!/usr/bin/env python3
"""SAFE paragraph rebuilding — groups sentences into paragraphs without duplication."""

import argparse, re, psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
MAX_SENTS = 12

PARA_START = re.compile(
    r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b|'
    r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Dasjenige|Diejenige)\b|'
    r'^(Das ist|Dieser|Diese|Dieses|Aber|Allein|Dagegen|Hingegen|Dem steht)\b|'
    r'^(Was ist|Wie ist|Worin|Wodurch|Warum)\b|'
    r'^(Ich möchte|Ich will|Ich werde|Gehen wir|Sehen wir|Wenden wir)\b'
)

def is_para_start(text):
    return bool(PARA_START.match((text or '').replace('\xad','').strip()))


def regroup_safe(cur, lecture_id):
    """Get sentences, group, UPDATE paragraph_id (no DELETE/INSERT of sentences)."""
    cur.execute("""
        SELECT s.id, s.text_de FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    rows = cur.fetchall()
    if len(rows) < 10:
        return 0, 0

    # Group into new paragraphs
    groups = []; current = []
    for sid, text in rows:
        if len(current) >= 2 and is_para_start(text):
            groups.append(current); current = []
        if len(current) >= MAX_SENTS:
            groups.append(current); current = []
        current.append(sid)
    if current: groups.append(current)

    # Merge small groups into neighbors
    merged = []
    for g in groups:
        if len(g) <= 1 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
    groups = merged

    if len(groups) <= 1:
        return 0, 0

    # Delete old paragraphs (sentences will be re-assigned)
    cur.execute(
        "UPDATE lecture_images SET after_sentence_id=NULL, after_paragraph_id=NULL WHERE lecture_id=%s",
        (lecture_id,)
    )
    cur.execute("DELETE FROM paragraphs WHERE lecture_id = %s", (lecture_id,))

    total = 0
    # Create new paragraphs and reassign sentences
    for pi, sent_ids in enumerate(groups, 1):
        cur.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
            (lecture_id, pi)
        )
        pid = cur.fetchone()[0]
        for si, sid in enumerate(sent_ids, 1):
            cur.execute(
                "UPDATE sentences SET paragraph_id=%s, order_index=%s WHERE id=%s",
                (pid, si, sid)
            )
        total += len(sent_ids)

    return len(groups), total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
    books = cur.fetchall()

    total_paras = 0
    total_sents = 0
    fixed = 0

    for bid, ga in books:
        cur.execute(
            "SELECT id FROM lectures WHERE book_id=%s AND level='lecture' ORDER BY order_index",
            (bid,)
        )
        for (lid,) in cur.fetchall():
            p, s = regroup_safe(cur, lid)
            if p > 0:
                total_paras += p
                total_sents += s
                fixed += 1

        if fixed > 0 and fixed % 50 == 0:
            print(f"  ... {fixed} lectures fixed ({total_paras} paras, {total_sents} sents)", flush=True)

    if not args.dry_run:
        conn.commit()
        print(f"Done: {fixed} lectures, {total_paras} paragraphs, {total_sents} sentences regrouped.", flush=True)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
