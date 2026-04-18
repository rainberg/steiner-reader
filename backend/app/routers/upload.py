"""PDF Upload and parsing router."""

import os
import uuid
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.db.database import get_db
from app.db.models import Book, Lecture, Paragraph, Sentence
from app.models.schemas import UploadResponse
from app.services.pdf_parser import parse_pdf, get_stats

router = APIRouter(prefix="/api", tags=["upload"])

ALLOWED_EXTENSIONS = {".pdf"}


@router.post("/books/upload", response_model=UploadResponse)
async def upload_pdf(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db),
):
    """Upload a PDF file, parse its structure, and save to database."""
    # Validate file extension
    filename = file.filename or ""
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Only PDF files are accepted")
    
    # Generate unique filename
    unique_name = f"{uuid.uuid4().hex[:12]}_{filename}"
    upload_dir = Path(settings.UPLOAD_DIR)
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / unique_name
    
    # Save uploaded file
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    # Parse PDF
    try:
        book_data = parse_pdf(str(file_path))
    except Exception as e:
        # Clean up file on parse failure
        os.unlink(file_path)
        raise HTTPException(
            status_code=422,
            detail=f"PDF parsing failed: {str(e)}"
        )
    
    # Save to database
    db_book = Book(
        ga_number=book_data.ga_number,
        title_de=book_data.title_de,
        pdf_filename=unique_name,
    )
    db.add(db_book)
    await db.flush()  # Get the book ID
    
    for lec_data in book_data.lectures:
        db_lecture = Lecture(
            book_id=db_book.id,
            title_de=lec_data.title_de,
            location=lec_data.location or None,
            order_index=lec_data.order_index,
        )
        # Parse date string to Date if present
        if lec_data.date:
            try:
                from datetime import datetime
                # Try common German date formats
                for fmt in ["%d. %B %Y", "%d.%m.%Y"]:
                    try:
                        db_lecture.lecture_date = datetime.strptime(lec_data.date, fmt).date()
                        break
                    except ValueError:
                        continue
            except Exception:
                pass
        
        db.add(db_lecture)
        await db.flush()
        
        for para_data in lec_data.paragraphs:
            db_paragraph = Paragraph(
                lecture_id=db_lecture.id,
                order_index=para_data.order_index,
            )
            db.add(db_paragraph)
            await db.flush()
            
            for sent_data in para_data.sentences:
                db_sentence = Sentence(
                    paragraph_id=db_paragraph.id,
                    order_index=sent_data.order_index,
                    text_de=sent_data.text_de,
                )
                db.add(db_sentence)
    
    await db.commit()
    
    stats = get_stats(book_data)
    
    return UploadResponse(
        book_id=db_book.id,
        message=f"PDF parsed successfully: {stats['lectures']} lectures, "
                f"{stats['paragraphs']} paragraphs, {stats['sentences']} sentences",
        ga_number=db_book.ga_number,
        stats=stats,
    )
