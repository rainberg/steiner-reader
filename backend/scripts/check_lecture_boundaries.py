"""
Lecture Boundary Verification - 4-layer check.
Run on Steiner production server (66.154.112.162).

Usage:
    python3 check_lecture_boundaries.py

Inputs:
    - /tmp/pdf_full_texts.json (217 GA PDF full texts)
    - PostgreSQL steiner_reader database
    - steiner.wiki (online)

Outputs:
    - /tmp/lecture_boundary_report.json
    - /tmp/lecture_boundary_report.txt
"""
import os
import json
import re
import unicodedata
import psycopg2
import requests
from datetime import datetime, timedelta

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FULL_FILE = "/tmp/pdf_full_texts.json"
OUTPUT_JSON = "/tmp/lecture_boundary_report.json"
OUTPUT_TXT = "/tmp/lecture_boundary_report.txt"
WIKI_BASE = "https://steiner.wiki/wiki/GA{}"


def normalize(s: str) -> str:
    """Normalize text for fuzzy matching: lowercase, remove accents/punctuation."""
    if not s:
        return ""
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.replace("ß", "ss")
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


def find_position(needle: str, haystack_norm: str, start_pos: int = 0) -> int:
    """Find position of needle in normalized haystack. Return -1 if not found."""
    needle_n = normalize(needle)
    if not needle_n or not haystack_norm:
        return -1

    # Try progressively shorter prefixes
    for length in [80, 60, 50, 40, 30, 25, 20]:
        if len(needle_n) >= length:
            chunk = needle_n[:length]
            pos = haystack_norm.find(chunk, start_pos)
            if pos >= 0:
                return pos

    # Try middle chunk
    if len(needle_n) >= 60:
        mid = len(needle_n) // 2
        chunk = needle_n[mid:mid+40]
        pos = haystack_norm.find(chunk, start_pos)
        if pos >= 0:
            return pos

    # Try from beginning (ignore start_pos)
    if start_pos > 0:
        for length in [80, 60, 50, 40, 30, 25, 20]:
            if len(needle_n) >= length:
                chunk = needle_n[:length]
                pos = haystack_norm.find(chunk, 0)
                if pos >= 0:
                    return pos

    return -1


def find_heading_position(title: str, haystack_norm: str) -> int:
    """Find heading title in PDF. Short titles need exact match."""
    title_n = normalize(title)
    if not title_n or not haystack_norm:
        return -1

    if len(title_n) < 20:
        # Short title: require full match
        return haystack_norm.find(title_n)
    else:
        # Long title: use first 20 chars
        return haystack_norm.find(title_n[:20])


