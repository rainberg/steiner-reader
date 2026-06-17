"""Comprehensive analysis v3: 进一步细化假阳性检测。

关键改进:
1. 已识别为模糊匹配错误的GA，其large_content_gap也归为假阳性
2. 识别附录类讲座标题（HINWEISE/ANHANG/PERSONENREGISTER/NAMENREGISTER等）
3. 识别导入元数据首句（如"GA 92 Die okkulten..."）
4. 识别表格/列表内容末句
"""
import json
import re
from collections import Counter, defaultdict

REPORT_PATH = "d:/00_dev/Codex/Steiner_Reader_Web/lecture_boundary_report.json"
OUTPUT_JSON = "d:/00_dev/Codex/Steiner_Reader_Web/comprehensive_analysis_v3.json"
OUTPUT_TXT = "d:/00_dev/Codex/Steiner_Reader_Web/comprehensive_analysis_v3.txt"

AUTHOR_PATTERNS = re.compile(r"rudolf\s*steiner", re.IGNORECASE)
TOC_PATTERNS = re.compile(r"inhalts?verzeichnis|^inhalt$|^verzeichnis", re.IGNORECASE)
META_PATTERNS = re.compile(r"GA\d|SE\d|-\d{4}-|Auflage|Tausend|Herausgeber|Copyright|Nachlassverwaltung", re.IGNORECASE)
INDEX_PATTERNS = re.compile(r"namenregister|bibliographisch|register|literaturverzeichnis|personenregister", re.IGNORECASE)
PAGE_REF_PATTERNS = re.compile(r"\[WA\s|Seite\s|\(S\.|\[S\.|,\s*\d{1,4}\)", re.IGNORECASE)

# 附录类讲座标题模式
APPENDIX_TITLE_PATTERNS = re.compile(
    r"^(HINWEISE|ANHANG|PERSONENREGISTER|NAMENREGISTER|KORRIGENDA|"
    r"REISEVERZEICHNIS|BIBLIOGRAPHISCH|ALPHABETISCHES|"
    r"ANSPRACHE|FRAGENBEANTWORTUNG|ERGÄNZENDE|SCHLUSSWORT|"
    r"VORWORT|VORREDE|NACHSCHRIFT|NACHWORT|BEMERKUNGEN|"
    r"ZUR EINFÜHRUNG|ÜBER.*VORTRAG|EXTRA-ANHANG)",
    re.IGNORECASE
)

# 导入元数据首句模式（如"GA 92 Die okkulten Wahrheiten alter Mythen und Sagen"）
IMPORT_META_FIRST = re.compile(r"^GA\s*\d+\s+Die\s", re.IGNORECASE)

# 表格/列表内容模式
TABLE_PATTERNS = re.compile(
    r"(Mensch\s+Löwe|Gott\s+physisch|Oberer\s+Devachan|"
    r"\d+\s+\w+\s+\d+\s+\w+\s+\d+|"
    r"Erstens|Zweitens|Drittens)",
    re.IGNORECASE
)


def parse_positions(desc):
    m = re.search(r"First pos \((\d+)\) >= last pos \((\d+)\)", desc)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.search(r"starts at (\d+) but previous ended at (\d+)", desc)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None, None


def is_appendix_lecture(issue):
    """判断是否是附录类讲座"""
    title = issue.get("lecture_title", "")
    return bool(APPENDIX_TITLE_PATTERNS.search(title))


