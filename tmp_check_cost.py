import json, urllib.request

lecture_id = 6904

cost_info = json.loads(urllib.request.urlopen(f'http://localhost:8000/api/lectures/{lecture_id}/translation-cost').read())
print("Translation cost info:")
for k, v in cost_info.items():
    print(f"  {k}: {v}")

status = json.loads(urllib.request.urlopen(f'http://localhost:8000/api/lectures/{lecture_id}/translation-status').read())
print("\nTranslation status:")
for k, v in status.items():
    print(f"  {k}: {v}")
