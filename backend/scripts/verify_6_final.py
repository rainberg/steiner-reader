"""验证6个可能缺失内容的讲座 - 检查是否是前一讲座末句定位错误

关键判断：
- 如果多个讲座的"当前首句位置"相同，说明是首句定位错误（导入元数据）
- 如果前一讲座末句定位错误，间隙会包含多个讲座的内容
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
    with open("/tmp/pdf_full_texts.json", "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 检查每个GA的所有讲座首句位置
    gas_to_check = ["GA110", "GA227", "GA271", "GA286"]

    for ga in gas_to_check:
        print(f"\n{'='*60}")
        print(f"检查 {ga}")

        pdf_data = pdf_texts.get(ga)
        if not pdf_data:
            print(f"  无PDF")
            continue
        pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
        pdf_norm = normalize(pdf_text)

        cur.execute("""
            SELECT l.id, l.title_de, l.order_index,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_s,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_s,
                   (SELECT COUNT(s.id) FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id) as sent_count
            FROM lectures l
            JOIN books b ON l.book_id = b.id
            WHERE b.ga_number = %s AND l.level = 'lecture'
            ORDER BY l.order_index ASC, l.id ASC
        """, (ga,))

        lectures = cur.fetchall()
        print(f"  讲座数: {len(lectures)}")

        # 显示每个讲座的首末句位置
        print(f"  {'ID':>6} {'Order':>5} {'Sents':>6} {'FirstPos':>9} {'LastPos':>9} {'FirstSent':40}")
        positions = []
        for row in lectures:
            lid, title, order, first_s, last_s, sent_count = row
            first_pos = find_position_progressive(first_s, pdf_norm) if first_s else -1
            last_pos = find_position_progressive(last_s, pdf_norm) if last_s else -1
            positions.append(first_pos)
            print(f"  {lid:>4} {order:>5} {sent_count:>6} {first_pos:>9} {last_pos:>9} {(first_s or '')[:40]}")

        # 检查首句位置是否都相同（导入元数据模式）
        unique_positions = set(positions)
        if len(unique_positions) <= 3:
            print(f"  ⚠ 首句位置只有{len(unique_positions)}种，可能是导入元数据模式")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
