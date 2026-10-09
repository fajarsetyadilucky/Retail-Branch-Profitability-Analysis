import json
import re

with open('save & Clean/projeck_portfolio_1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total cells: {len(nb['cells'])}")
for idx, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        text = ''.join(cell['source'])
        # Look for occurrences of z=, z-score, 42.1, 40.8, 254, 139, 41, 85, etc.
        matches = re.findall(r'(z\s*=\s*[\d,.-]+|z-score[\w\s,.-]+|42[,.]1|40[,.]8|254|139|41[.,]534|85[.,]020|24[,.]7|23[,.]86|23[,.]9)', text, re.IGNORECASE)
        if matches:
            print(f"Cell {idx} (Markdown):")
            for m in matches:
                print(f"  Match: {m}")
            print("  Excerpt:", text[:200].replace('\n', ' '))
            print()