def layer1_wiki_compare(cur):
    """Layer 1: Compare lecture count and dates with steiner.wiki for all 316 GAs."""
    # Get all books with GA numbers
    cur.execute("""
        SELECT id, ga_number, title_de
        FROM books
        WHERE ga_number IS NOT NULL AND ga_number != ''
        ORDER BY ga_number
    """)
    books = cur.fetchall()
    print(f"  Found {len(books)} books to compare with wiki", flush=True)

    results = []
    session = requests.Session()
    session.headers.update({"User-Agent": "SteinerReader/1.0"})

    for i, (book_id, ga_number, book_title) in enumerate(books):
        ga_num = ga_number.replace("GA", "") if ga_number.upper().startswith("GA") else ga_number

        # Fetch wiki page
        try:
            url = WIKI_BASE.format(ga_num)
            resp = session.get(url, timeout=15)
            if resp.status_code != 200:
                results.append({
                    "ga": ga_number,
                    "book_id": book_id,
                    "layer": 1,
                    "type": "wiki_fetch_error",
                    "severity": "warning",
                    "description": f"Wiki page returned {resp.status_code}",
                    "fix_suggestion": "Check if GA number exists on steiner.wiki",
                    "confidence": "high",
                })
                continue

            # Parse lecture dates from wiki
            wiki_dates = set()
            # Pattern 1: DD. Month YYYY (German months)
            for m in re.finditer(r'(\d{1,2})\.\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+(\d{4})', resp.text):
                day, month_name, year = int(m.group(1)), m.group(2), int(m.group(3))
                month_map = {"Januar":1,"Februar":2,"März":3,"April":4,"Mai":5,"Juni":6,
                             "Juli":7,"August":8,"September":9,"Oktober":10,"November":11,"Dezember":12}
                month = month_map.get(month_name)
                if month:
                    try:
                        wiki_dates.add(datetime(year, month, day).strftime("%Y-%m-%d"))
                    except ValueError:
                        pass
            # Pattern 2: DD.MM.YYYY
            for m in re.finditer(r'(\d{1,2})\.(\d{1,2})\.(\d{4})', resp.text):
                day, month, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
                try:
                    wiki_dates.add(datetime(year, month, day).strftime("%Y-%m-%d"))
                except ValueError:
                    pass

        except Exception as e:
            results.append({
                "ga": ga_number,
                "book_id": book_id,
                "layer": 1,
                "type": "wiki_fetch_error",
                "severity": "warning",
                "description": f"Error fetching wiki: {str(e)[:100]}",
                "fix_suggestion": "Check network connectivity",
                "confidence": "high",
            })
            continue

        # Get DB lecture dates
        cur.execute("""
            SELECT lecture_date
            FROM lectures
            WHERE book_id = %s AND level = 'lecture' AND lecture_date IS NOT NULL
            ORDER BY lecture_date
        """, (book_id,))
        db_dates_raw = cur.fetchall()
        db_dates = set()
        for (d,) in db_dates_raw:
            if d:
                db_dates.add(d.strftime("%Y-%m-%d"))

        # Compare
        wiki_only = wiki_dates - db_dates
        db_only = db_dates - wiki_dates

        if wiki_only or db_only:
            # Check for ±1 day matches (timezone differences)
            real_wiki_only = set()
            real_db_only = set()

            for wd in wiki_only:
                matched = False
                wd_dt = datetime.strptime(wd, "%Y-%m-%d")
                for dd in db_only:
                    dd_dt = datetime.strptime(dd, "%Y-%m-%d")
                    if abs((wd_dt - dd_dt).days) <= 1:
                        matched = True
                        break
                if not matched:
                    real_wiki_only.add(wd)

            for dd in db_only:
                matched = False
                dd_dt = datetime.strptime(dd, "%Y-%m-%d")
                for wd in wiki_only:
                    wd_dt = datetime.strptime(wd, "%Y-%m-%d")
                    if abs((wd_dt - dd_dt).days) <= 1:
                        matched = True
                        break
                if not matched:
                    real_db_only.add(dd)

            if real_wiki_only or real_db_only:
                results.append({
                    "ga": ga_number,
                    "book_id": book_id,
                    "layer": 1,
                    "type": "date_mismatch",
                    "severity": "error" if real_wiki_only else "warning",
                    "description": f"Wiki has {len(real_wiki_only)} extra dates, DB has {len(real_db_only)} extra dates",
                    "wiki_only_dates": sorted(real_wiki_only)[:10],
                    "db_only_dates": sorted(real_db_only)[:10],
                    "wiki_count": len(wiki_dates),
                    "db_count": len(db_dates),
                    "fix_suggestion": "Check if lectures are missing from DB or incorrectly imported",
                    "confidence": "high" if real_wiki_only else "medium",
                })

        if (i + 1) % 50 == 0:
            print(f"  Layer 1: {i+1}/{len(books)} processed", flush=True)

    print(f"  Layer 1 complete: {len(results)} issues found", flush=True)
    return results


