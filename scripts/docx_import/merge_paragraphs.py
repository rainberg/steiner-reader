"""Merge body text paragraphs while preserving header blocks.

Phase 1: Merge header ordinals (ERSTER VORTRAG, etc.) with their subtitle and date lines.
Phase 2: Merge body text continuations, but NEVER merge into or across header blocks.

Usage: python3 merge_v2.py [book_id]  # defaults to 302 (GA083)
"""
import psycopg2, re, sys

conn = psycopg2.connect("host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@")
cur = conn.cursor()

HEADER_KEYS = [
    "ERSTER VORTRAG", "ZWEITER VORTRAG", "DRITTER VORTRAG",
    "VIERTER VORTRAG", "FUNFTER VORTRAG",
    "SECHSTER VORTRAG", "SIEBENTER VORTRAG", "ACHTER VORTRAG",
    "NEUNTER VORTRAG", "ZEHNTER VORTRAG",
]
HEADER_PAT = re.compile(r'^(' + '|'.join(HEADER_KEYS) + r')\b')

MONTH_PAT = re.compile(
    r'(Januar|Februar|März|April|Mai|Juni|Juli|August|'
    r'September|Oktober|November|Dezember|\d{4})'
)

BODY_STARTERS = re.compile(
    r'^(Meine|Wir|Ich|Die|Das|Es|In|Auf|Aus|Bei|Mit|Nach|Von|Zu|'
    r'Diese|Dieser|Dieses|Welche|Welcher|Welches|'
    r'So|Da|Nun|Denn|Aber|Und|Oder|Doch|'
    r'Man|Wer|Was|Wie|Wann|Wo|Warum|Weshalb|'
    r'Wenn|Weil|Obwohl|Während|Bevor|Nachdem|Seit|'
    r'Durch|Für|Gegen|Ohne|Um|'
    r'Eine|Einer|Einem|Einen|'
    r'Kann|Können|Muss|Müssen|Soll|Sollen|Will|Wollen|'
    r'Hat|Habe|Haben|Ist|Sind|War|Waren|Wird|Werden)\b'
)

SHORT_CONNECTORS = {"und", "aber", "denn", "doch", "auch", "oder", "so", "nun", "da", "dann"}

def is_all_caps(text):
    letters = [c for c in text if c.isalpha()]
    if len(letters) < 3:
        return False
    return sum(1 for c in letters if c == c.upper()) / len(letters) > 0.8

def is_date_like(text):
    return bool(MONTH_PAT.search(text))

def is_header(text):
    return bool(HEADER_PAT.match(text.strip()))

def is_body_start(text):
    return bool(BODY_STARTERS.match(text.strip()))


book_id = int(sys.argv[1]) if len(sys.argv) > 1 else 302

# ============================================================
# Phase 1: Merge header blocks (header + subtitle + date)
# ============================================================
print("Phase 1: Merging header blocks...")
header_merges = 0

cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
lecture_ids = [r[0] for r in cur.fetchall()]

for lec_id in lecture_ids:
    cur.execute(
        "SELECT p.id, s.text_de, s.id as sid "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,)
    )
    paras = [(pid, (text or "").strip(), sid) for pid, text, sid in cur.fetchall()]

    i = 0
    while i < len(paras):
        if not is_header(paras[i][1]):
            i += 1
            continue

        # Collect header-adjacent lines
        merged_lines = [paras[i][1]]
        ids_to_delete = []

        for offset in range(1, min(4, len(paras) - i)):
            nt = paras[i + offset][1]
            if is_header(nt) or is_body_start(nt):
                break
            if is_all_caps(nt) or is_date_like(nt) or (len(nt) < 50 and not nt.endswith(('.', '!', '?'))):
                merged_lines.append(nt)
                ids_to_delete.append((paras[i + offset][0], paras[i + offset][2]))
            else:
                break

        if ids_to_delete:
            header_block = "\n".join(merged_lines)
            cur.execute(
                "UPDATE sentences SET text_de=%s, text_zh=NULL WHERE id=%s",
                (header_block, paras[i][2])
            )
            for del_pid, del_sid in ids_to_delete:
                cur.execute("DELETE FROM sentences WHERE id=%s", (del_sid,))
                cur.execute("DELETE FROM paragraphs WHERE id=%s", (del_pid,))
            header_merges += len(ids_to_delete)
            # Remove deleted from paras list
            deleted_sids = {s for _, s in ids_to_delete}
            paras = [p for p in paras if p[2] not in deleted_sids]

        i += 1

conn.commit()
print(f"  Merged {header_merges} subtitle/date lines into header blocks")

# ============================================================
# Phase 2: Merge body text (skip header blocks)
# ============================================================
print("\nPhase 2: Merging body text (skipping header blocks)...")
body_merges = 0

for lec_id in lecture_ids:
    cur.execute(
        "SELECT p.id, s.text_de, s.text_zh, s.id as sid "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,)
    )
    rows = [(pid, (td or "").strip(), (tz or "").strip() if tz else None, sid)
            for pid, td, tz, sid in cur.fetchall()]

    if len(rows) < 2:
        continue

    new_rows = list(rows)
    i = 0
    while i < len(new_rows) - 1:
        pid1, td1, tz1, sid1 = new_rows[i]
        pid2, td2, tz2, sid2 = new_rows[i + 1]

        # NEVER merge if either paragraph is a header block
        if is_header(td1) or is_header(td2):
            i += 1
            continue

        should_merge = False

        # Short connector words
        if len(td1) < 10 and td1.lower() in SHORT_CONNECTORS:
            should_merge = True
        # Previous para doesn't end with sentence-ending punctuation
        elif td1 and not td1[-1] in ".!?":
            should_merge = True

        if should_merge:
            merged_de = re.sub(r"\s+", " ", td1 + " " + td2)
            cur.execute(
                "UPDATE sentences SET text_de=%s, text_zh=NULL WHERE id=%s",
                (merged_de, sid1)
            )
            cur.execute("DELETE FROM sentences WHERE id=%s", (sid2,))
            cur.execute("DELETE FROM paragraphs WHERE id=%s", (pid2,))
            body_merges += 1
            new_rows[i] = (pid1, merged_de, None, sid1)
            new_rows.pop(i + 1)
        else:
            i += 1

conn.commit()
print(f"  Merged {body_merges} body text continuations")

# ============================================================
# Renumber paragraph order_index
# ============================================================
print("\nRenumbering paragraphs...")
for lec_id in lecture_ids:
    cur.execute(
        "SELECT id FROM paragraphs WHERE lecture_id=%s ORDER BY order_index, id",
        (lec_id,)
    )
    for idx, pid in enumerate([r[0] for r in cur.fetchall()]):
        cur.execute("UPDATE paragraphs SET order_index=%s WHERE id=%s", (idx, pid))

conn.commit()

cur.execute(
    "SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id "
    "WHERE p.lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,)
)
total = cur.fetchone()[0]
print(f"\nDone. Total paragraphs: {total} (header merges: {header_merges}, body merges: {body_merges})")

cur.close(); conn.close()
