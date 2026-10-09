# Roadmap Pengerjaan: Analisis Performa Cabang RANTING

Urutan kerja ini meniru alur kerja Data Analyst/BI sungguhan: dari requirement yang kabur, ke data mentah yang berantakan, sampai ke insight yang bisa dipakai stakeholder mengambil keputusan. Tidak langsung loncat ke dashboard.

---

## Fase 0: Klarifikasi Kebutuhan (sebelum sentuh data sama sekali)

**Kenapa fase ini ada duluan:** brief dari Pak Dimas masih kabur ("saya curiga soal food cost atau staffing"). Analis yang baik tidak langsung asumsi, tapi mengonfirmasi dulu supaya tidak salah arah dan buang waktu.

- Konfirmasi ulang 3 pertanyaan bisnis yang sudah diturunkan dari brief (lihat catatan KPI sebelumnya)
- Konfirmasi threshold: berapa food cost % dan margin % yang dianggap "bermasalah" menurut standar RANTING
- Konfirmasi audiens dashboard: dipakai harian oleh Pak Dimas sendiri, atau juga akan dilihat owner di rapat Jumat (ini menentukan tingkat detail vs ringkas)

**Output:** daftar pertanyaan bisnis final dan definisi "sehat vs bermasalah" yang disepakati.

---

## Fase 1: Data Understanding & Extraction

- Inventarisasi semua tabel sumber: `orders`, `order_items`, `purchases_monthly`, `inventory_monthly`, `shifts`, `employees`, `opex_monthly`, `branch_master`, `recipes`, `menu_items`, `customers`
- Cek struktur dan relasi antar tabel (mana primary key, mana foreign key)
- Tulis query ekstraksi awal: join dasar untuk memastikan semua tabel bisa terhubung lewat `branch_id`, `item_id`, `ingredient_id`

**Output:** skema relasi tabel (ERD sederhana), query ekstraksi dasar.

---

## Fase 2: Data Cleaning & Quality Check

- Cek konsistensi `branch_id` di semua tabel (kasus di `opex_monthly` yang formatnya tidak seragam)
- Cek nilai kosong: `utilities_cost` yang NaN di `opex_monthly`, tentukan cara penanganan (exclude dari perhitungan bulan itu, atau estimasi dari rata-rata bulan lain, dan catat keputusannya)
- Cek `order_status = Void`, pastikan dikeluarkan dari perhitungan revenue
- Cek outlier: cabang atau bulan dengan angka yang jauh di luar wajar, verifikasi apakah itu data error atau memang kejadian nyata (misal cabang baru buka)
- Validasi referensial: pastikan semua `branch_id`, `item_id`, `ingredient_id` di tabel transaksi ada di tabel master, tidak ada yang orphan

**Output:** data yang sudah bersih plus catatan log cleaning, apa saja yang diubah dan kenapa. Catatan ini penting untuk portofolio, tunjukkan bukan cuma hasil akhir tapi proses berpikirnya.

---

## Fase 3: Data Modeling

- Susun jadi model bintang (star schema) untuk kebutuhan Power BI: fact table (orders, order_items, purchases, shifts) dan dimension table (branch, menu, ingredient, employee, customer, date)
- Buat tabel kalender (date table) terpisah untuk mendukung perhitungan time intelligence di DAX (MTD, perbandingan usia cabang, dll)
- Tentukan relasi antar tabel di Power BI (one-to-many, arah filter)

**Output:** model data yang siap dipakai untuk perhitungan measure, bukan cuma tabel mentah ditumpuk.

---

## Fase 4: Perhitungan KPI (SQL/DAX) & Validasi

- Bangun measure untuk tiap KPI yang sudah ditentukan: Food Cost %, Labor Cost %, Net Margin %, Waste %, Revenue per hari usia-adjusted, Void Rate
- Validasi manual: ambil 1-2 cabang, hitung manual di Excel/kalkulator, bandingkan dengan hasil measure, pastikan tidak ada logika yang salah sebelum lanjut ke visual
- Ini langkah yang paling sering dilewati analis pemula tapi paling penting, karena dashboard yang salah hitung lebih berbahaya daripada tidak ada dashboard sama sekali

