# Catatan Data Quality Check & Cleaning: Proyek RANTING

Catatan ini didokumentasikan per langkah: apa yang dicek/dikerjakan, kenapa dilakukan, apa hasilnya, dan tindakan apa yang diambil. Ini jadi bukti proses berpikir untuk portofolio, bukan cuma laporan hasil akhir.

Bagian **Hasil** yang bertanda `[isi setelah dijalankan]` perlu Anda lengkapi sendiri dengan output aktual dari notebook, karena saya tidak menjalankan kodenya di sisi Anda. Yang sudah ada angkanya berarti sudah Anda sampaikan sebelumnya di percakapan ini.

---

## Step 1: Cek Missing Value di Semua Tabel

**Kenapa dilakukan:** untuk mengetahui tabel dan kolom mana saja yang datanya tidak lengkap, sebelum diputuskan cara penanganannya. Tidak semua nilai kosong berarti error, jadi perlu dilihat konteksnya dulu.

**Hasil:**
- `orders.customer_id`: 34.014 baris kosong
- `opex_monthly.utilities_cost`: 6 baris kosong
- Tabel lain: `[isi setelah dijalankan]`

**Kesimpulan & Tindakan:**
- `orders.customer_id` **dibiarkan kosong**, tidak dihapus dan tidak diisi. Kosong di sini mewakili kondisi bisnis yang wajar (pelanggan anonim/tidak check-in membership saat transaksi), bukan data yang seharusnya ada tapi hilang. Ditambahkan kolom bantu `customer_type` untuk memudahkan analisis ke depan, tanpa mengubah nilai aslinya.
- `opex_monthly.utilities_cost` **diisi dengan rata-rata per cabang** (`groupby('branch_id').transform(fillna mean)`), karena nilai kosong di sini kemungkinan besar karena laporan area manager yang telat/tidak lengkap, bukan makna bisnis tersendiri. Ditambahkan flag `utilities_missing_flag` sebelum diisi, supaya jejak baris yang diestimasi tetap bisa ditelusuri.

---

## Step 2: Cek Inkonsistensi Format Teks

**Kenapa dilakukan:** ID atau kategori yang sama tapi ditulis beda format (huruf besar/kecil, spasi ekstra) akan dianggap sebagai nilai berbeda oleh sistem, dan menyebabkan join antar tabel gagal secara diam-diam tanpa error yang jelas.

**Hasil:**
- `opex_monthly.branch_id`: ditemukan sejumlah baris dengan format tidak konsisten (huruf kecil dan/atau spasi ekstra) dibanding format standar di `branch_master`
- Tabel/kolom lain: `[isi setelah dijalankan]`

**Kesimpulan & Tindakan:**
- Kolom asli disimpan ke `branch_id_original` sebelum diubah, sebagai jejak audit
- `opex_monthly.branch_id` dibersihkan dengan `.str.strip().str.upper()`
- Diverifikasi ulang lewat pengecekan referential integrity (Step 4) untuk membuktikan perbaikan ini benar-benar menyelesaikan masalah, bukan cuma asumsi

---

## Step 3: Cek Duplikat

**Kenapa dilakukan:** baris yang tercatat dua kali akan membuat semua agregasi (revenue, jumlah order, dll) jadi lebih besar dari yang seharusnya, dan sering tidak disadari karena tidak memunculkan error.

**Hasil:** `[isi setelah dijalankan]`

**Kesimpulan & Tindakan:** `[isi setelah dijalankan — jika ada duplikat: berapa baris dihapus per tabel; jika tidak ada: catat "tidak ditemukan duplikat, tidak ada tindakan"]`

---

## Step 4: Validasi Referential Integrity (Orphan Check)

**Kenapa dilakukan:** memastikan setiap ID di tabel transaksi (fact) benar-benar punya pasangan yang valid di tabel master (dimension). Kalau ada ID yang "menggantung" tanpa pasangan, data itu tidak bisa digabungkan dengan benar saat analisis, dan bisa membuat baris tersebut hilang diam-diam saat join.

**Hasil:**
- `opex_monthly -> branch_master`: sebelum pembersihan format di Step 2, ditemukan baris orphan; setelah pembersihan, `[isi setelah dijalankan — seharusnya 0]`
- Relasi lain (order_items -> orders, purchases -> ingredients, shifts -> employees, dst): `[isi setelah dijalankan]`

