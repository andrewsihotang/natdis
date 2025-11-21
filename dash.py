import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. CSS STYLING (FIXED HEADER) ---
st.markdown("""
<style>
    /* 1. PENGATURAN JARAK ATAS (FIXED: DIPERBESAR AGAR TIDAK KETUTUPAN) */
    .block-container {
        padding-top: 3.5rem !important; /* Jarak diperbesar agar judul turun */
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

# --- TAB 1: BERANDA (KATA SAMBUTAN) ---
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

# --- TAB 2: MEDIA SOSIAL ---
with tab_medsos:
    st.markdown("### 📱 Tetap Terhubung Bersama Kami")
    st.caption("Ikuti update terbaru seputar kegiatan, ibadah, dan dokumentasi acara melalui kanal resmi kami.")
    
    def social_card(platform_name, handle, link, icon_url, color_stripe):
        with st.container(border=True):
            c1, c2 = st.columns([1, 4]) 
            with c1:
                st.image(icon_url, use_container_width=True)
            with c2:
                st.markdown(f"**{platform_name}**")
                st.caption(handle)
                st.link_button("Kunjungi Profil", link, use_container_width=True)

    # Grid Layout (2 Baris, 2 Kolom)
    col1, col2 = st.columns(2)
    
    with col1:
        social_card("Instagram", "@disdikdki_kriskath", "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", "#E1306C")
        social_card("YouTube", "Komunitas Kristen Disdik", "https://www.youtube.com/@kristen_katolik_disdik_dki", "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", "#FF0000")

    with col2:
        social_card("TikTok", "@disdik_kristen_katolik", "https://www.tiktok.com/@disdik_kristen_katolik", "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", "#000000")
        social_card("Facebook", "Persekutuan Doa Disdik", "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", "#1877F2")

# --- FOOTER ---
st.markdown('<p class="footer-text">Tim Multimedia - Komunitas Kristen & Katolik Disdik DKI Jakarta</p>', unsafe_allow_html=True)
