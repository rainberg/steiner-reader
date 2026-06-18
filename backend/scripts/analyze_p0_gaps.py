"""分析P0的10个可能缺失讲座间隙 - 提取PDF原文间隙内容，判断是否真的缺失讲座。

对每个P0问题:
1. 获取该GA的PDF全文和DB讲座列表
2. 定位间隙在PDF中的位置
3. 提取间隙文本（前500字符）
4. 分析是否包含讲座标志（日期+地点、标题等）
5. 输出确认结果
"""
import json
import re
import unicodedata
import psycopg2
from collections import defaultdict

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
REPORT_FILE = "/tmp/lecture_boundary_report.json"
OUTPUT_FILE = "/tmp/p0_analysis.json"


def normalize(s):
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.replace("ß", "ss")
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


def find_position(needle_norm, haystack_norm, start_pos=0):
    pos = haystack_norm.find(needle_norm, start_pos)
    return pos


def find_position_progressive(sentence, haystack_norm, start_pos=0):
    """渐进式搜索"""
    norm = normalize(sentence)
    for length in [80, 60, 50, 40, 30, 25, 20]:
        if len(norm) >= length:
            pos = haystack_norm.find(norm[:length], start_pos)
            if pos >= 0:
                return pos
    # 尝试中间片段
    if len(norm) >= 40:
        mid = len(norm) // 2
        pos = haystack_norm.find(norm[mid-20:mid+20], start_pos)
        if pos >= 0:
            return pos
    return -1


def main():
    # 加载PDF全文
    print("加载PDF全文...")
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)
    print(f"  {len(pdf_texts)} 个GA的PDF全文")

    # 加载验证报告
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)

    # 提取P0问题
    p0_issues = [i for i in report["issues"]
                 if i.get("has_date") and i.get("has_location")]
    print(f"P0问题: {len(p0_issues)}个")

    # 连接数据库
    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    results = []

    for issue in p0_issues:
        ga = issue["ga"]
        lecture_id = issue["lecture_id"]
        lecture_title = issue.get("lecture_title", "")
        gap_size = issue.get("gap_size", 0)

        print(f"\n{'='*60}")
        print(f"分析 {ga} #{lecture_id} ({lecture_title[:50]})")
        print(f"间隙大小: {gap_size} 字符")

        # 获取PDF全文
        pdf_key = ga if ga.upper().startswith("GA") else f"GA{ga}"
        pdf_data = pdf_texts.get(pdf_key)
        if not pdf_data:
            print(f"  ✗ 无PDF全文")
            results.append({
                "ga": ga, "lecture_id": lecture_id,
                "status": "no_pdf",
                "message": "无PDF全文，无法分析"
            })
            continue
        # PDF数据是dict，包含full_text字段
        pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
        pdf_norm = normalize(pdf_text)

        # 获取该GA的所有lecture，按order_index排序
        cur.execute("""
            SELECT l.id, l.title_de, l.order_index, l.level, l.parent_id,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1) as first_sentence,
                   (SELECT s.text_de FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = l.id
                    ORDER BY p.order_index DESC, s.order_index DESC LIMIT 1) as last_sentence
            FROM lectures l
            JOIN books b ON l.book_id = b.id
            WHERE b.ga_number = %s AND l.level = 'lecture'
            ORDER BY l.order_index ASC, l.id ASC
        """, (ga,))

        lectures = cur.fetchall()
        print(f"  DB讲座数: {len(lectures)}")

        # 找到当前lecture和前一个lecture
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

        if current_lecture is None:
            print(f"  ✗ 未找到lecture {lecture_id}")
            results.append({
                "ga": ga, "lecture_id": lecture_id,
                "status": "lecture_not_found",
                "message": "未找到lecture"
            })
            continue

        # 定位前一个lecture的末句和当前lecture的首句
        prev_last_pos = -1
        curr_first_pos = -1

        if prev_lecture and prev_lecture[6]:  # prev last_sentence
            prev_last_pos = find_position_progressive(prev_lecture[6], pdf_norm)
            print(f"  前一讲座 #{prev_lecture[0]} 末句位置: {prev_last_pos}")
            print(f"    末句: {prev_lecture[6][:80]}")

        if current_lecture[5]:  # current first_sentence
            # 从前一讲座末句位置之后开始搜索，避免定位到目录
            search_start = prev_last_pos + 1 if prev_last_pos >= 0 else 0
            curr_first_pos = find_position_progressive(current_lecture[5], pdf_norm, search_start)
            # 如果从prev_last_pos之后找不到，尝试从0搜索（但跳过前1000字符避免目录）
            if curr_first_pos < 0 and prev_last_pos >= 0:
                curr_first_pos = find_position_progressive(current_lecture[5], pdf_norm, 1000)
            print(f"  当前讲座 #{current_lecture[0]} 首句位置: {curr_first_pos}")
            print(f"    首句: {current_lecture[5][:80]}")

        # 提取间隙文本
        gap_text = ""
        gap_start = 0
        gap_end = 0

        if prev_last_pos >= 0 and curr_first_pos >= 0 and curr_first_pos > prev_last_pos:
            gap_start = prev_last_pos
            gap_end = curr_first_pos
            # 从原始PDF文本中提取间隙（使用归一化位置近似）
            gap_norm = pdf_norm[gap_start:gap_end]
            # 转换回可读文本（从原始PDF中提取对应位置）
            # 由于归一化会移除字符，我们使用近似位置
            approx_start = int(gap_start * len(pdf_text) / len(pdf_norm))
            approx_end = int(gap_end * len(pdf_text) / len(pdf_norm))
            gap_text = pdf_text[approx_start:approx_end]

            print(f"  间隙位置: {gap_start} - {gap_end}")
            print(f"  间隙文本前500字符:")
            print(f"    {gap_text[:500]}")
        else:
            print(f"  ✗ 无法定位间隙 (prev_last={prev_last_pos}, curr_first={curr_first_pos})")

        # 分析间隙内容
        gap_analysis = analyze_gap(gap_text, gap_size)

        result = {
            "ga": ga,
            "lecture_id": lecture_id,
            "lecture_title": lecture_title,
            "gap_size": gap_size,
            "prev_lecture_id": prev_lecture[0] if prev_lecture else None,
            "prev_lecture_title": prev_lecture[1] if prev_lecture else None,
            "prev_last_pos": prev_last_pos,
            "curr_first_pos": curr_first_pos,
            "gap_text_preview": gap_text[:1000],
            "analysis": gap_analysis,
            "status": gap_analysis["status"]
        }
        results.append(result)

        print(f"\n  分析结果: {gap_analysis['status']}")
        print(f"  {gap_analysis['message']}")

    # 保存结果
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n{'='*60}")
    print(f"结果保存到 {OUTPUT_FILE}")

    # 汇总
    status_counts = defaultdict(int)
    for r in results:
        status_counts[r["status"]] += 1
    print(f"\n汇总:")
    for status, count in status_counts.items():
        print(f"  {status}: {count}")

    cur.close()
    conn.close()


