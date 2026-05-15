#!/usr/bin/env python3
"""Simple retranslation for GA312 — uses deep-translator directly via psycopg2."""
import sys, time
import psycopg2
from deep_translator import GoogleTranslator

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"

def main():
    conn = psycopg2.connect(DB)
    cur = conn.cursor()

    # Get all lectures for book 258 (GA312)
    cur.execute("SELECT id FROM lectures WHERE book_id=258 AND level='lecture' ORDER BY order_index")
    lec_ids = [r[0] for r in cur.fetchall()]

    translator = GoogleTranslator(source='de', target='zh-CN')
    total_done = 0

    for lid in lec_ids:
        cur.execute("""
            SELECT s.id, s.text_de FROM sentences s
            JOIN paragraphs p ON s.paragraph_id = p.id
            WHERE p.lecture_id = %s AND (s.text_zh IS NULL OR s.text_zh = '')
            ORDER BY p.order_index, s.order_index
        """, (lid,))
        pending = cur.fetchall()

        if not pending:
            cur.execute("SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id WHERE p.lecture_id=%s", (lid,))
            total = cur.fetchone()[0]
            print(f"Lect {lid}: all {total} translated")
            continue

        print(f"Lect {lid}: {len(pending)} untranslated", flush=True)

        for i in range(0, len(pending), 10):
            batch = pending[i:i+10]
            for sid, text_de in batch:
                try:
                    zh = translator.translate(text_de[:4000])  # limit for API
                    cur.execute("UPDATE sentences SET text_zh=%s WHERE id=%s", (zh, sid))
                    total_done += 1
                except Exception as e:
                    print(f"  Error at sentence {sid}: {e}", flush=True)
                    time.sleep(2)
                time.sleep(0.2)  # rate limit
            conn.commit()
            print(f"  Batch {i}-{min(i+10, len(pending))}: {total_done} total done", flush=True)

        cur.execute("UPDATE lectures SET is_published=true WHERE id=%s", (lid,))
        conn.commit()
        print(f"Lect {lid}: DONE", flush=True)

    cur.close()
    conn.close()
    print(f"\nAll done. {total_done} sentences translated.", flush=True)


if __name__ == '__main__':
    main()
