#!/usr/bin/env python3
"""
快速翻译lecture 15539的最后17个句子。
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

def translate_sentence(text_de):
    try:
        translator = GoogleTranslator(source='de', target='zh-CN')
        return translator.translate(text_de)
    except Exception as e:
        return f"[翻译失败: {e}]"

def main():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    # 获取未翻译句子
    cur.execute("""
    SELECT s.id, s.text_de, p.order_index, s.order_index
    FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s AND s.text_zh IS NULL
    ORDER BY p.order_index, s.order_index
    """, (LECTURE_ID,))
    
    rows = cur.fetchall()
    print(f"需要翻译 {len(rows)} 个句子")
    
    for i, (sentence_id, text_de, para_order, sent_order) in enumerate(rows):
        print(f"翻译 [{i+1}/{len(rows)}] 段落 {para_order}.{sent_order}: {text_de[:60]}...")
        
        text_zh = translate_sentence(text_de)
        print(f"  结果: {text_zh[:60]}...")
        
        cur.execute(
            "UPDATE sentences SET text_zh = %s WHERE id = %s",
            (text_zh, sentence_id)
        )
        
        # 短延迟
        if i < len(rows) - 1:
            time.sleep(0.8)
    
    conn.commit()
    
    # 验证
    cur.execute("""
    SELECT COUNT(*) FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s AND s.text_zh IS NULL
    """, (LECTURE_ID,))
    remaining = cur.fetchone()[0]
    
    cur.execute("""
    SELECT COUNT(*) FROM sentences s
    JOIN paragraphs p ON s.paragraph_id = p.id
    WHERE p.lecture_id = %s
    """, (LECTURE_ID,))
    total = cur.fetchone()[0]
    
    conn.close()
    
    print(f"\n✅ 完成! 总句子: {total}, 未翻译: {remaining}")
    
    if remaining == 0:
        print("✅ 所有句子翻译完成!")
    else:
        print(f"⚠️  仍有 {remaining} 个句子未翻译")

if __name__ == "__main__":
    main()