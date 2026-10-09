import os
import subprocess
from pathlib import Path
import shutil
import base64

ROOT_DIR = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT_DIR / "reports"
CAROUSEL_DIR = REPORTS_DIR / "carousel_slides"
FIGURES_DIR = REPORTS_DIR / "figures"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
CAROUSEL_DIR.mkdir(parents=True, exist_ok=True)
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

html_file = REPORTS_DIR / "linkedin_carousel_preview.html"
pdf_file = REPORTS_DIR / "LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf"
pdf_root = ROOT_DIR / "LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf"
pdf_bi = ROOT_DIR / "power_bi" / "LINKEDIN_CAROUSEL_RANTING_RESTAURANT_BI.pdf"
post_copy_file = REPORTS_DIR / "LINKEDIN_POST_COPY.md"
audit_report_file = REPORTS_DIR / "CAROUSEL_AUDIT_EVALUATION_REPORT.md"

def get_base64_image(image_path):
    p = Path(image_path)
    if p.exists():
        ext = p.suffix.lower().replace(".", "")
        if ext == "jpg":
            ext = "jpeg"
        with open(p, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/{ext};base64,{b64}"
    return ""

author_photo_uri = get_base64_image(FIGURES_DIR / "author_fajar_setyadi.png")
overview_img_uri = get_base64_image(FIGURES_DIR / "dashboard_overview.jpg")
cabang_baru_img_uri = get_base64_image(FIGURES_DIR / "dashboard_cabang_baru.jpg")
root_cause_img_uri = get_base64_image(FIGURES_DIR / "dashboard_root_cause.jpg")

github_url = "https://github.com/fajarsetyadilucky/Retail-Branch-Profitability-Analysis"
author_name = "Fajar Setyadi"
author_role = "Data Analyst & Business Intelligence"
author_email = "Fajarsetyadilucky@gmail.com"
author_wa = "089630527099"
author_wa_formatted = "0896-3052-7099"

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>LinkedIn Carousel - RANTING Multi-Branch Profitability Optimization</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
<style>
    @page {{
        size: 1080px 1350px;
        margin: 0;
    }}
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        background: #080d1a;
        color: #f1f5f9;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}

    /* SLIDE CANVAS (4:5 RATIO FOR LINKEDIN DOCUMENT) */
    .slide-wrapper {{
        width: 1080px;
        height: 1350px;
        padding: 40px 52px 32px 52px;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: #0b1329;
        page-break-after: always;
        break-after: page;
        border-bottom: 2px solid #1e293b;
    }}

    /* SUBTLE GEOMETRIC BACKGROUND GRID */
    .grid-bg {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
        background-size: 36px 36px;
        pointer-events: none;
    }}

    /* HEADER */
    .slide-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        margin-bottom: 10px;
    }}
    .tag-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #141f36;
        border: 1px solid rgba(148, 163, 184, 0.28);
        color: #94a3b8;
        padding: 6px 16px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.6px;
        text-transform: uppercase;
    }}
    .tag-badge .accent {{
        color: #38bdf8;
    }}
    .slide-number {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 800;
        color: #94a3b8;
        background: #0f172a;
        padding: 5px 14px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}

    /* BODY */
    .slide-body {{
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        z-index: 10;
    }}

    .slide-category {{
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #38bdf8;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .hook-title {{
        font-size: 38px;
        font-weight: 900;
        line-height: 1.18;
        letter-spacing: -1.2px;
        color: #ffffff;
        margin-bottom: 12px;
    }}
    .hook-title span.emerald {{ color: #10b981; }}
    .hook-title span.amber {{ color: #f59e0b; }}
    .hook-title span.cyan {{ color: #38bdf8; }}
    .hook-title span.red {{ color: #f87171; }}

    .subtitle-text {{
        font-size: 16px;
        line-height: 1.52;
        color: #94a3b8;
        font-weight: 500;
        margin-bottom: 14px;
    }}

    /* AUTHOR HERO CONTAINER (SLIDE 1 TOP-CENTER) */
    .author-hero-container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin: 4px 0 14px 0;
    }}
    .author-hero-avatar {{
        width: 104px;
        height: 104px;
        border-radius: 50%;
        overflow: hidden;
        border: 3px solid #38bdf8;
        background: #1e293b;
        box-shadow: 0 8px 24px rgba(56, 189, 248, 0.28);
        margin-bottom: 8px;
    }}
    .author-hero-avatar img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .author-hero-name {{
        font-size: 19px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: 0.2px;
    }}
    .author-hero-role {{
        font-size: 13px;
        font-weight: 700;
        color: #38bdf8;
        letter-spacing: 0.5px;
        margin-top: 2px;
    }}

    /* BENTO CARDS */
    .bento-card {{
        background: #111c38;
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 10px;
        position: relative;
    }}
    .bento-card.highlight {{
        background: #132347;
        border: 1px solid rgba(56, 189, 248, 0.4);
    }}
    .bento-card.success {{
        background: #0d2826;
        border: 1px solid rgba(16, 185, 129, 0.4);
    }}
    .bento-card.warning {{
        background: #2a2014;
        border: 1px solid rgba(245, 158, 11, 0.4);
    }}
    .bento-card.danger {{
        background: #2a151b;
        border: 1px solid rgba(248, 113, 113, 0.4);
    }}

    /* DECISION FRAMEWORK ROW */
    .decision-row {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 12px;
    }}
    .decision-pill {{
        display: flex;
        align-items: flex-start;
        gap: 14px;
        background: #0e172c;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 12px 16px;
    }}
    .tag-label {{
        display: inline-block;
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 800;
        padding: 4px 10px;
        border-radius: 6px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        white-space: nowrap;
        margin-top: 2px;
    }}
    .tag-why {{
        background: rgba(245, 158, 11, 0.2);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.5);
    }}
    .tag-for {{
        background: rgba(56, 189, 248, 0.2);
        color: #38bdf8;
        border: 1px solid rgba(56, 189, 248, 0.5);
    }}
    .tag-so {{
        background: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.5);
    }}
    .decision-text {{
        font-size: 14px;
        line-height: 1.48;
        color: #cbd5e1;
        font-weight: 500;
    }}
    .decision-text strong {{
        color: #ffffff;
    }}

    /* GRIDS */
    .grid-2 {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 10px;
    }}
    .grid-3 {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 10px;
        margin-bottom: 10px;
    }}
    .grid-4 {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 10px;
        margin-bottom: 10px;
    }}

    .big-stat {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 32px;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -1px;
        margin-bottom: 3px;
    }}
    .big-stat.cyan {{ color: #38bdf8; }}
    .big-stat.emerald {{ color: #34d399; }}
    .big-stat.amber {{ color: #fbbf24; }}
    .big-stat.red {{ color: #f87171; }}

    .stat-title {{
        font-size: 13px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 2px;
    }}
    .stat-subtitle {{
        font-size: 12px;
        color: #94a3b8;
        line-height: 1.35;
    }}

    /* DASHBOARD WINDOW BEZEL */
    .dashboard-window {{
        background: #0a0f1d;
        border: 1px solid rgba(148, 163, 184, 0.3);
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 12px;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.45);
    }}
    .window-header {{
        background: #151f38;
        padding: 8px 14px;
        display: flex;
        align-items: center;
        gap: 8px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .window-dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
    }}
    .dot-red {{ background: #ef4444; }}
    .dot-yellow {{ background: #f59e0b; }}
    .dot-green {{ background: #10b981; }}
    .window-title {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 12px;
        font-weight: 600;
        color: #94a3b8;
        margin-left: 6px;
    }}
    .dashboard-window img {{
        width: 100%;
        height: 565px;
        object-fit: cover;
        object-position: top center;
        display: block;
    }}

    /* TABLE */
    .bento-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
        margin-top: 4px;
    }}
    .bento-table th {{
        background: #17254a;
        color: #94a3b8;
        text-align: left;
        padding: 8px 12px;
        font-weight: 700;
        font-size: 12px;
        text-transform: uppercase;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .bento-table td {{
        padding: 8px 12px;
        color: #e2e8f0;
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
        font-size: 13px;
    }}
    .bento-table tr:last-child td {{
        border-bottom: none;
    }}

    /* FOOTER */
    .slide-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        border-top: 1px solid rgba(148, 163, 184, 0.15);
        padding-top: 14px;
    }}
    .author-badge {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .author-avatar {{
        width: 42px;
        height: 42px;
        border-radius: 50%;
        overflow: hidden;
        border: 2px solid #38bdf8;
        background: #1e293b;
    }}
    .author-avatar img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .author-name {{
        font-weight: 800;
        font-size: 14px;
        color: #ffffff;
    }}
    .author-role {{
        font-size: 11px;
        color: #38bdf8;
        font-weight: 600;
        letter-spacing: 0.3px;
    }}
    .next-cta {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #15223d;
        border: 1px solid rgba(56, 189, 248, 0.4);
        color: #ffffff;
        padding: 7px 18px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.3px;
    }}
    .next-cta span {{
        color: #38bdf8;
    }}
</style>
</head>
<body>

<!-- ======================================================== -->
<!-- SLIDE 01: THE HOOK & PARADOX -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide1">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Case Study</span> • Retail F&amp;B Multi-Branch Analytics</div>
        <div class="slide-number">01 / 10</div>
    </div>

    <div class="slide-body">
        <!-- AUTHOR PROFILE HERO (TOP CENTER - CLEAN & PROMINENT) -->
        <div class="author-hero-container">
            <div class="author-hero-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div class="author-hero-name">{author_name}</div>
            <div class="author-hero-role">{author_role}</div>
        </div>

        <div class="slide-category" style="justify-content: center;">Portfolio Project 1 • Business Intelligence Case Study</div>
        
        <div class="hook-title" style="text-align: center; font-size: 35px; margin-bottom: 12px;">
            Revenue Rp 4,89 Miliar,<br>
            Tapi Ada <span class="amber">Kebocoran Laba Rp 254 Juta</span><br>
            di Bawah Radar?
        </div>
        
        <div class="subtitle-text" style="text-align: center; max-width: 920px; margin: 0 auto 16px auto;">
            Menganalisis 85.020 transaksi pesanan di 18 cabang Jabodetabek. Margin rata-rata konsorsium tampak sehat di <strong>33,8%</strong>. Namun bedah data membuktikan 4 cabang mengalami pendarahan laba struktural akibat 3 akar masalah yang berbeda.
        </div>

        <div class="grid-4">
            <div class="bento-card">
                <div class="stat-title">Skala Jaringan</div>
                <div class="big-stat cyan">18</div>
                <div class="stat-subtitle">Cabang aktif di Jabodetabek</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Total Transaksi</div>
                <div class="big-stat emerald">81.560</div>
                <div class="stat-subtitle">Pesanan valid diselesaikan</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Gross Revenue</div>
                <div class="big-stat cyan">4,89M</div>
                <div class="stat-subtitle">April–September 2026</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Kebocoran Laba</div>
                <div class="big-stat amber">254Jt</div>
                <div class="stat-subtitle">Potensi dividen tahunan</div>
            </div>
        </div>

        <div class="bento-card highlight" style="margin-top: 4px;">
            <div class="stat-title" style="color: #38bdf8; font-size: 14px; margin-bottom: 4px;">
                🎯 Nilai Tambah yang Ditonjolkan dalam Portofolio Ini:
            </div>
            <div style="font-size: 13px; line-height: 1.5; color: #cbd5e1;">
                Bukan sekadar keahlian membuat grafik, dokumen ini mendokumentasikan <strong>pola pikir pengambilan keputusan analitis</strong>: mengapa memilih langkah tertentu, untuk apa, dan dampak nyata apa yang dihasilkan bagi profitabilitas bisnis manajemen.
            </div>
        </div>
    </div>

    <!-- FOOTER SLIDE 1 (CLEAN NAVIGATION - NO DUPLICATE AVATAR) -->
    <div class="slide-footer">
        <div style="font-size: 13px; font-weight: 700; color: #94a3b8; display: flex; align-items: center; gap: 8px;">
            <span style="color: #38bdf8;">👤 Author:</span> {author_name} • Portfolio Project 1
        </div>
        <div class="next-cta">Bedah Pola Pikir Data Cleaning <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 02: DATA INTEGRITY & CLEANING PHILOSOPHY -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide2">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Data Integrity</span> • Logika Pembersihan Data</div>
        <div class="slide-number">02 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Filosofi Pembersihan Data • Integritas Analisis</div>
        <div class="hook-title">
            Mengapa Data Kosong <span class="cyan">SENGAJA Dibiarkan</span>, Bukan Diisi Nilai Rata-Rata?
        </div>
        <div class="subtitle-text">
            Kesalahan umum pemula adalah memaksakan pengisian nilai kosong (imputasi rata-rata) agar tabel tampak penuh. Pada data transaksi ritel riil, tindakan tersebut justru memanipulasi fakta lapangan.
        </div>

        <div class="decision-row">
            <div class="decision-pill">
                <span class="tag-label tag-why">Mengapa (Why)</span>
                <div class="decision-text">
                    Kolom <code>customer_id</code> yang kosong adalah <strong>catatan bukti riil transaksi anonim (walk-in kasir tanpa kartu member)</strong>. Nilai kosong tersebut mencerminkan perilaku pelanggan nyata di restoran fisik, bukan kesalahan input sistem.
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-for">Untuk Apa (What For)</span>
                <div class="decision-text">
                    Untuk <strong>memisahkan secara tegas</strong> segmen pelanggan loyal (terdata) dari pembeli walk-in. Nilai kosong tidak diisi rata-rata, melainkan dialokasikan ke entitas khusus <code>Guest/Walk-in</code> agar histori transaksi tetap murni 100%.
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-so">Supaya Apa (Dampak Nyata)</span>
                <div class="decision-text">
                    <strong>Supaya metrik retensi pelanggan, frekuensi beli, dan Customer Lifetime Value (LTV) tidak terdistorsi!</strong> Mengisi nilai rata-rata akan menciptakan 'pelanggan fiktif' dengan ribuan pesanan palsu yang merusak akurasi strategi promosi manajemen.
                </div>
            </div>
        </div>

        <div class="grid-2">
            <div class="bento-card danger">
                <div class="stat-title" style="color: #f87171;">❌ Jika Dipaksakan Isi Rata-Rata (Mean Imputation):</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Mendistorsi sebaran data, menyamarkan transaksi anonim, dan menghasilkan rekomendasi retensi pelanggan yang salah kaprah.
                </div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">✅ Dikelola Sesuai Kategori Guest/Walk-in:</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Menjaga kejujuran data transaksi 100%, memungkinkan manajemen membandingkan tren belanja member vs non-member secara objektif.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Lihat Dashboard Halaman 1 <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 03: DASHBOARD HALAMAN 1 - EXECUTIVE OVERVIEW -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide3">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Power BI Page 1</span> • Executive Overview</div>
        <div class="slide-number">03 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Visualisasi Interaktif • 18 Cabang</div>
        <div class="hook-title" style="font-size: 34px;">
            Halaman 1: Memetakan <span class="amber">Disparitas Margin</span> di 18 Cabang
        </div>

        <div class="dashboard-window">
            <div class="window-header">
                <div class="window-dot dot-red"></div>
                <div class="window-dot dot-yellow"></div>
                <div class="window-dot dot-green"></div>
                <div class="window-title">Power BI Service • 01_Executive_Overview.pbix</div>
            </div>
            <img src="{overview_img_uri}" alt="Power BI Overview Dashboard">
        </div>

        <div class="grid-2">
            <div class="bento-card">
                <div class="stat-title" style="color: #38bdf8;">Fokus Temuan Data (Kaca Pembesar):</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Perhatikan grafik batang di tengah: margin rata-rata 33,8% menyembunyikan jurang performa ekstrem: Cabang Kelapa Gading (<strong>23,9%</strong>) tertinggal 16,9% di bawah Benchmark Cinere (<strong>40,8%</strong>).
                </div>
            </div>
            <div class="bento-card">
                <div class="stat-title" style="color: #34d399;">Keputusan Manajemen:</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Mencegah kebijakan potong anggaran secara pukul rata. Upaya perbaikan difokuskan secara presisi hanya pada 4 cabang yang terbukti berdarah.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Bedah 4 Cabang Kritis <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 04: THE ROOT CAUSE MATRIX -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide4">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Diagnosa Operasional</span> • Analisis Multi-Cabang</div>
        <div class="slide-number">04 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Investigasi Akar Masalah • Presisi Solusi</div>
        <div class="hook-title">
            4 Cabang Kritis Mengidap <span class="red">3 Masalah Operasional</span> yang Berbeda
        </div>
        <div class="subtitle-text">
            Solusi seragam tidak akan menyelesaikan masalah. Setiap cabang memerlukan penanganan operasional yang spesifik:
        </div>

        <div class="bento-card danger" style="padding: 12px 16px;">
            <table class="bento-table">
                <thead>
                    <tr>
                        <th>Cabang</th>
                        <th>Net Margin</th>
                        <th>Akar Masalah Utama</th>
                        <th>Karakter Diagnosa Lapangan</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Kelapa Gading (BR03)</strong></td>
                        <td><span style="color: #f87171; font-weight:800;">23,9%</span></td>
                        <td>Biaya Tenaga Kerja (Labor 30,5%)</td>
                        <td>Overstaffing struktural saat jam sepi</td>
                    </tr>
                    <tr>
                        <td><strong>BSD (BR05)</strong></td>
                        <td><span style="color: #f87171; font-weight:800;">28,1%</span></td>
                        <td>Markup Bahan (+24%) &amp; Waste (5,6%)</td>
                        <td>Inefisiensi ganda (vendor &amp; dapur)</td>
                    </tr>
                    <tr>
                        <td><strong>Tangerang (BR11)</strong></td>
                        <td><span style="color: #fbbf24; font-weight:800;">30,5%</span></td>
                        <td>Harga Bahan (+14%) &amp; Waste (4,8%)</td>
                        <td>Food waste akibat portioning &amp; vendor mahal</td>
                    </tr>
                    <tr>
                        <td><strong>Sentul (BR13)</strong></td>
                        <td><span style="color: #fbbf24; font-weight:800;">32,3%</span></td>
                        <td>Murni Markup Supplier Lokal</td>
                        <td>Dapur sangat hemat &amp; terkontrol presisi</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="decision-pill" style="margin-top: 6px;">
            <span class="tag-label tag-so">Catatan Analis</span>
            <div class="decision-text">
                Mengirim tim audit ke dapur Sentul adalah pemborosan waktu karena dapurnya sudah sangat hemat. Masalah Sentul ada di <strong>kontrak supplier lokal</strong>, sedangkan masalah Kelapa Gading ada di <strong>penjadwalan shift kerja staf</strong>.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Validasi Uji Statistik Z-Score <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 05: STATISTICAL RIGOR (Z-SCORE) & DASHBOARD 2 -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide5">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Power BI Page 2</span> • Validasi Statistik</div>
        <div class="slide-number">05 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Statistik Inferensial • Uji Deviasi Standar</div>
        <div class="hook-title" style="font-size: 32px;">
            Halaman 2: Validasi <span class="cyan">Uji Statistik Z-Score</span> untuk Menguji Anomali
        </div>

        <div class="dashboard-window">
            <div class="window-header">
                <div class="window-dot dot-red"></div>
                <div class="window-dot dot-yellow"></div>
                <div class="window-dot dot-green"></div>
                <div class="window-title">Power BI Service • 02_Root_Cause_ZScore.pbix</div>
            </div>
            <img src="{root_cause_img_uri}" alt="Power BI Root Cause Dashboard">
        </div>

        <div class="grid-3">
            <div class="bento-card">
                <div class="stat-title">Labor BR03</div>
                <div class="big-stat red">+8,3σ</div>
                <div class="stat-subtitle">Biaya gaji 8x di luar batas normal</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Sourcing BR05</div>
                <div class="big-stat red">+27,7σ</div>
                <div class="stat-subtitle">Harga beli 27x di luar batas wajar</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Waste BR05</div>
                <div class="big-stat amber">+24,6σ</div>
                <div class="stat-subtitle">Bahan terbuang tertinggi di jaringan</div>
            </div>
        </div>

        <div class="decision-pill">
            <span class="tag-label tag-why">Arti Bisnis Z-Score</span>
            <div class="decision-text" style="font-size: 13px;">
                Z-Score memisahkan perdebatan opini subjektif. Nilai deviasi di atas <strong>+3,0σ</strong> membuktikan secara ilmiah bahwa angka tersebut adalah anomali sistemik yang mustahil terjadi secara kebetulan, sehingga wajib diintervensi oleh manajemen.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Paradoks Cabang Baru (BR18) <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 06: DASHBOARD HALAMAN 3 - CABANG BARU (BR18) -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide6">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Power BI Page 3</span> • Konteks Bisnis Riil</div>
        <div class="slide-number">06 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Kedewasaan Analitis • Dinamika Pertumbuhan</div>
        <div class="hook-title" style="font-size: 32px;">
            Halaman 3: Paradoks Cabang Baru — Keputusan: <span class="emerald">Tahan Intervensi</span>
        </div>

        <div class="dashboard-window">
            <div class="window-header">
                <div class="window-dot dot-red"></div>
                <div class="window-dot dot-yellow"></div>
                <div class="window-dot dot-green"></div>
                <div class="window-title">Power BI Service • 03_Cabang_Baru_BR18.pbix</div>
            </div>
            <img src="{cabang_baru_img_uri}" alt="Power BI Cabang Baru BR18 Dashboard">
        </div>

        <div class="bento-card success" style="padding: 14px 18px;">
            <div class="stat-title" style="color: #34d399; font-size: 14px;">
                🛡️ Mengapa Cabang Summarecon Bekasi (BR18) Tidak Boleh Dipotong Budget?
            </div>
            <div style="font-size: 13px; line-height: 1.52; color: #cbd5e1; margin-top: 4px;">
                Margin rata-rata BR18 rendah (<strong>25,0%</strong>) dan sempat dinilai bermasalah. Namun analisis tren membuktikan ini adalah <strong>kurva pertumbuhan alami (ramp-up curve)</strong>: Juni 19,9% ➔ Juli 23,5% ➔ Agustus 27,4% ➔ September <strong>29,1%</strong>. Intervensi tergesa-gesa (seperti memangkas staf) justru akan menurunkan kualitas pelayanan di gerai baru.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Role Model Benchmark Cinere <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 07: GOLDEN BENCHMARK (CINERE - BR09) -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide7">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Benchmark Model</span> • Standar Keunggulan</div>
        <div class="slide-number">07 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Replikasi Praktik Terbaik • Efisiensi Operasional</div>
        <div class="hook-title">
            Role Model Operasional: Rahasia Margin 40,8% <span class="emerald">Cabang Cinere (BR09)</span>
        </div>
        <div class="subtitle-text">
            Bukan sekadar menemukan masalah, analis harus menghadirkan tolok ukur solusi. Cabang Cinere membuktikan bahwa margin 40%+ dapat dicapai secara berkelanjutan di wilayah Jabodetabek:
        </div>

        <div class="grid-3">
            <div class="bento-card highlight">
                <div class="stat-title">Net Margin Konsisten</div>
                <div class="big-stat emerald">40,8%</div>
                <div class="stat-subtitle">Tertinggi dan paling stabil di konsorsium</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Sourcing Z-Score</div>
                <div class="big-stat emerald">-13,0σ</div>
                <div class="stat-subtitle">Disiplin harga beli bahan baku</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Waste Dapur</div>
                <div class="big-stat emerald">-10,7σ</div>
                <div class="stat-subtitle">SOP porsi presisi, minim bahan terbuang</div>
            </div>
        </div>

        <div class="decision-row">
            <div class="decision-pill">
                <span class="tag-label tag-why">Mengapa Cinere?</span>
                <div class="decision-text">
                    Membantah anggapan bahwa *"biaya operasional Jabodetabek memang mahal"*. Cinere bukan cabang sepi; volumenya berada di kuartil atas jaringan, membuktikan efisiensinya murni lahir dari kedisiplinan operasional, bukan anomali volume pesanan.
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-so">Supaya Apa?</span>
                <div class="decision-text">
                    SOP dapur dan jadwal shift Cinere dijadikan <strong>acuan standar konsorsium</strong> untuk direplikasi ke 4 cabang yang berdarah tanpa perlu berspekulasi.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Roadmap Eksekusi 30 Hari <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 08: 30-DAY ACTIONABLE ROADMAP -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide8">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Execution Plan</span> • Rekomendasi Bisnis Nyata</div>
        <div class="slide-number">08 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Rekomendasi Bisnis Nyata • Eksekusi Taktis</div>
        <div class="hook-title">
            Roadmap 30 Hari: Transformasi Data Menjadi <span class="cyan">Tindakan Operasional Nyata</span>
        </div>
        <div class="subtitle-text">
            Rekomendasi dirancang ke dalam 4 sprint mingguan terukur agar tim operasional dapat segera mengeksekusinya:
        </div>

        <div class="bento-card" style="padding: 14px 18px;">
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #1e3a8a; color: #60a5fa; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 1</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Triage Shift &amp; Rasio Staf di Kelapa Gading (BR03):</strong> Pangkas jam kerja kosong pada waktu sepi (14.00–17.00), sesuaikan jumlah staf dengan pola pesanan per jam.
                    </div>
                </div>
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #1e3a8a; color: #60a5fa; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 2</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Renegosiasi Kontrak Supplier BSD, Tangerang &amp; Sentul:</strong> Samakan harga kontrak bahan baku dengan vendor regional Cinere, eliminasi markup lokal 24%.
                    </div>
                </div>
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #1e3a8a; color: #60a5fa; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 3</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Standardisasi Porsi Dapur &amp; Kontrol Waste:</strong> Pelatihan ulang portioning tim dapur di BSD &amp; Tangerang mengadopsi standar porsi presisi Cinere.
                    </div>
                </div>
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #065f46; color: #34d399; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 4</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Monitoring &amp; Alerting Otomatis di Power BI:</strong> Pasang batas toleransi biaya otomatis; notifikasi dikirim jika margin harian menyimpang lebih dari 2σ.
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Hitung Dampak Finansial <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 09: FINANCIAL IMPACT & ROI -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide9">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Financial Impact</span> • Pemulihan Laba Bersih</div>
        <div class="slide-number">09 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Dampak Finansial Nyata • Nilai Tambah Bisnis</div>
        <div class="hook-title">
            Dampak Finansial: Menyelamatkan <span class="emerald">~Rp 254 Juta Laba Bersih</span> per Tahun
        </div>
        <div class="subtitle-text">
            Dihitung dari selisih pemborosan riil 4 cabang terhadap biaya standar benchmark Cinere pada volume pesanan yang sama:
        </div>

        <div class="grid-2">
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Kelapa Gading (BR03)</div>
                <div class="big-stat emerald">+Rp 97 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Penataan shift kerja &amp; efisiensi staf</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">BSD (BR05)</div>
                <div class="big-stat emerald">+Rp 68 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Renegosiasi supplier &amp; kontrol porsi dapur</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Tangerang (BR11)</div>
                <div class="big-stat emerald">+Rp 53 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Standardisasi porsi &amp; perbaikan kontrak bahan</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Sentul (BR13)</div>
                <div class="big-stat emerald">+Rp 36 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Eliminasi markup harga vendor lokal</div>
            </div>
        </div>

        <div class="bento-card highlight" style="text-align: center; padding: 14px 20px;">
            <div style="font-size: 13px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">
                Total Pemulihan Laba Bersih Tahunan (Bottom-Line Recovery):
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 38px; font-weight: 900; color: #34d399; margin: 4px 0;">
                ~Rp 254.000.000 / Tahun
            </div>
            <div style="font-size: 13px; color: #cbd5e1;">
                Setara dengan dividen laba membuka 2 cabang baru tanpa risiko modal Capex!
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta">Lihat Codebase di GitHub <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 10: REFINED CTA TO GITHUB & RECRUITMENT -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide10">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Codebase &amp; Portfolio</span> • Eksplorasi Lengkap</div>
        <div class="slide-number">10 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Dokumentasi Terbuka • Kolaborasi &amp; Rekrutmen</div>
        <div class="hook-title" style="font-size: 35px;">
            Tertarik Mendalami Analisis Ini? <span class="cyan">Eksplorasi Lengkap di GitHub!</span>
        </div>
        <div class="subtitle-text">
            Seluruh pipeline pembersihan data, file visualisasi Power BI, dan metodologi audit terbuka secara transparan di repositori publik:
        </div>

        <!-- HERO GITHUB CARD -->
        <div class="bento-card highlight" style="padding: 16px 20px; border-color: rgba(56, 189, 248, 0.6); background: #13274f;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 26px;">📂</span>
                    <div>
                        <div style="font-size: 12px; font-weight: 700; color: #38bdf8; text-transform: uppercase; letter-spacing: 0.5px;">GitHub Public Repository</div>
                        <div style="font-size: 16px; font-weight: 800; color: #ffffff;">Retail-Branch-Profitability-Analysis</div>
                    </div>
                </div>
                <div style="background: rgba(56, 189, 248, 0.2); border: 1px solid #38bdf8; color: #38bdf8; font-size: 11px; font-weight: 800; padding: 4px 10px; border-radius: 6px;">
                    OPEN SOURCE
                </div>
            </div>
            
            <div style="background: #091224; border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 10px 14px; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #38bdf8; word-break: break-all; margin: 8px 0;">
                https://github.com/fajarsetyadilucky/Retail-Branch-Profitability-Analysis
            </div>

            <div style="font-size: 12px; color: #38bdf8; font-weight: 600; margin-bottom: 6px;">
                🔗 Link aktif &amp; file .pbix asli dapat langsung diklik pada caption postingan di atas 👆
            </div>

            <div style="font-size: 12px; color: #94a3b8; display: flex; gap: 16px;">
                <span>📊 Dashboard File (.PBIX Asli)</span>
                <span>🐍 Python Cleaning Pipeline</span>
                <span>📑 Metodologi Audit Z-Score</span>
            </div>
        </div>

        <div class="grid-2" style="margin-top: 4px;">
            <div class="bento-card" style="padding: 14px 18px;">
                <div class="stat-title" style="color: #38bdf8; font-size: 14px;">Kompetensi yang Ditawarkan:</div>
                <ul style="font-size: 12px; color: #cbd5e1; line-height: 1.6; margin-left: 16px; margin-top: 6px;">
                    <li><strong>Integritas Data:</strong> Menolak manipulasi data tanpa dasar.</li>
                    <li><strong>Statistik Terapan:</strong> Validasi deviasi objektif (Z-Score).</li>
                    <li><strong>Data Modeling:</strong> Star Schema 1:N &amp; DAX Measures.</li>
                    <li><strong>Bisnis Nyata:</strong> Menghubungkan analitik ke margin &amp; profit.</li>
                </ul>
            </div>
            <div class="bento-card success" style="padding: 14px 18px;">
                <div class="stat-title" style="color: #34d399; font-size: 14px;">Kontak Langsung Kandidat:</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.7; margin-top: 6px;">
                    <div>👤 <strong>{author_name}</strong></div>
                    <div>📧 <strong>Email:</strong> {author_email}</div>
                    <div>💬 <strong>WhatsApp:</strong> {author_wa_formatted}</div>
                    <div style="color: #34d399; font-weight: 700; margin-top: 4px;">🟢 Siap untuk Posisi Full-Time / Kontrak</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">{author_role}</div>
            </div>
        </div>
        <div class="next-cta" style="background: #0284c7; border-color: #38bdf8;">Kunjungi Repositori GitHub! <span>🚀</span></div>
    </div>
</div>

</body>
</html>
"""

# Write HTML preview file
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"HTML preview written to: {html_file}")

# Render multi-page PDF using Chrome Headless
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(chrome_path):
    chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

cmd_pdf = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file}",
    str(html_file)
]

print("Rendering multi-page PDF with Chrome...")
res_pdf = subprocess.run(cmd_pdf, capture_output=True)
if pdf_file.exists():
    print(f"LinkedIn Carousel PDF generated: {pdf_file} (Size: {os.path.getsize(pdf_file)} bytes)")
    shutil.copyfile(pdf_file, pdf_root)
    print(f"Copied PDF to root: {pdf_root}")
    pdf_bi.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(pdf_file, pdf_bi)
    print(f"Copied PDF to BI folder: {pdf_bi}")
else:
    print("Warning: PDF file was not created. Error output:", res_pdf.stderr)

# Clean existing PNG files in CAROUSEL_DIR
for old_png in CAROUSEL_DIR.glob("*.png"):
    try:
        old_png.unlink()
    except Exception:
        pass

# Generate individual PNG slides for each of the 10 slides
print("Rendering individual PNG slides for LinkedIn...")
for i in range(1, 11):
    slide_html = REPORTS_DIR / f"temp_carousel_slide_{i}.html"
    slide_png = CAROUSEL_DIR / f"slide_{i:02d}.png"
    
    parts = html_content.split(f'id="slide{i}"')
    if len(parts) > 1:
        head = html_content.split('<div class="slide-wrapper" id="slide1">')[0]
        if i < 10:
            slide_body = '<div class="slide-wrapper" id="slide' + str(i) + '"' + parts[1].split('<!-- ======================================================== -->')[0]
        else:
            slide_body = '<div class="slide-wrapper" id="slide10"' + parts[1].split('</body>')[0]
            
        single_html = head + slide_body + "</body></html>"
        slide_html.write_text(single_html, encoding="utf-8")
        
        cmd_img = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--window-size=1080,1350",
            f"--screenshot={slide_png}",
            str(slide_html)
        ]
        subprocess.run(cmd_img, capture_output=True)
        if slide_html.exists():
            slide_html.unlink()
        print(f"Slide {i:02d} PNG generated: {slide_png.name} (Exists: {slide_png.exists()})")

# Generate LinkedIn Post Caption / Copy tailored for HR & Decision Making
post_copy = f"""Banyak praktisi data terjebak pada ilusi rata-rata: "Margin jaringan 33,8%, bisnis tampak sehat."
Namun saat data dibedah secara mendalam, ditemukan kebocoran laba Rp 254 Juta di 4 cabang dengan 3 masalah operasional yang berbeda total.

Sebagai Data Analyst & Business Intelligence, bagi saya data bukan sekadar grafik yang indah di layar—melainkan pola pikir pengambilan keputusan: MENGAPA melakukan sesuatu, UNTUK APA, dan DAMPAK BISNIS NYATA APA yang dihasilkan bagi manajemen.

Berikut 4 sorotan analitis dalam studi kasus ini:

1️⃣ Integritas Pembersihan Data (The Data Cleaning Philosophy):
Mengapa baris/kolom kosong SENGAJA dibiarkan dan dilarang diisi nilai rata-rata (mean imputation)?
Pada data transaksi, kolom customer_id kosong adalah bukti riil transaksi anonim (guest checkout / walk-in kasir). Mengisi nilai rata-rata justru akan menciptakan 'pelanggan fiktif' dan merusak analisis Customer Retention, LTV, serta segmentasi promosi. Kejujuran data menjaga keputusan manajemen tetap akurat.

2️⃣ Uji Statistik Deviasi (Z-Score Validation):
Menghindari keputusan 'pukul rata'. Dengan Z-Score, anomali divalidasi secara objektif:
• Kelapa Gading (BR03): Margin 23,9% ➔ Masalah Tenaga Kerja (Labor Z = +8,3σ).
• BSD (BR05): Margin 28,1% ➔ Markup Bahan Baku (Z = +27,7σ) & Bahan Terbuang di Dapur (Z = +24,6σ).
• Sentul (BR13): Margin 32,3% ➔ Murni markup vendor lokal (dapur sangat disiplin).

3️⃣ Kedewasaan Analitis: Keputusan Menahan Intervensi pada Cabang Baru:
Cabang Summarecon Bekasi (BR18) sempat dinilai bermasalah karena margin 25,0%. Namun analisis tren membuktikan ini adalah kurva pertumbuhan alami (ramp-up curve: 19,9% ➔ 29,1% dalam 4 bulan). Keputusan tepat: jangan diintervensi tergesa-gesa!

4️⃣ Rekomendasi Nyata & Pemulihan Finansial:
Mengadopsi blueprint cabang benchmark (Cinere - BR09, margin 40,8%) dan mengeksekusi Roadmap Taktis 30 Hari memulihkan potensi laba bersih ~Rp 254 JUTA / TAHUN tanpa perlu menambah modal gerai baru.

👉 Geser 10 slide dokumen carousel di atas untuk melihat 3 halaman dashboard lengkap Power BI, scatter plot Z-Score, dan arsitektur analitiknya!

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 Eksplorasi Dashboard Asli & Codebase Lengkap di GitHub:
{github_url}

📬 Terbuka untuk Diskusi & Peluang Kerja (Full-time / Kontrak):
👤 {author_name} | {author_role}
📧 {author_email}
💬 WhatsApp: {author_wa_formatted} (https://wa.me/62{author_wa[1:]})

Bagaimana pendekatan rekan-rekan dalam menjaga integritas data saat menghadapi transaksi anonim? Mari berdiskusi di kolom komentar! 👇

#BusinessIntelligence #DataAnalytics #DataStorytelling #PowerBI #DecisionIntelligence #RetailAnalytics #RootCauseAnalysis #DataIntegrity #HiringDataAnalyst #JobSeeker
"""

with open(post_copy_file, "w", encoding="utf-8") as f:
    f.write(post_copy)
print(f"LinkedIn Post Copy written to {post_copy_file}")

print("All 10 LinkedIn Carousel slides, PDF, and Post Copy generated successfully!")