def analyze_gap(gap_text, gap_size):
    """分析间隙内容，判断是否真的缺失讲座"""
    if not gap_text:
        return {
            "status": "cannot_analyze",
            "message": "无法提取间隙文本",
            "is_missing_lecture": False
        }

    # 检查是否包含讲座标志
    # 1. 日期+地点模式（如 "Berlin, 15. März 1923"）
    date_location_pattern = re.compile(
        r"(Berlin|München|Stuttgart|Dornach|Basel|Wien|Zürich|Bern|Köln|"
        r"Frankfurt|Hamburg|Dresden|Leipzig|Weimar|Jena|Erfurt|Nürnberg|"
        r"Breslau|Prag|Paris|London|Torquay|Penmaenmawr|Oxford|Arnheim|"
        r"Koberwitz|Düsseldorf|Hannover|Kassel|Darmstadt|Heidelberg)[,\s]+"
        r"(\d{1,2}\.\s*)?(Januar|Februar|März|April|Mai|Juni|Juli|August|"
        r"September|Oktober|November|Dezember|\d{1,2}\.)\s*\d{4}",
        re.IGNORECASE
    )

    # 2. 讲座标题模式（如 "ERSTER VORTRAG", "DRITTER VORTRAG"）
    lecture_title_pattern = re.compile(
        r"(ERSTER|ZWEITER|DRITTER|VIERTER|FÜNFTER|SECHSTER|SIEBENTER|"
        r"ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWÖLFTER|DREIZEHNTER|VIERZEHNTER|"
        r"FÜNFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|"
        r"ZWANZIGSTER)\s+VORTRAG",
        re.IGNORECASE
    )

    # 3. 附录/索引模式
    appendix_pattern = re.compile(
        r"(NAMENREGISTER|PERSONENREGISTER|BIBLIOGRAPHIE|LITERATURVERZEICHNIS|"
        r"HINWEISE|ANHANG|NACHWORT|VORWORT|INHALTSVERZEICHNIS|"
        r"REISEVERZEICHNIS|VERZEICHNIS)",
        re.IGNORECASE
    )

    # 4. 书信模式（GA262是书信集）
    letter_pattern = re.compile(
        r"(Brief|Briefe|An\s|Von\s|Liebe|Lieber|Herzlichst|"
        r"Dein|Rudolf|Marie)",
        re.IGNORECASE
    )

    has_date_location = bool(date_location_pattern.search(gap_text))
    has_lecture_title = bool(lecture_title_pattern.search(gap_text))
    has_appendix = bool(appendix_pattern.search(gap_text))
    has_letter = bool(letter_pattern.search(gap_text))

    # 统计日期+地点出现次数
    date_location_count = len(date_location_pattern.findall(gap_text))
    lecture_title_count = len(lecture_title_pattern.findall(gap_text))

    # 判断
    if has_lecture_title and lecture_title_count >= 2:
        return {
            "status": "likely_missing_lectures",
            "message": f"间隙包含{lecture_title_count}个讲座标题，高度怀疑缺失讲座",
            "is_missing_lecture": True,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }
    elif has_date_location and date_location_count >= 3:
        return {
            "status": "likely_missing_lectures",
            "message": f"间隙包含{date_location_count}个日期+地点模式，可能缺失多个讲座",
            "is_missing_lecture": True,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }
    elif has_appendix:
        return {
            "status": "appendix_content",
            "message": "间隙是附录/索引内容，非缺失讲座",
            "is_missing_lecture": False,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }
    elif has_letter and gap_size > 100000:
        return {
            "status": "letter_content",
            "message": "间隙是书信内容（GA262是书信集），可能是正常结构",
            "is_missing_lecture": False,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }
    elif has_date_location:
        return {
            "status": "needs_review",
            "message": f"间隙包含{date_location_count}个日期+地点，需人工确认",
            "is_missing_lecture": None,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }
    else:
        return {
            "status": "probably_not_missing",
            "message": "间隙未检测到讲座标志，可能不是缺失讲座",
            "is_missing_lecture": False,
            "date_location_count": date_location_count,
            "lecture_title_count": lecture_title_count,
            "has_appendix": has_appendix,
            "has_letter": has_letter
        }


if __name__ == "__main__":
    main()
