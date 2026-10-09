import pandas as pd
import numpy as np
import glob
import os

print("="*60)
print("1. AUDITING BIkpi_final.csv")
print("="*60)
df_kpi = pd.read_csv('save & Clean/save/BI/BIkpi_final.csv')
print("Unique months:", df_kpi['month'].unique())
print("Unique branches:", df_kpi['branch_id'].unique())

branch_agg = df_kpi.groupby('branch_id').agg({
    'revenue': 'sum',
    'cogs_used': 'sum',
    'labor_cost': 'sum',
    'rent_cost': 'sum',
    'marketing_cost': 'sum',
    'utilities_cost': 'sum',
    'total_cost': 'sum',
    'net_margin': 'sum'
}).reset_index()

branch_agg['net_margin_pct'] = branch_agg['net_margin'] / branch_agg['revenue'] * 100
branch_agg['food_cost_pct'] = branch_agg['cogs_used'] / branch_agg['revenue'] * 100
branch_agg['labor_cost_pct'] = branch_agg['labor_cost'] / branch_agg['revenue'] * 100
branch_agg['rent_pct'] = branch_agg['rent_cost'] / branch_agg['revenue'] * 100

# Mean and std of net_margin_pct across 10 branches
mean_margin = branch_agg['net_margin_pct'].mean()
std_margin = branch_agg['net_margin_pct'].std(ddof=0) # population or sample?
std_margin_sample = branch_agg['net_margin_pct'].std(ddof=1)

branch_agg['z_score_pop'] = (branch_agg['net_margin_pct'] - mean_margin) / std_margin
branch_agg['z_score_sample'] = (branch_agg['net_margin_pct'] - mean_margin) / std_margin_sample

# Sort by net margin ascending
branch_agg = branch_agg.sort_values('net_margin_pct').reset_index(drop=True)

print("\nBRANCH PERFORMANCE TABLE (Sorted by Net Margin %):")
for idx, r in branch_agg.iterrows():
    print(f"{r['branch_id']}: Rev={r['revenue']:12,.0f} | NetProfit={r['net_margin']:11,.0f} | "
          f"Margin={r['net_margin_pct']:6.2f}% | FC={r['food_cost_pct']:5.2f}% | LC={r['labor_cost_pct']:5.2f}% | "
          f"Rent={r['rent_pct']:5.2f}% | Z_pop={r['z_score_pop']:5.2f} | Z_sample={r['z_score_sample']:5.2f}")

tot_rev = branch_agg['revenue'].sum()
tot_profit = branch_agg['net_margin'].sum()
print("\nNETWORK TOTALS:")
print(f"Total Revenue: {tot_rev:,.0f}")
print(f"Total Net Profit: {tot_profit:,.0f}")
print(f"Weighted Net Margin: {tot_profit/tot_rev*100:.2f}%")
print(f"Unweighted Mean Net Margin: {mean_margin:.2f}%")
print(f"Population Std: {std_margin:.2f}%, Sample Std: {std_margin_sample:.2f}%")

print("\n" + "="*60)
print("2. AUDITING ORDERS DATA (Orders & Items)")
print("="*60)
orders_all = pd.read_csv('save & Clean/save/clean_orders_all.csv')
orders_comp = pd.read_csv('save & Clean/save/clean_orders_completed.csv')
order_items = pd.read_csv('save & Clean/save/clean_order_items.csv')

print(f"clean_orders_all count: {len(orders_all):,}")
print(f"orders status counts:\n{orders_all['order_status'].value_counts()}")
print(f"clean_orders_completed count: {len(orders_comp):,}")
print(f"clean_order_items count: {len(order_items):,}")
void_count = len(orders_all[orders_all['order_status'] == 'void'])
void_rate = void_count / len(orders_all) * 100
print(f"Void Count: {void_count:,} ({void_rate:.2f}%)")

print("\n" + "="*60)
print("3. AUDITING SAVING POTENTIAL (Rp 254 JUTA vs Rp 105 JUTA)")
print("="*60)
# Underperforming branches: BR03, BR05, BR11, BR13
target_cinere = branch_agg[branch_agg['branch_id'] == 'BR09']['net_margin_pct'].values[0] # 40.77%
target_mean = mean_margin # 33.68%
target_weighted = tot_profit / tot_rev * 100 # 33.40%

under = branch_agg[branch_agg['branch_id'].isin(['BR03', 'BR05', 'BR11', 'BR13'])].copy()

print(f"Target Benchmark Cinere (BR09): {target_cinere:.2f}%")
print(f"Target Unweighted Network Mean: {target_mean:.2f}%")
print(f"Target Weighted Network Mean: {target_weighted:.2f}%")

print("\nCalculation if raised to Cinere Benchmark (40.77%):")
for _, r in under.iterrows():
    diff_pct = target_cinere - r['net_margin_pct']
    pot_6m = r['revenue'] * (diff_pct / 100)
    pot_year = pot_6m * 2
    print(f"{r['branch_id']} (Margin {r['net_margin_pct']:.2f}%): +Rp {pot_6m:,.0f} (6 bln) -> +Rp {pot_year:,.0f} / tahun")

tot_pot_cinere_6m = (under['revenue'] * (target_cinere - under['net_margin_pct']) / 100).sum()
print(f"TOTAL Potensi Benchmark Cinere: +Rp {tot_pot_cinere_6m:,.0f} (6 bln) -> +Rp {tot_pot_cinere_6m*2:,.0f} / tahun")

print("\nCalculation if raised to Network Average (33.40%):")
for _, r in under.iterrows():
    diff_pct = target_weighted - r['net_margin_pct']
    pot_6m = r['revenue'] * (diff_pct / 100)
    pot_year = pot_6m * 2
    print(f"{r['branch_id']} (Margin {r['net_margin_pct']:.2f}%): +Rp {pot_6m:,.0f} (6 bln) -> +Rp {pot_year:,.0f} / tahun")

tot_pot_mean_6m = (under['revenue'] * (target_weighted - under['net_margin_pct']) / 100).sum()
print(f"TOTAL Potensi Network Average: +Rp {tot_pot_mean_6m:,.0f} (6 bln) -> +Rp {tot_pot_mean_6m*2:,.0f} / tahun")

print("\n" + "="*60)
print("4. AUDITING BR18 MONTHLY TRAJECTORY")
print("="*60)
br18 = df_kpi[df_kpi['branch_id'] == 'BR18'].sort_values('month')
for _, r in br18.iterrows():
    print(f"BR18 Month {r['month']}: Rev={r['revenue']:,.0f}, Profit={r['net_margin']:,.0f}, Margin%={r['net_margin_pct']:.2f}%, FC%={r['food_cost_pct']:.2f}%, LC%={r['labor_cost_pct']:.2f}%")
