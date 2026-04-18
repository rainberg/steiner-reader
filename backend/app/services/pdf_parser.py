"""
PDF Structure Parser for Rudolf Steiner's works (GA series).

Parses text-based PDFs to extract:
  Book → Lectures → Paragraphs → Sentences

Detection strategy for Steiner GA volumes:
  - Lecture headers: "ERSTER VORTRAG, Dornach, 4. August 1922"
  - Date/location: "Stadt, Tag. Monat Jahr" pattern
  - Paragraphs: separated by blank lines or indentation changes
  - Sentences: spaCy German sentence boundary detection
"""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import pdfplumber
import spacy

# Lazy-loaded German NLP model
_nlp = None


def get_nlp():
    global _nlp
    if _nlp is None:
        _nlp = spacy.load("de_core_news_sm")
    return _nlp


# ─── Data Models ────────────────────────────────────────────

@dataclass
class Sentence:
    text_de: str
    order_index: int = 0


@dataclass
class Paragraph:
    sentences: list[Sentence] = field(default_factory=list)
    order_index: int = 0


@dataclass
class Lecture:
    title_de: str = ""
    date: str = ""
    location: str = ""
    paragraphs: list[Paragraph] = field(default_factory=list)
    order_index: int = 0


@dataclass
class Book:
    title_de: str = ""
    ga_number: str = ""
    lectures: list[Lecture] = field(default_factory=list)


# ─── Regex Patterns ─────────────────────────────────────────

# Date/location: "Dornach, 4. August 1922" or "Berlin, 25. Oktober 1907"
DATE_LOCATION_RE = re.compile(
    r"([A-ZÄÖÜa-zäöüß][A-ZÄÖÜa-zäöüß\s\-]+?),\s+"  # city name
    r"(\d{1,2}\.\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|"
    r"August|September|Oktober|November|Dezember)\s+\d{4})"
)

# Lecture ordinal: "ERSTER VORTRAG", "ZWEITER VORTRAG", etc.
LECTURE_ORDINAL_RE = re.compile(
    r"(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|"
    r"ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWÖLFTER|DREIZEHNTER|VIERZEHNTER|"
    r"FÜNFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|"
    r"ZWANZIGSTER|EINUNDZWANZIGSTER|ZWEIUNDZWANZIGSTER|"
    r"DREIUNDZWANZIGSTER|VIERUNDZWANZIGSTER|FÜNFUNDZWANZIGSTER)\s+VORTRAG",
    re.IGNORECASE
)

# GA number pattern in metadata: "GA 115", "GA115", "Band 115"
GA_RE = re.compile(r"(?:GA|Band)\s*(\d+)", re.IGNORECASE)

# Page number pattern (bottom of page)
PAGE_NUM_RE = re.compile(r"^\s*(\d{1,3})\s*$")

# Footnote marker: superscript numbers like "¹" or "(1)"
FOOTNOTE_RE = re.compile(r"[¹²³⁴⁵⁶⁷⁸⁹⁰]+|\(\d+\)")


# ─── Page Block Extraction ──────────────────────────────────

def extract_page_blocks(page) -> list[dict]:
    """
    Extract text blocks with font metadata from a PDF page.
    Groups consecutive characters by font size and vertical position.
    """
    chars = page.chars
    if not chars:
        return []

    blocks = []
    current_block = {"text": "", "size": 0, "y": 0, "font": ""}

    for c in chars:
        text = c.get("text", "")
        size = round(c.get("size", 0), 1)
        y = round(c.get("top", 0), 0)
        font = c.get("fontname", "")

        # New block if: font size changes, y-position jumps, or font changes
        if (abs(size - current_block["size"]) > 0.5
                or abs(y - current_block["y"]) > 2
                or (font and font != current_block["font"])):
            if current_block["text"].strip():
                blocks.append(current_block)
            current_block = {"text": text, "size": size, "y": y, "font": font}
        else:
            current_block["text"] += text
            current_block["size"] = max(current_block["size"], size)

    if current_block["text"].strip():
        blocks.append(current_block)

    return blocks


# ─── Lecture Header Detection ───────────────────────────────

def detect_lecture_header(blocks: list[dict]) -> Optional[tuple[str, str, str]]:
    """
    Detect lecture header from page blocks.
    Returns (title, location, date) or None.

    Steiner GA typical header format:
      ERSTER VORTRAG
      Dornach, 4. August 1922
    or sometimes just:
      Dornach, 4. August 1922
    """
    # Check first 8 blocks for header patterns
    header_text = ""
    for block in blocks[:8]:
        if block["size"] < 10.5:  # Headers are typically smaller font
            header_text += block["text"] + " "

    header_text = header_text.strip()
    if not header_text:
        return None

    # Look for VORTRAG ordinal
    lecture_match = LECTURE_ORDINAL_RE.search(header_text)
    date_match = DATE_LOCATION_RE.search(header_text)

    if lecture_match:
        title = lecture_match.group(0).strip()
        if date_match:
            location = date_match.group(1).strip()
            date = date_match.group(2).strip()
            return (title, location, date)
        return (title, "", "")

    if date_match:
        # Title = everything before date/location
        title = header_text[:date_match.start()].strip()
        if not title:
            title = "Vortrag"
        location = date_match.group(1).strip()
        date = date_match.group(2).strip()
        return (title, location, date)

    return None


# ─── Text Processing ────────────────────────────────────────

def split_into_sentences(text: str) -> list[str]:
    """Use spaCy to split German text into sentences."""
    nlp = get_nlp()
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]


