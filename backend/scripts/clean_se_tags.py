"""一次性清理 sentences.text_zh 中的 #SE数字-数字 翻译标识。

用法：
    python3 clean_se_tags.py           # 预览模式，只显示影响范围和样例
    python3 clean_se_tags.py --execute # 执行清理
"""

import argparse
import psycopg2
import re

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "steiner_reader",
    "user": "steiner",
    "password": "Dd08120@",
}

# 匹配 #SE数字-数字 及前后空白
SE_PATTERN = r"\s*#SE\d+-\d+\s*"


def main():
    parser = argparse.ArgumentParser(description="清理翻译标识 #SE数字-数字")
    parser.add_argument("--execute", action="store_true", help="执行清理（默认只预览）")
    args = parser.parse_args()

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # 1. 统计影响范围
    cur.execute("SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE\\d+-\\d+'")
    total = cur.fetchone()[0]
    print(f"包含 #SE 标识的句子数: {total}")

    if total == 0:
        print("无需清理")
        return

    # 2. 显示清理前样例（10条）
    cur.execute("""
        SELECT id, text_zh FROM sentences
        WHERE text_zh ~ '#SE\\d+-\\d+'
        ORDER BY id
        LIMIT 10
    """)
    print("\n--- 清理前样例 ---")
    samples = cur.fetchall()
    for sid, text in samples:
        print(f"  [{sid}] {text[:120]}")

    # 3. 显示清理后样例
    print("\n--- 清理后样例 ---")
    for sid, text in samples:
        cleaned = re.sub(SE_PATTERN, " ", text).strip()
        print(f"  [{sid}] {cleaned[:120]}")

    if not args.execute:
        print("\n预览模式，未执行清理。添加 --execute 参数执行清理。")
        cur.close()
        conn.close()
        return

    # 4. 执行清理
    print("\n--- 执行清理 ---")
    cur.execute("""
        UPDATE sentences
        SET text_zh = btrim(regexp_replace(text_zh, '\\s*#SE\\d+-\\d+\\s*', ' ', 'g'))
        WHERE text_zh ~ '#SE\\d+-\\d+'
    """)
    updated = cur.rowcount
    conn.commit()
    print(f"已更新 {updated} 条句子")

    # 5. 验证
    cur.execute("SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE\\d+-\\d+'")
    remaining = cur.fetchone()[0]
    print(f"清理后剩余 #SE 标识句子数: {remaining}")

    if remaining > 0:
        print("警告：仍有残留标识，请检查")
    else:
        print("清理完成，所有 #SE 标识已移除")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
