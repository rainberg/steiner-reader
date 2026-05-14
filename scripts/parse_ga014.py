#!/usr/bin/env python3
"""
解析 GA014（四部神秘戏剧）的PDF，提取四级结构：
1. 戏剧（四个）
2. 每个戏剧内的场景（Bild）
"""
import os
import re
import sys
import psycopg2
import fitz  # PyMuPDF

# 数据库配置
DB_CONFIG = {
    "host": "localhost",
    "database": "steiner_reader",
    "user": "steiner",
    "password": "St3in3r_2026!"
}

# PDF 路径（在生产服务器上）
PDF_PATH = "/opt/steiner-reader/uploads/GA014.pdf"
DOCX_PATH = "/opt/steiner-reader/books/docx/GA014.docx"

# 四个戏剧标题
DRAMA_TITLES = [
    "Die Pforte der Einweihung",
    "Die Prüfung der Seele",
    "Der Hüter der Schwelle",
    "Der Seelen Erwachen"
]

# 场景模式（Bild, Vorspiel, Zwischenspiel）
SCENE_PATTERNS = [
    re.compile(r'^(Vorspiel|Zwischenspiel):?\s*(.*)', re.IGNORECASE),
    re.compile(r'^(\d+)\.\s*(Bild|bild):?\s*(.*)', re.IGNORECASE),
    re.compile(r'^(Erstes|Zweites|Drittes|Viertes|Fünftes|Sechstes|Siebentes|Achtes|Neuntes|Zehntes|Elftes|Zwölftes)\s+(Bild|bild):?\s*(.*)', re.IGNORECASE),
]

def split_into_sentences(text):
    """简单的句子分割"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 2]

def find_title_pages(pdf_doc, titles):
    """查找每个标题的起始页面"""
    title_pages = {}
    for title in titles:
        found = False
        for page_num in range(len(pdf_doc)):
            page = pdf_doc.load_page(page_num)
            text = page.get_text()
            # 检查标题是否以显著形式出现（可能跨行）
            if title in text:
                # 进一步确认：标题应该单独一行或前后有空格
                lines = text.split('\n')
                for i, line in enumerate(lines):
                    if title in line and len(line.strip()) < 100:
                        title_pages[title] = page_num
                        found = True
                        print(f"  Found '{title}' on page {page_num+1}")
                        break
                if found:
                    break
        if not found:
            print(f"  Warning: Could not find '{title}' in PDF")
    return title_pages

def extract_scenes_from_drama(pdf_doc, start_page, end_page, drama_title):
    """从一个戏剧中提取场景"""
    scenes = []
    current_scene = None
    current_text = []
    
    for page_num in range(start_page, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                if current_scene and current_text:
                    # 保存当前场景
                    scenes.append({
                        "title": current_scene,
                        "text": "\n".join(current_text),
                        "start_page": page_num + 1
                    })
                    current_text = []
                continue
            
            # 检查是否是场景标题
            is_scene = False
            scene_title = None
            for pattern in SCENE_PATTERNS:
                match = pattern.match(line)
                if match:
                    is_scene = True
                    if pattern.groups() == 3:
                        scene_title = f"{match.group(1)} {match.group(2)}: {match.group(3)}"
                    elif pattern.groups() == 2:
                        scene_title = f"{match.group(1)}: {match.group(2)}"
                    else:
                        scene_title = line
                    break
            
            if is_scene:
                if current_scene and current_text:
                    scenes.append({
                        "title": current_scene,
                        "text": "\n".join(current_text),
                        "start_page": page_num + 1
                    })
                current_scene = scene_title
                current_text = []
            else:
                if current_scene:
                    current_text.append(line)
    
    # 添加最后一个场景
    if current_scene and current_text:
        scenes.append({
            "title": current_scene,
            "text": "\n".join(current_text),
            "start_page": end_page + 1  # 近似
        })
    
    return scenes

def import_to_database(book_id, dramas):
    """导入到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    try:
        # 删除现有数据
        cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s))", (book_id,))
        cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s)", (book_id,))
        cur.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        
        drama_order = 0
        for drama in dramas:
            drama_order += 1
            # 插入戏剧作为父章节 (level='part')
            cur.execute(
                "INSERT INTO lectures (book_id, title_de, order_index, level) VALUES (%s, %s, %s, 'part') RETURNING id",
                (book_id, drama['title'], drama_order)
            )
            drama_id = cur.fetchone()[0]
            
            scene_order = 0
            for scene in drama['scenes']:
                scene_order += 1
                # 插入场景作为子章节 (level='lecture', parent_id=drama_id)
                cur.execute(
                    "INSERT INTO lectures (book_id, title_de, order_index, level, parent_id) VALUES (%s, %s, %s, 'lecture', %s) RETURNING id",
                    (book_id, scene['title'], scene_order, drama_id)
                )
                scene_id = cur.fetchone()[0]
                
                # 分割段落（按空行）
                paragraphs = [p.strip() for p in scene['text'].split('\n\n') if p.strip()]
                para_order = 0
                for para_text in paragraphs:
                    para_order += 1
                    cur.execute(
                        "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s, %s) RETURNING id",
                        (scene_id, para_order)
                    )
                    para_id = cur.fetchone()[0]
                    
                    # 插入句子
                    sentences = split_into_sentences(para_text)
                    for sent_order, sent_text in enumerate(sentences):
                        cur.execute(
                            "INSERT INTO sentences (paragraph_id, order_index, text_de) VALUES (%s, %s, %s)",
                            (para_id, sent_order + 1, sent_text)
                        )
        
        conn.commit()
        print(f"✅ 导入成功: {len(dramas)} 个戏剧, 总计 {sum(len(d['scenes']) for d in dramas)} 个场景")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ 数据库错误: {e}")
        raise
    finally:
        conn.close()

def main():
    print("解析 GA014 (四部神秘戏剧)")
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
    total_pages = len(pdf_doc)
    print(f"PDF 总页数: {total_pages}")
    
    # 查找戏剧标题的页面
    print("查找戏剧标题...")
    title_pages = find_title_pages(pdf_doc, DRAMA_TITLES)
    
    if len(title_pages) < 4:
        print("⚠️  警告: 未找到所有四个戏剧标题")
    
    # 按页面排序标题
    sorted_titles = sorted(title_pages.items(), key=lambda x: x[1])
    
    dramas = []
    for i, (title, start_page) in enumerate(sorted_titles):
        # 确定结束页面（下一个戏剧的开始或PDF结尾）
        if i + 1 < len(sorted_titles):
            end_page = sorted_titles[i + 1][1]
        else:
            end_page = total_pages
        
        print(f"处理戏剧: {title} (页面 {start_page+1}-{end_page})")
        scenes = extract_scenes_from_drama(pdf_doc, start_page, end_page, title)
        print(f"  找到 {len(scenes)} 个场景")
        
        dramas.append({
            "title": title,
            "scenes": scenes,
            "start_page": start_page + 1,
            "end_page": end_page
        })
    
    pdf_doc.close()
    
    # 导入数据库
    print("\n导入数据库...")
    import_to_database(book_id, dramas)
    
    print("完成！")

if __name__ == "__main__":
    main()