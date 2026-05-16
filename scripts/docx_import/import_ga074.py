"""Import GA074 from .docx with header block grouping.

Based on the GA083 v4 import logic (reimport_ga083_v4.py).
- Groups header blocks (title + subtitle + date into multi-line paragraphs)
- Detects VORTRAG lecture boundaries
- Merges body text continuations (skipping header blocks)
- Splits sentences within merged paragraphs (skipping header blocks)
"""
import csv, io, psycopg2, re, zipfile, sys
from xml.etree import ElementTree as ET

XHTML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# ── Config ────────────────────────────────────────────────────────
BOOK_ID = 59
DOCX_PATH = "/opt/steiner-reader/books/docx/GA074.docx"
TRANS_CSV = "/tmp/ga074_trans.csv"

LECTURE_TITLES = {
    "ERSTER VORTRAG": (
        "ERSTER VORTRAG\nThomas und Augustinus\nDornach, 22. Mai 1920",
        "第一讲",
    ),
    "ZWEITER VORTRAG": (
        "ZWEITER VORTRAG\nDas Wesen des Thomismus\nDornach, 23. Mai 1920",
        "第二讲",
    ),
    "DRITTER VORTRAG": (
        "DRITTER VORTRAG\nDie Bedeutung des Thomismus in der Gegenwart\nDornach, 24. Mai 1920",
        "第三讲",
    ),
    "ANHANG": ("ANHANG", "附录"),
}

HEADER_KEYS = [
    "ERSTER VORTRAG", "ZWEITER VORTRAG", "DRITTER VORTRAG",
    "ANHANG",
]

SUBTITLE_PREFIXES = [
    "THOMAS UND",
    "DAS WESEN DES THOMISMUS",
    "DIE BEDEUTUNG DES THOMISMUS IN DER GEGENWART",
]

DATE_PAT = re.compile(
    r"(Wien|Dornach|Berlin|München|Stuttgart|Zürich|Basel|Bern|Köln|Hamburg|Leipzig|Dresden|Nürnberg|Hannover|Breslau|Graz|Linz|Salzburg|Prag|Budapest|Paris|London|Kristiania|Oslo|Kopenhagen|Stockholm|Haag|Arnheim|Utrecht|Oxford|Torquay|Pennmaenmawr|Ilkley),\s*\d+\.?\s*(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember|Jänner)\s*\d{4}"
)

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


def norm(text):
    return re.sub(r"\s+", " ", (text or "").replace("\xad", "").strip())


# ── Header helpers ────────────────────────────────────────────────
def is_header_ordinal(text):
    t = text.strip()
    for hk in HEADER_KEYS:
        if t == hk or t.startswith(hk + "\n"):
            return hk
    first_line = t.split("\n")[0].strip()
    for hk in HEADER_KEYS:
        if first_line == hk:
            return hk
    return None


def is_subtitle_start(text):
    t = text.strip()
    for sp in SUBTITLE_PREFIXES:
        if t.upper().startswith(sp.upper()):
            return True
    if len(t) > 5 and len(t) < 80 and t.upper() == t:
        letters = [c for c in t if c.isalpha()]
        if letters and sum(1 for c in letters if c == c.upper()) / len(letters) > 0.8:
            return True
    return False


def extract_date_from_subtitle(text):
    t = text.strip()
    m = DATE_PAT.search(t)
    if m:
        before = t[: m.start()]
        for city in ["Wien", "Dornach", "Berlin", "München", "Stuttgart"]:
            city_idx = before.rfind(city)
            if city_idx >= 0:
                return t[:city_idx].strip(), t[city_idx:].strip()
        return t[: m.start()].strip(), t[m.start():].strip()
    return t, None


def looks_like_body(text):
    t = text.strip()
    if not t:
        return False
    if BODY_STARTERS_RE.match(t):
        return True
    if len(t) > 200:
        return True
    return False


# ── Parse .docx ───────────────────────────────────────────────────
print(f"Parsing {DOCX_PATH}...")
with zipfile.ZipFile(DOCX_PATH) as zf:
    xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    all_paras = []
    for p in root.iter(f"{{{XHTML_NS}}}p"):
        t = extract_para(p)
        if t and len(t) > 3:
            if re.match(r"^\d{1,3}$", t.strip()):
                continue
            all_paras.append(t)

print(f"  {len(all_paras)} raw paragraphs")

