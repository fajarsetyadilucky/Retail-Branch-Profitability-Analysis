# Dokumentasi Proyek Analisis Bisnis & Portofolio BI
## RANTING Restaurant Multi-Branch Optimization

Folder `docs/` merangkum seluruh dokumentasi terstruktur, mulai dari brief pemangku kepentingan (*stakeholder brief*), metodologi data engineering, pengujian statistik, hingga laporan rekomendasi eksekutif.

---

### 📚 Daftar Dokumen Utama (Core Documents)

1. [01. Business Brief and KPI Definition](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/01_business_brief_kpi.md)
   - Latar belakang bisnis dari Head of Operations (Dimas Pratama).
   - Penerjemahan 3 pertanyaan bisnis inti.
   - Definisi formula 7 KPI operasional F&B (Gross Revenue, Food Cost %, Labor Cost %, Net Margin %, Waste %, Revenue/Hari Usia-Adjusted, Void Rate).

2. [02. Data Cleaning & Quality Assurance Log](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/02_data_cleaning_log.md)
   - Log 8 tahapan pembersihan data: missing value handling, standardisasi teks, penanganan duplikat semu di `order_items`, validasi integritas referensial (orphan check), konversi tipe data & tanggal, penanganan transaksi void, serta deteksi outlier IQR.

3. [03. Root-Cause Analysis & Statistical Validation](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/03_root_cause_analysis.md)
   - Uji statistik inferensial Z-Score terhadap Standard Error untuk Sourcing, Waste, Labor Cost, dan Net Margin.
   - Diagnosa 4 cabang kritis (BR03, BR05, BR11, BR13) vs kasus cabang baru (BR18) vs benchmark tunggal (BR09).

4. [04. Executive Recommendation & Financial Impact](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/04_executive_recommendations.md)
   - Rekomendasi taktis bertingkat berdasarkan prioritas urgensi.
   - Model penyelamatan margin: pemulihan potensi laba bersih **~Rp 254 Juta per tahun** dengan mereplikasi standar emas Cinere (40,8%).
   - Roadmap aksi terarah 30 hari (4 sprint mingguan).

5. [05. Final Findings Report](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/05_final_findings_report.md)
   - Laporan narasi eksekutif formal dari Data Analyst (Fajar) kepada Head of Operations untuk diteruskan ke Owner.

---

### 📝 Catatan Riset & Analisis Teknis Pendukung (`docs/notes/`)

- [labor_cost_significance.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/labor_cost_significance.md): Pembuktian empiris overstaffing di Kelapa Gading (Labor Z-Score = +8,3).
- [net_margin_interpretation.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/net_margin_interpretation.md): Interpretasi ranking margin kontribusi 18 cabang Jabodetabek.
- [food_cost_recommendations.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/food_cost_recommendations.md): Memo awal penghematan biaya bahan baku cabang BSD, Tangerang, dan Sentul.
- [monthly_margin_trends.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/monthly_margin_trends.md): Penjelasan tren stabilitas margin untuk sesi presentasi ke Owner.
- [project_roadmap.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/project_roadmap.md): Roadmap 8 fase pengerjaan proyek dari inisiasi requirement hingga storytelling.
- [action_items_summary.md](file:///d:/BOOTCAMP%20BUSSINESS%20INTELEGENCE%20&%20DATA%20ANALYST/project/Portfolio%20Projoject%201/docs/notes/action_items_summary.md): Ringkasan matriks tindak lanjut per cabang.
