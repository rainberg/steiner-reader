#!/usr/bin/env python3
"""
Simplified GA book importer - text only, with image analysis logging.

This script focuses on fixing the 30 problematic books by:
1. Extracting correct titles from PDF metadata or TOC
2. Proper chapter structure detection
3. Logging image analysis for later processing
4. Updating existing database records

Use for batch re-import of problematic GA books.
"""

import re
import sys
import fitz  # PyMuPDF
import psycopg2
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional

# === CONFIG ===
PRODUCTION_DB_HOST = "localhost"  # On production server, localhost connects to Docker PostgreSQL
PRODUCTION_DB_PORT = 5432
PRODUCTION_DB_NAME = "steiner_reader"
PRODUCTION_DB_USER = "steiner"
PRODUCTION_DB_PASSWORD = "password"

PRODUCTION_PDF_DIR = "/opt/steiner-reader/books"
LOCAL_PDF_DIR = "/home/ubuntu/steiner-reader/data/pdf"

@dataclass
class ChapterInfo:
    order_index: int
    title_de: str
    start_page: int  # printed page number
    end_page: int   # printed page number

@dataclass
class ImageAnalysis:
    total_pages: int
    pages_with_images: int
    pages_with_large_images: int  # >1000x1000 pixels
    estimated_full_page_scan: bool
    recommendation: str