def split_into_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs by double newlines or indentation."""
    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    
    # Split on double newlines
    paragraphs = re.split(r"\n\s*\n", text)
    
    result = []
    for p in paragraphs:
        p = p.strip()
        if p and len(p) > 15:  # Skip very short "paragraphs" (page nums, headers)
            result.append(p)
    
    return result


def clean_text(text: str) -> str:
    """Clean extracted PDF text."""
    # Remove footnote markers
    text = FOOTNOTE_RE.sub("", text)
    # Fix common PDF extraction issues
    text = re.sub(r"-\n(\w)", r"\1", text)  # Rejoin hyphenated words
    text = re.sub(r"\s+", " ", text)  # Normalize whitespace
    return text.strip()


def detect_front_matter_end(full_text: str) -> int:
    """
    Find where front matter (TOC, preface) ends and content begins.
    Returns the page index (0-based) where content starts.
    
    Heuristic: look for first "VORTRAG" or consistent body text pattern.
    """
    lines = full_text.split("\n")
    for i, line in enumerate(lines):
        if LECTURE_ORDINAL_RE.search(line):
            # Rough estimate: assume ~40 lines per page
            return max(0, (i // 40) - 1)
    return 4  # Default: skip first 5 pages


# ─── Main Parser ────────────────────────────────────────────

def parse_pdf(pdf_path: str, progress_callback=None) -> Book:
    """
    Parse a Steiner PDF into structured Book → Lecture → Paragraph → Sentence.
    
    Args:
        pdf_path: Path to the PDF file
        progress_callback: Optional callable(page_num, total_pages) for progress
    
    Returns:
        Book dataclass with nested structure
    """
    path = Path(pdf_path)
    book = Book()
    
    with pdfplumber.open(str(path)) as pdf:
        total_pages = len(pdf.pages)
        
        # ── Phase 1: Extract metadata ──
        title = pdf.metadata.get("Title", "")
        if title:
            book.title_de = title
            ga_match = GA_RE.search(title)
            if ga_match:
                book.ga_number = f"GA {ga_match.group(1)}"
        
        # ── Phase 2: First pass — extract text and detect lecture headers ──
        page_texts = {}
        page_blocks = {}
        lecture_start_pages = []
        
        for i, page in enumerate(pdf.pages):
            if progress_callback:
                progress_callback(i, total_pages)
            
            text = page.extract_text()
            if text:
                page_texts[i] = text
                blocks = extract_page_blocks(page)
                page_blocks[i] = blocks
                
                header = detect_lecture_header(blocks)
                if header:
                    title_de, location, date = header
                    lecture = Lecture(
                        title_de=title_de,
                        location=location,
                        date=date,
                        order_index=len(book.lectures),
                    )
                    book.lectures.append(lecture)
                    lecture_start_pages.append(i)
        
        # Fallback: no lectures detected → treat entire book as one lecture
        if not book.lectures:
            lecture = Lecture(
                title_de=book.title_de or book.ga_number or "Gesamtwerk",
                order_index=0
            )
            book.lectures.append(lecture)
            lecture_start_pages = [0]
        
        # ── Phase 3: Second pass — extract paragraphs and sentences ──
        for page_num in sorted(page_texts.keys()):
            page_text = page_texts[page_num]
            cleaned = clean_text(page_text)
            
            # Skip very short pages (likely blank or cover)
            if len(cleaned) < 50:
                continue
            
            # Determine which lecture this page belongs to
            lecture_idx = 0
            for idx, start_page in enumerate(lecture_start_pages):
                if page_num >= start_page:
                    lecture_idx = idx
            
            lecture = book.lectures[lecture_idx]
            
            # Extract paragraphs
            paragraphs = split_into_paragraphs(cleaned)
            
            for para_text in paragraphs:
                # Skip lines that are just page numbers
                if PAGE_NUM_RE.match(para_text):
                    continue
                
                paragraph = Paragraph(
                    order_index=len(lecture.paragraphs)
                )
                
                # Split paragraph into sentences using spaCy
                sentences = split_into_sentences(para_text)
                
                for sent_text in sentences:
                    if len(sent_text) > 5:  # Skip fragments
                        sentence = Sentence(
                            text_de=sent_text,
                            order_index=len(paragraph.sentences),
                        )
                        paragraph.sentences.append(sentence)
                
                if paragraph.sentences:
                    lecture.paragraphs.append(paragraph)
        
        # Set book title if not in metadata
        if not book.title_de and book.ga_number:
            book.title_de = f"({book.ga_number})"
        
        if progress_callback:
            progress_callback(total_pages, total_pages)
    
    return book


# ─── Serialization ──────────────────────────────────────────

def book_to_dict(book: Book) -> dict:
    """Convert Book dataclass to JSON-serializable dict."""
    return {
        "title_de": book.title_de,
        "ga_number": book.ga_number,
        "lectures": [
            {
                "title_de": lec.title_de,
                "location": lec.location,
                "date": lec.date,
                "order_index": lec.order_index,
                "paragraphs": [
                    {
                        "order_index": para.order_index,
                        "sentences": [
                            {
                                "text_de": sent.text_de,
                                "order_index": sent.order_index,
                            }
                            for sent in para.sentences
                        ],
                    }
                    for para in lec.paragraphs
                ],
            }
            for lec in book.lectures
        ],
    }


def get_stats(book: Book) -> dict:
    """Get parsing statistics."""
    total_paragraphs = sum(len(lec.paragraphs) for lec in book.lectures)
    total_sentences = sum(
        len(para.sentences)
        for lec in book.lectures
        for para in lec.paragraphs
    )
    return {
        "lectures": len(book.lectures),
        "paragraphs": total_paragraphs,
        "sentences": total_sentences,
    }
