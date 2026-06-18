"""P1真实问题深度过滤：识别更多假阳性模式，提取PDF原文确认真实问题。

假阳性模式：
1. 元数据首句："-YYYY-SE..." 或 "GA NN ..." 格式
2. 引用/注释末句：包含 [WA ...]、Seite ...、Auflage ... 等
3. 前言/序言：标题包含 VORREDE, VORWORT, VORBEMERKUNG 等（这些在PDF中可能出现在目录）
4. 短引用末句：日期+地点格式如 "Jena, d. 19. November 1794"
"""
import json
import re
import unicodedata
import psycopg2
from collections import Counter

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"
PDF_FILE = "/tmp/pdf_full_texts.json"
INPUT_FILE = "/tmp/p1_analysis.json"
OUTPUT_FILE = "/tmp/p1_real_issues.json"


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


def is_metadata_first_sentence(text):
    """检测元数据首句"""
    if not text:
        return False
    # -YYYY-SE... 格式
    if re.match(r"^-?\d{4}-?SE\d+", text.strip()):
        return True
    # GA NN ... 格式
    if re.match(r"^GA\s*\d+\s", text.strip(), re.IGNORECASE):
        return True
    # 纯数字或纯标点
    if len(text.strip()) < 5:
        return True
    return False


def is_citation_last_sentence(text):
    """检测引用/注释末句"""
    if not text:
        return False
    # [WA ...] 格式（Weimar Ausgabe引用）
    if re.search(r"\[WA\s", text):
        return True
    # Seite ... 格式
    if re.search(r"Seite\s+\w+", text) and len(text) < 80:
        return True
    # Auflage ... 格式
    if re.search(r"Auflage", text) and len(text) < 80:
        return True
    # 日期+地点格式（如 "Jena, d. 19. November 1794"）
    if re.search(r"^\w+,\s*d\.\s*\d{1,2}\.\s*\w+\s*\d{4}", text.strip()):
        return True
    # 纯日期
    if re.match(r"^\d{1,2}\.\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s*\d{4}\.?$", text.strip()):
        return True
    # 短引用（括号内）
    if text.strip().startswith("(") and text.strip().endswith(")") and len(text) < 80:
        return True
    return False


