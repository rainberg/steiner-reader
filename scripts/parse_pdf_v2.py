#!/usr/bin/env python3
"""
PDF Parser for Lecture Collections using TOC page numbers.
Strategy:
1. Extract TOC from PDF
2. Parse chapter titles + printed page numbers
3. Calculate offset (printed_page = pdf_index + offset)
4. Use page numbers to extract chapter text
"""
import re
import sqlite3
import fitz  # PyMuPDF
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path.home() / "steiner-reader" / "data" / "pdf"
DB_PATH = Path.home() / "steiner-reader" / "data" / "steiner.db"

# ============================================================
# TOC Parsing
# ============================================================

# Patterns for chapter entries with page numbers
TOC_CHAP_PATTERNS = [
    # "erster vortrag, Dornach, 24. Juni 1924 ... 42"
    re.compile(
        r'^(Erster|Zweiter|Dritter|Vierter|Fünfter|Sechster|Siebenter|Siebter|Achter|Neunter|Zehnter|'
        r'Elfter|Zwölfter|Dreizehnter|Vierzehnter|Fünfzehnter|Sechzehnter|Siebzehnter|Achtzehnter|Neunzehnter|'
        r'Zwanzigster|Einundzwanzigster|Zweiundzwanzigster|Dreiundzwanzigster|Vierundzwanzigster|Fünfundzwanzigster|'
        r'Sechsundzwanzigster|Siebenundzwanzigster|Achtundzwanzigster|Neunundzwanzigster|Dreißigster|'
        r'Einunddreißigster|Zweiunddreißigster|Dreiunddreißigster|Vierunddreißigster|Fünfunddreißigster|'
        r'Sechsunddreißigster|Siebenunddreißigster|Achtunddreißigster|Neununddreißigster|Vierzigster|'
        r'Einundvierzigster|Zweiundvierzigster|Dreiundvierzigster|Vierundvierzigster|Fünfundvierzigster|'
        r'Sechsundvierzigster|Siebenundvierzigster|Achtundvierzigster|Neunundvierzigster|Fünfzigster|'
        r'Einundfünfzigster|Zweiundfünfzigster)\s+'
        r'[Vv]ortrag[,.]?\s*(.*?)\s*[\.\s]+(\d+)\s*$',
        re.IGNORECASE | re.UNICODE
    ),
    # "1. Vortrag, Berlin, 25. Mai 1906 ... 42"
    re.compile(
        r'^(\d+)\.\s*[Vv]ortrag[,.]?\s*(.*?)\s*[\.\s]+(\d+)\s*$',
        re.IGNORECASE
    ),
    # "Vortrag 1, Berlin, 25. Mai 1906 ... 42"
    re.compile(
        r'^[Vv]ortrag\s+(\d+)[,.]?\s*(.*?)\s*[\.\s]+(\d+)\s*$',
        re.IGNORECASE
    ),
]

# Simpler pattern: anything ending with a page number
SIMPLE_TOC_PATTERN = re.compile(
    r'^(.*?)\s+[\.\s]+(\d+)\s*$'
)

# German date in a string
DATE_PATTERN = re.compile(
    r'(\d{1,2}\.?\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4})',
    re.IGNORECASE
)

