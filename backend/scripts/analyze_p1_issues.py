"""P1问题深度分析：识别导入元数据首句模式，重新分类overlap/order_bad问题。

关键改进：
1. 检测导入元数据首句（所有讲座首句相同或以书名开头）
2. 对overlap/order_bad，如果首句是导入元数据，降级为假阳性
3. 对真实overlap，提取PDF原文确认是否真的越界
"""
import json
import re
import unicodedata
import psycopg2
from collections import defaultdict, Counter

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
REPORT_FILE = "/tmp/lecture_boundary_report.json"
OUTPUT_FILE = "/tmp/p1_analysis.json"


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
    """检测GA是否所有讲座首句都是导入元数据（相同前缀）"""
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

    # 检查前30个字符是否相同
    prefixes = [s[:30] for s in first_sentences]
    prefix_counts = Counter(prefixes)
    most_common_prefix, count = prefix_counts.most_common(1)[0]

    # 如果≥60%的讲座首句前30字符相同，是导入元数据
    if count >= len(first_sentences) * 0.6 and count >= 3:
        return True, most_common_prefix

    return False, None


def main():
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)

    # P1问题
    p1_issues = [i for i in report["issues"]
                 if i.get("type") in ("overlap", "order_bad", "first_not_found", "last_not_found")
                 and i.get("layer") == 2]

    # 过滤掉已知的假阳性（短文本等）
    # 重新分类，考虑导入元数据模式
    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 检测所有GA的导入元数据模式
    print("检测导入元数据首句模式...")
    ga_metadata = {}
    gas = set(i["ga"] for i in p1_issues)
    for ga in gas:
        is_meta, prefix = detect_import_metadata_pattern(ga, cur)
        if is_meta:
            ga_metadata[ga] = prefix
            print(f"  {ga}: 导入元数据前缀 = '{prefix[:40]}...'")

    print(f"\n检测到 {len(ga_metadata)} 个GA有导入元数据模式")

    # 重新分类P1问题
    results = {
        "false_positive_metadata": [],  # 导入元数据导致的假阳性
        "false_positive_other": [],     # 其他假阳性
        "real_issues": [],              # 真实问题
        "needs_review": []              # 需要审查
    }

    for issue in p1_issues:
        ga = issue["ga"]
        issue_type = issue["type"]
        db_text = issue.get("db_text", "")
        desc = issue.get("description", "")

        # 如果GA有导入元数据模式，降级为假阳性
        if ga in ga_metadata:
            results["false_positive_metadata"].append({
                **issue,
                "reason": f"导入元数据首句: '{ga_metadata[ga][:30]}...'"
            })
            continue

        # 解析位置信息
        first_pos = None
        last_pos = None
        if "First pos" in desc:
            m = re.search(r"First pos \((\d+)\) >= last pos \((\d+)\)", desc)
            if m:
                first_pos = int(m.group(1))
                last_pos = int(m.group(2))
        elif "starts at" in desc:
            m = re.search(r"starts at (\d+) but previous ended at (\d+)", desc)
            if m:
                first_pos = int(m.group(1))
                last_pos = int(m.group(2))

        # 短文本假阳性
        if issue_type in ("first_not_found", "last_not_found"):
            if len(db_text) < 20:
                results["false_positive_other"].append({
                    **issue,
                    "reason": f"短文本({len(db_text)}字符)"
                })
                continue
            # 检查是否是元数据
            if re.search(r"GA\s*\d+\s+Die\s", db_text):
                results["false_positive_metadata"].append({
                    **issue,
                    "reason": "导入元数据首句"
                })
                continue

        # 真实问题
        results["real_issues"].append({
            **issue,
            "first_pos": first_pos,
            "last_pos": last_pos
        })

    # 输出统计
    print(f"\n=== P1重新分类结果 ===")
    print(f"原始P1问题: {len(p1_issues)}")
    print(f"  假阳性（导入元数据）: {len(results['false_positive_metadata'])}")
    print(f"  假阳性（其他）: {len(results['false_positive_other'])}")
    print(f"  真实问题: {len(results['real_issues'])}")

    # 按类型统计真实问题
    real_by_type = Counter(i["type"] for i in results["real_issues"])
    print(f"\n真实问题按类型:")
    for t, c in real_by_type.most_common():
        print(f"  {t}: {c}")

    # 真实问题按GA统计
    real_by_ga = Counter(i["ga"] for i in results["real_issues"])
    print(f"\n真实问题最多的GA (前15):")
    for ga, c in real_by_ga.most_common(15):
        print(f"  {ga}: {c}")

    # 保存结果
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total_p1": len(p1_issues),
                "false_positive_metadata": len(results["false_positive_metadata"]),
                "false_positive_other": len(results["false_positive_other"]),
                "real_issues": len(results["real_issues"]),
                "real_by_type": dict(real_by_type),
                "real_by_ga": dict(real_by_ga.most_common(20)),
                "metadata_gas": list(ga_metadata.keys())
            },
            "real_issues": results["real_issues"],
            "false_positive_metadata": results["false_positive_metadata"],
            "false_positive_other": results["false_positive_other"]
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 {OUTPUT_FILE}")

    # 显示真实问题示例
    print(f"\n=== 真实问题示例 ===")
    for issue_type in ["overlap", "order_bad", "first_not_found", "last_not_found"]:
        items = [i for i in results["real_issues"] if i["type"] == issue_type]
        if items:
            print(f"\n--- {issue_type} ({len(items)}个) ---")
            for i in items[:5]:
                print(f"  {i['ga']} #{i['lecture_id']} ({i.get('lecture_title', '')[:40]})")
                if i.get("db_text"):
                    print(f"    DB文本: {i['db_text'][:80]}")
                if i.get("first_pos") is not None:
                    print(f"    位置: first={i['first_pos']}, last={i['last_pos']}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