def layer2_boundary_check(cur, pdf_full):
    """Layer 2: Position each lecture's first/last sentence in PDF full text."""
    results = []
    issues = []

    for ga_key, pdf_info in sorted(pdf_full.items()):
        if "error" in pdf_info:
            continue

        full_text = pdf_info.get("full_text", "")
        if not full_text:
            continue

        full_text_norm = normalize(full_text)

        # Get book_id
        cur.execute("SELECT id FROM books WHERE ga_number = %s", (ga_key,))
        book = cur.fetchone()
        if not book:
            continue
        book_id = book[0]

        # Get all lectures ordered by order_index, id
        cur.execute("""
            SELECT id, title_de, order_index
            FROM lectures
            WHERE book_id = %s AND level = 'lecture'
            ORDER BY order_index ASC, id ASC
        """, (book_id,))
        lectures = cur.fetchall()

        if not lectures:
            continue

        prev_last_pos = -1

        for lec_id, lec_title, _ in lectures:
            # Get first sentence
            cur.execute("""
                SELECT s.text_de
                FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
                ORDER BY p.order_index ASC, s.order_index ASC
                LIMIT 1
            """, (lec_id,))
            first_row = cur.fetchone()
            first_text = first_row[0] if first_row else ""

            # Get last sentence
            cur.execute("""
                SELECT s.text_de
                FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
                ORDER BY p.order_index DESC, s.order_index DESC
                LIMIT 1
            """, (lec_id,))
            last_row = cur.fetchone()
            last_text = last_row[0] if last_row else ""

            # Find positions
            search_start = prev_last_pos if prev_last_pos > 0 else 0
            first_pos = find_position(first_text, full_text_norm, search_start) if first_text else -1

            last_search_start = first_pos if first_pos > 0 else 0
            last_pos = find_position(last_text, full_text_norm, last_search_start) if last_text else -1

            # Check: first_found
            if first_text and first_pos < 0:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": lec_id,
                    "lecture_title": lec_title,
                    "layer": 2,
                    "type": "first_not_found",
                    "severity": "error",
                    "description": f"First sentence not found in PDF",
                    "db_text": first_text[:200],
                    "fix_suggestion": "Check if lecture is truncated at start, or first sentence differs from PDF",
                    "confidence": "high",
                })

            # Check: last_found
            if last_text and last_pos < 0:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": lec_id,
                    "lecture_title": lec_title,
                    "layer": 2,
                    "type": "last_not_found",
                    "severity": "warning",
                    "description": f"Last sentence not found in PDF",
                    "db_text": last_text[:200],
                    "fix_suggestion": "Check if lecture is truncated at end, or last sentence differs from PDF",
                    "confidence": "medium",
                })

            # Check: order_ok (first < last)
            if first_pos >= 0 and last_pos >= 0 and first_pos >= last_pos:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": lec_id,
                    "lecture_title": lec_title,
                    "layer": 2,
                    "type": "order_bad",
                    "severity": "error",
                    "description": f"First pos ({first_pos}) >= last pos ({last_pos})",
                    "fix_suggestion": "Lecture boundary is seriously wrong, check import",
                    "confidence": "high",
                })

            # Check: no_overlap (first >= prev_last)
            if prev_last_pos > 0 and first_pos > 0 and first_pos < prev_last_pos:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": lec_id,
                    "lecture_title": lec_title,
                    "layer": 2,
                    "type": "overlap",
                    "severity": "error",
                    "description": f"Lecture starts at {first_pos} but previous ended at {prev_last_pos}",
                    "fix_suggestion": "Lecture may include content from previous lecture's ending",
                    "confidence": "high",
                })

            if last_pos > 0:
                prev_last_pos = last_pos

    print(f"  Layer 2 complete: {len(issues)} issues found", flush=True)
    return results, issues


