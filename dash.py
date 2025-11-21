import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. CSS STYLING (COMPACT & NO SCROLL) ---
st.markdown("""
<style>
    /* 1. MENGHILANGKAN PADDING BAWAAN STREAMLIT AGAR FULL SCREEN */
    .block-container {
        padding-top: 1.5rem !important; /* Mengurangi jarak atas drastis */
        padding-bottom: 1rem !important;
    }
    
    /* 2. HEADER STYLING (LEBIH KECIL & RAPAT) */
    .main-header {
        font-size: 2rem; /* Ukuran font dikurangi sedikit */
        color: #b30000; 
        text-align: center; 
        font-weight: bold;
        margin-top: -10px;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1rem; 
        color: var(--text-color); 
        text-align: center; 
        margin-bottom: 1.5rem;
        opacity: 0.8;
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

    /* 4. LOCATION CARD (COMPACT) */
    .location-card {
        background-color: var(--secondary-background-color);
        border-radius: 12px;
        padding: 20px; /* Padding diperkecil */
        border: 1px solid rgba(128, 128, 128, 0.2);
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        max-width: 500px;
        margin: 10px auto; 
    }
    
    /* Footer styling */
    .footer-text {
        text-align: center; 
        color: var(--text-color); 
        opacity: 0.6; 
        font-size: 0.75em; 
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HEADER SECTION (LOGO KECIL & DI TENGAH) ---

# Kita gunakan 3 kolom untuk memaksa logo di tengah dengan ukuran pas
col_left, col_center, col_right = st.columns([4, 2, 4])

with col_center:
    # width=170 memastikan logo KECIL dan tidak melebar
    st.image("https://github.com/andrewsihotang/natdis/raw/main/logo_komunitas.png", width=170)

st.markdown('<p class="main-header">🎄 Natal Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Komunitas Kristen & Katolik - Dinas Pendidikan Provinsi DKI Jakarta</p>', unsafe_allow_html=True)

# --- 4. TABS NAVIGATION ---
tab_beranda, tab_medsos = st.tabs(["🏠 Beranda", "🌐 Media Sosial"])

# --- TAB 1: BERANDA (LOKASI) ---
with tab_beranda:
    MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=Dinas+Pendidikan+Provinsi+DKI+Jakarta"
    
    st.markdown(f"""
    <div class="location-card">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">🏢</div>
        <h4 style="margin: 0; color: var(--text-color);">Gedung Dinas Pendidikan</h4>
        <p style="font-size: 0.9rem; margin: 5px 0 15px 0; color: var(--text-color); opacity: 0.8;">
            Provinsi DKI Jakarta
        </p>
        <a href="{MAPS_LINK}" target="_blank" style="
            text-decoration: none;
            background-color: #b30000;
            color: white;
            padding: 10px 25px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: bold;
            display: inline-block;
            transition: 0.3s;
        ">
            🗺️ Buka Peta
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- TAB 2: MEDIA SOSIAL ---
with tab_medsos:
    def social_card(platform_name, handle, link, icon_url, color_stripe):
        with st.container(border=True):
            c1, c2 = st.columns([1, 3]) # Kolom icon lebih kecil
            with c1:
                st.image(icon_url, use_container_width=True)
            with c2:
                st.markdown(f"**{platform_name}**")
                st.caption(handle)
                st.link_button("Buka", link, use_container_width=True)

    # Grid Layout (2 Baris, 2 Kolom)
    col1, col2 = st.columns(2)
    
    with col1:
        social_card("Instagram", "@disdikdki_kriskath", "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", "#E1306C")
        social_card("YouTube", "Komunitas Kristen Disdik", "https://www.youtube.com/@kristen_katolik_disdik_dki", "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", "#FF0000")

    with col2:
        social_card("TikTok", "@disdik_kristen_katolik", "https://www.tiktok.com/@disdik_kristen_katolik", "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", "#000000")
        social_card("Facebook", "Persekutuan Doa Disdik", "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", "#1877F2")

# --- FOOTER (MINIMALIS) ---
st.markdown('<p class="footer-text">Tim Multimedia - Komunitas Kristen & Katolik Disdik DKI Jakarta</p>', unsafe_allow_html=True)
