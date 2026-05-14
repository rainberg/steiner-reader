#!/usr/bin/env python3
"""
Import GA279 (Eurythmie als sichtbare Sprache) into production PostgreSQL database.

Parses the PDF, extracts 17 lectures with paragraphs and sentences,
and inserts them into the steiner_reader database on the production server.
"""
import re
import fitz  # PyMuPDF
import psycopg2
from pathlib import Path

# === CONFIG ===
PDF_PATH = Path("/opt/steiner-reader/books/GA279.pdf")
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "steiner_reader"
DB_USER = "steiner"
DB_PASSWORD = "password"

# === TOC: printed page number -> (lecture_number, title, date, location) ===
# From the PDF TOC on pages 3-4
# PDF page offset: printed_page = pdf_page + 3
# 15 main lectures + 2 intro lectures = 17 total

LECTURES = [
    # (order, title_de, location, date_str, printed_start_page, printed_end_page)
    # The 2 introductory lectures
    (1, "Über die eurythmische Kunst", "Dornach", "1922-08-04", 7, 20),
    (2, "Eurythmie, was sie ist und wie sie entstanden ist", "Penmaenmawr", "1923-08-26", 21, 41),
    # The 15 main lectures (24. Juni - 12. Juli 1924)
    (3, "Erster Vortrag: Die Eurythmie als sichtbare Sprache", "Dornach", "1924-06-24", 42, 58),
    (4, "Zweiter Vortrag: Der Charakter der einzelnen Laute", "Dornach", "1924-06-25", 59, 73),
    (5, "Dritter Vortrag: Die erlebte und die geformte Gebärde", "Dornach", "1924-06-26", 74, 89),
    (6, "Vierter Vortrag: Die einzelnen Laute und ihre Zusammenhänge", "Dornach", "1924-06-27", 90, 103),
    (7, "Fünfter Vortrag: Der Stimmungsgehalt der Seele bei einer Dichtung", "Dornach", "1924-06-30", 104, 115),
    (8, "Sechster Vortrag: Gemütsstimmungen und Charakteristik einzelner Seelenzustände. - Die Farbe als Gemütsinhalt", "Dornach", "1924-07-01", 116, 129),
    (9, "Siebenter Vortrag: Die plastische Gestaltung des Sprachlichen", "Dornach", "1924-07-02", 130, 141),
    (10, "Achter Vortrag: Das Wort als Bezeichnung und das Wort in seinen Zusammenhängen", "Dornach", "1924-07-03", 142, 156),
    (11, "Neunter Vortrag: Die gestaltete Rede", "Dornach", "1924-07-04", 157, 170),
    (12, "Zehnter Vortrag: Formen, die sich aus der Wesenheit des Menschen ergeben", "Dornach", "1924-07-07", 171, 190),
    (13, "Elfter Vortrag: Das Sich-Hineinleben in Gebärde und Form", "Dornach", "1924-07-08", 191, 201),
    (14, "Zwölfter Vortrag: Moralisch-seelische Heilwirkungen durch das Ausströmen der Menschenseele in Form und Bewegung", "Dornach", "1924-07-09", 202, 214),
    (15, "Dreizehnter Vortrag: Seelenstimmungen, die aus der Geste des Lautes herauszufinden sind", "Dornach", "1924-07-10", 215, 224),
    (16, "Vierzehnter Vortrag: Gliederung der Worte - innere Gliederung der Strophen", "Dornach", "1924-07-11", 225, 239),
    (17, "Fünfzehnter Vortrag: Der ganze Körper muß in der eurythmischen Ausführung Seele werden", "Dornach", "1924-07-12", 240, 256),
]


def printed_to_pdf_page(printed_page):
    """Convert printed page number to PDF page index (0-based)."""
    return printed_page - 3


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


def clean_lecture_text(text, title):
    """Remove the title/header from the beginning of lecture text."""
    lines = text.split('\n')
    cleaned_lines = []
    skip_header = True
    
    for line in lines:
        if skip_header:
            stripped = line.strip()
            if stripped.upper() in title.upper() or title.upper().startswith(stripped.upper()):
                continue
            if not stripped:
                skip_header = False
                continue
            skip_header = False
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)


def update_book(cursor):
    """Update the existing GA279 book record with correct title."""
    cursor.execute("UPDATE books SET title_de = %s WHERE ga_number = %s RETURNING id",
                   ("Eurythmie als sichtbare Sprache (Laut-Eurythmie-Kurs)", "GA279"))
    row = cursor.fetchone()
    if row:
        book_id = row[0]
        print(f"    Updated existing book ID: {book_id}")
        # Clear existing lectures
        cursor.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        print(f"    Cleared existing lectures: {cursor.rowcount}")
        return book_id
    # If no existing book, insert new one
    cursor.execute("""
        INSERT INTO books (ga_number, title_de, pdf_filename)
        VALUES (%s, %s, %s)
        RETURNING id
    """, ("GA279", "Eurythmie als sichtbare Sprache (Laut-Eurythmie-Kurs)", "GA279.pdf"))
    return cursor.fetchone()[0]


def insert_lecture(cursor, book_id, lecture_info, text):
    """Insert a lecture with its paragraphs and sentences."""
    order, title, location, date_str, _, _ = lecture_info
    
    cursor.execute("""
        INSERT INTO lectures (book_id, title_de, lecture_date, location, order_index)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
    """, (book_id, title, date_str, location, order))
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
    print("GA279 Import Script (Production)")
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
        
        # 4. Import each lecture
        print(f"\n[4] Importing {len(LECTURES)} lectures...")
        total_paragraphs = 0
        total_sentences = 0
        
        for lecture_info in LECTURES:
            order, title, location, date_str, start_page, end_page = lecture_info
            
            print(f"\n    Lecture {order}: {title[:50]}...")
            print(f"      Pages: {start_page}-{end_page}")
            
            text = extract_text(pdf_doc, start_page, end_page)
            print(f"      Text length: {len(text)} chars")
            
            text = clean_lecture_text(text, title)
            
            lecture_id, para_count = insert_lecture(cursor, book_id, lecture_info, text)
            total_paragraphs += para_count
            
            cursor.execute("""
                SELECT COUNT(*) FROM sentences s
                JOIN paragraphs p ON s.paragraph_id = p.id
                WHERE p.lecture_id = %s
            """, (lecture_id,))
            sent_count = cursor.fetchone()[0]
            total_sentences += sent_count
            
            print(f"      Lecture ID: {lecture_id}, Paragraphs: {para_count}, Sentences: {sent_count}")
        
        # 5. Commit
        conn.commit()
        print(f"\n[5] COMMIT successful!")
        print(f"    Total: {len(LECTURES)} lectures, {total_paragraphs} paragraphs, {total_sentences} sentences")
        
        # 6. Verify
        print(f"\n[6] Verification...")
        cursor.execute("""
            SELECT COUNT(*) FROM lectures WHERE book_id = %s
        """, (book_id,))
        actual_lectures = cursor.fetchone()[0]
        
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
        
        print(f"\n    Book: GA279 (ID={book_id})")
        print(f"    Lectures: {actual_lectures}")
        print(f"    Paragraphs: {actual_paragraphs}")
        print(f"    Sentences: {actual_sentences}")
        
        cursor.execute("""
            SELECT id, order_index, title_de, location, lecture_date
            FROM lectures WHERE book_id = %s
            ORDER BY order_index LIMIT 20
        """, (book_id,))
        print(f"\n    Lectures in database:")
        for l in cursor.fetchall():
            print(f"      [{l[1]}] {l[2][:50]}... | {l[3]} | {l[4]}")
        
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
