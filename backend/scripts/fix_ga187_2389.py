"""修复GA187 #2389 (HINWEISE) - 从PDF提取完整内容

DB现状: 51句, 4189字符
PDF实际: 121句, 9736字符
"""
import json
import re
import unicodedata
import psycopg2

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"


def normalize(s):
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.replace("ß", "ss")
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


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
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ«0-9])', paragraph)
    return [s.strip() for s in sentences if s.strip()]


def main():
    with open("/tmp/pdf_full_texts.json", "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)
    pdf_data = pdf_texts["GA187"]
    pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
    pdf_norm = normalize(pdf_text)

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 获取DB首末句
    cur.execute("""
        SELECT
            (SELECT s.text_de FROM paragraphs p
             JOIN sentences s ON s.paragraph_id = p.id
             WHERE p.lecture_id = 2389
             ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_s,
            (SELECT s.text_de FROM paragraphs p
             JOIN sentences s ON s.paragraph_id = p.id
             WHERE p.lecture_id = 2389
             ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_s
    """)
    row = cur.fetchone()
    first_s, last_s = row
    print(f"DB首句: {first_s[:80]}")
    print(f"DB末句: {last_s[:80]}")

    # 在PDF中定位首末句
    first_pos = pdf_norm.find(normalize(first_s)[:30])
    last_pos = pdf_norm.find(normalize(last_s)[:30])
    print(f"首句位置: {first_pos}")
    print(f"末句位置: {last_pos}")

    # 提取PDF中首末句之间的内容
    if first_pos >= 0 and last_pos >= 0:
        ratio = len(pdf_text) / len(pdf_norm)
        approx_start = int(first_pos * ratio)
        approx_end = int(last_pos * ratio) + 200  # 多取一些确保包含末句
        lecture_content = pdf_text[approx_start:approx_end]

        # 找到末句的结尾位置
        last_s_end = lecture_content.find(last_s[:30])
        if last_s_end >= 0:
            # 找到末句后的句号
            end_pos = lecture_content.find(".", last_s_end + len(last_s))
            if end_pos >= 0:
                lecture_content = lecture_content[:end_pos + 1]

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

        # 备份
        cur.execute("""
            SELECT p.id, p.order_index, s.id, s.order_index, s.text_de
            FROM paragraphs p
            JOIN sentences s ON s.paragraph_id = p.id
            WHERE p.lecture_id = 2389
            ORDER BY p.order_index, s.order_index
        """)
        backup = cur.fetchall()
        with open("/tmp/ga187_2389_backup.json", "w", encoding="utf-8") as f:
            json.dump([{"para_id": r[0], "para_order": r[1], "sent_id": r[2],
                        "sent_order": r[3], "text": r[4]} for r in backup], f,
                      ensure_ascii=False, indent=2)

        # 更新
        cur.execute("BEGIN")
        try:
            cur.execute("""
                DELETE FROM sentences
                WHERE paragraph_id IN (
                    SELECT id FROM paragraphs WHERE lecture_id = 2389
                )
            """)
            print(f"\n删除句子: {cur.rowcount}")

            cur.execute("DELETE FROM paragraphs WHERE lecture_id = 2389")
            print(f"删除段落: {cur.rowcount}")

            for para_idx, para in enumerate(paragraphs):
                cur.execute("""
                    INSERT INTO paragraphs (lecture_id, order_index)
                    VALUES (2389, %s)
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
                WHERE p.lecture_id = 2389
            """)
            row = cur.fetchone()
            print(f"\n更新后: {row[0]}段落, {row[1]}句子, {row[2]}字符")

            cur.execute("COMMIT")
            print("✓ 更新成功！")

        except Exception as e:
            cur.execute("ROLLBACK")
            print(f"✗ 更新失败: {e}")
            raise

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
