"""
PDF Structure Parser for Rudolf Steiner's works (GA series).
Memory-optimized: processes pages one at a time.

Parses text-based PDFs to extract:
  Book → Lectures → Paragraphs → Sentences
"""

import gc
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Callable

import pdfplumber

# Lazy-loaded spaCy (optional, falls back to regex)
_nlp = None
_nlp_loaded = False


def get_nlp():
    global _nlp, _nlp_loaded
    if not _nlp_loaded:
        _nlp_loaded = True
        try:
            import spacy
            _nlp = spacy.load("de_core_news_sm")
        except (ImportError, OSError):
            _nlp = None
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

DATE_LOCATION_RE = re.compile(
    r"([A-ZÄÖÜa-zäöüß][A-ZÄÖÜa-zäöüß\s\-]+?),\s+"
    r"(\d{1,2}\.\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|"
    r"August|September|Oktober|November|Dezember)\s+\d{4})"
)

LECTURE_ORDINAL_RE = re.compile(
    r"(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|"
    r"ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWÖLFTER|DREIZEHNTER|VIERZEHNTER|"
    r"FÜNFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|"
    r"ZWANZIGSTER|EINUNDZWANZIGSTER|ZWEIUNDZWANZIGSTER|"
    r"DREIUNDZWANZIGSTER|VIERUNDZWANZIGSTER|FÜNFUNDZWANZIGSTER)\s+VORTRAG",
    re.IGNORECASE
)

GA_RE = re.compile(r"(?:GA|Band)\s*(\d+)", re.IGNORECASE)

PAGE_NUM_RE = re.compile(r"^\s*(\d{1,3})\s*$")

FOOTNOTE_RE = re.compile(r"[¹²³⁴⁵⁶⁷⁸⁹⁰]+|\(\d+\)")


# ─── Text Processing ────────────────────────────────────────

def split_into_sentences(text: str) -> list[str]:
    """Split German text into sentences. spaCy if available, else regex."""
    nlp = get_nlp()
    if nlp is not None:
        doc = nlp(text)
        return [sent.text.strip() for sent in doc.sents if sent.text.strip()]
    # Regex fallback
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', text)
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]


def split_into_paragraphs(text: str) -> list[str]:
    """Split text by double newlines."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = re.split(r"\n\s*\n", text)
    return [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 15]


def clean_text(text: str) -> str:
    """Clean extracted PDF text."""
    text = FOOTNOTE_RE.sub("", text)
    text = re.sub(r"-\n(\w)", r"\1", text)  # Rejoin hyphenated words
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ─── Header Detection (per-page) ────────────────────────────

def detect_lecture_header_from_text(text: str) -> Optional[tuple[str, str, str]]:
    """
    Detect lecture header from extracted page text.
    Returns (title, location, date) or None.
    """
    # Check first 500 chars for header patterns
    header_region = text[:500]
    
    lecture_match = LECTURE_ORDINAL_RE.search(header_region)
    date_match = DATE_LOCATION_RE.search(header_region)
    
    if lecture_match:
        title = lecture_match.group(0).strip()
        if date_match:
            return (title, date_match.group(1).strip(), date_match.group(2).strip())
        return (title, "", "")
    
    if date_match:
        title = header_region[:date_match.start()].strip()
        if not title:
            title = "Vortrag"
        return (title, date_match.group(1).strip(), date_match.group(2).strip())
    
    return None


# ─── Main Parser (memory-optimized) ─────────────────────────

def parse_pdf(pdf_path: str, progress_callback: Optional[Callable] = None) -> Book:
    """
    Parse a Steiner PDF into structured Book → Lecture → Paragraph → Sentence.
    
    Memory-optimized: processes one page at a time and releases resources.
    """
    path = Path(pdf_path)
    book = Book()
    
    with pdfplumber.open(str(path)) as pdf:
        total_pages = len(pdf.pages)
        
        # Extract metadata (lightweight)
        title = pdf.metadata.get("Title", "")
        if title:
            book.title_de = title
            ga_match = GA_RE.search(title)
            if ga_match:
                book.ga_number = f"GA {ga_match.group(1)}"
        
        current_lecture = None
        lecture_order = 0
        
        # Process pages one at a time (memory-efficient)
        for i, page in enumerate(pdf.pages):
            if progress_callback:
                progress_callback(i, total_pages)
            
            # Extract text only (no char-level data to save memory)
            text = page.extract_text()
            if not text or len(text.strip()) < 30:
                continue
            
            cleaned = clean_text(text)
            
            # Check for lecture header
            header = detect_lecture_header_from_text(cleaned)
            if header:
                title_de, location, date = header
                current_lecture = Lecture(
                    title_de=title_de,
                    location=location,
                    date=date,
                    order_index=lecture_order,
                )
                book.lectures.append(current_lecture)
                lecture_order += 1
            
            # Skip front matter (first ~5 pages)
            if i < 5:
                del text, cleaned
                gc.collect()
                continue
            
            # Ensure we have a lecture
            if current_lecture is None:
                current_lecture = Lecture(
                    title_de=book.title_de or book.ga_number or "Gesamtwerk",
                    order_index=0
                )
                book.lectures.append(current_lecture)
                lecture_order = 1
            
            # Split into paragraphs
            paragraphs = split_into_paragraphs(cleaned)
            
            for para_text in paragraphs:
                if PAGE_NUM_RE.match(para_text):
                    continue
                
                paragraph = Paragraph(order_index=len(current_lecture.paragraphs))
                
                sentences = split_into_sentences(para_text)
                
                for sent_text in sentences:
                    if len(sent_text) > 5:
                        paragraph.sentences.append(Sentence(
                            text_de=sent_text,
                            order_index=len(paragraph.sentences),
                        ))
                
                if paragraph.sentences:
                    current_lecture.paragraphs.append(paragraph)
            
            # Free memory after each page
            del text, cleaned, paragraphs
            if i % 10 == 0:
                gc.collect()
        
        if not book.title_de and book.ga_number:
            book.title_de = f"({book.ga_number})"
        
        if progress_callback:
            progress_callback(total_pages, total_pages)
    
    gc.collect()
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
