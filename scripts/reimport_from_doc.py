#!/usr/bin/env python3
"""
Re-import a book from .doc source file with proper paragraph structure.
Matches existing translations by text similarity after re-import.

Usage: python3 scripts/reimport_from_doc.py GA312
"""

import argparse
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

DATE_PATTERN = re.compile(r'(\d{1,2})\.\s*(Januar|Februar|März|April|Mai|Juni|Juli|'
                          r'August|September|Oktober|November|Dezember)\s*(\d{4})')

GERMAN_MONTHS = {
    'Januar':1,'Februar':2,'März':3,'April':4,'Mai':5,'Juni':6,
    'Juli':7,'August':8,'September':9,'Oktober':10,'November':11,'Dezember':12
}

def parse_german_date(text):
    """Parse German date like '21. März 1920' into ISO format."""
    m = DATE_PATTERN.search(text)
    if m:
        day, month_de, year = m.group(1), m.group(2), m.group(3)
        month = GERMAN_MONTHS.get(month_de, 1)
        return f"{year}-{month:02d}-{int(day):02d}"
    return None

SENTENCE_BREAK = re.compile(r'(?<=[.!?])(?<!\d\.)(?<!\d\d\.)\s+(?=[A-ZÄÖÜ"«„0-9])')


def normalize(text):
    text = text or ''
    text = text.replace('\xad', '').replace('­', '')
    for old, new in [('Ã¤','ä'),('Ã¶','ö'),('Ã¼','ü'),('ÃŸ','ß'),
                      ('Ã„','Ä'),('Ã–','Ö'),('Ãœ','Ü')]:
        text = text.replace(old, new)
    return re.sub(r'\s+', ' ', text).strip()


def parse_doc(doc_path):
    """Parse .doc into structured lectures with paragraphs and sentences."""
    result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=120)
    content = result.stdout.decode('latin-1')
    pages = content.split('\x0c')

    lectures = {}
    current_lecture = None
    buffered_paras = []  # paras before lecture detection starts

    for pi, page_text in enumerate(pages):
        if pi < 3:
            continue

        lines = page_text.strip().split('\n')
        first_line = lines[0].strip() if lines else ''

        if 'INHALT' in page_text[:200]:
            continue

        header_match = LECTURE_PATTERN.match(first_line)
        if header_match:
            current_lecture = LECTURE_ORDINALS.get(header_match.group(1), 0)
            # Extract date and location from header line
            rest = first_line[header_match.end():].strip()
            date_str = parse_german_date(rest)
            if date_str:
                # Location is text before the date pattern
                m = DATE_PATTERN.search(rest)
                location = rest[:m.start()].strip(', ') if m else rest
            else:
                location = rest

            lectures[current_lecture] = {
                'order': current_lecture,
                'title_de': first_line,
                'location': location if location else None,
                'date': date_str,
                'paragraphs': []
            }
            lines = lines[1:]

        if current_lecture is None:
            continue

        # Extract paragraphs from remaining lines
        cur_para = []
        for line in lines:
            s = line.strip()
            if s:
                cur_para.append(s)
            elif cur_para:
                para_text = normalize(' '.join(cur_para))
                if len(para_text) > 40:
                    sentences = SENTENCE_BREAK.split(para_text)
                    sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
                    if sentences:
                        lectures[current_lecture]['paragraphs'].append(sentences)
                cur_para = []
        if cur_para:
            para_text = normalize(' '.join(cur_para))
            if len(para_text) > 40:
                sentences = SENTENCE_BREAK.split(para_text)
                sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
                if sentences:
                    lectures[current_lecture]['paragraphs'].append(sentences)

    return lectures


def save_existing_translations(cursor, book_id):
    """Save existing translations keyed by normalized German text."""
    cursor.execute("""
        SELECT s.text_de, s.text_zh
        FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        JOIN lectures l ON p.lecture_id = l.id
        WHERE l.book_id = %s AND s.text_zh IS NOT NULL AND s.text_zh != ''
    """, (book_id,))
    translations = {}
    for text_de, text_zh in cursor.fetchall():
        key = normalize(text_de)
        if key and text_zh:
            translations[key] = text_zh
    return translations


