#!/usr/bin/env python3
"""
Parse lecture collections from PDF using TOC page numbers.
Strategy:
1. Parse TOC from PDF text
2. For each chapter in TOC, use the printed page number to find the PDF page
3. Extract text from that PDF page until the next chapter's page
"""
import re
import json
import sqlite3
import fitz  # PyMuPDF
from pathlib import Path
from collections import defaultdict

PDF_DIR = Path.home() / "steiner-reader" / "data" / "pdf"
DB_PATH = Path.home() / "steiner-reader" / "data" / "steiner.db"

# TOC chapter patterns (same as before)
CHAP_PATTERNS = [
    # Ordinal words with location+date
    re.compile(
        r'^(Erster|Zweiter|Dritter|Vierter|Fünfter|Sechster|Siebenter|Siebter|Achter|Neunter|Zehnter|'
        r'Elfter|Zwölfter|Dreizehnter|Vierzehnter|Fünfzehnter|Sechzehnter|Siebzehnter|Achtzehnter|Neunzehnter|'
        r'Zwanzigster|Einundzwanzigster|Zweiundzwanzigster|Dreiundzwanzigster|Vierundzwanzigster|Fünfundzwanzigster|'
        r'Sechsundzwanzigster|Siebenundzwanzigster|Achtundzwanzigster|Neunundzwanzigster|Dreißigster|'
        r'Einunddreißigster|Zweiunddreißigster|Dreiunddreißigster|Vierunddreißigster|Fünfunddreißigster|'
        r'Sechsunddreißigster|Siebenunddreißigster|Achtunddreißigster|Neununddreißigster|Vierzigster|'
        r'Einundvierzigster|Zweiundvierzigster|Dreiundvierzigster|Vierundvierzigster|Fünfundvierzigster|'
        r'Sechsundvierzigster|Siebenundvierzigster|Achtundvierzigster|Neunundvierzigster|Fünfzigster)\s+'
        r'[Vv]ortrag[,.]?\s*(.*)',
        re.IGNORECASE
    ),
    # Numbered lectures
    re.compile(r'^(\d+)\.\s*[Vv]ortrag[,.]?\s*(.*)', re.IGNORECASE),
    # "Vortrag" with ordinal
    re.compile(r'^[Vv]ortrag\s+(\d+)[,.]?\s*(.*)', re.IGNORECASE),
]

# German date patterns
DATE_PATTERN = re.compile(
    r'(\d{1,2}\.?\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s+\d{4})',
    re.IGNORECASE
)

# Location pattern (capitalized word before date)
LOCATION_PATTERN = re.compile(
    r'^([A-ZÄÖÜ][a-zäöüß]+(?:\s+[A-ZÄÖÜ][a-zäöüß]+)*)[,.]?\s*(?:' + DATE_PATTERN.pattern + r'|$)',
    re.IGNORECASE
)

def parse_toc_from_text(text):
    """Extract TOC entries from PDF text."""
    chapters = []
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Try each pattern
        for pattern in CHAP_PATTERNS:
            match = pattern.match(line)
            if match:
                # Extract title from the match
                title = line
                # Try to extract location and date
                date_match = DATE_PATTERN.search(line)
                location_match = LOCATION_PATTERN.search(line)
                
                date = date_match.group(1) if date_match else ""
                location = location_match.group(1) if location_match else ""
                
                chapters.append({
                    'title': title,
                    'date': date,
                    'location': location,
                    'raw_line': line
                })
                break
    
    return chapters

def find_toc_pages(pdf_doc):
    """Find the TOC section in the PDF by looking for 'INHALT' or table of contents patterns."""
    toc_pages = []
    
    for page_num in range(min(50, len(pdf_doc))):  # TOC is usually in first 50 pages
        page = pdf_doc[page_num]
        text = page.get_text()
        
        # Check if this page has TOC markers
        if any(keyword in text.upper() for keyword in ['INHALT', 'INHALTSVERZEICHNIS', 'VORTRAG', 'VORTRÄGE']):
            # Check if page has page numbers (TOC entries typically have numbers at end)
            lines = text.split('\n')
            toc_line_count = 0
            for line in lines:
                line = line.strip()
                if re.search(r'\d+\s*$', line) and len(line) > 20:
                    toc_line_count += 1
            
            if toc_line_count >= 3:  # At least 3 lines look like TOC entries
                toc_pages.append(page_num)
    
    return toc_pages

