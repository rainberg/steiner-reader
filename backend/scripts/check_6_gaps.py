"""逐一检查6个可能缺失的gap问题 - 对比DB内容量和PDF中间隙内容量"""
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
    with open("/tmp/p1_gap_verified.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open("/tmp/pdf_full_texts.json", "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    actual_missing = data["actual_missing"]
    print(f"待检查: {len(actual_missing)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    results = []

    for issue in actual_missing:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]
        title = issue.get("lecture_title", "")
        db_sent_count = issue["sent_count"]
        db_total_chars = issue["total_chars"]

        print(f"\n{'='*60}")
        print(f"{ga} #{lecture_id} ({title[:50]})")
        print(f"DB内容: {db_sent_count}句, {db_total_chars}字符")

        # 获取PDF
        pdf_data = pdf_texts.get(ga)
        if not pdf_data:
            print(f"  无PDF")
            results.append({**issue, "verdict": "no_pdf"})
            continue
        pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
        pdf_norm = normalize(pdf_text)

        # 获取前一讲座末句和当前讲座首句
        cur.execute("""
            SELECT l.id, l.order_index, l.title_de,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_s,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_s
            FROM lectures l
            JOIN books b ON l.book_id = b.id
            WHERE b.ga_number = %s AND l.level = 'lecture'
            ORDER BY l.order_index ASC, l.id ASC
        """, (ga,))

        lectures = cur.fetchall()
        current_idx = None
        prev_lecture = None
        current_lecture = None

        for idx, row in enumerate(lectures):
            if row[0] == lecture_id:
                current_idx = idx
                current_lecture = row
                if idx > 0:
                    prev_lecture = lectures[idx - 1]
                break

        if not current_lecture or not prev_lecture:
            print(f"  无法找到讲座")
            results.append({**issue, "verdict": "not_found"})
            continue

        # 定位 (row: id, order_index, title_de, first_s, last_s)
        prev_last_pos = -1
        curr_first_pos = -1

        if prev_lecture[4]:  # last_s of prev (index 4)
            prev_last_pos = find_position_progressive(prev_lecture[4], pdf_norm)

        if current_lecture[3]:  # first_s of current (index 3)
            search_start = prev_last_pos + 1 if prev_last_pos >= 0 else 0
            curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, search_start)
            if curr_first_pos < 0:
                curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, 0)

        print(f"  前一讲座#{prev_lecture[0]}末句位置: {prev_last_pos}")
        print(f"  当前讲座首句位置: {curr_first_pos}")

        if prev_last_pos < 0 or curr_first_pos < 0 or curr_first_pos <= prev_last_pos:
            print(f"  定位失败，可能是导入元数据首句")
            results.append({**issue, "verdict": "locate_failed", "prev_last_pos": prev_last_pos, "curr_first_pos": curr_first_pos})
            continue

        # 计算间隙大小
        gap_size_norm = curr_first_pos - prev_last_pos
        ratio = len(pdf_text) / len(pdf_norm)
        gap_size_orig = int(gap_size_norm * ratio)
        print(f"  间隙大小: {gap_size_orig}字符 (归一化: {gap_size_norm})")

        # 提取间隙文本
        approx_start = int(prev_last_pos * ratio)
        approx_end = int(curr_first_pos * ratio)
        gap_text = pdf_text[approx_start:approx_end]

        # 统计间隙中的句子数
        gap_sentences = re.split(r'(?<=[.!?])\s+', gap_text)
        gap_sent_count = len([s for s in gap_sentences if len(s.strip()) > 20])
        print(f"  间隙句子数: {gap_sent_count}")
        print(f"  间隙开头: {gap_text[:200]}")
        print(f"  间隙结尾: {gap_text[-200:]}")

        # 判断
        # 如果间隙内容量是DB内容量的2倍以上，可能缺失内容
        if gap_sent_count > db_sent_count * 2 and gap_size_orig > db_total_chars * 2:
            verdict = "likely_missing_content"
            reason = f"间隙内容({gap_sent_count}句,{gap_size_orig}字符)远大于DB内容({db_sent_count}句,{db_total_chars}字符)"
        elif gap_sent_count > db_sent_count * 1.5:
            verdict = "possibly_missing_content"
            reason = f"间隙内容({gap_sent_count}句)略多于DB内容({db_sent_count}句)"
        else:
            verdict = "probably_complete"
            reason = f"间隙内容({gap_sent_count}句)与DB内容({db_sent_count}句)相当"

        print(f"  判定: {verdict}")
        print(f"  原因: {reason}")

        results.append({
            **issue,
            "verdict": verdict,
            "reason": reason,
            "gap_sent_count": gap_sent_count,
            "gap_size_orig": gap_size_orig,
            "gap_text_preview": gap_text[:500]
        })

    # 汇总
    print(f"\n{'='*60}")
    print(f"=== 最终汇总 ===")
    from collections import Counter
    verdicts = Counter(r["verdict"] for r in results)
    for v, c in verdicts.most_common():
        print(f"  {v}: {c}")

    print(f"\n可能缺失内容的:")
    for r in results:
        if r["verdict"] in ("likely_missing_content", "possibly_missing_content"):
            print(f"  {r['ga']} #{r['lecture_id']} ({r.get('lecture_title', '')[:40]})")
            print(f"    {r['reason']}")

    # 保存
    with open("/tmp/p1_gap_final_verified.json", "w", encoding="utf-8") as f:
        json.dump({
            "results": results,
            "verdicts": dict(verdicts)
        }, f, ensure_ascii=False, indent=2)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
