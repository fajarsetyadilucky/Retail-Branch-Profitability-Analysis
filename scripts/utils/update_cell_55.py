import json

with open('save & Clean/projeck_portfolio_1.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find Cell 55
cell_55 = nb['cells'][55]
print("Original source of Cell 55:")
print(''.join(cell_55['source']))

new_source = [
    "Catatan Hasil:\n",
    "Pola ini konsisten dan mengonfirmasi semua temuan sebelumnya. Urutan margin terendah persis sejalan dengan cabang-cabang yang sudah kita buktikan bermasalah secara statistik di tahap Food Cost dan Labor Cost. Tidak ada kejutan baru di sini, ini justru bukti bahwa analisis dari awal sampai akhir saling konsisten satu sama lain.\n",
    "\n",
    "Catatan khusus BR18: di tabel ini muncul status \"Bermasalah ganda: sourcing, labor\", tapi ingat konteksnya tetap sama seperti sebelumnya, ini efek wajar cabang baru yang belum mencapai skala ekonomis, bukan indikasi mismanajemen seperti BR03. Jangan disamakan prioritas penanganannya.\n",
    "Temuan Tambahan yang Perlu Diwaspadai: Label Otomatis Tidak Selalu Mencerminkan Dampak Nyata\n",
    "\n",
    "Ada tiga kasus di tabel ini yang labelnya perlu dibaca hati-hati, jangan diambil mentah-mentah dari status \"Bermasalah\"/\"Efisien\"/\"Benchmark\":\n",
    "\n",
    "\n",
    "*   BR01 berstatus \"Bermasalah murni: sourcing\" (z=2,4, sedikit di atas ambang 2), tapi margin_z-nya nyaris 0 (0,2), nyaris sama dengan rata-rata keseluruhan. Artinya meski sourcing-nya sedikit menyimpang secara statistik, dampaknya ke kesehatan bisnis cabang ini nyaris tidak terasa.\n",
    "*   BR07 dan BR02 berstatus \"Benchmark (unggul di banyak sisi)\", tapi margin_z-nya cuma 0,9 dan 0,6, jauh di bawah BR09 (4,3) yang benar-benar menonjol. Predikat \"Benchmark\" untuk BR07/BR02 ini lebih karena kebetulan efisien di dua metrik biaya sekaligus (ambang z<-2), bukan karena performa bisnis keseluruhannya benar-benar istimewa.\n",
    "\n",
    "Cara membaca hasil otomatis seperti ini: ambang statistik (z>2 atau z<-2) itu berguna untuk menyaring kandidat awal, tapi keputusan akhir soal mana yang benar-benar \"penting ditindaklanjuti\" tetap harus dicek silang dengan dampaknya ke Net Margin, bukan diambil mentah dari label kategorikal. BR03, BR18, BR05, BR11, BR13 layak jadi prioritas karena z-score bermasalahnya SEKALIGUS diikuti margin yang jelas di bawah rata-rata. BR01, BR07, BR02 tidak perlu masuk daftar prioritas, karena meski lolos ambang statistik di satu metrik, dampaknya ke margin keseluruhan tidak berarti.\n",
    "\n",
    "**Kesimpulan Final Root Cause Analysis:**\n",
    "Prioritas tindak lanjut (urut dari paling mendesak):\n",
    "\n",
    "*   BR03 — audit staffing/SOP shift kerja\n",
    "*   BR18 — pantau, bukan tindak lanjuti aktif, ini efek wajar cabang baru\n",
    "*   BR05 — audit ganda: supplier dan SOP dapur\n",
    "*   BR11 — audit ganda: supplier dan SOP dapur, prioritas lebih rendah dari BR05\n",
    "*   BR13 — evaluasi supplier/kontrak harga saja\n",
    "\n",
    "Tidak perlu tindakan: 12 cabang sisanya, termasuk BR01, BR07, BR02 yang sempat muncul di label statistik tapi dampaknya ke margin tidak signifikan.\n",
    "\n",
    "Benchmark tunggal: BR09, unggul di semua dimensi (sourcing, waste, labor) DAN margin-nya jauh di atas cabang lain (z=4,3), satu-satunya cabang yang layak dijadikan studi kasus SOP terbaik untuk disebarkan ke jaringan.\n",
    "\n",
    "Dengan ini, Fase 4 (Perhitungan KPI dan Root Cause Analysis) resmi tuntas 100%. Langkah selanjutnya: Fase 5, Exploratory Analysis, atau langsung menyusun ringkasan eksekutif final untuk dibawa ke rapat dengan owner/atasan.\n"
]

cell_55['source'] = new_source

with open('save & Clean/projeck_portfolio_1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("\nCell 55 successfully updated in projeck_portfolio_1.ipynb!")
