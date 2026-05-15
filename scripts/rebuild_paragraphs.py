#!/usr/bin/env python3
"""
Exact paragraph boundary extraction from source files and DB alignment.

Pipeline per book:
1. Find best source file (DOC > PDF)
2. Extract text with paragraph structure
3. Detect document format (lecture-based, chapter-based, etc.)
4. Match extracted paragraphs to DB sentences using text alignment
5. Apply exact paragraph regrouping
6. Verify result

Usage:
  python3 scripts/rebuild_paragraphs.py GA312              # single book
  python3 scripts/rebuild_paragraphs.py --dry-run GA312    # preview
  python3 scripts/rebuild_paragraphs.py --all --dry-run    # all books preview
  python3 scripts/rebuild_paragraphs.py --all              # all books
"""

import argparse
import difflib
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

# ── Text normalization for comparison ──────────────────────────

def normalize(text):
    """Aggressive normalization for text comparison."""
    text = text or ''
    # Fix latin-1 double-encoded chars from catdoc
    for old, new in [('Ã¤','ä'),('Ã¶','ö'),('Ã¼','ü'),('ÃŸ','ß'),
                      ('Ã„','Ä'),('Ã–','Ö'),('Ãœ','Ü'),
                      ('Ã©','é'),('Ã¨','è'),('Ãª','ê')]:
        text = text.replace(old, new)
    text = text.replace('\xad', '')  # soft hyphen
    text = text.replace('­', '')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ── Source file inventory ─────────────────────────────────────

def find_source_files(ga_number):
    """Find available source files for a GA number.
    Returns dict of format -> path, prioritized DOC > PDF.
    """
    sources = {}
    doc_dir = "/opt/steiner-reader/books/doc"
    uploads_dir = "/opt/steiner-reader/uploads"

    # Check .doc
    doc_path = os.path.join(doc_dir, f"{ga_number}.doc")
    if os.path.exists(doc_path):
        sources['doc'] = doc_path

    # Check uploaded PDFs
    for f in os.listdir(uploads_dir) if os.path.isdir(uploads_dir) else []:
        if f.startswith(ga_number) or f"{ga_number}_" in f or f"{ga_number}." in f:
            sources['pdf'] = os.path.join(uploads_dir, f)
            break

    # Check for epub
    epub_dir = "/opt/steiner-reader/books/epub"
    epub_path = os.path.join(epub_dir, f"{ga_number}.epub") if os.path.isdir(epub_dir) else ""
    if os.path.exists(epub_path):
        sources['epub'] = epub_path

    return sources


# ── DOC extraction ─────────────────────────────────────────────

def extract_doc_paragraphs(doc_path):
    """Extract all paragraphs from .doc via catdoc.
    Paragraphs are text blocks separated by blank lines.
    Returns full text and list of (start_char, end_char, text).
    """
    try:
        result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=60)
        content = result.stdout.decode('latin-1')
    except Exception as e:
        print(f"    catdoc failed: {e}", file=sys.stderr)
        return "", []

    pages = content.split('\x0c')
    all_paragraphs = []
    full_text = ""

    for page_text in pages:
        lines = page_text.split('\n')
        current_para = []
        for line in lines:
            stripped = line.strip()
            if stripped:
                current_para.append(stripped)
            else:
                if current_para:
                    para_text = normalize(' '.join(current_para))
                    if len(para_text) > 30:
                        start = len(full_text)
                        full_text += para_text + "\n"
                        end = len(full_text) - 1
                        all_paragraphs.append((start, end, para_text))
                    current_para = []
        if current_para:
            para_text = normalize(' '.join(current_para))
            if len(para_text) > 30:
                start = len(full_text)
                full_text += para_text + "\n"
                end = len(full_text) - 1
                all_paragraphs.append((start, end, para_text))

    return full_text, all_paragraphs


# ── PDF extraction ─────────────────────────────────────────────

def extract_pdf_paragraphs(pdf_path):
    """Extract text from PDF with page-level structure."""
    try:
        import pdfplumber
    except ImportError:
        print("    pdfplumber not available", file=sys.stderr)
        return "", []

    full_text = ""
    all_paragraphs = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            # Split page text into paragraphs (double newlines)
            paras = re.split(r'\n\s*\n', text)
            for para_text in paras:
                para_text = normalize(para_text)
                if len(para_text) > 30:
                    start = len(full_text)
                    full_text += para_text + "\n"
                    end = len(full_text) - 1
                    all_paragraphs.append((start, end, para_text))

    return full_text, all_paragraphs


# ── DB sentence retrieval ──────────────────────────────────────

def get_lecture_sentences(cursor, lecture_id):
    """Get all sentences for a lecture, ordered."""
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    return cursor.fetchall()


def build_sentence_index(sentences):
    """Build concatenated text and sentence boundaries for matching."""
    full_text = ""
    boundaries = []  # [(start, end, sid)]
    for sid, text_de, text_zh in sentences:
        text = normalize(text_de)
        if text:
            start = len(full_text)
            full_text += text + " "
            end = len(full_text) - 1
            boundaries.append((start, end, sid, text_de, text_zh))
    return full_text, boundaries