def parse_toc_entries(pdf_doc):
    """Parse TOC entries from the PDF, returning list of (title, page_number)."""
    entries = []
    
    # Find TOC section (usually in first 30 pages)
    toc_text = ""
    for page_num in range(min(40, len(pdf_doc))):
        page = pdf_doc[page_num]
        text = page.get_text()
        # Look for TOC markers
        if any(kw in text.upper() for kw in ['INHALT', 'INHALTSVERZEICHNIS']):
            # Collect TOC text from this and following pages
            for p in range(page_num, min(page_num + 20, len(pdf_doc))):
                toc_text += pdf_doc[p].get_text() + "\n"
            break
    
    if not toc_text:
        return entries, -1
    
    # Parse each line
    toc_end_page = -1  # PDF page where TOC ends
    
    for line in toc_text.split('\n'):
        line = line.strip()
        if not line or len(line) < 10:
            continue
        
        # Try structured patterns first
        for pattern in TOC_CHAP_PATTERNS:
            match = pattern.match(line)
            if match:
                groups = match.groups()
                if len(groups) == 3:
                    # (ordinal, details, page) or (num, details, page)
                    title = line
                    page_num = int(groups[-1])
                    entries.append({
                        'title': title,
                        'page': page_num,
                        'date': extract_date(title),
                        'location': extract_location(title)
                    })
                    break
        
        # Simple fallback: line ending with a number
        else:
            match = SIMPLE_TOC_PATTERN.match(line)
            if match:
                title = match.group(1).strip()
                page_num = int(match.group(2))
                
                # Filter: page number should be reasonable (not a year, not too small/large)
                if 10 <= page_num <= 2000 and len(title) > 15:
                    # Check if it looks like a lecture title
                    is_lecture = any(kw in title.lower() for kw in 
                        ['vortrag', 'kapitel', 'teil', 'vorlesung', 'vorträge'])
                    # Or has ordinal words
                    is_lecture = is_lecture or any(kw in title.lower() for kw in
                        ['erster', 'zweiter', 'dritter', 'vierter', 'fünfter',
                         'sechster', 'siebenter', 'achter', 'neunter', 'zehnter',
                         'erste', 'zweite', 'dritte', 'vierte', 'fünfte'])
                    
                    if is_lecture:
                        entries.append({
                            'title': title,
                            'page': page_num,
                            'date': extract_date(title),
                            'location': extract_location(title)
                        })
    
    return entries

def extract_date(text):
    """Extract German date from text."""
    match = DATE_PATTERN.search(text)
    return match.group(1) if match else ""

def extract_location(text):
    """Extract location from text (word before date)."""
    date_match = DATE_PATTERN.search(text)
    if date_match:
        before_date = text[:date_match.start()].strip()
        # Remove ordinal and "Vortrag" parts
        before_date = re.sub(r'^(Erster|Zweiter|Dritter|...)\s+[Vv]ortrag[,.]?\s*', '', before_date)
        # Get last word (location)
        parts = before_date.rstrip(',').split()
        if parts:
            return parts[-1]
    return ""

def calculate_page_offset(pdf_doc, toc_entries):
    """
    Calculate the offset between PDF page index and printed page number.
    printed_page = pdf_index + offset
    """
    if not toc_entries:
        return 0
    
    # Find the first chapter's page number and search for it in the PDF
    first_entry = toc_entries[0]
    printed_page = first_entry['page']
    
    # The first chapter's title should appear on the printed page
    # Try PDF pages near (printed_page - 5) to (printed_page + 5)
    title = first_entry['title']
    
    for offset_guess in range(-10, 10):
        pdf_idx = printed_page - offset_guess
        if 0 <= pdf_idx < len(pdf_doc):
            text = pdf_doc[pdf_idx].get_text()[:2000]
            if title[:30].lower() in text.lower():
                # Found! offset = printed_page - pdf_idx
                return offset_guess
    
    # Fallback: estimate based on typical book structure
    # Usually the first content page is around PDF page 10-20 with printed page 1-10
    # So offset is usually negative (printed < pdf_index)
    # But we can estimate from the TOC page
    # If the last TOC entry page number is N and TOC ends at PDF page M,
    # then offset ≈ N - M - (some content pages after TOC)
    
    return 0  # Conservative default

def extract_chapter_text(pdf_doc, start_pdf_page, end_pdf_page):
    """Extract text from a range of PDF pages."""
    text_parts = []
    for page_num in range(max(0, start_pdf_page), min(end_pdf_page, len(pdf_doc))):
        page = pdf_doc[page_num]
        text = page.get_text()
        text_parts.append(text)
    return '\n'.join(text_parts)