def get_page_offset(pdf_doc, toc_entries):
    """
    Calculate the offset between PDF page index and printed page number.
    Returns: offset such that printed_page = pdf_index + offset
    """
    if not toc_entries:
        return 0
    
    # Try to find the first chapter in the PDF by searching for its title
    for entry in toc_entries[:10]:  # Try first 10 entries
        title = entry['title']
        # Extract the ordinal part for matching
        for page_num in range(len(pdf_doc)):
            page = pdf_doc[page_num]
            text = page.get_text()[:500]  # Check first 500 chars
            
            # Check if the chapter title appears on this page
            if len(title) > 15:
                # Use partial match (first 30 chars)
                search_text = title[:30].lower()
                if search_text in text.lower():
                    # Found! The printed page number for this chapter
                    # should be close to this PDF page + some offset
                    # We can't determine exact offset without knowing the printed number
                    # but we can estimate based on typical book structure
                    return page_num  # Return the PDF page where first chapter starts
    
    return 0  # Default: no offset

def extract_chapter_text(pdf_doc, start_page, end_page):
    """Extract text from PDF pages."""
    text_parts = []
    for page_num in range(start_page, min(end_page, len(pdf_doc))):
        page = pdf_doc[page_num]
        text = page.get_text()
        text_parts.append(text)
    
    return '\n'.join(text_parts)

def split_into_paragraphs(text):
    """Split text into paragraphs."""
    # Split by double newlines or indentation patterns
    paragraphs = re.split(r'\n\s*\n', text)
    # Clean up
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return paragraphs

def split_into_sentences(text):
    """Split text into sentences."""
    # Simple German sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter out short fragments
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
    return sentences

def parse_book_from_pdf(ga_id, pdf_path):
    """Parse a single book from PDF using TOC-based chapter detection."""
    print(f"\nParsing GA{ga_id} from PDF...")
    
    try:
        pdf_doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"  Error opening PDF: {e}")
        return None
    
    # Step 1: Find TOC pages
    toc_pages = find_toc_pages(pdf_doc)
    print(f"  TOC pages: {toc_pages}")
    
    if not toc_pages:
        print(f"  No TOC found in PDF, skipping...")
        pdf_doc.close()
        return None
    
    # Step 2: Extract TOC text
    toc_text = ""
    for page_num in toc_pages:
        page = pdf_doc[page_num]
        toc_text += page.get_text() + "\n"
    
    # Step 3: Parse TOC entries
    toc_entries = parse_toc_from_text(toc_text)
    print(f"  TOC entries found: {len(toc_entries)}")
    
    if not toc_entries:
        print(f"  No chapters found in TOC, skipping...")
        pdf_doc.close()
        return None
    
    # Step 4: For each TOC entry, find its PDF page by searching for the title
    chapters = []
    total_pages = len(pdf_doc)
    
    for i, entry in enumerate(toc_entries):
        title = entry['title']
        
        # Search for this chapter in the PDF
        found_page = None
        for page_num in range(total_pages):
            page = pdf_doc[page_num]
            text = page.get_text()[:1000]  # Check first 1000 chars
            
            # Check if the chapter title appears on this page
            if len(title) > 15:
                # Use the ordinal part for matching
                search_text = title[:40].lower()
                if search_text in text.lower():
                    found_page = page_num
                    break
        
        if found_page is None:
            # Use linear estimation based on position in TOC
            # Skip first 10% of pages (cover, TOC), distribute remaining
            start_page = int((i + 1) / (len(toc_entries) + 1) * (total_pages - 10)) + 5
        else:
            start_page = found_page
        
        # End page is start of next chapter or end of book
        if i + 1 < len(toc_entries):
            next_entry = toc_entries[i + 1]
            # Try to find next chapter's page
            next_page = None
            for page_num in range(start_page + 1, total_pages):
                page = pdf_doc[page_num]
                text = page.get_text()[:1000]
                search_text = next_entry['title'][:40].lower()
                if search_text in text.lower():
                    next_page = page_num
                    break
            
            if next_page is None:
                end_page = min(start_page + 20, total_pages)  # Estimate 20 pages per lecture
            else:
                end_page = next_page
        else:
            end_page = total_pages
        
        # Extract text for this chapter
        chapter_text = extract_chapter_text(pdf_doc, start_page, end_page)
        
        # Split into paragraphs
        paragraphs = split_into_paragraphs(chapter_text)
        
        chapters.append({
            'title': title,
            'date': entry.get('date', ''),
            'location': entry.get('location', ''),
            'start_page': start_page,
            'end_page': end_page,
            'paragraphs': paragraphs,
            'paragraph_count': len(paragraphs)
        })
    
    pdf_doc.close()
    
    return {
        'ga_id': ga_id,
        'total_pages': total_pages,
        'chapters': chapters,
        'chapter_count': len(chapters)
    }

