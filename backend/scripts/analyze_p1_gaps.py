"""分析P1的large_content_gap问题 - 检查间隙是否是缺失内容

策略：
1. 获取所有large_content_gap问题
2. 对每个间隙，检查是否是导入元数据首句导致的假阳性
3. 对真实间隙，提取PDF原文判断是否是缺失内容
"""
import json
import re
import unicodedata
import psycopg2
from collections import Counter, defaultdict

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
REPORT_FILE = "/tmp/lecture_boundary_report.json"


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


def detect_import_metadata_pattern(ga, cur):
    """检测GA是否所有讲座首句都是导入元数据"""
    cur.execute("""
        SELECT l.id,
               (SELECT s.text_de FROM paragraphs p
                JOIN sentences s ON s.paragraph_id = p.id
                WHERE p.lecture_id = l.id
                ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_sentence
        FROM lectures l
        JOIN books b ON l.book_id = b.id
        WHERE b.ga_number = %s AND l.level = 'lecture'
        ORDER BY l.order_index ASC, l.id ASC
    """, (ga,))

    rows = cur.fetchall()
    if len(rows) < 3:
        return False, None

    first_sentences = [r[1] for r in rows if r[1]]
    if len(first_sentences) < 3:
        return False, None

    prefixes = [s[:30] for s in first_sentences]
    prefix_counts = Counter(prefixes)
    most_common_prefix, count = prefix_counts.most_common(1)[0]

    if count >= len(first_sentences) * 0.6 and count >= 3:
        return True, most_common_prefix

    return False, None


