"""Reimport GA083 from .docx with proper header detection and lecture splitting.

Key fixes over reimport_final3.py:
1. "FÜNFTER VORTRAG" with umlaut (not "FUNFTER") → detects 5th lecture separately
2. Handle subtitle+date on same line (common in .docx)
3. Proper header block merging (detect by content, not fixed position)
4. Improved merge logic that skips ALL header blocks
"""
import psycopg2, re, zipfile, sys
from xml.etree import ElementTree as ET

XHTML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# ── .docx text extraction ────────────────────────────────────────
def extract_para(p_elem):
    parts = []
    for r in p_elem.iter(f"{{{XHTML_NS}}}r"):
        for t in r.iter(f"{{{XHTML_NS}}}t"):
            if t.text:
                parts.append(t.text)
    result = []
    for i, part in enumerate(parts):
        if i > 0:
            prev = parts[i - 1]
            if (
                prev and part
                and not prev.endswith(" ")
                and not prev.endswith("-")
                and not part.startswith(" ")
                and not part.startswith("-")
            ):
                result.append(" ")
        result.append(part)
    return "".join(result).strip()


def norm(t):
    return re.sub(r"\s+", " ", (t or "").replace("\xad", "").strip())


# ── Parse .docx ───────────────────────────────────────────────────
docx_path = "/opt/steiner-reader/books/docx/GA083.docx"
with zipfile.ZipFile(docx_path) as zf:
    xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    all_paras = []
    for p in root.iter(f"{{{XHTML_NS}}}p"):
        t = extract_para(p)
        if t and len(t) > 3:
            if re.match(r"^\d{1,3}$", t.strip()):
                continue  # page numbers
            all_paras.append(t)

# ── Load existing translations ────────────────────────────────────
trans_map = {}
trans_csv = "/tmp/ga083_trans.csv"
try:
    with open(trans_csv) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            idx = line.find(",")
            if idx < 0: continue
            key = norm(line[:idx].strip().strip('"'))
            val = line[idx+1:].strip().strip('"')
            if key and val and len(val) > 2:
                trans_map[key] = val
    print(f"Loaded {len(trans_map)} existing translations")
except FileNotFoundError:
    print("No translation backup found, proceeding without")

# ── Header keys and patterns ──────────────────────────────────────
HEADER_KEYS = [
    "ERSTER VORTRAG", "ZWEITER VORTRAG", "DRITTER VORTRAG",
    "VIERTER VORTRAG", "FÜNFTER VORTRAG",  # ← Ü umlaut!
    "SECHSTER VORTRAG", "SIEBENTER VORTRAG", "ACHTER VORTRAG",
    "NEUNTER VORTRAG", "ZEHNTER VORTRAG", "ANHANG",
]

# Known subtitle patterns (check if text STARTS WITH these)
SUBTITLE_PREFIXES = [
    "ANTHROPOSOPHIE UND",
    "DIE ZEIT UND IHRE SOZIAL",
    "DIE KERNPUNKTE DER SOZIALEN FRAGE",
]

# Date/location pattern
DATE_PAT = re.compile(
    r"(Wien|Dornach|Berlin|München|Stuttgart|Zürich|Basel|Bern|Köln|Hamburg|Leipzig|Dresden|Nürnberg|Hannover|Breslau|Graz|Linz|Salzburg|Prag|Budapest|Paris|London|Kristiania|Oslo|Kopenhagen|Stockholm|Haag|Arnheim|Utrecht|Oxford|Torquay|Pennmaenmawr|Ilkley),\s*\d+\.?\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|Jänner)\s*\d{4}"
)

# Common body text sentence starters
BODY_STARTERS_RE = re.compile(
    r"^(Meine|Wir|Ich|Die|Das|Es|In|Auf|Aus|Bei|Mit|Nach|Von|Zu|"
    r"Diese|Dieser|Dieses|Welche|Welcher|Welches|"
    r"So|Da|Nun|Denn|Aber|Und|Oder|Doch|"
    r"Man|Wer|Was|Wie|Wann|Wo|Warum|Weshalb|"
    r"Wenn|Weil|Obwohl|Während|Bevor|Nachdem|Seit|"
    r"Durch|Für|Gegen|Ohne|Um|"
    r"Eine|Einer|Einem|Einen|"
    r"Kann|Können|Muss|Müssen|Soll|Sollen|Will|Wollen|"
    r"Hat|Habe|Haben|Ist|Sind|War|Waren|Wird|Werden)\b"
)