def update_database(ga_id, parsed_data):
    """Update the database with parsed chapters."""
    if not parsed_data:
        return
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        # Find the book
        cursor.execute("SELECT id FROM books WHERE ga_id = ?", (f"GA{ga_id}",))
        book = cursor.fetchone()
        if not book:
            print(f"  Book GA{ga_id} not found in database")
            return
        
        book_id = book[0]
        
        # Delete existing chapters for this book
        cursor.execute("DELETE FROM lectures WHERE book_id = ?", (book_id,))
        
        # Insert new chapters
        for i, chapter in enumerate(parsed_data['chapters']):
            # Combine all paragraphs into text
            full_text = '\n\n'.join(chapter['paragraphs'])
            
            cursor.execute("""
                INSERT INTO lectures (book_id, title, content, lecture_date, sort_order, paragraph_count)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                book_id,
                chapter['title'],
                full_text,
                chapter['date'],
                i + 1,
                chapter['paragraph_count']
            ))
            
            lecture_id = cursor.lastrowid
            
            # Insert sentences
            sentences = split_into_sentences(full_text)
            for j, sentence in enumerate(sentences):
                cursor.execute("""
                    INSERT INTO sentences (lecture_id, text, sort_order)
                    VALUES (?, ?, ?)
                """, (lecture_id, sentence, j + 1))
        
        conn.commit()
        print(f"  Updated database with {len(parsed_data['chapters'])} chapters")
        
    except Exception as e:
        print(f"  Database error: {e}")
        conn.rollback()
    finally:
        conn.close()

def main():
    """Main function to process PDFs."""
    print("PDF-based Lecture Collection Parser")
    print("=" * 50)
    
    # Check which PDFs are available
    available_pdfs = list(PDF_DIR.glob("GA*.pdf"))
    print(f"Available PDFs: {len(available_pdfs)}")
    
    # Get books from database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ga_id FROM books ORDER BY ga_id")
    db_books = [row[0] for row in cursor.fetchall()]
    conn.close()
    
    print(f"Books in database: {len(db_books)}")
    
    # Process each available PDF
    processed = 0
    for pdf_path in sorted(available_pdfs):
        ga_id = pdf_path.stem[2:]  # Remove 'GA' prefix
        
        if ga_id not in db_books:
            print(f"  GA{ga_id} not in database, skipping...")
            continue
        
        # Parse the PDF
        parsed = parse_book_from_pdf(ga_id, pdf_path)
        
        if parsed and parsed['chapter_count'] > 1:
            # Update database
            update_database(ga_id, parsed)
            processed += 1
            
            print(f"  GA{ga_id}: {parsed['chapter_count']} chapters, {parsed['total_pages']} pages")
    
    print(f"\nProcessed {processed} books from PDFs")

if __name__ == "__main__":
    main()
