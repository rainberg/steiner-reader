#!/usr/bin/env python3
"""
Generic import script for GA books with text and image extraction.

Features:
1. Auto-detect GA number from PDF filename
2. Parse table of contents (TOC) from PDF
3. Extract chapter text and structure
4. Identify and extract standalone illustrations (not full-page scans)
5. Record full-page scan books for later processing
6. Insert into production PostgreSQL database
"""

import re
import os
import json
import fitz  # PyMuPDF
import psycopg2
from pathlib import Path
from dataclasses import dataclass
from typing import List, Tuple, Optional, Dict, Any

# === CONFIG ===
PRODUCTION_SERVER = "66.154.112.162"
PRODUCTION_DB_HOST = "localhost"
PRODUCTION_DB_PORT = 5432
PRODUCTION_DB_NAME = "steiner_reader"
PRODUCTION_DB_USER = "steiner"
PRODUCTION_DB_PASSWORD = "password"

PRODUCTION_PDF_DIR = "/opt/steiner-reader/books"
PRODUCTION_IMAGES_DIR = "/opt/steiner-reader/uploads/images"
LOCAL_PDF_DIR = "/home/ubuntu/steiner-reader/data/pdf"

# === CONSTANTS ===
FULL_PAGE_THRESHOLD = 1000  # pixels, width and height
TEXT_DENSITY_THRESHOLD = 10.0  # characters per 10k pixels

@dataclass
class ChapterInfo:
    """Information about a chapter/lecture."""
    order_index: int
    title_de: str
    start_page: int  # printed page number
    end_page: int   # printed page number
    
@dataclass  
class ImageInfo:
    """Information about an extracted image."""
    xref: int
    page_num: int  # 0-based PDF page index
    width: int
    height: int
    filename: str
    is_full_page: bool
    lecture_id: Optional[int] = None
    after_paragraph_id: Optional[int] = None