class SimpleGAImporter:
    """Simple importer focused on text correction."""
    
    def __init__(self, ga_number: str):
        self.ga_number = ga_number
        self.pdf_path = self.find_pdf()
        self.pdf_doc = None
        self.chapters: List[ChapterInfo] = []
        self.image_analysis: Optional[ImageAnalysis] = None
        
    def find_pdf(self) -> Path:
        """Find PDF file for GA number."""
        ga_num = self.ga_number[2:].zfill(3)  # GA001 -> 001
        pdf_name = f"GA{ga_num}.pdf"
        
        # Check local directory
        local_path = Path(LOCAL_PDF_DIR) / pdf_name
        if local_path.exists():
            return local_path
            
        # Check production directory
        prod_path = Path(PRODUCTION_PDF_DIR) / pdf_name
        if prod_path.exists():
            return prod_path
            
        raise FileNotFoundError(f"PDF not found for {self.ga_number}")
    
    def connect_db(self):
        """Connect to production database."""
        return psycopg2.connect(
            host=PRODUCTION_DB_HOST,
            port=PRODUCTION_DB_PORT,
            database=PRODUCTION_DB_NAME,
            user=PRODUCTION_DB_USER,
            password=PRODUCTION_DB_PASSWORD
        )
    
    def extract_title_from_pdf(self) -> str:
        """Extract title from PDF metadata or first pages."""
        if not self.pdf_doc:
            return self.ga_number
            
        # Try PDF metadata first
        metadata = self.pdf_doc.metadata
        if metadata.get('title') and len(metadata['title']) > 10:
            title = metadata['title']
            # Clean up common issues
            title = re.sub(r'^\s*RUDOLF\s+STEINER\s*[-:]?\s*', '', title, flags=re.IGNORECASE)
            title = re.sub(r'\s*\.pdf$', '', title, flags=re.IGNORECASE)
            if len(title) > 10:
                return title
        
        # Try to extract from TOC or first chapter title
        if self.chapters and len(self.chapters) > 0:
            # Use first chapter title as base
            first_chapter_title = self.chapters[0].title_de
            # Clean it up
            first_chapter_title = re.sub(r'^\d+[\.\)]\s*', '', first_chapter_title)
            first_chapter_title = re.sub(r'^[IVXLCDM]+[\.\)]\s*', '', first_chapter_title)
            first_chapter_title = re.sub(r'^[A-Z]\s*', '', first_chapter_title)
            
            if len(first_chapter_title) > 20:
                # For GA001, the first chapter is "Zur Einführung. Aus «Mein Lebensgang», Kap. VI"
                # We want something like "Einleitungen zu Goethes Naturwissenschaftliche Schriften"
                # Look for the actual book title in the first few pages
                for page_idx in range(min(3, len(self.pdf_doc))):
                    page = self.pdf_doc[page_idx]
                    text = page.get_text()
                    
                    # Look for patterns like "Einleitungen zu Goethes..."
                    if 'Einleitungen zu Goethes' in text:
                        lines = text.split('\n')
                        for line in lines:
                            if 'Einleitungen zu Goethes' in line:
                                return line.strip()
        
        # Fallback: use GA number with descriptive text
        return f"{self.ga_number} - Rudolf Steiner"
    
    def find_toc_page(self) -> Optional[int]:
        """Find the table of contents page."""
        if not self.pdf_doc:
            return None
            
        for page_idx in range(min(50, len(self.pdf_doc))):
            page = self.pdf_doc[page_idx]
            text = page.get_text().upper()
            
            # TOC markers
            if 'INHALT' in text or 'INHALTSVERZEICHNIS' in text:
                # Verify it's actually a TOC by checking for page numbers
                lines = text.split('\n')
                page_num_count = sum(1 for line in lines if re.search(r'\d+\s*$', line.strip()))
                if page_num_count >= 3:
                    return page_idx
        
        return None
    
    def parse_toc_entries(self, toc_page_idx: int) -> List[Tuple[str, int]]:
        """Parse TOC entries from a page."""
        entries = []
        if not self.pdf_doc or toc_page_idx >= len(self.pdf_doc):
            return entries
            
        page = self.pdf_doc[toc_page_idx]
        text = page.get_text()
        
        # Simple parsing: look for lines with page numbers at the end
        lines = text.split('\n')
        current_entry = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Check if line ends with a page number
            match = re.search(r'(\d+)\s*$', line)
            if match:
                page_num = int(match.group(1))
                # Combine with previous line if we were building an entry
                if current_entry:
                    entry_text = current_entry + " " + line[:match.start()].strip()
                else:
                    entry_text = line[:match.start()].strip()
                
                # Clean up the entry
                entry_text = re.sub(r'\.+$', '', entry_text)
                entry_text = re.sub(r'^\d+[\.\)]\s*', '', entry_text)  # Remove numbering
                
                if entry_text and len(entry_text) > 3:
                    entries.append((entry_text, page_num))
                
                current_entry = ""
            else:
                # This might be a continuation line
                if line and not line.isdigit():  # Skip pure number lines
                    current_entry = line if not current_entry else current_entry + " " + line
        
        return entries
    
    def detect_chapters(self) -> List[ChapterInfo]:
        """Detect chapter structure."""
        chapters = []
        
        # Try to find and parse TOC
        toc_page_idx = self.find_toc_page()
        if toc_page_idx is not None:
            print(f"  Found TOC on page {toc_page_idx + 1}")
            entries = self.parse_toc_entries(toc_page_idx)
            
            if entries:
                print(f"  Parsed {len(entries)} TOC entries")
                
                for i, (title, page_num) in enumerate(entries):
                    # Determine end page
                    if i < len(entries) - 1:
                        end_page = entries[i+1][1] - 1
                    else:
                        # Last chapter: go to end of book
                        end_page = len(self.pdf_doc)
                    
                    chapters.append(ChapterInfo(
                        order_index=i + 1,
                        title_de=title,
                        start_page=page_num,
                        end_page=end_page
                    ))
        
        # If no chapters found via TOC, try heuristic
        if not chapters:
            print("  No TOC found, checking for chapter markers in text...")
            
            # Look for chapter markers in first 100 pages
            chapter_markers = []
            for page_idx in range(min(100, len(self.pdf_doc))):
                page = self.pdf_doc[page_idx]
                text = page.get_text()
                
                # Look for Roman numerals or numbered chapters
                lines = text.split('\n')
                for line in lines:
                    line = line.strip()
                    # Patterns like "I.", "II.", "1.", "Kapitel 1", etc.
                    if (re.match(r'^(I{1,3}|IV|V|VI{0,3}|IX|X{1,3})\.', line) or
                        re.match(r'^\d+\.', line) or
                        re.match(r'^Kapitel\s+\d+', line, re.IGNORECASE) or
                        re.match(r'^Teil\s+[IVXLCDM]+', line, re.IGNORECASE)):
                        
                        # Extract title
                        title = re.sub(r'^(I{1,3}|IV|V|VI{0,3}|IX|X{1,3})\.\s*', '', line)
                        title = re.sub(r'^\d+\.\s*', '', title)
                        title = re.sub(r'^Kapitel\s+\d+\s*[:\.]?\s*', '', title, flags=re.IGNORECASE)
                        title = re.sub(r'^Teil\s+[IVXLCDM]+\s*[:\.]?\s*', '', title, flags=re.IGNORECASE)
                        
                        if title and len(title) > 3:
                            chapter_markers.append((page_idx + 1, title))
            
            if chapter_markers:
                print(f"  Found {len(chapter_markers)} chapter markers")
                
                for i, (page_num, title) in enumerate(chapter_markers):
                    if i < len(chapter_markers) - 1:
                        end_page = chapter_markers[i+1][0] - 1
                    else:
                        end_page = len(self.pdf_doc)
                    
                    chapters.append(ChapterInfo(
                        order_index=i + 1,
                        title_de=title,
                        start_page=page_num,
                        end_page=end_page
                    ))
        
        # Final fallback: single chapter
        if not chapters:
            print("  Using single chapter for entire book")
            title = self.extract_title_from_pdf()
            chapters.append(ChapterInfo(
                order_index=1,
                title_de=title,
                start_page=1,
                end_page=len(self.pdf_doc)
            ))
        
        return chapters
    
    def analyze_images(self) -> ImageAnalysis:
        """Analyze images in PDF for reporting."""
        if not self.pdf_doc:
            return ImageAnalysis(0, 0, 0, False, "No PDF loaded")
        
        total_pages = len(self.pdf_doc)
        pages_with_images = 0
        pages_with_large_images = 0
        full_page_scan_pages = 0
        
        for page_idx in range(total_pages):
            page = self.pdf_doc[page_idx]
            images = page.get_images()
            text = page.get_text()
            text_length = len(text.strip())
            
            if images:
                pages_with_images += 1
                
                # Check image sizes
                large_image_on_page = False
                for img_info in images:
                    xref = img_info[0]
                    pix = fitz.Pixmap(self.pdf_doc, xref)
                    
                    # Check if large image
                    if pix.width > 1000 and pix.height > 1000:
                        large_image_on_page = True
                        
                        # Check if full-page scan (large image with little text)
                        if text_length < 500:
                            full_page_scan_pages += 1
                    
                    pix = None
                
                if large_image_on_page:
                    pages_with_large_images += 1
        
        # Determine if this is mostly full-page scans
        estimated_full_page_scan = False
        if total_pages > 0:
            full_page_ratio = full_page_scan_pages / total_pages
            estimated_full_page_scan = full_page_ratio > 0.5
        
        # Generate recommendation
        if estimated_full_page_scan:
            recommendation = "Full-page scans detected. Consider OCR enhancement or page image viewer."
        elif pages_with_large_images > 0:
            recommendation = f"Contains {pages_with_large_images} pages with large images. May need special handling."
        elif pages_with_images > 0:
            recommendation = f"Contains {pages_with_images} pages with small images (likely illustrations)."
        else:
            recommendation = "No significant images found."
        
        return ImageAnalysis(
            total_pages=total_pages,
            pages_with_images=pages_with_images,
            pages_with_large_images=pages_with_large_images,
            estimated_full_page_scan=estimated_full_page_scan,
            recommendation=recommendation
        )
    
    def get_book_id(self, cursor) -> int:
        """Get existing book ID."""
        cursor.execute(
            "SELECT id, title_de FROM books WHERE ga_number = %s",
            (self.ga_number,)
        )
        result = cursor.fetchone()
        
        if result:
            book_id, current_title = result
            print(f"  Existing book ID: {book_id}")
            print(f"  Current title: {current_title[:80]}...")
            return book_id
        else:
            raise ValueError(f"Book {self.ga_number} not found in database")
    
    def update_book_title(self, cursor, book_id: int, new_title: str):
        """Update book title if it's a placeholder."""
        cursor.execute(
            "SELECT title_de FROM books WHERE id = %s",
            (book_id,)
        )
        current_title = cursor.fetchone()[0]
        
        # Check if current title is a placeholder
        placeholder_indicators = [
            'Rudolf Steiner Online Archiv',
            'http://home.att.net',
            '...',
            'INHALT...',
            'RUDOLF STEINER GESAMTAUSGABE...'
        ]
        
        is_placeholder = any(indicator in current_title for indicator in placeholder_indicators)
        
        if is_placeholder or len(current_title) < 10:
            print(f"  Updating placeholder title to: {new_title[:80]}...")
            cursor.execute(
                "UPDATE books SET title_de = %s WHERE id = %s",
                (new_title, book_id)
            )
            return True
        else:
            print(f"  Title already OK: {current_title[:80]}...")
            return False
    
    def clear_existing_lectures(self, cursor, book_id: int):
        """Delete existing lectures and their content."""
        print(f"  Clearing existing lectures for book {book_id}...")
        cursor.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        print(f"  Deleted existing lectures")
    
    def extract_chapter_text(self, start_page: int, end_page: int) -> str:
        """Extract text for a chapter."""
        text_parts = []
        
        # Convert to 0-based indices (assuming printed page 1 = PDF page 0)
        start_idx = start_page - 1
        end_idx = end_page - 1
        
        for page_idx in range(start_idx, min(end_idx + 1, len(self.pdf_doc))):
            page = self.pdf_doc[page_idx]
            text = page.get_text()
            text_parts.append(text)
        
        return '\n'.join(text_parts)
    
    def insert_chapter(self, cursor, book_id: int, chapter: ChapterInfo, text: str) -> Tuple[int, int]:
        """Insert a chapter with paragraphs and sentences."""
        # Insert lecture
        cursor.execute(
            """
            INSERT INTO lectures (book_id, order_index, title_de, created_at)
            VALUES (%s, %s, %s, NOW())
            RETURNING id
            """,
            (book_id, chapter.order_index, chapter.title_de)
        )
        lecture_id = cursor.fetchone()[0]
        
        # Split into paragraphs
        paragraphs = re.split(r'\n\s*\n', text)
        paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 20]
        
        para_count = 0
        for para_idx, para_text in enumerate(paragraphs):
            cursor.execute(
                """
                INSERT INTO paragraphs (lecture_id, order_index, created_at)
                VALUES (%s, %s, NOW())
                RETURNING id
                """,
                (lecture_id, para_idx + 1)
            )
            paragraph_id = cursor.fetchone()[0]
            
            # Split into sentences
            para_text = re.sub(r'\s+', ' ', para_text).strip()
            sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', para_text)
            sentences = [s.strip() for s in sentences if len(s.strip()) > 5]
            
            for sent_idx, sent_text in enumerate(sentences):
                cursor.execute(
                    """
                    INSERT INTO sentences (paragraph_id, order_index, text_de, created_at)
                    VALUES (%s, %s, %s, NOW())
                    """,
                    (paragraph_id, sent_idx + 1, sent_text)
                )
            
            para_count += 1
        
        return lecture_id, para_count
    
    def run_import(self):
        """Main import process."""
        print(f"\n=== Processing {self.ga_number} ===")
        
        # Open PDF
        self.pdf_doc = fitz.open(str(self.pdf_path))
        print(f"  PDF: {len(self.pdf_doc)} pages")
        
        # Analyze images (for reporting only)
        self.image_analysis = self.analyze_images()
        print(f"  Image analysis: {self.image_analysis.recommendation}")
        
        # Extract title
        book_title = self.extract_title_from_pdf()
        print(f"  Extracted title: {book_title[:80]}...")
        
        # Detect chapters
        self.chapters = self.detect_chapters()
        print(f"  Detected {len(self.chapters)} chapters")
        
        # Connect to database
        conn = self.connect_db()
        cursor = conn.cursor()
        
        try:
            # Get book ID
            book_id = self.get_book_id(cursor)
            
            # Update title if needed
            title_updated = self.update_book_title(cursor, book_id, book_title)
            
            # Clear existing lectures
            self.clear_existing_lectures(cursor, book_id)
            
            # Insert new chapters
            total_paragraphs = 0
            total_sentences = 0
            
            for chapter in self.chapters:
                print(f"  Chapter {chapter.order_index}: {chapter.title_de[:60]}...")
                
                # Extract text
                text = self.extract_chapter_text(chapter.start_page, chapter.end_page)
                
                # Insert chapter
                lecture_id, para_count = self.insert_chapter(cursor, book_id, chapter, text)
                total_paragraphs += para_count
                
                # Count sentences
                cursor.execute(
                    """
                    SELECT COUNT(*) FROM sentences s
                    JOIN paragraphs p ON s.paragraph_id = p.id
                    WHERE p.lecture_id = %s
                    """,
                    (lecture_id,)
                )
                sent_count = cursor.fetchone()[0]
                total_sentences += sent_count
                
                print(f"    -> ID: {lecture_id}, Paragraphs: {para_count}, Sentences: {sent_count}")
            
            # Commit
            conn.commit()
            
            print(f"\n  ✓ Import successful!")
            print(f"     Chapters: {len(self.chapters)}")
            print(f"     Paragraphs: {total_paragraphs}")
            print(f"     Sentences: {total_sentences}")
            print(f"     Image status: {self.image_analysis.recommendation}")
            
            if self.image_analysis.estimated_full_page_scan:
                print(f"     ⚠️  Full-page scan book - needs special image handling")
            
            return True
            
        except Exception as e:
            print(f"\n  ✗ Error: {e}")
            conn.rollback()
            return False
            
        finally:
            cursor.close()
            conn.close()
            if self.pdf_doc:
                self.pdf_doc.close()

def main():
    """Command-line interface."""
    if len(sys.argv) != 2:
        print("Usage: python3 import_ga_simple.py <GA_NUMBER>")
        print("Example: python3 import_ga_simple.py GA001")
        sys.exit(1)
    
    ga_number = sys.argv[1].upper()
    
    try:
        importer = SimpleGAImporter(ga_number)
        success = importer.run_import()
        
        if success:
            print(f"\n✅ {ga_number} imported successfully")
            sys.exit(0)
        else:
            print(f"\n❌ {ga_number} import failed")
            sys.exit(1)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()