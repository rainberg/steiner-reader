"""检查P2剩余6个问题 - 验证内容是否完整"""
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


def find_position_progressive(sentence, haystack_norm, start_pos=0):
    norm = normalize(sentence)
    for length in [80, 60, 50, 40, 30, 25, 20]:
        if len(norm) >= length:
            pos = haystack_norm.find(norm[:length], start_pos)
            if pos >= 0:
                return pos
    if len(norm) >= 40:
        mid = len(norm) // 2
        pos = haystack_norm.find(norm[mid-20:mid+20], start_pos)
        if pos >= 0:
            return pos
    return -1


def main():
    with open("/tmp/p2_analysis.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open("/tmp/pdf_full_texts.json", "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    needs_review = data["needs_review"]
    print(f"待检查: {len(needs_review)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    for issue in needs_review:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]
        title = issue.get("lecture_title", "")
        db_sent_count = issue.get("sent_count", 0)
        db_total_chars = issue.get("total_chars", 0)

        print(f"\n{'='*60}")
        print(f"{ga} #{lecture_id} ({title[:50]})")
        print(f"DB内容: {db_sent_count}句, {db_total_chars}字符")

        # 获取讲座首末句
        cur.execute("""
            SELECT
                (SELECT s.text_de FROM paragraphs p
                 JOIN sentences s ON s.paragraph_id = p.id
                 WHERE p.lecture_id = l.id
                 ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_s,
                (SELECT s.text_de FROM paragraphs p
                 JOIN sentences s ON s.paragraph_id = p.id
                 WHERE p.lecture_id = l.id
                 ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_s
            FROM lectures l
            WHERE l.id = %s
        """, (lecture_id,))
        row = cur.fetchone()
        first_s, last_s = row

        pdf_data = pdf_texts.get(ga)
        if not pdf_data:
            print(f"  无PDF")
            continue
        pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
        pdf_norm = normalize(pdf_text)

        first_pos = find_position_progressive(first_s, pdf_norm) if first_s else -1
        last_pos = find_position_progressive(last_s, pdf_norm) if last_s else -1
        print(f"首句位置: {first_pos}, 末句位置: {last_pos}")

        if first_pos >= 0 and last_pos >= 0:
            pdf_length = last_pos - first_pos
            ratio = len(pdf_text) / len(pdf_norm)
            pdf_length_orig = int(pdf_length * ratio)
            print(f"PDF中间距: {pdf_length_orig}字符")

            if pdf_length_orig > db_total_chars * 2:
                print(f"  ⚠ PDF间距({pdf_length_orig})远大于DB内容({db_total_chars})")
                # 提取PDF内容
                approx_start = int(first_pos * ratio)
                approx_end = int(last_pos * ratio)
                pdf_content = pdf_text[approx_start:approx_end]
                pdf_sentences = re.split(r'(?<=[.!?])\s+', pdf_content)
                pdf_sent_count = len([s for s in pdf_sentences if len(s.strip()) > 20])
                print(f"  PDF内容句子数: {pdf_sent_count}")
                print(f"  PDF内容开头: {pdf_content[:200]}")
            else:
                print(f"  ✓ PDF间距({pdf_length_orig})与DB内容({db_total_chars})相当，内容完整")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