# ── Boundary matching ──────────────────────────────────────────

def match_paragraphs_to_sentences(source_paras, sent_text, sent_boundaries):
    """Match source paragraphs to DB sentences using text alignment.

    For each source paragraph, finds the range of DB sentences that
    contain its text. Uses start-key and end-key matching.

    Returns list of (first_sentence_idx, last_sentence_idx) pairs.
    """
    if not source_paras or not sent_boundaries:
        return []

    matches = []
    search_start = 0

    for (p_start, p_end, para_text) in source_paras:
        if len(para_text) < 30:
            continue

        # Find paragraph in sent_text
        # Use the first 25 and last 25 chars as keys
        start_key = para_text[:25]
        end_key = para_text[-25:]

        # Find start
        pos = sent_text.find(start_key, search_start)
        if pos < 0:
            # Try shorter key
            start_key = para_text[:15]
            pos = sent_text.find(start_key, search_start)
        if pos < 0:
            continue

        # Find end
        end_pos = sent_text.find(end_key, pos)
        if end_pos < 0:
            end_key = para_text[-15:]
            end_pos = sent_text.find(end_key, pos)
        if end_pos < 0:
            continue

        # Map character positions to sentence indices
        first_sent = None
        last_sent = None
        for idx, (s_start, s_end, sid, t_de, t_zh) in enumerate(sent_boundaries):
            if pos < s_end and first_sent is None:
                first_sent = idx
            if end_pos < s_end and last_sent is None:
                last_sent = idx
            if first_sent is not None and last_sent is not None:
                break

        if first_sent is not None and last_sent is not None:
            matches.append((first_sent, last_sent))
            search_start = end_pos + len(end_key)

    return matches


# ── Apply regrouping ──────────────────────────────────────────

def apply_regrouping(cursor, lecture_id, sentence_data, matches, dry_run=False):
    """Apply paragraph regrouping based on matched boundaries.

    Includes ALL sentences: fill gaps between matched boundaries and
    handle sentences before first / after last boundary.
    """
    if not matches or not sentence_data:
        return 0, 0, 0

    # Sort matches and fill gaps
    matches = sorted(matches, key=lambda m: m[0])
    total_sents = len(sentence_data)

    groups = []
    used_flags = [False] * total_sents

    for (first, last) in matches:
        if first < total_sents and last < total_sents:
            group = sentence_data[first:last + 1]
            if group:
                groups.append(group)
                for i in range(first, last + 1):
                    used_flags[i] = True

    # Handle unassigned sentences: distribute to nearest matched groups
    for i in range(total_sents):
        if not used_flags[i]:
            # Before first match: prepend to first group
            if i < matches[0][0]:
                groups[0] = [sentence_data[i]] + groups[0]
            # After last match: append to last group
            elif i > matches[-1][1]:
                groups[-1].append(sentence_data[i])
            # Between matches: append to previous group
            else:
                for gi in range(len(matches) - 1):
                    if matches[gi][1] < i < matches[gi + 1][0]:
                        groups[gi].append(sentence_data[i])
                        break

    if not groups:
        return 0, 0, 0

    # Sub-split oversized paragraphs (>30 sentences) using content signals
    PARA_START = re.compile(
        r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b|'
        r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Dasjenige|Diejenige)\b|'
        r'^(Das ist|Dieser|Diese|Dieses|Aber|Allein|Dagegen|Hingegen|Dem steht)\b|'
        r'^(Was ist|Wie ist|Worin|Wodurch|Warum)\b'
    )

    new_groups = []
    for group in groups:
        if len(group) > 30:
            sub = []; cur = []
            for sd in group:
                text_de = normalize(sd[1] or '')
                if len(cur) >= 3 and PARA_START.match(text_de):
                    sub.append(cur); cur = []
                cur.append(sd)
            if cur: sub.append(cur)
            new_groups.extend(sub)
        else:
            new_groups.append(group)
    groups = new_groups

    cursor.execute(
        "SELECT COUNT(*) FROM paragraphs WHERE lecture_id = %s", (lecture_id,)
    )
    old_paras = cursor.fetchone()[0]

    if dry_run:
        return old_paras, len(groups), len(sentence_data)

    # Clear image refs, delete old paragraphs
    cursor.execute(
        "UPDATE lecture_images SET after_sentence_id=NULL, after_paragraph_id=NULL WHERE lecture_id=%s",
        (lecture_id,)
    )
    cursor.execute("DELETE FROM paragraphs WHERE lecture_id = %s", (lecture_id,))

    for pi, group in enumerate(groups, 1):
        cursor.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
            (lecture_id, pi)
        )
        para_id = cursor.fetchone()[0]
        for si, (sid, text_de, text_zh) in enumerate(group, 1):
            cursor.execute(
                "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s,%s,%s,%s)",
                (para_id, si, text_de, text_zh)
            )

    return old_paras, len(groups), len(sentence_data)


# ── Verification ───────────────────────────────────────────────

