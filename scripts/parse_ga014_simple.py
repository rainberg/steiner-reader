#!/usr/bin/env python3
"""
简单解析 GA014：将四部戏剧作为四个章节导入，不处理场景。
"""
import os
import re
import sys
import psycopg2
import fitz  # PyMuPDF

DB_CONFIG = {
    "host": "localhost",
    "database": "steiner_reader",
    "user": "steiner",
    "password": "St3in3r_2026!"
}

PDF_PATH = "/opt/steiner-reader/uploads/GA014.pdf"

# 戏剧标题和起始页面（基于PDF检查）
DRAMAS = [
    {"title": "Die Pforte der Einweihung", "start_page": 14, "end_page": 161},
    {"title": "Die Prüfung der Seele", "start_page": 162, "end_page": 283},
    {"title": "Der Hüter der Schwelle", "start_page": 284, "end_page": 407},
    {"title": "Der Seelen Erwachen", "start_page": 408, "end_page": 544}
]

def split_into_sentences(text):
    """简单的句子分割"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 2]

def extract_drama_text(pdf_doc, start_page, end_page):
    """提取页面范围内的文本，合并页面"""
    text_parts = []
    # 注意：页码是1-based，fitz是0-based
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        text_parts.append(text)
    return "\n".join(text_parts)

def import_dramas(book_id, pdf_doc):
    """导入戏剧到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    try:
        # 删除现有数据
        cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s))", (book_id,))
        cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s)", (book_id,))
        cur.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        
        order_idx = 0
        total_paragraphs = 0
        total_sentences = 0
        
        for drama in DRAMAS:
            order_idx += 1
            print(f"处理戏剧: {drama['title']} (页面 {drama['start_page']}-{drama['end_page']})")
            # 插入戏剧作为章节 (level='part')
            cur.execute(
                "INSERT INTO lectures (book_id, title_de, order_index, level) VALUES (%s, %s, %s, 'part') RETURNING id",
                (book_id, drama['title'], order_idx)
            )
            drama_id = cur.fetchone()[0]
            
            # 提取文本
            text = extract_drama_text(pdf_doc, drama['start_page'], drama['end_page'])
            # 按空行分割段落
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            
            para_order = 0
            for para_text in paragraphs:
                para_order += 1
                cur.execute(
                    "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s, %s) RETURNING id",
                    (drama_id, para_order)
                )
                para_id = cur.fetchone()[0]
                
                sentences = split_into_sentences(para_text)
                for sent_order, sent_text in enumerate(sentences):
                    cur.execute(
                        "INSERT INTO sentences (paragraph_id, order_index, text_de) VALUES (%s, %s, %s)",
                        (para_id, sent_order + 1, sent_text)
                    )
                    total_sentences += 1
            
            total_paragraphs += para_order
            print(f"  段落: {para_order}, 句子: {len(sentences)}")
        
        conn.commit()
        print(f"\n✅ 导入完成: {order_idx} 个戏剧, {total_paragraphs} 段落, {total_sentences} 句子")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ 数据库错误: {e}")
        raise
    finally:
        conn.close()

def main():
    print("简单解析 GA014 (四部神秘戏剧)")
    print("=" * 50)
    
    if not os.path.exists(PDF_PATH):
        print(f"❌ PDF 文件不存在: {PDF_PATH}")
        sys.exit(1)
    
    # 获取 book_id
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT id FROM books WHERE ga_number = 'GA014'")
    row = cur.fetchone()
    if not row:
        print("❌ 数据库中找不到 GA014")
        sys.exit(1)
    book_id = row[0]
    conn.close()
    
    # 打开 PDF
    pdf_doc = fitz.open(PDF_PATH)
    print(f"PDF 总页数: {len(pdf_doc)}")
    
    # 导入
    import_dramas(book_id, pdf_doc)
    
    pdf_doc.close()
    print("完成！")

if __name__ == "__main__":
    main()