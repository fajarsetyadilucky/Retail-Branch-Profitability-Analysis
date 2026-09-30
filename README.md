# Retail-Branch-Profitability-Analysis
End-to-end retail branch profitability analysis: Python data cleaning, statistical significance testing (z-score) for root cause identification, and an interactive Power BI dashboard. Simulated case study across 18 branches with an estimated IDR 254M/year financial impact.
Retail Branch Profitability Analysis
End-to-end data analysis project simulating the full workflow of a Data Analyst/BI role: from messy raw data to a statistically validated, executive-ready recommendation.
Tools: Python (Pandas, NumPy) · SQL (DuckDB) · Power BI (DAX, Power Query) · Statistical Testing (Z-score, Standard Error)
---
Background
This project simulates a real analyst assignment for RANTING, a fictional F&B chain with 18 branches across Jabodetabek, Indonesia. The Head of Operations, two months into the role, needed answers to three business questions:
Which branches look busy but have thin margins, and why?
Is the newest branch underperforming, or is it simply still ramping up?
Which branch is the most profitable, and can its practices be replicated?
The dataset is synthetic, generated to mirror the imperfections of real operational data (inconsistent formatting, missing values with genuine business meaning, transactional noise) to practice a realistic cleaning and validation process rather than working with a pre-cleaned dataset.
Workflow
1. Data Cleaning & Validation (Python, Google Colab)
Full data quality audit across 12+ relational tables: missing values, text formatting inconsistencies, duplicates, and referential integrity checks. Every cleaning decision is logged with its rationale, for example, distinguishing between missing values that are data errors (imputed) versus missing values that carry genuine business meaning (deliberately left as-is).
2. Data Modeling
Star schema design: fact tables (orders, purchases, shifts) and dimension tables (branch, menu, ingredient, employee, customer), with a dedicated date table for time intelligence.
3. KPI Calculation & Root Cause Analysis (Python, SQL via DuckDB)
Core KPIs: Food Cost %, Labor Cost %, Net Margin %, Waste %, Sourcing Cost Ratio, Void Rate. Every flagged branch was tested for statistical significance (Z-score against standard error) before being labeled as a genuine issue, separating real structural problems from ordinary monthly variance.
4. Dashboard (Power BI, DAX)
A 3-page interactive report: Performance Overview, New Branch Analysis, and Root Cause Detail, with conditional formatting that surfaces priority branches at a glance.
Key Findings
Network-wide average net margin: 33.8%, food cost 29.5%, labor cost 20.3%, order void rate 4.1%, on total revenue of IDR 4.89 billion over 6 months.
4 of 18 branches show a statistically significant margin gap below the network average, each with a distinct root cause:
One branch: overstaffing (labor cost issue only)
Two branches: above-market ingredient sourcing costs combined with high kitchen waste
One branch: sourcing cost issue only, kitchen operations are normal
1 branch significantly outperforms on every metric (sourcing, waste, labor, margin) and is recommended as the internal best-practice benchmark.
The newest branch (opened mid-analysis period) shows a healthy, consistent ramp-up curve and was explicitly excluded from the "underperforming" category, a key distinction requested in the original business brief.
Estimated financial impact if the 4 underperforming branches are left unaddressed: ~IDR 254 million/year.
Dashboard Preview
![Overview](screenshots/01-overview.png)
![New Branch Analysis](screenshots/02-cabang-baru.png)
![Root Cause Detail](screenshots/03-root-cause.png)
Repository Structure
```
├── data/            Cleaned CSV datasets (branch, orders, purchases, inventory, etc.)
├── notebooks/        Google Colab notebook: cleaning, KPI calculation, statistical testing
├── dashboard/        Power BI (.pbix) file
├── docs/              Methodology notes and the final executive recommendation report
└── screenshots/       Dashboard page exports (PNG)
```
Methodology Notes
Statistical significance was assessed using Z-scores derived from standard error, not raw ranking. A branch is only labeled "problematic" if its deviation from the network mean exceeds a 2-standard-error threshold.
Net Margin here refers to branch-level contribution margin (revenue minus cost of goods sold, labor, rent, marketing, and utilities), and does not include head-office overhead or tax, which is disclosed explicitly to avoid overstating the figure as final net profit.
Full methodology, data-cleaning decision log, and the complete executive recommendation are available in `/docs`.
Disclaimer
The company, branch names, and dataset in this project are entirely fictional and were generated for educational and portfolio purposes. The analytical methodology, statistical rigor, and tooling demonstrated are directly transferable to real business data.
---
Author: Fajar Setyadi · Data Analyst / BI Analyst
www.linkedin.com/in/fajar-setyadi-23abb8293 · Fajarsetyadilucky@gmail.com