def reimport_book(cursor, book_id, ga_number, doc_path, translations, dry_run=False):
    """Re-import a book from .doc, matching existing translations."""
    parsed = parse_doc(doc_path)

    if not parsed:
        print(f"  No lectures found in {doc_path}")
        return False

    print(f"  Parsed {len(parsed)} lectures from .doc")

    if dry_run:
        for order in sorted(parsed.keys()):
            lec = parsed[order]
            total_sents = sum(len(p) for p in lec['paragraphs'])
            print(f"    Lecture {order}: {len(lec['paragraphs'])} paras, {total_sents} sents - {lec['title_de'][:60]}")
        return True

    # Delete existing content for this book
    cursor.execute("DELETE FROM lecture_images WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,))
    cursor.execute("DELETE FROM contributions WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,))
    cursor.execute("DELETE FROM lecture_access WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,))
    cursor.execute("DELETE FROM edit_audit_log WHERE sentence_id IN (SELECT s.id FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id JOIN lectures l ON p.lecture_id=l.id WHERE l.book_id=%s)", (book_id,))
    cursor.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s))", (book_id,))
    cursor.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,))
    cursor.execute("DELETE FROM lectures WHERE book_id=%s", (book_id,))

    # Update book metadata
    cursor.execute("UPDATE books SET pdf_filename=%s WHERE id=%s", (f"{ga_number}.pdf", book_id))

    total_paras = 0
    total_sents = 0
    matched_translations = 0

    for order in sorted(parsed.keys()):
        lec = parsed[order]
        cursor.execute(
            "INSERT INTO lectures (book_id, title_de, lecture_date, location, order_index, level) VALUES (%s,%s,%s,%s,%s,'lecture') RETURNING id",
            (book_id, lec['title_de'], lec.get('date'), lec.get('location'), order)
        )
        lec_id = cursor.fetchone()[0]

        for pi, sentences in enumerate(lec['paragraphs'], 1):
            cursor.execute(
                "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
                (lec_id, pi)
            )
            para_id = cursor.fetchone()[0]
            total_paras += 1

            for si, sent_text in enumerate(sentences, 1):
                sent_text = sent_text.strip()
                if len(sent_text) < 3:
                    continue
                key = normalize(sent_text)
                text_zh = translations.get(key)
                if text_zh:
                    matched_translations += 1

                cursor.execute(
                    "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s,%s,%s,%s)",
                    (para_id, si, sent_text, text_zh)
                )
                total_sents += 1

    print(f"  Re-imported: {total_paras} paragraphs, {total_sents} sentences")
    print(f"  Translations matched: {matched_translations}/{total_sents}")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ga_filter", nargs="+")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    doc_dir = "/opt/steiner-reader/books/doc"

    try:
        for ga in args.ga_filter:
            doc_path = f"{doc_dir}/{ga}.doc"
            if not __import__('os').path.exists(doc_path):
                print(f"{ga}: .doc not found at {doc_path}, skipping")
                continue

            cursor.execute("SELECT id FROM books WHERE ga_number=%s", (ga,))
            row = cursor.fetchone()
            if not row:
                print(f"{ga}: not in DB, skipping")
                continue
            book_id = row[0]

            print(f"{ga}: saving translations...", flush=True)
            translations = save_existing_translations(cursor, book_id)
            print(f"  {len(translations)} translations saved", flush=True)

            ok = reimport_book(cursor, book_id, ga, doc_path, translations, dry_run=args.dry_run)
            if ok and not args.dry_run:
                conn.commit()
                print(f"  Committed.", flush=True)

    except Exception as e:
        conn.rollback()
        import traceback
        print(f"ERROR: {e}")
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