def verify_lecture(cursor, lecture_id, title_de, ga_number):
    """Verify paragraph regrouping: check sentence count and paragraph sizes."""
    cursor.execute("""
        SELECT p.order_index, COUNT(s.id)
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        GROUP BY p.order_index
        ORDER BY p.order_index
    """, (lecture_id,))
    rows = cursor.fetchall()
    if not rows:
        return False, "NO PARAGRAPHS"

    sizes = [r[1] for r in rows]
    total = sum(sizes)
    avg = total / len(rows)
    min_s = min(sizes)
    max_s = max(sizes)

    issues = []
    if max_s > 30:
        issues.append(f"max_para_too_large({max_s})")
    if min_s < 1:
        issues.append(f"empty_para")
    if avg < 2:
        issues.append(f"avg_too_small({avg:.1f})")
    if total == 0:
        issues.append("no_sentences")

    status = "OK" if not issues else "WARN:" + ",".join(issues)

    print(f"  [{status}] {ga_number} lect {lecture_id} \"{title_de[:30]}\": "
          f"{len(rows)} paras, {total} sents, sizes {min_s}-{max_s} (avg {avg:.1f})",
          flush=True)

    return len(issues) == 0, status


# ── Main ───────────────────────────────────────────────────────

def process_book(cursor, ga_number, book_id, dry_run=False, force=False):
    """Process one book: extract, match, regroup, verify."""
    sources = find_source_files(ga_number)
    if not sources:
        return (None, "no_source")

    # Try DOC first, then PDF
    full_text = ""
    all_paras = []
    source_type = None

    for fmt in ['doc', 'pdf', 'epub']:
        if fmt in sources:
            if fmt == 'doc':
                full_text, all_paras = extract_doc_paragraphs(sources[fmt])
            elif fmt == 'pdf':
                full_text, all_paras = extract_pdf_paragraphs(sources[fmt])
            if full_text and all_paras:
                source_type = fmt
                break

    if not all_paras:
        return (None, "extraction_failed")

    # Get lectures for this book
    cursor.execute("""
        SELECT id, order_index, title_de FROM lectures
        WHERE book_id = %s ORDER BY order_index
    """, (book_id,))
    lectures = cursor.fetchall()

    results = []
    for lid, lorder, ltitle in lectures:
        sentences = get_lecture_sentences(cursor, lid)
        if not sentences:
            continue

        sent_text, sent_boundaries = build_sentence_index(sentences)
        matches = match_paragraphs_to_sentences(all_paras, sent_text, sent_boundaries)

        if len(matches) < 2:
            results.append((lid, lorder, ltitle, "too_few_matches", 0, 0, 0))
            continue

        old, new, total = apply_regrouping(cursor, lid, sentences, matches, dry_run=dry_run)
        if old > 0 and new != old:
            ok, status = verify_lecture(cursor, lid, ltitle, ga_number) if not dry_run else (True, "DRY_RUN")
            results.append((lid, lorder, ltitle, status, old, new, total))

    return results, source_type


def main():
    parser = argparse.ArgumentParser(description="Rebuild paragraphs from source files")
    parser.add_argument("ga_filter", nargs="*", help="GA numbers to process")
    parser.add_argument("--all", action="store_true", help="Process all books")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--verify-only", action="store_true", help="Only verify, don't change")
    args = parser.parse_args()

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
                            user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    try:
        # Get books to process
        if args.ga_filter:
            placeholders = ','.join(['%s'] * len(args.ga_filter))
            cursor.execute(f"""
                SELECT id, ga_number FROM books WHERE ga_number IN ({placeholders}) ORDER BY ga_number
            """, tuple(args.ga_filter))
        else:
            cursor.execute("SELECT id, ga_number FROM books ORDER BY ga_number")

        books = cursor.fetchall()

        total_fixed = 0
        total_lectures = 0
        summary = []

        for book_id, ga in books:
            if args.verify_only:
                cursor.execute("SELECT id, title_de FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
                for lid, ltitle in cursor.fetchall():
                    verify_lecture(cursor, lid, ltitle, ga)
                continue

            proc_result = process_book(cursor, ga, book_id, dry_run=args.dry_run)
            if proc_result[0] is None:
                summary.append(f"{ga}: SKIP ({proc_result[1]})")
                continue

            results, source_type = proc_result
            fixed = sum(1 for r in results if r[4] > 0 and r[4] != r[5])
            if fixed > 0:
                total_fixed += 1
                total_lectures += fixed
                summary.append(f"{ga}: {source_type} source, {fixed} lectures fixed")
            else:
                summary.append(f"{ga}: {source_type} source, no changes needed")

        # Print summary
        print(f"\n{'='*60}")
        print(f"SUMMARY: {total_fixed} books, {total_lectures} lectures")
        if args.dry_run:
            print("DRY RUN — no changes applied")
        for s in summary:
            print(f"  {s}")

        if not args.dry_run and not args.verify_only and total_fixed > 0:
            conn.commit()
            print(f"\nCommitted. Fixed {total_fixed} books.")

    except Exception as e:
        conn.rollback()
        import traceback
        print(f"FATAL: {e}")
        traceback.print_exc()
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
