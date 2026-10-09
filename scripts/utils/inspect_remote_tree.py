import urllib.request
import json

def list_remote_path(path=""):
    url = f"https://api.github.com/repos/fajarsetyadilucky/Retail-Branch-Profitability-Analysis/contents/{path}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            items = json.loads(resp.read().decode())
            for it in items:
                print(f"{it['path']} ({it['type']})")
                if it['type'] == 'dir':
                    list_remote_path(it['path'])
    except Exception as e:
        print(f"Error on {path}: {e}")

list_remote_path("")