def classify_first_not_found(issue):
    db_text = issue.get("db_text", "")
    text_len = len(db_text)

    # 导入元数据首句（如"GA 92 Die okkulten..."）
    if IMPORT_META_FIRST.search(db_text):
        return "P3-false_positive", "import_metadata", "导入元数据被当作首句"

    if text_len < 20:
        if AUTHOR_PATTERNS.search(db_text):
            return "P3-false_positive", "author_name", "作者名被当作首句"
        if TOC_PATTERNS.search(db_text):
            return "P3-false_positive", "toc_label", "目录标签被当作首句"
        if db_text.isupper() or db_text.replace(".", "").replace(" ", "").isupper():
            return "P3-false_positive", "section_label", "章节标签被当作首句"
        return "P3-false_positive", "short_text", f"短文本({text_len}字符)"

    if text_len < 50:
        if AUTHOR_PATTERNS.search(db_text):
            return "P3-false_positive", "author_name", "作者名被当作首句"
        if TOC_PATTERNS.search(db_text):
            return "P3-false_positive", "toc_label", "目录标签被当作首句"
        if META_PATTERNS.search(db_text):
            return "P3-false_positive", "metadata", "导入元数据被当作首句"
        if db_text.isupper():
            return "P3-false_positive", "section_title", "章节标题被当作首句"
        return "P2-needs_review", "short_content", f"短内容({text_len}字符)"

    if META_PATTERNS.search(db_text):
        return "P3-false_positive", "metadata_long", "导入元数据被当作首句"

    # 附录类讲座的首句找不到，通常是附录格式与正文不同
    if is_appendix_lecture(issue):
        return "P2-needs_review", "appendix_content", "附录类讲座首句差异（格式不同）"

    return "P1-real_issue", "real_content", "真实首句差异"


def classify_last_not_found(issue):
    db_text = issue.get("db_text", "")
    text_len = len(db_text)

    if text_len < 20:
        if PAGE_REF_PATTERNS.search(db_text):
            return "P3-false_positive", "page_ref", "页码/引用标记"
        if re.search(r"\d{4}\)|\d{1,2}\.\s*\d{1,2}\.", db_text):
            return "P3-false_positive", "date_ref", "日期标记"
        return "P3-false_positive", "short_text", f"短文本({text_len}字符)"

    if text_len < 50:
        if PAGE_REF_PATTERNS.search(db_text):
            return "P3-false_positive", "page_ref", "页码/引用标记"
        if META_PATTERNS.search(db_text):
            return "P3-false_positive", "metadata", "导入元数据"
        return "P2-needs_review", "short_content", f"短内容({text_len}字符)"

    if META_PATTERNS.search(db_text):
        return "P3-false_positive", "metadata_long", "导入元数据"

    # 表格/列表内容
    if TABLE_PATTERNS.search(db_text):
        return "P3-false_positive", "table_content", "表格/列表内容（模糊匹配难以定位）"

    # 人名索引模式（如"Beethoven, Ludwig van 225, 226 Böcklin..."）
    if re.search(r"\w+,\s+\w+\s+\d+,\s*\d+\s+\w+,\s+\w+\s+\d+", db_text):
        return "P3-false_positive", "name_index", "人名索引内容"

    if PAGE_REF_PATTERNS.search(db_text):
        return "P2-needs_review", "citation", "引用/参考文献"

    # 附录类讲座
    if is_appendix_lecture(issue):
        return "P2-needs_review", "appendix_content", "附录类讲座末句差异"

    return "P1-real_issue", "real_content", "真实末句差异"


def detect_matching_error_pattern(ga_issues):
    """检测模糊匹配定位错误模式"""
    overlap_positions = []
    order_bad_positions = []

    for issue in ga_issues:
        if issue["type"] == "overlap":
            start, _ = parse_positions(issue.get("description", ""))
            if start is not None:
                overlap_positions.append(start)
        elif issue["type"] == "order_bad":
            first_pos, _ = parse_positions(issue.get("description", ""))
            if first_pos is not None:
                order_bad_positions.append(first_pos)

    if len(overlap_positions) >= 5:
        early_count = sum(1 for p in overlap_positions if p < 5000)
        if early_count >= len(overlap_positions) * 0.7:
            return True, "overlap_early_position"

    if len(order_bad_positions) >= 5:
        if len(set(order_bad_positions)) <= 3:
            return True, "order_bad_same_position"
        early_count = sum(1 for p in order_bad_positions if p < 5000)
        if early_count >= len(order_bad_positions) * 0.7:
            return True, "order_bad_early_position"

    return False, None


