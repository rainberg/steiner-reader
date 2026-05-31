import requests
import json

r = requests.get("https://auth.3mudi.com/openapi.json")
d = r.json()
for p in sorted(d.get("paths", {}).keys()):
    print(p)
