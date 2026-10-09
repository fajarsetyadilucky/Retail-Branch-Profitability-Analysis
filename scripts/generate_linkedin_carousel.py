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

github_url = "https://github.com/fajarsetyadilucky/Portfolio_Restaurant_Branch_Optimization"
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
        background: #050811;
        color: #f8fafc;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}

    .slide-wrapper {{
        width: 1080px;
        height: 1350px;
        padding: 44px 56px 38px 56px;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: radial-gradient(circle at 80% 15%, rgba(30, 58, 138, 0.35) 0%, rgba(9, 13, 24, 0.98) 70%), #090d18;
        page-break-after: always;
        break-after: page;
    }}

    /* Glow Orbs */
    .glow-cyan {{
        position: absolute;
        width: 480px;
        height: 480px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.14) 0%, transparent 70%);
        top: -80px;
        right: -80px;
        pointer-events: none;
    }}
    .glow-indigo {{
        position: absolute;
        width: 520px;
        height: 520px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.16) 0%, transparent 70%);
        bottom: -100px;
        left: -100px;
        pointer-events: none;
    }}
    .glow-emerald {{
        position: absolute;
        width: 420px;
        height: 420px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(52, 211, 153, 0.14) 0%, transparent 70%);
        top: 35%;
        right: -100px;
        pointer-events: none;
    }}

    /* SLIDE HEADER */
    .slide-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        margin-bottom: 8px;
    }}
    .tag-badge {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(56, 189, 248, 0.15);
        border: 1px solid rgba(56, 189, 248, 0.45);
        color: #38bdf8;
        padding: 6px 16px;
        border-radius: 100px;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.8px;
        text-transform: uppercase;
    }}
    .slide-number {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 15px;
        font-weight: 800;
        color: #f8fafc;
        background: rgba(255, 255, 255, 0.1);
        padding: 5px 14px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    /* SLIDE BODY */
    .slide-body {{
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        z-index: 10;
        padding: 4px 0;
    }}

    .hook-title {{
        font-size: 40px;
        font-weight: 900;
        line-height: 1.18;
        letter-spacing: -1px;
        color: #ffffff;
        margin-bottom: 10px;
    }}
    .hook-title span.cyan {{
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hook-title span.green {{
        background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hook-title span.amber {{
        background: linear-gradient(135deg, #fbbf24 0%, #f97316 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .hook-title span.red {{
        background: linear-gradient(135deg, #f87171 0%, #ef4444 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .subtitle-text {{
        font-size: 18px;
        line-height: 1.48;
        color: #cbd5e1;
        font-weight: 500;
        margin-bottom: 14px;
    }}

    /* CARDS & CONTAINERS */
    .metric-card {{
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.14);
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 10px;
        position: relative;
    }}
    .metric-card.highlight {{
        background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(56, 189, 248, 0.45);
        box-shadow: 0 8px 24px rgba(56, 189, 248, 0.12);
    }}
    .metric-card.warning {{
        background: linear-gradient(135deg, rgba(180, 83, 9, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(245, 158, 11, 0.45);
    }}
    .metric-card.danger {{
        background: linear-gradient(135deg, rgba(220, 38, 38, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(248, 113, 113, 0.45);
    }}
    .metric-card.success {{
        background: linear-gradient(135deg, rgba(6, 95, 70, 0.3) 0%, rgba(15, 23, 42, 0.9) 100%);
        border: 1px solid rgba(52, 211, 153, 0.45);
    }}

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
        margin-bottom: 10px;
    }}
    .grid-4 {{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr;
        gap: 10px;
        margin-bottom: 10px;
    }}

    .big-number {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 38px;
        font-weight: 800;
        line-height: 1.05;
        letter-spacing: -1px;
        margin-bottom: 4px;
    }}
    .big-number.cyan {{ color: #38bdf8; }}
    .big-number.green {{ color: #34d399; }}
    .big-number.amber {{ color: #fbbf24; }}
    .big-number.red {{ color: #f87171; }}

    .card-label {{
        font-size: 13px;
        font-weight: 800;
        color: #f8fafc;
        margin-bottom: 3px;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }}
    .card-desc {{
        font-size: 14px;
        color: #cbd5e1;
        line-height: 1.4;
    }}

    /* DASHBOARD SCREENSHOT FRAME (WINDOW STYLE) */
    .dashboard-frame {{
        background: #090d18;
        border-radius: 14px;
        border: 1.5px solid rgba(56, 189, 248, 0.45);
        box-shadow: 0 14px 32px rgba(0, 0, 0, 0.6), 0 0 24px rgba(56, 189, 248, 0.15);
        overflow: hidden;
        margin-bottom: 10px;
        position: relative;
    }}
    .dashboard-frame-bar {{
        background: #0f172a;
        padding: 7px 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .dashboard-frame-bar .dots {{
        display: flex;
        gap: 6px;
    }}
    .dashboard-frame-bar .dot {{
        width: 10px;
        height: 10px;
        border-radius: 50%;
    }}
    .dot-red {{ background: #f87171; }}
    .dot-yellow {{ background: #fbbf24; }}
    .dot-green {{ background: #34d399; }}
    .dashboard-frame-bar .title-text {{
        font-size: 12px;
        font-weight: 800;
        color: #e2e8f0;
        letter-spacing: 0.6px;
        text-transform: uppercase;
        font-family: 'JetBrains Mono', monospace;
    }}
    .dashboard-frame img {{
        width: 100%;
        height: auto;
        display: block;
    }}
    .dashboard-notation-bar {{
        background: rgba(15, 23, 42, 0.96);
        border-top: 1px solid rgba(56, 189, 248, 0.35);
        padding: 7px 16px;
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 13px;
        color: #cbd5e1;
        letter-spacing: 0.2px;
        line-height: 1.4;
    }}
    .dashboard-notation-bar strong {{
        color: #38bdf8;
        font-weight: 800;
    }}
    .dashboard-notation-bar em {{
        color: #ffffff;
        font-style: normal;
        font-weight: 700;
    }}

    /* COMPARISON TABLE ON SLIDES */
    .compare-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.12);
        margin-bottom: 10px;
        background: rgba(15, 23, 42, 0.7);
    }}
    .compare-table th {{
        background: #1e293b;
        color: #38bdf8;
        font-size: 13px;
        font-weight: 800;
        text-transform: uppercase;
        padding: 9px 12px;
        text-align: left;
        letter-spacing: 0.5px;
    }}
    .compare-table td {{
        padding: 8px 12px;
        font-size: 14px;
        color: #e2e8f0;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }}
    .compare-table tr:hover td {{
        background: rgba(56, 189, 248, 0.06);
    }}

    /* SLIDE FOOTER */
    .slide-footer {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 10;
        border-top: 1px solid rgba(255, 255, 255, 0.12);
        padding-top: 10px;
    }}
    .author-info {{
        display: flex;
        align-items: center;
        gap: 10px;
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
    .micro-cta {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.2) 0%, rgba(129, 140, 248, 0.25) 100%);
        border: 1px solid rgba(56, 189, 248, 0.6);
        color: #ffffff;
        padding: 7px 18px;
        border-radius: 100px;
        font-size: 13px;
        font-weight: 800;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 14px rgba(56, 189, 248, 0.2);
    }}
</style>
</head>
<body>

<!-- ======================================================== -->
<!-- SLIDE 01: THE PARADOX HOOK -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide1">
    <div class="glow-cyan"></div>
    <div class="glow-indigo"></div>

    <div class="slide-header">
        <div class="tag-badge">🔍 Portfolio Project 1 • F&amp;B Multi-Branch Analytics</div>
        <div class="slide-number">01 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Revenue Rp 4,89 Miliar,<br>
            Tapi Ada <span class="amber">Kebocoran Laba Rp 254 Juta</span><br>
            di Bawah Radar?
        </div>
        <div class="subtitle-text">
            Menganalisis 85.020 transaksi pesanan (81.560 Completed) di 18 cabang Jabodetabek (April–September 2026). Di permukaan, konsorsium tampak prima dengan Net Margin rata-rata 33,8%. Namun bedah data membuktikan 4 cabang mengalami pendarahan laba struktural!
        </div>

        <!-- 4 METRICS GRID -->
        <div class="grid-2">
            <div class="metric-card">
                <div class="card-label">Skala Jaringan</div>
                <div class="big-number cyan">18 Cabang</div>
                <div class="card-desc">Ekspansi multi-outlet di wilayah Jabodetabek</div>
            </div>
            <div class="metric-card">
                <div class="card-label">Total Transaksi</div>
                <div class="big-number green">85.020</div>
                <div class="card-desc">Volume order (81.560 Completed • 4,1% Void)</div>
            </div>
            <div class="metric-card">
                <div class="card-label">Gross Revenue</div>
                <div class="big-number cyan">Rp 4,89 M</div>
                <div class="card-desc">Total omzet bruto konsolidasi seluruh gerai</div>
            </div>
            <div class="metric-card highlight">
                <div class="card-label" style="color: #34d399;">Penyelamatan Laba</div>
                <div class="big-number green">~Rp 254 Jt</div>
                <div class="card-desc" style="color: #f8fafc; font-weight: 600;">Potensi dividen tahunan dari pemulihan 4 cabang kritis</div>
            </div>
        </div>

        <div class="metric-card warning" style="margin-bottom: 0;">
            <div style="font-size: 15px; font-weight: 700; color: #fbbf24; margin-bottom: 4px;">
                ⚠️ Jebakan Fatal Solusi Konvensional: "Tekan Biaya Semua Cabang Secara Merata!"
            </div>
            <div style="font-size: 14px; color: #e2e8f0; line-height: 1.45;">
                Jika disamaratakan, cabang yang efisien akan tertekan dan cabang bermasalah justru salah sasaran penanganan. Mengapa tiap cabang butuh presisi resep yang berbeda?
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Geser untuk Bedah Anomali Data 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 02: THE NETWORK OVERVIEW & MARGIN ILLUSION -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide2">
    <div class="glow-cyan"></div>

    <div class="slide-header">
        <div class="tag-badge">📊 Executive Snapshot • Power BI Overview</div>
        <div class="slide-number">02 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Ilusi Margin Rata-Rata:<br>
            Saat Angka Agregat <span class="cyan">Menutupi Bahaya Nyata</span>
        </div>
        <div class="subtitle-text">
            Head of Operations (Dimas) butuh kepastian setiap Senin pagi: Cabang mana yang wajib ditelepon karena profitnya tipis meski restorannya selalu ramai?
        </div>

        <div class="dashboard-frame">
            <div class="dashboard-frame-bar">
                <div class="dots">
                    <div class="dot dot-red"></div>
                    <div class="dot dot-yellow"></div>
                    <div class="dot dot-green"></div>
                </div>
                <div class="title-text">Microsoft Power BI Desktop • Executive Overview Page</div>
                <div style="font-size: 11px; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">18 Cabang Jabodetabek</div>
            </div>
            <img src="{overview_img_uri}" alt="Power BI Overview Dashboard">
            <div class="dashboard-notation-bar">
                <strong>📌 Catatan Eksekutif:</strong>
                <span>Satuan <em>Miliar (M)</em> &amp; <em>Juta (Jt)</em> Rupiah terstandarisasi. Total Omzet <em>Rp 4,89 Miliar</em>, Net Margin konsolidasi <em>33,8%</em>.</span>
            </div>
        </div>

        <div class="grid-2" style="margin-bottom: 0;">
            <div class="metric-card" style="margin: 0; padding: 12px 16px;">
                <div style="font-size: 13px; font-weight: 800; color: #34d399; margin-bottom: 2px;">🟢 13 CABANG SANGAT STABIL</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">Mengelompok rapat di kisaran margin <strong>34% – 37%</strong>. Sehat secara struktural dan tidak butuh intervensi khusus.</div>
            </div>
            <div class="metric-card danger" style="margin: 0; padding: 12px 16px;">
                <div style="font-size: 13px; font-weight: 800; color: #f87171; margin-bottom: 2px;">🔴 DISPARITAS EKSTREM 23,9% VS 40,8%</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">Cabang terlemah (Kelapa Gading 23,9%) tertinggal jauh di bawah benchmark (Cinere 40,8%). Selisih 16,9% mengindikasikan kebocoran serius!</div>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Mengapa Tiap Cabang Beda Penyakit? 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 03: THE FATAL TRAP: 4 CABANG, 3 AKAR MASALAH -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide3">
    <div class="glow-emerald"></div>

    <div class="slide-header">
        <div class="tag-badge">🔬 Root Cause Dissection • 4 Critical Branches</div>
        <div class="slide-number">03 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Jebakan Diagnosa Seragam:<br>
            <span class="red">4 Cabang Kritis</span>, <span class="cyan">3 Penyakit Berbeda</span>
        </div>
        <div class="subtitle-text">
            Menangani semua cabang dengan resep yang sama adalah kesalahan fatal. Bedah multi-tabel (Purchases, Inventory, Shifts, Opex) membuktikan sumber kebocoran yang berlainan:
        </div>

        <div class="grid-2">
            <!-- BR03 -->
            <div class="metric-card danger" style="padding: 14px 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 15px; font-weight: 900; color: #ffffff;">BR03 • Kelapa Gading</span>
                    <span style="background: rgba(239,68,68,0.25); color: #f87171; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px;">Margin 23,9%</span>
                </div>
                <div style="font-size: 13px; font-weight: 800; color: #f87171; margin-bottom: 4px;">100% MASALAH TENAGA KERJA (LABOR)</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">
                    Food cost &amp; waste dapur tergolong normal, tetapi <strong>rasio gaji menyedot 30,5% revenue</strong>. Terbukti overstaffed struktural dibanding cabang setara.
                </div>
            </div>

            <!-- BR05 -->
            <div class="metric-card danger" style="padding: 14px 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 15px; font-weight: 900; color: #ffffff;">BR05 • BSD</span>
                    <span style="background: rgba(239,68,68,0.25); color: #f87171; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px;">Margin 28,1%</span>
                </div>
                <div style="font-size: 13px; font-weight: 800; color: #fbbf24; margin-bottom: 4px;">MASALAH GANDA (SOURCING + WASTE)</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">
                    Dua kebocoran sekaligus: <strong>Harga beli bahan baku +24% di atas pasar</strong> dan <strong>tingkat bahan terbuang (waste) tertinggi di jaringan (5,6%)</strong>.
                </div>
            </div>

            <!-- BR11 -->
            <div class="metric-card warning" style="padding: 14px 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 15px; font-weight: 900; color: #ffffff;">BR11 • Tangerang</span>
                    <span style="background: rgba(245,158,11,0.25); color: #fbbf24; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px;">Margin 30,5%</span>
                </div>
                <div style="font-size: 13px; font-weight: 800; color: #fbbf24; margin-bottom: 4px;">MASALAH GANDA (SOURCING + WASTE)</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">
                    Pola serupa dengan BSD (harga supplier mahal dan kontrol porsi dapur longgar), namun tingkat keparahannya berada di level moderat.
                </div>
            </div>

            <!-- BR13 -->
            <div class="metric-card highlight" style="padding: 14px 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 15px; font-weight: 900; color: #ffffff;">BR13 • Sentul</span>
                    <span style="background: rgba(56,189,248,0.25); color: #38bdf8; font-size: 12px; font-weight: 800; padding: 2px 8px; border-radius: 6px;">Margin 32,3%</span>
                </div>
                <div style="font-size: 13px; font-weight: 800; color: #38bdf8; margin-bottom: 4px;">100% MASALAH HARGA SUPPLIER (SOURCING)</div>
                <div style="font-size: 13px; color: #cbd5e1; line-height: 1.4;">
                    Operasional dapur sangat disiplin (waste sangat rendah), staf efisien. Masalah <strong>murni pada kontrak harga pembelian bahan baku</strong>.
                </div>
            </div>
        </div>

        <div class="metric-card" style="margin-bottom: 0; background: rgba(30, 41, 59, 0.7); border-color: rgba(56, 189, 248, 0.4);">
            <div style="font-size: 14px; color: #f8fafc; line-height: 1.45;">
                💡 <strong>Prinsip Keputusan Bisnis:</strong> Jika Kelapa Gading diaudit dapurnya: <em>sia-sia</em>! Jika Sentul ditekan jadwal stafnya: <em>salah sasaran</em>! Intervensi manajemen wajib dipandu oleh temuan data riil.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Lihat Pembuktian Statistik Z-Score 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 04: STATISTICAL RIGOR: Z-SCORE VALIDATION -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide4">
    <div class="glow-indigo"></div>

    <div class="slide-header">
        <div class="tag-badge">📐 Statistical Rigor • Z-Score Validation</div>
        <div class="slide-number">04 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Bukan Sekadar Feeling:<br>
            Validasi Deviasi via <span class="cyan">Uji Statistik Z-Score</span>
        </div>
        <div class="subtitle-text">
            Untuk membuktikan deviasi bukan kebetulan acak, data diuji menggunakan Standard Score: <code style="color: #38bdf8; font-weight: 700; background: rgba(56,189,248,0.15); padding: 2px 6px; border-radius: 4px;">Z = (X - μ) / σ</code>. Nilai <code style="color: #f87171; font-weight: 700;">|Z| &gt; 2,0</code> membuktikan anomali signifikan secara statistik:
        </div>

        <div class="dashboard-frame">
            <div class="dashboard-frame-bar">
                <div class="dots">
                    <div class="dot dot-red"></div>
                    <div class="dot dot-yellow"></div>
                    <div class="dot dot-green"></div>
                </div>
                <div class="title-text">Microsoft Power BI Desktop • Statistical Root Cause Page</div>
                <div style="font-size: 11px; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">Scatter Plot &amp; Outlier Matrix</div>
            </div>
            <img src="{root_cause_img_uri}" alt="Power BI Root Cause Dashboard">
            <div class="dashboard-notation-bar">
                <strong>📌 Bukti Statistik:</strong>
                <span>Labor BR03 <em>Z = +8,3</em> (overstaffing nyata). Sourcing BR05 <em>Z = +27,7</em> &amp; Waste <em>Z = +24,6</em>. Cinere (BR09) efisien mutlak di <em>Z = -13,0</em> &amp; <em>-10,7</em>.</span>
            </div>
        </div>

        <div class="metric-card warning" style="margin-bottom: 0; padding: 12px 18px;">
            <div style="font-size: 14px; font-weight: 800; color: #fbbf24; margin-bottom: 3px;">
                ⚠️ Insight Analitis: Mengapa Label Otomatis Tidak Boleh Ditelan Mentah-Mentah?
            </div>
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                Kasus <strong>BR01</strong> (Z Sourcing = +2,4) sekilas berlabel bermasalah, tapi Net Margin-nya normal (34,5%). Sebaliknya, <strong>BR07 &amp; BR02</strong> berlabel "Benchmark" karena biaya rendah, tapi margin keseluruhannya biasa saja. <strong>Pelajaran:</strong> Ambang statistik wajib selalu diverifikasi silang terhadap dampaknya ke Bottom-Line Net Margin!
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Bagaimana Nasib Cabang Baru BR18? 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 05: THE NEW BRANCH PARADOX: BR18 -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide5">
    <div class="glow-cyan"></div>

    <div class="slide-header">
        <div class="tag-badge">⚡ Growth Dynamics • New Branch Evaluation</div>
        <div class="slide-number">05 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Paradoks Cabang Baru:<br>
            Jangan Hakimi <span class="amber">BR18</span> dengan <span class="cyan">Kacamata Cabang Lama!</span>
        </div>
        <div class="subtitle-text">
            Sistem otomatis menandai <strong>BR18 (Summarecon Bekasi)</strong> sebagai cabang bermasalah karena margin 24,9% dan Z-Score Labor +3,5. Apakah Head of Operations harus mengaudit cabang ini?
        </div>

        <div class="dashboard-frame">
            <div class="dashboard-frame-bar">
                <div class="dots">
                    <div class="dot dot-red"></div>
                    <div class="dot dot-yellow"></div>
                    <div class="dot dot-green"></div>
                </div>
                <div class="title-text">Microsoft Power BI Desktop • New Branch Ramp-Up Curve</div>
                <div style="font-size: 11px; color: #94a3b8; font-family: 'JetBrains Mono', monospace;">BR18 Operasional Bulan ke-4</div>
            </div>
            <img src="{cabang_baru_img_uri}" alt="Power BI Cabang Baru BR18 Dashboard">
            <div class="dashboard-notation-bar">
                <strong>📌 Fakta Pertumbuhan:</strong>
                <span>Baru buka Juni 2026. Tren margin naik konsisten tiap bulan: <em>19,9% (Jun) → 23,5% (Jul) → 27,4% (Agu) → 29,1% (Sep)</em>.</span>
            </div>
        </div>

        <div class="metric-card success" style="margin-bottom: 0; padding: 14px 18px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 15px; font-weight: 900; color: #34d399;">🛡️ PUTUSAN ANALIS DATA: DO NOT INTERVENE!</span>
                <span style="font-size: 11px; background: rgba(52,211,153,0.25); color: #34d399; padding: 2px 8px; border-radius: 4px; font-weight: 800;">Healthy Ramp-Up</span>
            </div>
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                Biaya tenaga kerja tinggi di awal adalah wajar karena adanya kuota staf minimum operasional <em>(fixed base staffing)</em> saat volume transaksi baru bertumbuh. Menekan staf sekarang justru akan merusak kualitas layanan pembukaan gerai baru. <strong>Cukup pantau lintasan pertumbuhannya!</strong>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Lihat Golden Benchmark BR09 Cinere 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 06: THE GOLDEN BENCHMARK: CINERE (BR09) -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide6">
    <div class="glow-emerald"></div>

    <div class="slide-header">
        <div class="tag-badge">🏆 Best Practice • Golden Benchmark Model</div>
        <div class="slide-number">06 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Benchmark Tak Tertandingi:<br>
            Rahasia Efisiensi <span class="green">RANTING - Cinere (BR09)</span>
        </div>
        <div class="subtitle-text">
            Net Margin <strong>40,8%</strong> konsisten rata-rata setiap bulan (rentang 38% – 43%). Cinere membuktikan bahwa margin tebal dicapai dengan keunggulan simultan di 3 pilar operasional F&amp;B:
        </div>

        <div class="grid-3">
            <div class="metric-card highlight" style="padding: 16px 14px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 4px;">🤝</div>
                <div style="font-size: 13px; font-weight: 800; color: #38bdf8; text-transform: uppercase; margin-bottom: 3px;">Sourcing Master</div>
                <div class="big-number cyan" style="font-size: 28px;">Z = -13,0</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.35;">
                    Harga beli bahan 8% di bawah rata-rata berkat kontrak volume pasokan rutin.
                </div>
            </div>

            <div class="metric-card success" style="padding: 16px 14px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 4px;">🍳</div>
                <div style="font-size: 13px; font-weight: 800; color: #34d399; text-transform: uppercase; margin-bottom: 3px;">Kitchen Precision</div>
                <div class="big-number green" style="font-size: 28px;">Z = -10,7</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.35;">
                    Rasio waste hanya 1,2% (terendah di 18 cabang) berkat kontrol porsi ketat &amp; rotasi FIFO.
                </div>
            </div>

            <div class="metric-card highlight" style="padding: 16px 14px; text-align: center;">
                <div style="font-size: 28px; margin-bottom: 4px;">⏱️</div>
                <div style="font-size: 13px; font-weight: 800; color: #a78bfa; text-transform: uppercase; margin-bottom: 3px;">Labor Efficiency</div>
                <div class="big-number cyan" style="font-size: 28px; color: #a78bfa;">Z = -3,5</div>
                <div style="font-size: 12px; color: #cbd5e1; line-height: 1.35;">
                    Rasio biaya gaji hanya 16,2% terhadap omzet melalui penjadwalan shift yang sangat presisi.
                </div>
            </div>
        </div>

        <div class="metric-card" style="margin-bottom: 0; background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 58, 138, 0.3) 100%); border-color: rgba(52, 211, 153, 0.4);">
            <div style="font-size: 14px; font-weight: 800; color: #34d399; margin-bottom: 3px;">
                📋 Rekomendasi Replikasi untuk Konsorsium:
            </div>
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                Jangan biarkan praktik terbaik Cinere terkunci di satu cabang! Jadikan checklist kontrol porsi dapur, roster shift staf, dan kontak vendor Cinere sebagai <strong>SOP Baku Jaringan</strong> untuk ditransfer langsung ke cabang BSD, Tangerang, dan Kelapa Gading.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Berapa Nilai Rupiah yang Diselamatkan? 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 07: FINANCIAL IMPACT: RECOVERY RP 254 JUTA -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide7">
    <div class="glow-indigo"></div>

    <div class="slide-header">
        <div class="tag-badge">💰 Value Creation • Financial Recovery Model</div>
        <div class="slide-number">07 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Dari Data ke Nilai Riil:<br>
            <span class="green">Rp 254 Juta / Tahun</span> Laba Diselamatkan
        </div>
        <div class="subtitle-text">
            Analisis data bernilai nol jika tidak menghasilkan dividen finansial. Dengan mereplikasi standar operasional Benchmark Emas Cinere (Target Margin ~40,8%), konsorsium menyelamatkan laba bersih nyata:
        </div>

        <table class="compare-table" style="margin-bottom: 8px;">
            <thead>
                <tr>
                    <th>Cabang Prioritas</th>
                    <th>Akar Masalah Kunci</th>
                    <th>Margin Awal</th>
                    <th>Target (Cinere Model)</th>
                    <th>Potensi Tambahan Laba</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>BR03 • Kelapa Gading</strong></td>
                    <td style="color: #f87171; font-weight: 700;">Overstaffing Shift Kerja</td>
                    <td>23,9%</td>
                    <td style="color: #34d399; font-weight: 700;">40,8%</td>
                    <td style="color: #34d399; font-weight: 800; font-family: 'JetBrains Mono';">+Rp 97 Juta / Thn</td>
                </tr>
                <tr>
                    <td><strong>BR05 • BSD</strong></td>
                    <td style="color: #fbbf24; font-weight: 700;">Sourcing Mahal &amp; Waste Dapur</td>
                    <td>28,1%</td>
                    <td style="color: #34d399; font-weight: 700;">40,8%</td>
                    <td style="color: #34d399; font-weight: 800; font-family: 'JetBrains Mono';">+Rp 68 Juta / Thn</td>
                </tr>
                <tr>
                    <td><strong>BR11 • Tangerang</strong></td>
                    <td style="color: #fbbf24; font-weight: 700;">Sourcing &amp; Porsi Dapur</td>
                    <td>30,5%</td>
                    <td style="color: #34d399; font-weight: 700;">40,8%</td>
                    <td style="color: #34d399; font-weight: 800; font-family: 'JetBrains Mono';">+Rp 53 Juta / Thn</td>
                </tr>
                <tr>
                    <td><strong>BR13 • Sentul</strong></td>
                    <td style="color: #38bdf8; font-weight: 700;">Kontrak Harga Supplier</td>
                    <td>32,3%</td>
                    <td style="color: #34d399; font-weight: 700;">40,8%</td>
                    <td style="color: #34d399; font-weight: 800; font-family: 'JetBrains Mono';">+Rp 38 Juta / Thn</td>
                </tr>
                <tr style="background: rgba(52, 211, 153, 0.15);">
                    <td colspan="4" style="font-weight: 900; color: #ffffff; text-transform: uppercase;">Total Pemulihan Laba Bersih Konsorsium:</td>
                    <td style="color: #34d399; font-weight: 900; font-size: 17px; font-family: 'JetBrains Mono';">~Rp 254 Juta / Thn</td>
                </tr>
            </tbody>
        </table>
        <div style="font-size: 12px; color: #94a3b8; margin-top: -2px; margin-bottom: 10px;">
            *Catatan Presisi: Dihitung dari selisih margin terhadap Benchmark Cinere (40,8%). Jika target dinaikkan ke baseline rata-rata (33,5%), dividen pemulihan adalah ~Rp 105–111 Juta / tahun.
        </div>

        <!-- EXECUTIVE FINANCIAL BREAKDOWN CARDS -->
        <div class="grid-3" style="margin-bottom: 12px;">
            <div class="metric-card" style="margin: 0; padding: 14px 16px; background: rgba(30, 41, 59, 0.6); text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase; font-weight: 800; margin-bottom: 2px;">Pemulihan 6 Bulan</div>
                <div class="big-number cyan" style="font-size: 26px; margin-bottom: 0;">Rp 139 Jt</div>
                <div style="font-size: 11px; color: #cbd5e1;">Arus kas periode berjalan</div>
            </div>
            <div class="metric-card" style="margin: 0; padding: 14px 16px; background: rgba(30, 41, 59, 0.6); text-align: center;">
                <div style="font-size: 11px; color: #94a3b8; text-transform: uppercase; font-weight: 800; margin-bottom: 2px;">Ekspansi Cabang Baru</div>
                <div class="big-number green" style="font-size: 26px; margin-bottom: 0;">0 Modal</div>
                <div style="font-size: 11px; color: #cbd5e1;">Murni optimasi margin internal</div>
            </div>
            <div class="metric-card highlight" style="margin: 0; padding: 14px 16px; text-align: center;">
                <div style="font-size: 11px; color: #34d399; text-transform: uppercase; font-weight: 800; margin-bottom: 2px;">ROI Data BI</div>
                <div class="big-number green" style="font-size: 26px; margin-bottom: 0;">&gt; 500%</div>
                <div style="font-size: 11px; color: #cbd5e1;">Kembali dalam &lt; 30 hari</div>
            </div>
        </div>

        <div class="metric-card success" style="margin-bottom: 0; padding: 14px 18px;">
            <div style="font-size: 13px; color: #e2e8f0; line-height: 1.45;">
                🎯 <strong>ROI Business Intelligence:</strong> Rp 254 Juta adalah laba bersih murni yang kembali ke pemilik modal setiap tahun tanpa perlu menambah cabang baru atau membakar biaya promosi. Inilah bukti bahwa Business Intelligence adalah <em>Profit Center</em>, bukan beban biaya.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Bagaimana Rencana Aksi 30 Harinya? 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 08: 30-DAY EXECUTION ROADMAP & GOVERNANCE -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide8">
    <div class="glow-cyan"></div>

    <div class="slide-header">
        <div class="tag-badge">📅 Actionable Roadmap • 30-Day Sprint</div>
        <div class="slide-number">08 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Roadmap 30 Hari:<br>
            <span class="cyan">Eksekusi Taktis</span> Tanpa Hambat Operasional
        </div>
        <div class="subtitle-text">
            Head of Operations (Dimas) dan Store Manager mengeksekusi rencana perbaikan terfokus dalam 4 tahapan sprint mingguan yang terukur dan akuntabel:
        </div>

        <!-- NATIVE CRISP SPRINT CARDS (4 WEEKS) -->
        <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 12px;">
            <div class="metric-card" style="margin: 0; padding: 12px 18px; display: flex; align-items: center; gap: 16px; border-left: 4px solid #f87171;">
                <div style="background: rgba(239,68,68,0.2); color: #f87171; font-family: 'JetBrains Mono'; font-weight: 800; font-size: 16px; padding: 6px 12px; border-radius: 8px; flex-shrink: 0;">MINGGU 1</div>
                <div style="flex: 1;">
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 2px;">Audit Staffing Kelapa Gading (BR03) &amp; Review Supplier BSD (BR05)</div>
                    <div style="font-size: 12px; color: #cbd5e1;">Re-rostering jadwal shift BR03 sesuai kurva transaksi jam sibuk; bekukan penambahan kru baru. Mulai evaluasi kontrak vendor bahan baku utama di BSD dan Tangerang.</div>
                </div>
            </div>

            <div class="metric-card" style="margin: 0; padding: 12px 18px; display: flex; align-items: center; gap: 16px; border-left: 4px solid #fbbf24;">
                <div style="background: rgba(245,158,11,0.2); color: #fbbf24; font-family: 'JetBrains Mono'; font-weight: 800; font-size: 16px; padding: 6px 12px; border-radius: 8px; flex-shrink: 0;">MINGGU 2</div>
                <div style="flex: 1;">
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 2px;">Audit Dapur BSD &amp; Tangerang + Negosiasi Kontrak Sentul (BR13)</div>
                    <div style="font-size: 12px; color: #cbd5e1;">Kunjungan lapangan verifikasi porsi resep dan penyimpanan bahan. Buka negosiasi ulang kontrak supplier Sentul untuk menurunkan selisih harga dari acuan pasar.</div>
                </div>
            </div>

            <div class="metric-card" style="margin: 0; padding: 12px 18px; display: flex; align-items: center; gap: 16px; border-left: 4px solid #38bdf8;">
                <div style="background: rgba(56,189,248,0.2); color: #38bdf8; font-family: 'JetBrains Mono'; font-weight: 800; font-size: 16px; padding: 6px 12px; border-radius: 8px; flex-shrink: 0;">MINGGU 3</div>
                <div style="flex: 1;">
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 2px;">Kodifikasi &amp; Dokumentasi SOP Praktik Terbaik Cinere (BR09)</div>
                    <div style="font-size: 12px; color: #cbd5e1;">Dokumentasikan checklist kontrol porsi dapur, jadwal shift staf, dan teknik negosiasi supplier Cinere menjadi modul SOP resmi jaringan.</div>
                </div>
            </div>

            <div class="metric-card success" style="margin: 0; padding: 12px 18px; display: flex; align-items: center; gap: 16px; border-left: 4px solid #34d399;">
                <div style="background: rgba(52,211,153,0.2); color: #34d399; font-family: 'JetBrains Mono'; font-weight: 800; font-size: 16px; padding: 6px 12px; border-radius: 8px; flex-shrink: 0;">MINGGU 4</div>
                <div style="flex: 1;">
                    <div style="font-size: 14px; font-weight: 800; color: #ffffff; margin-bottom: 2px;">Sosialisasi SOP, Baseline Monitoring, &amp; Evaluasi Ramp-Up BR18</div>
                    <div style="font-size: 12px; color: #cbd5e1;">Terapkan SOP di seluruh cabang bermasalah. Tetapkan baseline target margin baru di Power BI dan pantau pergerakan bulanan BR18 secara berkala.</div>
                </div>
            </div>
        </div>

        <div class="metric-card highlight" style="margin-bottom: 0; padding: 12px 18px;">
            <div style="font-size: 13px; color: #f8fafc; line-height: 1.45;">
                👥 <strong>Akuntabilitas Eksekutif:</strong> Rapat evaluasi efisiensi operasional rutin dipimpin oleh Head of Operations setiap hari Senin pukul 09.00 WIB menggunakan Dashboard Power BI Desktop sebagai acuan tunggal <em>(Single Source of Truth)</em>.
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Lihat Arsitektur Teknis Power BI 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 09: TECHNICAL FOUNDATION & DATA ENGINEERING -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide9">
    <div class="glow-indigo"></div>

    <div class="slide-header">
        <div class="tag-badge">⚙️ Data Architecture • Power BI &amp; Python Stack</div>
        <div class="slide-number">09 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Fondasi Teknis:<br>
            <span class="cyan">Star Schema, Data Pipeline</span> &amp; <span class="green">DAX Engine</span>
        </div>
        <div class="subtitle-text">
            Bagaimana data mentah 85.020 order dan 170.546 item transaksi ditransformasikan menjadi sistem pendukung keputusan eksekutif yang cepat, bersih, dan reproducible:
        </div>

        <div class="grid-3" style="margin-bottom: 12px;">
            <div class="metric-card" style="padding: 16px 16px; margin: 0;">
                <div style="font-size: 26px; margin-bottom: 4px;">🐍</div>
                <div class="card-label" style="color: #38bdf8;">1. Cleansing Pipeline</div>
                <div class="card-desc">
                    Penanganan 34.014 anonymous orders, imputasi cerdas utility opex via conditional branch-mean, audit integritas referensial.
                </div>
            </div>

            <div class="metric-card" style="padding: 16px 16px; margin: 0;">
                <div style="font-size: 26px; margin-bottom: 4px;">🗄️</div>
                <div class="card-label" style="color: #34d399;">2. Star Schema Model</div>
                <div class="card-desc">
                    Arsitektur relasi 1:N antara Dim_Branch, Dim_Calendar, Dim_Menu, Dim_Ingredient dengan Fact_Orders, Purchases, Inventory, &amp; Opex.
                </div>
            </div>

            <div class="metric-card" style="padding: 16px 16px; margin: 0;">
                <div style="font-size: 26px; margin-bottom: 4px;">📐</div>
                <div class="card-label" style="color: #a78bfa;">3. DAX Intelligence</div>
                <div class="card-desc">
                    Kalkulasi dinamis Weighted Food Cost %, Contribution Margin, Uji Signifikansi Z-Score, dan dynamic rolling ramp-up curve.
                </div>
            </div>
        </div>

        <!-- STAR SCHEMA ARCHITECTURE VISUALIZATION -->
        <div class="metric-card" style="margin-bottom: 10px; padding: 14px 18px; background: rgba(30, 41, 59, 0.5);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                <span style="font-size: 13px; font-weight: 800; color: #e2e8f0; text-transform: uppercase;">Star Schema Entity Relationship</span>
                <span style="font-size: 11px; background: rgba(56,189,248,0.2); color: #38bdf8; padding: 2px 8px; border-radius: 4px; font-weight: 700;">1:Many Relationships</span>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: #cbd5e1; line-height: 1.5;">
                [Dim_Branch, Dim_Calendar, Dim_Menu, Dim_Ingredients, Dim_Suppliers]<br>
                &nbsp;&nbsp;&nbsp;&nbsp;└── (1:N) ──► [Fact_Orders, Fact_Purchases, Fact_Inventory, Fact_Shifts, Fact_Opex]
            </div>
        </div>

        <div class="metric-card" style="margin-bottom: 0; padding: 12px 18px; background: rgba(15, 23, 42, 0.95); border-color: rgba(56, 189, 248, 0.4);">
            <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                <span class="tag-badge" style="font-size: 12px; padding: 3px 10px;">Python (Pandas, NumPy)</span>
                <span class="tag-badge" style="font-size: 12px; padding: 3px 10px;">Power BI Desktop (.pbix / .pbip)</span>
                <span class="tag-badge" style="font-size: 12px; padding: 3px 10px;">DAX Calculated Measures</span>
                <span class="tag-badge" style="font-size: 12px; padding: 3px 10px;">Z-Score Outlier Engine</span>
                <span class="tag-badge" style="font-size: 12px; padding: 3px 10px;">Executive C-Level Report</span>
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div class="micro-cta">
            Akses Repositori &amp; Terhubung Langsung 👉
        </div>
    </div>
</div>

<!-- ======================================================== -->
<!-- SLIDE 10: OPEN SOURCE CODEBASE & RECRUITMENT CTA -->
<!-- ======================================================== -->
<div class="slide-wrapper" id="slide10">
    <div class="glow-cyan"></div>
    <div class="glow-emerald"></div>

    <div class="slide-header">
        <div class="tag-badge" style="border-color: #34d399; color: #34d399;">🤝 Open-Source Codebase &amp; Contact</div>
        <div class="slide-number">10 / 10</div>
    </div>

    <div class="slide-body">
        <div class="hook-title">
            Let's Build Impactful<br>
            <span class="cyan">Data-Driven Solutions</span> Together!
        </div>
        <div class="subtitle-text">
            Seluruh pipeline analisis data, file dashboard Power BI (.pbix / .pbip), script Python ETL &amp; Z-score, serta laporan eksekutif tersedia secara terbuka di GitHub:
        </div>

        <!-- REPO CARD -->
        <div class="metric-card highlight" style="padding: 16px 20px; margin-bottom: 12px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                <span style="font-size: 14px; color: #cbd5e1; text-transform: uppercase; font-weight: 800;">🔗 GitHub Repository (Open-Source)</span>
                <span class="tag-badge" style="font-size: 11px; padding: 2px 8px;">Power BI, Python &amp; Data Marts</span>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #38bdf8; word-break: break-all; font-weight: 700;">
                {github_url}
            </div>
        </div>

        <!-- CONTACT CARDS -->
        <div class="grid-2" style="margin-bottom: 12px;">
            <div class="metric-card" style="margin: 0; padding: 14px 18px;">
                <div style="font-size: 12px; color: #cbd5e1; text-transform: uppercase; font-weight: 800; margin-bottom: 4px;">✉️ Direct Email</div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 15px; color: #ffffff; font-weight: 700;">{author_email}</div>
            </div>
            <div class="metric-card" style="margin: 0; padding: 14px 18px; border-color: rgba(52, 211, 153, 0.45);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
                    <span style="font-size: 12px; color: #cbd5e1; text-transform: uppercase; font-weight: 800;">💬 WhatsApp Active</span>
                    <span style="font-size: 10px; background: rgba(52,211,153,0.25); color: #34d399; padding: 2px 6px; border-radius: 4px; font-weight: 800;">Fast Response</span>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 16px; color: #34d399; font-weight: 800;">{author_wa_formatted}</div>
            </div>
        </div>

        <!-- ASSET PILLS -->
        <div class="grid-2" style="margin-bottom: 12px;">
            <div class="metric-card" style="margin: 0; padding: 10px 14px; background: rgba(30, 41, 59, 0.5);">
                <span style="font-size: 13px; font-weight: 600; color: #f8fafc;">📊 Microsoft Power BI Dashboard (.PBIX &amp; PBIP)</span>
            </div>
            <div class="metric-card" style="margin: 0; padding: 10px 14px; background: rgba(30, 41, 59, 0.5);">
                <span style="font-size: 13px; font-weight: 600; color: #f8fafc;">🐍 Python Notebook: Data Cleaning &amp; Z-Score Engine</span>
            </div>
            <div class="metric-card" style="margin: 0; padding: 10px 14px; background: rgba(30, 41, 59, 0.5);">
                <span style="font-size: 13px; font-weight: 600; color: #f8fafc;">📑 Laporan Eksekutif C-Level (PDF)</span>
            </div>
            <div class="metric-card" style="margin: 0; padding: 10px 14px; background: rgba(30, 41, 59, 0.5);">
                <span style="font-size: 13px; font-weight: 600; color: #f8fafc;">📐 Star Schema &amp; Data Cleaning Audit Log</span>
            </div>
        </div>

        <div class="metric-card success" style="margin-bottom: 0; padding: 12px 18px; text-align: center;">
            <div style="font-size: 14px; font-weight: 800; color: #34d399;">
                🚀 Open for Data Analyst &amp; Business Intelligence Roles (Full-Time / Contract)
            </div>
        </div>
    </div>

    <div class="slide-footer">
        <div class="author-info">
            <div class="author-avatar">
                <img src="{author_photo_uri}" alt="{author_name}">
            </div>
            <div>
                <div class="author-name">{author_name}</div>
                <div class="author-role">Data Analyst &amp; Business Intelligence</div>
            </div>
        </div>
        <div style="color: #38bdf8; font-weight: 800; font-size: 14px;">
            Let's Connect &amp; Collaborate on LinkedIn! 🤝
        </div>
    </div>
</div>

</body>
</html>
"""

# Write HTML
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Carousel HTML written to {html_file}")

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
subprocess.run(cmd_pdf, capture_output=True)
print(f"LinkedIn Carousel PDF generated: {pdf_file} (Size: {os.path.getsize(pdf_file)} bytes)")

# Copy PDF to root and BI directories
shutil.copyfile(pdf_file, pdf_root)
print(f"Copied PDF to root: {pdf_root}")

pdf_bi.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(pdf_file, pdf_bi)
print(f"Copied PDF to BI folder: {pdf_bi}")

# Clean existing PNG files in CAROUSEL_DIR
for old_png in CAROUSEL_DIR.glob("*.png"):
    try:
        old_png.unlink()
    except Exception:
        pass

# Generate individual PNG slides for each of the 10 slides
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
        print(f"Slide {i} PNG generated: {slide_png.name} (Exists: {slide_png.exists()})")

# Generate LinkedIn Post Caption / Copy (Option: Executive Trailer / Paradox Hook)
post_copy = f"""Banyak bisnis ritel dan F&B terjebak pada Ilusi Omzet: restoran selalu ramai dan omzet tembus miliaran, tapi laba bersih menguap tanpa jejak.

Di industri restoran multi-cabang, saat laba tertekan, reaksi spontan manajemen biasanya memukul rata: "Potong budget semua cabang secara merata!"

Tapi bagaimana jika data membuktikan bahwa 4 cabang yang berdarah ternyata mengidap 3 PENYAKIT OPERASIONAL YANG BERBEDA TOTAL?

Untuk menjawab tantangan Head of Operations RANTING (konsorsium 18 gerai di Jabodetabek dengan omzet Rp 4,89 Miliar dari 85.020 transaksi pesanan [81.560 completed]), saya membangun Business Intelligence Architecture & Uji Statistik Z-Score menggunakan Python & Microsoft Power BI.

Berikut 4 temuan data kunci dari investigasi ini:

⚡ 100% Masalah Tenaga Kerja di Kelapa Gading (BR03): Margin anjlok ke 23,9% (terendah di jaringan). Dapur dan harga beli bahan normal, tetapi rasio gaji menyedot 30,5% revenue (Z-Score Labor = +8,3). Terbukti overstaffing struktural.
🔥 Inefisiensi Ganda di BSD (BR05) & Tangerang (BR11): Margin BSD 28,1% tergerus dua kebocoran sekaligus: harga beli bahan baku 24% di atas pasar (Z = +27,7) dan tingkat bahan terbuang di dapur tertinggi di jaringan (5,6%, Z = +24,6).
🎯 Murni Masalah Supplier di Sentul (BR13): Margin 32,3% murni akibat markup harga vendor. Dapurnya sangat disiplin dengan waste rendah. Solusinya renegosiasi kontrak, bukan audit dapur.
🛡️ Paradoks Cabang Baru di Summarecon Bekasi (BR18): Margin rata-rata 25,0% dan labor tinggi sempat dicap 'bermasalah'. Faktanya, ini kurva pertumbuhan alami (19,9% ➔ 29,1% dalam 4 bulan). Putusan analis: DO NOT INTERVENE!

🏆 Dividen Nyata: Menyelamatkan ~Rp 254 Juta Laba Bersih per Tahun
Dengan mereplikasi standar operasional cabang benchmark (Cinere - BR09, margin 40,8% & Z-Score +4,3) dan mengeksekusi Roadmap Taktis 30 Hari, konsorsium memulihkan potensi laba bersih ~Rp 254.000.000 per tahun (baseline konservatif rata-rata jaringan Rp 105 Juta/tahun) tanpa perlu menambah cabang baru atau bakar uang promosi.

👉 Geser 10 slide dokumen di atas untuk melihat dashboard interaktif Power BI, scatter plot Z-Score, dan arsitektur Star Schema lengkapnya!

━━━━━━━━━━━━━━━━━━━━━━━━━━━
📂 Open-Source Codebase & Dashboard:
{github_url}

📬 Open for Discussion & Opportunities:
👤 {author_name} | Data Analyst & Business Intelligence
📧 {author_email}
💬 WhatsApp: {author_wa_formatted} (https://wa.me/62{author_wa[1:]})

Bagaimana pendekatan rekan-rekan dalam membedah anomali operasional agar tidak terjebak solusi "pukul rata"? Let's discuss in the comments! 👇

#BusinessIntelligence #DataAnalytics #PowerBI #FoodAndBeverage #RetailAnalytics #RootCauseAnalysis #DecisionIntelligence #DataPortfolio #HiringDataAnalyst #DataStorytelling
"""

with open(post_copy_file, "w", encoding="utf-8") as f:
    f.write(post_copy)
print(f"LinkedIn Post Copy written to {post_copy_file}")

print("All 10 LinkedIn Carousel slides, PDF, and Post Copy generated successfully!")
