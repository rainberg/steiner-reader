#!/usr/bin/env python3
"""
Use .doc source to determine paragraph boundaries, then group existing
DB sentences to match. Preserves all translations.

For each lecture: extract paragraph sentence counts from .doc,
then redistribute DB sentences into that many paragraphs proportionally.
"""

import argparse, os, re, subprocess, sys, psycopg2

DB = "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
DOC_DIR = "/opt/steiner-reader/books/doc"

SENTENCE_BREAK = re.compile(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ"«„0-9])')

def normalize(text):
    text = text or ''
    text = text.replace('\xad', '').replace('­', '')
    for old, new in [('Ã¤','ä'),('Ã¶','ö'),('Ã¼','ü'),('ÃŸ','ß'),
                      ('Ã„','Ä'),('Ã–','Ö'),('Ãœ','Ü')]:
        text = text.replace(old, new)
    return re.sub(r'\s+', ' ', text).strip()


def get_doc_para_sizes(doc_path):
    """Extract paragraph sizes (sentence counts) from .doc file."""
    try:
        result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=120)
        content = result.stdout.decode('latin-1')
    except Exception:
        return None

    pages = content.split('\x0c')
    para_sizes = []

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
                if len(para) > 40:
                    sents = len(SENTENCE_BREAK.split(para))
                    if sents > 0:
                        para_sizes.append(max(1, sents))
                current = []
        if current:
            para = normalize(' '.join(current))
            if len(para) > 40:
                sents = len(SENTENCE_BREAK.split(para))
                if sents > 0:
                    para_sizes.append(max(1, sents))

    return para_sizes if para_sizes else None


def regroup_lecture(cur, lec_id, para_sizes):
    """Redistribute DB sentences into paragraphs matching source sizes."""
    # Get all sentences for this lecture
    cur.execute("""
        SELECT s.id, s.text_de, s.text_zh FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lec_id,))
    sents = cur.fetchall()
    db_total = len(sents)
    if db_total < 10:
        return 0

    # Scale para_sizes to match DB sentence count
    doc_total = sum(para_sizes)
    if doc_total == 0:
        return 0
    scale = db_total / doc_total

    # Build groups
    groups = []
    pos = 0
    for size in para_sizes:
        n = max(1, round(size * scale))
        n = min(n, db_total - pos)
        if n > 0:
            groups.append(sents[pos:pos + n])
            pos += n
        if pos >= db_total:
            break

    # Add any remaining sentences to last group
    if pos < db_total:
        groups[-1].extend(sents[pos:])

    if len(groups) <= 1:
        return 0

    # Save image refs
    cur.execute("UPDATE lecture_images SET after_sentence_id=NULL, after_paragraph_id=NULL WHERE lecture_id=%s", (lec_id,))

    # Delete old paragraphs
    cur.execute("DELETE FROM paragraphs WHERE lecture_id = %s", (lec_id,))

    # Create new paragraphs and UPDATE sentences
    for pi, group in enumerate(groups, 1):
        cur.execute("INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id", (lec_id, pi))
        pid = cur.fetchone()[0]
        for si, (sid, td, tz) in enumerate(group, 1):
            cur.execute("UPDATE sentences SET paragraph_id=%s, order_index=%s WHERE id=%s", (pid, si, sid))

    return len(groups)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("books", nargs="*")
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(DB)
    cur = conn.cursor()

    if args.books:
        placeholders = ','.join(['%s'] * len(args.books))
        cur.execute(f"SELECT id, ga_number FROM books WHERE ga_number IN ({placeholders}) ORDER BY ga_number", args.books)
    else:
        cur.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
    books = cur.fetchall()

    fixed = 0
    for bid, ga in books:
        doc_path = os.path.join(DOC_DIR, f"{ga}.doc")
        if not os.path.exists(doc_path):
            continue

        print(f"{ga}: ", end="", flush=True)
        para_sizes = get_doc_para_sizes(doc_path)
        if not para_sizes:
            print("no doc paras found", flush=True)
            continue

        # Get lectures and assign each a portion of the paragraph sizes
        cur.execute("SELECT id, title_de FROM lectures WHERE book_id=%s ORDER BY order_index", (bid,))
        lectures = cur.fetchall()
        if not lectures:
            print("no lectures", flush=True)
            continue

        total_doc_paras = len(para_sizes)
        n_lecs = len(lectures)
        book_changed = 0

        for li, (lid, ltitle) in enumerate(lectures):
            start = li * total_doc_paras // n_lecs
            end = (li + 1) * total_doc_paras // n_lecs
            lec_para_sizes = para_sizes[start:end]
            if not lec_para_sizes:
                continue

            n = regroup_lecture(cur, lid, lec_para_sizes)
            if n > 0:
                book_changed += n

        if args.dry_run:
            print(f"DRY RUN: {total_doc_paras} doc paras -> {book_changed} DB groups", flush=True)
        else:
            print(f"{total_doc_paras} doc paras -> {book_changed} DB groups", flush=True)
            fixed += 1

    if not args.dry_run and fixed > 0:
        conn.commit()
        print(f"\nDone. {fixed} books fixed.", flush=True)
    elif args.dry_run:
        print(f"\nDRY RUN: {fixed} books would be fixed.", flush=True)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
