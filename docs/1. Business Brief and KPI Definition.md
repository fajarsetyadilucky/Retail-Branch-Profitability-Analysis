# Catatan Proyek: Analisis Performa Cabang RANTING

## 1. Latar Belakang & Tugas dari Stakeholder

**Dari:** Dimas Pratama, Head of Operations, RANTING (jaringan F&B multi-cabang, 18 outlet di Jabodetabek)
**Kepada:** Fajar (Data Analyst)
**Perihal:** Butuh visibility performa cabang

> Fajar, saya baru 2 bulan pegang divisi ini dan terus terang saya masih blank soal cabang mana yang sehat dan mana yang bermasalah. Selama ini laporan datang dari masing-masing area manager dalam format Excel yang beda-beda, ada yang mingguan ada yang bulanan, dan angkanya sering nggak nyambung satu sama lain.
>
> Saya butuh sesuatu yang bisa saya buka tiap Senin pagi dan langsung tahu: cabang mana yang perlu saya telepon hari itu juga.
>
> Yang saya bayangkan kira-kira begini, tapi Anda yang lebih paham datanya, jadi tolong dikoreksi kalau saya salah asumsi:
> - Beberapa cabang kelihatan ramai tapi profitnya tipis, saya curiga soal food cost atau staffing yang boros
> - Ada cabang baru yang saya nggak yakin performanya dibandingkan cabang lama, apakah masih wajar untuk usia segitu atau sudah harus dievaluasi
> - Owner sering tanya "cabang mana yang paling untung", dan saya belum bisa jawab dengan percaya diri
>
> Untuk minggu ini, tolong siapkan dashboard awal plus temuan-temuan penting yang saya perlu tahu. Saya presentasikan ke owner hari Jumat.

**Tenggat:** dashboard awal + temuan kunci, dipresentasikan Jumat.
**Cakupan:** 18 cabang RANTING, data transaksi dan operasional April–September 2026.

## 2. Menerjemahkan Permintaan Menjadi Pertanyaan Bisnis

Dari brief di atas, permintaan yang masih kabur diterjemahkan menjadi tiga pertanyaan yang bisa dijawab dengan data:

1. Cabang mana yang **revenue tinggi tapi margin rendah**, dan apa penyebabnya, food cost atau labor cost?
2. Apakah **cabang baru** benar-benar bermasalah, atau performanya masih wajar untuk usia operasionalnya (ramp-up curve)?
3. Cabang mana yang **paling menguntungkan secara konsisten**, sehingga bisa dijadikan acuan/benchmark untuk cabang lain?

## 3. KPI yang Dipilih dan Alasannya

| KPI | Formula / Sumber | Alasan Dipilih |
|---|---|---|
| **Revenue per Cabang per Bulan** | `SUM(order_items.quantity × unit_price)` dari order dengan status Completed | Baseline paling dasar, tapi sengaja **tidak dijadikan satu-satunya** ukuran kesehatan cabang, karena revenue tinggi bisa menutupi masalah margin. Tetap perlu ditampilkan sebagai konteks. |
| **Food Cost %** | `Total COGS (dari purchases × recipe usage) / Revenue × 100%` | Ini KPI inti untuk menjawab kecurigaan Pak Dimas soal "ramai tapi profit tipis". Industri F&B punya rule of thumb food cost sehat di kisaran 28–35%; di atas itu jadi sinyal masalah sourcing atau waste. |
| **Labor Cost %** | `SUM(shifts.hours_worked × hourly_rate) / Revenue × 100%` | Melengkapi Food Cost %. Cabang bisa saja food cost-nya normal tapi overstaffed, sehingga margin tetap tergerus dari sisi lain. Tanpa KPI ini, akar masalah bisa salah didiagnosis. |
| **Net Margin %** | `(Revenue − COGS − Labor − Rent − Utilities − Marketing) / Revenue × 100%` | Ini jawaban langsung untuk pertanyaan owner "cabang mana yang paling untung". Revenue saja tidak cukup, margin bersih yang jadi ukuran akhir kesehatan bisnis per cabang. |
| **Waste %** | `waste_qty / theoretical_usage` dari inventory | Diagnostik lanjutan dari Food Cost %. Kalau food cost tinggi, KPI ini membantu memisahkan penyebab: karena harga beli mahal (sourcing) atau karena banyak bahan terbuang (operasional dapur). |
| **Revenue per Hari Operasional (usia-adjusted)** | Revenue dibagi jumlah hari sejak `opening_date`, dibandingkan kurva ramp-up cabang lain di usia yang sama | Menjawab langsung kekhawatiran soal cabang baru. Membandingkan cabang berusia 3 bulan dengan cabang berusia 3 tahun pakai angka mentah itu tidak adil; KPI ini menormalkan perbandingan berdasarkan usia operasional. |
| **Order Void Rate** | `COUNT(order_status='Void') / COUNT(total order)` | Indikator kualitas operasional dan potensi kebocoran (void yang tidak wajar tinggi bisa menandakan masalah lain, misalnya kesalahan input atau kecurangan kasir). Bukan fokus utama Pak Dimas, tapi murah untuk dihitung dan bisa jadi temuan tambahan yang menunjukkan ketelitian analisis. |

## 4. KPI yang Sengaja Tidak Dijadikan Sorotan Utama

- **Rating pelanggan / channel mix**: relevan untuk tim marketing, tapi di luar pertanyaan inti Pak Dimas soal profitabilitas cabang. Disinggung sebagai insight tambahan saja, tidak dijadikan headline dashboard.
- **Jumlah transaksi**: bisa menyesatkan tanpa dikaitkan ke average order value dan margin, jadi tidak berdiri sendiri sebagai KPI utama.

## 5. Output yang Disiapkan

1. Dashboard Power BI: ranking cabang berdasarkan Net Margin %, breakdown Food Cost % vs Labor Cost % per cabang, dan tren revenue per usia cabang.
2. Ringkasan temuan kunci (3–5 poin) untuk dibawa Pak Dimas ke rapat Jumat dengan owner.
3. Catatan data limitation: metode costing pakai rata-rata bulanan (bukan FIFO), waste dicatat agregat bulanan tanpa breakdown penyebab.