def layer3_gap_analysis(cur, pdf_full):
    """Layer 3: Check gaps between adjacent lectures for missing content."""
    results = []
    issues = []

    # Date + location patterns for gap content classification
    date_pattern = re.compile(r'\d{1,2}\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s*\d{4}', re.IGNORECASE)
    date_pattern2 = re.compile(r'\d{1,2}\.\s*\d{1,2}\.\s*\d{4}')
    location_pattern = re.compile(r'(Berlin|München|Stuttgart|Dornach|Wien|Hamburg|Frankfurt|Köln|Leipzig|Dresden|Bremen|Nürnberg|Düsseldorf|Bern|Zürich)', re.IGNORECASE)
    index_pattern = re.compile(r'\d+\s*,\s*\d+', re.IGNORECASE)

    for ga_key, pdf_info in sorted(pdf_full.items()):
        if "error" in pdf_info:
            continue

        full_text = pdf_info.get("full_text", "")
        if not full_text:
            continue

        full_text_norm = normalize(full_text)

        cur.execute("SELECT id FROM books WHERE ga_number = %s", (ga_key,))
        book = cur.fetchone()
        if not book:
            continue
        book_id = book[0]

        cur.execute("""
            SELECT id, title_de, order_index
            FROM lectures
            WHERE book_id = %s AND level = 'lecture'
            ORDER BY order_index ASC, id ASC
        """, (book_id,))
        lectures = cur.fetchall()

        if len(lectures) < 2:
            continue

        # Get positions for all lectures
        positions = []
        for lec_id, lec_title, _ in lectures:
            cur.execute("""
                SELECT s.text_de
                FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
                ORDER BY p.order_index ASC, s.order_index ASC
                LIMIT 1
            """, (lec_id,))
            first_row = cur.fetchone()
            first_text = first_row[0] if first_row else ""

            cur.execute("""
                SELECT s.text_de
                FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
                ORDER BY p.order_index DESC, s.order_index DESC
                LIMIT 1
            """, (lec_id,))
            last_row = cur.fetchone()
            last_text = last_row[0] if last_row else ""

            search_start = positions[-1]["last_pos"] if positions and positions[-1]["last_pos"] > 0 else 0
            first_pos = find_position(first_text, full_text_norm, search_start) if first_text else -1
            last_search = first_pos if first_pos > 0 else 0
            last_pos = find_position(last_text, full_text_norm, last_search) if last_text else -1

            positions.append({
                "lec_id": lec_id,
                "title": lec_title,
                "first_pos": first_pos,
                "last_pos": last_pos,
            })

        # Check gaps between consecutive lectures
        for i in range(1, len(positions)):
            prev = positions[i - 1]
            curr = positions[i]

            if prev["last_pos"] < 0 or curr["first_pos"] < 0:
                continue

            gap = curr["first_pos"] - prev["last_pos"]

            if gap > 2000:
                # Extract gap text from original (non-normalized) PDF text
                gap_text_norm = full_text_norm[prev["last_pos"]:curr["first_pos"]]
                gap_text_orig = full_text[prev["last_pos"]:curr["first_pos"]] if len(full_text) > curr["first_pos"] else ""

                # Classify gap content
                has_date = bool(date_pattern.search(gap_text_orig)) or bool(date_pattern2.search(gap_text_orig))
                has_location = bool(location_pattern.search(gap_text_orig))
                has_index = bool(index_pattern.search(gap_text_norm[:500]))

                severity = "warning"
                gap_type = "large_gap"
                if gap > 5000:
                    gap_type = "very_large_gap"
                    severity = "error"

                if has_date and has_location:
                    severity = "error"
                    fix_suggestion = "Gap contains date+location pattern, likely a missing lecture. Check PDF pages manually."
                    confidence = "high"
                elif has_index and not has_date:
                    severity = "info"
                    fix_suggestion = "Gap appears to be index/reference content, likely not a missing lecture."
                    confidence = "medium"
                else:
                    fix_suggestion = "Large gap detected, manually check if content is missing."
                    confidence = "low"

                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": curr["lec_id"],
                    "lecture_title": curr["title"],
                    "layer": 3,
                    "type": gap_type,
                    "severity": severity,
                    "description": f"Gap of {gap} chars before this lecture",
                    "gap_size": gap,
                    "gap_preview": gap_text_norm[:200],
                    "has_date": has_date,
                    "has_location": has_location,
                    "fix_suggestion": fix_suggestion,
                    "confidence": confidence,
                })

    print(f"  Layer 3 complete: {len(issues)} issues found", flush=True)
    return results, issues