def is_header_ordinal(text):
    """Check if text matches a header key (exact match or starts with)."""
    t = text.strip()
    for hk in HEADER_KEYS:
        if t == hk or t.startswith(hk + "\n"):
            return hk
    # Also try: first line matches
    first_line = t.split("\n")[0].strip()
    for hk in HEADER_KEYS:
        if first_line == hk:
            return hk
    return None


def is_subtitle_start(text):
    """Check if text looks like a subtitle (ALL CAPS line or known prefix)."""
    t = text.strip()
    for sp in SUBTITLE_PREFIXES:
        if t.upper().startswith(sp.upper()):
            return True
    # All caps, reasonably short
    if len(t) > 5 and len(t) < 80 and t.upper() == t:
        letters = [c for c in t if c.isalpha()]
        if letters and sum(1 for c in letters if c == c.upper()) / len(letters) > 0.8:
            return True
    return False


def extract_date_from_subtitle(text):
    """If subtitle line also contains a date, extract the date part.
    Returns (subtitle_part, date_part) or (text, None)."""
    t = text.strip()
    m = DATE_PAT.search(t)
    if m:
        date_start = m.start()
        # Find where the date actually begins (look for city name)
        before = t[:date_start]
        # Try to split before the city name
        for city in ["Wien", "Dornach", "Berlin", "München", "Stuttgart"]:
            city_idx = before.rfind(city)
            if city_idx >= 0:
                return t[:city_idx].strip(), t[city_idx:].strip()
        # Fallback: split at the regex match position
        return t[:date_start].strip(), t[date_start:].strip()
    return t, None


def looks_like_body(text):
    """Check if text looks like body text (should NOT be in header block)."""
    t = text.strip()
    if not t:
        return False
    if BODY_STARTERS_RE.match(t):
        return True
    # Long paragraph is probably body text
    if len(t) > 200:
        return True
    return False


# ── Group header blocks ───────────────────────────────────────────
# In .docx, structure varies:
#   [header ord]         "ERSTER VORTRAG"
#   [subtitle]           "ANTHROPOSOPHIE UND NATURWISSENSCHAFT"   OR
#   [subtitle+date]      "ANTHROPOSOPHIE UND KOSMOLOGIE Wien, 5. Juni 1922"
#   [date]               "Wien, 3. Juni 1922"
#   [body]               "Meine sehr verehrten Anwesenden!..."

print("\nPhase 1: Grouping header blocks...")
grouped = []
i = 0
header_group_count = 0
while i < len(all_paras):
    p = all_paras[i]
    hk = is_header_ordinal(p)
    if hk:
        header_lines = [p.strip()]
        i += 1
        # Collect subtitle and date lines (up to 3 following paragraphs)
        for _ in range(3):
            if i >= len(all_paras):
                break
            next_p = all_paras[i].strip()
            # Stop if it's another header or body text
            if is_header_ordinal(next_p):
                break
            if looks_like_body(next_p):
                break
            # Check if it's subtitle or date-like
            if is_subtitle_start(next_p):
                # This is a subtitle line - check if date is on same line
                sub_part, date_part = extract_date_from_subtitle(next_p)
                header_lines.append(sub_part)
                if date_part:
                    header_lines.append(date_part)
                i += 1
                continue
            if DATE_PAT.match(next_p) or DATE_PAT.search(next_p):
                header_lines.append(next_p)
                i += 1
                continue
            # Not subtitle or date - stop collecting
            break
        if len(header_lines) > 1:
            header_group_count += 1
        grouped.append("\n".join(header_lines))
    else:
        # Handle "orphan" subtitle/date lines (no header ordinal before them)
        # These occur when a FUNFTER VORTRAG was missed
        grouped.append(p)
        i += 1

print(f"  Grouped: {len(all_paras)} -> {len(grouped)} paragraphs ({header_group_count} header blocks)")

# ── Detect lecture boundaries ─────────────────────────────────────
boundaries = []
for i, para in enumerate(grouped):
    hk = is_header_ordinal(para)
    if hk and "VORTRAG" in hk:
        boundaries.append((i, hk))

print(f"\nPhase 2: Lecture boundaries ({len(boundaries)} found):")
for pos, key in boundaries:
    next_pos = "end" if boundaries.index((pos, key)) == len(boundaries) - 1 else boundaries[boundaries.index((pos, key)) + 1][0]
    print(f"  {key} at para {pos} (→ {next_pos})")

