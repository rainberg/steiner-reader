#!/usr/bin/env python3
"""
Import GA011 (Aus der Akasha-Chronik) into production PostgreSQL database.

Parses the PDF, extracts chapters with paragraphs and sentences,
and inserts them into the steiner_reader database on the production server.
"""
import re
import fitz  # PyMuPDF
import psycopg2
from pathlib import Path

# === CONFIG ===
PDF_PATH = Path("/opt/steiner-reader/books/GA011.pdf")
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "password"

# === CHAPTERS: (order, title_de, printed_start_page, printed_end_page) ===
# From the TOC on PDF page 5 (printed page 5)
# printed_page = pdf_page_index + 1 (GA011 offset is 1)
CHAPTERS = [
    (1, "Vorwort Marie Steiners zur ersten Buchausgabe 1939", 7, 8),
    (2, "Die Kultur der Gegenwart im Spiegel der Geisteswissenschaft", 9, 20),
    (3, "Aus der Akasha-Chronik — Vorwort", 21, 25),
    (4, "Unsere atlantischen Vorfahren", 26, 43),
    (5, "Übergang der vierten in die fünfte Wurzelrasse", 44, 56),
    (6, "Die lemurische Rasse", 57, 73),
    (7, "Die Trennung in Geschlechter", 74, 86),
    (8, "Die letzten Zeiten vor der Geschlechtertrennung", 87, 97),
    (9, "Die hyperboräische und die polarische Epoche", 98, 110),
    (10, "Anfang der gegenwärtigen Erde. Austritt der Sonne", 111, 119),
    (11, "Austritt des Mondes", 120, 128),
    (12, "Einige notwendige Zwischenbemerkungen", 129, 140),
    (13, "Von der Herkunft der Erde", 141, 150),
    (14, "Die Erde und ihre Zukunft", 151, 160),
    (15, "Das Leben des Saturn", 161, 170),
    (16, "Das Leben der Sonne", 171, 182),
    (17, "Das Leben auf dem Monde", 183, 195),
    (18, "Das Leben der Erde", 196, 212),
    (19, "Der viergliedrige Erdenmensch", 213, 232),
    (20, "Fragenbeantwortung", 233, 237),
    (21, "Vorurteile aus vermeintlicher Wissenschaft", 238, 250),
    (22, "Hinweise", 251, 252),
    # 23: Übersicht über die Rudolf Steiner Gesamtausgabe starts at p.253 but
    # the PDF only has 252 pages - it's probably not included in this scan
]


def printed_to_pdf_page(printed_page):
    """Convert printed page number to PDF page index (0-based).
    
    For GA011: printed_page 7 = PDF page index 6 (7-1=6)
    """
    return printed_page - 1


def extract_text(pdf_doc, start_printed, end_printed):
    """Extract text from a range of printed pages."""
    start_pdf = printed_to_pdf_page(start_printed)
    end_pdf = printed_to_pdf_page(end_printed)
    
    text_parts = []
    for page_idx in range(start_pdf, min(end_pdf + 1, len(pdf_doc))):
        page = pdf_doc[page_idx]
        text = page.get_text()
        text_parts.append(text)
    
    full_text = '\n'.join(text_parts)
    return full_text


def split_into_paragraphs(text):
    """Split text into paragraphs."""
    paragraphs = re.split(r'\n\s*\n', text)
    paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 20]
    return paragraphs


def split_into_sentences(text):
    """Split German text into sentences."""
    text = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
    return sentences


def clean_chapter_text(text, title):
    """Remove the title/header from the beginning of chapter text."""
    lines = text.split('\n')
    cleaned_lines = []
    skip_header = True
    
    for line in lines:
        if skip_header:
            stripped = line.strip()
            # Skip empty lines after the header
            if not stripped:
                skip_header = False
                continue
            # Skip lines that match parts of the title
            # (keep going until we hit a non-title line)
            continue
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def update_book(cursor):
    """Update the existing GA011 book record with correct title."""
    cursor.execute("UPDATE books SET title_de = %s WHERE ga_number = %s RETURNING id",
                   ("Aus der Akasha-Chronik", "GA011"))
    row = cursor.fetchone()
    if row:
        book_id = row[0]
        print(f"    Updated existing book ID: {book_id}")
        # Clear existing lectures/chapters
        cursor.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        print(f"    Cleared existing lectures: {cursor.rowcount}")
        return book_id
    # If no existing book, insert new one
    cursor.execute("""
        INSERT INTO books (ga_number, title_de, pdf_filename)
        VALUES (%s, %s, %s)
        RETURNING id
    """, ("GA011", "Aus der Akasha-Chronik", "GA011.pdf"))
    return cursor.fetchone()[0]