def layer4_heading_check(cur, pdf_full):
    """Layer 4: Verify heading titles appear in PDF at correct positions."""
    results = []
    issues = []

    # Keywords for auto-generated headings to skip
    skip_keywords = ["inhaltsverzeichnis", "titel", "cover", "vorwort", "geleitwort",
                     "faksimilie", "verzeichnis", "bibliographie"]

    for ga_key, pdf_info in sorted(pdf_full.items()):
        if "error" in pdf_info:
            continue

        full_text = pdf_info.get("full_text", "")
        if not full_text:
            continue

        full_text_norm = normalize(full_text)

        cur.execute("SELECT id FROM books WHERE ga_number = %s", (ga_key,))
        book = cur.fetchone()
        if not book:
            continue
        book_id = book[0]

        # Get all headings
        cur.execute("""
            SELECT id, title_de, parent_id, order_index
            FROM lectures
            WHERE book_id = %s AND level = 'heading'
            ORDER BY order_index ASC, id ASC
        """, (book_id,))
        headings = cur.fetchall()

        for h_id, h_title, h_parent_id, _ in headings:
            if not h_title:
                continue

            # Skip auto-generated headings
            title_norm_check = normalize(h_title)
            if any(kw in title_norm_check for kw in skip_keywords):
                continue

            # Find heading in PDF
            heading_pos = find_heading_position(h_title, full_text_norm)

            if heading_pos < 0:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": h_id,
                    "lecture_title": h_title,
                    "layer": 4,
                    "type": "heading_not_found",
                    "severity": "warning",
                    "description": f"Heading title not found in PDF",
                    "fix_suggestion": "Heading may be incorrectly created or title text differs from PDF",
                    "confidence": "medium",
                })
                continue

            # Get child lectures of this heading
            cur.execute("""
                SELECT id
                FROM lectures
                WHERE parent_id = %s AND level = 'lecture'
                ORDER BY order_index ASC, id ASC
            """, (h_id,))
            children = cur.fetchall()

            if not children:
                issues.append({
                    "ga": ga_key,
                    "book_id": book_id,
                    "lecture_id": h_id,
                    "lecture_title": h_title,
                    "layer": 4,
                    "type": "heading_orphan",
                    "severity": "info",
                    "description": "Heading has no child lectures",
                    "fix_suggestion": "May be an empty section or import error",
                    "confidence": "low",
                })
                continue

            # Check heading is before its children
            first_child_id = children[0][0]
            cur.execute("""
                SELECT s.text_de
                FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
                ORDER BY p.order_index ASC, s.order_index ASC
                LIMIT 1
            """, (first_child_id,))
            child_row = cur.fetchone()
            child_text = child_row[0] if child_row else ""

            if child_text:
                child_pos = find_position(child_text, full_text_norm, 0)
                if child_pos >= 0 and heading_pos >= child_pos:
                    issues.append({
                        "ga": ga_key,
                        "book_id": book_id,
                        "lecture_id": h_id,
                        "lecture_title": h_title,
                        "layer": 4,
                        "type": "heading_after_children",
                        "severity": "error",
                        "description": f"Heading at pos {heading_pos} is after child at pos {child_pos}",
                        "fix_suggestion": "Heading position is after its child lectures, structural order may be wrong",
                        "confidence": "high",
                    })

    print(f"  Layer 4 complete: {len(issues)} issues found", flush=True)
    return results, issues


