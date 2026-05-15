#!/usr/bin/env python3
"""Re-group sentences into proper paragraphs using content-aware heuristics.

Paragraph breaks are detected by:
1. Transition words at sentence start (Erstens, Heute, Nun, Diese, etc.)
2. Maximum paragraph size (default 12 sentences)

Usage:
  python3 scripts/fix_paragraphs.py --dry-run
  python3 scripts/fix_paragraphs.py GA312
  python3 scripts/fix_paragraphs.py           # fix all
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

# Sentences starting with these patterns strongly indicate a new paragraph
PARA_START_PATTERNS = [
    # Ordinal/enumeration markers
    r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b',
    r'^[IVXLCDM]+\.\s',  # Roman numerals like "IV."
    r'^\d+\.\s',  # Numbered items like "1."
    # Topic shift markers
    r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Abschließend)\b',
    r'^(Dasjenige|Diejenige|Das ist|Dies ist|Dieser|Diese|Dieses)\b',
    r'^(Wenden wir uns|Gehen wir|Kommen wir|Sehen wir)\b',
    r'^(Ich möchte|Ich will|Ich werde)\b',
    # Contrast/transition
    r'^(Aber|Allein|Dagegen|Hingegen|Demgegenüber|Indessen|Jedoch)\b',
    r'^(Dem steht|Demgegenüber steht|Entgegen)\b',
    # Questions starting new sections
    r'^(Was ist|Wie ist|Worin|Wodurch|Warum|Weshalb|Wieso)\b',
    # Named entities at start (proper names with comma, common in academic lectures)
    r'^[A-ZÄÖÜ][a-zäöüß]+ [A-ZÄÖÜ][a-zäöüß]+[,:]',
]

MAX_SENTENCES = 12  # Maximum sentences per paragraph
MIN_SENTENCES = 2   # Minimum sentences before allowing a forced break


def is_paragraph_start(sentence_text: str) -> bool:
    """Check if a sentence likely starts a new paragraph."""
    text = sentence_text.strip()
    for pattern in PARA_START_PATTERNS:
        if re.match(pattern, text):
            return True
    return False


def regroup_lecture(cursor, lecture_id, dry_run=False):
    """Redistribute sentences into content-aware paragraphs."""
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    sentences = cursor.fetchall()

    total = len(sentences)
    if total == 0:
        return 0, 0, 0

    # Group sentences: break on detected paragraph starts, with max size limit
    groups = []
    current_group = []

    for (sid, text_de, text_zh) in sentences:
        # Start new paragraph if:
        # 1. We detect a paragraph start word AND have enough sentences in current group
        # 2. Current group has reached MAX_SENTENCES
        should_break = False
        if current_group and len(current_group) >= MIN_SENTENCES:
            if is_paragraph_start(text_de or ''):
                should_break = True
        if current_group and len(current_group) >= MAX_SENTENCES:
            should_break = True

        if should_break:
            groups.append(current_group)
            current_group = []

        current_group.append((sid, text_de, text_zh))

    if current_group:
        groups.append(current_group)

    # Merge very small groups into neighbors
    merged = []
    i = 0
    while i < len(groups):
        g = groups[i]
        if len(g) <= 2 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
        i += 1

    cursor.execute(
        "SELECT COUNT(*) FROM paragraphs WHERE lecture_id = %s", (lecture_id,)
    )
    old_paras = cursor.fetchone()[0]

    if dry_run:
        return old_paras, len(merged), total

    # Clear image references
    cursor.execute(
        "UPDATE lecture_images SET after_sentence_id = NULL, after_paragraph_id = NULL WHERE lecture_id = %s",
        (lecture_id,)
    )
    # Delete old paragraphs (cascades to sentences)
    cursor.execute("DELETE FROM paragraphs WHERE lecture_id = %s", (lecture_id,))

    # Insert new paragraphs
    for pi, group in enumerate(merged, 1):
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

    return old_paras, len(merged), total


def main():
    parser = argparse.ArgumentParser(description="Content-aware paragraph regrouping")
    parser.add_argument("ga_filter", nargs="*", help="GA numbers (e.g. GA312)")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-sents", type=int, default=MAX_SENTENCES)
    parser.add_argument("--min-ratio", type=int, default=30)
    args = parser.parse_args()

    max_sents = args.max_sents

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    conn.autocommit = False
    cursor = conn.cursor()

    try:
        where = ""
        params = []
        if args.ga_filter:
            where = "WHERE b.ga_number = ANY(%s)"
            params.append(args.ga_filter)

        cursor.execute(f"""
            SELECT b.id, b.ga_number, l.id, l.title_de
            FROM books b
            JOIN lectures l ON l.book_id = b.id
            {where}
            ORDER BY b.ga_number, l.order_index
        """, params)
        rows = cursor.fetchall()

        books = {}
        for (bid, ga, lid, ltitle) in rows:
            books.setdefault(bid, (ga, []))[1].append((lid, ltitle))

        grand_old = 0
        grand_new = 0
        grand_sents = 0
        fixed_lectures = 0

        for bid, (ga, lectures) in books.items():
            book_old = 0
            book_new = 0
            for lid, ltitle in lectures:
                old, new, total = regroup_lecture(cursor, lid, dry_run=args.dry_run)
                if old <= 1 and new <= 1 and total <= max_sents:
                    continue
                if total / max(old, 1) < args.min_ratio and old > 1:
                    continue

                book_old += old
                book_new += new
                grand_sents += total
                fixed_lectures += 1

                if args.dry_run:
                    avg = total / max(new, 1)
                    print(f"  {ga} lect {lid} \"{ltitle[:40]}\": {old}→{new} paras ({total} s, ~{avg:.1f}/para)", flush=True)

            grand_old += book_old
            grand_new += book_new
            if book_old > 0 and book_new != book_old:
                print(f"{ga}: {book_old}→{book_new} paragraphs ({'DRY RUN' if args.dry_run else 'FIXED'})", flush=True)

        if not args.dry_run and grand_old > 0:
            conn.commit()
            print(f"\nDone. {fixed_lectures} lectures: {grand_old}→{grand_new} paragraphs, {grand_sents} sentences.", flush=True)
        elif args.dry_run:
            print(f"\nDRY RUN: {fixed_lectures} lectures: {grand_old}→{grand_new} paragraphs, {grand_sents} sentences.", flush=True)
        else:
            print("No changes needed.", flush=True)

    except Exception as e:
        conn.rollback()
        import traceback
        print(f"ERROR: {e}", flush=True)
        traceback.print_exc()
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
