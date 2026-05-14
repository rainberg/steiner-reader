#!/usr/bin/env python3
"""
临时脚本：导入GA279 PDF到新数据库
"""
import asyncio
import asyncpg
import sys
import os
from pathlib import Path

# 添加后端目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / 'backend'))

from app.services.pdf_parser import parse_pdf

async def import_ga279():
    # 数据库连接配置
    DATABASE_URL = "postgresql://steiner:password@localhost:5433/steiner_reader"
    
    # PDF文件路径
    pdf_path = Path.home() / "steiner-reader" / "data" / "pdf" / "GA279.pdf"
    
    if not pdf_path.exists():
        print(f"PDF文件不存在: {pdf_path}")
        return
    
    print(f"解析PDF: {pdf_path}")
    
    # 解析PDF
    book = parse_pdf(str(pdf_path))
    
    print(f"解析完成: {book.ga_number} - {book.title_de}")
    print(f"包含 {len(book.lectures)} 个讲座")
    
    # 连接数据库
    conn = await asyncpg.connect(DATABASE_URL)
    
    try:
        # 开始事务
        async with conn.transaction():
            # 插入书籍
            book_id = await conn.fetchval("""
                INSERT INTO books (ga_number, title_de, pdf_filename, created_at)
                VALUES ($1, $2, $3, NOW())
                RETURNING id
            """, book.ga_number, book.title_de, pdf_path.name)
            
            print(f"插入书籍，ID: {book_id}")
            
            # 插入每个讲座
            for lecture_idx, lecture in enumerate(book.lectures):
                lecture_id = await conn.fetchval("""
                    INSERT INTO lectures (book_id, title_de, lecture_date, location, order_index, created_at)
                    VALUES ($1, $2, $3, $4, $5, NOW())
                    RETURNING id
                """, book_id, lecture.title_de, lecture.date if lecture.date else None, 
                     lecture.location if lecture.location else None, lecture.order_index)
                
                print(f"  讲座 {lecture_idx+1}: {lecture.title_de[:50]}... (ID: {lecture_id})")
                
                # 插入段落和句子
                for para_idx, paragraph in enumerate(lecture.paragraphs):
                    para_id = await conn.fetchval("""
                        INSERT INTO paragraphs (lecture_id, order_index, created_at)
                        VALUES ($1, $2, NOW())
                        RETURNING id
                    """, lecture_id, para_idx)
                    
                    for sent_idx, sentence in enumerate(paragraph.sentences):
                        await conn.execute("""
                            INSERT INTO sentences (paragraph_id, order_index, text_de, created_at)
                            VALUES ($1, $2, $3, NOW())
                        """, para_id, sent_idx, sentence.text_de)
                    
                    print(f"    段落 {para_idx+1}: {len(paragraph.sentences)} 个句子")
            
            print(f"导入完成！书籍ID: {book_id}")
            
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(import_ga279())