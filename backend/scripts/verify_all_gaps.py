"""批量验证所有likely_missing_lectures - 检查讲座内容是否完整

关键判断：如果讲座有>50句子，说明内容完整，gap是定位错误（假阳性）
"""
import json
import psycopg2
from collections import Counter

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"


def main():
    with open("/tmp/p1_gap_final.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    real_missing = data["real_missing"]
    print(f"待验证: {len(real_missing)}个")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    false_positive_content_complete = []
    actual_missing = []

    for issue in real_missing:
        lecture_id = issue["lecture_id"]

        # 获取讲座内容量
        cur.execute("""
            SELECT COUNT(s.id), COALESCE(SUM(LENGTH(s.text_de)), 0)
            FROM paragraphs p
            JOIN sentences s ON s.paragraph_id = p.id
            WHERE p.lecture_id = %s
        """, (lecture_id,))

        row = cur.fetchone()
        sent_count = row[0] or 0
        total_chars = row[1] or 0

        # 判断内容是否完整
        if sent_count > 50 and total_chars > 5000:
            false_positive_content_complete.append({
                **issue,
                "sent_count": sent_count,
                "total_chars": total_chars,
                "reason": f"内容完整({sent_count}句,{total_chars}字符)，gap是定位错误"
            })
        elif sent_count < 5:
            actual_missing.append({
                **issue,
                "sent_count": sent_count,
                "total_chars": total_chars,
                "reason": f"内容过少({sent_count}句,{total_chars}字符)，可能缺失"
            })
        else:
            # 中等内容量，需要进一步检查
            actual_missing.append({
                **issue,
                "sent_count": sent_count,
                "total_chars": total_chars,
                "reason": f"内容中等({sent_count}句,{total_chars}字符)，需确认"
            })

    print(f"\n=== 验证结果 ===")
    print(f"假阳性（内容完整）: {len(false_positive_content_complete)}")
    print(f"可能缺失/需确认: {len(actual_missing)}")

    # 按GA统计
    actual_by_ga = Counter(r["ga"] for r in actual_missing)
    print(f"\n可能缺失最多的GA:")
    for ga, c in actual_by_ga.most_common(20):
        print(f"  {ga}: {c}")

    # 显示可能缺失的
    print(f"\n=== 可能缺失/需确认 ===")
    for r in actual_missing:
        print(f"  {r['ga']} #{r['lecture_id']} ({r.get('lecture_title', '')[:40]})")
        print(f"    {r['reason']}")

    # 保存
    with open("/tmp/p1_gap_verified.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "total": len(real_missing),
                "false_positive_content_complete": len(false_positive_content_complete),
                "actual_missing": len(actual_missing)
            },
            "actual_missing": actual_missing,
            "false_positive": false_positive_content_complete
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 /tmp/p1_gap_verified.json")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
