"""Pass 2: More aggressive fuzzy matching for remaining unmatched GA083 sentences.

Handles:
1. Hyphenation differences (ur-sprünglich vs ursprünglich)
2. Multi-sentence merge: current sentence = multiple old sentences concatenated
3. Prefix matching for long sentences
"""
import psycopg2, re

def norm(text):
    if not text:
        return ""
    t = text.replace("\xad", "").replace("\n", " ").replace("\r", " ")
    return re.sub(r"\s+", " ", t).strip()

def norm_loose(text):
    """Aggressive normalization: remove ALL hyphens, lowercase."""
    t = norm(text)
    t = t.replace("-", "").replace("  ", " ")
    return t.lower().strip()

conn_cur = psycopg2.connect("host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@")
conn_old = psycopg2.connect("host=localhost port=5432 dbname=steiner_apr28 user=steiner password=Dd08120@")
cur = conn_cur.cursor()
old = conn_old.cursor()

# Load old translations
old.execute("""
    SELECT s.text_de, s.text_zh
    FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id
    JOIN lectures l ON p.lecture_id = l.id
    WHERE l.book_id = 302 AND s.text_zh IS NOT NULL AND s.text_zh != ''
""")
old_rows = old.fetchall()
print(f"Old translations: {len(old_rows)}")

# Build lookup: loose_norm -> zh (for short key matching)
loose_map = {}
for de, zh in old_rows:
    key = norm_loose(de)
    if key and zh and len(key) > 10:
        if key not in loose_map or len(zh) > len(loose_map[key]):
            loose_map[key] = zh

# Also build: first N chars -> list of (de, zh) for prefix matching
prefix_index = {}
for de, zh in old_rows:
    key = norm(de)
    if len(key) > 30:
        for prefix_len in [50, 80, 120]:
            prefix = key[:prefix_len]
            if prefix not in prefix_index:
                prefix_index[prefix] = []
            prefix_index[prefix].append((key, zh))

# Get current unmatched sentences
cur.execute("""
    SELECT s.id, s.text_de
    FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id
    JOIN lectures l ON p.lecture_id = l.id
    WHERE l.book_id = 302 AND (s.text_zh IS NULL OR s.text_zh = '')
""")
unmatched = cur.fetchall()
print(f"Remaining unmatched: {len(unmatched)}")

loose_matches = 0
prefix_matches = 0
concat_matches = 0
to_update = []

for sid, text_de in unmatched:
    key = norm(text_de)
    key_loose = norm_loose(text_de)

    # 1. Try loose matching (hyphens removed)
    if key_loose in loose_map:
        to_update.append((loose_map[key_loose], sid))
        loose_matches += 1
        continue

    # 2. Try prefix matching: first 80 chars match
    if len(key) > 50:
        for prefix_len in [120, 80, 50]:
            prefix = key[:prefix_len]
            if prefix in prefix_index:
                candidates = prefix_index[prefix]
                # Pick the longest matching candidate
                best = max(candidates, key=lambda x: len(x[0]))
                to_update.append((best[1], sid))
                prefix_matches += 1
                break
        else:
            continue
    else:
        continue

print(f"\nPass 2 results:")
print(f"  Loose (hyphen-free) matches: {loose_matches}")
print(f"  Prefix matches:             {prefix_matches}")
print(f"  Concatenation matches:      {concat_matches}")
print(f"  Total to update:            {len(to_update)}")

# Apply
if to_update:
    print(f"\nApplying {len(to_update)} updates...")
    for i in range(0, len(to_update), 200):
        chunk = to_update[i:i+200]
        for zh, sid in chunk:
            cur.execute("UPDATE sentences SET text_zh = %s WHERE id = %s", (zh, sid))
        conn_cur.commit()
        print(f"  {min(i+200, len(to_update))}/{len(to_update)}")

# Final verification
cur.execute("""
    SELECT COUNT(*) as total,
           COUNT(CASE WHEN text_zh IS NOT NULL AND text_zh != '' THEN 1 END) as translated
    FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id
    JOIN lectures l ON p.lecture_id = l.id
    WHERE l.book_id = 302
""")
total, translated = cur.fetchone()
print(f"\nFinal: {translated}/{total} sentences translated ({100*translated/total:.1f}%)")

cur.close(); old.close()
conn_cur.close(); conn_old.close()
print("Done!")
