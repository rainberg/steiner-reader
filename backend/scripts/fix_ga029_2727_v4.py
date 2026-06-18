"""修复GA029 #2727 v4 - 从正确位置289080重新提取"""
import json
import re
import psycopg2

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"


def split_into_paragraphs(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = re.split(r'\n\s*\n', text)
    result = []
    for p in paragraphs:
        p = re.sub(r'-\s*\n\s*', '', p)
        p = re.sub(r'\s*\n\s*', ' ', p)
        p = re.sub(r'\s+', ' ', p).strip()
        if p and len(p) > 10:
            result.append(p)
    return result


def split_into_sentences(paragraph):
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ«])', paragraph)
    return [s.strip() for s in sentences if s.strip()]


def main():
    with open("/tmp/pdf_full_texts.json", "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)
    pdf_data = pdf_texts["GA029"]
    pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data

    # 正确的起始位置
    first_pos = pdf_text.find("In der letzten Nummer dieser Zeitschrift")
    print(f"首句位置: {first_pos}")

    # 下一讲座位置 - 搜索"BEMERKUNGEN"（在首句之后）
    bemerkungen_pos = pdf_text.find("BEMERKUNGEN", first_pos + 100)
    print(f"下一讲座位置: {bemerkungen_pos}")

    # 提取讲座内容
    lecture_content = pdf_text[first_pos:bemerkungen_pos].strip()
    print(f"\n讲座内容长度: {len(lecture_content)}字符")
    print(f"开头: {lecture_content[:200]}")
    print(f"结尾: {lecture_content[-200:]}")

    # 分割段落和句子
    paragraphs = split_into_paragraphs(lecture_content)
    print(f"\n段落分割: {len(paragraphs)}个段落")

    all_sentences = []
    for para_idx, para in enumerate(paragraphs):
        sentences = split_into_sentences(para)
        print(f"  段落{para_idx+1}: {len(sentences)}句子, {len(para)}字符 - {para[:60]}...")
        for sent_idx, sent in enumerate(sentences):
            all_sentences.append((para_idx, sent_idx, sent))

    print(f"\n总句子数: {len(all_sentences)}")
    print(f"总字符数: {sum(len(s[2]) for s in all_sentences)}")

    # 更新数据库
    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    cur.execute("BEGIN")
    try:
        # 删除旧数据
        cur.execute("""
            DELETE FROM sentences
            WHERE paragraph_id IN (
                SELECT id FROM paragraphs WHERE lecture_id = 2727
            )
        """)
        print(f"\n删除句子: {cur.rowcount}")

        cur.execute("DELETE FROM paragraphs WHERE lecture_id = 2727")
        print(f"删除段落: {cur.rowcount}")

        # 插入新数据
        for para_idx, para in enumerate(paragraphs):
            cur.execute("""
                INSERT INTO paragraphs (lecture_id, order_index)
                VALUES (2727, %s)
                RETURNING id
            """, (para_idx + 1,))
            para_id = cur.fetchone()[0]

            sentences = split_into_sentences(para)
            for sent_idx, sent in enumerate(sentences):
                cur.execute("""
                    INSERT INTO sentences (paragraph_id, order_index, text_de)
                    VALUES (%s, %s, %s)
                """, (para_id, sent_idx + 1, sent))

        cur.execute("""
            SELECT COUNT(DISTINCT p.id), COUNT(s.id), SUM(LENGTH(s.text_de))
            FROM paragraphs p
            LEFT JOIN sentences s ON s.paragraph_id = p.id
            WHERE p.lecture_id = 2727
        """)
        row = cur.fetchone()
        print(f"\n更新后: {row[0]}段落, {row[1]}句子, {row[2]}字符")

        cur.execute("COMMIT")
        print("✓ 更新成功！")

    except Exception as e:
        cur.execute("ROLLBACK")
        print(f"✗ 更新失败: {e}")
        raise

    # 验证首句
    cur.execute("""
        SELECT s.text_de FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = 2727
        ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1
    """)
    first_sent = cur.fetchone()[0]
    print(f"\n首句: {first_sent[:100]}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