def insert_chapter(cursor, book_id, chapter_info, text):
    """Insert a chapter with its paragraphs and sentences."""
    order, title, _, _ = chapter_info
    
    cursor.execute("""
        INSERT INTO lectures (book_id, title_de, order_index)
        VALUES (%s, %s, %s)
        RETURNING id
    """, (book_id, title, order))
    lecture_id = cursor.fetchone()[0]
    
    paragraphs = split_into_paragraphs(text)
    
    for para_idx, para_text in enumerate(paragraphs, 1):
        cursor.execute("""
            INSERT INTO paragraphs (lecture_id, order_index)
            VALUES (%s, %s)
            RETURNING id
        """, (lecture_id, para_idx))
        paragraph_id = cursor.fetchone()[0]
        
        sentences = split_into_sentences(para_text)
        
        for sent_idx, sent_text in enumerate(sentences, 1):
            cursor.execute("""
                INSERT INTO sentences (paragraph_id, order_index, text_de)
                VALUES (%s, %s, %s)
            """, (paragraph_id, sent_idx, sent_text))
    
    return lecture_id, len(paragraphs)


def main():
    print("=" * 60)
    print("GA011 Import Script (Production)")
    print("=" * 60)
    
    # 1. Open PDF
    print(f"\n[1] Opening PDF: {PDF_PATH}")
    pdf_doc = fitz.open(str(PDF_PATH))
    print(f"    PDF pages: {len(pdf_doc)}")
    
    # 2. Connect to database
    print(f"\n[2] Connecting to database: {DB_HOST}:{DB_PORT}/{DB_NAME}")
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT,
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    cursor = conn.cursor()
    print("    Connected.")
    
    try:
        # 3. Update book record
        print(f"\n[3] Updating book record...")
        book_id = update_book(cursor)
        print(f"    Book ID: {book_id}")
        
        # 4. Import each chapter
        print(f"\n[4] Importing {len(CHAPTERS)} chapters...")
        total_paragraphs = 0
        total_sentences = 0
        
        for chapter_info in CHAPTERS:
            order, title, start_page, end_page = chapter_info
            
            print(f"\n    Chapter {order}: {title[:50]}...")
            print(f"      Pages: {start_page}-{end_page}")
            
            text = extract_text(pdf_doc, start_page, end_page)
            print(f"      Text length: {len(text)} chars")
            
            text = clean_chapter_text(text, title)
            
            lecture_id, para_count = insert_chapter(cursor, book_id, chapter_info, text)
            total_paragraphs += para_count
            
            cursor.execute("""
                SELECT COUNT(*) FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
            """, (lecture_id,))
            sent_count = cursor.fetchone()[0]
            total_sentences += sent_count
            
            print(f"      Chapter ID: {lecture_id}, Paragraphs: {para_count}, Sentences: {sent_count}")
        
        # 5. Commit
        conn.commit()
        print(f"\n[5] COMMIT successful!")
        print(f"    Total: {len(CHAPTERS)} chapters, {total_paragraphs} paragraphs, {total_sentences} sentences")
        
        # 6. Verify
        print(f"\n[6] Verification...")
        cursor.execute("""
            SELECT COUNT(*) FROM lectures WHERE book_id = %s
        """, (book_id,))
        actual_chapters = cursor.fetchone()[0]
        
        cursor.execute("""
            SELECT COUNT(*) FROM paragraphs p
            JOIN lectures l ON p.lecture_id = l.id
            WHERE l.book_id = %s
        """, (book_id,))
        actual_paragraphs = cursor.fetchone()[0]
        
        cursor.execute("""
            SELECT COUNT(*) FROM sentences s
            JOIN paragraphs p ON s.paragraph_id = p.id
            JOIN lectures l ON p.lecture_id = l.id
            WHERE l.book_id = %s
        """, (book_id,))
        actual_sentences = cursor.fetchone()[0]
        
        print(f"\n    Book: GA011 (ID={book_id})")
        print(f"    Chapters: {actual_chapters}")
        print(f"    Paragraphs: {actual_paragraphs}")
        print(f"    Sentences: {actual_sentences}")
        
        cursor.execute("""
            SELECT id, order_index, title_de
            FROM lectures WHERE book_id = %s
            ORDER BY order_index
        """, (book_id,))
        print(f"\n    Chapters in database:")
        for l in cursor.fetchall():
            print(f"      [{l[1]}] {l[2][:60]}...")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
        pdf_doc.close()
        print("\nDone.")


if __name__ == "__main__":
    main()
