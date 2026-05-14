#!/usr/bin/env python3
"""Generate standalone import scripts for each bad EPUB book.

Uses the fixed paragraph parser from epub_importer_pipe.py.
Outputs individual scripts to scripts/individual/.
"""

import json
import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from epub_importer_pipe import parse_epub  # noqa: E402


def _make_template(ga_number, title, chapters_json):
    """Build the template with placeholders already filled in."""
    # We build the template inline, filling in GA_NUMBER and TITLE
    # but leaving CHAPTERS_JSON to be inserted after template rendering
    t = '''#!/usr/bin/env python3
"""Standalone import script for {gn} — {ti}"""

import subprocess
import sys
from pathlib import Path

# === CONFIGURATION ===
BOOK_TITLE = """{ti}"""
GA_NUMBER = "{gn}"
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DOCKER_CONTAINER = "steiner-postgres"

# === CHAPTER DATA ===
CHAPTERS = {cj}

# === SQL GENERATION ===
def generate_sql():
    """Generate SQL using PL/pgSQL DO block."""
    sql_lines = []
    sql_lines.append("-- Auto-generated import for " + GA_NUMBER)
    sql_lines.append("BEGIN;")
    sql_lines.append("")
    sql_lines.append("DO $$")
    sql_lines.append("DECLARE")
    sql_lines.append("    v_book_id INT;")
    sql_lines.append("    v_lecture_id INT;")
    sql_lines.append("    v_para_id INT;")
    sql_lines.append("BEGIN")
    sql_lines.append("    -- Create or get book")
    te = BOOK_TITLE.replace("'", "''")
    sql_lines.append("    v_book_id := (SELECT id FROM books WHERE ga_number = '%s');" % GA_NUMBER)
    sql_lines.append("    IF v_book_id IS NULL THEN")
    sql_lines.append("        INSERT INTO books (ga_number, title_de, pdf_filename)")
    sql_lines.append("        VALUES ('%s', '%s', '%s.epub')" % (GA_NUMBER, te, GA_NUMBER))
    sql_lines.append("        RETURNING id INTO v_book_id;")
    sql_lines.append("    ELSE")
    sql_lines.append("        UPDATE books SET title_de = '%s' WHERE id = v_book_id;" % te)
    sql_lines.append("    END IF;")
    sql_lines.append("")
    sql_lines.append("    -- Delete old data (cascades to paragraphs/sentences)")
    sql_lines.append("    DELETE FROM lectures WHERE book_id = v_book_id;")
    sql_lines.append("")

    for ch in CHAPTERS:
        te = ch["title_de"].replace("'", "''")
        sql_lines.append("    -- Chapter %d: %s" % (ch["order"], te))
        sql_lines.append("    INSERT INTO lectures (book_id, title_de, order_index, level)")
        sql_lines.append("    VALUES (v_book_id, '%s', %d, 'lecture')" % (te, ch["order"]))
        sql_lines.append("    RETURNING id INTO v_lecture_id;")
        sql_lines.append("")

        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else []
            if not sentences:
                continue

            sql_lines.append("    INSERT INTO paragraphs (lecture_id, order_index)")
            sql_lines.append("    VALUES (v_lecture_id, %d)" % pi)
            sql_lines.append("    RETURNING id INTO v_para_id;")
            sql_lines.append("")

            for si, sent in enumerate(sentences, 1):
                se = sent.replace("'", "''")
                sql_lines.append("    INSERT INTO sentences (paragraph_id, order_index, text_de)")
                sql_lines.append("    VALUES (v_para_id, %d, '%s');" % (si, se))
                sql_lines.append("")

    sql_lines.append("END $$;")
    sql_lines.append("COMMIT;")
    sql_lines.append("")

    return "\\n".join(sql_lines)


def import_to_db():
    """Run the SQL import via docker exec psql."""
    print("Generating SQL for %s..." % GA_NUMBER)
    sql = generate_sql()
    sql_path = "/tmp/%s_import.sql" % GA_NUMBER
    Path(sql_path).write_text(sql, encoding='utf-8')
    ln = len(sql.split('\\n'))
    sk = len(sql) / 1024
    print("  SQL written: %s (%d lines, %d KB)" % (sql_path, ln, sk))

    result = subprocess.run(
        ["docker", "cp", sql_path, "%s:/tmp/%s_import.sql" % (DOCKER_CONTAINER, GA_NUMBER)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("  FAILED COPY: %s" % result.stderr)
        return False

    print("  Importing into Docker PostgreSQL...")
    with open(sql_path, 'r') as f:
        proc = subprocess.Popen(
            ["docker", "exec", "-i", DOCKER_CONTAINER, "psql", "-U", DB_USER, "-d", DB_NAME],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = proc.communicate(input=sql)

    if proc.returncode != 0:
        sl = stderr.strip().split('\\n')
        print("  psql error (exit=%d):" % proc.returncode)
        for line in sl[-5:]:
            print("     %s" % line)
        return False
    else:
        print("  IMPORTED %s successfully!" % GA_NUMBER)
        if stdout.strip():
            for line in stdout.strip().split('\\n')[-3:]:
                print("     %s" % line)
        return True


if __name__ == "__main__":
    print()
    print("=" * 60)
    print("Importing %s: %s" % (GA_NUMBER, BOOK_TITLE))
    print("=" * 60)

    tp = sum(len(c["paragraphs"]) for c in CHAPTERS)
    ts = sum(sum(len(s) for s in c["sentences"]) for c in CHAPTERS)
    print("  %d chapters, %d paragraphs, %d sentences" % (len(CHAPTERS), tp, ts))

    success = import_to_db()
    sys.exit(0 if success else 1)
'''
    return t.format(gn=ga_number, ti=title, cj=chapters_json)


