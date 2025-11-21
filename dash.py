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

# --- 3. CSS STYLING (FIXED DYNAMIC WIDTH) ---
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

    /* --- PERBAIKAN CSS SIDEBAR (FULL WIDTH) --- */
    
    /* 1. Target Widget Radio Utama di Sidebar */
    [data-testid="stSidebar"] [data-testid="stRadio"] {
        width: 100% !important;
    }

    /* 2. Target Group Container */
    [data-testid="stSidebar"] [role="radiogroup"] {
        width: 100% !important;
        display: flex !important;
        flex-direction: column !important;
        gap: 10px !important; /* Jarak antar tombol */
    }

    /* 3. Sembunyikan bulatan radio button */
    [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
        display: none !important;
    }

    /* 4. Styling Kotak Tombol (Label) - INI KUNCINYA */
    [data-testid="stSidebar"] [role="radiogroup"] label {
        width: 100% !important;      /* Memaksa lebar 100% dari sidebar */
        display: flex !important;    /* Flexbox agar isi bisa diatur */
        justify-content: center !important; /* Teks di tengah horizontal */
        align-items: center !important;     /* Teks di tengah vertikal */
        
        padding: 15px 0px !important; /* Padding atas bawah */
        margin: 0px !important;
        
        background-color: var(--background-color); 
        color: var(--text-color);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 8px;
        transition: all 0.2s;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    /* 5. Memastikan teks di dalam label juga mengambil lebar penuh */
    [data-testid="stSidebar"] [role="radiogroup"] label > div {
        width: 100% !important;
        text-align: center !important;
        line-height: 1.2 !important;
    }

    /* 6. Hover effect */
    [data-testid="stSidebar"] [role="radiogroup"] label:hover {
        border-color: #b30000 !important;
        color: #b30000 !important;
        background-color: var(--secondary-background-color) !important;
        cursor: pointer;
    }

    /* 7. Active/Selected State */
    [data-testid="stSidebar"] [role="radiogroup"] label[aria-checked="true"] {
        background-color: #b30000 !important;
        border-color: #b30000 !important;
        color: white !important;
    }
    
    /* Warna teks saat aktif */
    [data-testid="stSidebar"] [role="radiogroup"] label[aria-checked="true"] p {
        color: white !important;
        font-weight: bold !important;
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
    
    # Menu Navigasi
    selected_page = st.radio(
        "Menu Navigasi", 
        ["Beranda", "Media Sosial"], 
        key="page",
        label_visibility="collapsed" 
    )
    
    # (Bagian Lokasi sudah dihapus)

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
