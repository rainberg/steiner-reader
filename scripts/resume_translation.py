#!/usr/bin/env python3
"""
续传翻译lecture 15539的剩余句子。
"""
import time
import sys
import psycopg2
from deep_translator import GoogleTranslator

DB_CONFIG = {
    "host": "localhost",
    "database": "steiner_reader",
    "user": "steiner",
    "password": "St3in3r_2026!"
}

LECTURE_ID = 15539

def translate_sentence_safe(text_de: str, max_retries: int = 3) -> str:
    for attempt in range(max_retries):
        try:
            translator = GoogleTranslator(source='de', target='zh-CN')
            return translator.translate(text_de)
        except Exception as e:
            print(f"  尝试 {attempt+1}/{max_retries} 失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
            else:
                return f"[翻译失败: {e}]"
    return "[翻译失败]"

def fetch_untranslated_sentences(lecture_id):
    """获取未翻译的句子"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = """
    SELECT s.id, s.order_index, s.text_de, p.order_index AS para_order
    FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s AND s.text_zh IS NULL
    ORDER BY p.order_index, s.order_index
    """
    
    cur.execute(query, (lecture_id,))
    rows = cur.fetchall()
    
    # 获取总句子数
    cur.execute("""
    SELECT COUNT(s.id)
    FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s
    """, (lecture_id,))
    total = cur.fetchone()[0]
    
    conn.close()
    return rows, total

def update_sentence_translation(sentence_id, text_zh):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute(
        "UPDATE sentences SET text_zh = %s WHERE id = %s",
        (text_zh, sentence_id)
    )
    conn.commit()
    conn.close()

def main():
    print(f"续传翻译lecture {LECTURE_ID}")
    print("=" * 50)
    
    # 获取未翻译句子
    untranslated, total = fetch_untranslated_sentences(LECTURE_ID)
    translated_count = total - len(untranslated)
    
    print(f"总句子数: {total}")
    print(f"已翻译: {translated_count}")
    print(f"待翻译: {len(untranslated)}")
    
    if len(untranslated) == 0:
        print("✅ 所有句子已翻译完成!")
        return
    
    # 开始翻译
    print("\n开始翻译剩余句子...")
    completed = 0
    failed = 0
    
    for i, (sentence_id, order_idx, text_de, para_order) in enumerate(untranslated):
        progress = (translated_count + i + 1) / total * 100
        sys.stdout.write(f"\r进度: {translated_count + i + 1}/{total} ({progress:.1f}%) - 段落 {para_order}.{order_idx}")
        sys.stdout.flush()
        
        text_zh = translate_sentence_safe(text_de)
        
        if text_zh.startswith("[翻译失败"):
            print(f"\n  ❌ 翻译失败: {text_de[:50]}...")
            failed += 1
            text_zh = f"[翻译失败] {text_de[:100]}"
        else:
            completed += 1
        
        update_sentence_translation(sentence_id, text_zh)
        
        # 延迟
        if (i + 1) % 3 == 0 and i + 1 < len(untranslated):
            time.sleep(1.5)  # 稍微长一点的延迟
    
    print()  # 换行
    print(f"\n✅ 完成!")
    print(f"新增翻译: {completed}")
    print(f"新增失败: {failed}")
    
    # 最终验证
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("""
    SELECT COUNT(s.id) FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s AND s.text_zh IS NULL
    """, (LECTURE_ID,))
    remaining = cur.fetchone()[0]
    conn.close()
    
    if remaining == 0:
        print("✅ 所有句子翻译完成!")
    else:
        print(f"⚠️  仍有 {remaining} 个句子未翻译")
    
    print("\n请访问 https://steiner.3mudi.com/books/520/lectures/15539 检查翻译结果")

if __name__ == "__main__":
    main()