**Output:** measure yang sudah tervalidasi angkanya benar, bukan cuma "kelihatan masuk akal".

---

## Fase 5: Exploratory Analysis & Insight Finding

- Ranking semua cabang berdasarkan Net Margin %, lihat pola di kelompok atas dan bawah
- Untuk cabang dengan margin rendah, breakdown: penyebabnya Food Cost tinggi, Labor Cost tinggi, atau dua-duanya
- Untuk cabang baru, bandingkan kurva revenue-nya terhadap cabang lain di usia operasional yang sama (bukan dibandingkan mentah dengan cabang berusia 3 tahun)
- Cari korelasi: apakah Food Cost tinggi berasal dari harga beli (sourcing) atau dari waste tinggi di dapur

**Output:** 3-5 temuan kunci yang jelas, bukan sekadar tabel angka, tapi kesimpulan yang menjawab kekhawatiran Pak Dimas di brief.

---

## Fase 6: Dashboard Build (Power BI)

- Halaman 1 (Overview): ranking cabang, KPI card ringkas, highlight cabang yang perlu perhatian (conditional formatting)
- Halaman 2 (Diagnostic): breakdown Food Cost % vs Labor Cost % per cabang, untuk cari akar masalah
- Halaman 3 (Cabang Baru): kurva ramp-up dibanding cabang sejenis
- Terapkan filter interaktif (per bulan, per area)

**Output:** dashboard fungsional, bukan sekadar cantik tapi juga menjawab pertanyaan yang diajukan di Fase 0.

---

## Fase 7: Validasi & QA

- Cross-check ulang beberapa angka di dashboard dengan hasil query SQL mentah, pastikan tidak ada selisih akibat kesalahan relasi tabel
- Review checklist: apakah semua pertanyaan bisnis di Fase 0 sudah terjawab

**Output:** dashboard yang sudah terverifikasi, siap dipresentasikan.

---

## Fase 8: Storytelling & Executive Summary

- Terjemahkan temuan teknis jadi bahasa bisnis untuk Pak Dimas, misal bukan "food cost 38%" tapi "cabang X kehilangan potensi profit karena biaya bahan baku 6 poin persentase di atas rata-rata cabang lain"
- Susun rekomendasi konkret per kategori cabang, bukan cuma laporan angka

**Output:** ringkasan eksekutif 1 halaman, siap dibawa Pak Dimas ke rapat dengan owner.

---

## Fase 9: Dokumentasi & Pengemasan Portofolio

- Tulis studi kasus: latar belakang masalah, proses, temuan, dan dampak (real atau simulatif)
- Dokumentasikan asumsi dan keterbatasan data yang sudah dicatat sebelumnya
- Siapkan cuplikan query SQL kunci dan screenshot dashboard untuk portofolio

**Output:** materi siap pakai untuk portofolio dan bahan cerita saat wawancara.

---

## Estimasi Waktu (mengikuti tenggat 1-2 minggu dari brief)

| Fase | Perkiraan Waktu |
|---|---|
| 0. Klarifikasi kebutuhan | 0.5 hari |
| 1. Data understanding & extraction | 1 hari |
| 2. Data cleaning & QC | 1.5 hari |
| 3. Data modeling | 1 hari |
| 4. Perhitungan KPI & validasi | 1.5 hari |
| 5. Exploratory analysis | 1.5 hari |
| 6. Dashboard build | 2 hari |
| 7. Validasi & QA | 0.5 hari |
| 8. Storytelling & executive summary | 0.5 hari |
| 9. Dokumentasi portofolio | 1 hari |

Total sekitar 11 hari kerja, sesuai anggaran waktu 1-2 minggu yang diberikan Pak Dimas.
