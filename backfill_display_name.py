import psycopg2
import httpx
import json

DB_URL = "postgresql://steiner:Dd08120%40@localhost:5432/steiner_reader"
AUTH_URL = "https://auth.3mudi.com"

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

cur.execute("SELECT DISTINCT user_id FROM contributions WHERE display_name IS NULL OR display_name = ''")
user_ids = [row[0] for row in cur.fetchall()]
print(f"Found {len(user_ids)} users with missing display_name: {user_ids}")

for uid in user_ids:
    try:
        resp = httpx.get(f"{AUTH_URL}/api/auth/user/{uid}", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            dn = data.get("display_name") or data.get("username") or data.get("email", "")
            if dn:
                cur.execute("UPDATE contributions SET display_name = %s WHERE user_id = %s AND (display_name IS NULL OR display_name = '')", (dn, uid))
                print(f"  user_id={uid} -> display_name='{dn}' (updated {cur.rowcount} rows)")
            else:
                print(f"  user_id={uid} -> no display_name found: {json.dumps(data)}")
        else:
            print(f"  user_id={uid} -> auth service returned {resp.status_code}: {resp.text[:200]}")
    except Exception as e:
        print(f"  user_id={uid} -> error: {e}")

conn.commit()
cur.close()
conn.close()
print("Done!")
