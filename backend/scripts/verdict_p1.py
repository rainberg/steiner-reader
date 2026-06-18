"""对15个确认真实问题进行最终验证：检查DB讲座内容是否完整。

关键判断：
- overlap/order_bad可能是首句在目录中出现导致定位错误，实际内容可能正确
- 检查DB中讲座的段落数、句子数、总字符数，判断内容是否完整
- 如果内容完整，说明只是定位错误，不是真实问题
"""
import json
import re
import unicodedata
import psycopg2

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
INPUT_FILE = "/tmp/p1_final_confirm.json"


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
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    confirmed = data["confirmed_issues"]
    print(f"确认真实问题: {len(confirmed)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    results = []

    for issue in confirmed:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]
        title = issue.get("lecture_title", "")
        issue_type = issue["type"]

        print(f"\n{'='*60}")
        print(f"{ga} #{lecture_id} ({title[:50]}) [{issue_type}]")

        # 获取讲座的段落数、句子数、总字符数
        cur.execute("""
            SELECT
                COUNT(DISTINCT p.id) as paragraph_count,
                COUNT(s.id) as sentence_count,
                COALESCE(SUM(LENGTH(s.text_de)), 0) as total_chars
            FROM lectures l
            LEFT JOIN paragraphs p ON p.lecture_id = l.id
            LEFT JOIN sentences s ON s.paragraph_id = p.id
            WHERE l.id = %s
        """, (lecture_id,))

        row = cur.fetchone()
        para_count = row[0] or 0
        sent_count = row[1] or 0
        total_chars = row[2] or 0

        print(f"  DB内容: {para_count}段落, {sent_count}句子, {total_chars}字符")

        # 获取前一个讲座的信息
        cur.execute("""
            SELECT l.id, l.title_de, l.order_index
            FROM lectures l
            JOIN books b ON l.book_id = b.id
            WHERE b.ga_number = %s AND l.level = 'lecture'
                AND l.order_index < (
                    SELECT order_index FROM lectures WHERE id = %s
                )
            ORDER BY l.order_index DESC LIMIT 1
        """, (ga, lecture_id))
        prev = cur.fetchone()

        # 获取后一个讲座的信息
        cur.execute("""
            SELECT l.id, l.title_de, l.order_index
            FROM lectures l
            JOIN books b ON l.book_id = b.id
            WHERE b.ga_number = %s AND l.level = 'lecture'
                AND l.order_index > (
                    SELECT order_index FROM lectures WHERE id = %s
                )
            ORDER BY l.order_index ASC LIMIT 1
        """, (ga, lecture_id))
        next_l = cur.fetchone()

        if prev:
            print(f"  前一讲座: #{prev[0]} (order={prev[2]}) {prev[1][:40]}")
        if next_l:
            print(f"  后一讲座: #{next_l[0]} (order={next_l[2]}) {next_l[1][:40]}")

        # 判断内容是否完整
        # 如果讲座有>50句子和>5000字符，内容可能是完整的
        is_content_complete = sent_count > 50 and total_chars > 5000

        # 对overlap/order_bad，如果内容完整，说明只是定位错误
        if issue_type in ("overlap", "order_bad"):
            if is_content_complete:
                verdict = "定位错误（内容完整）"
                is_real_issue = False
            elif sent_count < 5:
                verdict = "内容过少（可能是真实问题）"
                is_real_issue = True
            else:
                verdict = "需进一步检查"
                is_real_issue = None
        elif issue_type == "last_not_found":
            # last_not_found的2个都是引用/文献提示
            if "Bibl.-Nr." in issue.get("db_text", "") or "Verzeichmsse" in issue.get("db_text", ""):
                verdict = "引用/文献提示（假阳性）"
                is_real_issue = False
            else:
                verdict = "需进一步检查"
                is_real_issue = None
        else:
            verdict = "需进一步检查"
            is_real_issue = None

        print(f"  判定: {verdict}")

        # 对定位错误的overlap/order_bad，尝试重新定位首句
        if issue_type in ("overlap", "order_bad") and not is_real_issue:
            # 获取首句和末句
            cur.execute("""
                SELECT
                    (SELECT s.text_de FROM paragraphs p
                     JOIN sentences s ON s.paragraph_id = p.id
                     WHERE p.lecture_id = %s
                     ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_s,
                    (SELECT s.text_de FROM paragraphs p
                     JOIN sentences s ON s.paragraph_id = p.id
                     WHERE p.lecture_id = %s
                     ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_s
            """, (lecture_id, lecture_id))
            row = cur.fetchone()
            first_s = row[0] or ""
            last_s = row[1] or ""

            pdf_data = pdf_texts.get(ga)
            if pdf_data and first_s:
                pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
                pdf_norm = normalize(pdf_text)

                # 从前一讲座末句之后开始搜索
                if prev:
                    cur.execute("""
                        SELECT s.text_de FROM paragraphs p
                        JOIN sentences s ON s.paragraph_id = p.id
                        WHERE p.lecture_id = %s
                        ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1
                    """, (prev[0],))
                    prev_last = cur.fetchone()[0]
                    if prev_last:
                        prev_last_pos = find_position_progressive(prev_last, pdf_norm)
                        if prev_last_pos >= 0:
                            # 从前一讲座末句之后搜索当前讲座首句
                            new_first_pos = find_position_progressive(first_s, pdf_norm, prev_last_pos + 1)
                            print(f"  重新定位: prev_last={prev_last_pos}, new_first={new_first_pos}")
                            if new_first_pos >= 0:
                                issue["new_first_pos"] = new_first_pos
                                if new_first_pos > prev_last_pos:
                                    verdict = "定位错误已修正（内容正确）"
                                    is_real_issue = False

        result = {
            **issue,
            "paragraph_count": para_count,
            "sentence_count": sent_count,
            "total_chars": total_chars,
            "prev_lecture_id": prev[0] if prev else None,
            "next_lecture_id": next_l[0] if next_l else None,
            "verdict": verdict,
            "is_real_issue": is_real_issue
        }
        results.append(result)

    # 汇总
    print(f"\n{'='*60}")
    print(f"=== 最终汇总 ===")
    real_count = sum(1 for r in results if r["is_real_issue"])
    false_count = sum(1 for r in results if not r["is_real_issue"])
    unknown_count = sum(1 for r in results if r["is_real_issue"] is None)

    print(f"真实问题: {real_count}")
    print(f"假阳性: {false_count}")
    print(f"待确认: {unknown_count}")

    print(f"\n真实问题列表:")
    for r in results:
        if r["is_real_issue"]:
            print(f"  {r['ga']} #{r['lecture_id']} ({r['lecture_title'][:40]}) [{r['type']}]")
            print(f"    {r['verdict']}")

    print(f"\n假阳性列表:")
    for r in results:
        if not r["is_real_issue"]:
            print(f"  {r['ga']} #{r['lecture_id']} ({r['lecture_title'][:40]}) [{r['type']}]")
            print(f"    {r['verdict']}")

    # 保存
    with open("/tmp/p1_verdict.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total": len(results),
                "real": real_count,
                "false_positive": false_count,
                "unknown": unknown_count
            },
            "results": results
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 /tmp/p1_verdict.json")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
