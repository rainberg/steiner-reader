#!/usr/bin/env python3
"""Regroup sentences using exact paragraph boundaries from source .doc file.

Matches paragraph start/end text from .doc to corresponding DB sentences,
then groups sentences precisely according to the original document structure.
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

LECTURE_PATTERN = re.compile(
    r'^(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|'
    r'ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWÖLFTER|DREIZEHNTER|VIERZEHNTER|'
    r'FÜNFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|ZWANZIGSTER)'
    r'\s+VORTRAG'
)

LECTURE_ORDINALS = {
    'ERSTER':1,'ZWEITER':2,'DRITTER':3,'VIERTER':4,'FÜNFTER':5,
    'SECHSTER':6,'SIEBENTER':7,'ACHTER':8,'NEUNTER':9,'ZEHNTER':10,
    'ELFTER':11,'ZWÖLFTER':12,'DREIZEHNTER':13,'VIERZEHNTER':14,
    'FÜNFZEHNTER':15,'SECHZEHNTER':16,'SIEBZEHNTER':17,'ACHTZEHNTER':18,
    'NEUNZEHNTER':19,'ZWANZIGSTER':20
}


def normalize(text):
    """Normalize text for comparison: collapse whitespace, remove soft hyphens, unicode chars."""
    text = text.replace('\xad', '')  # soft hyphen
    text = text.replace('Ã¤', 'ä').replace('Ã¶', 'ö').replace('Ã¼', 'ü')
    text = text.replace('ÃŸ', 'ß').replace('Ã„', 'Ä').replace('Ã–', 'Ö').replace('Ãœ', 'Ü')
    text = text.replace('Â«', '«').replace('Â»', '»')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_paragraphs_from_doc(doc_path):
    """Extract paragraphs from .doc, grouped by lecture.
    Returns: {lecture_order: [(para_text, start_60_chars, end_60_chars), ...]}
    """
    result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=60)
    content = result.stdout.decode('latin-1')

    pages = content.split('\x0c')
    lecture_data = {}

    for pi, page_text in enumerate(pages):
        if pi < 3:
            continue

        lines = page_text.strip().split('\n')
        first_line = lines[0].strip() if lines else ''

        if 'INHALT' in page_text[:200] or 'HINWEISE' in page_text[:200]:
            continue

        header_match = LECTURE_PATTERN.match(first_line)
        current_lecture = None

        if header_match:
            current_lecture = LECTURE_ORDINALS.get(header_match.group(1), 0)
            if current_lecture not in lecture_data:
                lecture_data[current_lecture] = []
            lines = lines[1:]
        elif lecture_data:
            current_lecture = max(lecture_data.keys())
        else:
            continue

        if not current_lecture or current_lecture > 20:
            continue

        current_para = []
        for line in lines:
            s = line.strip()
            if s:
                current_para.append(s)
            else:
                if current_para:
                    para_text = normalize(' '.join(current_para))
                    if len(para_text) > 50:
                        start = para_text[:60]
                        end = para_text[-60:]
                        lecture_data[current_lecture].append((para_text, start, end))
                    current_para = []
        if current_para:
            para_text = normalize(' '.join(current_para))
            if len(para_text) > 50:
                start = para_text[:60]
                end = para_text[-60:]
                lecture_data[current_lecture].append((para_text, start, end))

    return lecture_data


def find_exact_boundaries(cursor, lecture_id, doc_paragraphs):
    """Find exact paragraph boundaries by matching start/end text to DB sentences.

    Handles the case where DB sentences may not be perfectly split — paragraph
    boundaries might fall in the middle of a DB sentence. In that case, uses
    the closest sentence boundary.

    Returns list of (start_sentence_index, end_sentence_index) pairs.
    """
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    db_sentences = cursor.fetchall()

    if not db_sentences:
        return []

    # Build a concatenated text of all DB sentences, tracking sentence boundaries
    full_text = ""
    sent_positions = []  # (start_char, end_char) for each sentence
    for sid, text_de, text_zh in db_sentences:
        s_norm = normalize(text_de or '')
        if s_norm:
            start = len(full_text)
            full_text += s_norm + " "
            end = len(full_text) - 1
            sent_positions.append((start, end))

    boundaries = []
    search_pos = 0  # character position in full_text

    for (para_text, doc_start, doc_end) in doc_paragraphs:
        # Find paragraph start: look for first ~25 chars of paragraph in full_text
        start_key = doc_start[:25]
        start_idx = full_text.find(start_key, search_pos)
        if start_idx < 0:
            # Try shorter key
            start_key = doc_start[:15]
            start_idx = full_text.find(start_key, search_pos)
        if start_idx < 0:
            continue

        # Find paragraph end: look for last ~30 chars
        end_key = doc_end[-30:]
        end_idx = full_text.find(end_key, start_idx)
        if end_idx < 0:
            # Try shorter
            end_key = doc_end[-20:]
            end_idx = full_text.find(end_key, start_idx)
        if end_idx < 0:
            continue

        # Map character positions to sentence indices
        start_sent = None
        end_sent = None
        for si, (s_start, s_end) in enumerate(sent_positions):
            if start_idx <= s_end and start_sent is None:
                start_sent = si
            if end_idx <= s_end and end_sent is None:
                end_sent = si
            if start_sent is not None and end_sent is not None:
                break

        if start_sent is not None and end_sent is not None:
            boundaries.append((start_sent, end_sent))
            search_pos = end_idx + len(end_key)

    return boundaries


def regroup_lecture_exact(cursor, lecture_id, boundaries, dry_run=False):
    """Regroup DB sentences using exact paragraph boundaries."""
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    db_sentences = cursor.fetchall()
    db_total = len(db_sentences)

    if db_total == 0 or not boundaries:
        return 0, 0, 0

    # Build groups from boundaries
    groups = []
    for (start_idx, end_idx) in boundaries:
        if start_idx < len(db_sentences) and end_idx < len(db_sentences):
            group = db_sentences[start_idx:end_idx + 1]
            if group:
                groups.append(group)

    # Handle unassigned sentences (shouldn't happen if matching is perfect)
    if groups:
        last_end = boundaries[-1][1]
        if last_end + 1 < len(db_sentences):
            groups[-1].extend(db_sentences[last_end + 1:])
        if boundaries[0][0] > 0:
            groups[0] = db_sentences[:boundaries[0][0]] + groups[0]

    cursor.execute(
        "SELECT COUNT(*) FROM paragraphs WHERE lecture_id = %s", (lecture_id,)
    )
    old_paras = cursor.fetchone()[0]
    new_paras = len(groups)

    if dry_run or new_paras <= 1:
        return old_paras, new_paras, db_total

    # Apply
    cursor.execute(
        "UPDATE lecture_images SET after_sentence_id = NULL, after_paragraph_id = NULL WHERE lecture_id = %s",
        (lecture_id,)
    )
    cursor.execute("DELETE FROM paragraphs WHERE lecture_id = %s", (lecture_id,))

    for pi, group in enumerate(groups, 1):
        cursor.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s, %s) RETURNING id",
            (lecture_id, pi)
        )
        para_id = cursor.fetchone()[0]
        for si, (sid, text_de, text_zh) in enumerate(group, 1):
            cursor.execute(
                "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s, %s, %s, %s)",
                (para_id, si, text_de, text_zh)
            )

    return old_paras, new_paras, db_total


def main():
    parser = argparse.ArgumentParser(description="Exact paragraph regrouping from .doc")
    parser.add_argument("ga_filter", nargs="*")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    doc_dir = "/opt/steiner-reader/books/doc"
    doc_files = {}
    if os.path.isdir(doc_dir):
        for f in os.listdir(doc_dir):
            m = re.match(r'GA(\d+)\.doc', f)
            if m:
                doc_files[f"GA{m.group(1)}"] = os.path.join(doc_dir, f)

    ga_list = args.ga_filter if args.ga_filter else sorted(doc_files.keys())

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        total_fixed = 0
        for ga in sorted(ga_list):
            doc_path = doc_files.get(ga)
            if not doc_path:
                continue

            print(f"{ga}: extracting from .doc...", end=' ', flush=True)
            doc_structure = extract_paragraphs_from_doc(doc_path)
            if not doc_structure:
                print("no paragraphs found")
                continue
            print(f"{sum(len(v) for v in doc_structure.values())} paragraphs in {len(doc_structure)} lectures")

            cursor.execute("SELECT id FROM books WHERE ga_number = %s", (ga,))
            book = cursor.fetchone()
            if not book:
                continue
            book_id = book[0]

            cursor.execute("""
                SELECT id, order_index, title_de FROM lectures
                WHERE book_id = %s ORDER BY order_index
            """, (book_id,))
            db_lectures = cursor.fetchall()

            book_old = 0
            book_new = 0
            for lid, db_order, ltitle in db_lectures:
                doc_paras = doc_structure.get(db_order)
                if not doc_paras:
                    continue

                boundaries = find_exact_boundaries(cursor, lid, doc_paras)
                if len(boundaries) < 2:
                    continue  # couldn't match enough boundaries

                old, new, total = regroup_lecture_exact(cursor, lid, boundaries, dry_run=args.dry_run)
                book_old += old
                book_new += new

                if args.dry_run:
                    print(f"  lect {db_order}: {old}→{new} paras ({total}s, matched {len(boundaries)}/{len(doc_paras)} boundaries)")
                else:
                    print(f"  lect {db_order} \"{ltitle[:30]}\": {old}→{new} paras", flush=True)

            if book_old > 0 and book_new != book_old:
                total_fixed += 1
                print(f"  => {ga}: {book_old}→{book_new} paragraphs ({'DRY RUN' if args.dry_run else 'FIXED'})", flush=True)

        if not args.dry_run and total_fixed > 0:
            conn.commit()
            print(f"\nDone. {total_fixed} books fixed.")
        elif args.dry_run:
            print(f"\nDRY RUN: {total_fixed} books would be fixed.")
        else:
            print("No changes.")

    except Exception as e:
        conn.rollback()
        import traceback
        print(f"ERROR: {e}")
        traceback.print_exc()
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
