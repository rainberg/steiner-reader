#!/usr/bin/env python3
"""
解析 GA014（四部神秘戏剧）的PDF，提取两级结构：
1. 戏剧（四个）作为顶级章节 (level='part')
2. 每个戏剧内的场景（Bild/Vorspiel）作为子章节 (level='lecture')
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

def parse_toc_page(pdf_doc, toc_page_num=5):
    """解析目录页（PDF页码6，索引5），返回场景列表"""
    page = pdf_doc.load_page(toc_page_num)  # 0-based
    text = page.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    scenes = []
    current_title = None
    collecting_dots = False
    
    for line in lines:
        # 检查是否是场景标题（包含Bild/Vorspiel/Zwischenspiel）
        if 'Bild' in line or 'Vorspiel' in line or 'Zwischenspiel' in line:
            # 如果之前有未完成的标题，保存它
            if current_title:
                scenes.append({"title": current_title, "toc_page": None})
            current_title = line
            collecting_dots = True
        elif collecting_dots and (line.isdigit() or (line.replace('.', '').isdigit() and '.' in line)):
            # 页码行（可能包含点）
            page_num = int(line.replace('.', ''))
            if current_title:
                scenes.append({"title": current_title, "toc_page": page_num})
                current_title = None
                collecting_dots = False
        elif collecting_dots and (line == '.' or all(c == '.' for c in line)):
            # 点行，忽略
            continue
        elif current_title and collecting_dots:
            # 可能是标题的续行
            current_title += " " + line
    
    # 处理最后一个场景
    if current_title:
        scenes.append({"title": current_title, "toc_page": None})
    
    return scenes

def calculate_page_offset(pdf_doc, scenes):
    """计算目录页码到PDF实际页码的偏移量"""
    # 查找第一个有页码的场景在PDF中的实际位置
    for scene in scenes:
        if scene['toc_page']:
            toc_page = scene['toc_page']
            scene_title_clean = re.split(r'[:.]', scene['title'])[0].strip()
            # 在PDF中搜索该场景
            for page_num in range(len(pdf_doc)):
                page = pdf_doc.load_page(page_num)
                text = page.get_text()
                if scene_title_clean in text:
                    pdf_page = page_num + 1  # 1-based
                    offset = pdf_page - toc_page
                    print(f"偏移量计算: 目录页码 {toc_page} -> PDF页码 {pdf_page}, 偏移量 {offset}")
                    return offset
    # 默认偏移量（基于观察）
    return 8

def find_scene_start_page(pdf_doc, scene_title, start_search, end_search):
    """在页面范围内查找场景标题的实际起始页"""
    scene_title_clean = re.split(r'[:.]', scene_title)[0].strip()
    for page_num in range(start_search - 1, min(end_search, len(pdf_doc))):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        if scene_title_clean in text:
            # 进一步确认：标题应单独一行或显著
            lines = text.split('\n')
            for line in lines:
                if scene_title_clean in line and len(line.strip()) < 100:
                    return page_num + 1  # 1-based
    return None

def extract_scene_text(pdf_doc, start_page, end_page):
    """提取页面范围内的文本"""
    text_parts = []
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        text_parts.append(text)
    return "\n".join(text_parts)

def import_with_scenes(book_id, pdf_doc):
    """导入戏剧和场景到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    try:
        # 删除现有数据
        cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s))", (book_id,))
        cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s)", (book_id,))
        cur.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        
        # 解析目录
        print("解析目录页...")
        scenes_toc = parse_toc_page(pdf_doc, 5)  # 第6页是目录
        print(f"从目录中找到 {len(scenes_toc)} 个场景条目")
        for i, scene in enumerate(scenes_toc[:10]):
            print(f"  {i+1}: {scene['title']} -> 目录页码 {scene['toc_page']}")
        
        # 计算偏移量
        offset = calculate_page_offset(pdf_doc, scenes_toc)
        print(f"使用偏移量: {offset}")
        
        # 按戏剧分组场景（前两个戏剧在目录中）
        drama1_scenes = []  # Die Pforte der Einweihung
        drama2_scenes = []  # Die Prüfung der Seele
        drama3_scenes = []  # Der Hüter der Schwelle（可能不在目录中）
        drama4_scenes = []  # Der Seelen Erwachen（可能不在目录中）
        
        current_drama = 1
        for scene in scenes_toc:
            title_lower = scene['title'].lower()
            if 'prüfung' in title_lower or 'seele' in title_lower:
                current_drama = 2
            elif 'hüter' in title_lower or 'schwelle' in title_lower:
                current_drama = 3
            elif 'erwachen' in title_lower:
                current_drama = 4
            
            if current_drama == 1:
                drama1_scenes.append(scene)
            elif current_drama == 2:
                drama2_scenes.append(scene)
            elif current_drama == 3:
                drama3_scenes.append(scene)
            elif current_drama == 4:
                drama4_scenes.append(scene)
        
        print(f"戏剧1场景数: {len(drama1_scenes)}")
        print(f"戏剧2场景数: {len(drama2_scenes)}")
        print(f"戏剧3场景数: {len(drama3_scenes)}")
        print(f"戏剧4场景数: {len(drama4_scenes)}")
        
        # 如果没有找到足够场景，使用默认场景标题
        if len(drama3_scenes) == 0:
            drama3_scenes = [{"title": "Szenen", "toc_page": None}]
        if len(drama4_scenes) == 0:
            drama4_scenes = [{"title": "Szenen", "toc_page": None}]
        
        dramas_with_scenes = [
            {"drama": DRAMAS[0], "scenes": drama1_scenes},
            {"drama": DRAMAS[1], "scenes": drama2_scenes},
            {"drama": DRAMAS[2], "scenes": drama3_scenes},
            {"drama": DRAMAS[3], "scenes": drama4_scenes},
        ]
        
        total_lectures = 0
        total_paragraphs = 0
        total_sentences = 0
        
        # 导入每个戏剧
        for drama_idx, drama_info in enumerate(dramas_with_scenes):
            drama = drama_info['drama']
            scenes = drama_info['scenes']
            
            print(f"\n处理戏剧 {drama_idx+1}: {drama['title']}")
            
            # 插入戏剧作为顶级章节
            cur.execute(
                "INSERT INTO lectures (book_id, title_de, order_index, level) VALUES (%s, %s, %s, 'part') RETURNING id",
                (book_id, drama['title'], drama_idx + 1)
            )
            drama_id = cur.fetchone()[0]
            total_lectures += 1
            
            # 确定场景的页面范围
            scene_start_pages = []
            for i, scene in enumerate(scenes):
                if scene['toc_page']:
                    pdf_page = scene['toc_page'] + offset
                else:
                    # 估计页面：均匀分布或搜索
                    pdf_page = None
                
                if pdf_page and pdf_page >= drama['start_page'] and pdf_page <= drama['end_page']:
                    scene_start_pages.append((scene['title'], pdf_page))
                else:
                    # 使用默认：按顺序分配页面
                    estimated_page = drama['start_page'] + (i * (drama['end_page'] - drama['start_page'])) // len(scenes)
                    scene_start_pages.append((scene['title'], estimated_page))
            
            # 添加结束边界
            scene_start_pages.append(("END", drama['end_page'] + 1))
            
            # 处理每个场景
            for scene_idx in range(len(scene_start_pages) - 1):
                scene_title, start_page = scene_start_pages[scene_idx]
                _, end_page = scene_start_pages[scene_idx + 1]
                
                # 插入场景作为子章节
                cur.execute(
                    "INSERT INTO lectures (book_id, title_de, order_index, level, parent_id) VALUES (%s, %s, %s, 'lecture', %s) RETURNING id",
                    (book_id, scene_title, scene_idx + 1, drama_id)
                )
                scene_id = cur.fetchone()[0]
                total_lectures += 1
                
                # 提取场景文本
                text = extract_scene_text(pdf_doc, start_page, end_page - 1)
                paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
                
                para_order = 0
                for para_text in paragraphs:
                    para_order += 1
                    cur.execute(
                        "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s, %s) RETURNING id",
                        (scene_id, para_order)
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
                print(f"  场景 {scene_idx+1}: {scene_title[:50]}... (页 {start_page}-{end_page-1}), 段落 {para_order}")
        
        conn.commit()
        print(f"\n✅ 导入完成: {total_lectures} 章节, {total_paragraphs} 段落, {total_sentences} 句子")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ 数据库错误: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        conn.close()

def main():
    print("解析 GA014 (四部神秘戏剧，带场景)")
    print("=" * 60)
    
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
    import_with_scenes(book_id, pdf_doc)
    
    pdf_doc.close()
    print("完成！")

if __name__ == "__main__":
    main()