#!/usr/bin/env python3
"""
解析 GA014（四部神秘戏剧）的PDF，提取两级结构：
1. 戏剧（四个）作为顶级章节 (level='part')
2. 每个戏剧内的场景（Bild/Vorspiel）作为子章节 (level='lecture')
改进版本：正确解析目录，处理偏移量，搜索后两个戏剧的场景。
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

# 偏移量：目录页码 -> PDF实际页码
TOC_OFFSET = 8  # 目录页码5对应PDF页码13

def split_into_sentences(text):
    """简单的句子分割"""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 2]

def parse_toc(pdf_doc, toc_page_num=5):
    """
    解析目录页，返回两个列表：
    - drama1_scenes: 第一个戏剧的场景列表
    - drama2_scenes: 第二个戏剧的场景列表
    每个场景是字典：{'title': '...', 'toc_page': 123}
    """
    page = pdf_doc.load_page(toc_page_num)
    text = page.get_text()
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    drama1_scenes = []
    drama2_scenes = []
    current_drama = 1  # 1 = Die Pforte der Einweihung, 2 = Die Prüfung der Seele
    current_title = None
    collecting = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # 检查是否切换到第二个戏剧
        if "DIE PRÜFUNG DER SEELE" in line or "PRÜFUNG DER SEELE" in line:
            current_drama = 2
            i += 1
            continue
        
        # 检查是否是场景标题
        if ('Bild' in line or 'Vorspiel' in line or 'Zwischenspiel' in line) and not line.isdigit():
            # 保存前一个场景（如果有）
            if current_title and collecting:
                # 尝试从后续行获取页码
                page_num = None
                # 检查当前行是否包含页码（如 ". . . 153"）
                if re.search(r'\d+', line):
                    match = re.search(r'(\d+)', line)
                    if match:
                        page_num = int(match.group(1))
                # 如果当前行没有，检查下一行
                elif i + 1 < len(lines) and re.search(r'\d+', lines[i + 1]):
                    match = re.search(r'(\d+)', lines[i + 1])
                    if match:
                        page_num = int(match.group(1))
                        i += 1
                
                if current_drama == 1:
                    drama1_scenes.append({'title': current_title, 'toc_page': page_num})
                else:
                    drama2_scenes.append({'title': current_title, 'toc_page': page_num})
            
            # 开始收集新标题
            current_title = line
            collecting = True
            i += 1
            continue
        
        # 如果正在收集标题，且当前行是页码
        if collecting and re.search(r'^\d+$', line):
            page_num = int(line)
            if current_drama == 1:
                drama1_scenes.append({'title': current_title, 'toc_page': page_num})
            else:
                drama2_scenes.append({'title': current_title, 'toc_page': page_num})
            current_title = None
            collecting = False
            i += 1
            continue
        
        # 如果正在收集标题，且当前行包含页码（如 ". . . 153"）
        if collecting and re.search(r'\d+', line):
            match = re.search(r'(\d+)', line)
            if match:
                page_num = int(match.group(1))
                if current_drama == 1:
                    drama1_scenes.append({'title': current_title, 'toc_page': page_num})
                else:
                    drama2_scenes.append({'title': current_title, 'toc_page': page_num})
                current_title = None
                collecting = False
            i += 1
            continue
        
        # 其他情况：点号行或无关文本，跳过
        i += 1
    
    # 处理最后一个场景
    if current_title and collecting:
        if current_drama == 1:
            drama1_scenes.append({'title': current_title, 'toc_page': None})
        else:
            drama2_scenes.append({'title': current_title, 'toc_page': None})
    
    return drama1_scenes, drama2_scenes

def find_scenes_in_pdf(pdf_doc, start_page, end_page, drama_title):
    """
    在PDF中搜索场景标题（后两个戏剧没有目录）
    返回场景列表：[{'title': '...', 'pdf_page': 123}]
    """
    scenes = []
    scene_patterns = [
        re.compile(r'^(Vorspiel|Zwischenspiel)\b', re.IGNORECASE),
        re.compile(r'^(\d+)\.\s*(Bild|bild)\b', re.IGNORECASE),
        re.compile(r'^(Erstes|Zweites|Drittes|Viertes|Fünftes|Sechstes|Siebentes|Achtes|Neuntes|Zehntes|Elftes|Zwölftes)\s+(Bild|bild)\b', re.IGNORECASE),
    ]
    
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # 检查是否是场景标题
            for pattern in scene_patterns:
                match = pattern.match(line)
                if match:
                    scenes.append({
                        'title': line,
                        'pdf_page': page_num + 1  # 1-based
                    })
                    break
    
    # 去重（同一场景可能出现在多页）
    unique_scenes = []
    seen_titles = set()
    for scene in scenes:
        # 提取标题核心部分（去掉页码等）
        title_simple = re.split(r'[:.]', scene['title'])[0].strip()
        if title_simple not in seen_titles:
            seen_titles.add(title_simple)
            unique_scenes.append(scene)
    
    # 按页码排序
    unique_scenes.sort(key=lambda x: x['pdf_page'])
    
    # 如果没有找到场景，使用默认
    if len(unique_scenes) == 0:
        unique_scenes.append({'title': drama_title, 'pdf_page': start_page})
    
    return unique_scenes

def extract_text_between(pdf_doc, start_page, end_page):
    """提取页面范围内的文本"""
    text_parts = []
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        text_parts.append(text)
    return "\n".join(text_parts)

def import_all_scenes(book_id, pdf_doc):
    """导入所有戏剧和场景到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    try:
        # 删除现有数据
        cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s))", (book_id,))
        cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s)", (book_id,))
        cur.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        
        print("解析目录...")
        drama1_scenes, drama2_scenes = parse_toc(pdf_doc, 5)
        print(f"第一个戏剧场景数: {len(drama1_scenes)}")
        for i, scene in enumerate(drama1_scenes):
            print(f"  {i+1}: {scene['title']} -> 目录页码 {scene['toc_page']}")
        print(f"第二个戏剧场景数: {len(drama2_scenes)}")
        for i, scene in enumerate(drama2_scenes):
            print(f"  {i+1}: {scene['title']} -> 目录页码 {scene['toc_page']}")
        
        # 为后两个戏剧搜索场景
        print("\n搜索后两个戏剧的场景...")
        drama3_scenes = find_scenes_in_pdf(pdf_doc, DRAMAS[2]['start_page'], DRAMAS[2]['end_page'], DRAMAS[2]['title'])
        drama4_scenes = find_scenes_in_pdf(pdf_doc, DRAMAS[3]['start_page'], DRAMAS[3]['end_page'], DRAMAS[3]['title'])
        
        print(f"第三个戏剧场景数: {len(drama3_scenes)}")
        for i, scene in enumerate(drama3_scenes):
            print(f"  {i+1}: {scene['title']} -> PDF页码 {scene['pdf_page']}")
        print(f"第四个戏剧场景数: {len(drama4_scenes)}")
        for i, scene in enumerate(drama4_scenes):
            print(f"  {i+1}: {scene['title']} -> PDF页码 {scene['pdf_page']}")
        
        # 准备场景数据
        dramas_with_scenes = [
            {"drama": DRAMAS[0], "scenes": drama1_scenes, "has_toc": True},
            {"drama": DRAMAS[1], "scenes": drama2_scenes, "has_toc": True},
            {"drama": DRAMAS[2], "scenes": drama3_scenes, "has_toc": False},
            {"drama": DRAMAS[3], "scenes": drama4_scenes, "has_toc": False},
        ]
        
        total_lectures = 0
        total_paragraphs = 0
        total_sentences = 0
        
        # 导入每个戏剧
        for drama_idx, drama_info in enumerate(dramas_with_scenes):
            drama = drama_info['drama']
            scenes = drama_info['scenes']
            has_toc = drama_info['has_toc']
            
            print(f"\n处理戏剧 {drama_idx+1}: {drama['title']}")
            
            # 插入戏剧作为顶级章节
            cur.execute(
                "INSERT INTO lectures (book_id, title_de, order_index, level) VALUES (%s, %s, %s, 'part') RETURNING id",
                (book_id, drama['title'], drama_idx + 1)
            )
            drama_id = cur.fetchone()[0]
            total_lectures += 1
            
            # 确定场景的页面范围
            scene_ranges = []
            for i, scene in enumerate(scenes):
                if has_toc and scene['toc_page']:
                    pdf_page = scene['toc_page'] + TOC_OFFSET
                elif 'pdf_page' in scene:
                    pdf_page = scene['pdf_page']
                else:
                    # 估计页面
                    pdf_page = drama['start_page'] + (i * (drama['end_page'] - drama['start_page'])) // max(1, len(scenes))
                
                scene_ranges.append({
                    'title': scene['title'],
                    'start_page': pdf_page
                })
            
            # 为每个场景设置结束页面（下一个场景的开始或戏剧结束）
            for i in range(len(scene_ranges)):
                if i + 1 < len(scene_ranges):
                    end_page = scene_ranges[i + 1]['start_page']
                else:
                    end_page = drama['end_page'] + 1  # 包含最后一页
                
                # 确保开始页 < 结束页
                if scene_ranges[i]['start_page'] >= end_page:
                    end_page = scene_ranges[i]['start_page'] + 1
                
                scene_ranges[i]['end_page'] = end_page
            
            # 处理每个场景
            for scene_idx, scene_range in enumerate(scene_ranges):
                start_page = scene_range['start_page']
                end_page = scene_range['end_page']
                scene_title = scene_range['title']
                
                # 确保页面范围有效
                if start_page >= end_page:
                    print(f"  警告: 场景 {scene_title} 页面范围无效 {start_page}-{end_page}，跳过")
                    continue
                
                # 插入场景作为子章节
                cur.execute(
                    "INSERT INTO lectures (book_id, title_de, order_index, level, parent_id) VALUES (%s, %s, %s, 'lecture', %s) RETURNING id",
                    (book_id, scene_title, scene_idx + 1, drama_id)
                )
                scene_id = cur.fetchone()[0]
                total_lectures += 1
                
                # 提取场景文本
                text = extract_text_between(pdf_doc, start_page, end_page - 1)
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
                print(f"  场景 {scene_idx+1}: {scene_title[:40]}... (页 {start_page}-{end_page-1}), 段落 {para_order}")
        
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
    print("解析 GA014 (四部神秘戏剧，带场景) - 版本2")
    print("=" * 70)
    
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
    print(f"使用偏移量: {TOC_OFFSET} (目录页码 + {TOC_OFFSET} = PDF页码)")
    
    # 导入
    import_all_scenes(book_id, pdf_doc)
    
    pdf_doc.close()
    print("完成！")

if __name__ == "__main__":
    main()