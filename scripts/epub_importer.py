#!/usr/bin/env python3
"""
Universal EPUB-based import script for Steiner Reader.
Parses nav.xhtml + content*.xhtml → lectures / paragraphs / sentences in PostgreSQL.

Usage:
  python3 epub_importer.py test GA009.epub     # Dry run, no DB
  python3 epub_importer.py GA009.epub GA010.epub  # Import to DB
  python3 epub_importer.py /path/to/epub/*.epub   # Batch import
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

import psycopg2

# ── DB Config ──────────────────────────────────────────────
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "***"

# ── EPUB Namespaces ────────────────────────────────────────
XHTML_NS = "http://www.w3.org/1999/xhtml"

# ── Sentence Splitter ──────────────────────────────────────
_SENTENCE_BREAK = re.compile(r'(?<=[.!?])(?<!\d\.)(?<!\d\d\.)\s+(?=[A-ZÄÖÜ"«„])')

def split_sentences(text: str) -> list[str]:
    """Split German text into sentences."""
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


def extract_paragraphs_from_elem(p_elem) -> list[str]:
    """Extract clean paragraphs from a <p> element, handling <br/> separators."""
    raw = get_element_text(p_elem).strip()
    if not raw or len(raw) <= 10:
        return []
    
    # Remove leading metadata like "GA 9 - Theosophie" before first <br/><br/>
    # Pattern: metadata lines followed by double newline
    raw = re.sub(r'^GA \d+ - .*?(?:\n\n|\n\r\n)', '', raw)
    
    # Remove standalone printing/bibliographic info lines
    raw = re.sub(r'(?m)^\d+\.\s*Auflage.*$', '', raw)
    raw = re.sub(r'(?m)^ISBN.*$', '', raw)
    raw = re.sub(r'(?m)^Alle Rechte.*$', '', raw)
    raw = re.sub(r'(?m)^.*Rudolf Steiner.*$', '', raw)
    
    # Split by double newlines (from <br/><br/>)
    paragraphs = re.split(r'\n\s*\n+', raw)
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    
    # Further process: split on lines that look like section headings
    result = []
    for para in paragraphs:
        # Check if para contains inline headings separated by single newlines
        lines = para.split('\n')
        if len(lines) <= 1 and len(para) < 200:
            result.append(para)
            continue
        
        # Split on heading lines (Roman numeral heading or short all-caps-like)
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
    
    # Filter trivial paragraphs
    result = [p for p in result if len(p) > 10]
    return result


def parse_epub(epub_path: str) -> dict:
    """Parse an EPUB file and return structured content."""
    result = {
        "ga_number": None,
        "title_de": None,
        "chapters": [],
    }
    
    # Determine GA number from filename
    ga_match = re.search(r'GA(\d+)', Path(epub_path).stem)
    if not ga_match:
        print(f"  ERROR: Cannot determine GA number from {epub_path}")
        return None
    result["ga_number"] = f"GA{ga_match.group(1)}"
    
    with zipfile.ZipFile(epub_path, 'r') as zf:
        # ── 1) Parse nav.xhtml for TOC ──
        nav_xml = zf.read("nav.xhtml").decode("utf-8")
        nav_root = ET.fromstring(nav_xml)
        
        # Find TOC nav
        # Use manual iteration since ElementTree doesn't support namespace prefixes in XPath
        toc_nav = None
        for nav_elem in nav_root.iter(f"{{{XHTML_NS}}}nav"):
            nav_type = nav_elem.get(f"{{http://www.idpf.org/2007/ops}}type") or \
                       nav_elem.get(f"{{http://www.w3.org/1999/xhtml}}type") or \
                       nav_elem.get("type", "")
            if nav_type == "toc":
                toc_nav = nav_elem
                break
        if toc_nav is None:
            # Fallback: first nav element
            toc_nav = nav_root.find(f".//{{{XHTML_NS}}}nav")
        
        # Extract TOC entries
        toc_entries = []
        if toc_nav is not None:
            for li in toc_nav.iter(f"{{{XHTML_NS}}}li"):
                a = li.find(f"{{{XHTML_NS}}}a")
                if a is not None:
                    href = a.get("href", "")
                    title = "".join(a.itertext()).strip()
                    if title and href:
                        toc_entries.append((title, href))
        
        # Filter out cover and nav itself
        toc_entries = [(t, h) for t, h in toc_entries
                       if "cover" not in h.lower()
                       and "nav.xhtml" not in h.lower()
                       and t.lower() not in ("buchcover", "cover")]
        
        # ── 2) Parse title from OPF ──
        for opf_name in ["content.opf", "inhalt.opf"]:
            if opf_name in zf.namelist():
                opf_xml = zf.read(opf_name).decode("utf-8")
                m = re.search(r'<dc:title[^>]*>(.*?)</dc:title>', opf_xml)
                if m:
                    result["title_de"] = m.group(1).strip()
                break
        
        # ── 3) Parse each content file ──
        order = 0
        for title, href in toc_entries:
            order += 1
            content_path = href.split("#")[0]  # Remove anchor
            
            # Find the actual file in the zip
            if content_path not in zf.namelist():
                for entry in zf.namelist():
                    if entry.endswith("/" + content_path) or entry == content_path:
                        content_path = entry
                        break
                else:
                    print(f"  WARNING: {content_path} not found, skipping")
                    order -= 1
                    continue
            
            # Read and parse content file
            content_xml = zf.read(content_path).decode("utf-8")
            content_root = ET.fromstring(content_xml)
            
            # Title from <h2>
            chapter_title = title
            h2 = content_root.find(f".//{{{XHTML_NS}}}h2")
            if h2 is not None and "".join(h2.itertext()).strip():
                chapter_title = "".join(h2.itertext()).strip()
            
            # Extract paragraphs
            p_elements = content_root.findall(f".//{{{XHTML_NS}}}p")
            paragraphs = []
            for p_elem in p_elements:
                paras = extract_paragraphs_from_elem(p_elem)
                paragraphs.extend(paras)
            
            # Also extract table rows (for INHALT pages)
            tables = content_root.findall(f".//{{{XHTML_NS}}}table")
            for table in tables:
                rows_text = []
                for tr in table.findall(f".//{{{XHTML_NS}}}tr"):
                    cells = tr.findall(f".//{{{XHTML_NS}}}th") + tr.findall(f".//{{{XHTML_NS}}}td")
                    cell_text = " ".join("".join(c.itertext()).strip() for c in cells)
                    cell_text = re.sub(r'\s+', ' ', cell_text).strip()
                    if cell_text:
                        rows_text.append(cell_text)
                if rows_text:
                    paragraphs.append("\n".join(rows_text))
            
            # Split paragraphs into sentences
            chapter_sentences = [split_sentences(p) for p in paragraphs]
            
            ch = {
                "order": order,
                "title_de": chapter_title,
                "href": href,
                "paragraphs": paragraphs,
                "sentences": chapter_sentences,
            }
            result["chapters"].append(ch)
            
            total_sents = sum(len(s) for s in chapter_sentences)
            preview = (paragraphs[0][:60] if paragraphs else "(empty)").replace('\n', ' ')
            print(f"  [{order:2d}] {chapter_title[:50]:50s} | {len(paragraphs):3d} paras, {total_sents:4d} sents | {preview}...")
    
    return result


def import_to_db(conn, book_data: dict) -> int:
    """Insert book data into database."""
    cursor = conn.cursor()
    
    ga_number = book_data["ga_number"]
    title_de = book_data["title_de"] or ga_number
    
    # Check if book exists
    cursor.execute("SELECT id FROM books WHERE ga_number = %s", (ga_number,))
    row = cursor.fetchone()
    
    if row:
        book_id = row[0]
        print(f"\n  Book {ga_number} exists (ID={book_id}), replacing lectures...")
        cursor.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        cursor.execute("UPDATE books SET title_de = %s WHERE id = %s", (title_de, book_id))
        print(f"  Deleted {cursor.rowcount} old lectures")
    else:
        cursor.execute("""
            INSERT INTO books (ga_number, title_de, pdf_filename)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (ga_number, title_de, f"{ga_number}.epub"))
        book_id = cursor.fetchone()[0]
        print(f"\n  Created new book (ID={book_id})")
    
    # Insert chapters
    total_paras = 0
    total_sents = 0
    
    for ch in book_data["chapters"]:
        cursor.execute("""
            INSERT INTO lectures (book_id, title_de, order_index)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (book_id, ch["title_de"], ch["order"]))
        lecture_id = cursor.fetchone()[0]
        
        for pi, para_text in enumerate(ch["paragraphs"], 1):
            cursor.execute("""
                INSERT INTO paragraphs (lecture_id, order_index)
                VALUES (%s, %s)
                RETURNING id
            """, (lecture_id, pi))
            para_id = cursor.fetchone()[0]
            total_paras += 1
            
            sentences = ch["sentences"][pi - 1] if pi - 1 < len(ch["sentences"]) else split_sentences(para_text)
            for si, sent_text in enumerate(sentences, 1):
                cursor.execute("""
                    INSERT INTO sentences (paragraph_id, order_index, text_de)
                    VALUES (%s, %s, %s)
                """, (para_id, si, sent_text))
                total_sents += 1
    
    conn.commit()
    cursor.close()
    
    n_ch = len(book_data["chapters"])
    print(f"  ✅ Imported: {n_ch} chapters, {total_paras} paragraphs, {total_sents} sentences")
    return book_id


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    
    mode = "import"
    if args[0] == "test":
        mode = "test"
        args = args[1:]
    
    # Collect epub files
    epub_files = []
    for arg in args:
        p = Path(arg)
        if p.exists():
            epub_files.append(str(p))
        elif p.with_suffix(".epub").exists():
            epub_files.append(str(p.with_suffix(".epub")))
    
    if not epub_files:
        print(f"No EPUB files found in: {args}")
        return
    
    for epub_path in epub_files:
        print(f"\n{'='*60}")
        print(f"📖 {Path(epub_path).name}")
        print(f"{'='*60}")
        
        data = parse_epub(epub_path)
        if not data:
            continue
        
        total_paras = sum(len(c["paragraphs"]) for c in data["chapters"])
        total_sents = sum(sum(len(s) for s in c["sentences"]) for c in data["chapters"])
        print(f"\n  ── Summary ──")
        print(f"  GA: {data['ga_number']} | Title: {data['title_de']}")
        print(f"  {len(data['chapters'])} chapters, {total_paras} paragraphs, {total_sents} sentences")
        
        if mode == "test":
            continue
        
        # Import mode
        print(f"\n  Connecting to DB...")
        try:
            conn = psycopg2.connect(
                host=DB_HOST, port=DB_PORT,
                dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
            )
            book_id = import_to_db(conn, data)
            conn.close()
            print(f"  ✅ {data['ga_number']} imported (Book ID={book_id})")
        except Exception as e:
            print(f"  ❌ DB Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
