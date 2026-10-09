## Catatan Hasil: Uji Signifikansi Labor Cost (Standard Error)

**Hasil:**
```
branch_id  avg_labor_pct  n_records  z_vs_overall_mean
BR03            30.52          6                8.3
BR18            25.60          4                3.5
BR16            20.26          6               -0.2
...
BR09            16.17          6               -3.5
```

### Interpretasi

**BR03 dengan z-score 8,3**, jauh di atas ambang signifikan (>2). Ini membuktikan secara statistik bahwa kecurigaan Pak Dimas di brief awal soal "staffing boros" itu benar, bukan sekadar kesan sekilas. BR03 secara struktural overstaffed dibanding cabang lain, bukan variasi kebetulan bulan ke bulan.

**BR18 dengan z-score 3,5**, juga melewati ambang signifikan. Tapi z-score tinggi di sini **tidak otomatis berarti "bermasalah"** seperti BR03, karena BR18 adalah cabang baru (baru 4 bulan beroperasi dari 6 bulan periode analisis). Signifikansi ini kemungkinan besar mencerminkan kebutuhan staf minimum yang tetap ada meski volume order belum optimal, bukan inefisiensi manajemen seperti di BR03. Perlu dipantau di bulan-bulan berikutnya untuk melihat apakah rasio ini turun seiring bertambahnya usia operasional (ramp-up), bukan langsung diberi tindakan korektif seperti BR03.

**BR09 dengan z-score -3,5**, mengonfirmasi kembali sisi efisiensinya, kali ini di dimensi tenaga kerja. Menyatukan tiga temuan sebelumnya (sourcing, waste, sekarang labor), BR09 unggul di ketiga dimensi operasional sekaligus, memperkuat kelayakannya sebagai benchmark utama, bukan cuma pilihan berdasarkan satu metrik saja.

**Cabang lain (14 cabang selain BR03, BR18, BR09)** semuanya berada di rentang z-score -1,1 sampai -0,2, jauh di bawah ambang signifikan. Ini artinya labor cost di cabang-cabang ini seragam dan sehat, tidak perlu tindakan apapun.

### Catatan Metodologi (penting untuk transparansi di portofolio)

Uji ini menggunakan **6 titik data per cabang** (6 bulan), jauh lebih sedikit dibanding uji Sourcing sebelumnya yang memakai 108 transaksi pembelian per cabang. Ini karena Labor Cost % dihitung di level agregat bulanan, bukan per transaksi individual seperti pembelian bahan baku. Konsekuensinya, uji ini punya kekuatan statistik (statistical power) yang lebih rendah, standard error-nya lebih besar (1,22 dibanding 0,008 di sourcing). Meski begitu, karena selisih BR03 dan BR18 terhadap rata-rata cukup besar, keduanya tetap terbukti signifikan walau dengan sampel yang lebih kecil. Ini penting dicatat sebagai batasan analisis, bukan disembunyikan, kalau ditanya HR soal keterbatasan metode.

### Ringkasan Root Cause Analysis (Update, Food Cost + Labor Cost)

| Cabang | Food Cost | Sourcing | Waste | Labor Cost | Kesimpulan |
|---|---|---|---|---|---|
| BR05 | Signifikan tinggi | Signifikan tinggi | Signifikan tinggi | Normal | Masalah murni food cost (sourcing + waste) |
| BR11 | Signifikan tinggi | Signifikan tinggi | Signifikan tinggi | Normal | Masalah murni food cost (sourcing + waste) |
| BR13 | Signifikan tinggi | Signifikan tinggi | Normal | Normal | Masalah murni sourcing |
| BR03 | Normal | Normal | Normal | **Signifikan tinggi** | Masalah murni staffing/labor |
| BR18 | Sedikit tinggi (wajar usia) | Sedikit tinggi (wajar usia) | Rendah (baik) | Signifikan tinggi (wajar usia) | Cabang baru, pantau bukan tindak lanjuti |
| BR09 | Signifikan rendah | Signifikan rendah | Signifikan rendah | Signifikan rendah | Benchmark di semua dimensi |

### Langkah Selanjutnya

Root cause analysis untuk Food Cost dan Labor Cost sudah tuntas dan terbukti secara statistik. Langkah berikutnya adalah menghitung **Net Margin %**, KPI final yang menggabungkan Revenue, Food Cost, Labor Cost, dan Opex (rent, marketing, utilities) jadi satu angka kesehatan bisnis per cabang, sesuai KPI yang sudah ditentukan di awal proyek untuk menjawab pertanyaan owner "cabang mana yang paling untung".
