# 🍽️ RANTING Multi-Branch F&B Performance Optimization
### Business Intelligence, Statistical Root-Cause Analysis & Executive Decision Support

[![Power BI](https://img.shields.io/badge/Power_BI-Desktop_PBIP-F2C811?logo=powerbi&logoColor=black)](power_bi/)
[![Python](https://img.shields.io/badge/Python-3.14_Pandas_NumPy-3776AB?logo=python&logoColor=white)](notebooks/)
[![LinkedIn Carousel](https://img.shields.io/badge/LinkedIn-Carousel_PDF_(10_Slides)-0A66C2?logo=linkedin&logoColor=white)](LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf)
[![Documentation](https://img.shields.io/badge/Documentation-5_Core_Docs-success)](docs/)

---

## 📌 Executive Summary

Pada industri restoran multi-cabang (F&B retail), manajemen sering kali terjebak dalam **"Ilusi Omzet"**: restoran tampak selalu ramai pelanggan dengan omzet mencapai miliaran rupiah, tetapi laba bersih di tingkat cabang menguap tanpa jejak. Reaksi spontan manajemen saat laba tertekan biasanya adalah memukul rata: *"Potong anggaran belanja dan operasional seluruh cabang secara seragam!"*

Proyek ini membuktikan melalui **Business Intelligence Architecture (Power BI)** dan **Pengujian Statistik Z-Score (Python)** bahwa 4 gerai yang mengalami penurunan margin keuntungan ternyata mengidap **3 penyakit operasional yang berbeda total**, sehingga memerlukan intervensi presisi yang berbeda pula:

1. **Kelapa Gading (BR03) — 100% Masalah Tenaga Kerja:** Margin 23,9% (terendah di jaringan). Dapur dan harga beli bahan baku normal, namun rasio biaya gaji menyedot 30,5% revenue ($Z_{\text{Labor}} = +8,3$). Terbukti mengalami *overstaffing* struktural.
2. **BSD (BR05) & Tangerang (BR11) — Inefisiensi Ganda:** Margin BSD anjlok ke 28,1% akibat dua kebocoran simultan: harga beli bahan baku 24% di atas harga pasar wajar ($Z_{\text{Sourcing}} = +27,7$) dan tingkat bahan terbuang di dapur tertinggi di jaringan ($5,6\%, Z_{\text{Waste}} = +24,6$).
3. **Sentul (BR13) — Murni Masalah Vendor Sourcing:** Margin 32,3% murni akibat markup harga supplier ($Z_{\text{Sourcing}} = +10,7$). Operasional dapur terbukti sangat disiplin dengan tingkat waste rendah ($Z_{\text{Waste}} = +1,8$). Solusinya adalah negosiasi kontrak, bukan audit dapur.
4. **Summarecon Bekasi (BR18) — Paradoks Cabang Baru:** Margin rata-rata 25,0% dan rasio staf awal yang tinggi sempat dicap "bermasalah". Analisis membuktikan ini adalah kurva pertumbuhan alami (*healthy ramp-up curve*, naik dari 19,9% ke 29,1% dalam 4 bulan). Putusan analis: **DO NOT INTERVENE!**

> 💰 **Dampak Finansial Nyata:** Dengan mereplikasi SOP dari cabang acuan terbaik (**RANTING - Cinere / BR09**, Net Margin 40,8%, $Z = +4,3$) dan menerapkan Roadmap Taktis 30 Hari, konsorsium dapat memulihkan potensi laba bersih **~Rp 254.000.000 per tahun** (dengan baseline konservatif rata-rata jaringan Rp 105–111 Juta/tahun) tanpa perlu menambah cabang baru atau membakar biaya promosi.

---

## 📊 Metrik Utama Konsorsium (April – September 2026)

| Parameter Metrik | Nilai Aktual Konsolidasi | Keterangan & Dasar Pembuktian |
| :--- | :--- | :--- |
| **Gross Revenue** | **Rp 4.894.946.000** (~Rp 4,89 Miliar) | Akumulasi 170.546 baris transaksi item pesanan |
| **Total Pesanan (Orders)** | **85.020 Transaksi** | 81.560 Completed & 3.460 Void |
| **Order Void Rate** | **4,1%** (4,07%) | Indikator integritas kasir dan operasional kasir |
| **Rata-rata Net Margin** | **33,8%** (Weighted) | 13 cabang stabil mengelompok di 34% – 37% |
| **Food Cost (COGS)** | **Rp 1.444.165.138** (29,5%) | Agregat bahan baku teoritis resep POS |
| **Labor Cost (Gaji)** | **Rp 991.584.200** (20,3%) | Jam kerja shift terkalibrasi per cabang |
| **Cabang Terbaik (Benchmark)** | **BR09 - Cinere (40,8%)** | Unggul simultan di Sourcing, Waste, dan Staffing |
| **Cabang Terendah** | **BR03 - Kelapa Gading (23,9%)** | Terpaut disparitas 16,9% di bawah Cinere |
| **Potensi Dividen Pemulihan** | **~Rp 254 Juta / Tahun** | Target pemulihan 4 cabang ke Benchmark Cinere |

---

## 🏛️ Arsitektur Tatakelola Direktori Repositori

Repositori ini telah distrukturisasi dengan standar tata kelola profesional (*industry-standard data analytics repository*):

```
Portfolio Project 1/
│
├── README.md                               <-- Panduan Utama Repositori & Dokumentasi Portofolio
├── LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf  <-- Dokumen Carousel PDF LinkedIn (10 Slide Emas 4:5)
│
├── data/
│   ├── raw/                                <-- 11 file CSV data mentah asli (orders, shifts, inventory, opex, etc.)
│   └── processed/                          <-- Dataset bersih (clean_orders_all.csv, clean_order_items.csv, BIkpi_final.csv, etc.)
│
├── notebooks/
│   └── restaurant_branch_optimization.ipynb <-- Notebook Jupyter Python (ETL, Cleaning, Uji Signifikansi & Z-Score)
│
├── power_bi/
│   ├── Tabs.pbip                           <-- Berkas Utama Microsoft Power BI Desktop Project
│   ├── Tabs.Report/                        <-- Tata letak kanvas, visualisasi interaktif, dan halaman dashboard
│   ├── Tabs.SemanticModel/                 <-- Arsitektur data Star Schema dan DAX measures
│   ├── datasets/                           <-- Dataset acuan lokal Power BI (BIclean_*.csv & BIkpi_final.csv)
│   └── README.md                           <-- Petunjuk teknis membuka dan eksplorasi dashboard Power BI
│
├── docs/                                   <-- Dokumentasi Formal & Metodologi Analisis
│   ├── 01_business_brief_kpi.md            <-- Brief Stakeholder (Dimas Pratama), Problem Framing, 7 KPI F&B
│   ├── 02_data_cleaning_log.md             <-- Log 8 tahap pembersihan data (missing, duplicates, orphan audit)
│   ├── 03_root_cause_analysis.md           <-- Matriks pengujian statistik Z-Score gabungan seluruh cabang
│   ├── 04_executive_recommendations.md     <-- Rekomendasi taktis, model penyelamatan laba Rp 254 Jt, roadmap 30 hari
│   ├── 05_final_findings_report.md         <-- Laporan narasi eksekutif final ke Head of Operations & Owner
│   ├── README.md                           <-- Indeks dan panduan membaca seluruh dokumentasi
│   └── notes/                              -- Catatan riset pendukung (labor cost, net margin, food cost, tren)
│
├── reports/                                <-- Deliverables Eksekutif & Presentasi LinkedIn
│   ├── LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf  <-- Dokumen Carousel PDF (1080×1350 px, rasio 4:5)
│   ├── LINKEDIN_POST_COPY.md                        <-- Copywriting caption postingan LinkedIn siap publikasi
│   ├── CAROUSEL_AUDIT_EVALUATION_REPORT.md          <-- Laporan evaluasi menyeluruh 360° (Storyline, Angka, PUEBI)
│   ├── linkedin_carousel_preview.html               <-- Pratinjau interaktif web browser untuk semua slide
│   ├── carousel_slides/                             <-- 10 Slide gambar PNG resolusi tinggi (slide_01 s/d slide_10)
│   └── figures/                                     <-- Tangkapan layar Power BI & foto profil author
│
├── scripts/                                <-- Skrip Otomasi Python
│   ├── generate_linkedin_carousel.py       <-- Generator otomatis PDF, PNG slides, pratinjau HTML & copywriting
│   └── utils/                              <-- Skrip audit konsistensi data & verifikasi koding
│
└── _archive/                               <-- Arsip Berkas Riwayat & Cadangan
    ├── legacy_data_mentah/                 <-- Berkas data mentah awal
    ├── legacy_save_and_clean/              <-- Berkas kerja draf lama
    ├── duplicate_copies/                   <-- Salinan duplikat ('Copy of...') dan duplikasi folder lama
    └── backup_notebooks/                   <-- Berkas backup notebook (.bak)
```

---

## 📈 Dashboard Power BI (Overview & Preview)

Dashboard interaktif dibangun di **Power BI Desktop** menggunakan arsitektur relasi **Star Schema (1:N)** antara dimensi (`Dim_Branch`, `Dim_Calendar`, `Dim_Menu`, `Dim_Ingredient`, `Dim_Supplier`) dan tabel fakta (`Fact_Orders`, `Fact_Order_Items`, `Fact_Purchases`, `Fact_Inventory`, `Fact_Shifts`, `Fact_Opex`):

- **Halaman 1 (Executive Overview):** Pemantauan KPI omzet, persentase biaya, dan ranking margin 18 cabang dengan *conditional formatting*.
- **Halaman 2 (Root-Cause Matrix):** Scatter plot interaktif korelasi Z-Score Sourcing vs Waste Dapur dan disparitas beban tenaga kerja.
- **Halaman 3 (New Branch Ramp-Up Curve):** Normalisasi kurva pertumbuhan margin bulanan BR18 untuk membedakan cabang baru dari cabang bermasalah.

Akses proyek langsung di folder [`power_bi/`](power_bi/).

---

## 📑 LinkedIn Document Carousel (10 Slide)

Dokumen Carousel LinkedIn telah dirancang dengan standar rasio **4:5 Emas (1080 × 1350 px)** tanpa *scroll* vertikal, tema *executive dark-mode*, dan tipografi *Plus Jakarta Sans*:

1. **Slide 01:** *The Paradox Hook* — Omzet Rp 4,89 Miliar vs Kebocoran Laba Rp 254 Juta di Bawah Radar.
2. **Slide 02:** *Ilusi Margin Rata-Rata* — Snapshot Dashboard Power BI & Disparitas 23,9% vs 40,8%.
3. **Slide 03:** *Jebakan Diagnosa Seragam* — 4 Cabang Kritis dengan 3 Akar Masalah Berbeda.
4. **Slide 04:** *Pembuktian Statistik Z-Score* — Uji Signifikansi Standard Error Biaya Tenaga Kerja & Bahan Baku.
5. **Slide 05:** *Paradoks Cabang Baru (BR18)* — Kurva Pertumbuhan Sehat (*Healthy Ramp-Up Curve*).
6. **Slide 06:** *The Golden Benchmark (Cinere Model)* — Keunggulan Simultan Sourcing, Waste, dan Staffing.
7. **Slide 07:** *Value Creation Model* — Rekalkulasi Dividen Penyelamatan Laba **~Rp 254 Juta / Tahun**.
8. **Slide 08:** *Roadmap Taktis 30 Hari* — Sprint 4 Minggu Tanpa Mengganggu Operasional Harian.
9. **Slide 09:** *Fondasi Data Engineering* — Star Schema 1:N, Pipeline Pembersihan Data, & DAX Measures.
10. **Slide 10:** *Open-Source Codebase & Call to Action* — Undangan Diskusi & Peluang Kolaborasi.

👉 Unduh atau tinjau langsung PDF Carousel: [LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf)  
👉 Naskah Copywriting LinkedIn: [reports/LINKEDIN_POST_COPY.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/reports/LINKEDIN_POST_COPY.md)  
👉 Galeri Slide PNG: [reports/carousel_slides/](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/reports/carousel_slides/)

---

## 👨‍💻 Profil Author & Kontak

**Fajar Setyadi**  
*Data Analyst & Business Intelligence Specialist*  
- 📧 Email: [Fajarsetyadilucky@gmail.com](mailto:Fajarsetyadilucky@gmail.com)  
- 💬 WhatsApp: [+62 896-3052-7099](https://wa.me/6289630527099)  
- 💻 GitHub: [github.com/fajarsetyadilucky](https://github.com/fajarsetyadilucky/Portfolio_Restaurant_Branch_Optimization)  

*Terbuka untuk diskusi teknis, evaluasi proyek portofolio, dan peluang karir di bidang Data Analytics / Business Intelligence.*