def classify_order_bad(issue, is_matching_error):
    if is_matching_error:
        return "P3-false_positive", "matching_error", "模糊匹配定位错误"

    first_pos, last_pos = parse_positions(issue.get("description", ""))
    if first_pos is not None and last_pos is not None:
        diff = abs(first_pos - last_pos)
        if first_pos == last_pos:
            return "P3-false_positive", "same_position", "定位到同一位置"
        if diff < 100:
            return "P3-false_positive", "tiny_diff", f"差距极小({diff}字符)"
        if diff < 1000:
            return "P2-needs_review", "small_diff", f"差距较小({diff}字符)"
        return "P1-real_issue", "large_diff", f"差距大({diff}字符)"

    return "P2-needs_review", "unknown", "无法解析位置"


def classify_overlap(issue, is_matching_error):
    if is_matching_error:
        return "P3-false_positive", "matching_error", "模糊匹配定位错误"

    start_pos, prev_end = parse_positions(issue.get("description", ""))
    if start_pos is not None and prev_end is not None:
        diff = prev_end - start_pos
        if start_pos == prev_end:
            return "P3-false_positive", "same_position", "定位到同一位置"
        if diff < 100:
            return "P3-false_positive", "tiny_diff", f"越界极小({diff}字符)"
        if diff < 1000:
            return "P2-needs_review", "small_diff", f"越界较小({diff}字符)"

        # 附录类讲座的越界通常是定位错误
        if is_appendix_lecture(issue):
            return "P3-false_positive", "appendix_matching_error", "附录类讲座定位错误"

        return "P1-real_issue", "large_diff", f"越界大({diff}字符)"

    return "P2-needs_review", "unknown", "无法解析位置"


def classify_gap(issue, ga_is_matching_error):
    gap_size = issue.get("gap_size", 0)
    preview = issue.get("gap_preview", "")
    has_date = issue.get("has_date", False)
    has_location = issue.get("has_location", False)

    # P0: 含日期+地点
    if has_date and has_location:
        return "P0-missing_lecture", "date_location", f"间隙含日期+地点({gap_size}字符)"

    # 间隙>100000字符：定位错误
    if gap_size > 100000:
        return "P3-false_positive", "huge_gap_matching_error", f"间隙异常大({gap_size}字符)"

    # 如果GA已被识别为模糊匹配错误，间隙也是定位错误
    if ga_is_matching_error:
        return "P3-false_positive", "matching_error_gap", f"模糊匹配错误导致的间隙({gap_size}字符)"

    # 假阳性：索引/目录
    if INDEX_PATTERNS.search(preview):
        return "P3-false_positive", "index_content", "间隙是索引/参考文献"
    if TOC_PATTERNS.search(preview):
        return "P3-false_positive", "toc_content", "间隙是目录内容"
    if AUTHOR_PATTERNS.search(preview) and gap_size < 5000:
        return "P3-false_positive", "author_info", "间隙是作者信息页"

    if re.search(r"\d{3}(nachwort|vorwort|hinweise|anhang)", preview, re.IGNORECASE):
        return "P3-false_positive", "toc_with_pages", "间隙是带页码的目录"

    if gap_size < 5000 and re.search(r"[A-Z]{4,}", preview[:100]):
        return "P3-false_positive", "section_title_page", "间隙是章节标题页"

    # 真实内容间隙
    if gap_size > 20000:
        return "P1-real_issue", "large_content_gap", f"大间隙({gap_size}字符)"
    if gap_size > 5000:
        return "P2-needs_review", "medium_gap", f"中等间隙({gap_size}字符)"
    return "P3-false_positive", "small_gap", f"小间隙({gap_size}字符)"


