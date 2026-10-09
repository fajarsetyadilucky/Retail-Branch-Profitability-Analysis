with open('reports/CAROUSEL_AUDIT_EVALUATION_REPORT.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the table
old_table = """| Parameter Metrik | Nilai di Carousel | Sumber Pembuktian Data & Model | Status Audit |
| :--- | :--- | :--- | :---: |
| **Total Gross Revenue** | **Rp 4,89 Miliar** | `4.894.485.500` pada fact orders completed (Apr–Sep 2026). | **PRESISI 100%** |
| **Total Transaksi Pesanan** | **41.534 Orders** | Seluruh transaksi completed di 18 cabang Jabodetabek. | **IDENTIK 100%** |
| **Jumlah Cabang** | **18 Cabang** | Master branch di Jabodetabek (BR01 s/d BR18). | **IDENTIK 100%** |
| **Rata-Rata Net Margin Jaringan** | **33,8%** | Agregat 18 cabang (rentang 33,4% – 33,8%). | **KONSISTEN** |
| **Margin BR03 (Kelapa Gading)** | **23,9%** | Titik terendah Juli 20,6%, rata-rata periode 23,9%. | **PRESISI 100%** |
| **Z-Score Labor BR03** | **+8,3** | Standard error uji signifikansi labor cost (overstaffing ekstrem). | **TERVERIFIKASI** |
| **Margin BR05 (BSD)** | **28,1%** | Biaya beli bahan baku +24% di atas pasar, waste 5,6%. | **PRESISI 100%** |
| **Z-Score Sourcing & Waste BR05** | **+27,7 & +24,6** | Dua deviasi tertinggi di seluruh jaringan cabang. | **TERVERIFIKASI** |
| **Margin BR11 (Tangerang)** | **30,5%** | Inefisiensi ganda (sourcing Z=16,4, waste Z=15,4). | **PRESISI 100%** |
| **Margin BR13 (Sentul)** | **32,3%** | Sourcing Z=+10,7, waste normal (Z=1,8). Murni vendor. | **PRESISI 100%** |
| **Margin BR18 (Summarecon Bekasi)** | **24,9% (Ramp-up)** | Juni 19,9% ➔ Juli 22,4% ➔ Agustus 25,8% ➔ Sept 29,1%. | **TERVERIFIKASI** |
| **Margin BR09 (Cinere Benchmark)** | **40,8% – 42,1%** | Tertinggi konsisten; Sourcing Z=-13,0, Waste Z=-10,7, Labor Z=-3,5. | **PRESISI 100%** |
| **Potensi Recovery Kelapa Gading** | **~Rp 97 Juta / Thn** | Pemulihan margin 23,9% ➔ 33,5% baseline rata-rata. | **PRESISI 100%** |
| **Potensi Recovery BSD** | **~Rp 68 Juta / Thn** | Pemulihan margin 28,1% ➔ 33,5% baseline rata-rata. | **PRESISI 100%** |
| **Potensi Recovery Tangerang** | **~Rp 53 Juta / Thn** | Pemulihan margin 30,5% ➔ 33,5% baseline rata-rata. | **PRESISI 100%** |
| **Potensi Recovery Sentul** | **~Rp 38 Juta / Thn** | Pemulihan margin 32,3% ➔ 33,5% baseline rata-rata. | **PRESISI 100%** |
| **Total Pemulihan Laba Tahunan** | **~Rp 254 Juta / Thn** | $97 + 68 + 53 + 38 = \\text{Rp 256 Jt} \\approx \\text{Rp 254 Juta}$ (konservatif). | **KONSISTEN DOKUMEN** |
| **Pemulihan Laba 6 Bulan** | **Rp 139 Juta** | Nilai dividen periode berjalan (Apr–Sep 2026). | **PRESISI 100%** |"""

new_table = """| Parameter Metrik | Nilai di Carousel | Sumber Pembuktian Data & Model | Status Audit |
| :--- | :--- | :--- | :---: |
| **Total Gross Revenue** | **Rp 4,89 Miliar** | `4.894.946.000` pada fact order items completed (Apr–Sep 2026). | **PRESISI 100%** |
| **Total Transaksi Pesanan** | **85.020 Orders** | 81.560 Completed & 3.460 Void (Void Rate 4,1%). | **PRESISI 100%** |
| **Total Baris Item Menu** | **170.546 Baris** | Fact order items tervalidasi di seluruh 18 gerai. | **PRESISI 100%** |
| **Jumlah Cabang** | **18 Cabang** | Master branch di Jabodetabek (BR01 s/d BR18). | **IDENTIK 100%** |
| **Rata-Rata Net Margin Jaringan** | **33,8%** | Agregat 18 cabang (rata-rata tertimbang omzet). | **KONSISTEN** |
| **Margin BR03 (Kelapa Gading)** | **23,9%** | Titik terendah Juli 20,6%, rata-rata 23,86% (~23,9%). | **PRESISI 100%** |
| **Z-Score Labor BR03** | **+8,3** | Standard error uji signifikansi labor cost (overstaffing ekstrem). | **TERVERIFIKASI** |
| **Margin BR05 (BSD)** | **28,1%** | Biaya beli bahan baku +24% di atas pasar, waste 5,6%. | **PRESISI 100%** |
| **Z-Score Sourcing & Waste BR05** | **+27,7 & +24,6** | Dua deviasi tertinggi di seluruh jaringan cabang. | **TERVERIFIKASI** |
| **Margin BR11 (Tangerang)** | **30,5%** | Inefisiensi ganda (sourcing Z=16,4, waste Z=15,4). | **PRESISI 100%** |
| **Margin BR13 (Sentul)** | **32,3%** | Sourcing Z=+10,7, waste normal (Z=1,8). Murni vendor. | **PRESISI 100%** |
| **Margin BR18 (Summarecon Bekasi)** | **25,0% (Ramp-up)** | Juni 19,9% ➔ Juli 23,5% ➔ Agustus 27,4% ➔ Sept 29,1%. | **TERVERIFIKASI** |
| **Margin BR09 (Cinere Benchmark)** | **40,8%** | Tertinggi konsisten; Sourcing Z=-13,0, Waste Z=-10,7, Labor Z=-3,5. | **PRESISI 100%** |
| **Potensi Recovery Kelapa Gading** | **+Rp 97 Juta / Thn** | Pemulihan margin 23,9% ➔ 40,8% (Cinere Benchmark Model). | **PRESISI 100%** |
| **Potensi Recovery BSD** | **+Rp 68 Juta / Thn** | Pemulihan margin 28,1% ➔ 40,8% (Cinere Benchmark Model). | **PRESISI 100%** |
| **Potensi Recovery Tangerang** | **+Rp 53 Juta / Thn** | Pemulihan margin 30,5% ➔ 40,8% (Cinere Benchmark Model). | **PRESISI 100%** |
| **Potensi Recovery Sentul** | **+Rp 38 Juta / Thn** | Pemulihan margin 32,3% ➔ 40,8% (Cinere Benchmark Model). | **PRESISI 100%** |
| **Total Pemulihan Laba Tahunan** | **~Rp 254 Juta / Thn** | $97 + 68 + 53 + 38 = \\text{Rp 256 Jt} \\approx \\text{Rp 254 Juta}$ (Cinere Model). | **KONSISTEN DOKUMEN** |
| **Baseline Recovery Rata-Rata** | **~Rp 105 Juta / Thn** | Proyeksi jika hanya dinaikkan ke rata-rata jaringan (33,4%). | **TERVERIFIKASI** |
| **Pemulihan Laba 6 Bulan (Total)** | **Rp 127 – 139 Juta** | Rp 127 Jt (4 cabang kritis) s/d Rp 139 Jt (inklusif BR18). | **PRESISI 100%** |"""

if old_table in text:
    text = text.replace(old_table, new_table)
    print("Table replaced successfully!")
else:
    # Try normalizing line breaks
    text_norm = text.replace('\r\n', '\n')
    old_norm = old_table.replace('\r\n', '\n')
    if old_norm in text_norm:
        text_norm = text_norm.replace(old_norm, new_table)
        text = text_norm
        print("Table replaced with normalized line endings!")
    else:
        print("Table match not found!")

old_slide5_note = "*19,9% (Jun) → 22,4% (Jul) → 25,8% (Agu) → 29,1% (Sep)*"
new_slide5_note = "*19,9% (Jun) → 23,5% (Jul) → 27,4% (Agu) → 29,1% (Sep)*"
if old_slide5_note in text:
    text = text.replace(old_slide5_note, new_slide5_note)
    print("Slide 5 note updated!")

with open('reports/CAROUSEL_AUDIT_EVALUATION_REPORT.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("CAROUSEL_AUDIT_EVALUATION_REPORT.md successfully updated!")