def generate_report(results, issues):
    """Generate JSON and text reports."""
    # Count by severity and layer
    by_severity = {"error": 0, "warning": 0, "info": 0}
    by_layer = {1: 0, 2: 0, 3: 0, 4: 0}

    for issue in issues:
        sev = issue.get("severity", "warning")
        layer = issue.get("layer", 0)
        by_severity[sev] = by_severity.get(sev, 0) + 1
        by_layer[layer] = by_layer.get(layer, 0) + 1

    # Group issues by GA
    issues_by_ga = {}
    for issue in issues:
        ga = issue.get("ga", "unknown")
        if ga not in issues_by_ga:
            issues_by_ga[ga] = []
        issues_by_ga[ga].append(issue)

    # JSON report
    json_report = {
        "summary": {
            "total_issues": len(issues),
            "issues_by_severity": by_severity,
            "issues_by_layer": by_layer,
            "gas_with_issues": len(issues_by_ga),
        },
        "issues": issues,
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_report, f, ensure_ascii=False, indent=2)

    # Text report
    lines = []
    lines.append("=" * 70)
    lines.append("讲座边界验证报告 (Lecture Boundary Verification Report)")
    lines.append("=" * 70)
    lines.append(f"总计: {len(issues)} 个问题")
    lines.append(f"  错误(error): {by_severity.get('error', 0)}")
    lines.append(f"  警告(warning): {by_severity.get('warning', 0)}")
    lines.append(f"  信息(info): {by_severity.get('info', 0)}")
    lines.append(f"  涉及GA: {len(issues_by_ga)}")
    lines.append(f"  按层分布: L1={by_layer.get(1,0)}, L2={by_layer.get(2,0)}, L3={by_layer.get(3,0)}, L4={by_layer.get(4,0)}")
    lines.append("")

    # Show errors first, then warnings, then info
    for severity in ["error", "warning", "info"]:
        sev_issues = [i for i in issues if i.get("severity") == severity]
        if not sev_issues:
            continue

        sev_label = {"error": "错误", "warning": "警告", "info": "信息"}[severity]
        lines.append(f"\n{'='*70}")
        lines.append(f"{sev_label} ({len(sev_issues)}个)")
        lines.append(f"{'='*70}\n")

        # Group by GA
        sev_by_ga = {}
        for issue in sev_issues:
            ga = issue.get("ga", "unknown")
            if ga not in sev_by_ga:
                sev_by_ga[ga] = []
            sev_by_ga[ga].append(issue)

        for ga in sorted(sev_by_ga.keys()):
            ga_issues = sev_by_ga[ga]
            lines.append(f"--- {ga} ({len(ga_issues)}个{sev_label}) ---")

            for issue in ga_issues:
                layer = issue.get("layer", "?")
                itype = issue.get("type", "unknown")
                desc = issue.get("description", "")
                lec_id = issue.get("lecture_id", "")
                lec_title = issue.get("lecture_title", "")
                suggestion = issue.get("fix_suggestion", "")
                confidence = issue.get("confidence", "")

                lines.append(f"  [L{layer}-{itype}] 讲座#{lec_id} {lec_title[:50]}")
                lines.append(f"    {desc}")

                if "db_text" in issue:
                    lines.append(f"    DB文本: {issue['db_text'][:100]}...")
                if "gap_preview" in issue:
                    lines.append(f"    间隙预览: {issue['gap_preview'][:100]}...")
                if "wiki_only_dates" in issue and issue["wiki_only_dates"]:
                    lines.append(f"    Wiki多出日期: {issue['wiki_only_dates'][:5]}")
                if "db_only_dates" in issue and issue["db_only_dates"]:
                    lines.append(f"    DB多出日期: {issue['db_only_dates'][:5]}")

                lines.append(f"    建议: {suggestion}")
                lines.append(f"    置信度: {confidence}")
                lines.append("")

    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"  Report generated: {len(issues)} issues", flush=True)
    print(f"  By severity: {by_severity}", flush=True)
    print(f"  By layer: {by_layer}", flush=True)


def main():
    print("=== Lecture Boundary Verification ===", flush=True)
    print(f"Start time: {datetime.now()}", flush=True)

    # Load PDF full texts
    with open(PDF_FULL_FILE, "r", encoding="utf-8") as f:
        pdf_full = json.load(f)
    print(f"Loaded {len(pdf_full)} PDF full texts", flush=True)

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    all_results = []
    all_issues = []

    # Run 4 layers
    print("\n--- Layer 1: Wiki count + date comparison ---", flush=True)
    layer1_results = layer1_wiki_compare(cur)
    all_results.extend(layer1_results)
    all_issues.extend(layer1_results)

    print("\n--- Layer 2: Boundary positioning ---", flush=True)
    layer2_results, l2_issues = layer2_boundary_check(cur, pdf_full)
    all_results.extend(layer2_results)
    all_issues.extend(l2_issues)

    print("\n--- Layer 3: Gap analysis ---", flush=True)
    layer3_results, l3_issues = layer3_gap_analysis(cur, pdf_full)
    all_results.extend(layer3_results)
    all_issues.extend(l3_issues)

    print("\n--- Layer 4: Heading verification ---", flush=True)
    layer4_results, l4_issues = layer4_heading_check(cur, pdf_full)
    all_results.extend(layer4_results)
    all_issues.extend(l4_issues)

    cur.close()
    conn.close()

    # Generate reports
    print("\n--- Generating reports ---", flush=True)
    generate_report(all_results, all_issues)

    print(f"\nDone! Time: {datetime.now()}", flush=True)
    print(f"JSON report: {OUTPUT_JSON}", flush=True)
    print(f"Text report: {OUTPUT_TXT}", flush=True)


if __name__ == "__main__":
    main()
