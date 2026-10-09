import os
import shutil
from pathlib import Path

ROOT = Path(".").resolve()
print(f"Working in workspace: {ROOT}")

# Define Target Directories
DIRS = [
    ROOT / "data" / "raw",
    ROOT / "data" / "processed",
    ROOT / "notebooks",
    ROOT / "power_bi",
    ROOT / "power_bi" / "datasets",
    ROOT / "docs",
    ROOT / "docs" / "notes",
    ROOT / "reports",
    ROOT / "scripts" / "utils",
    ROOT / "_archive" / "old_save_and_clean",
    ROOT / "_archive" / "duplicate_copies",
    ROOT / "_archive" / "backup_notebooks",
]

for d in DIRS:
    d.mkdir(parents=True, exist_ok=True)
print("Created target directories successfully.")

# 1. DATA RAW (from 'Data mentah')
raw_src = ROOT / "Data mentah"
if raw_src.exists():
    for f in raw_src.glob("*.csv"):
        shutil.copy2(f, ROOT / "data" / "raw" / f.name)
        print(f"Copied raw: {f.name} -> data/raw/")

# 2. DATA PROCESSED (from 'save & Clean/save')
save_src = ROOT / "save & Clean" / "save"
if save_src.exists():
    for f in save_src.glob("clean_*.csv"):
        shutil.copy2(f, ROOT / "data" / "processed" / f.name)
        print(f"Copied processed: {f.name} -> data/processed/")

# Also copy BIclean_*.csv and BIkpi_final.csv to data/processed
bi_csv_src = ROOT / "save & Clean" / "save" / "BI"
if bi_csv_src.exists():
    for f in bi_csv_src.glob("BI*.csv"):
        shutil.copy2(f, ROOT / "data" / "processed" / f.name)
        print(f"Copied processed BI: {f.name} -> data/processed/")

# 3. POWER BI PROJECT
if bi_csv_src.exists():
    # Copy Tabs.pbip
    pbip_file = bi_csv_src / "Tabs.pbip"
    if pbip_file.exists():
        shutil.copy2(pbip_file, ROOT / "power_bi" / "Tabs.pbip")
        print("Copied Tabs.pbip -> power_bi/")
    
    # Copy Tabs.Report and Tabs.SemanticModel
    for folder_name in ["Tabs.Report", "Tabs.SemanticModel"]:
        src_folder = bi_csv_src / folder_name
        dest_folder = ROOT / "power_bi" / folder_name
        if src_folder.exists():
            if dest_folder.exists():
                shutil.rmtree(dest_folder)
            shutil.copytree(src_folder, dest_folder)
            print(f"Copied {folder_name} -> power_bi/")
            
    # Copy BIclean_*.csv & BIkpi_final.csv directly to power_bi/ and power_bi/datasets/
    for f in bi_csv_src.glob("BI*.csv"):
        shutil.copy2(f, ROOT / "power_bi" / f.name)
        shutil.copy2(f, ROOT / "power_bi" / "datasets" / f.name)
    print("Copied BI datasets -> power_bi/ and power_bi/datasets/")

# 4. NOTEBOOKS
nb_src = ROOT / "save & Clean" / "projeck_portfolio_1.ipynb"
if nb_src.exists():
    shutil.copy2(nb_src, ROOT / "notebooks" / "restaurant_branch_optimization.ipynb")
    print("Copied notebook -> notebooks/restaurant_branch_optimization.ipynb")

