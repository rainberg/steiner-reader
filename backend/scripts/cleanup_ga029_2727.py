"""清理GA029 #2727中的PDF换行残留（如"Bemer kungen" -> "Bemerkungen"）"""
import re
import psycopg2

DB_CONN = "host=localhost dbname=steiner_reader user=steiner password=Dd08120@"


def main():
    conn = psycopg2.connect(DB_CONN)
    cur = conn.cursor()

    # 获取所有句子
    cur.execute("""
        SELECT s.id, s.text_de
        FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = 2727
        ORDER BY p.order_index, s.order_index
    """)
    rows = cur.fetchall()
    print(f"获取 {len(rows)} 个句子")

    # 清理每个句子中的PDF换行残留
    # 模式：单词中间有空格（如"Bemer kungen" -> "Bemerkungen"）
    # 但这很难自动判断，我们只修复明显的案例
    updates = 0
    for sent_id, text in rows:
        original = text
        # 修复 "Bemer kungen" -> "Bemerkungen"
        text = text.replace("Bemer kungen", "Bemerkungen")
        # 修复 "Über einstimmung" -> "Übereinstimmung"
        text = text.replace("Über einstimmung", "Übereinstimmung")
        # 修复 "Men schen" -> "Menschen"
        text = text.replace("Men schen", "Menschen")
        # 修复 "Wil lens" -> "Willens"
        text = text.replace("Wil lens", "Willens")
        # 修复 "unse rer" -> "unserer"
        text = text.replace("unse rer", "unserer")
        # 修复 "Ver hältnis" -> "Verhältnis"
        text = text.replace("Ver hältnis", "Verhältnis")
        # 修复 "zurück-\ngeführt" 等连字符换行（已在段落分割时处理）
        # 修复其他明显的换行残留
        text = re.sub(r'(\w)[ \t]+(kungen|stimmung|schen|lens|rer|hltnis|geführt)', r'\1\2', text)

        if text != original:
            cur.execute("UPDATE sentences SET text_de = %s WHERE id = %s", (text, sent_id))
            updates += 1
            print(f"  更新 #{sent_id}: {original[:60]} -> {text[:60]}")

    conn.commit()
    print(f"\n✓ 更新 {updates} 个句子")

    # 验证首句
    cur.execute("""
        SELECT s.text_de FROM paragraphs p
        JOIN sentences s ON s.paragraph_id = p.id
        WHERE p.lecture_id = 2727
        ORDER BY p.order_index ASC, s.order_index ASC LIMIT 1
    """)
    print(f"\n首句: {cur.fetchone()[0][:120]}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
