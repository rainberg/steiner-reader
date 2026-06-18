"""深入检查gap的likely_missing_lectures - 判断是否是假阳性

关键判断：间隙中包含"ZWEITER VORTRAG"等标题，是因为：
1. 真实缺失讲座（间隙中有未被DB收录的讲座）
2. 假阳性：间隙末尾就是下一讲座的标题（正常情况）

检查方法：
- 如果"VORTRAG"标题出现在间隙末尾附近，说明是下一讲座标题，假阳性
- 如果"VORTRAG"标题出现在间隙中间，说明可能缺失讲座
"""
import json
import re
import unicodedata
import psycopg2
from collections import Counter

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"


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
    with open("/tmp/p1_gap_analysis.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    # 获取likely_missing_lectures的间隙
    likely_missing = [r for r in data["real_gap_results"]
                      if r["status"] == "likely_missing_lectures"]
    print(f"likely_missing_lectures: {len(likely_missing)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 分类
    false_positive_title_at_end = []  # 标题在间隙末尾（下一讲座标题）
    real_missing = []  # 真实缺失
    needs_review = []  # 需要进一步检查

    pdf_cache = {}

    for issue in likely_missing:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]

        if ga not in pdf_cache:
            pdf_data = pdf_texts.get(ga)
            if pdf_data:
                pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
                pdf_cache[ga] = (pdf_text, normalize(pdf_text))
            else:
                pdf_cache[ga] = (None, None)

        pdf_text, pdf_norm = pdf_cache[ga]
        if not pdf_norm:
            needs_review.append({**issue, "reason": "no_pdf"})
            continue

        # 获取当前讲座和前一讲座
        cur.execute("""
            SELECT l.id, l.title_de, l.order_index,
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
            needs_review.append({**issue, "reason": "no_prev"})
            continue

        # 定位
        prev_last_pos = -1
        curr_first_pos = -1

        if prev_lecture[4]:
            prev_last_pos = find_position_progressive(prev_lecture[4], pdf_norm)

        if current_lecture[3]:
            search_start = prev_last_pos + 1 if prev_last_pos >= 0 else 0
            curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, search_start)
            if curr_first_pos < 0 and prev_last_pos >= 0:
                curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, 1000)

        if prev_last_pos < 0 or curr_first_pos < 0 or curr_first_pos <= prev_last_pos:
            needs_review.append({**issue, "reason": f"定位失败 prev={prev_last_pos} curr={curr_first_pos}"})
            continue

        # 提取间隙文本
        ratio = len(pdf_text) / len(pdf_norm)
        approx_start = int(prev_last_pos * ratio)
        approx_end = int(curr_first_pos * ratio)
        gap_text = pdf_text[approx_start:approx_end]

        # 检查"VORTRAG"标题在间隙中的位置
        vortag_pattern = re.compile(
            r"(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|"
            r"ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWÖLFTER|DREIZEHNTER|VIERZEHNTER|"
            r"FÜNFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|"
            r"ZWANZIGSTER)\s+VORTRAG", re.IGNORECASE
        )

        matches = list(vortag_pattern.finditer(gap_text))
        if not matches:
            needs_review.append({**issue, "reason": "无VORTRAG标题"})
            continue

        # 检查最后一个VORTRAG标题是否在间隙末尾20%以内
        last_match = matches[-1]
        last_match_pos = last_match.start()
        gap_length = len(gap_text)

        # 间隙末尾20%的位置
        end_threshold = gap_length * 0.8

        if last_match_pos >= end_threshold:
            # 标题在末尾，可能是下一讲座标题（假阳性）
            # 但也可能是真实缺失的最后一个讲座
            # 检查标题后面是否还有大量内容
            content_after_title = gap_text[last_match.end():]
            if len(content_after_title.strip()) < 200:
                # 标题后面内容很少，说明是下一讲座标题
                false_positive_title_at_end.append({
                    **issue,
                    "reason": f"VORTRAG标题在间隙末尾({last_match_pos}/{gap_length})，是下一讲座标题"
                })
            else:
                # 标题后面还有大量内容，可能缺失讲座
                real_missing.append({
                    **issue,
                    "reason": f"VORTRAG标题后还有{len(content_after_title)}字符内容",
                    "vortag_count": len(matches),
                    "last_vortag_pos": last_match_pos,
                    "gap_length": gap_length
                })
        else:
            # 标题在间隙中间，可能缺失讲座
            real_missing.append({
                **issue,
                "reason": f"VORTRAG标题在间隙中间({last_match_pos}/{gap_length})",
                "vortag_count": len(matches),
                "last_vortag_pos": last_match_pos,
                "gap_length": gap_length
            })

    print(f"\n=== 分类结果 ===")
    print(f"假阳性（标题在末尾）: {len(false_positive_title_at_end)}")
    print(f"真实缺失: {len(real_missing)}")
    print(f"需要检查: {len(needs_review)}")

    # 真实缺失按GA统计
    real_by_ga = Counter(r["ga"] for r in real_missing)
    print(f"\n真实缺失最多的GA:")
    for ga, c in real_by_ga.most_common(20):
        print(f"  {ga}: {c}")

    # 显示真实缺失
    print(f"\n=== 真实缺失间隙 ===")
    for r in real_missing:
        print(f"  {r['ga']} #{r['lecture_id']} ({r.get('lecture_title', '')[:40]})")
        print(f"    {r['reason']}")

    # 保存
    with open("/tmp/p1_gap_final.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total_likely_missing": len(likely_missing),
                "false_positive_title_at_end": len(false_positive_title_at_end),
                "real_missing": len(real_missing),
                "needs_review": len(needs_review)
            },
            "real_missing": real_missing,
            "false_positive_title_at_end": false_positive_title_at_end,
            "needs_review": needs_review
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 /tmp/p1_gap_final.json")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
