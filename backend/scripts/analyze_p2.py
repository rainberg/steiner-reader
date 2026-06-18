"""P2问题批量处理 - 基于之前的分析模式批量过滤

P2问题分类：
- short_content: 短内容（<20字符）
- appendix_content: 附录类讲座
- citation: 引用/参考文献
- small_diff: 差距较小
- medium_gap: 中等间隙
- unknown: 无法解析

策略：
- short_content, appendix_content, citation: 假阳性
- small_diff: 假阳性（差距小）
- medium_gap: 检查是否是导入元数据
- unknown: 假阳性
"""
import json
import re
import unicodedata
import psycopg2
from collections import Counter, defaultdict

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"


def normalize(s):
    s = s.lower()
    s = unicodedata.normalize("NFKD", s)
    s = s.encode("ascii", "ignore").decode("ascii")
    s = s.replace("ß", "ss")
    s = re.sub(r"[^a-z0-9]", "", s)
    return s


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
        return False

    first_sentences = [r[1] for r in rows if r[1]]
    if len(first_sentences) < 3:
        return False

    prefixes = [s[:30] for s in first_sentences]
    prefix_counts = Counter(prefixes)
    most_common_prefix, count = prefix_counts.most_common(1)[0]

    if count >= len(first_sentences) * 0.6 and count >= 3:
        return True

    return False


def main():
    # 读取comprehensive_analysis_v3的结果
    with open("/tmp/comprehensive_analysis_v3.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 获取P2问题
    p2_issues = data.get("by_priority", {}).get("P2-needs_review", [])
    if not p2_issues:
        # 尝试其他结构
        p2_issues = data.get("p2_needs_review", [])

    print(f"P2问题: {len(p2_issues)}")

    if not p2_issues:
        print("无P2问题")
        return

    # 按category统计
    cat_counts = Counter(i.get("category", "unknown") for i in p2_issues)
    print(f"\n按category统计:")
    for c, count in cat_counts.most_common():
        print(f"  {c}: {count}")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 检测导入元数据模式
    gas = set(i.get("ga", "") for i in p2_issues)
    ga_metadata = set()
    for ga in gas:
        if ga and detect_import_metadata_pattern(ga, cur):
            ga_metadata.add(ga)

    print(f"\n有导入元数据模式的GA: {len(ga_metadata)}")

    # 分类
    false_positive = []
    needs_review = []

    for issue in p2_issues:
        ga = issue.get("ga", "")
        category = issue.get("category", "unknown")
        reason = issue.get("reason", "")

        # 导入元数据 -> 假阳性
        if ga in ga_metadata:
            false_positive.append({**issue, "verdict": "导入元数据首句"})
            continue

        # 短内容、附录、引用 -> 假阳性
        if category in ("short_content", "appendix_content", "citation"):
            false_positive.append({**issue, "verdict": f"{category}"})
            continue

        # 小差距 -> 假阳性
        if category == "small_diff":
            false_positive.append({**issue, "verdict": "差距较小"})
            continue

        # 无法解析 -> 假阳性
        if category == "unknown":
            false_positive.append({**issue, "verdict": "无法解析"})
            continue

        # 中等间隙 -> 需要检查
        if category == "medium_gap":
            # 检查讲座内容是否完整
            lecture_id = issue.get("lecture_id")
            if lecture_id:
                cur.execute("""
                    SELECT COUNT(s.id), COALESCE(SUM(LENGTH(s.text_de)), 0)
                    FROM paragraphs p
                    JOIN sentences s ON s.paragraph_id = p.id
                    WHERE p.lecture_id = %s
                """, (lecture_id,))
                row = cur.fetchone()
                sent_count = row[0] or 0
                total_chars = row[1] or 0

                if sent_count > 50 and total_chars > 5000:
                    false_positive.append({**issue, "verdict": f"内容完整({sent_count}句)"})
                else:
                    needs_review.append({**issue, "sent_count": sent_count, "total_chars": total_chars})
            else:
                needs_review.append(issue)
        else:
            needs_review.append(issue)

    print(f"\n=== 分类结果 ===")
    print(f"假阳性: {len(false_positive)}")
    print(f"需要审查: {len(needs_review)}")

    # 需要审查的按GA统计
    if needs_review:
        review_by_ga = Counter(i.get("ga", "") for i in needs_review)
        print(f"\n需要审查最多的GA:")
        for ga, c in review_by_ga.most_common(20):
            print(f"  {ga}: {c}")

        # 显示需要审查的
        print(f"\n=== 需要审查的问题 ===")
        for i in needs_review[:20]:
            print(f"  {i.get('ga', '')} #{i.get('lecture_id', '')} ({i.get('lecture_title', '')[:40]})")
            print(f"    {i.get('category', '')}: {i.get('reason', '')}")
            if i.get("sent_count"):
                print(f"    内容: {i['sent_count']}句, {i['total_chars']}字符")

    # 保存
    with open("/tmp/p2_analysis.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total": len(p2_issues),
                "false_positive": len(false_positive),
                "needs_review": len(needs_review)
            },
            "needs_review": needs_review,
            "false_positive": false_positive
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 /tmp/p2_analysis.json")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
