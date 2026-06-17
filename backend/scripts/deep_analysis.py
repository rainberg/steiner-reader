"""Deep analysis of key issues: order_bad, real first_not_found, and missing lecture gaps."""
import json
from collections import Counter

with open("d:/00_dev/Codex/Steiner_Reader_Web/lecture_boundary_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

issues = report["issues"]

# 1. Analyze order_bad - are these real or matching artifacts?
order_bad = [i for i in issues if i["type"] == "order_bad"]
print(f"=== ORDER_BAD ANALYSIS ({len(order_bad)} issues) ===")
print(f"Sample order_bad issues:")
for i in order_bad[:10]:
    print(f"  {i['ga']} #{i['lecture_id']}: {i['description']}")

# 2. first_not_found with long DB text (real content, not titles)
first_nf = [i for i in issues if i["type"] == "first_not_found"]
real_first_nf = [i for i in first_nf if len(i.get("db_text", "")) >= 50]
short_first_nf = [i for i in first_nf if len(i.get("db_text", "")) < 50]
print(f"\n=== FIRST_NOT_FOUND ANALYSIS ({len(first_nf)} total) ===")
print(f"  Short DB text (<50 chars, likely titles/labels): {len(short_first_nf)}")
print(f"  Long DB text (>=50 chars, real content): {len(real_first_nf)}")
print(f"\n  Real first_not_found (long DB text, first 20):")
for i in real_first_nf[:20]:
    print(f"    {i['ga']} #{i['lecture_id']}: {i.get('db_text', '')[:100]}")

# 3. last_not_found with long DB text
last_nf = [i for i in issues if i["type"] == "last_not_found"]
real_last_nf = [i for i in last_nf if len(i.get("db_text", "")) >= 50]
print(f"\n=== LAST_NOT_FOUND ANALYSIS ({len(last_nf)} total) ===")
print(f"  Long DB text (>=50 chars, real content): {len(real_last_nf)}")
print(f"\n  Real last_not_found (first 15):")
for i in real_last_nf[:15]:
    print(f"    {i['ga']} #{i['lecture_id']}: {i.get('db_text', '')[:100]}")

# 4. The 10 potential missing lectures (gaps with date+location)
missing_likely = [i for i in issues if i.get("has_date") and i.get("has_location")]
print(f"\n=== POTENTIAL MISSING LECTURES ({len(missing_likely)} gaps with date+location) ===")
for i in missing_likely:
    print(f"\n  {i['ga']} #{i['lecture_id']} ({i.get('lecture_title', '')[:50]})")
    print(f"    Gap size: {i['gap_size']} chars")
    print(f"    Preview: {i.get('gap_preview', '')[:150]}")

# 5. overlap analysis
overlap = [i for i in issues if i["type"] == "overlap"]
print(f"\n=== OVERLAP ANALYSIS ({len(overlap)} issues) ===")
# Group by GA
overlap_by_ga = Counter(i["ga"] for i in overlap)
print(f"  Top GAs with overlap issues:")
for ga, c in overlap_by_ga.most_common(10):
    print(f"    {ga}: {c} overlaps")
