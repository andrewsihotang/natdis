import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. SESSION STATE MANAGEMENT ---
if 'page' not in st.session_state:
    st.session_state.page = "Beranda"

def navigate_to(page_name):
    st.session_state.page = page_name

# --- 3. CSS STYLING (ADAPTIVE DARK/LIGHT MODE) ---
st.markdown("""
<style>
    /* HEADER STYLING */
    .main-header {
        font-size: 2.5rem; 
        color: #b30000; 
        text-align: center; 
        font-weight: bold;
        margin-top: -20px;
    }
    .sub-header {
        font-size: 1.2rem; 
        color: var(--text-color); 
        text-align: center; 
        margin-bottom: 2rem;
    }

    /* NAVIGATION TABS STYLING */
    [data-testid="stSidebar"] [role="radiogroup"] > label > div:first-child { display: none; }
    
    [data-testid="stSidebar"] [role="radiogroup"] > label {
        padding: 12px 20px;
        background-color: var(--background-color); 
        color: var(--text-color);
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        width: 100%; display: block; text-align: center; 
    }

    [data-testid="stSidebar"] [role="radiogroup"] > label:hover {
        border-color: #b30000;
        color: #b30000;
        cursor: pointer;
        background-color: var(--secondary-background-color);
    }

    [data-testid="stSidebar"] [role="radiogroup"] > label[aria-checked="true"] {
        background-color: #b30000 !important;
        border-color: #b30000;
        color: white !important;
    }
    
    [data-testid="stSidebar"] [role="radiogroup"] > label[aria-checked="true"] p {
        color: white !important;
        font-weight: bold;
    }
    
    /* LOCATION CARD HOVER EFFECT */
    .location-card:hover {
        transform: scale(1.02);
        transition: transform 0.2s;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. HEADER FUNCTION ---
def header():
    st.markdown('<p class="main-header">🎄 Natal Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Komunitas Kristen & Katolik - Dinas Pendidikan Provinsi DKI Jakarta</p>', unsafe_allow_html=True)
    st.markdown("---")

# --- 5. SIDEBAR NAVIGATION ---
with st.sidebar:
    # Logo
    st.image("https://github.com/andrewsihotang/natdis/raw/main/logo_komunitas.png", use_container_width=True)
    
    # Menu Navigasi (Hanya 2 Menu Sekarang)
    selected_page = st.radio(
        "Menu Navigasi", 
        ["Beranda", "Media Sosial"], # Dokumentasi dihapus
        key="page",
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    
    # --- NEW LOCATION CARD DESIGN ---
    st.markdown("### 📍 Lokasi Acara")
    
    # Link Google Maps ke Dinas Pendidikan DKI
    MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=Dinas+Pendidikan+Provinsi+DKI+Jakarta"
    
    st.markdown(f"""
    <div class="location-card" style="
        background-color: var(--secondary-background-color);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    ">
        <div style="font-size: 2.5rem; margin-bottom: 10px;">🏢</div>
        <p style="font-weight: bold; margin: 0; font-size: 1rem; color: var(--text-color);">Gedung Dinas Pendidikan</p>
        <p style="font-size: 0.85rem; margin: 5px 0 15px 0; color: var(--text-color); opacity: 0.8;">
            Provinsi DKI Jakarta
        </p>
        <a href="{MAPS_LINK}" target="_blank" style="
            text-decoration: none;
            background-color: #b30000;
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            font-size: 0.9rem;
            font-weight: bold;
            display: inline-block;
            transition: 0.3s;
            box-shadow: 0 2px 5px rgba(179, 0, 0, 0.3);
        ">
            🗺️ Buka Peta
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 1: BERANDA ---
if selected_page == "Beranda":
    header()
    
    st.subheader("👋 Selamat Datang!")
    st.info("""
    **Syalom!** Selamat datang di Portal Informasi Natal Dinas Pendidikan DKI Jakarta.
    
    Website ini didedikasikan untuk memberikan informasi terkini mengenai perayaan Natal kita, 
    mulai dari jadwal ibadah hingga tautan media sosial resmi komunitas.
    Mari kita rayakan sukacita Natal dengan semangat kebersamaan dan pelayanan.
    """)

    st.markdown("### 📌 Menu Cepat")
    
    # Layout disederhanakan karena hanya ada 1 menu cepat sekarang
    with st.container(border=True):
        c1, c2 = st.columns([1, 3])
        with c1:
            st.image("https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", width=100)
        with c2:
            st.markdown("### 🌐 Media Sosial")
            st.write("Ikuti akun resmi Instagram, TikTok, YouTube, dan Facebook kami untuk update terbaru.")
            st.button("👉 Buka Media Sosial", on_click=navigate_to, args=("Media Sosial",), use_container_width=True)

# --- PAGE 2: MEDIA SOSIAL ---
elif selected_page == "Media Sosial":
    st.title("🌐 Media Sosial")
    st.write("Terhubunglah dengan kanal resmi Komunitas Kristen & Katolik Disdik DKI Jakarta.")
    st.markdown("---")

    def social_card(platform_name, handle, desc, link, icon_url, color_stripe):
        with st.container(border=True):
            c1, c2 = st.columns([1, 4])
            with c1:
                st.image(icon_url, use_container_width=True)
            with c2:
                st.subheader(platform_name)
                st.markdown(f"**Akun:** `{handle}`")
                st.caption(desc)
                st.link_button(f"👉 Ikuti di {platform_name}", link, use_container_width=True)

    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        social_card("Instagram", "@disdikdki_kriskath", "Akun Instagram Resmi Komunitas.", "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", "#E1306C")
    with row1_col2:
        social_card("TikTok", "@disdik_kristen_katolik", "Akun Tiktok Resmi Komunitas.", "https://www.tiktok.com/@disdik_kristen_katolik", "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", "#000000")
        
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        social_card("YouTube", "Komunitas Kristen Disdik DKI", "Akun Youtube Resmi Komunitas.", "https://www.youtube.com/@kristen_katolik_disdik_dki", "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", "#FF0000")
    with row2_col2:
        social_card("Facebook", "Persekutuan Doa Disdik DKI", "Akun Facebook Resmi Komunitas.", "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", "#1877F2")
        
    st.markdown("---")
    st.success("💡 **Tips:** Klik tombol di atas untuk langsung membuka aplikasi.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: var(--text-color); opacity: 0.7; font-size: 0.8em;'>Dibuat oleh Tim Multimedia - Komunitas Kristen dan Katolik Dinas Pendidikan DKI Jakarta</div>", unsafe_allow_html=True)