# 5. STRUCTURED DOCS
# Core documents (01 to 05)
doc_mappings = [
    (ROOT / "save & Clean" / "save" / "BI" / "Document" / "1. Business Brief and KPI Definition.md", ROOT / "docs" / "01_business_brief_kpi.md"),
    (ROOT / "save & Clean" / "save" / "BI" / "Document" / "2. Data Cleaning log.md", ROOT / "docs" / "02_data_cleaning_log.md"),
    (ROOT / "save & Clean" / "save" / "BI" / "Document" / "3. Root-Cause Analysis.md", ROOT / "docs" / "03_root_cause_analysis.md"),
    (ROOT / "save & Clean" / "save" / "BI" / "Document" / "4. Executive Recommendation.md", ROOT / "docs" / "04_executive_recommendations.md"),
    (ROOT / "save & Clean" / "laporan-temuan-final-ranting.md", ROOT / "docs" / "05_final_findings_report.md"),
]

for src, dst in doc_mappings:
    if src.exists():
        shutil.copy2(src, dst)
        print(f"Copied doc: {src.name} -> {dst.relative_to(ROOT)}")

# Notes documents
note_mappings = [
    (ROOT / "save & Clean" / "catatan-labor-cost-signifikansi.md", ROOT / "docs" / "notes" / "labor_cost_significance.md"),
    (ROOT / "save & Clean" / "catatan-net-margin-interpretasi.md", ROOT / "docs" / "notes" / "net_margin_interpretation.md"),
    (ROOT / "Data mentah" / "rekomendasi-food-cost-ranting.md", ROOT / "docs" / "notes" / "food_cost_recommendations.md"),
    (ROOT / "save & Clean" / "penjelasan-tren-margin-owner.md", ROOT / "docs" / "notes" / "monthly_margin_trends.md"),
    (ROOT / "Data mentah" / "roadmap-pengerjaan-ranting.md", ROOT / "docs" / "notes" / "project_roadmap.md"),
    (ROOT / "save & Clean" / "catatan-ringkasan-tindak-lanjut.md", ROOT / "docs" / "notes" / "action_items_summary.md"),
]

for src, dst in note_mappings:
    if src.exists():
        shutil.copy2(src, dst)
        print(f"Copied note: {src.name} -> {dst.relative_to(ROOT)}")

# 6. ARCHIVE DUPLICATES & OLD BACKUPS
# Copy of BIclean...
if save_src.exists():
    for f in save_src.glob("Copy of *.csv"):
        shutil.move(str(f), str(ROOT / "_archive" / "duplicate_copies" / f.name))
        print(f"Archived duplicate: {f.name}")

# .bak notebook
bak_nb = ROOT / "save & Clean" / "projeck_portfolio_1.ipynb.bak"
if bak_nb.exists():
    shutil.move(str(bak_nb), str(ROOT / "_archive" / "backup_notebooks" / bak_nb.name))
    print("Archived backup notebook.")

# Older root cause draft
old_rc = ROOT / "save & Clean" / "catatan-root-cause-final.md"
if old_rc.exists():
    shutil.copy2(old_rc, ROOT / "_archive" / "old_save_and_clean" / old_rc.name)
old_rc1 = ROOT / "save & Clean" / "catatan-root-cause-final (1).md"
if old_rc1.exists():
    shutil.copy2(old_rc1, ROOT / "_archive" / "old_save_and_clean" / old_rc1.name)

# Root redundant BI/BI folder
root_bi = ROOT / "BI"
if root_bi.exists():
    archive_bi = ROOT / "_archive" / "duplicate_copies" / "BI_root"
    if archive_bi.exists():
        shutil.rmtree(archive_bi)
    shutil.move(str(root_bi), str(archive_bi))
    print("Archived redundant root BI folder.")

# Helper utility scripts
script_utils = [
    "audit_code_vs_markdown.py",
    "inspect_cells_50_59.py",
    "inspect_notebook.py",
    "list_md_files.py",
    "scan_notebook_markdown.py",
    "update_audit_report.py",
    "update_cell_55.py",
    "verify_data_consistency.py",
]
for s in script_utils:
    p = ROOT / "scripts" / s
    if p.exists():
        shutil.move(str(p), str(ROOT / "scripts" / "utils" / s))
        print(f"Moved utility script: {s} -> scripts/utils/")

print("\nReorganization script executed successfully!")
