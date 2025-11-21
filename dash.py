import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Komunitas Kristen & Katolik Disdik DKI",
    page_icon="🎄",
    layout="wide"
)

# --- 2. CSS STYLING (ANTI-CURSOR TEXT & FORCE LIGHT MODE) ---
st.markdown("""
<style>
    /* --- 1. FIX KURSOR KEDAP-KEDIP (SOLUSI UTAMA) --- */
    
    /* Terapkan ke seluruh aplikasi */
    [data-testid="stAppViewContainer"], body, html {
        caret-color: transparent !important; /* Hilangkan garis kedap-kedip */
        cursor: default !important; /* Kursor jadi panah, bukan bentuk 'I' text-select */
    }
    
    /* Kembalikan kursor jari (pointer) hanya untuk benda yang bisa diklik */
    a, button, [role="button"], .stTabs [data-baseweb="tab"] {
        cursor: pointer !important;
    }

    /* --- 2. FORCE LIGHT MODE --- */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff !important;
    }
    [data-testid="stHeader"] {
        background-color: rgba(255, 255, 255, 0.0) !important;
    }
    
    /* GLOBAL TEXT COLOR: Hitam */
    body, .stMarkdown, .stText, h1, h2, h3, h4, h5, h6, p, li, div {
        color: #333333 !important;
    }

    /* --- 3. HEADER & LAYOUT --- */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
    }
    .main-header {
        font-size: 2.3rem;
        color: #b30000 !important;
        text-align: center; 
        font-weight: 800;
        margin-top: 0px;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.3rem; /* Sedikit diperbesar agar nama Dinas terbaca jelas */
        color: #555555 !important;
        text-align: center; 
        margin-bottom: 2rem;
        opacity: 0.9;
        font-weight: 600; /* Sedikit lebih tebal */
    }

    /* --- 4. TABS STYLING (FIXED COLOR) --- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: transparent;
        padding: 10px 0;
        border-radius: 0px;
        display: flex;
        justify-content: center;
        border-bottom: 1px solid #eeeeee;
    }

    /* Tab Pasif */
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f4f4f4 !important;
        border-radius: 25px;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        padding: 0 25px;
    }
    .stTabs [data-baseweb="tab"] p, 
    .stTabs [data-baseweb="tab"] div {
        color: #555555 !important;
        font-weight: 600;
        font-size: 1rem;
    }

    /* Tab Hover */
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #fff0f0 !important;
        border-color: #ffcccc;
        transform: translateY(-2px);
    }
    .stTabs [data-baseweb="tab"]:hover p,
    .stTabs [data-baseweb="tab"]:hover div {
        color: #b30000 !important;
    }

    /* Tab Aktif */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #b30000 !important;
        box-shadow: 0 4px 10px rgba(179, 0, 0, 0.3);
        transform: scale(1.05);
        border: none;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p,
    .stTabs [data-baseweb="tab"][aria-selected="true"] div {
        color: #ffffff !important; /* Teks Putih */
        opacity: 1 !important;
    }
    
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent !important; 
    }

    /* --- 5. CONTENT & SOCIAL CARDS --- */
    .welcome-text {
        text-align: justify;
        font-size: 1.05rem;
        line-height: 1.6;
        color: #333333;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: white;
        border-radius: 10px;
    }

    .social-card {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 20px;
        display: flex;
        align-items: center;
        gap: 20px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        text-decoration: none;
        position: relative;
        overflow: hidden;
        cursor: pointer !important; /* Pastikan kartu bisa diklik */
    }
    .social-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        border-color: transparent;
    }
    .social-icon-img {
        width: 60px;
        height: 60px;
        object-fit: contain;
        transition: transform 0.3s ease;
    }
    .social-card:hover .social-icon-img {
        transform: scale(1.1);
    }
    .social-content h4 {
        margin: 0;
        font-size: 1.1rem;
        color: #222222 !important;
        font-weight: 700;
    }
    .social-content p {
        margin: 2px 0 8px 0;
        font-size: 0.85rem;
        color: #666666 !important;
    }
    .fake-btn {
        display: inline-block;
        padding: 6px 15px;
        background-color: #f4f4f4;
        border: 1px solid #ddd;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #555 !important;
        font-weight: 600;
        transition: background 0.3s;
        cursor: pointer !important;
    }
    .social-card:hover .fake-btn {
        background-color: #b30000;
        color: white !important;
        border-color: #b30000;
    }

    /* Footer styling */
    .footer-text {
        text-align: center; 
        color: #888888 !important; 
        font-size: 0.75em; 
        margin-top: 30px;
        border-top: 1px solid #eeeeee;
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER SECTION (DIPERBARUI) ---
# Judul dipecah agar terlihat proporsional (Nama Komunitas di atas, Nama Dinas di bawah)
st.markdown('<p class="main-header">Komunitas Kristen & Katolik</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)

# --- 4. TABS NAVIGATION ---
tab_beranda, tab_medsos = st.tabs(["🏠 Beranda", "🌐 Media Sosial"])

# --- TAB 1: BERANDA ---
with tab_beranda:
    with st.container(border=True):
        st.markdown("<h3 style='color: #333;'>Damai Sejahtera Bagi Kita Semua</h3>", unsafe_allow_html=True)
        st.markdown("---")
        
        st.markdown("""
        <div class="welcome-text">
            <p>
                Shalom dan Salam Sejahtera,
            </p>
            <p>
                Selamat datang di laman resmi <b>Komunitas Kristen & Katolik Dinas Pendidikan Provinsi DKI Jakarta</b>. 
                Puji syukur kita panjatkan ke hadirat Tuhan Yang Maha Esa, karena atas kasih dan anugerah-Nya, 
                kita dapat kembali menyongsong sukacita Natal tahun ini.
            </p>
            <p>
                Melalui perayaan Natal ini, marilah kita mempererat tali persaudaraan antar pegawai, guru, dan tenaga kependidikan 
                di lingkungan Dinas Pendidikan. Biarlah semangat Natal membawa damai di hati dan memotivasi kita untuk terus 
                memberikan pelayanan terbaik bagi pendidikan di Jakarta.
            </p>
            <p>
                Semoga sukacita Natal memberkati tugas dan pengabdian kita semua. Tuhan memberkati.
            </p>
            <br>
            <p style="text-align: right; font-weight: bold; font-style: italic; color: #555;">
                - Panitia Natal Disdik DKI Jakarta
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: MEDIA SOSIAL ---
with tab_medsos:
    st.markdown("<h3 style='color: #333;'>Tetap Terhubung Bersama Kami</h3>", unsafe_allow_html=True)
    st.caption("Ikuti update terbaru seputar kegiatan, ibadah, dan dokumentasi acara melalui kanal resmi kami.")

    def render_social_card_html(platform, handle, link, icon_url, color_theme):
        return f"""
        <a href="{link}" target="_blank" class="social-card" style="border-left: 5px solid {color_theme};">
            <div class="social-icon">
                <img src="{icon_url}" class="social-icon-img">
            </div>
            <div class="social-content">
                <h4>{platform}</h4>
                <p>{handle}</p>
                <span class="fake-btn">Kunjungi Profil &rarr;</span>
            </div>
        </a>
        """

    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(render_social_card_html(
            "Instagram", "@disdikdki_kriskath", 
            "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", 
            "#E1306C"
        ), unsafe_allow_html=True)
        
        st.markdown(render_social_card_html(
            "YouTube", "Komunitas Kristen Disdik", 
            "https://www.youtube.com/@kristen_katolik_disdik_dki", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", 
            "#FF0000"
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_social_card_html(
            "TikTok", "@disdik_kristen_katolik", 
            "https://www.tiktok.com/@disdik_kristen_katolik", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", 
            "#000000"
        ), unsafe_allow_html=True)
        
        st.markdown(render_social_card_html(
            "Facebook", "Persekutuan Doa Disdik", 
            "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", 
            "#1877F2"
        ), unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<p class="footer-text">Tim Multimedia - Komunitas Kristen & Katolik Disdik DKI Jakarta</p>', unsafe_allow_html=True)
