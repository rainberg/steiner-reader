#!/usr/bin/env python3
"""
Fix broken German sentence segmentation caused by ordinal abbreviations.

Pattern: "Im 17." + "Jahrhundert" -> "Im 17. Jahrhundert"
Also handles: Auflage, Band, Teil, Jahrgang, Seite, etc.

This script is idempotent and can be re-run safely.
Run after importing any new book to fix ordinal-related segmentation errors.

Usage:
  python3 scripts/fix_ordinal_sentences.py                  # Fix all books
  python3 scripts/fix_ordinal_sentences.py --book GA034     # Fix specific book
  python3 scripts/fix_ordinal_sentences.py --dry-run        # Preview only
"""

import argparse
import re
import sys

import psycopg2

DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "Dd08120@"

ORDINAL_FOLLOW_WORDS = re.compile(
    r'^(Jahrhundert|Jahrhunderts|Jahres|Jahrgang|Jahrgangs|Jahrestag|Jahrestages'
    r'|Jahr|Auflage|Auflage\)|Band|Bandes|Bande|Bands'
    r'|Teil|Teils|Kapitel|Abschnitt|Seite|S\.|Nr\.'
    r'|Tausend|Mitte|Ende|Anfang'
    r'|Dezember|Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November)'
)

ENDS_WITH_ORDINAL = re.compile(r'\d+\.$')
STANDALONE_ORDINAL = re.compile(r'^\d+\.$')
STARTS_WITH_LOWER = re.compile(r'^[a-zäöüß]')


def find_merge_pairs_forward(cursor, book_filter=None):
    """Find sentence pairs where current_text ends with number+period,
    next_text starts with lowercase or ordinal-following word.
    """
    where_clause = ""
    params = []
    if book_filter:
        where_clause = "AND b.ga_number = %s"
        params = [book_filter]

    cursor.execute(f"""
        WITH broken AS (
            SELECT s.id, s.text_de, s.order_index, s.paragraph_id,
                   LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_text,
                   LEAD(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_id,
                   LEAD(s.order_index) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_order
            FROM sentences s
            JOIN paragraphs p ON s.paragraph_id = p.id
            JOIN lectures l ON p.lecture_id = l.id
            JOIN books b ON l.book_id = b.id
            WHERE 1=1 {where_clause}
        )
        SELECT b.id, b.text_de, b.next_id, b.next_text, b.paragraph_id,
               b.order_index, b.next_order
        FROM broken b
        WHERE b.text_de ~ '\d+\.$'
          AND b.text_de !~ '^\d+\.$'
          AND b.next_text IS NOT NULL
          AND (
            b.next_text ~ '^[a-zäöüß]'
            OR b.next_text ~ '^(Jahrhundert|Jahrhunderts|Jahres|Jahrgang|Jahrgangs|Jahrestag|Jahrestages|Jahr|Auflage|Auflage\)|Band|Bandes|Bande|Bands|Teil|Teils|Kapitel|Abschnitt|Seite|S\.|Nr\.|Tausend|Mitte|Ende|Anfang|Dezember|Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November)'
          )
    """, params)

    return cursor.fetchall()


def find_standalone_ordinals(cursor, book_filter=None):
    """Find standalone ordinal (like "17." alone) that should merge with previous.
    """
    where_clause = ""
    params = []
    if book_filter:
        where_clause = "AND b.ga_number = %s"
        params = [book_filter]

    cursor.execute(f"""
        WITH broken AS (
            SELECT s.id, s.text_de, s.order_index, s.paragraph_id,
                   LAG(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS prev_text,
                   LAG(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS prev_id
            FROM sentences s
            JOIN paragraphs p ON s.paragraph_id = p.id
            JOIN lectures l ON p.lecture_id = l.id
            JOIN books b ON l.book_id = b.id
            WHERE s.text_de ~ '^\d+\.$'
              {where_clause}
        )
        SELECT b.id, b.text_de, b.prev_id, b.prev_text, b.paragraph_id
        FROM broken b
        WHERE b.prev_id IS NOT NULL
          AND b.prev_text IS NOT NULL
          AND (
            b.prev_text ~ '\d+\.$'
            OR b.prev_text ~ '[a-zäöüß]\s*$'
            OR b.prev_text ~ '(Band|Teil|Auflage|Jahrgang|Jahrhundert|Jahr|Kapitel|Abschnitt|Seite|S\.|Nr\.)\s*$'
          )
    """, params)

    return cursor.fetchall()


def fix_sentences(conn, book_filter=None, dry_run=False):
    cursor = conn.cursor()

    forward_pairs = find_merge_pairs_forward(cursor, book_filter)
    standalone_pairs = find_standalone_ordinals(cursor, book_filter)

    print(f"Forward merge pairs (current ends with ordinal + next starts with keyword): {len(forward_pairs)}")
    print(f"Standalone ordinal merge pairs (standalone number + previous): {len(standalone_pairs)}")

    if dry_run:
        print("\n--- DRY RUN: Preview of changes ---")
        for row in forward_pairs[:10]:
            cur_id, cur_text, next_id, next_text, para_id, cur_order, next_order = row
            print(f"  Merge: [{cur_text}] + [{next_text}]")
        if len(forward_pairs) > 10:
            print(f"  ... and {len(forward_pairs) - 10} more forward merges")

        for row in standalone_pairs[:10]:
            cur_id, cur_text, prev_id, prev_text, para_id = row
            print(f"  Merge: [{prev_text}] + [{cur_text}]")
        if len(standalone_pairs) > 10:
            print(f"  ... and {len(standalone_pairs) - 10} more standalone merges")
        return

    total_merged = 0
    translations_cleared = 0

    for row in forward_pairs:
        cur_id, cur_text, next_id, next_text, para_id, cur_order, next_order = row
        merged_text = f"{cur_text} {next_text}"
        cursor.execute("UPDATE sentences SET text_de = %s, text_zh = NULL WHERE id = %s", (merged_text, cur_id))
        cursor.execute("DELETE FROM sentences WHERE id = %s", (next_id,))
        total_merged += 1

    for row in standalone_pairs:
        cur_id, cur_text, prev_id, prev_text, para_id = row
        merged_text = f"{prev_text} {cur_text}"
        cursor.execute("UPDATE sentences SET text_de = %s, text_zh = NULL WHERE id = %s", (merged_text, prev_id))
        cursor.execute("DELETE FROM sentences WHERE id = %s", (cur_id,))
        total_merged += 1

    conn.commit()
    print(f"\nFixed {total_merged} broken sentence pairs.")

    remaining_forward = find_merge_pairs_forward(cursor, book_filter)
    remaining_standalone = find_standalone_ordinals(cursor, book_filter)
    print(f"Remaining issues: {len(remaining_forward)} forward, {len(remaining_standalone)} standalone")

    cursor.close()


def main():
    parser = argparse.ArgumentParser(description="Fix German ordinal sentence segmentation errors")
    parser.add_argument("--book", help="Fix specific book only (e.g., GA034)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--db-host", default=DB_HOST)
    parser.add_argument("--db-port", type=int, default=DB_PORT)
    parser.add_argument("--db-name", default=DB_NAME)
    parser.add_argument("--db-user", default=DB_USER)
    parser.add_argument("--db-password", default=DB_PASSWORD)
    args = parser.parse_args()

    conn = psycopg2.connect(
        host=args.db_host, port=args.db_port,
        dbname=args.db_name, user=args.db_user, password=args.db_password
    )

    try:
        fix_sentences(conn, book_filter=args.book, dry_run=args.dry_run)
    except Exception as e:
        conn.rollback()
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
