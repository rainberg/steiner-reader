#!/usr/bin/env python3
"""
Steiner Reader EPUB Importer — Pipeline Mode
Parses an EPUB and pipes SQL to docker exec psql.
"""

import re
import sys
import subprocess
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

# ── EPUB Namespaces ────────────────────────────────────────
XHTML_NS = "http://www.w3.org/1999/xhtml"

# ── Sentence Splitter ──────────────────────────────────────
_SENTENCE_BREAK = re.compile(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ"«„])')

def split_sentences(text: str) -> list[str]:
    text = re.sub(r'\s+', ' ', text).strip()
    if not text or len(text) < 5:
        return []
    parts = _SENTENCE_BREAK.split(text)
    return [p.strip() for p in parts if len(p.strip()) > 3]


def get_element_text(elem) -> str:
    """Get full text of element, including <br/> as newlines."""
    parts = []
    if elem.text:
        parts.append(elem.text)
    for child in elem:
        tag = child.tag
        if tag == f"{{{XHTML_NS}}}br" or tag == "br":
            parts.append("\n")
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def _has_many_br(p_elem) -> bool:
    """Heuristic: does this <p> use <br/> as paragraph separators (bad epub format)?"""
    import itertools
    text_len = len(''.join(p_elem.itertext()).strip())
    br_count = len(list(itertools.chain(
        p_elem.iter(f'{{{XHTML_NS}}}br'),
        p_elem.iter('br'),
    )))
    # Bad epub: one <p> has 2000+ chars and 5+ <br/> tags
    return text_len > 2000 and br_count >= 5


def _clean_ga_metadata(raw: str) -> str:
    """Remove GA epub metadata markers like #G004-1987-SE007, #TI, #TX, etc."""
    # Remove the leading GA identifier line completely (from start of raw or after newline)
    # Pattern: #G004-1992tb-SE013 - Buchtitle
    raw = re.sub(r'^#[A-Za-z]\d{3}-\d{4}[a-z]*[-][A-Z]{1,4}\d{3,4}\s+-\s+.*?(?:\n|$)', '', raw, flags=re.MULTILINE)
    raw = re.sub(r'\n#[A-Za-z]\d{3}-\d{4}[a-z]*[-][A-Z]{1,4}\d{3,4}\s+-\s+.*?(?:\n|$)', '\n', raw)
    # Also handle #G004-1992tb-SE013 without trailing text
    raw = re.sub(r'#[A-Za-z]\d{3}-\d{4}[a-z]*[-](?:[A-Z]{1,4}\d{3,4}|SE\d{3,4})', '', raw)
    # Pattern 2: #Ti / #TI (chapter title) - remove everything between #Ti and #TX
    raw = re.sub(r'#T[Ii].*?(?=#TX)', '', raw, flags=re.DOTALL)
    # Pattern 3: #TX marker itself
    raw = re.sub(r'#TX', '', raw)
    # Pattern 4: any remaining #... markers
    raw = re.sub(r'#[A-Za-z0-9]{2,15}\s*', '', raw)
    # Pattern 5: #SE004-010 style markers inside text (page references)
    raw = re.sub(r'#SE\d{3}-\d{3,4}', '', raw)
    # Pattern 6: residual fragments like "-1992tb-SE013" (leftover after #G... removal)
    raw = re.sub(r'-\d{4}[a-z]*-(?:[A-Z]{1,4}\d{3,4}|SE\d{3,4})', '', raw)
    # Pattern 7: standalone residual like "-016" or "-SE013"
    raw = re.sub(r'-\d{3,4}(?:\s|$)', ' ', raw)
    return raw


def _split_by_newline_blocks(text: str) -> list[str]:
    """Split text into paragraphs by double newlines, then by single newlines."""
    # First try splitting by double newlines
    blocks = re.split(r'\n\s*\n+', text)
    blocks = [b.strip() for b in blocks if b.strip()]
    
    # Then for each block, split by single newline (for bad epub format)
    result = []
    for block in blocks:
        lines = block.split('\n')
        lines = [l.strip() for l in lines if l.strip()]
        if len(lines) <= 1:
            result.append(block)
        else:
            result.extend(lines)
    return result


def _split_on_roman_headings(paragraphs: list[str]) -> list[str]:
    """Further split paragraphs on Roman numeral headings."""
    result = []
    for para in paragraphs:
        lines = para.split('\n')
        if len(lines) <= 1:
            result.append(para)
            continue
        current = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            is_heading = bool(re.match(r'^([IVXLCDM]+)[\.\)]\s+[A-ZÄÖÜ]', line))
            if is_heading and current:
                result.append(' '.join(current))
                current = []
            current.append(line)
        if current:
            result.append(' '.join(current))
    return result


def extract_paragraphs_from_elem(p_elem) -> list[str]:
    raw = get_element_text(p_elem).strip()
    if not raw or len(raw) <= 10:
        return []
    
    # Detect bad epub format: one <p> with many <br/> as paragraph separators
    is_bad_format = _has_many_br(p_elem)
    # Extra heuristic: single <p> with no <br/> but very long text (3000+ chars)
    is_single_block = not is_bad_format and len(raw) > 3000
    
    # Remove metadata prefix lines
    raw = re.sub(r'^GA \d+ - .*?(?:\n\n|\n\r\n)', '', raw)
    raw = re.sub(r'(?m)^\d+\.\s*Auflage.*$', '', raw)
    raw = re.sub(r'(?m)^ISBN.*$', '', raw)
    raw = re.sub(r'(?m)^Alle Rechte.*$', '', raw)
    
    # Clean GA metadata markers
    raw = _clean_ga_metadata(raw)
    
    # Also clean the first line if it's just a short metadata line
    lines = raw.split('\n', 1)
    if len(lines) > 1 and len(lines[0].strip()) < 5:
        raw = lines[1]
    elif len(lines) > 1 and re.match(r'^[A-ZÄÖÜ \\-]{2,40}$', lines[0].strip()):
        raw = lines[1]
    
    # Split into paragraph blocks
    paragraphs = _split_by_newline_blocks(raw)
    
    # Further split on Roman numeral headings
    paragraphs = _split_on_roman_headings(paragraphs)
    
    # For bad epub format: also try splitting very long paragraphs on sentence boundaries
    # when they still exceed a reasonable paragraph length
    if is_bad_format or is_single_block:
        final = []
        for p in paragraphs:
            if len(p) > 1500:
                # Try to split on ". " or "? " that starts a new thought
                # Use a more aggressive sentence boundary approach
                sents = split_sentences(p)
                # Merge short sentences back together until we reach ~200 chars
                merged = []
                buf = []
                for s in sents:
                    buf.append(s)
                    if sum(len(x) for x in buf) > 200 and len(buf) >= 2:
                        merged.append(' '.join(buf))
                        buf = []
                if buf:
                    merged.append(' '.join(buf))
                if len(merged) > 1:
                    final.extend(merged)
                else:
                    final.append(p)
            else:
                final.append(p)
        paragraphs = final
    
    return [p for p in paragraphs if len(p) > 10]


def parse_epub(epub_path: str) -> dict:
    """Parse EPUB → structured dict."""
    result = {"ga_number": None, "title_de": None, "chapters": []}
    
    ga_match = re.search(r'GA(\d+)', Path(epub_path).stem)
    if not ga_match:
        print(f"  ERROR: Cannot determine GA number from {epub_path}")
        return None
    result["ga_number"] = f"GA{ga_match.group(1)}"
    
    with zipfile.ZipFile(epub_path, 'r') as zf:
        # Parse nav.xhtml TOC
        nav_xml = zf.read("nav.xhtml").decode("utf-8")
        nav_root = ET.fromstring(nav_xml)
        
        toc_nav = None
        for nav_elem in nav_root.iter(f"{{{XHTML_NS}}}nav"):
            nav_type = nav_elem.get(f"{{http://www.idpf.org/2007/ops}}type") or ""
            if nav_type == "toc":
                toc_nav = nav_elem
                break
        if toc_nav is None:
            toc_nav = nav_root.find(f".//{{{XHTML_NS}}}nav")
        
        toc_entries = []
        if toc_nav is not None:
            for li in toc_nav.iter(f"{{{XHTML_NS}}}li"):
                a = li.find(f"{{{XHTML_NS}}}a")
                if a is not None:
                    href = a.get("href", "")
                    title = "".join(a.itertext()).strip()
                    if title and href:
                        toc_entries.append((title, href))
        
        # Filter cover/nav
        toc_entries = [(t, h) for t, h in toc_entries
                       if "cover" not in h.lower()
                       and "nav.xhtml" not in h.lower()
                       and t.lower() not in ("buchcover", "cover")]
        
        # Parse title from OPF
        for opf_name in ["content.opf", "inhalt.opf"]:
            if opf_name in zf.namelist():
                opf_xml = zf.read(opf_name).decode("utf-8")
                m = re.search(r'<dc:title[^>]*>(.*?)</dc:title>', opf_xml)
                if m:
                    result["title_de"] = m.group(1).strip()
                break
        
        # Parse each content file
        for order, (title, href) in enumerate(toc_entries, 1):
            content_path = href.split("#")[0]
            
            if content_path not in zf.namelist():
                for entry in zf.namelist():
                    if entry.endswith("/" + content_path) or entry == content_path:
                        content_path = entry
                        break
                else:
                    order -= 1
                    continue
            
            content_xml = zf.read(content_path).decode("utf-8")
            content_root = ET.fromstring(content_xml)
            
            # Title from <h2>
            chapter_title = title
            h2 = content_root.find(f".//{{{XHTML_NS}}}h2")
            if h2 is not None and "".join(h2.itertext()).strip():
                chapter_title = "".join(h2.itertext()).strip()
            
            # Extract paragraphs from <p>
            p_elements = content_root.findall(f".//{{{XHTML_NS}}}p")
            paragraphs = []
            for p_elem in p_elements:
                paras = extract_paragraphs_from_elem(p_elem)
                paragraphs.extend(paras)
            
            # Extract table rows for INHALT
            for table in content_root.findall(f".//{{{XHTML_NS}}}table"):
                rows_text = []
                for tr in table.findall(f".//{{{XHTML_NS}}}tr"):
                    cells = tr.findall(f".//{{{XHTML_NS}}}th") + tr.findall(f".//{{{XHTML_NS}}}td")
                    cell_text = " ".join("".join(c.itertext()).strip() for c in cells)
                    cell_text = re.sub(r'\s+', ' ', cell_text).strip()
                    if cell_text:
                        rows_text.append(cell_text)
                if rows_text:
                    paragraphs.append("\n".join(rows_text))
            
            # Sentences
            chapter_sentences = [split_sentences(p) for p in paragraphs]
            
            ch = {
                "order": order,
                "title_de": chapter_title,
                "paragraphs": paragraphs,
                "sentences": chapter_sentences,
            }
            result["chapters"].append(ch)
            
            total_sents = sum(len(s) for s in chapter_sentences)
            preview = (paragraphs[0][:60] if paragraphs else "(empty)").replace('\n', ' ')
            print(f"  [{order:2d}] {chapter_title[:50]:50s} | {len(paragraphs):3d} paras, {total_sents:4d} sents | {preview}...")
    
    return result


def generate_sql(book_data: dict) -> str:
    """Generate SQL to replace book data."""
    ga_number = book_data["ga_number"]
    title_de = (book_data["title_de"] or ga_number).replace("'", "''")
    
    lines = []
    lines.append("-- Auto-generated import script for " + ga_number)
    lines.append("BEGIN;")
    lines.append("")
    
    # Upsert book
    lines.append(f"""
DO $$
DECLARE
    v_book_id INT;
BEGIN
    -- Get or create book
    INSERT INTO books (ga_number, title_de, pdf_filename)
    VALUES ('{ga_number}', '{title_de}', '{ga_number}.epub')
    ON CONFLICT (ga_number) DO UPDATE SET title_de = '{title_de}'
    RETURNING id INTO v_book_id;
    
    -- Delete old lectures (cascades to paragraphs and sentences)
    DELETE FROM lectures WHERE book_id = v_book_id;
""")
    
    # Insert lectures
    for ch in book_data["chapters"]:
        title_escaped = ch["title_de"].replace("'", "''")
        lines.append(f"""
    INSERT INTO lectures (book_id, title_de, order_index)
    VALUES (v_book_id, '{title_escaped}', {ch["order"]})
    RETURNING id INTO v_book_id;
""")
        # Actually, we need separate variables per lecture. Use RETURNING with a loop instead.
    
    # Hmm, let me rethink this. PL/pgSQL approach is getting messy.
    # Better: simple idempotent SQL.
    
    lines = []
    lines.append("-- Auto-generated import for " + ga_number)
    lines.append("BEGIN;")
    lines.append("")
    
    # Get book ID
    # First check if book exists
    lines.append(f"""
-- Find or create book
WITH
book_upsert AS (
    INSERT INTO books (ga_number, title_de, pdf_filename)
    VALUES ('{ga_number}', '{title_de}', '{ga_number}.epub')
    ON CONFLICT (ga_number) DO UPDATE SET title_de = '{title_de}'
    RETURNING id
),
book_id AS (
    SELECT id FROM book_upsert
)
SELECT id INTO TEMP TABLE _tmp_book_id FROM book_id;

-- Delete old data (cascades)
DELETE FROM lectures WHERE book_id = (SELECT id FROM _tmp_book_id);
""")
    
    # Insert lectures, paragraphs, sentences
    for ch in book_data["chapters"]:
        title_escaped = ch["title_de"].replace("'", "''")
        lines.append(f"""
-- Chapter {ch["order"]}: {title_escaped}
WITH lecture_ins AS (
    INSERT INTO lectures (book_id, title_de, order_index)
    VALUES ((SELECT id FROM _tmp_book_id), '{title_escaped}', {ch["order"]})
    RETURNING id
)
""")
        # Generate paragraph + sentence inserts
        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else split_sentences(para_text)
            if not sentences:
                continue
            
            lines.append(f""", para_{ch["order"]}_{pi} AS (
    INSERT INTO paragraphs (lecture_id, order_index)
    SELECT id, {pi} FROM lecture_ins
    RETURNING id
)
""")
            
            # Batch sentence inserts (10 at a time for readability)
            sent_batches = [sentences[i:i+10] for i in range(0, len(sentences), 10)]
            for bi, batch in enumerate(sent_batches):
                values = []
                for si, sent in enumerate(batch, bi * 10 + 1):
                    sent_esc = sent.replace("'", "''")
                    values.append(f"((SELECT id FROM para_{ch['order']}_{pi}), {si}, '{sent_esc}')")
                
                lines.append(f""", sent_{ch["order"]}_{pi}_{bi} AS (
    INSERT INTO sentences (paragraph_id, order_index, text_de)
    VALUES {', '.join(values)}
    SELECT 1
)
""")
        
        # Use a dummy SELECT to terminate the CTE chain
        # Actually, let's batch differently. The CTE approach gets too long with 70+ paragraphs.
    
    # SIMPLER approach: just generate the SQL with individual statements
    lines = []
    lines.append("-- Auto-generated import for " + ga_number)
    lines.append("BEGIN;")
    lines.append("")
    
    # Book ID
    lines.append(f"""
DO $$
DECLARE
    v_book_id INT;
    v_lecture_id INT;
    v_para_id INT;
BEGIN
    -- Create or get book
    v_book_id := (SELECT id FROM books WHERE ga_number = '{ga_number}');
    IF v_book_id IS NULL THEN
        INSERT INTO books (ga_number, title_de, pdf_filename)
        VALUES ('{ga_number}', '{title_de}', '{ga_number}.epub')
        RETURNING id INTO v_book_id;
    ELSE
        UPDATE books SET title_de = '{title_de}' WHERE id = v_book_id;
    END IF;
    
    -- Delete old data (cascades to paragraphs/sentences)
    DELETE FROM lectures WHERE book_id = v_book_id;
""")
    
    for ch in book_data["chapters"]:
        title_escaped = ch["title_de"].replace("'", "''")
        lines.append(f"""
    -- Chapter {ch["order"]}: {title_escaped}
    INSERT INTO lectures (book_id, title_de, order_index)
    VALUES (v_book_id, '{title_escaped}', {ch["order"]})
    RETURNING id INTO v_lecture_id;
""")
        
        for pi, para_text in enumerate(ch["paragraphs"], 1):
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else split_sentences(para_text)
            if not sentences:
                continue
            
            lines.append(f"""
    INSERT INTO paragraphs (lecture_id, order_index)
    VALUES (v_lecture_id, {pi})
    RETURNING id INTO v_para_id;
""")
            
            for si, sent in enumerate(sentences, 1):
                sent_esc = sent.replace("'", "''")
                lines.append(f"""
    INSERT INTO sentences (paragraph_id, order_index, text_de)
    VALUES (v_para_id, {si}, '{sent_esc}');
""")
    
    lines.append(f"""
END $$;
COMMIT;
""")
    
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 epub_importer_pipe.py <epub_file>")
        print("Or:    python3 epub_importer_pipe.py test <epub_file>")
        return
    
    mode = "import"
    if args[0] == "test":
        mode = "test"
        args = args[1:]
    
    for epub_path in args:
        p = Path(epub_path)
        if not p.exists():
            p = p.with_suffix(".epub")
        if not p.exists():
            print(f"✗ {epub_path} not found")
            continue
        
        print(f"\n{'='*60}")
        print(f"📖 {p.name}")
        print(f"{'='*60}")
        
        data = parse_epub(str(p))
        if not data:
            continue
        
        total_paras = sum(len(c["paragraphs"]) for c in data["chapters"])
        total_sents = sum(sum(len(s) for s in c["sentences"]) for c in data["chapters"])
        print(f"\n  ── Summary ──")
        print(f"  GA: {data['ga_number']} | Title: {data['title_de']}")
        print(f"  {len(data['chapters'])} chapters, {total_paras} paragraphs, {total_sents} sentences")
        
        if mode == "test":
            continue
        
        # Generate SQL and pipe to docker exec psql
        print(f"  Generating SQL...")
        sql = generate_sql(data)
        
        sql_path = f"/tmp/{data['ga_number']}_import.sql"
        Path(sql_path).write_text(sql, encoding='utf-8')
        
        lines = len(sql.split('\n'))
        size_kb = len(sql) / 1024
        print(f"  SQL written: {sql_path} ({lines} lines, {size_kb:.0f} KB)")
        
        print(f"  Piping to psql via docker exec...")
        result = subprocess.run(
            ["docker", "cp", sql_path, f"steiner-postgres:/tmp/{data['ga_number']}_import.sql"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"  ❌ COPY failed: {result.stderr}")
            continue
        
        with open(sql_path, 'r') as f:
            proc = subprocess.Popen(
                ["docker", "exec", "-i", "steiner-postgres", "psql", "-U", "steiner", "-d", "steiner_reader"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = proc.communicate(input=sql)
        
        if proc.returncode != 0:
            stderr_lines = stderr.strip().split('\n')
            print(f"  ❌ psql error (exit={proc.returncode}):")
            for line in stderr_lines[-5:]:
                print(f"     {line}")
        else:
            print(f"  ✅ {data['ga_number']} imported successfully!")
            if stdout.strip():
                for line in stdout.strip().split('\n')[-3:]:
                    print(f"     {line}")


if __name__ == "__main__":
    main()