# ── Load existing translations ────────────────────────────────────
trans_map = {}
try:
    with open(TRANS_CSV, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                key = norm(row[0])
                val = norm(row[1])
                if key and val and len(val) > 2:
                    trans_map[key] = val
    print(f"Loaded {len(trans_map)} existing translations")
except FileNotFoundError:
    print("No translation backup, proceeding without")

# ── Phase 1: Group header blocks ──────────────────────────────────
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
        for _ in range(3):
            if i >= len(all_paras):
                break
            next_p = all_paras[i].strip()
            if is_header_ordinal(next_p) or looks_like_body(next_p):
                break
            if is_subtitle_start(next_p):
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
            break
        if len(header_lines) > 1:
            header_group_count += 1
        grouped.append("\n".join(header_lines))
    else:
        grouped.append(p)
        i += 1

print(f"  {len(all_paras)} -> {len(grouped)} paragraphs ({header_group_count} header blocks)")

# ── Phase 2: Detect lecture boundaries ────────────────────────────
boundaries = []
for i, para in enumerate(grouped):
    hk = is_header_ordinal(para)
    if hk and "VORTRAG" in hk:
        boundaries.append((i, hk))
    elif hk == "ANHANG":
        # Only use ANHANG that appears after all VORTRAG lectures
        pass

# Find ANHANG after last VORTRAG lecture
last_vortrag_pos = boundaries[-1][0] if boundaries else 0
for i, para in enumerate(grouped):
    if i > last_vortrag_pos + 5 and is_header_ordinal(para) == "ANHANG":
        boundaries.append((i, "ANHANG"))
        break

print(f"\nPhase 2: {len(boundaries)} lecture boundaries")
for pos, key in boundaries:
    print(f"  {key} at para {pos}")

# ── Phase 3: Build lectures ───────────────────────────────────────
first_body = boundaries[0][0]
front_matter = grouped[:first_body]

body_lectures = []
for j, (pos, key) in enumerate(boundaries):
    end = boundaries[j + 1][0] if j + 1 < len(boundaries) else len(grouped)
    body = grouped[pos:end]
    td, tz = LECTURE_TITLES.get(key, (key, key))
    body_lectures.append((td, tz, body))

lec_data = [("Die Philosophie des Thomas von Aquino", "托马斯·阿奎那的哲学", front_matter)] + body_lectures

print(f"\nPhase 3: {len(lec_data)} lectures (1 TOC + {len(body_lectures)} body)")

# ── Phase 4: Database import ──────────────────────────────────────
conn = psycopg2.connect(
    "host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@"
)
cur = conn.cursor()

print("\nPhase 4: Clearing existing GA074 data...")
cur.execute("DELETE FROM lecture_images WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (BOOK_ID,))
cur.execute("DELETE FROM sentences WHERE paragraph_id IN (SELECT id FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s))", (BOOK_ID,))
cur.execute("DELETE FROM paragraphs WHERE lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (BOOK_ID,))
cur.execute("DELETE FROM lectures WHERE book_id=%s", (BOOK_ID,))
conn.commit()

tp = ts = m = 0
for oi, (td, tz, body) in enumerate(lec_data, 1):
    if not body:
        continue
    cur.execute(
        "INSERT INTO lectures (book_id, title_de, title_zh, order_index, level) VALUES (%s,%s,%s,%s,%s) RETURNING id",
        (BOOK_ID, td, tz, oi, "lecture"),
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

# ── Phase 5: Merge body text continuations ────────────────────────
print("\nPhase 5: Merging body text continuations...")
merged = 0
SHORT_CONNECTORS = {"und", "aber", "denn", "doch", "auch", "oder", "so", "nun", "da", "dann"}

cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (BOOK_ID,))
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

# ── Phase 6: Split sentences ──────────────────────────────────────
print("\nPhase 6: Splitting sentences...")
SENT_SPLIT = re.compile(
    r"(?<=[.!?])\s+(?=[A-ZÄÖÜ])(?!(?:Januar|Februar|März|April|Mai|Juni|Juli|August|"
    r"September|Oktober|November|Dezember|Jänner)\b)"
)

cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (BOOK_ID,))
for (lec_id,) in cur.fetchall():
    cur.execute(
        "SELECT p.id, s.text_de, s.text_zh "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,),
    )
    for pid, td, tz in cur.fetchall():
        if not td or is_header_ordinal(td):
            continue
        parts = SENT_SPLIT.split(td)
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
    "WHERE p.lecture_id IN (SELECT id FROM lectures WHERE book_id=%s) GROUP BY p.id) sub",
    (BOOK_ID,),
)
total_paras, avg_sents = cur.fetchone()
print(f"\n{'='*60}")
print(f"Final: {total_paras} paragraphs, avg {avg_sents} sentences/para")

cur.execute(
    "SELECT id, title_de, order_index FROM lectures WHERE book_id=%s ORDER BY order_index",
    (BOOK_ID,),
)
for lec_id, td, oi in cur.fetchall():
    cur.execute(
        "SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id WHERE p.lecture_id = %s",
        (lec_id,),
    )
    sc = cur.fetchone()[0]
    title_line = td.split(chr(10))[0][:50]
    print(f"  Lec {oi}: {sc:4d} sentences - {title_line}")

cur.close()
conn.close()
print("\nDone!")
