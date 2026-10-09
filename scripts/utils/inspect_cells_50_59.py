import json

with open('save & Clean/projeck_portfolio_1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i in range(50, 60):
    cell = nb['cells'][i]
    print(f"\n==================== CELL {i} ({cell.get('cell_type')}) ====================")
    src = ''.join(cell.get('source', []))
    print(src)
    if cell.get('outputs'):
        for o, out in enumerate(cell['outputs']):
            print(f"--- OUTPUT {o} ---")
            if 'text' in out:
                print(''.join(out['text']))
            elif 'data' in out:
                for k, v in out['data'].items():
                    if k == 'text/plain':
                        print(''.join(v))
