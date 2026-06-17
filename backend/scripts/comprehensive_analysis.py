"""Comprehensive analysis of 2514 boundary issues: classify, prioritize, generate actionable fix list.

分类维度:
- L1 wiki_fetch_error: 全部P4（URL格式问题，不影响数据）
- L2 first_not_found: 按文本长度+内容模式分类（作者名/目录/章节标签/真实内容）
- L2 last_not_found: 同上+页码/引用模式
- L2 order_bad: 按位置差距分类（假阳性=定位到同一位置 vs 真实问题）
- L2 overlap: 同上
- L3 间隙: 按内容分类（含日期+地点/索引目录/作者信息/真实内容）

优先级:
- P0: 可能缺失讲座（间隙含日期+地点）
- P1: 真实首末句问题（长文本，非标题/标签）
- P2: 真实order_bad/overlap（位置差距大）
- P3: 假阳性（短文本、定位错误、索引间隙）
- P4: L1 wiki URL问题、L4无问题
"""
import json
import re
from collections import Counter, defaultdict

REPORT_PATH = "d:/00_dev/Codex/Steiner_Reader_Web/lecture_boundary_report.json"
OUTPUT_JSON = "d:/00_dev/Codex/Steiner_Reader_Web/comprehensive_analysis.json"
OUTPUT_TXT = "d:/00_dev/Codex/Steiner_Reader_Web/comprehensive_analysis.txt"

# 假阳性模式
AUTHOR_PATTERNS = re.compile(r"rudolf\s*steiner", re.IGNORECASE)
TOC_PATTERNS = re.compile(r"inhalts?verzeichnis|^inhalt$|^verzeichnis", re.IGNORECASE)
META_PATTERNS = re.compile(r"GA\d|SE\d|-\d{4}-|Auflage|Tausend|Herausgeber", re.IGNORECASE)
INDEX_PATTERNS = re.compile(r"namenregister|bibliographisch|register|literaturverzeichnis", re.IGNORECASE)
PAGE_REF_PATTERNS = re.compile(r"\[WA\s|Seite\s|\(S\.|\[S\.|,\s*\d{1,4}\)", re.IGNORECASE)


def classify_first_not_found(issue):
    """分类 first_not_found 问题"""
    db_text = issue.get("db_text", "")
    text_len = len(db_text)

    # 极短文本 (<20字符): 作者名、章节标签
    if text_len < 20:
        if AUTHOR_PATTERNS.search(db_text):
            return "P3-false_positive", "author_name", "作者名被当作首句"
        if TOC_PATTERNS.search(db_text):
            return "P3-false_positive", "toc_label", "目录标签被当作首句"
        if db_text.isupper() or db_text.replace(".", "").replace(" ", "").isupper():
            return "P3-false_positive", "section_label", "章节标签被当作首句"
        return "P3-false_positive", "short_text", f"短文本({text_len}字符): {db_text[:30]}"

    # 短文本 (20-50字符)
    if text_len < 50:
        if AUTHOR_PATTERNS.search(db_text):
            return "P3-false_positive", "author_name", "作者名被当作首句"
        if TOC_PATTERNS.search(db_text):
            return "P3-false_positive", "toc_label", "目录标签被当作首句"
        if META_PATTERNS.search(db_text):
            return "P3-false_positive", "metadata", "导入元数据被当作首句"
        if db_text.isupper():
            return "P3-false_positive", "section_title", "章节标题被当作首句"
        return "P2-needs_review", "short_content", f"短内容({text_len}字符): {db_text[:40]}"

    # 长文本 (≥50字符): 真实内容
    if META_PATTERNS.search(db_text):
        return "P3-false_positive", "metadata_long", "导入元数据被当作首句"
    return "P1-real_issue", "real_content", f"真实首句差异: {db_text[:60]}"


