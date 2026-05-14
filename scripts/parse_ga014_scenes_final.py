#!/usr/bin/env python3
"""
解析 GA014（四部神秘戏剧）的PDF，提取两级结构：
最终版本：手动修正页码错误。
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

def parse_toc_manual():
    """
    手动解析目录（基于目录页分析）
    返回两个列表：drama1_scenes, drama2_scenes
    """
    # 第一个戏剧：Die Pforte der Einweihung
    drama1_scenes = [
        {'title': 'Vorspiel: Ein Zimmer der Sophia', 'toc_page': 5},
        {'title': 'Erstes Bild: Ein Zimmer in rosenrotem Grundton', 'toc_page': 13},
        {'title': 'Zweites Bild: Gegend im Freien', 'toc_page': 50},
        {'title': 'Drittes Bild: Ein Meditationszimmer', 'toc_page': 57},
        {'title': 'Viertes Bild: Die Seelenwelt', 'toc_page': 69},
        {'title': 'Fünftes Bild: Ein unterirdischer Felsentempel', 'toc_page': 83},
        {'title': 'Sechstes Bild: Die Seelenwelt', 'toc_page': 93},
        {'title': 'Siebentes Bild: Das Gebiet des Geistes', 'toc_page': 100},
        {'title': 'Zwischenspiel: Ein Zimmer der Sophia', 'toc_page': 114},
        {'title': 'Achtes Bild: Ein Zimmer in rosenrotem Grundton', 'toc_page': 120},
        {'title': 'Neuntes Bild: Gegend im Freien', 'toc_page': 129},
        {'title': 'Zehntes Bild: Ein Meditationszimmer', 'toc_page': 133},
        {'title': 'Elftes Bild: Der Sonnentempel', 'toc_page': 140},
    ]
    
    # 第二个戏剧：Die Prüfung der Seele
    drama2_scenes = [
        {'title': 'Erstes Bild: Ein Studierzimmer des Capesius', 'toc_page': 153},
        {'title': 'Zweites Bild: Ein Meditationszimmer', 'toc_page': 165},
        {'title': 'Drittes Bild: Ein Zimmer in rosenrotem Grundton', 'toc_page': 176},
        {'title': 'Viertes Bild: Ein Studierzimmer des Capesius', 'toc_page': 183},
        {'title': 'Fünftes Bild: Eine Landschaft', 'toc_page': 191},
        {'title': 'Sechstes Bild: Eine Waldwiese', 'toc_page': 207},  # 修正：2,07 -> 207
    ]
    
    return drama1_scenes, drama2_scenes

def find_and_deduplicate_scenes(pdf_doc, start_page, end_page, drama_title):
    """
    在PDF中搜索场景标题，并去重（合并大写/小写版本）
    返回场景列表：[{'title': '...', 'pdf_page': 123}]
    """
    scenes = []
    # 更精确的场景标题模式
    scene_patterns = [
        re.compile(r'^(VORSPIEL|ZWISCHENSPIEL)\b', re.IGNORECASE),
        re.compile(r'^(\d+)\.\s*(BILD|bild)\b', re.IGNORECASE),
        re.compile(r'^(ERSTES|ZWEITES|DRITTES|VIERTES|FÜNFTES|SECHSTES|SIEBENTES|ACHTES|NEUNTES|ZEHNTES|ELFTES|ZWÖLFTES)\s+(BILD|bild)\b', re.IGNORECASE),
    ]
    
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line or len(line) > 200:
                continue
            
            # 检查是否是场景标题
            for pattern in scene_patterns:
                match = pattern.match(line)
                if match:
                    # 提取标题核心（去掉多余空格和标点）
                    title_clean = re.sub(r'\s+', ' ', line).strip()
                    scenes.append({
                        'title': title_clean,
                        'pdf_page': page_num + 1,
                        'line': line
                    })
                    break
    
    # 去重和合并：优先使用小写版本
    title_to_scene = {}
    for scene in scenes:
        title_lower = scene['title'].lower()
        # 提取数字部分（如果有）
        num_match = re.search(r'(\d+|erste|zweite|dritte|vierte|fünfte|sechste|siebente|achte|neunte|zehnte|elfte|zwölfte)', title_lower, re.IGNORECASE)
        if not num_match:
            continue
        
        # 标准化标题：使用小写德语序数词
        if title_lower not in title_to_scene:
            title_to_scene[title_lower] = scene
        else:
            # 如果已经存在，优先选择非全大写的版本
            existing = title_to_scene[title_lower]
            if existing['title'].isupper() and not scene['title'].isupper():
                title_to_scene[title_lower] = scene
    
    # 转换为列表并按页码排序
    unique_scenes = list(title_to_scene.values())
    unique_scenes.sort(key=lambda x: x['pdf_page'])
    
    # 如果没有找到场景，使用默认
    if len(unique_scenes) == 0:
        unique_scenes.append({'title': drama_title, 'pdf_page': start_page})
    
    return unique_scenes

def extract_text_between(pdf_doc, start_page, end_page):
    """提取页面范围内的文本"""
    if start_page >= end_page:
        return ""
    text_parts = []
    for page_num in range(start_page - 1, end_page):
        page = pdf_doc.load_page(page_num)
        text = page.get_text()
        text_parts.append(text)
    return "\n".join(text_parts)

def import_all_scenes_final(book_id, pdf_doc):
    """导入所有戏剧和场景到数据库"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    try:
        # 删除现有数据
        cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s))", (book_id,))
        cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id = %s)", (book_id,))
        cur.execute("DELETE FROM lectures WHERE book_id = %s", (book_id,))
        
        print("使用手动解析的目录...")
        drama1_scenes, drama2_scenes = parse_toc_manual()
        print(f"第一个戏剧场景数: {len(drama1_scenes)}")
        for i, scene in enumerate(drama1_scenes):
            pdf_page = scene['toc_page'] + TOC_OFFSET
            print(f"  {i+1}: {scene['title'][:50]}... -> 目录页码 {scene['toc_page']} -> PDF页码 {pdf_page}")
        print(f"第二个戏剧场景数: {len(drama2_scenes)}")
        for i, scene in enumerate(drama2_scenes):
            pdf_page = scene['toc_page'] + TOC_OFFSET
            print(f"  {i+1}: {scene['title'][:50]}... -> 目录页码 {scene['toc_page']} -> PDF页码 {pdf_page}")
        
        # 为后两个戏剧搜索场景
        print("\n搜索后两个戏剧的场景...")
        drama3_scenes = find_and_deduplicate_scenes(pdf_doc, DRAMAS[2]['start_page'], DRAMAS[2]['end_page'], DRAMAS[2]['title'])
        drama4_scenes = find_and_deduplicate_scenes(pdf_doc, DRAMAS[3]['start_page'], DRAMAS[3]['end_page'], DRAMAS[3]['title'])
        
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
                if has_toc and scene.get('toc_page'):
                    pdf_page = scene['toc_page'] + TOC_OFFSET
                elif 'pdf_page' in scene:
                    pdf_page = scene['pdf_page']
                else:
                    # 估计页面
                    pdf_page = drama['start_page'] + (i * (drama['end_page'] - drama['start_page'])) // max(1, len(scenes))
                
                # 确保页码在合理范围内
                pdf_page = max(drama['start_page'], min(pdf_page, drama['end_page']))
                
                scene_ranges.append({
                    'title': scene['title'],
                    'start_page': pdf_page
                })
            
            # 为每个场景设置结束页面
            for i in range(len(scene_ranges)):
                if i + 1 < len(scene_ranges):
                    end_page = scene_ranges[i + 1]['start_page']
                else:
                    end_page = drama['end_page'] + 1
                
                # 确保开始页 < 结束页，且至少包含一页
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
    print("解析 GA014 (四部神秘戏剧，带场景) - 最终版本")
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
    import_all_scenes_final(book_id, pdf_doc)
    
    pdf_doc.close()
    print("完成！")

if __name__ == "__main__":
    main()