def split_into_sentences(text):
    """Split text into German sentences."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 10]

def parse_book_pdf(ga_id):
    """Parse a book from PDF using TOC page numbers."""
    pdf_path = PDF_DIR / f"GA{ga_id.upper()}.pdf"
    if not pdf_path.exists():
        return None
    
    print(f"\nParsing GA{ga_id}...")
    
    try:
        pdf_doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"  Error opening PDF: {e}")
        return None
    
    total_pages = len(pdf_doc)
    print(f"  PDF pages: {total_pages}")
    
    # Step 1: Parse TOC
    toc_entries = parse_toc_entries(pdf_doc)
    print(f"  TOC entries: {len(toc_entries)}")
    
    if len(toc_entries) < 2:
        print(f"  Not enough TOC entries, skipping")
        pdf_doc.close()
        return None
    
    # Step 2: Calculate page offset
    offset = calculate_page_offset(pdf_doc, toc_entries)
    print(f"  Page offset: {offset}")
    
    # Step 3: Extract chapters
    chapters = []
    for i, entry in enumerate(toc_entries):
        # Convert printed page to PDF index
        start_pdf_page = max(0, entry['page'] - offset)
        
        # End page is start of next chapter or end of book
        if i + 1 < len(toc_entries):
            end_pdf_page = max(0, toc_entries[i + 1]['page'] - offset)
        else:
            end_pdf_page = total_pages
        
        # Extract text
        chapter_text = extract_chapter_text(pdf_doc, start_pdf_page, end_pdf_page)
        
        if len(chapter_text.strip()) < 50:
            print(f"  WARNING: Chapter {i+1} has very little text ({len(chapter_text)} chars)")
        
        chapters.append({
            'title': entry['title'],
            'date': entry.get('date', ''),
            'location': entry.get('location', ''),
            'start_page': start_pdf_page,
            'end_page': end_pdf_page,
            'text': chapter_text,
            'char_count': len(chapter_text)
        })
    
    pdf_doc.close()
    
    result = {
        'ga_id': ga_id,
        'total_pages': total_pages,
        'offset': offset,
        'chapters': chapters,
        'chapter_count': len(chapters),
        'total_chars': sum(c['char_count'] for c in chapters)
    }
    
    print(f"  Result: {result['chapter_count']} chapters, {result['total_chars']} chars")
    
    return result

def update_database(ga_id, parsed):
    """Update database with parsed chapters."""
    if not parsed:
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM books WHERE ga_id = ?", (f"GA{ga_id}",))
        book = cursor.fetchone()
        if not book:
            print(f"  Book GA{ga_id} not in database")
            return
        
        book_id = book[0]
        cursor.execute("DELETE FROM lectures WHERE book_id = ?", (book_id,))
        
        for i, chapter in enumerate(parsed['chapters']):
            cursor.execute("""
                INSERT INTO lectures (book_id, title, content, lecture_date, sort_order)
                VALUES (?, ?, ?, ?, ?)
            """, (book_id, chapter['title'], chapter['text'], chapter['date'], i + 1))
            
            lecture_id = cursor.lastrowid
            sentences = split_into_sentences(chapter['text'])
            for j, sentence in enumerate(sentences):
                cursor.execute("""
                    INSERT INTO sentences (lecture_id, text, sort_order)
                    VALUES (?, ?, ?)
                """, (lecture_id, sentence, j + 1))
        
        conn.commit()
        print(f"  DB updated: {len(parsed['chapters'])} chapters")
        
    except Exception as e:
        print(f"  DB error: {e}")
        conn.rollback()
    finally:
        conn.close()

# ============================================================
# Main
# ============================================================

def test_single(ga_id):
    """Test parsing a single book."""
    parsed = parse_book_pdf(ga_id)
    if parsed:
        for i, ch in enumerate(parsed['chapters'][:5]):
            print(f"\n  Chapter {i+1}: {ch['title'][:60]}...")
            print(f"    Pages: {ch['start_page']}-{ch['end_page']}")
            print(f"    Text preview: {ch['text'][:150]}...")
    return parsed

if __name__ == "__main__":
    import sys
    ga_id = sys.argv[1] if len(sys.argv) > 1 else "279"
    test_single(ga_id)
