"""Analyze lecture boundary report - categorize issues by type and pattern."""
import json
from collections import Counter, defaultdict

with open("d:/00_dev/Codex/Steiner_Reader_Web/lecture_boundary_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

issues = report["issues"]

# Count by type
type_counts = Counter()
for issue in issues:
    type_counts[f"L{issue['layer']}-{issue['type']}"] += 1

print("=== ISSUE TYPE DISTRIBUTION ===")
for t, c in type_counts.most_common():
    print(f"  {t}: {c}")

# Layer 1 analysis
l1 = [i for i in issues if i["layer"] == 1]
l1_types = Counter(i["type"] for i in l1)
print(f"\n=== LAYER 1 ({len(l1)} issues) ===")
for t, c in l1_types.most_common():
    print(f"  {t}: {c}")

# Check if all L1 are wiki_fetch_error (316 = all GAs)
l1_errors = [i for i in l1 if i["type"] == "wiki_fetch_error"]
l1_mismatch = [i for i in l1 if i["type"] == "date_mismatch"]
print(f"  wiki_fetch_error: {len(l1_errors)}")
print(f"  date_mismatch: {len(l1_mismatch)}")
if l1_errors:
    print(f"  Sample error: {l1_errors[0]['description']}")

# Layer 2 analysis
l2 = [i for i in issues if i["layer"] == 2]
l2_types = Counter(i["type"] for i in l2)
print(f"\n=== LAYER 2 ({len(l2)} issues) ===")
for t, c in l2_types.most_common():
    print(f"  {t}: {c}")

# Analyze first_not_found - what do the DB texts look like?
l2_first_nf = [i for i in l2 if i["type"] == "first_not_found"]
print(f"\n  first_not_found samples (first 15):")
for i in l2_first_nf[:15]:
    db_text = i.get("db_text", "")[:80]
    print(f"    {i['ga']} #{i['lecture_id']}: {db_text}")

# Check for pattern: short DB texts (headings mistaken as lectures)
short_texts = [i for i in l2_first_nf if len(i.get("db_text", "")) < 30]
print(f"\n  first_not_found with very short DB text (<30 chars): {len(short_texts)}")
for i in short_texts[:10]:
    print(f"    {i['ga']} #{i['lecture_id']}: '{i.get('db_text', '')}'")

# Layer 3 analysis
l3 = [i for i in issues if i["layer"] == 3]
l3_types = Counter(i["type"] for i in l3)
print(f"\n=== LAYER 3 ({len(l3)} issues) ===")
for t, c in l3_types.most_common():
    print(f"  {t}: {c}")

# Check gap content patterns
l3_with_date = [i for i in l3 if i.get("has_date")]
l3_with_location = [i for i in l3 if i.get("has_location")]
l3_with_both = [i for i in l3 if i.get("has_date") and i.get("has_location")]
print(f"  Gaps with date pattern: {len(l3_with_date)}")
print(f"  Gaps with location pattern: {len(l3_with_location)}")
print(f"  Gaps with BOTH date+location (likely missing lecture): {len(l3_with_both)}")

if l3_with_both:
    print(f"\n  Gaps with date+location (likely missing lectures):")
    for i in l3_with_both[:20]:
        print(f"    {i['ga']} #{i['lecture_id']}: gap={i['gap_size']}, preview={i.get('gap_preview', '')[:80]}")
