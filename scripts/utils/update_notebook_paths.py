import json
from pathlib import Path

nb_path = Path('notebooks/restaurant_branch_optimization.ipynb')
with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Update Cell 3
cell_3_src = [
    "# Resolusi Path Dataset (fleksibel di Google Colab maupun Lokal)\n",
    "if IN_COLAB:\n",
    "    data_dir = Path('/content/drive/MyDrive/Portfolio Projoject 1')\n",
    "else:\n",
    "    cwd = Path.cwd()\n",
    "    if (cwd / 'data' / 'raw').exists():\n",
    "        data_dir = cwd / 'data' / 'raw'\n",
    "    elif (cwd.parent / 'data' / 'raw').exists():\n",
    "        data_dir = cwd.parent / 'data' / 'raw'\n",
    "    elif (cwd / 'Data mentah').exists():\n",
    "        data_dir = cwd / 'Data mentah'\n",
    "    elif (cwd.parent / 'Data mentah').exists():\n",
    "        data_dir = cwd.parent / 'Data mentah'\n",
    "    else:\n",
    "        data_dir = cwd\n",
    "\n",
    "print('Data directory:', data_dir)\n",
    "branch_master   = pd.read_csv(data_dir / 'branch_master.csv')\n",
    "menu_items      = pd.read_csv(data_dir / 'menu_items.csv')\n",
    "ingredients     = pd.read_csv(data_dir / 'ingredients.csv')\n",
    "recipes         = pd.read_csv(data_dir / 'recipes.csv')\n",
    "suppliers       = pd.read_csv(data_dir / 'suppliers.csv')\n",
    "purchases       = pd.read_csv(data_dir / 'purchases_monthly.csv')\n",
    "inventory       = pd.read_csv(data_dir / 'inventory_monthly.csv')\n",
    "employees       = pd.read_csv(data_dir / 'employees.csv')\n",
    "shifts          = pd.read_csv(data_dir / 'shifts.csv')\n",
    "customers       = pd.read_csv(data_dir / 'customers.csv')\n",
    "orders          = pd.read_csv(data_dir / 'orders.csv')\n",
    "order_items     = pd.read_csv(data_dir / 'order_items.csv')\n",
    "opex_monthly    = pd.read_csv(data_dir / 'opex_monthly.csv')\n"
]
nb['cells'][3]['source'] = cell_3_src

# Update Cell 20
cell_20_src = [
    "# 4. Simpan semua tabel yang sudah bersih sebagai file baru\n",
    "if IN_COLAB:\n",
    "    save_dir = Path('/content/drive/MyDrive/Portfolio Projoject 1/save')\n",
    "else:\n",
    "    cwd = Path.cwd()\n",
    "    if (cwd / 'data' / 'processed').exists():\n",
    "        save_dir = cwd / 'data' / 'processed'\n",
    "    elif (cwd.parent / 'data' / 'processed').exists():\n",
    "        save_dir = cwd.parent / 'data' / 'processed'\n",
    "    else:\n",
    "        save_dir = cwd / 'data' / 'processed'\n",
    "save_dir.mkdir(parents=True, exist_ok=True)\n",
    "\n",
    "branch_master.to_csv(save_dir / 'clean_branch_master.csv', index=False)\n",
    "orders_completed.to_csv(save_dir / 'clean_orders_completed.csv', index=False)\n",
    "orders.to_csv(save_dir / 'clean_orders_all.csv', index=False)  # simpan versi lengkap termasuk Void, untuk hitung Void Rate nanti\n",
    "order_items.to_csv(save_dir / 'clean_order_items.csv', index=False)\n",
    "opex_monthly.to_csv(save_dir / 'clean_opex_monthly.csv', index=False)\n",
    "purchases.to_csv(save_dir / 'clean_purchases.csv', index=False)\n",
    "inventory.to_csv(save_dir / 'clean_inventory.csv', index=False)\n",
    "shifts.to_csv(save_dir / 'clean_shifts.csv', index=False)\n",
    "employees.to_csv(save_dir / 'clean_employees.csv', index=False)\n",
    "customers.to_csv(save_dir / 'clean_customers.csv', index=False)\n",
    "recipes.to_csv(save_dir / 'clean_recipes.csv', index=False)\n",
    "menu_items.to_csv(save_dir / 'clean_menu_items.csv', index=False)\n",
    "ingredients.to_csv(save_dir / 'clean_ingredients.csv', index=False)\n",
    "suppliers.to_csv(save_dir / 'clean_suppliers.csv', index=False)\n",
    "calendar.to_csv(save_dir / 'clean_calendar.csv', index=False)\n",
    "print('Semua tabel bersih berhasil disimpan ke:', save_dir)\n"
]
nb['cells'][20]['source'] = cell_20_src

# Update Cell 48
cell_48_src = [
    "if IN_COLAB:\n",
    "    opex_path = Path('/content/drive/MyDrive/Portfolio Projoject 1/opex_monthly.csv')\n",
    "else:\n",
    "    opex_path = data_dir / 'opex_monthly.csv'\n",
    "\n",
    "opex_monthly = pd.read_csv(opex_path)\n",
    "print(opex_monthly.shape)\n",
    "print(opex_monthly.head())\n",
    "print(opex_monthly.dtypes)\n"
]
nb['cells'][48]['source'] = cell_48_src

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Updated notebooks/restaurant_branch_optimization.ipynb with portable paths!')
