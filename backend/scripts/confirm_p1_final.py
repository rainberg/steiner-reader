"""对问题最多的GA进行深入检查，提取PDF原文确认是否真的影响阅读。

策略：
1. 对每个问题，提取PDF中对应位置的原文
2. 判断是否是真实内容问题（影响阅读）vs 元数据/附录问题
3. 输出最终需要修复的问题列表
"""
import json
import re
import unicodedata
import psycopg2
from collections import Counter, defaultdict

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
INPUT_FILE = "/tmp/p1_real_issues.json"
OUTPUT_FILE = "/tmp/p1_final_confirm.json"


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


def is_non_content(title, db_text):
    """判断是否是非内容（勘误表、索引、附录、元数据）"""
    if not title:
        return False, ""
    title_upper = title.upper()

    # 勘误表
    if "KORRIGENDA" in title_upper or "ERRATA" in title_upper:
        return True, "勘误表"
    # 索引
    if "REGISTER" in title_upper or "VERZEICHNIS" in title_upper:
        return True, "索引"
    # 附录
    if title_upper.startswith("ANHANG") or "HINWEISE" in title_upper:
        return True, "附录"
    # 元数据首句
    if db_text:
        if re.match(r"^[,(-]?\d{4}", db_text.strip()):
            return True, "元数据首句"
        if re.match(r"^G\d+\s", db_text.strip(), re.IGNORECASE):
            return True, "元数据首句"
        if re.match(r"^GA\s*\d+", db_text.strip(), re.IGNORECASE):
            return True, "元数据首句"
    return False, ""


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    final_real = data["final_real_issues"]
    print(f"输入: {len(final_real)}个真实问题")

    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 按GA分组
    by_ga = defaultdict(list)
    for issue in final_real:
        by_ga[issue["ga"]].append(issue)

    # 对每个问题进行最终确认
    confirmed_issues = []
    non_content_issues = []

    pdf_cache = {}

    for issue in final_real:
        ga = issue["ga"]
        title = issue.get("lecture_title", "")
        db_text = issue.get("db_text", "")
        issue_type = issue["type"]

        # 检查是否是非内容
        is_non, reason = is_non_content(title, db_text)
        if is_non:
            non_content_issues.append({**issue, "reason": reason})
            continue

        # 加载PDF
        if ga not in pdf_cache:
            pdf_data = pdf_texts.get(ga)
            if pdf_data:
                pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
                pdf_cache[ga] = (pdf_text, normalize(pdf_text))
            else:
                pdf_cache[ga] = (None, None)

        pdf_text, pdf_norm = pdf_cache[ga]

        if issue_type in ("overlap", "order_bad"):
            # 对overlap/order_bad，检查首句是否定位到目录
            first_pos = issue.get("first_pos")
            if first_pos is not None and first_pos < 5000:
                # 首句定位到PDF前5000字符，可能是目录
                # 检查PDF前5000字符是否包含目录标志
                if pdf_text:
                    front_text = pdf_text[:5000]
                    if re.search(r"(Inhalt|INHALT|Table of Contents)", front_text, re.IGNORECASE):
                        non_content_issues.append({**issue, "reason": "首句定位到目录区"})
                        continue
                    # 检查是否是前言区
                    if first_pos < 1000:
                        non_content_issues.append({**issue, "reason": "首句定位到PDF开头（可能是标题页）"})
                        continue

            # 检查多个讲座是否定位到同一位置
            if first_pos is not None:
                same_pos_count = sum(1 for i in by_ga[ga]
                                     if i.get("first_pos") == first_pos
                                     and i["type"] in ("overlap", "order_bad"))
                if same_pos_count >= 2:
                    non_content_issues.append({**issue, "reason": f"多个讲座定位到同一位置{first_pos}"})
                    continue

            confirmed_issues.append(issue)

        elif issue_type in ("first_not_found", "last_not_found"):
            # 对not_found，检查是否是真实内容
            if not db_text or len(db_text) < 10:
                non_content_issues.append({**issue, "reason": "文本太短"})
                continue

            # 如果有PDF，尝试最终搜索
            if pdf_norm:
                norm = normalize(db_text)
                # 尝试搜索前5个字符
                if len(norm) >= 5:
                    pos = pdf_norm.find(norm[:5])
                    if pos >= 0:
                        non_content_issues.append({**issue, "reason": f"用短搜索找到(pos={pos})"})
                        continue

            confirmed_issues.append(issue)

    print(f"\n=== 最终确认结果 ===")
    print(f"非内容问题（假阳性）: {len(non_content_issues)}")
    print(f"确认真实问题: {len(confirmed_issues)}")

    # 按类型统计
    confirmed_by_type = Counter(i["type"] for i in confirmed_issues)
    print(f"\n确认真实问题按类型:")
    for t, c in confirmed_by_type.most_common():
        print(f"  {t}: {c}")

    # 按GA统计
    confirmed_by_ga = Counter(i["ga"] for i in confirmed_issues)
    print(f"\n确认真实问题最多的GA:")
    for ga, c in confirmed_by_ga.most_common(25):
        print(f"  {ga}: {c}")

    # 非内容问题统计
    non_content_reasons = Counter(i["reason"] for i in non_content_issues)
    print(f"\n非内容问题原因:")
    for r, c in non_content_reasons.most_common():
        print(f"  {r}: {c}")

    # 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "input": len(final_real),
                "non_content": len(non_content_issues),
                "confirmed": len(confirmed_issues),
                "confirmed_by_type": dict(confirmed_by_type),
                "confirmed_by_ga": dict(confirmed_by_ga.most_common(30)),
                "non_content_reasons": dict(non_content_reasons)
            },
            "confirmed_issues": confirmed_issues,
            "non_content_issues": non_content_issues
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 {OUTPUT_FILE}")

    # 显示确认的真实问题
    print(f"\n=== 确认的真实问题（全部） ===")
    for issue_type in ["overlap", "order_bad", "first_not_found", "last_not_found"]:
        items = [i for i in confirmed_issues if i["type"] == issue_type]
        if items:
            print(f"\n--- {issue_type} ({len(items)}个) ---")
            for i in items:
                print(f"  {i['ga']} #{i['lecture_id']} ({i.get('lecture_title', '')[:50]})")
                if i.get("db_text"):
                    print(f"    DB: {i['db_text'][:80]}")
                if i.get("first_pos") is not None:
                    print(f"    pos: first={i['first_pos']}, last={i['last_pos']}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
