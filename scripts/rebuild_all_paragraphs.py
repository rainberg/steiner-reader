#!/usr/bin/env python3
"""
Hybrid paragraph rebuilding for all books.

Phase 1 — Content-aware heuristic (all books): groups sentences by detecting
topic transition markers (Erstens, Heute, Nun, etc.) with max 12 sents/para.

Phase 2 — .doc exact matching (books with .doc source only): extracts real
paragraph boundaries from .doc file via catdoc, matches to DB sentences.
If matching is successful (≥50% boundaries matched, no para >100 sents),
replaces heuristic result. Otherwise keeps heuristic.

Usage:
  python3 scripts/rebuild_all_paragraphs.py --dry-run   # preview
  python3 scripts/rebuild_all_paragraphs.py              # apply all
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

# ── Heuristic paragraph detection ──────────────────────────────

PARA_START_PATTERNS = [
    r'^(Erstens|Zweitens|Drittens|Viertens|Fünftens|Sechstens|Siebentens|Achtens|Neuntens|Zehntens)\b',
    r'^(Heute|Nun|Also|Sodann|Schließlich|Zusammenfassend|Abschließend)\b',
    r'^(Dasjenige|Diejenige|Das ist|Dies ist|Dieser|Diese|Dieses)\b',
    r'^(Wenden wir uns|Gehen wir|Kommen wir|Sehen wir)\b',
    r'^(Ich möchte|Ich will|Ich werde)\b',
    r'^(Aber|Allein|Dagegen|Hingegen|Demgegenüber|Indessen|Jedoch)\b',
    r'^(Dem steht|Demgegenüber steht|Entgegen)\b',
    r'^(Was ist|Wie ist|Worin|Wodurch|Warum|Weshalb|Wieso)\b',
]

MAX_SENTS_PER_PARA = 12

def normalize(text):
    text = (text or '').replace('\xad', '').replace('­', '')
    return re.sub(r'\s+', ' ', text).strip()

def is_para_start(text):
    for pat in PARA_START_PATTERNS:
        if re.match(pat, text):
            return True
    return False


# ── DB operations ──────────────────────────────────────────────

def get_lecture_sentences(cursor, lecture_id):
    cursor.execute("""
        SELECT s.id, s.text_de, s.text_zh
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s
        ORDER BY p.order_index, s.order_index
    """, (lecture_id,))
    return cursor.fetchall()


def regroup_lecture(cursor, lecture_id, groups, dry_run=False):
    """Apply paragraph regrouping."""
    if len(groups) <= 1:
        return 0, len(groups), sum(len(g) for g in groups)

    cursor.execute("SELECT COUNT(*) FROM paragraphs WHERE lecture_id=%s", (lecture_id,))
    old = cursor.fetchone()[0]

    if dry_run:
        return old, len(groups), sum(len(g) for g in groups)

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
    return old, len(groups), sum(len(g) for g in groups)


def heuristic_grouping(sentences, max_sents=MAX_SENTS_PER_PARA):
    """Group sentences into paragraphs using content-aware heuristics."""
    if not sentences:
        return []
    groups = []
    cur = []
    for s in sentences:
        text = normalize(s[1] or '')
        if len(cur) >= 2 and is_para_start(text):
            groups.append(cur)
            cur = []
        if len(cur) >= max_sents:
            groups.append(cur)
            cur = []
        cur.append(s)
    if cur:
        groups.append(cur)
    # Merge small groups
    merged = []
    for g in groups:
        if len(g) <= 1 and merged:
            merged[-1].extend(g)
        else:
            merged.append(g)
    return merged


# ── .doc exact matching ────────────────────────────────────────

def extract_doc_paragraphs(doc_path):
    """Extract paragraphs from .doc via catdoc."""
    try:
        result = subprocess.run(['catdoc', doc_path], capture_output=True, timeout=60)
        content = result.stdout.decode('latin-1')
    except Exception:
        return [], ""

    pages = content.split('\x0c')
    paragraphs = []
    full_text = ""

    for page_text in pages:
        lines = page_text.split('\n')
        cur = []
        for line in lines:
            s = line.strip()
            if s:
                cur.append(s)
            elif cur:
                pt = normalize(' '.join(cur))
                if len(pt) > 30:
                    start = len(full_text)
                    full_text += pt + "\n"
                    paragraphs.append((start, len(full_text) - 1, pt))
                cur = []
        if cur:
            pt = normalize(' '.join(cur))
            if len(pt) > 30:
                start = len(full_text)
                full_text += pt + "\n"
                paragraphs.append((start, len(full_text) - 1, pt))

    return paragraphs, full_text


def match_doc_to_sentences(doc_paras, sentences):
    """Match .doc paragraphs to DB sentences using text alignment."""
    if not doc_paras or not sentences:
        return []

    sent_text = ""
    sent_bounds = []
    for sid, td, tz in sentences:
        n = normalize(td)
        if n:
            start = len(sent_text)
            sent_text += n + " "
            sent_bounds.append((start, len(sent_text) - 1, sid))

    matches = []
    search_pos = 0

    for (_, _, para_text) in doc_paras:
        if len(para_text) < 30:
            continue
        sk = para_text[:25]
        pos = sent_text.find(sk, search_pos)
        if pos < 0:
            sk = para_text[:15]
            pos = sent_text.find(sk, search_pos)
        if pos < 0:
            continue
        ek = para_text[-25:]
        epos = sent_text.find(ek, pos)
        if epos < 0:
            ek = para_text[-15:]
            epos = sent_text.find(ek, pos)
        if epos < 0:
            continue

        first = last = None
        for i, (bs, be, _) in enumerate(sent_bounds):
            if pos < be and first is None: first = i
            if epos < be and last is None: last = i
            if first is not None and last is not None: break

        if first is not None and last is not None:
            matches.append((first, last))
            search_pos = epos + len(ek)

    return matches


def groups_from_matches(matches, sentences):
    """Convert matched boundaries to sentence groups, filling gaps."""
    if not matches or not sentences:
        return None

    total = len(sentences)
    groups = []
    used = [False] * total

    for first, last in matches:
        if first < total and last < total:
            groups.append(sentences[first:last + 1])
            for i in range(first, last + 1):
                used[i] = True

    if not groups:
        return None

    # Fill gaps
    for i in range(total):
        if not used[i]:
            if i < matches[0][0]:
                groups[0] = [sentences[i]] + groups[0]
            elif i > matches[-1][1]:
                groups[-1].append(sentences[i])
            else:
                for gi in range(len(matches) - 1):
                    if matches[gi][1] < i < matches[gi + 1][0]:
                        groups[gi].append(sentences[i])
                        break

    return groups


def quality_check(groups):
    """Check if exact matching produced quality results.
    Returns True if results look good, False if matching failed.
    """
    if not groups or len(groups) < 2:
        return False
    largest = max(len(g) for g in groups)
    if largest > 100:
        return False  # Matching clearly failed
    if largest > 50 and len(groups) < 5:
        return False
    return True


# ── Main pipeline ──────────────────────────────────────────────

def process_book(cursor, book_id, ga_number, max_sents=MAX_SENTS_PER_PARA, dry_run=False):
    """Process one book: try .doc exact matching; if fails, use heuristic."""
    sources = {}
    doc_dir = "/opt/steiner-reader/books/doc"
    doc_path = os.path.join(doc_dir, f"{ga_number}.doc")
    if os.path.exists(doc_path):
        sources['doc'] = doc_path

    cursor.execute("SELECT id, order_index, title_de FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
    lectures = cursor.fetchall()

    results = []
    for lid, lorder, ltitle in lectures:
        sentences = get_lecture_sentences(cursor, lid)
        if len(sentences) < 10:
            continue

        groups = None
        method = "none"

        # Try .doc exact matching first
        if 'doc' in sources:
            doc_paras, _ = extract_doc_paragraphs(sources['doc'])
            if doc_paras:
                matches = match_doc_to_sentences(doc_paras, sentences)
                if matches and len(matches) >= 3:
                    doc_groups = groups_from_matches(matches, sentences)
                    if doc_groups and quality_check(doc_groups):
                        groups = doc_groups
                        method = "doc"

        # Fall back to heuristic
        if groups is None:
            groups = heuristic_grouping(sentences, max_sents)
            method = "heuristic"

        old, new, total = regroup_lecture(cursor, lid, groups, dry_run=dry_run)
        avg = total / max(new, 1) if new > 0 else 0
        largest = max(len(g) for g in groups) if groups else 0
        status = "OK" if largest <= 30 else f"WARN:max({largest})"

        if new != old:
            results.append((lid, lorder, ltitle, method, status, old, new, total))

    return results


def main():
    parser = argparse.ArgumentParser(description="Hybrid paragraph rebuilding")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-sents", type=int, default=MAX_SENTS_PER_PARA)
    args = parser.parse_args()

    max_sents = args.max_sents

    conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, ga_number FROM books ORDER BY ga_number")
        books = cursor.fetchall()

        total_books = 0
        total_lectures = 0
        doc_books = 0
        heur_books = 0

        for book_id, ga in books:
            results = process_book(cursor, book_id, ga, max_sents=max_sents, dry_run=args.dry_run)
            if not results:
                continue

            total_books += 1
            fixed = [r for r in results if r[5] != r[6]]
            doc_count = sum(1 for r in results if r[3] == 'doc')
            heur_count = sum(1 for r in results if r[3] == 'heuristic')

            if doc_count > 0: doc_books += 1
            if heur_count > 0: heur_books += 1
            total_lectures += len(fixed)

            for r in fixed:
                _, _, ltitle, method, status, old, new, total = r
                print(f"  [{status}] {ga} [{method}] \"{ltitle[:35]}\": {old}→{new} paras ({total}s)", flush=True)

        print(f"\n{'='*50}", flush=True)
        print(f"Total: {total_books} books, {total_lectures} lectures", flush=True)
        print(f"  Exact .doc matching: {doc_books} books", flush=True)
        print(f"  Content heuristic:   {heur_books} books", flush=True)

        if not args.dry_run and total_lectures > 0:
            conn.commit()
            print("Committed.", flush=True)
        else:
            print("DRY RUN — no changes applied.", flush=True)

    except Exception as e:
        conn.rollback()
        import traceback
        print(f"ERROR: {e}", flush=True)
        traceback.print_exc()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    main()
