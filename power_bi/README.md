# Microsoft Power BI Desktop Project (.PBIP)
## RANTING Multi-Branch Performance Optimization

Direktori ini berisi proyek resmi **Microsoft Power BI Project (`.pbip`)** untuk visualisasi analitis performa multi-cabang konsorsium restoran RANTING.

---

### 📂 Struktur Direktori Power BI

```
power_bi/
├── Tabs.pbip                     # Berkas Utama Power BI Project (Buka berkas ini di Power BI Desktop)
├── Tabs.Report/                  # Definisi visual, halaman dashboard, dan tata letak UI Power BI
├── Tabs.SemanticModel/           # Model data, arsitektur relasi Star Schema, dan DAX measures
├── datasets/                     # Kumpulan berkas CSV bersih yang menjadi sumber data Power BI
│   ├── BIclean_branch_master.csv
│   ├── BIclean_calendar.csv
│   ├── BIclean_ingredients.csv
│   ├── BIclean_inventory.csv
│   ├── BIclean_menu_items.csv
│   ├── BIclean_orders_all.csv
│   ├── BIclean_purchases.csv
│   ├── BIclean_suppliers.csv
│   └── BIkpi_final.csv
└── README.md                     # Panduan penggunaan proyek Power BI
```

---

### 🚀 Cara Membuka Proyek di Power BI Desktop

1. Pastikan Anda telah menginstal **Microsoft Power BI Desktop** versi terbaru.
2. Aktifkan fitur pratinjau **Power BI Project (.pbip)** jika diperlukan di menu:
   `File > Options and settings > Options > Preview features > Power BI Project (.pbip) save option`.
3. Buka berkas `Tabs.pbip` langsung dari folder ini.
4. Power BI akan otomatis memuat seluruh laporan (3 Halaman Utama: *Overview Performa*, *Root Cause Diagnostic*, dan *Ramp-Up Cabang Baru*) beserta model semantiknya.

---

### 📊 Halaman Dashboard yang Tersedia

1. **Page 1: Executive Overview Dashboard**
   - KPI Summary Cards: Gross Revenue (Rp 4,89 Miliar), Food Cost % (29,5%), Labor Cost % (20,3%), Net Margin % (33,8%), Void Rate (4,1%).
   - Ranking Net Margin 18 Cabang Jabodetabek (Cinere 40,8% s/d Kelapa Gading 23,9%).
   - Pemetaan Klaster Cabang Sehat (13 gerai) vs Cabang Bermasalah (4 gerai).

2. **Page 2: Diagnostic & Root-Cause Matrix**
   - Scatter Plot Z-Score Sourcing vs Z-Score Waste Dapur.
   - Analisis Disparitas Biaya Tenaga Kerja (Labor Z-Score BR03 = +8,3).
   - Pemetaan Akar Masalah: Inefisiensi Ganda (BSD & Tangerang) vs Murni Vendor (Sentul).

3. **Page 3: New Branch Ramp-Up Curve (BR18)**
   - Lintasan Pertumbuhan Margin Bulanan Summarecon Bekasi (19,9% ➔ 23,5% ➔ 27,4% ➔ 29,1%).
   - Perbandingan Kurva Usia Operasional (*Age-Adjusted Revenue per Day*).
   - Keputusan Analitis: *Healthy Ramp-Up Curve / Do Not Intervene*.
