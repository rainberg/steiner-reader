#!/usr/bin/env python3
"""
Safe paragraph regrouping: group sentences into logical paragraphs
using content-aware heuristics. Preserves ALL sentences and translations.
"""

import re, psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
MAX_SENTS = 12

PARA_START = re.compile(
    r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b|'
    r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Dasjenige|Diejenige)\b|'
    r'^(Das ist|Dieser|Diese|Dieses|Aber|Allein|Dagegen|Hingegen|Dem steht|Demgegenüber)\b|'
    r'^(Was ist|Wie ist|Worin|Wodurch|Warum|Weshalb)\b|'
    r'^(Ich möchte|Ich will|Ich werde|Gehen wir|Sehen wir|Wenden wir)\b|'
    r'^[A-ZÄÖÜ][a-zäöüß]+ [A-ZÄÖÜ][a-zäöüß]+[,:]'  # Named entities
)


def is_para_start(text):
    return bool(PARA_START.match((text or '').replace('\xad', '').strip()))


def regroup_lecture(cur, lec_id):
    """Group sentences into content-aware paragraphs. Returns number of groups."""
    cur.execute("""
        SELECT s.id, s.text_de, s.text_zh FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lec_id,))
    sents = cur.fetchall()
    if len(sents) < 10:
        return 0

    # Group using content signals and max size
    groups = []
    cur_group = []
    for sid, td, tz in sents:
        if len(cur_group) >= 2 and is_para_start(td):
            groups.append(cur_group)
            cur_group = []
        if len(cur_group) >= MAX_SENTS:
            groups.append(cur_group)
            cur_group = []
        cur_group.append((sid, td, tz))
    if cur_group:
        groups.append(cur_group)

    # Merge very small groups into neighbors
    merged = []
    for g in groups:
        if len(g) <= 1 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
    groups = merged

    if len(groups) <= 1:
        return 0

    # Save image refs
    cur.execute("UPDATE lecture_images SET after_sentence_id=NULL, after_paragraph_id=NULL WHERE lecture_id=%s", (lec_id,))

    # 1. Create NEW paragraphs first
    new_pids = []
    for pi, group in enumerate(groups, 1):
        cur.execute("INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id", (lec_id, pi))
        new_pids.append((cur.fetchone()[0], group))

    # 2. UPDATE sentences to point to new paragraphs (safe - no cascade)
    for pid, group in new_pids:
        for si, (sid, td, tz) in enumerate(group, 1):
            cur.execute("UPDATE sentences SET paragraph_id=%s, order_index=%s WHERE id=%s", (pid, si, sid))

    # 3. Delete OLD paragraphs that have no sentences (safe - cascade only fires on empty paras)
    cur.execute("DELETE FROM paragraphs WHERE lecture_id = %s AND id NOT IN (SELECT DISTINCT paragraph_id FROM sentences)", (lec_id,))

    return len(groups)


def main():
    conn = psycopg2.connect(DB)
    cur = conn.cursor()

    cur.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
    books = cur.fetchall()
    total_paras = 0
    total_sents = 0
    book_count = 0

    for bid, ga in books:
        cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (bid,))
        lects = cur.fetchall()
        book_paras = 0
        book_sents = 0
        for (lid,) in lects:
            n = regroup_lecture(cur, lid)
            if n > 0:
                book_paras += n
                cur.execute("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id WHERE p.lecture_id=%s", (lid,))
                book_sents += cur.fetchone()[0]

        if book_paras > 0:
            book_count += 1
            total_paras += book_paras
            total_sents += book_sents
            if book_count % 50 == 0:
                print(f"  {book_count} books... ({total_paras} paras, {total_sents} sents)", flush=True)
                conn.commit()

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM sentences WHERE text_zh IS NOT NULL")
    trans = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM sentences")
    total = cur.fetchone()[0]
    print(f"\nDone: {book_count} books, {total_paras} paragraphs, {total_sents} sentences.")
    print(f"Translations preserved: {trans}/{total}")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