**Kesimpulan & Tindakan:**
- Orphan tidak langsung dihapus otomatis, karena penyebabnya bisa bermacam-macam (typo, data baru yang belum terdaftar, data historis karyawan resign, dll), dan masing-masing butuh keputusan berbeda
- Untuk kasus `opex_monthly`, orphan-nya adalah **akibat** dari masalah format teks di Step 2, bukan masalah berdiri sendiri, sehingga otomatis selesai begitu Step 2 dibereskan

---

## Step 5: Cek Tipe Data

**Kenapa dilakukan:** kolom yang seharusnya numerik tapi tersimpan sebagai teks (object) tidak bisa dihitung (dijumlah, dirata-rata) tanpa dikonversi dulu, dan sering lolos tanpa disadari sampai muncul error di tahap perhitungan.

**Hasil:** `[isi setelah dijalankan]`

**Kesimpulan & Tindakan:** `[isi setelah dijalankan — kolom apa saja yang dikonversi, atau catat "semua kolom numerik sudah bertipe benar sejak awal"]`

---

## Step 6: Cek & Konversi Kolom Tanggal

**Kenapa dilakukan:** kolom tanggal yang masih berupa string tidak bisa difilter berdasarkan rentang waktu, tidak bisa dihitung selisih harinya (misal untuk usia cabang), dan tidak bisa dipakai untuk fungsi time intelligence nanti di Power BI.

**Hasil:**
- Sebelum konversi: seluruh kolom tanggal (`orders.date`, `shifts.date`, `purchases.month`, `inventory.month`, `opex_monthly.month`, `branch_master.opening_date`, `customers.join_date`) bertipe object/string
- Setelah konversi ke `pd.to_datetime()`: `[isi setelah dijalankan — jumlah baris yang gagal dikonversi per kolom, seharusnya 0]`

**Kesimpulan & Tindakan:** semua kolom tanggal dikonversi ke tipe `datetime64` menggunakan `pd.to_datetime()`, dengan `errors='coerce'` agar nilai yang gagal dikonversi terlihat sebagai NaT (bisa ditelusuri), bukan menyebabkan program berhenti.

---

## Step 7: Penanganan Order Void

**Kenapa dilakukan:** order dengan status `Void` bukan transaksi valid (dibatalkan), sehingga kalau ikut dihitung akan membuat revenue dan semua KPI turunannya (Food Cost %, Net Margin %) menjadi salah lebih tinggi dari kondisi sebenarnya.

**Hasil:** `[isi setelah dijalankan — jumlah dan persentase order Void]`

**Kesimpulan & Tindakan:** dibuat dataset kerja terpisah `orders_completed` yang hanya berisi status `Completed`, dipakai untuk semua perhitungan revenue dan KPI ke depannya. Data `orders` asli (termasuk yang Void) tetap disimpan utuh, karena masih dibutuhkan untuk menghitung KPI Void Rate sebagai indikator kualitas operasional tersendiri.

---

## Step 8: Cek Outlier

**Kenapa dilakukan:** revenue harian yang jauh di luar kewajaran perlu diperiksa dulu sebelum dipakai untuk kesimpulan, karena bisa jadi kesalahan input, atau justru kondisi nyata yang penting (misal cabang baru yang masih ramp-up, atau cabang terbaik yang memang jauh di atas rata-rata).

**Hasil:** `[isi setelah dijalankan — jumlah hari-cabang yang terdeteksi outlier dari metode IQR]`

**Kesimpulan & Tindakan:** outlier **tidak otomatis dihapus atau di-cap**. Tiap kasus diperiksa satu per satu dengan membandingkan `date` dan `branch_id`-nya terhadap `opening_date` cabang tersebut di `branch_master`, untuk membedakan mana yang anomali data dan mana yang kondisi bisnis nyata (misal ramp-up cabang baru atau performa cabang terbaik).

---

## Ringkasan Prinsip Cleaning yang Dipegang di Proyek Ini

1. Setiap nilai kosong diperiksa dulu maknanya sebelum diputuskan diisi atau dibiarkan, bukan langsung `fillna()` untuk semua kolom dengan cara yang sama
2. Setiap perubahan data (format teks, isi nilai kosong) disimpan jejak versinya (`_original`), supaya bisa ditelusuri ulang
3. Baris bermasalah (orphan, outlier) diisolasi untuk diperiksa dulu, tidak langsung dihapus, karena bisa jadi sinyal masalah yang lebih besar
4. Data mentah (`orders` lengkap dengan Void) tetap disimpan utuh terpisah dari data yang sudah difilter untuk analisis (`orders_completed`), supaya tidak kehilangan informasi yang justru dibutuhkan di KPI lain
