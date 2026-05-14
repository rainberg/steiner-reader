#!/usr/bin/env python3
"""
修复 GA014 中lecture 15539的翻译错位问题。
清除现有翻译并逐句重新翻译，确保顺序正确。
"""
import asyncio
import time
import sys
import psycopg2
from deep_translator import GoogleTranslator

# 数据库配置
DB_CONFIG = {
    "host": "localhost",
    "database": "steiner_reader",
    "user": "steiner",
    "password": "St3in3r_2026!"
}

LECTURE_ID = 15539

def translate_sentence_safe(text_de: str, max_retries: int = 3) -> str:
    """安全地翻译单个句子，带重试机制"""
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source='de', target='zh-CN')
            translated = translator.translate(text_de)
            return translated
        except Exception as e:
            print(f"  尝试 {attempt+1}/{max_retries} 失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)  # 指数退避
            else:
                return f"[翻译失败: {e}]"
    return "[翻译失败]"

def fetch_sentences(lecture_id):
    """获取lecture的所有句子，按段落和句子顺序排序"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = """
    SELECT s.id, s.order_index, s.text_de, s.text_zh, p.order_index AS para_order
    FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s
    ORDER BY p.order_index, s.order_index
    """
    
    cur.execute(query, (lecture_id,))
    rows = cur.fetchall()
    conn.close()
    
    return rows

def update_sentence_translation(sentence_id, text_zh):
    """更新句子的中文翻译"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "UPDATE sentences SET text_zh = %s WHERE id = %s",
        (text_zh, sentence_id)
    )
    conn.commit()
    conn.close()

def clear_translations(lecture_id):
    """清除lecture的所有翻译"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # 统计要清除的句子数
    cur.execute("""
    SELECT COUNT(s.id)
    FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s AND s.text_zh IS NOT NULL
    """, (lecture_id,))
    count = cur.fetchone()[0]
    
    if count > 0:
        cur.execute("""
        UPDATE sentences s
        SET text_zh = NULL
        FROM paragraphs p
        WHERE s.paragraph_id = p.id AND p.lecture_id = %s
        """, (lecture_id,))
        conn.commit()
        print(f"已清除 {count} 个句子的翻译")
    else:
        print("没有需要清除的翻译")
    
    conn.close()

def main():
    print(f"修复lecture {LECTURE_ID}的翻译错位问题")
    print("=" * 60)
    
    # 1. 获取lecture信息
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
    SELECT l.title_de, b.ga_number, b.title_de AS book_title
    FROM lectures l
    JOIN books b ON l.book_id = b.id
    WHERE l.id = %s
    """, (LECTURE_ID,))
    lecture_info = cur.fetchone()
    conn.close()
    
    if not lecture_info:
        print(f"❌ 找不到lecture {LECTURE_ID}")
        sys.exit(1)
    
    title_de, ga_number, book_title = lecture_info
    print(f"书籍: {ga_number} - {book_title}")
    print(f"章节: {title_de}")
    
    # 2. 获取句子总数
    sentences = fetch_sentences(LECTURE_ID)
    print(f"句子总数: {len(sentences)}")
    
    if len(sentences) == 0:
        print("❌ 没有找到句子")
        sys.exit(1)
    
    # 3. 询问是否清除现有翻译
    response = input("是否清除现有翻译并重新翻译? (y/N): ").strip().lower()
    if response != 'y':
        print("操作取消")
        sys.exit(0)
    
    # 4. 清除翻译
    clear_translations(LECTURE_ID)
    
    # 5. 逐句翻译
    print("\n开始逐句翻译...")
    total = len(sentences)
    translated_count = 0
    failed_count = 0
    
    for i, (sentence_id, order_idx, text_de, old_text_zh, para_order) in enumerate(sentences):
        print(f"[段落 {para_order}.{order_idx}] {text_de[:80]}...")
        
        # 翻译
        text_zh = translate_sentence_safe(text_de)
        
        if text_zh.startswith("[翻译失败"):
            print(f"  ❌ 翻译失败: {text_zh}")
            failed_count += 1
        else:
            # 更新数据库
            update_sentence_translation(sentence_id, text_zh)
            print(f"  ✅ {text_zh[:80]}...")
            translated_count += 1
        
        # 进度显示
        progress = (i + 1) / total * 100
        print(f"进度: {i+1}/{total} ({progress:.1f}%)")
        
        # 延迟以避免速率限制（每5句后延迟1秒）
        if (i + 1) % 5 == 0 and i + 1 < total:
            time.sleep(1)
    
    # 6. 总结
    print(f"\n✅ 完成!")
    print(f"总句子数: {total}")
    print(f"成功翻译: {translated_count}")
    print(f"失败: {failed_count}")
    
    # 7. 验证
    if translated_count > 0:
        print("\n验证翻译结果...")
        # 随机抽取几个句子检查
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("""
        SELECT s.text_de, s.text_zh
        FROM sentences s
        JOIN paragraphs p ON s.paragraph_id = p.id
        WHERE p.lecture_id = %s AND s.text_zh IS NOT NULL
        ORDER BY RANDOM()
        LIMIT 3
        """, (LECTURE_ID,))
        samples = cur.fetchall()
        conn.close()
        
        print("随机样本检查:")
        for i, (text_de, text_zh) in enumerate(samples):
            print(f"样本 {i+1}:")
            print(f"  德文: {text_de[:100]}...")
            print(f"  中文: {text_zh[:100]}...")
            print()

if __name__ == "__main__":
    main()