class GAImporter:
    """Main importer class for GA books."""
    
    def __init__(self, ga_number: str, pdf_path: Path, production: bool = True):
        self.ga_number = ga_number
        self.pdf_path = pdf_path
        self.production = production
        
        # Database connection
        if production:
            self.db_host = PRODUCTION_DB_HOST
            self.db_port = PRODUCTION_DB_PORT
            self.db_name = PRODUCTION_DB_NAME
            self.db_user = PRODUCTION_DB_USER
            self.db_password = PRODUCTION_DB_PASSWORD
            self.images_dir = Path(PRODUCTION_IMAGES_DIR)
        else:
            # Local/test mode
            self.db_host = "localhost"
            self.db_port = 5432
            self.db_name = "steiner_reader"
            self.db_user = "steiner"
            self.db_password = "password"
            self.images_dir = Path("/tmp/steiner_images")
            
        self.images_dir.mkdir(parents=True, exist_ok=True)
        
        # State
        self.pdf_doc = None
        self.book_id = None
        self.chapters: List[ChapterInfo] = []
        self.images: List[ImageInfo] = []
        self.full_page_scan_detected = False
        
    def connect_db(self):
        """Connect to PostgreSQL database."""
        return psycopg2.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_password
        )
    
    def extract_ga_number_from_filename(self, filename: str) -> Optional[str]:
        """Extract GA number from filename (e.g., GA001.pdf -> GA001)."""
        match = re.search(r'GA\d+', filename, re.IGNORECASE)
        return match.group(0).upper() if match else None
    
    def find_toc_pages(self) -> List[int]:
        """Find pages containing table of contents."""
        toc_pages = []
        if not self.pdf_doc:
            return toc_pages
            
        for page_idx in range(min(50, len(self.pdf_doc))):
            page = self.pdf_doc[page_idx]
            text = page.get_text().upper()
            
            # TOC markers
            toc_keywords = ['INHALT', 'INHALTSVERZEICHNIS', 'VORTRAG', 'VORTRÄGE', 
                           'KAPITEL', 'TEIL', 'INHALTSÜBERSICHT']
            
            if any(keyword in text for keyword in toc_keywords):
                # Check for page numbers pattern (typical in TOC)
                lines = text.split('\n')
                page_num_lines = 0
                for line in lines:
                    if re.search(r'\d+\s*$', line.strip()) and len(line.strip()) > 10:
                        page_num_lines += 1
                
                if page_num_lines >= 3:  # At least 3 TOC entries
                    toc_pages.append(page_idx)
                    
        return toc_pages
    
    def parse_toc_from_page(self, page_idx: int) -> List[Tuple[str, int]]:
        """Parse TOC entries from a specific page.
        
        Returns list of (title, page_number) tuples.
        """
        entries = []
        if not self.pdf_doc or page_idx >= len(self.pdf_doc):
            return entries
            
        page = self.pdf_doc[page_idx]
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Pattern: title ... page_number
            # Try to find page number at the end
            match = re.search(r'(\d+)\s*$', line)
            if match:
                page_num = int(match.group(1))
                title = line[:match.start()].strip()
                # Remove trailing dots
                title = re.sub(r'\.+$', '', title)
                
                if title and len(title) > 3:
                    entries.append((title, page_num))
                    
        return entries
    
    def detect_chapter_structure(self) -> List[ChapterInfo]:
        """Detect chapter structure from TOC or heuristic analysis."""
        chapters = []
        
        # Try to find TOC
        toc_pages = self.find_toc_pages()
        if toc_pages:
            print(f"Found TOC on pages: {[p+1 for p in toc_pages]}")
            # Parse first TOC page
            entries = self.parse_toc_from_page(toc_pages[0])
            
            for i, (title, page_num) in enumerate(entries):
                # Determine end page (next chapter's start page - 1)
                end_page = page_num
                if i < len(entries) - 1:
                    end_page = entries[i+1][1] - 1
                else:
                    # Last chapter: go to end of PDF
                    end_page = len(self.pdf_doc)
                    
                chapters.append(ChapterInfo(
                    order_index=i+1,
                    title_de=title,
                    start_page=page_num,
                    end_page=end_page
                ))
                
            print(f"Parsed {len(chapters)} chapters from TOC")
            
        if not chapters:
            print("No TOC found, using single chapter for entire book")
            # Fallback: single chapter for entire book
            chapters.append(ChapterInfo(
                order_index=1,
                title_de=f"{self.ga_number} - Complete Book",
                start_page=1,
                end_page=len(self.pdf_doc)
            ))
            
        return chapters
    
    def analyze_page_images(self, page_idx: int) -> Tuple[bool, List[ImageInfo]]:
        """Analyze images on a page.
        
        Returns: (is_full_page_scan, list_of_image_info)
        """
        if not self.pdf_doc or page_idx >= len(self.pdf_doc):
            return False, []
            
        page = self.pdf_doc[page_idx]
        images = page.get_images()
        text = page.get_text()
        text_length = len(text.strip())
        
        page_images = []
        is_full_page = False
        
        for img_info in images:
            xref = img_info[0]
            pix = fitz.Pixmap(self.pdf_doc, xref)
            
            image_info = ImageInfo(
                xref=xref,
                page_num=page_idx,
                width=pix.width,
                height=pix.height,
                filename=f"{self.ga_number}_p{page_idx+1}_{xref}.png",
                is_full_page=False
            )
            
            # Check if this is a full-page scan
            # Criteria: large image with little text
            if (pix.width > FULL_PAGE_THRESHOLD and 
                pix.height > FULL_PAGE_THRESHOLD and
                text_length < 500):  # Very little text
                image_info.is_full_page = True
                is_full_page = True
                self.full_page_scan_detected = True
                print(f"  Page {page_idx+1}: Full-page scan detected "
                      f"({pix.width}x{pix.height}, {text_length} chars)")
            
            page_images.append(image_info)
            pix = None
            
        return is_full_page, page_images
    
    def extract_and_save_image(self, image_info: ImageInfo) -> bool:
        """Extract and save an image to disk."""
        try:
            pix = fitz.Pixmap(self.pdf_doc, image_info.xref)
            output_path = self.images_dir / image_info.filename
            pix.save(str(output_path))
            pix = None
            return True
        except Exception as e:
            print(f"Error saving image {image_info.filename}: {e}")
            return False
    
    def get_or_create_book_id(self, cursor) -> int:
        """Get existing book ID or create new entry."""
        # Try to find existing book
        cursor.execute(
            "SELECT id FROM books WHERE ga_number = %s",
            (self.ga_number,)
        )
        result = cursor.fetchone()
        
        if result:
            book_id = result[0]
            print(f"Found existing book ID: {book_id}")
            
            # Update title if it's a placeholder
            cursor.execute(
                "SELECT title_de FROM books WHERE id = %s",
                (book_id,)
            )
            title = cursor.fetchone()[0]
            
            if "Rudolf Steiner Online Archiv" in title or title.endswith("..."):
                # Update with better title (from first chapter or PDF metadata)
                new_title = self.chapters[0].title_de if self.chapters else self.ga_number
                cursor.execute(
                    "UPDATE books SET title_de = %s WHERE id = %s",
                    (new_title, book_id)
                )
                print(f"Updated placeholder title to: {new_title}")
                
            return book_id
        else:
            # Create new book
            title = self.chapters[0].title_de if self.chapters else self.ga_number
            cursor.execute(
                """
                INSERT INTO books (ga_number, title_de, created_at)
                VALUES (%s, %s, NOW())
                RETURNING id
                """,
                (self.ga_number, title)
            )
            book_id = cursor.fetchone()[0]
            print(f"Created new book ID: {book_id}")
            return book_id
    
    def insert_chapter(self, cursor, book_id: int, chapter: ChapterInfo, 
                      text: str) -> Tuple[int, int]:
        """Insert a chapter and its paragraphs/sentences."""
        # Insert lecture/chapter
        cursor.execute(
            """
            INSERT INTO lectures (book_id, order_index, title_de, created_at)
            VALUES (%s, %s, %s, NOW())
            ON CONFLICT (book_id, order_index) DO UPDATE
            SET title_de = EXCLUDED.title_de
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
    
    def insert_image(self, cursor, image_info: ImageInfo) -> int:
        """Insert image record into database."""
        cursor.execute(
            """
            INSERT INTO lecture_images 
            (lecture_id, filename, page_number, width, height, order_index, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            RETURNING id
            """,
            (image_info.lecture_id, image_info.filename, image_info.page_num + 1,
             image_info.width, image_info.height, 0)
        )
        return cursor.fetchone()[0]
    
    def run(self):
        """Main import process."""
        print(f"=== Importing {self.ga_number} ===")
        
        # Open PDF
        self.pdf_doc = fitz.open(str(self.pdf_path))
        print(f"PDF opened: {len(self.pdf_doc)} pages")
        
        # Detect chapter structure
        self.chapters = self.detect_chapter_structure()
        
        # Connect to database
        conn = self.connect_db()
        cursor = conn.cursor()
        
        try:
            # Get or create book ID
            self.book_id = self.get_or_create_book_id(cursor)
            
            # Process each chapter
            total_paragraphs = 0
            total_sentences = 0
            total_images = 0
            
            for chapter in self.chapters:
                print(f"\nProcessing chapter {chapter.order_index}: {chapter.title_de}")
                print(f"  Pages: {chapter.start_page} - {chapter.end_page}")
                
                # Extract text for this chapter
                text_parts = []
                chapter_images = []
                
                # Convert printed page numbers to PDF indices (0-based)
                # Assuming printed page 1 = PDF page 0 (may need adjustment)
                start_pdf = chapter.start_page - 1
                end_pdf = chapter.end_page - 1
                
                for page_idx in range(start_pdf, min(end_pdf + 1, len(self.pdf_doc))):
                    page = self.pdf_doc[page_idx]
                    text = page.get_text()
                    text_parts.append(text)
                    
                    # Analyze images on this page
                    is_full_page, page_images = self.analyze_page_images(page_idx)
                    
                    # Only save non-full-page images (illustrations)
                    for img_info in page_images:
                        if not img_info.is_full_page:
                            # Save image
                            if self.extract_and_save_image(img_info):
                                img_info.lecture_id = None  # Will be set after chapter insert
                                chapter_images.append(img_info)
                                total_images += 1
                
                full_text = '\n'.join(text_parts)
                
                # Insert chapter
                lecture_id, para_count = self.insert_chapter(
                    cursor, self.book_id, chapter, full_text
                )
                total_paragraphs += para_count
                
                # Count sentences for this chapter
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
                
                print(f"  Chapter ID: {lecture_id}, Paragraphs: {para_count}, "
                      f"Sentences: {sent_count}")
                
                # Insert images for this chapter
                for img_info in chapter_images:
                    img_info.lecture_id = lecture_id
                    self.insert_image(cursor, img_info)
                    print(f"    Image: {img_info.filename} ({img_info.width}x{img_info.height})")
            
            # Commit
            conn.commit()
            
            print(f"\n=== Import Complete ===")
            print(f"Book: {self.ga_number} (ID={self.book_id})")
            print(f"Chapters: {len(self.chapters)}")
            print(f"Paragraphs: {total_paragraphs}")
            print(f"Sentences: {total_sentences}")
            print(f"Images extracted: {total_images}")
            
            if self.full_page_scan_detected:
                print(f"\n⚠️  Full-page scans detected in {self.ga_number}")
                print("   This book appears to be a scanned PDF with images as text background.")
                print("   Consider OCR enhancement or separate page image viewer.")
            
        except Exception as e:
            print(f"\nERROR: {e}")
            conn.rollback()
            raise
        finally:
            cursor.close()
            conn.close()
            if self.pdf_doc:
                self.pdf_doc.close()
        
        print("\nDone.")

def main():
    """Command-line interface."""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description='Import GA book with images')
    parser.add_argument('ga_number', help='GA number (e.g., GA001)')
    parser.add_argument('--pdf', help='Path to PDF file (optional)')
    parser.add_argument('--production', action='store_true', 
                       help='Import to production server')
    parser.add_argument('--local', action='store_true',
                       help='Import to local database')
    
    args = parser.parse_args()
    
    # Determine PDF path
    if args.pdf:
        pdf_path = Path(args.pdf)
    else:
        # Try to find PDF in standard locations
        ga_num = args.ga_number[2:].zfill(3)  # GA001 -> 001
        pdf_name = f"GA{ga_num}.pdf"
        
        # Check local directory first
        local_path = Path(LOCAL_PDF_DIR) / pdf_name
        if local_path.exists():
            pdf_path = local_path
        else:
            # Check production directory
            prod_path = Path(PRODUCTION_PDF_DIR) / pdf_name
            if prod_path.exists():
                pdf_path = prod_path
            else:
                print(f"Error: PDF not found for {args.ga_number}")
                print(f"  Looked in: {local_path}")
                print(f"  Looked in: {prod_path}")
                sys.exit(1)
    
    # Determine mode
    production = args.production or (not args.local)
    
    # Run importer
    importer = GAImporter(args.ga_number, pdf_path, production)
    importer.run()

if __name__ == "__main__":
    main()