def generate_import_script(book_data):
    """Generate a standalone import script from parsed book data."""
    ga_number = book_data["ga_number"]
    title = book_data["title_de"] or ga_number
    chapters = book_data["chapters"]

    # Serialize chapters to JSON
    chapters_json = json.dumps(chapters, ensure_ascii=False, indent=2)

    return _make_template(ga_number, title, chapters_json)


def main():
    output_dir = Path(__file__).parent / "individual"
    output_dir.mkdir(parents=True, exist_ok=True)

    bad_books = [
        122, 114, 81, 73, 52, 4, 140, 107, 28, 118,
        180, 184, 29, 188, 186, 130, 123, 129, 67, 7,
        155, 141, 76, 183, 153, 138, 16, 3, 179, 12,
        109, 116, 17, 112, 62, 181, 158, 126, 120, 117,
        11, 136, 121, 119, 21, 176, 135, 132, 54, 24,
        127, 27, 8, 18, 143, 133, 128, 124, 108, 57, 55,
    ]

    epub_dir = Path("/tmp/epub_batch")

    for ga_num in bad_books:
        ga_str = "GA{:03d}".format(ga_num)
        epub_path = epub_dir / "{}.epub".format(ga_str)

        if not epub_path.exists():
            print("SKIP {} not found".format(epub_path))
            continue

        print()
        print("=" * 60)
        print("Parsing {}".format(epub_path.name))
        print("=" * 60)

        data = parse_epub(str(epub_path))
        if not data:
            print("  FAILED to parse {}".format(ga_str))
            continue

        script_content = generate_import_script(data)
        script_path = output_dir / "{}_import.py".format(ga_str)
        script_path.write_text(script_content, encoding='utf-8')
        script_path.chmod(0o755)

        tp = sum(len(c["paragraphs"]) for c in data["chapters"])
        ts = sum(sum(len(s) for s in c["sentences"]) for c in data["chapters"])
        print("  Script saved: {}".format(script_path))
        print("     {} chapters, {} paragraphs, {} sentences".format(
            len(data["chapters"]), tp, ts))


if __name__ == "__main__":
    main()
