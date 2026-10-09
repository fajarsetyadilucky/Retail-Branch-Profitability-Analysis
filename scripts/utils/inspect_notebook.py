import json

with open('save & Clean/projeck_portfolio_1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells in notebook: {len(nb['cells'])}")
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    if any(k in src.lower() for k in ['z_score', 'zscore', 'br03', 'br09', 'potensi', '254', '40.8', 'cinere']):
        print(f"\n--- Cell {i} ({cell.get('cell_type')}) ---")
        lines = src.split('\n')
        for line in lines[:8]:
            print("  [SRC]", line)
        if len(lines) > 8:
            print("  [SRC] ...")
        if cell.get('outputs'):
            for out in cell['outputs']:
                if 'text' in out:
                    out_text = ''.join(out['text'])
                    for oline in out_text.split('\n')[:8]:
                        print("  [OUT]", oline)