def classify_last_not_found(issue):
    """分类 last_not_found 问题"""
    db_text = issue.get("db_text", "")
    text_len = len(db_text)

    # 极短文本
    if text_len < 20:
        if PAGE_REF_PATTERNS.search(db_text):
            return "P3-false_positive", "page_ref", "页码/引用标记"
        if re.search(r"\d{4}\)|\d{1,2}\.\s*\d{1,2}\.", db_text):
            return "P3-false_positive", "date_ref", "日期标记"
        return "P3-false_positive", "short_text", f"短文本({text_len}字符): {db_text[:30]}"

    # 短文本
    if text_len < 50:
        if PAGE_REF_PATTERNS.search(db_text):
            return "P3-false_positive", "page_ref", "页码/引用标记"
        if META_PATTERNS.search(db_text):
            return "P3-false_positive", "metadata", "导入元数据"
        return "P2-needs_review", "short_content", f"短内容({text_len}字符): {db_text[:40]}"

    # 长文本
    if META_PATTERNS.search(db_text):
        return "P3-false_positive", "metadata_long", "导入元数据"
    if PAGE_REF_PATTERNS.search(db_text):
        return "P2-needs_review", "citation", "引用/参考文献"
    return "P1-real_issue", "real_content", f"真实末句差异: {db_text[:60]}"


def classify_order_bad(issue):
    """分类 order_bad 问题"""
    desc = issue.get("description", "")
    # 解析 "First pos (X) >= last pos (Y)"
    match = re.search(r"First pos \((\d+)\) >= last pos \((\d+)\)", desc)
    if match:
        first_pos = int(match.group(1))
        last_pos = int(match.group(2))
        diff = abs(first_pos - last_pos)

        if first_pos == last_pos:
            return "P3-false_positive", "same_position", "模糊匹配定位到同一位置"
        if diff < 100:
            return "P3-false_positive", "tiny_diff", f"位置差距极小({diff}字符)，模糊匹配误差"
        if diff < 1000:
            return "P2-needs_review", "small_diff", f"位置差距较小({diff}字符)"
        return "P1-real_issue", "large_diff", f"位置差距大({diff}字符)，边界严重错误"

    return "P2-needs_review", "unknown", "无法解析位置信息"


def classify_overlap(issue):
    """分类 overlap 问题"""
    desc = issue.get("description", "")
    # 解析 "Lecture starts at X but previous ended at Y"
    match = re.search(r"starts at (\d+) but previous ended at (\d+)", desc)
    if match:
        start_pos = int(match.group(1))
        prev_end = int(match.group(2))
        diff = prev_end - start_pos

        if start_pos == prev_end:
            return "P3-false_positive", "same_position", "模糊匹配定位到同一位置"
        if diff < 100:
            return "P3-false_positive", "tiny_diff", f"越界极小({diff}字符)，模糊匹配误差"
        if diff < 1000:
            return "P2-needs_review", "small_diff", f"越界较小({diff}字符)"
        return "P1-real_issue", "large_diff", f"越界大({diff}字符)，可能包含上一讲座结尾"

    return "P2-needs_review", "unknown", "无法解析位置信息"


def classify_gap(issue):
    """分类间隙问题"""
    gap_size = issue.get("gap_size", 0)
    preview = issue.get("gap_preview", "")
    has_date = issue.get("has_date", False)
    has_location = issue.get("has_location", False)

    # P0: 含日期+地点，高度怀疑缺失讲座
    if has_date and has_location:
        return "P0-missing_lecture", "date_location", f"间隙含日期+地点({gap_size}字符)，高度怀疑缺失讲座"

    # 假阳性：索引/目录/参考文献
    if INDEX_PATTERNS.search(preview):
        return "P3-false_positive", "index_content", "间隙是索引/参考文献内容"
    if TOC_PATTERNS.search(preview):
        return "P3-false_positive", "toc_content", "间隙是目录内容"
    if AUTHOR_PATTERNS.search(preview) and gap_size < 5000:
        return "P3-false_positive", "author_info", "间隙是作者信息页"

    # 间隙预览包含大量页码模式（如"204nachwort"）
    if re.search(r"\d{3}(nachwort|vorwort|hinweise|anhang)", preview, re.IGNORECASE):
        return "P3-false_positive", "toc_with_pages", "间隙是带页码的目录"

    # 章节标题页（短间隙+大写标题）
    if gap_size < 5000 and re.search(r"[A-Z]{4,}", preview[:100]):
        return "P3-false_positive", "section_title_page", "间隙是章节标题页"

    # 真实内容间隙
    if gap_size > 20000:
        return "P1-real_issue", "large_content_gap", f"大间隙({gap_size}字符)，可能遗漏内容"
    if gap_size > 5000:
        return "P2-needs_review", "medium_gap", f"中等间隙({gap_size}字符)，需要检查"
    return "P3-false_positive", "small_gap", f"小间隙({gap_size}字符)，可能是正常间隔"