def main():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report = json.load(f)

    issues = report["issues"]
    print(f"加载 {len(issues)} 个问题")

    # 按GA分组，检测模糊匹配定位错误
    issues_by_ga = defaultdict(list)
    for issue in issues:
        issues_by_ga[issue["ga"]].append(issue)

    ga_matching_error = {}
    for ga, ga_issues in issues_by_ga.items():
        is_error, pattern = detect_matching_error_pattern(ga_issues)
        if is_error:
            ga_matching_error[ga] = (is_error, pattern)

    print(f"检测到 {len(ga_matching_error)} 个GA有模糊匹配定位错误模式")

    # 分类所有问题
    classified = []
    for issue in issues:
        layer = issue.get("layer")
        issue_type = issue.get("type")
        ga = issue.get("ga", "")

        if layer == 1:
            priority, category, reason = "P4-skip", "wiki_url_error", "L1 wiki URL全部404"
        elif layer == 4:
            priority, category, reason = "P4-skip", "no_issue", "L4无问题"
        elif issue_type == "first_not_found":
            priority, category, reason = classify_first_not_found(issue)
        elif issue_type == "last_not_found":
            priority, category, reason = classify_last_not_found(issue)
        elif issue_type == "order_bad":
            is_me = ga in ga_matching_error
            priority, category, reason = classify_order_bad(issue, is_me)
        elif issue_type == "overlap":
            is_me = ga in ga_matching_error
            priority, category, reason = classify_overlap(issue, is_me)
        elif issue_type in ("very_large_gap", "large_gap"):
            ga_is_me = ga in ga_matching_error
            priority, category, reason = classify_gap(issue, ga_is_me)
        else:
            priority, category, reason = "P2-needs_review", "unknown_type", f"未知类型: {issue_type}"

        classified.append({
            **issue,
            "priority": priority,
            "category": category,
            "reason": reason
        })

    # 统计
    priority_counts = Counter(c["priority"] for c in classified)
    category_counts = Counter(c["category"] for c in classified)

    by_priority = defaultdict(list)
    for c in classified:
        by_priority[c["priority"]].append(c)

    real_issues_by_ga = defaultdict(int)
    for c in classified:
        if c["priority"] in ("P0-missing_lecture", "P1-real_issue"):
            real_issues_by_ga[c["ga"]] += 1

    # 生成JSON报告
    output = {
        "summary": {
            "total_issues": len(classified),
            "priority_distribution": dict(priority_counts),
            "category_distribution": dict(category_counts),
            "matching_error_gas": list(ga_matching_error.keys()),
            "real_issues_by_ga": dict(sorted(real_issues_by_ga.items(), key=lambda x: -x[1])[:30]),
        },
        "p0_missing_lectures": by_priority["P0-missing_lecture"],
        "p1_real_issues": by_priority["P1-real_issue"],
        "p2_needs_review": by_priority["P2-needs_review"],
        "p3_false_positives": by_priority["P3-false_positive"],
        "p4_skip": by_priority["P4-skip"],
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"JSON报告: {OUTPUT_JSON}")

    # 生成人类可读报告
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write("=" * 70 + "\n")
        f.write("讲座边界验证 - 全面分析报告 v3 (最终版)\n")
        f.write("=" * 70 + "\n\n")

        f.write("=== 总览 ===\n")
        f.write(f"总问题数: {len(classified)}\n\n")

        f.write("=== 优先级分布 ===\n")
        for p in ["P0-missing_lecture", "P1-real_issue", "P2-needs_review", "P3-false_positive", "P4-skip"]:
            count = priority_counts.get(p, 0)
            f.write(f"  {p}: {count}\n")
        f.write("\n")

        f.write("=== 分类分布 ===\n")
        for cat, count in category_counts.most_common():
            f.write(f"  {cat}: {count}\n")
        f.write("\n")

        f.write(f"=== 模糊匹配定位错误的GA ({len(ga_matching_error)}个) ===\n")
        for ga, (_, pattern) in ga_matching_error.items():
            f.write(f"  {ga}: {pattern}\n")
        f.write("\n")

        # P0
        f.write("=" * 70 + "\n")
        f.write(f"P0 - 可能缺失讲座 ({len(by_priority['P0-missing_lecture'])}个) ★最高优先级\n")
        f.write("=" * 70 + "\n")
        f.write("【立即人工审查】间隙含日期+地点模式，高度怀疑遗漏讲座\n\n")
        for c in by_priority["P0-missing_lecture"]:
            f.write(f"  {c['ga']} #{c.get('lecture_id', '?')} ({c.get('lecture_title', '')[:50]})\n")
            f.write(f"    间隙: {c.get('gap_size', '?')} 字符\n")
            f.write(f"    预览: {c.get('gap_preview', '')[:200]}\n")
            f.write(f"    建议: 检查PDF对应页面，确认是否缺失讲座\n\n")

        # P1
        f.write("=" * 70 + "\n")
        f.write(f"P1 - 真实问题 ({len(by_priority['P1-real_issue'])}个) ★高优先级\n")
        f.write("=" * 70 + "\n")
        f.write("【需要修复】真实的首末句差异、边界严重错误、大间隙\n\n")

        p1_by_type = defaultdict(list)
        for c in by_priority["P1-real_issue"]:
            p1_by_type[c["type"]].append(c)

        for issue_type, items in p1_by_type.items():
            f.write(f"--- {issue_type} ({len(items)}个) ---\n")
            for c in items[:50]:
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')} ({c.get('lecture_title', '')[:40]})\n")
                f.write(f"    分类: {c['category']} | {c['reason']}\n")
                if c.get("db_text"):
                    f.write(f"    DB文本: {c['db_text'][:80]}\n")
                f.write("\n")
            if len(items) > 50:
                f.write(f"  ... 还有 {len(items) - 50} 个\n\n")

        # P2
        f.write("=" * 70 + "\n")
        f.write(f"P2 - 需要人工审查 ({len(by_priority['P2-needs_review'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【中优先级】附录内容、短内容、引用等，需人工确认\n\n")

        p2_by_type = defaultdict(list)
        for c in by_priority["P2-needs_review"]:
            p2_by_type[c["type"]].append(c)

        for issue_type, items in p2_by_type.items():
            f.write(f"--- {issue_type} ({len(items)}个) ---\n")
            for c in items[:20]:
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')}: {c['reason']}\n")
            if len(items) > 20:
                f.write(f"  ... 还有 {len(items) - 20} 个\n")
            f.write("\n")

        # P3
        f.write("=" * 70 + "\n")
        f.write(f"P3 - 假阳性 ({len(by_priority['P3-false_positive'])}个) 无需修复\n")
        f.write("=" * 70 + "\n\n")

        p3_by_category = defaultdict(list)
        for c in by_priority["P3-false_positive"]:
            p3_by_category[c["category"]].append(c)

        for cat, items in sorted(p3_by_category.items(), key=lambda x: -len(x[1])):
            f.write(f"--- {cat} ({len(items)}个) ---\n")
            for c in items[:3]:
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')}: {c['reason']}\n")
            if len(items) > 3:
                f.write(f"  ... 还有 {len(items) - 3} 个\n")
            f.write("\n")

        # P4
        f.write("=" * 70 + "\n")
        f.write(f"P4 - 跳过 ({len(by_priority['P4-skip'])}个)\n")
        f.write("=" * 70 + "\n\n")

        # 真实问题最多的GA
        f.write("=" * 70 + "\n")
        f.write("真实问题最多的GA (P0+P1)\n")
        f.write("=" * 70 + "\n")
        for ga, count in sorted(real_issues_by_ga.items(), key=lambda x: -x[1])[:25]:
            f.write(f"  {ga}: {count}个\n")

        # 最终结论
        f.write("\n" + "=" * 70 + "\n")
        f.write("最终结论与修复建议\n")
        f.write("=" * 70 + "\n\n")

        p0_count = len(by_priority["P0-missing_lecture"])
        p1_count = len(by_priority["P1-real_issue"])
        p2_count = len(by_priority["P2-needs_review"])
        p3_count = len(by_priority["P3-false_positive"])
        p4_count = len(by_priority["P4-skip"])

        f.write(f"原始问题: 2514个\n")
        f.write(f"经过细致分类后:\n")
        f.write(f"  - P0 可能缺失讲座: {p0_count}个 (需立即处理)\n")
        f.write(f"  - P1 真实问题: {p1_count}个 (需修复)\n")
        f.write(f"  - P2 需审查: {p2_count}个 (需人工确认)\n")
        f.write(f"  - P3 假阳性: {p3_count}个 (无需处理)\n")
        f.write(f"  - P4 跳过: {p4_count}个 (L1 wiki URL问题)\n\n")

        f.write(f"假阳性率: {p3_count}/{p0_count+p1_count+p2_count+p3_count} = {p3_count*100//(p0_count+p1_count+p2_count+p3_count)}%\n\n")

        f.write("修复优先级:\n\n")

        f.write(f"1. 【P0 - 立即处理】{p0_count}个可能缺失讲座\n")
        f.write("   涉及GA: " + ", ".join(sorted(set(c['ga'] for c in by_priority['P0-missing_lecture']))) + "\n")
        f.write("   行动: 人工检查PDF对应页面，确认是否缺失讲座\n")
        f.write("   如果确认缺失，从PDF重新导入对应讲座\n\n")

        f.write(f"2. 【P1 - 高优先级】{p1_count}个真实问题\n")
        f.write("   行动: 逐个检查首末句差异，对比DB与PDF原文\n")
        f.write("   如果是OCR差异，更新DB文本；如果是截断，重新导入\n\n")

        f.write(f"3. 【P2 - 中优先级】{p2_count}个需审查\n")
        f.write("   行动: 抽样检查，确认是否为真实问题\n\n")

        f.write(f"4. 【P3 - 无需处理】{p3_count}个假阳性\n")
        f.write(f"   原因: {len(ga_matching_error)}个GA的模糊匹配定位错误、附录/索引内容、短文本误判\n")
        f.write("   行动: 改进验证脚本的匹配策略（使用更长片段、排除附录类讲座）\n\n")

        f.write(f"5. 【P4 - 单独处理】{p4_count}个跳过\n")
        f.write("   行动: 调查steiner.wiki正确URL格式，重新运行L1\n\n")

        f.write("验证脚本改进建议:\n")
        f.write("   - 对附录类讲座（HINWEISE/ANHANG/PERSONENREGISTER等）单独处理或排除\n")
        f.write("   - 对导入元数据首句（如'GA 92 Die okkulten...'）过滤\n")
        f.write("   - 对表格/列表内容使用更宽松的匹配策略\n")
        f.write("   - 对模糊匹配定位错误检测：如果同一GA多个讲座定位到同一位置，标记为定位错误\n")
        f.write("   - 对间隙>100000字符的，标记为定位错误而非真实缺失\n")

    print(f"文本报告: {OUTPUT_TXT}")

    # 打印摘要
    print("\n=== 分析摘要 v3 (最终) ===")
    print(f"总问题数: {len(classified)}")
    print(f"模糊匹配定位错误的GA: {len(ga_matching_error)}个")
    print("\n优先级分布:")
    for p in ["P0-missing_lecture", "P1-real_issue", "P2-needs_review", "P3-false_positive", "P4-skip"]:
        count = priority_counts.get(p, 0)
        print(f"  {p}: {count}")
    print("\n分类分布 (前15):")
    for cat, count in category_counts.most_common(15):
        print(f"  {cat}: {count}")

    p0_count = len(by_priority["P0-missing_lecture"])
    p1_count = len(by_priority["P1-real_issue"])
    p2_count = len(by_priority["P2-needs_review"])
    p3_count = len(by_priority["P3-false_positive"])
    total_real = p0_count + p1_count + p2_count + p3_count
    if total_real > 0:
        print(f"\n假阳性率: {p3_count}/{total_real} = {p3_count*100//total_real}%")


if __name__ == "__main__":
    main()
