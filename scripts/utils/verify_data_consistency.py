import pandas as pd

items = pd.read_csv('save & Clean/save/clean_order_items.csv')
print("Order items columns:", items.columns.tolist())
print(items.head(2))

orders_comp = pd.read_csv('save & Clean/save/clean_orders_completed.csv')
print("Orders completed columns:", orders_comp.columns.tolist())
print(orders_comp.head(2))

kpi = pd.read_csv('save & Clean/save/BI/BIkpi_final.csv')
price_col = [c for c in items.columns if 'price' in c.lower() or 'subtotal' in c.lower() or 'total' in c.lower()][0]
qty_col = 'quantity'
comp_ids = set(orders_comp['order_id'])
comp_items = items[items['order_id'].isin(comp_ids)]
rev_items = (comp_items[qty_col] * comp_items[price_col]).sum()
print(f"\nCalculated Rev from items: Rp {rev_items:,.0f}")
print(f"Total Rev in BIkpi_final:  Rp {kpi['revenue'].sum():,.0f}")
print(f"Difference: Rp {kpi['revenue'].sum() - rev_items:,.0f}")