def is_preface_title(title):
    """检测前言/序言标题"""
    if not title:
        return False
    title_upper = title.upper()
    preface_patterns = [
        "VORREDE", "VORWORT", "VORBEMERKUNG", "EINLEITUNG",
        "ZU DIESER AUSGABE", "ZUR EINFÜHRUNG", "NACHWORT",
        "ANHANG", "HINWEISE", "INHALT", "REGISTER",
        "BIBLIOGRAPHIE", "LITERATURVERZEICHNIS"
    ]
    for p in preface_patterns:
        if p in title_upper:
            return True
    return False


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(PDF_FILE, "r", encoding="utf-8") as f:
        pdf_texts = json.load(f)

    real_issues = data["real_issues"]
    print(f"输入真实问题: {len(real_issues)}")

    # 进一步过滤
    false_positive_2 = []
    confirmed_real = []

    for issue in real_issues:
        issue_type = issue["type"]
        db_text = issue.get("db_text", "")
        title = issue.get("lecture_title", "")

        is_fp = False
        reason = ""

        # first_not_found: 检查元数据首句
        if issue_type == "first_not_found":
            if is_metadata_first_sentence(db_text):
                is_fp = True
                reason = "元数据首句"
            elif is_preface_title(title):
                is_fp = True
                reason = "前言/序言标题（可能在目录中出现）"

        # last_not_found: 检查引用末句
        elif issue_type == "last_not_found":
            if is_citation_last_sentence(db_text):
                is_fp = True
                reason = "引用/注释末句"
            elif is_preface_title(title):
                is_fp = True
                reason = "前言/序言标题"

        # overlap/order_bad: 检查前言标题
        elif issue_type in ("overlap", "order_bad"):
            if is_preface_title(title):
                is_fp = True
                reason = "前言/序言（定位可能在目录）"

        if is_fp:
            false_positive_2.append({**issue, "reason": reason})
        else:
            confirmed_real.append(issue)

    print(f"二次过滤假阳性: {len(false_positive_2)}")
    print(f"确认真实问题: {len(confirmed_real)}")

    # 按类型统计
    real_by_type = Counter(i["type"] for i in confirmed_real)
    print(f"\n确认真实问题按类型:")
    for t, c in real_by_type.most_common():
        print(f"  {t}: {c}")

    # 按GA统计
    real_by_ga = Counter(i["ga"] for i in confirmed_real)
    print(f"\n确认真实问题最多的GA (前20):")
    for ga, c in real_by_ga.most_common(20):
        print(f"  {ga}: {c}")

    # 对确认的真实问题，尝试用PDF全文重新定位
    print(f"\n=== 用PDF全文重新验证确认的真实问题 ===")
    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    reverified = []
    pdf_cache = {}

    for issue in confirmed_real:
        ga = issue["ga"]
        if ga not in pdf_cache:
            pdf_data = pdf_texts.get(ga)
            if pdf_data:
                pdf_text = pdf_data["full_text"] if isinstance(pdf_data, dict) else pdf_data
                pdf_cache[ga] = normalize(pdf_text)
            else:
                pdf_cache[ga] = None

        pdf_norm = pdf_cache[ga]
        if not pdf_norm:
            issue["reverify_status"] = "no_pdf"
            reverified.append(issue)
            continue

        db_text = issue.get("db_text", "")
        issue_type = issue["type"]

        if issue_type == "first_not_found" and db_text:
            # 尝试更短的搜索
            pos = find_position_progressive(db_text, pdf_norm)
            if pos >= 0:
                issue["reverify_status"] = "found_with_progressive"
                issue["reverify_pos"] = pos
            else:
                # 尝试搜索前10个字符
                norm = normalize(db_text)
                if len(norm) >= 10:
                    pos = pdf_norm.find(norm[:10])
                    if pos >= 0:
                        issue["reverify_status"] = "found_with_short"
                        issue["reverify_pos"] = pos
                    else:
                        issue["reverify_status"] = "still_not_found"
                else:
                    issue["reverify_status"] = "too_short"
        elif issue_type == "last_not_found" and db_text:
            pos = find_position_progressive(db_text, pdf_norm)
            if pos >= 0:
                issue["reverify_status"] = "found_with_progressive"
                issue["reverify_pos"] = pos
            else:
                norm = normalize(db_text)
                if len(norm) >= 10:
                    pos = pdf_norm.find(norm[:10])
                    if pos >= 0:
                        issue["reverify_status"] = "found_with_short"
                        issue["reverify_pos"] = pos
                    else:
                        issue["reverify_status"] = "still_not_found"
                else:
                    issue["reverify_status"] = "too_short"
        else:
            issue["reverify_status"] = "skipped"

        reverified.append(issue)

    # 统计重新验证结果
    reverify_counts = Counter(i.get("reverify_status") for i in reverified)
    print(f"\n重新验证结果:")
    for status, count in reverify_counts.most_common():
        print(f"  {status}: {count}")

    # 最终真实问题（still_not_found的）
    final_real = [i for i in reverified
                  if i.get("reverify_status") in ("still_not_found", "no_pdf", "too_short")
                  and i["type"] in ("first_not_found", "last_not_found")]
    # 加上overlap和order_bad（这些不需要重新验证）
    final_real += [i for i in reverified if i["type"] in ("overlap", "order_bad")]

    print(f"\n最终真实问题: {len(final_real)}")
    final_by_type = Counter(i["type"] for i in final_real)
    for t, c in final_by_type.most_common():
        print(f"  {t}: {c}")

    final_by_ga = Counter(i["ga"] for i in final_real)
    print(f"\n最终真实问题最多的GA (前20):")
    for ga, c in final_by_ga.most_common(20):
        print(f"  {ga}: {c}")

    # 保存
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "summary": {
                "input_real": len(real_issues),
                "false_positive_2": len(false_positive_2),
                "confirmed_real": len(confirmed_real),
                "final_real": len(final_real),
                "final_by_type": dict(final_by_type),
                "final_by_ga": dict(final_by_ga.most_common(30))
            },
            "final_real_issues": final_real,
            "false_positive_2": false_positive_2,
            "reverified": reverified
        }, f, ensure_ascii=False, indent=2)

    print(f"\n结果保存到 {OUTPUT_FILE}")

    # 显示最终真实问题示例
    print(f"\n=== 最终真实问题示例 ===")
    for issue_type in ["overlap", "order_bad", "first_not_found", "last_not_found"]:
        items = [i for i in final_real if i["type"] == issue_type]
        if items:
            print(f"\n--- {issue_type} ({len(items)}个) ---")
            for i in items[:8]:
                print(f"  {i['ga']} #{i['lecture_id']} ({i.get('lecture_title', '')[:40]})")
                if i.get("db_text"):
                    print(f"    DB文本: {i['db_text'][:80]}")
                if i.get("first_pos") is not None:
                    print(f"    位置: first={i['first_pos']}, last={i['last_pos']}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