# ── Lecture titles ────────────────────────────────────────────────
lecture_titles = {
    "ERSTER VORTRAG": (
        "ERSTER VORTRAG\nANTHROPOSOPHIE UND NATURWISSENSCHAFT\nWien, 1. Juni 1922",
        "第一讲",
    ),
    "ZWEITER VORTRAG": (
        "ZWEITER VORTRAG\nAnthroposophie und Psychologie\nWien, 2. Juni 1922",
        "第二讲",
    ),
    "DRITTER VORTRAG": (
        "DRITTER VORTRAG\nAnthroposophie und Weltorientierung\nWien, 3. Juni 1922",
        "第三讲",
    ),
    "VIERTER VORTRAG": (
        "VIERTER VORTRAG\nAnthroposophie und Weltentwicklung\nWien, 4. Juni 1922",
        "第四讲",
    ),
    "FÜNFTER VORTRAG": (
        "FÜNFTER VORTRAG\nAnthroposophie und Kosmologie\nWien, 5. Juni 1922",
        "第五讲",
    ),
    "SECHSTER VORTRAG": (
        "SECHSTER VORTRAG\nDie Zeit und ihre sozialen Forderungen\nWien, 7. Juni 1922",
        "第六讲",
    ),
    "SIEBENTER VORTRAG": (
        "SIEBENTER VORTRAG\nDie Zeit und ihre soziale Gestaltung\nWien, 8. Juni 1922",
        "第七讲",
    ),
    "ACHTER VORTRAG": (
        "ACHTER VORTRAG\nDie Zeit und ihre sozialen Mängel\nWien, 9. Juni 1922",
        "第八讲",
    ),
    "NEUNTER VORTRAG": (
        "NEUNTER VORTRAG\nDie Zeit und ihre sozialen Hoffnungen\nWien, 10. Juni 1922",
        "第九讲",
    ),
    "ZEHNTER VORTRAG": (
        "ZEHNTER VORTRAG\nDie Kernpunkte der sozialen Frage\nWien, 11. Juni 1922",
        "第十讲",
    ),
    "ANHANG": ("ANHANG", "附录"),
}

# ── Build lecture bodies ──────────────────────────────────────────
first_body = boundaries[0][0]
front_matter = grouped[:first_body]

body_lectures = []
for j, (pos, key) in enumerate(boundaries):
    end = boundaries[j + 1][0] if j + 1 < len(boundaries) else len(grouped)
    body = grouped[pos:end]
    td, tz = lecture_titles.get(key, (key, key))
    body_lectures.append((td, tz, body))

lec_data = [("Vorwort und Inhaltsverzeichnis", "前言和目录", front_matter)] + body_lectures

print(f"\nPhase 3: {len(lec_data)} lectures to import (1 TOC + {len(body_lectures)} body)")

# ── Database import ───────────────────────────────────────────────
conn = psycopg2.connect(
    "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
)
cur = conn.cursor()

# Clear existing data
print("\nPhase 4: Clearing existing GA083 data...")
cur.execute("DELETE FROM lecture_images WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=302)")
cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=302))")
cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=302)")
cur.execute("DELETE FROM lectures WHERE book_id=302")
conn.commit()

tp = ts = m = 0

for oi, (td, tz, body) in enumerate(lec_data, 1):
    if not body:
        continue
    cur.execute(
        "INSERT INTO lectures (book_id, title_de, title_zh, order_index, level) VALUES (302,%s,%s,%s,%s) RETURNING id",
        (td, tz, oi, "lecture"),
    )
    lid = cur.fetchone()[0]
    for pi, para in enumerate(body, 1):
        if len(para) < 3:
            continue
        zh = trans_map.get(norm(para))
        if zh:
            m += 1
        cur.execute(
            "INSERT INTO paragraphs (lecture_id, order_index) VALUES (%s,%s) RETURNING id",
            (lid, pi),
        )
        pid = cur.fetchone()[0]
        tp += 1
        cur.execute(
            "INSERT INTO sentences (paragraph_id, order_index, text_de, text_zh) VALUES (%s,0,%s,%s)",
            (pid, para, zh),
        )
        ts += 1

conn.commit()
print(f"  Imported: {len(lec_data)} lectures, {tp} paras, {ts} sentences, {m} translations")

# ── Merge continuation paragraphs (skip header blocks) ────────────
print("\nPhase 5: Merging body text continuations...")
merged = 0
SHORT_CONNECTORS = {"und", "aber", "denn", "doch", "auch", "oder", "so", "nun", "da", "dann"}

