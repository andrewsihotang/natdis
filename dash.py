import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. CSS STYLING (ANIMASI HOVER & TAMPILAN KEREN) ---
st.markdown("""
<style>
    /* 1. PENGATURAN JARAK ATAS */
    .block-container {
        padding-top: 3.5rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* 2. HEADER STYLING */
    .main-header {
        font-size: 2.2rem;
        color: #b30000; 
        text-align: center; 
        font-weight: bold;
        margin-top: 0px;
        margin-bottom: 5px;
    }
    .sub-header {
        font-size: 1.1rem; 
        color: var(--text-color); 
        text-align: center; 
        margin-bottom: 2rem;
        opacity: 0.8;
        font-style: italic;
    }

    /* 3. TABS STYLING */
    button[data-baseweb="tab"] {
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.5rem 1rem;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #b30000 !important;
        border-bottom-color: #b30000 !important;
    }

    /* 4. WELCOME CARD STYLING */
    .welcome-text {
        text-align: justify;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    
    /* --- 5. CSS KHUSUS SOCIAL MEDIA CARD (NEW!) --- */
    .social-card {
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 20px;
        display: flex;
        align-items: center;
        gap: 20px;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1); /* Animasi halus */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        text-decoration: none; /* Hilangkan garis bawah link */
        color: inherit;
        position: relative;
        overflow: hidden;
    }

    /* EFEK SAAT MOUSE HOVER (DIARAHKAN) */
    .social-card:hover {
        transform: translateY(-7px); /* Kartu naik ke atas */
        box-shadow: 0 15px 25px rgba(0,0,0,0.15); /* Bayangan menebal */
        border-color: transparent; /* Border asli hilang diganti glow */
    }

    /* Icon Styling */
    .social-icon-img {
        width: 60px;
        height: 60px;
        object-fit: contain;
        transition: transform 0.3s ease;
    }
    .social-card:hover .social-icon-img {
        transform: scale(1.1); /* Icon membesar sedikit saat hover */
    }

    /* Text Styling inside Card */
    .social-content h4 {
        margin: 0;
        font-size: 1.1rem;
        color: #333;
        font-weight: 700;
    }
    .social-content p {
        margin: 2px 0 8px 0;
        font-size: 0.85rem;
        color: #666;
    }

    /* Tombol Palsu (Styling Only) */
    .fake-btn {
        display: inline-block;
        padding: 6px 15px;
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #555;
        font-weight: 600;
        transition: background 0.3s;
    }
    .social-card:hover .fake-btn {
        background-color: #b30000;
        color: white;
        border-color: #b30000;
    }

    /* Footer styling */
    .footer-text {
        text-align: center; 
        color: var(--text-color); 
        opacity: 0.6; 
        font-size: 0.75em; 
        margin-top: 30px;
        border-top: 1px solid rgba(128,128,128,0.2);
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
st.markdown('<p class="main-header">🎄 Natal Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">"Mempererat Persaudaraan, Mewujudkan Pelayanan Kasih"</p>', unsafe_allow_html=True)

# --- 4. TABS NAVIGATION ---
tab_beranda, tab_medsos = st.tabs(["🏠 Beranda", "🌐 Media Sosial"])

# --- TAB 1: BERANDA ---
with tab_beranda:
    with st.container(border=True):
        st.markdown("### ✨ Damai Sejahtera Bagi Kita Semua")
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
            <p style="text-align: right; font-weight: bold; font-style: italic;">
                - Panitia Natal Disdik DKI Jakarta
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- TAB 2: MEDIA SOSIAL (DENGAN ANIMASI HOVER) ---
with tab_medsos:
    st.markdown("### 📱 Tetap Terhubung Bersama Kami")
    st.caption("Ikuti update terbaru seputar kegiatan, ibadah, dan dokumentasi acara melalui kanal resmi kami.")

    # Fungsi Python untuk merender HTML Card
    def render_social_card_html(platform, handle, link, icon_url, color_theme):
        # Kita menyuntikkan CSS border-left warna-warni langsung di elemen
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
            "#E1306C"  # Warna Pink Instagram
        ), unsafe_allow_html=True)
        
        st.markdown(render_social_card_html(
            "YouTube", "Komunitas Kristen Disdik", 
            "https://www.youtube.com/@kristen_katolik_disdik_dki", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", 
            "#FF0000" # Warna Merah YouTube
        ), unsafe_allow_html=True)

    with col2:
        st.markdown(render_social_card_html(
            "TikTok", "@disdik_kristen_katolik", 
            "https://www.tiktok.com/@disdik_kristen_katolik", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", 
            "#000000" # Warna Hitam TikTok
        ), unsafe_allow_html=True)
        
        st.markdown(render_social_card_html(
            "Facebook", "Persekutuan Doa Disdik", 
            "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", 
            "#1877F2" # Warna Biru Facebook
        ), unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<p class="footer-text">Tim Multimedia - Komunitas Kristen & Katolik Disdik DKI Jakarta</p>', unsafe_allow_html=True)
