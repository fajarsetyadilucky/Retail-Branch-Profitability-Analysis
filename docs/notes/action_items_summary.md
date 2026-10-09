## Catatan Hasil: Ringkasan Cabang yang Perlu Tindak Lanjut

Tabel ini adalah **tampilan tersaring** dari root cause analysis gabungan sebelumnya, hanya menampilkan cabang yang kesimpulannya bukan "Normal" (9 dari 18 cabang), plus dua kolom angka mentah (`sourcing_z` dan `waste_z`) untuk referensi cepat.

**Penting dipahami:** kolom `kesimpulan` di tabel ini tetap dihitung dari status gabungan tiga metrik sekaligus (sourcing, waste, DAN labor), bukan cuma dari dua kolom yang ditampilkan (`sourcing_z`, `waste_z`). Jadi kalau ada baris yang z-score sourcing/waste-nya kelihatan biasa saja tapi kesimpulannya tetap "Bermasalah", itu karena masalahnya ada di `labor_z` yang tidak ditampilkan di tabel ringkas ini.

### Verifikasi Data (memastikan tidak ada yang tertukar)

- **BR03**: `sourcing_z` = -3,9 (efisien) dan `waste_z` = -5,1 (efisien), tapi kesimpulannya tetap "Bermasalah murni: labor". Ini konsisten, karena BR03 memang bersih di sourcing dan waste, masalahnya murni di staffing (labor_z = 8,3, tidak ditampilkan di kolom tabel ini tapi menentukan kesimpulan)
- **BR18**: sourcing_z 3,7 (bermasalah, tapi wajar untuk cabang baru) dan waste_z -2,6 (efisien), kesimpulan "Bermasalah ganda: sourcing, labor" karena labor_z-nya juga tinggi
- **BR05 dan BR11**: keduanya tinggi di sourcing_z DAN waste_z, konsisten dengan kesimpulan "Bermasalah ganda: sourcing, waste"
- **BR13**: tinggi di sourcing_z (10,7) tapi waste_z normal (1,8), konsisten dengan "Bermasalah murni: sourcing"
- **BR01**: sourcing_z 2,4 (sedikit di atas ambang), waste_z -2,3 (efisien), tetap masuk kategori "Bermasalah murni: sourcing", meski seperti sudah dibahas di catatan sebelumnya, dampaknya ke margin nyaris tidak terasa (margin_z hanya 0,2)
- **BR07, BR02, BR09**: ketiganya efisien di sourcing dan waste sekaligus, masuk kategori "Benchmark", tapi ingat dari catatan sebelumnya, cuma BR09 yang benar-benar menonjol di margin (z=4,3), BR07 dan BR02 marginnya biasa saja (z=0,9 dan 0,6)

### Kesimpulan

Tabel ini tidak mengubah apapun dari kesimpulan final yang sudah didokumentasikan sebelumnya, ini cuma cara lain menampilkan data yang sama (versi tersaring, hanya baris yang perlu perhatian, dengan angka mentah sourcing/waste sebagai referensi). Prioritas tindak lanjut tetap sama: **BR03, BR18, BR05, BR11, BR13** sebagai cabang yang butuh intervensi nyata, dengan BR09 sebagai benchmark tunggal yang layak dipelajari.