def main():
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)

    # 获取所有gap问题（very_large_gap和large_gap）
    gap_issues = [i for i in report["issues"]
                  if i.get("type") in ("very_large_gap", "large_gap")]

    print(f"large_content_gap问题: {len(gap_issues)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 检测导入元数据模式
    gas = set(i["ga"] for i in gap_issues)
    ga_metadata = {}
    for ga in gas:
        is_meta, prefix = detect_import_metadata_pattern(ga, cur)
        if is_meta:
            ga_metadata[ga] = prefix

    print(f"有导入元数据模式的GA: {len(ga_metadata)}")

    # 分类
    false_positive_meta = []
    false_positive_other = []
    real_gaps = []

    for issue in gap_issues:
        ga = issue["ga"]
        gap_size = issue.get("gap_size", 0)
        desc = issue.get("description", "")

        # 如果GA有导入元数据模式，间隙是假阳性
        if ga in ga_metadata:
            false_positive_meta.append({
                **issue,
                "reason": f"导入元数据首句: '{ga_metadata[ga][:30]}...'"
            })
            continue

        # 解析间隙大小
        m = re.search(r"gap of (\d+) chars", desc)
        if m:
            gap_size = int(m.group(1))

        # 小间隙（<5000）可能是正常的段落间隔
        if gap_size < 5000:
            false_positive_other.append({
                **issue,
                "reason": f"小间隙({gap_size}字符)，可能是正常段落间隔"
            })
            continue

        real_gaps.append(issue)

    print(f"\n=== 分类结果 ===")
    print(f"假阳性（导入元数据）: {len(false_positive_meta)}")
    print(f"假阳性（小间隙）: {len(false_positive_other)}")
    print(f"真实间隙: {len(real_gaps)}")

    # 真实间隙按GA统计
    real_by_ga = Counter(i["ga"] for i in real_gaps)
    print(f"\n真实间隙最多的GA:")
    for ga, c in real_by_ga.most_common(20):
        print(f"  {ga}: {c}")

    # 对真实间隙，提取PDF原文分析
    print(f"\n=== 真实间隙分析 ===")
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    pdf_cache = {}
    results = []

    for issue in real_gaps:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]
        title = issue.get("lecture_title", "")

        if ga not in pdf_cache:
            pdf_data = pdf_texts.get(ga)
            if pdf_data:
                pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
                pdf_cache[ga] = (pdf_text, normalize(pdf_text))
            else:
                pdf_cache[ga] = (None, None)

        pdf_text, pdf_norm = pdf_cache[ga]
        if not pdf_norm:
            results.append({**issue, "status": "no_pdf"})
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
            results.append({**issue, "status": "no_prev_lecture"})
            continue

        # 定位前一讲座末句和当前讲座首句
        prev_last_pos = -1
        curr_first_pos = -1

        if prev_lecture[4]:  # prev last_s
            prev_last_pos = find_position_progressive(prev_lecture[4], pdf_norm)

        if current_lecture[3]:  # current first_s
            search_start = prev_last_pos + 1 if prev_last_pos >= 0 else 0
            curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, search_start)
            if curr_first_pos < 0 and prev_last_pos >= 0:
                curr_first_pos = find_position_progressive(current_lecture[3], pdf_norm, 1000)

        if prev_last_pos >= 0 and curr_first_pos >= 0 and curr_first_pos > prev_last_pos:
            # 提取间隙文本
            ratio = len(pdf_text) / len(pdf_norm)
            approx_start = int(prev_last_pos * ratio)
            approx_end = int(curr_first_pos * ratio)
            gap_text = pdf_text[approx_start:approx_end]

            # 分析间隙内容
            # 检查是否包含讲座标志
            date_location_pattern = re.compile(
                r"(Berlin|München|Stuttgart|Dornach|Basel|Wien|Zürich|Bern|Köln|"
                r"Frankfurt|Hamburg|Dresden|Leipzig|Weimar|Jena|Erfurt|Nürnberg)[,\s]+"
                r"(\d{1,2}\.\s*)?(Januar|Februar|März|April|Mai|Juni|Juli|August|"
                r"September|Oktober|November|Dezember|\d{1,2}\.)\s*\d{4}",
                re.IGNORECASE
            )
            lecture_title_pattern = re.compile(
                r"(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|"
                r"ACHTER|NEUNTER|ZEHNTER)\s+VORTRAG", re.IGNORECASE
            )
            appendix_pattern = re.compile(
                r"(NAMENREGISTER|PERSONENREGISTER|BIBLIOGRAPHIE|LITERATURVERZEICHNIS|"
                r"HINWEISE|ANHANG|NACHWORT|VORWORT|INHALTSVERZEICHNIS|"
                r"REISEVERZEICHNIS|VERZEICHNIS)", re.IGNORECASE
            )

            has_date_location = bool(date_location_pattern.search(gap_text))
            has_lecture_title = bool(lecture_title_pattern.search(gap_text))
            has_appendix = bool(appendix_pattern.search(gap_text))
            date_count = len(date_location_pattern.findall(gap_text))

            if has_lecture_title:
                status = "likely_missing_lectures"
                reason = f"包含讲座标题模式"
            elif has_date_location and date_count >= 3:
                status = "likely_missing_lectures"
                reason = f"包含{date_count}个日期+地点"
            elif has_appendix:
                status = "appendix_content"
                reason = "附录内容"
            elif has_date_location:
                status = "needs_review"
                reason = f"包含{date_count}个日期+地点"
            else:
                status = "probably_not_missing"
                reason = "未检测到讲座标志"

            results.append({
                **issue,
                "status": status,
                "reason": reason,
                "gap_text_preview": gap_text[:500],
                "date_count": date_count,
                "has_lecture_title": has_lecture_title,
                "has_appendix": has_appendix
            })
        else:
            results.append({
                **issue,
                "status": "cannot_locate",
                "reason": f"prev_last={prev_last_pos}, curr_first={curr_first_pos}"
            })

    # 统计
    status_counts = Counter(r["status"] for r in results)
    print(f"\n真实间隙分析结果:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")

    # 显示需要关注的
    print(f"\n=== 需要关注的间隙 ===")
    for r in results:
        if r["status"] in ("likely_missing_lectures", "needs_review"):
            print(f"\n{r['ga']} #{r['lecture_id']} ({r.get('lecture_title', '')[:40]})")
            print(f"  状态: {r['status']} - {r['reason']}")
            if r.get("gap_text_preview"):
                print(f"  间隙预览: {r['gap_text_preview'][:200]}")

    # 保存
    with open("/tmp/p1_gap_analysis.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total": len(gap_issues),
                "false_positive_meta": len(false_positive_meta),
                "false_positive_other": len(false_positive_other),
                "real_gaps": len(real_gaps),
                "status_counts": dict(status_counts)
            },
            "real_gap_results": results,
            "false_positive_meta": false_positive_meta,
            "false_positive_other": false_positive_other
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 /tmp/p1_gap_analysis.json")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