cur.execute(
    "SELECT id FROM lectures WHERE book_id=302 ORDER BY order_index"
)
for (lec_id,) in cur.fetchall():
    cur.execute(
        "SELECT p.id, s.text_de, s.text_zh, s.id as sid "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,),
    )
    rows = [(pid, (td or "").strip(), tz, sid) for pid, td, tz, sid in cur.fetchall()]
    if len(rows) < 2:
        continue

    new_rows = list(rows)
    i = 0
    while i < len(new_rows) - 1:
        pid1, td1, tz1, sid1 = new_rows[i]
        pid2, td2, tz2, sid2 = new_rows[i + 1]

        # Skip header blocks: multi-line VORTRAG paragraphs
        is_header = bool(is_header_ordinal(td1)) or bool(is_header_ordinal(td2))

        if not is_header:
            should_merge = False
            if len(td1) < 10 and td1.lower() in SHORT_CONNECTORS:
                should_merge = True
            elif td1 and not td1[-1] in ".!?":
                should_merge = True

            if should_merge:
                merged_de = re.sub(r"\s+", " ", td1 + " " + td2)
                cur.execute(
                    "UPDATE sentences SET text_de=%s, text_zh=NULL WHERE id=%s",
                    (merged_de, sid1),
                )
                cur.execute("DELETE FROM sentences WHERE id=%s", (sid2,))
                cur.execute("DELETE FROM paragraphs WHERE id=%s", (pid2,))
                merged += 1
                new_rows[i] = (pid1, merged_de, None, sid1)
                new_rows.pop(i + 1)
                continue
        i += 1

conn.commit()
print(f"  Merged: {merged} body continuations")

# ── Split sentences (skip header blocks) ──────────────────────────
print("\nPhase 6: Splitting sentences...")
SENT_SPLIT = re.compile(
    r"(?<=[.!?])\s+(?=[A-ZÄÖÜ])(?!(?:Januar|Februar|März|April|Mai|Juni|Juli|August|"
    r"September|Oktober|November|Dezember|Jänner)\b)"
)

cur.execute(
    "SELECT id FROM lectures WHERE book_id=302 ORDER BY order_index"
)
for (lec_id,) in cur.fetchall():
    cur.execute(
        "SELECT p.id, s.text_de, s.text_zh "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,),
    )
    for pid, td, tz in cur.fetchall():
        if not td:
            continue
        # Skip header blocks (multi-line VORTRAG paragraphs)
        if is_header_ordinal(td):
            continue
        # Split at sentence boundaries
        parts = SENT_SPLIT.split(td)
        # Re-merge number+period fragments (e.g., "16. Jahrhundert")
        merged_parts = []
        for p in parts:
            p = p.strip()
            if not p:
                continue
            if merged_parts and re.search(r"\d+\.\s*$", merged_parts[-1]):
                merged_parts[-1] = merged_parts[-1] + " " + p
            else:
                merged_parts.append(p)
        merged_parts = [p for p in merged_parts if len(p) > 3]
        if len(merged_parts) <= 1:
            continue
        # Update first sentence, insert rest
        for si, sent in enumerate(merged_parts):
            if si == 0:
                cur.execute(
                    "UPDATE sentences SET text_de=%s, order_index=0 WHERE paragraph_id=%s",
                    (sent, pid),
                )
            else:
                cur.execute(
                    "INSERT INTO sentences (paragraph_id, order_index, text_de) VALUES (%s,%s,%s)",
                    (pid, si, sent),
                )

conn.commit()

# ── Report ─────────────────────────────────────────────────────────
cur.execute(
    "SELECT COUNT(*), ROUND(AVG(cnt)::numeric,1) "
    "FROM (SELECT COUNT(s.id) as cnt FROM paragraphs p "
    "JOIN sentences s ON s.paragraph_id = p.id "
    "WHERE p.lecture_id IN (SELECT id FROM lectures WHERE book_id=302) GROUP BY p.id) sub"
)
total_paras, avg_sents = cur.fetchone()
print(f"\n{'='*60}")
print(f"Final: {total_paras} paragraphs, avg {avg_sents} sentences/para")

# List all lectures
cur.execute(
    "SELECT id, title_de, order_index FROM lectures WHERE book_id=302 ORDER BY order_index"
)
for (lec_id, td, oi) in cur.fetchall():
    print(f"  Lecture {oi}: {td.split(chr(10))[0][:60]}")

cur.close()
conn.close()
print("\nDone!")
