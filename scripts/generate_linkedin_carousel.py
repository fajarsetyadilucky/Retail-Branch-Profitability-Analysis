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
author_email = "Fajarsetyadilucky@gmail.com"
author_wa = "089630527099"
author_wa_formatted = "0896-3052-7099"

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8">
<title>LinkedIn Carousel - RANTING Multi-Branch F&B Performance Optimization</title>
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
        font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
        background: #080d1a;
        color: #f1f5f9;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}

    /* SLIDE CANVAS */
    .slide-wrapper {{
        width: 1080px;
        height: 1350px;
        padding: 44px 52px 36px 52px;
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

    /* SUBTLE GEOMETRIC ACCENTS (NO NEON GLOW) */
    .grid-bg {{
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-image: linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
    }}

    /* SLIDE HEADER */
    .slide-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        margin-bottom: 12px;
    }}
    .tag-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(30, 41, 59, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.3);
        color: #94a3b8;
        padding: 6px 16px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}
    .tag-badge .accent {{
        color: #38bdf8;
    }}
    .slide-number {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        font-weight: 800;
        color: #64748b;
        background: #0f172a;
        padding: 5px 14px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    /* SLIDE BODY */
    .slide-body {{
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        z-index: 10;
        padding-top: 4px;
    }}

    /* HEADINGS */
    .slide-category {{
        font-size: 14px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #38bdf8;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .hook-title {{
        font-size: 40px;
        font-weight: 900;
        line-height: 1.18;
        letter-spacing: -1.2px;
        color: #ffffff;
        margin-bottom: 14px;
    }}
    .hook-title span.emerald {{ color: #10b981; }}
    .hook-title span.amber {{ color: #f59e0b; }}
    .hook-title span.cyan {{ color: #38bdf8; }}
    .hook-title span.red {{ color: #f87171; }}

    .subtitle-text {{
        font-size: 17px;
        line-height: 1.5;
        color: #94a3b8;
        font-weight: 500;
        margin-bottom: 16px;
    }}

    /* BENTO BOX CONTAINERS */
    .bento-card {{
        background: #111c38;
        border: 1px solid rgba(148, 163, 184, 0.18);
        border-radius: 14px;
        padding: 16px 20px;
        margin-bottom: 12px;
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

    /* DECISION TAGS: WHY / WHAT FOR / SO WHAT */
    .decision-row {{
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-bottom: 14px;
    }}
    .decision-pill {{
        display: flex;
        align-items: flex-start;
        gap: 12px;
        background: #0f172a;
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
        font-size: 15px;
        line-height: 1.45;
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
        margin-bottom: 12px;
    }}
    .grid-3 {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 10px;
        margin-bottom: 12px;
    }}
    .grid-4 {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 10px;
        margin-bottom: 12px;
    }}

    .big-stat {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 34px;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -1px;
        margin-bottom: 4px;
    }}
    .big-stat.cyan {{ color: #38bdf8; }}
    .big-stat.emerald {{ color: #34d399; }}
    .big-stat.amber {{ color: #fbbf24; }}
    .big-stat.red {{ color: #f87171; }}

    .stat-title {{
        font-size: 13px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 3px;
    }}
    .stat-subtitle {{
        font-size: 12px;
        color: #94a3b8;
        line-height: 1.35;
    }}

    /* APP WINDOW FRAME FOR DASHBOARD SCREENSHOTS */
    .dashboard-window {{
        background: #0a0f1d;
        border: 1px solid rgba(148, 163, 184, 0.3);
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 14px;
        box-shadow: 0 12px 32px rgba(0, 0, 0, 0.45);
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
        height: 520px;
        object-fit: cover;
        object-position: top;
        display: block;
    }}
    .dashboard-window.compact img {{
        height: 480px;
    }}

    /* TABLE STYLES */
    .bento-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 13px;
        margin-top: 6px;
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
        padding: 9px 12px;
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
        padding-top: 16px;
    }}
    .author-badge {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}
    .author-avatar {{
        width: 44px;
        height: 44px;
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
        background: #1e293b;
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
        <div class="tag-badge"><span class="accent">Case Study</span> • Retail F&amp;B Multi-Branch BI</div>
        <div class="slide-number">01 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Decision Intelligence • Profitability Audit</div>
        <div class="hook-title">
            Revenue Rp 4,89 Miliar,<br>
            Tapi Ada <span class="amber">Kebocoran Laba Rp 254 Juta</span><br>
            di Bawah Radar?
        </div>
        <div class="subtitle-text">
            Banyak bisnis ritel &amp; F&amp;B terlena pada angka rata-rata: margin konsorsium tampak sehat di <strong>33,8%</strong>. Namun bedah data membuktikan 4 cabang mengalami pendarahan laba struktural dengan penyakit yang berbeda total!
        </div>

        <div class="grid-4">
            <div class="bento-card">
                <div class="stat-title">Skala Jaringan</div>
                <div class="big-stat cyan">18</div>
                <div class="stat-subtitle">Cabang aktif Jabodetabek</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Transaksi Selesai</div>
                <div class="big-stat emerald">81.560</div>
                <div class="stat-subtitle">Dari 85.020 total order</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Gross Revenue</div>
                <div class="big-stat cyan">4,89M</div>
                <div class="stat-subtitle">April–September 2026</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Kebocoran Laba</div>
                <div class="big-stat amber">254Jt</div>
                <div class="stat-subtitle">Potensi pemulihan tahunan</div>
            </div>
        </div>

        <div class="bento-card highlight" style="margin-top: 6px;">
            <div class="stat-title" style="color: #38bdf8; font-size: 15px; margin-bottom: 8px;">
                🎯 Fokus Portofolio Ini untuk HR &amp; Hiring Manager:
            </div>
            <div style="font-size: 14px; line-height: 1.55; color: #cbd5e1;">
                Bukan sekadar memperlihatkan visual grafik, dokumen ini mendokumentasikan <strong>pola pikir pengambilan keputusan (decision-making framework)</strong> seorang Data Analyst: mengapa memilih teknik ini, untuk apa, dan dampak nyata apa yang dihasilkan bagi profitabilitas bisnis.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
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
        <div class="tag-badge"><span class="accent">Data Integrity</span> • Mindset &amp; Pre-Processing</div>
        <div class="slide-number">02 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Filosofi Pembersihan Data • Integritas Bisnis</div>
        <div class="hook-title">
            Mengapa Baris/Kolom Kosong <span class="cyan">SENGAJA Dibiarkan</span> &amp; Dilarang Diisi Nilai Rata-Rata?
        </div>
        <div class="subtitle-text">
            Kesalahan umum pemula adalah memaksakan <em>mean/mode imputation</em> agar dataset "terlihat penuh". Pada bisnis restoran nyata, keputusan itu fatal dan memanipulasi bukti transaksi.
        </div>

        <div class="decision-row">
            <div class="decision-pill">
                <span class="tag-label tag-why">Mengapa (Why)</span>
                <div class="decision-text">
                    Kolom <code>customer_id</code> kosong adalah <strong>catatan bukti riil transaksi anonim (guest checkout / walk-in kasir)</strong>. Pelanggan datang langsung tanpa kartu membership. Nilai kosong tersebut mencerminkan perilaku transaksi nyata, bukan kegagalan sistem.
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-for">Untuk Apa (What For)</span>
                <div class="decision-text">
                    Untuk <strong>memisahkan secara tegas</strong> segmen pelanggan loyal (terdata) dari pelanggan anonim (non-member). Data anonim dikelompokkan dalam kategori khusus <code>Guest/Walk-in</code>, bukan dipaksa diasosiasikan ke pelanggan tertentu.
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-so">Supaya Apa (Business Impact)</span>
                <div class="decision-text">
                    <strong>Supaya metrik Customer Retention Rate, Frekuensi Kunjungan, dan LTV tidak terdistorsi!</strong> Mengisi nilai rata-rata akan menciptakan 'pelanggan fiktif' dengan ribuan transaksi palsu, yang berakibat fatal pada strategi marketing dan proyeksi promo.
                </div>
            </div>
        </div>

        <div class="grid-2">
            <div class="bento-card danger">
                <div class="stat-title" style="color: #f87171;">❌ Jika Diisi Nilai Rata-Rata:</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Mendistorsi distribusi statistik, menyamarkan transaksi kasir anonim, dan menghasilkan rekomendasi retensi fiktif.
                </div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">✅ Dikelola Sesuai Realitas Lapangan:</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.45; margin-top: 4px;">
                    Menjaga integritas 100% data riil, memungkinkan perbandingan performa member vs non-member secara akurat.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
            Halaman 1: Membongkar <span class="amber">'Ilusi Rata-Rata'</span> di 18 Cabang
        </div>

        <div class="dashboard-window compact">
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
                <div class="stat-title" style="color: #38bdf8;">Mengapa Tampilan Ini Dibuat?</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4; margin-top: 4px;">
                    Memberikan C-Level visibilitas instan bahwa rata-rata 33,8% menyembunyikan jurang lebar: Cabang terendah <strong>23,9%</strong> vs Cabang tertinggi <strong>40,8%</strong>.
                </div>
            </div>
            <div class="bento-card">
                <div class="stat-title" style="color: #34d399;">Supaya Apa (Keputusan Bisnis)?</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4; margin-top: 4px;">
                    Mencegah direksi memotong anggaran secara pukul rata. Intervensi harus difokuskan ke 4 cabang yang berdarah secara spesifik.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Root Cause Analysis</span> • Diagnosa Cabang</div>
        <div class="slide-number">04 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Investigasi Lapangan • Diagnosa Multi-Varian</div>
        <div class="hook-title">
            4 Cabang Kritis Mengidap <span class="red">3 Penyakit Operasional</span> yang Berbeda Total
        </div>
        <div class="subtitle-text">
            Jika manajemen menggunakan solusi seragam, biaya akan terbuang percuma. Setiap cabang memiliki pemicu kebocoran yang unik:
        </div>

        <div class="bento-card danger" style="padding: 12px 16px;">
            <table class="bento-table">
                <thead>
                    <tr>
                        <th>Cabang</th>
                        <th>Net Margin</th>
                        <th>Akar Masalah Utama</th>
                        <th>Karakter Diagnosa</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Kelapa Gading (BR03)</strong></td>
                        <td><span style="color: #f87171; font-weight:800;">23,9%</span></td>
                        <td>Biaya Tenaga Kerja (Labor 30,5%)</td>
                        <td>Overstaffing struktural saat off-peak</td>
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
                        <td>SOP porsi bocor &amp; supplier mahal</td>
                    </tr>
                    <tr>
                        <td><strong>Sentul (BR13)</strong></td>
                        <td><span style="color: #fbbf24; font-weight:800;">32,3%</span></td>
                        <td>Murni Markup Vendor Lokal</td>
                        <td>Dapur sangat disiplin (waste rendah)</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="decision-pill" style="margin-top: 4px;">
            <span class="tag-label tag-so">Insight Analis</span>
            <div class="decision-text">
                Audit dapur di Sentul adalah pemborosan waktu karena dapurnya hemat! Masalah Sentul adalah <strong>kontrak supplier</strong>. Sebaliknya di Kelapa Gading, masalahnya bukan bahan baku, melainkan <strong>penjadwalan shift kasir &amp; waiter</strong>.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Power BI Page 2</span> • Statistical Rigor</div>
        <div class="slide-number">05 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Statistik Inferensial • Uji Deviasi Standar</div>
        <div class="hook-title" style="font-size: 32px;">
            Halaman 2: Validasi <span class="cyan">Uji Statistik Z-Score</span> &amp; Drill-Down Biaya
        </div>

        <div class="dashboard-window compact">
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
                <div class="stat-subtitle">Anomali gaji di atas rata-rata</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Sourcing BR05</div>
                <div class="big-stat red">+27,7σ</div>
                <div class="stat-subtitle">Harga beli bahan baku abnormal</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Waste BR05</div>
                <div class="big-stat amber">+24,6σ</div>
                <div class="stat-subtitle">Bahan terbuang tertinggi di jaringan</div>
            </div>
        </div>

        <div class="decision-pill">
            <span class="tag-label tag-why">Mengapa Z-Score?</span>
            <div class="decision-text" style="font-size: 13px;">
                Z-Score menghilangkan perdebatan opini subjektif. Nilai di atas <strong>+3,0σ</strong> membuktikan secara ilmiah bahwa ini bukan fluktuasi acak, melainkan inefisiensi sistemik yang wajib diintervensi.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Power BI Page 3</span> • Business Acumen</div>
        <div class="slide-number">06 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Kedewasaan Analitis • Konteks Bisnis</div>
        <div class="hook-title" style="font-size: 32px;">
            Halaman 3: Paradoks Cabang Baru — Keputusan <span class="emerald">'DO NOT INTERVENE!'</span>
        </div>

        <div class="dashboard-window compact">
            <div class="window-header">
                <div class="window-dot dot-red"></div>
                <div class="window-dot dot-yellow"></div>
                <div class="window-dot dot-green"></div>
                <div class="window-title">Power BI Service • 03_Cabang_Baru_BR18.pbix</div>
            </div>
            <img src="{cabang_baru_img_uri}" alt="Power BI Cabang Baru BR18 Dashboard">
        </div>

        <div class="bento-card success" style="padding: 12px 18px;">
            <div class="stat-title" style="color: #34d399; font-size: 14px;">
                🛡️ Mengapa Cabang Summarecon Bekasi (BR18) TIDAK BOLEH Diintervensi?
            </div>
            <div style="font-size: 13px; line-height: 1.5; color: #cbd5e1; margin-top: 4px;">
                Margin rata-rata BR18 rendah (<strong>25,0%</strong>) dan sempat dicap merah oleh manajemen. Namun analisis tren membuktikan ini adalah <strong>Ramp-up Curve alami</strong>: Juni 19,9% ➔ Juli 23,5% ➔ Agustus 27,4% ➔ Sept <strong>29,1%</strong>. Intervensi prematur (seperti pemotongan staf) justru akan merusak kepuasan pelanggan baru!
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Benchmark Model</span> • Best Practice Replikasi</div>
        <div class="slide-number">07 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Standarisasi Keunggulan • Operational Excellence</div>
        <div class="hook-title">
            The Golden Benchmark: Membedah DNA Efisiensi <span class="emerald">Cabang Cinere (BR09)</span>
        </div>
        <div class="subtitle-text">
            Bukan sekadar menemukan masalah, analis harus menyediakan solusi nyata. Cabang Cinere membuktikan margin 40%+ dapat dicapai secara berkelanjutan di Jabodetabek:
        </div>

        <div class="grid-3">
            <div class="bento-card highlight">
                <div class="stat-title">Net Margin Konsisten</div>
                <div class="big-stat emerald">40,8%</div>
                <div class="stat-subtitle">Tertinggi dan paling stabil di jaringan</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Sourcing Z-Score</div>
                <div class="big-stat emerald">-13,0σ</div>
                <div class="stat-subtitle">Disiplin harga beli bahan baku</div>
            </div>
            <div class="bento-card">
                <div class="stat-title">Waste Dapur</div>
                <div class="big-stat emerald">-10,7σ</div>
                <div class="stat-subtitle">SOP portioning sangat presisi</div>
            </div>
        </div>

        <div class="decision-row">
            <div class="decision-pill">
                <span class="tag-label tag-why">Mengapa Cinere?</span>
                <div class="decision-text">
                    Menghilangkan alasan manajemen bahwa *"kondisi Jabodetabek memang mahal"*. Cinere beroperasi di demografi serupa namun menghasilkan efisiensi prima di semua variabel (Labor, Sourcing, Waste).
                </div>
            </div>
            <div class="decision-pill">
                <span class="tag-label tag-so">Supaya Apa?</span>
                <div class="decision-text">
                    SOP dapur dan jadwal shift Cinere dijadikan <strong>blueprint standar operasional konsorsium</strong> untuk direplikasi ke 4 cabang kritis.
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Execution Plan</span> • 30-Day Actionable Roadmap</div>
        <div class="slide-number">08 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Rekomendasi Bisnis Nyata • Eksekusi Taktis</div>
        <div class="hook-title">
            Roadmap 30 Hari: Dari Diagnosa Data Menjadi <span class="cyan">Aksi Lapangan Konkret</span>
        </div>
        <div class="subtitle-text">
            Rekomendasi dibagi ke dalam 4 sprint mingguan terukur agar Head of Operations dapat langsung mengeksekusinya:
        </div>

        <div class="bento-card" style="padding: 14px 18px;">
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #1e3a8a; color: #60a5fa; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 1</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Triage Shift &amp; Rasio Headcount di Kelapa Gading (BR03):</strong> Pangkas shift idle pada jam off-peak (14.00–17.00), sinkronkan jumlah staf dengan kurva pesanan per jam.
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
                        <strong>Standardisasi SOP Dapur &amp; Kontrol Waste:</strong> Pelatihan ulang portioning tim dapur di BSD &amp; Tangerang mengadopsi standar zero-waste Cinere.
                    </div>
                </div>
                <div style="display: flex; gap: 14px; align-items: flex-start;">
                    <div style="background: #065f46; color: #34d399; font-weight: 800; font-size: 13px; padding: 4px 10px; border-radius: 6px; white-space: nowrap;">Minggu 4</div>
                    <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                        <strong>Governance &amp; Alerting Otomatis di Power BI:</strong> Pasang threshold otomatis; notifikasi dikirim ke manajer area jika margin harian menyimpang &gt; 2σ.
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
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
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
        <div class="tag-badge"><span class="accent">Financial Recovery</span> • Dividen Pemulihan Laba</div>
        <div class="slide-number">09 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Dampak Bisnis Riil • Nilai Tambah Analis</div>
        <div class="hook-title">
            Dampak Finansial: Menyelamatkan <span class="emerald">~Rp 254 Juta Laba Bersih</span> per Tahun
        </div>
        <div class="subtitle-text">
            Dengan menaikkan performa 4 cabang kritis menuju benchmark Cinere, konsorsium memulihkan dividen tunai tanpa perlu membuka gerai baru:
        </div>

        <div class="grid-2">
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Kelapa Gading (BR03)</div>
                <div class="big-stat emerald">+Rp 97 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Optimalisasi shift &amp; efisiensi headcount</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">BSD (BR05)</div>
                <div class="big-stat emerald">+Rp 68 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Renegosiasi vendor &amp; penurunan waste dapur</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Tangerang (BR11)</div>
                <div class="big-stat emerald">+Rp 53 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Perbaikan SOP porsi &amp; kontrak harga bahan</div>
            </div>
            <div class="bento-card success">
                <div class="stat-title" style="color: #34d399;">Sentul (BR13)</div>
                <div class="big-stat emerald">+Rp 36 Jt<span style="font-size: 18px;">/Thn</span></div>
                <div class="stat-subtitle">Eliminasi markup vendor bahan lokal</div>
            </div>
        </div>

        <div class="bento-card highlight" style="text-align: center; padding: 14px 20px;">
            <div style="font-size: 13px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px;">
                Total Pemulihan Margin Tahunan (Bottom-Line Impact):
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 38px; font-weight: 900; color: #34d399; margin: 4px 0;">
                ~Rp 254.000.000 / Tahun
            </div>
            <div style="font-size: 13px; color: #cbd5e1;">
                Equivalent dengan laba bersih dari membuka 2 gerai baru tanpa resiko modal capex!
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="next-cta">Profil Kandidat &amp; Tautan Codebase <span>👉</span></div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 10: CANDIDATE PROFILE & RECRUITMENT CTA -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide10">
    <div class="grid-bg"></div>
    <div class="slide-header">
        <div class="tag-badge"><span class="accent">Candidate Profile</span> • Ready to Deliver Impact</div>
        <div class="slide-number">10 / 10</div>
    </div>

    <div class="slide-body">
        <div class="slide-category">Rekrutmen &amp; Kesiapan Kerja</div>
        <div class="hook-title" style="font-size: 36px;">
            Siap Membawa <span class="cyan">Keputusan Berbasis Data</span> ke Tim Perusahaan Anda
        </div>

        <div class="bento-card highlight" style="display: flex; gap: 20px; align-items: center; padding: 18px 24px;">
            <div class="author-avatar" style="width: 80px; height: 80px; border-width: 3px; flex-shrink: 0;">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div style="font-size: 22px; font-weight: 800; color: #ffffff;">{author_name}</div>
                <div style="font-size: 14px; font-weight: 700; color: #38bdf8; margin: 2px 0 6px 0;">
                    Data Analyst &amp; Business Intelligence Specialist
                </div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">
                    Berpengalaman menerjemahkan data mentah menjadi keputusan bisnis konkret bernilai ratusan juta rupiah menggunakan Python, SQL, Star Schema, dan Power BI.
                </div>
            </div>
        </div>

        <div class="grid-2">
            <div class="bento-card">
                <div class="stat-title" style="color: #38bdf8;">Kompetensi yang Terbukti:</div>
                <ul style="font-size: 13px; color: #cbd5e1; line-height: 1.6; margin-left: 18px; margin-top: 6px;">
                    <li><strong>Data Integrity:</strong> Menjaga kejujuran data tanpa imputasi buta.</li>
                    <li><strong>Statistical Rigor:</strong> Uji Z-Score untuk validasi anomali.</li>
                    <li><strong>Star Schema DAX:</strong> Relasi 1:N &amp; pipeline 85k order.</li>
                    <li><strong>Business Acumen:</strong> Menghasilkan rekomendasi ROI nyata.</li>
                </ul>
            </div>
            <div class="bento-card">
                <div class="stat-title" style="color: #34d399;">Tautan &amp; Kontak Langsung:</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.7; margin-top: 6px;">
                    <div>📂 <strong>GitHub:</strong> <span style="color: #38bdf8; font-size: 11px;">fajarsetyadilucky/Retail-Branch-Profitability-Analysis</span></div>
                    <div>📧 <strong>Email:</strong> {author_email}</div>
                    <div>💬 <strong>WhatsApp:</strong> {author_wa_formatted}</div>
                    <div style="color: #10b981; font-weight: 700; margin-top: 4px;">🟢 Open for Full-Time / Contract Roles</div>
                </div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-badge">
            <div class="author-avatar"><img src="{author_photo_uri}" alt="{author_name}"></div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="next-cta" style="background: #0284c7; border-color: #38bdf8;">Mari Terhubung di LinkedIn! <span>🚀</span></div>
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
post_copy = f"""Banyak praktisi data terjebak pada Ilusi Rata-Rata: "Margin konsorsium 33,8%, bisnis tampak sehat."
Tapi bagaimana jika bedah data membuktikan ada kebocoran laba Rp 254 Juta di 4 cabang dengan 3 penyakit yang berbeda total?

Sebagai Data Analyst & Business Intelligence Specialist, bagi saya data bukan sekadar grafik yang indah di layar—melainkan pola pikir pengambilan keputusan: MENGAPA melakukan sesuatu, UNTUK APA, dan DAMPAK BISNIS NYATA APA yang dihasilkan.

Berikut beberapa intisari pendekatan analitis dalam project ini:

1️⃣ Integritas Pembersihan Data (The Data Cleaning Philosophy):
Mengapa baris/kolom kosong SENGAJA dibiarkan dan dilarang diisi nilai rata-rata (mean imputation)?
Pada data transaksi, kolom customer_id kosong adalah bukti riil transaksi anonim (guest checkout kasir). Mengisi nilai rata-rata justru akan menciptakan 'pelanggan fiktif' dan merusak analisis Customer Retention, LTV, serta segmentasi pelanggan. Kejujuran data menjaga keputusan bisnis tetap akurat.

2️⃣ Uji Statistik Deviasi (Z-Score Validation):
Menghindari keputusan 'pukul rata'. Dengan Z-Score, anomali divalidasi secara ilmiah:
• Kelapa Gading (BR03): Margin 23,9% ➔ 100% masalah Tenaga Kerja (Labor Z = +8,3σ).
• BSD (BR05): Margin 28,1% ➔ Markup Bahan Baku (Z = +27,7σ) & Waste Dapur (Z = +24,6σ).
• Sentul (BR13): Margin 32,3% ➔ Murni markup vendor lokal (dapur sangat disiplin).

3️⃣ Kedewasaan Analisis: Keputusan "DO NOT INTERVENE" pada Cabang Baru:
Cabang Summarecon Bekasi (BR18) sempat dicap merah karena margin 25,0%. Namun analisis tren membuktikan ini adalah kurva pertumbuhan alami (ramp-up curve: 19,9% ➔ 29,1% dalam 4 bulan). Keputusan tepat: jangan diintervensi!

4️⃣ Rekomendasi Nyata & Dampak Finansial:
Mengadopsi blueprint cabang benchmark (Cinere - BR09, margin 40,8%) dan mengeksekusi Roadmap Taktis 30 Hari memulihkan potensi laba bersih ~Rp 254 JUTA / TAHUN.

👉 Geser 10 slide dokumen carousel di atas untuk melihat 3 halaman dashboard lengkap Power BI, scatter plot Z-Score, dan arsitektur analitiknya!

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 Open-Source Codebase & PBIX:
{github_url}

📬 Open for Discussion & Opportunities (Full-time / Contract):
👤 {author_name} | Data Analyst & Business Intelligence
📧 {author_email}
💬 WhatsApp: {author_wa_formatted} (https://wa.me/62{author_wa[1:]})

Bagaimana pendekatan rekan-rekan dalam menjaga integritas data saat membersihkan dataset kotor? Let's discuss in the comments! 👇

#BusinessIntelligence #DataAnalytics #DataStorytelling #PowerBI #DecisionIntelligence #RetailAnalytics #RootCauseAnalysis #DataIntegrity #HiringDataAnalyst #JobSeeker
"""

with open(post_copy_file, "w", encoding="utf-8") as f:
    f.write(post_copy)
print(f"LinkedIn Post Copy written to {post_copy_file}")

print("All 10 LinkedIn Carousel slides, PDF, and Post Copy generated successfully!")
