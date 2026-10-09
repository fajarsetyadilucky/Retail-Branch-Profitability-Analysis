## Catatan Hasil: Root Cause Analysis Gabungan (Final, Setelah Semua Koreksi Data)

Tabel ini adalah versi final root cause analysis, dihitung setelah tiga perbaikan data selesai diterapkan: koreksi duplikat palsu di `order_items`, kalibrasi ulang `shifts` (labor cost), kalibrasi ulang `rent_cost`, dan imputasi `utilities_cost` yang sempat tertinggal.

### Tabel Final

| Cabang | Sourcing | Waste | Labor | Margin Z | Kesimpulan |
|---|---|---|---|---|---|
| BR03 | Efisien | Efisien | Bermasalah | -5,5 | Bermasalah murni: labor |
| BR18 | Bermasalah | Efisien | Bermasalah | -4,0 | Bermasalah ganda: sourcing, labor |
| BR05 | Bermasalah | Bermasalah | Normal | -3,0 | Bermasalah ganda: sourcing, waste |
| BR11 | Bermasalah | Bermasalah | Normal | -1,6 | Bermasalah ganda: sourcing, waste |
| BR13 | Bermasalah | Normal | Normal | -0,7 | Bermasalah murni: sourcing |
| BR01 | Bermasalah | Efisien | Normal | 0,2 | Bermasalah murni: sourcing (dampak margin nyaris nol) |
| BR02, BR07, BR09 | Efisien | Efisien | (BR09 juga Efisien) | 0,6 / 0,9 / 4,3 | Benchmark (unggul di banyak sisi) |
| 9 cabang lainnya | Normal/Efisien campuran | | | 0,2 s/d 1,5 | Normal |

### Lima Prioritas Tindak Lanjut (urut margin terendah)

1. **BR03** (margin_z -5,5) — murni masalah staffing, audit SOP shift kerja
2. **BR18** (margin_z -4,0) — cabang baru, kombinasi wajar sourcing+labor karena belum skala ekonomis, pantau bukan tindak lanjuti aktif
3. **BR05** (margin_z -3,0) — masalah ganda sourcing dan waste, prioritas audit tertinggi di antara kasus food cost
4. **BR11** (margin_z -1,6) — pola sama seperti BR05, tingkat keparahan lebih ringan, belum signifikan di margin
5. **BR13** (margin_z -0,7) — murni sourcing, belum signifikan di margin, cukup evaluasi supplier saja

**Catatan penting:** BR11 dan BR13 terbukti signifikan bermasalah di komponen individual (sourcing/waste), tapi dampaknya ke margin keseluruhan belum melewati ambang signifikan (z > -2). Ini bukan berarti diabaikan, tapi levelnya belum semendesak BR03 dan BR05.

**BR01** menunjukkan status "Bermasalah" di sourcing tapi margin_z-nya nyaris nol (0,2), dampak nyatanya ke bisnis dapat diabaikan, tidak perlu masuk prioritas tindak lanjut.

### Benchmark

**BR09** tetap satu-satunya cabang yang unggul di ketiga metrik biaya SEKALIGUS margin jauh di atas rata-rata (z=4,3), layak jadi studi kasus SOP terbaik untuk disebarkan ke jaringan. BR02 dan BR07 efisien di sourcing dan waste tapi dampak margin mereka biasa saja (z=0,6 dan 0,9), tidak setara BR09.

### Riwayat Perbaikan Data yang Mendasari Angka Final Ini

Angka di tabel ini adalah hasil akhir setelah menemukan dan memperbaiki empat isu data sepanjang proyek:
1. `order_items` — 1.710 baris transaksi sah salah terhapus oleh `drop_duplicates()` tanpa kolom ID unik
2. `shifts` — jam kerja/labor cost tidak terkalibrasi terhadap revenue (rasio awal 69,9%, tidak realistis)
3. `opex_monthly.rent_cost` — sewa flat tidak proporsional terhadap skala cabang (sempat menyebabkan seluruh Net Margin negatif ekstrem)
4. `opex_monthly.utilities_cost` — nilai kosong sempat dianggap nol alih-alih diimputasi rata-rata cabang, menyebabkan margin BR03 September bias ke atas secara artifisial

Ini penting dicantumkan di catatan metodologi laporan akhir, sebagai bukti proses validasi data yang menyeluruh, bukan sekadar menerima angka pertama yang keluar dari perhitungan.

### Status

Fase 4 (Perhitungan KPI dan Root Cause Analysis) tuntas dengan data final yang sudah tervalidasi berlapis. Lanjut ke Fase 5 (Exploratory Analysis) dan penyusunan ringkasan eksekutif final.