def main():
    with open(REPORT_PATH, "r", encoding="utf-8") as f:
        report = json.load(f)

    issues = report["issues"]
    print(f"加载 {len(issues)} 个问题")

    # 分类所有问题
    classified = []
    for issue in issues:
        layer = issue.get("layer")
        issue_type = issue.get("type")

        if layer == 1:
            priority, category, reason = "P4-skip", "wiki_url_error", "L1 wiki URL全部404，不影响数据完整性"
        elif layer == 4:
            priority, category, reason = "P4-skip", "no_issue", "L4 heading验证无问题"
        elif issue_type == "first_not_found":
            priority, category, reason = classify_first_not_found(issue)
        elif issue_type == "last_not_found":
            priority, category, reason = classify_last_not_found(issue)
        elif issue_type == "order_bad":
            priority, category, reason = classify_order_bad(issue)
        elif issue_type == "overlap":
            priority, category, reason = classify_overlap(issue)
        elif issue_type in ("very_large_gap", "large_gap"):
            priority, category, reason = classify_gap(issue)
        else:
            priority, category, reason = "P2-needs_review", "unknown_type", f"未知问题类型: {issue_type}"

        classified.append({
            **issue,
            "priority": priority,
            "category": category,
            "reason": reason
        })

    # 统计
    priority_counts = Counter(c["priority"] for c in classified)
    category_counts = Counter(c["category"] for c in classified)

    # 按优先级分组
    by_priority = defaultdict(list)
    for c in classified:
        by_priority[c["priority"]].append(c)

    # 按GA统计真实问题
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
        f.write("讲座边界验证 - 全面分析报告\n")
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

        # P0: 可能缺失讲座
        f.write("=" * 70 + "\n")
        f.write(f"P0 - 可能缺失讲座 ({len(by_priority['P0-missing_lecture'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【立即人工审查】间隙含日期+地点模式，高度怀疑遗漏讲座\n\n")
        for c in by_priority["P0-missing_lecture"]:
            f.write(f"  {c['ga']} #{c.get('lecture_id', '?')} ({c.get('lecture_title', '')[:50]})\n")
            f.write(f"    间隙大小: {c.get('gap_size', '?')} 字符\n")
            f.write(f"    预览: {c.get('gap_preview', '')[:200]}\n")
            f.write(f"    建议: 检查PDF对应页面，确认是否缺失讲座\n\n")

        # P1: 真实问题
        f.write("=" * 70 + "\n")
        f.write(f"P1 - 真实问题 ({len(by_priority['P1-real_issue'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【高优先级修复】真实的首末句差异、边界严重错误、大间隙\n\n")

        # 按类型子分组
        p1_by_type = defaultdict(list)
        for c in by_priority["P1-real_issue"]:
            p1_by_type[c["type"]].append(c)

        for issue_type, items in p1_by_type.items():
            f.write(f"--- {issue_type} ({len(items)}个) ---\n")
            for c in items[:30]:  # 每类最多显示30个
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')} ({c.get('lecture_title', '')[:40]})\n")
                f.write(f"    分类: {c['category']}\n")
                f.write(f"    原因: {c['reason']}\n")
                if c.get("db_text"):
                    f.write(f"    DB文本: {c['db_text'][:80]}\n")
                f.write("\n")
            if len(items) > 30:
                f.write(f"  ... 还有 {len(items) - 30} 个\n\n")

        # P2: 需要审查
        f.write("=" * 70 + "\n")
        f.write(f"P2 - 需要人工审查 ({len(by_priority['P2-needs_review'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【中优先级】位置差距较小、短内容、引用等，需人工确认\n\n")

        p2_by_type = defaultdict(list)
        for c in by_priority["P2-needs_review"]:
            p2_by_type[c["type"]].append(c)

        for issue_type, items in p2_by_type.items():
            f.write(f"--- {issue_type} ({len(items)}个) ---\n")
            for c in items[:15]:
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')}: {c['reason']}\n")
            if len(items) > 15:
                f.write(f"  ... 还有 {len(items) - 15} 个\n")
            f.write("\n")

        # P3: 假阳性
        f.write("=" * 70 + "\n")
        f.write(f"P3 - 假阳性 ({len(by_priority['P3-false_positive'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【无需修复】短文本、模糊匹配误差、索引/目录内容\n\n")

        p3_by_category = defaultdict(list)
        for c in by_priority["P3-false_positive"]:
            p3_by_category[c["category"]].append(c)

        for cat, items in sorted(p3_by_category.items(), key=lambda x: -len(x[1])):
            f.write(f"--- {cat} ({len(items)}个) ---\n")
            # 显示前5个示例
            for c in items[:5]:
                f.write(f"  {c['ga']} #{c.get('lecture_id', '?')}: {c['reason']}\n")
            if len(items) > 5:
                f.write(f"  ... 还有 {len(items) - 5} 个\n")
            f.write("\n")

        # P4: 跳过
        f.write("=" * 70 + "\n")
        f.write(f"P4 - 跳过 ({len(by_priority['P4-skip'])}个)\n")
        f.write("=" * 70 + "\n")
        f.write("【无需处理】L1 wiki URL全部404（需单独修复URL格式）、L4无问题\n\n")

        # 真实问题最多的GA
        f.write("=" * 70 + "\n")
        f.write("真实问题最多的GA (P0+P1)\n")
        f.write("=" * 70 + "\n")
        for ga, count in sorted(real_issues_by_ga.items(), key=lambda x: -x[1])[:20]:
            f.write(f"  {ga}: {count}个真实问题\n")

        # 修复建议总结
        f.write("\n" + "=" * 70 + "\n")
        f.write("修复建议总结\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"1. 【立即处理】P0 - {len(by_priority['P0-missing_lecture'])}个可能缺失讲座\n")
        f.write("   行动: 人工检查GA024, GA262, GA269, GA284的PDF对应页面\n")
        f.write("   如果确认缺失，从PDF重新导入对应讲座\n\n")

        f.write(f"2. 【高优先级】P1 - {len(by_priority['P1-real_issue'])}个真实问题\n")
        f.write("   行动: 逐个检查首末句差异，对比DB与PDF原文\n")
        f.write("   如果是OCR差异，更新DB文本；如果是截断，重新导入\n\n")

        f.write(f"3. 【中优先级】P2 - {len(by_priority['P2-needs_review'])}个需审查\n")
        f.write("   行动: 抽样检查，确认是否为真实问题\n\n")

        f.write(f"4. 【无需处理】P3 - {len(by_priority['P3-false_positive'])}个假阳性\n")
        f.write("   原因: 短文本被当作首句、模糊匹配定位误差、索引/目录内容\n")
        f.write("   行动: 改进验证脚本，过滤这些模式\n\n")

        f.write(f"5. 【单独处理】P4 - {len(by_priority['P4-skip'])}个跳过\n")
        f.write("   行动: 调查steiner.wiki正确URL格式，重新运行L1\n")

    print(f"文本报告: {OUTPUT_TXT}")

    # 打印摘要
    print("\n=== 分析摘要 ===")
    print(f"总问题数: {len(classified)}")
    print("\n优先级分布:")
    for p in ["P0-missing_lecture", "P1-real_issue", "P2-needs_review", "P3-false_positive", "P4-skip"]:
        count = priority_counts.get(p, 0)
        print(f"  {p}: {count}")
    print("\n分类分布 (前10):")
    for cat, count in category_counts.most_common(10):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
