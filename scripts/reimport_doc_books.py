#!/usr/bin/env python3
"""Re-import books from .doc source files with proper paragraph structure.

Paragraphs are separated by blank lines in .doc files.
Existing translations are preserved by text matching.
"""

import argparse, os, re, subprocess, sys, psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
DOC_DIR = "/opt/steiner-reader/books/doc"

SENTENCE_BREAK = re.compile(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ"«„0-9])')


def normalize(text):
    """Normalize German text for matching."""
    text = text or ''
    text = text.replace('\xad', '').replace('­', '')
    # Fix latin-1 double encoding from catdoc
    for old, new in [('Ã¤','ä'),('Ã¶','ö'),('Ã¼','ü'),('ÃŸ','ß'),
                      ('Ã„','Ä'),('Ã–','Ö'),('Ãœ','Ü')]:
        text = text.replace(old, new)
    return re.sub(r'\s+', ' ', text).strip()


def extract_doc_paragraphs(doc_path):
    """Extract paragraphs from .doc file using blank line separation."""
    try:
        result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=120)
        content = result.stdout.decode('latin-1')
    except Exception as e:
        print(f"  ERROR extracting {doc_path}: {e}", file=sys.stderr)
        return []

    pages = content.split('\x0c')
    all_paragraphs = []

    for page_text in pages:
        if not page_text.strip():
            continue
        lines = page_text.split('\n')
        current = []
        for line in lines:
            s = line.strip()
            if s:
                current.append(s)
            elif current:
                para = normalize(' '.join(current))
                if len(para) > 40:  # skip short fragments
                    # Skip front matter
                    if any(para.startswith(w) for w in ('INHALT', 'HINWEISE', 'RUDOLF STEINER')):
                        current = []
                        continue
                    all_paragraphs.append(para)
                current = []
        if current:
            para = normalize(' '.join(current))
            if len(para) > 40:
                all_paragraphs.append(para)

    return all_paragraphs


def reimport_book(cursor, book_id, ga_number, dry_run=False):
    """Re-import one book from .doc, preserving translations."""
    doc_path = os.path.join(DOC_DIR, f"{ga_number}.doc")
    if not os.path.exists(doc_path):
        return None, "no_doc"

    paragraphs = extract_doc_paragraphs(doc_path)
    if len(paragraphs) < 3:
        return None, f"too_few_paras({len(paragraphs)})"

    # Save existing translations
    cursor.execute("""
        SELECT s.text_de, s.text_zh FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        JOIN lectures l ON p.lecture_id = l.id
        WHERE l.book_id = %s AND s.text_zh IS NOT NULL AND s.text_zh != ''
    """, (book_id,))
    translations = {}
    for td, tz in cursor.fetchall():
        key = normalize(td)
        if key and tz:
            translations[key] = tz

    if dry_run:
        total_sents = sum(len(SENTENCE_BREAK.split(p)) for p in paragraphs)
        return (len(paragraphs), total_sents, len(translations)), "ok"

    # Get existing lectures for this book (preserve their metadata)
    cursor.execute("""
        SELECT id, title_de, lecture_date, location, order_index
        FROM lectures WHERE book_id = %s ORDER BY order_index
    """, (book_id,))
    old_lectures = cursor.fetchall()

    # Clear old data for this book
    cursor.execute(
        "DELETE FROM lecture_images WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)",
        (book_id,))
    cursor.execute(
        "DELETE FROM contributions WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)",
        (book_id,))
    cursor.execute(
        "DELETE FROM lecture_access WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)",
        (book_id,))
    cursor.execute(
        "DELETE FROM edit_audit_log WHERE sentence_id IN (SELECT s.id FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id JOIN lectures l ON p.lecture_id=l.id WHERE l.book_id=%s)",
        (book_id,))
    cursor.execute(
        "DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s))",
        (book_id,))
    cursor.execute(
        "DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)",
        (book_id,))

    # Keep existing lectures or create new ones if none exist
    # For now, distribute paragraphs evenly across existing lectures
    n_lecs = len(old_lectures) if old_lectures else 1
    if n_lecs == 0:
        cursor.execute("INSERT INTO lectures (book_id, title_de, order_index) VALUES (%s,%s,1) RETURNING id",
                       (book_id, ga_number))
        old_lectures = [(cursor.fetchone()[0], ga_number, None, None, 1)]
        n_lecs = 1

    # Distribute paragraphs to lectures proportionally
    n_paras = len(paragraphs)
    lec_assignments = []
    for i in range(n_lecs):
        start = i * n_paras // n_lecs
        end = (i + 1) * n_paras // n_lecs
        lec_assignments.append((old_lectures[i][0], paragraphs[start:end]))

    total_paras = 0
    total_sents = 0
    matched = 0

    for lec_id, lec_paras in lec_assignments:
        for pi, para_text in enumerate(lec_paras, 1):
            sentences = SENTENCE_BREAK.split(para_text)
            sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
            if not sentences:
                continue

            cursor.execute(
                "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
                (lec_id, pi))
            para_id = cursor.fetchone()[0]

            for si, sent_text in enumerate(sentences, 1):
                key = normalize(sent_text)
                zh = translations.get(key)
                if zh:
                    matched += 1
                cursor.execute(
                    "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s,%s,%s,%s)",
                    (para_id, si, sent_text, zh))
                total_sents += 1
            total_paras += 1

    return (total_paras, total_sents, matched), "ok"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("books", nargs="*", help="GA numbers to process (e.g. GA312)")
    parser.add_argument("--all", action="store_true", help="All books with .doc")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(DB)
    cursor = conn.cursor()

    # Get books to process
    if args.books:
        placeholders = ','.join(['%s'] * len(args.books))
        cursor.execute(f"SELECT id, ga_number FROM books WHERE ga_number IN ({placeholders}) ORDER BY ga_number", args.books)
    else:
        cursor.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
    books = cursor.fetchall()

    fixed = 0
    failed = 0
    for bid, ga in books:
        print(f"{ga}: ", end="", flush=True)
        result, reason = reimport_book(cursor, bid, ga, dry_run=args.dry_run)
        if result is None:
            print(f"SKIP ({reason})", flush=True)
            failed += 1
        else:
            paras, sents, matched = result
            rate = f"{matched}/{sents}" if sents > 0 else "0"
            print(f"{'DRY RUN: ' if args.dry_run else ''}{paras} paras, {sents} sents, {rate} translations matched", flush=True)
            fixed += 1

    if not args.dry_run and fixed > 0:
        conn.commit()
        print(f"\nDone. Fixed {fixed} books. {failed} skipped.", flush=True)
    elif args.dry_run:
        print(f"\nDRY RUN: {fixed} would be fixed. {failed} skipped.", flush=True)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
