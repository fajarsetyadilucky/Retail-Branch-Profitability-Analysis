import urllib.request
import json

url = "https://api.github.com/repos/fajarsetyadilucky/Retail-Branch-Profitability-Analysis/contents"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        items = json.loads(resp.read().decode())
        print(f"Total items in root of remote repo: {len(items)}")
        for it in items:
            print(f" - {it['name']} ({it['type']}, size: {it.get('size', 0)})")
except Exception as e:
    print("Error:", e)
