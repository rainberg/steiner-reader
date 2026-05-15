#!/usr/bin/env python3
"""
Verify and fix paragraph structure for books with .doc source files.
Uses full-text paragraph extraction (no lecture detection needed) and
matches to DB sentences within each lecture.

Usage: python3 scripts/verify_and_fix_paras.py GA312 --dry-run
       python3 scripts/verify_and_fix_paras.py GA312
       python3 scripts/verify_and_fix_paras.py --all
"""

import argparse
import os
import re
import subprocess
import sys
import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "Dd08120@"


def normalize(text):
    text = (text or '').replace('\xad', '').replace('­', '')
    for old, new in [('Ã¤','ä'),('Ã¶','ö'),('Ã¼','ü'),('ÃŸ','ß'),
                      ('Ã„','Ä'),('Ã–','Ö'),('Ãœ','Ü')]:
        text = text.replace(old, new)
    return re.sub(r'\s+', ' ', text).strip()


def extract_all_paragraphs_from_doc(doc_path):
    """Extract ALL paragraphs from .doc file via catdoc.
    Uses blank lines as paragraph separators. No lecture detection needed.
    Returns list of paragraph texts in order.
    """
    try:
        result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=60)
        content = result.stdout.decode('latin-1')
    except Exception as e:
        print(f"    catdoc error: {e}", file=sys.stderr)
        return []

    pages = content.split('\x0c')
    all_paras = []

    for page_text in pages:
        lines = page_text.split('\n')
        cur = []
        for line in lines:
            s = line.strip()
            if s:
                cur.append(s)
            elif cur:
                pt = normalize(' '.join(cur))
                if len(pt) > 30:  # skip very short lines
                    all_paras.append(pt)
                cur = []
        if cur:
            pt = normalize(' '.join(cur))
            if len(pt) > 30:
                all_paras.append(pt)

    return all_paras


def verify_lecture(cursor, lecture_id, title_de, source_paras):
    """Check if lecture paragraphs align with source. Returns (ok, details)."""
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    sentences = cursor.fetchall()

    if len(sentences) < 10:
        return True, f"too_small({len(sentences)}s)"

    # Build sentence text index
    sent_text = ""
    sent_bounds = []
    for sid, td, tz in sentences:
        n = normalize(td)
        if n:
            start = len(sent_text)
            sent_text += n + " "
            sent_bounds.append((start, len(sent_text) - 1, sid))

    # Try to match source paragraphs to sentence ranges
    matched = 0
    search_pos = 0
    for para_text in source_paras:
        if len(para_text) < 30:
            continue
        # Use first 25 chars as key
        key = para_text[:25]
        pos = sent_text.find(key, search_pos)
        if pos < 0:
            key = para_text[:15]
            pos = sent_text.find(key, search_pos)
        if pos >= 0:
            matched += 1
            search_pos = pos + len(key)

    match_rate = matched / max(len(source_paras), 1)
    if match_rate > 0.3:
        return True, f"matched({matched}/{len(source_paras)})"
    else:
        return False, f"low_match({matched}/{len(source_paras)})"


def fix_lecture_paras(cursor, lecture_id, source_paras, dry_run=False):
    """Regroup lecture paragraphs using content-aware heuristic."""
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    sentences = cursor.fetchall()

    if len(sentences) < 10:
        return 0, 0, 0

    # Content-aware grouping
    PARA_START = re.compile(
        r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b|'
        r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Dasjenige|Diejenige)\b|'
        r'^(Das ist|Dieser|Diese|Dieses|Aber|Allein|Dagegen|Hingegen|Dem steht)\b|'
        r'^(Was ist|Wie ist|Worin|Wodurch|Warum)\b|'
        r'^(Ich möchte|Ich will|Ich werde|Gehen wir|Sehen wir|Wenden wir)\b'
    )
    MAX_SENTS = 12

    groups = []
    cur = []
    for s in sentences:
        if len(cur) >= 2 and PARA_START.match(normalize(s[1])):
            groups.append(cur)
            cur = []
        if len(cur) >= MAX_SENTS:
            groups.append(cur)
            cur = []
        cur.append(s)
    if cur:
        groups.append(cur)

    # Merge singles
    merged = []
    for g in groups:
        if len(g) <= 1 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
    groups = merged

    if len(groups) <= 1:
        return 0, len(groups), len(sentences)

    cursor.execute("SELECT COUNT(*) FROM paragraphs WHERE lecture_id=%s", (lecture_id,))
    old_paras = cursor.fetchone()[0]

    if dry_run:
        return old_paras, len(groups), len(sentences)

    cursor.execute(
        "UPDATE lecture_images SET after_sentence_id=NULL, after_paragraph_id=NULL WHERE lecture_id=%s",
        (lecture_id,)
    )
    cursor.execute("DELETE FROM paragraphs WHERE lecture_id=%s", (lecture_id,))

    for pi, group in enumerate(groups, 1):
        cursor.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
            (lecture_id, pi)
        )
        pid = cursor.fetchone()[0]
        for si, (sid, td, tz) in enumerate(group, 1):
            cursor.execute(
                "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s,%s,%s,%s)",
                (pid, si, td, tz)
            )

    return old_paras, len(groups), len(sentences)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("books", nargs="*", help="GA numbers to process")
    parser.add_argument("--all", action="store_true", help="All books with .doc")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    doc_dir = "/opt/steiner-reader/books/doc"

    # Get books to process
    if args.books:
        placeholders = ','.join(['%s'] * len(args.books))
        cursor.execute(f"SELECT id, ga_number FROM books WHERE ga_number IN ({placeholders}) ORDER BY ga_number", args.books)
    else:
        cursor.execute("SELECT id, ga_number FROM books ORDER BY ga_number")

    books = cursor.fetchall()
    total_ok = 0
    total_fixed = 0
    total_failed = 0
    total_no_doc = 0

    for book_id, ga in books:
        doc_path = os.path.join(doc_dir, f"{ga}.doc")
        if not os.path.exists(doc_path):
            total_no_doc += 1
            continue

        # Extract paragraphs from .doc
        source_paras = extract_all_paragraphs_from_doc(doc_path)
        if len(source_paras) < 5:
            total_failed += 1
            continue

        # Verify each lecture
        cursor.execute("SELECT id, title_de FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
        lectures = cursor.fetchall()

        book_ok = 0
        book_fixed = 0
        for lid, ltitle in lectures:
            ok, detail = verify_lecture(cursor, lid, ltitle, source_paras)
            if ok:
                book_ok += 1
            elif not args.verify_only:
                old, new, total = fix_lecture_paras(cursor, lid, source_paras, dry_run=args.dry_run)
                if new != old and new > 1:
                    book_fixed += 1
                    print(f"  [{ga}] lect {lid}: {old}→{new} paras ({total}s) {'DRY RUN' if args.dry_run else 'FIXED'}", flush=True)

        if book_fixed > 0:
            total_fixed += 1
        elif book_ok == len(lectures):
            total_ok += 1
        elif book_ok + book_fixed < len(lectures):
            total_failed += 1

    if not args.dry_run and total_fixed > 0:
        conn.commit()

    print(f"\nResults: {total_ok} OK, {total_fixed} fixed, {total_failed} failed, {total_no_doc} no .doc", flush=True)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
