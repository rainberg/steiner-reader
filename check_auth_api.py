import httpx
import json

AUTH_URL = "https://auth.3mudi.com"

# Test /api/admin/users response format (without auth - will fail but shows endpoint exists)
resp = httpx.get(f"{AUTH_URL}/api/admin/users", timeout=10)
print(f"Status: {resp.status_code}")
print(f"Body: {resp.text[:500]}")
