import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. SESSION STATE MANAGEMENT (Navigation Logic) ---
# Initialize 'page' in session_state if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = "Beranda"

def navigate_to(page_name):
    """Callback function to change the page"""
    st.session_state.page = page_name

# --- 3. CSS STYLING ---
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
        color: #4a4a4a; 
        text-align: center; 
        margin-bottom: 2rem;
    }

    /* CURSOR FIXES (No blinking caret in read-only areas) */
    [data-testid="stAppViewContainer"] {
        caret-color: transparent;
    }
    input, textarea {
        caret-color: auto !important;
    }

    /* NAVIGATION TABS STYLING (Rectangles instead of Radio Buttons) */
    /* 1. Hide the little circle (radio input) */
    [data-testid="stSidebar"] [role="radiogroup"] > label > div:first-child {
        display: none;
    }
    
    /* 2. Style the rectangle box */
    [data-testid="stSidebar"] [role="radiogroup"] > label {
        padding: 12px 20px;
        background-color: white;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* 3. Hover effect */
    [data-testid="stSidebar"] [role="radiogroup"] > label:hover {
        border-color: #b30000;
        background-color: #fff5f5;
        cursor: pointer;
        transform: translateX(5px);
    }

    /* 4. Active/Selected State */
    [data-testid="stSidebar"] [role="radiogroup"] > label[aria-checked="true"] {
        background-color: #b30000 !important;
        border-color: #b30000;
        color: white !important;
    }
    
    /* Ensure text inside active tab is white */
    [data-testid="stSidebar"] [role="radiogroup"] > label[aria-checked="true"] p {
        color: white !important;
        font-weight: bold;
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
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Logo_of_Ministry_of_Education_and_Culture_of_Republic_of_Indonesia.svg/1200px-Logo_of_Ministry_of_Education_and_Culture_of_Indonesia.svg.png", width=80)
    
    st.header("Menu Navigasi")
    
    # Using session_state for the value allows us to change it programmatically from the main page
    selected_page = st.radio(
        "Pilih Halaman:", 
        ["Beranda", "Media Sosial", "Upload Dokumentasi"],
        key="page" # Binds this widget to st.session_state.page
    )
    
    st.markdown("---")
    st.markdown("📍 **Lokasi:**\nGedung Dinas Pendidikan\nDKI Jakarta")

# --- PAGE 1: BERANDA (OVERVIEW) ---
if selected_page == "Beranda":
    header()
    
    st.subheader("👋 Selamat Datang!")
    st.info("""
    **Syalom!** Selamat datang di Portal Informasi Natal Dinas Pendidikan DKI Jakarta.
    
    Website ini didedikasikan untuk memberikan informasi terkini mengenai perayaan Natal kita, 
    mulai dari jadwal ibadah, dokumentasi kegiatan, hingga tautan media sosial resmi komunitas.
    Mari kita rayakan sukacita Natal dengan semangat kebersamaan dan pelayanan.
    """)

    st.markdown("### 📌 Menu Cepat")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### 🌐 Media Sosial")
            st.write("Ikuti akun resmi Instagram, TikTok, YouTube, dan Facebook kami untuk update terbaru.")
            # Clicking this button updates the session state and reruns the app
            st.button("👉 Buka Media Sosial", on_click=navigate_to, args=("Media Sosial",), use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 📸 Upload Dokumentasi")
            st.write("Punya foto/video kegiatan latihan atau rapat? Kirimkan file Anda ke panitia di sini.")
            st.button("👉 Upload File", on_click=navigate_to, args=("Upload Dokumentasi",), use_container_width=True)

# --- PAGE 2: MEDIA SOSIAL ---
elif selected_page == "Media Sosial":
    st.title("🌐 Media Sosial")
    st.write("Terhubunglah dengan kanal resmi Komunitas Kristen & Katolik Disdik DKI Jakarta.")
    st.markdown("---")

    # Function to render cards (Updated with Raw Links)
    def social_card(platform_name, handle, desc, link, icon_url, color_stripe):
        with st.container(border=True):
            c1, c2 = st.columns([1, 4])
            with c1:
                # st.image handles URL images
                st.image(icon_url, use_container_width=True)
            with c2:
                st.subheader(platform_name)
                st.markdown(f"**Akun:** `{handle}`")
                st.caption(desc)
                st.link_button(f"👉 Ikuti di {platform_name}", link, use_container_width=True)

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    # NOTE: Replaced 'blob' with 'raw' in GitHub URLs so images render correctly
    
    # INSTAGRAM
    with row1_col1:
        social_card(
            "Instagram", 
            "@disdikdki_kriskath", 
            "Info terbaru, poster acara, dan update harian via story.", 
            "https://instagram.com/", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png",
            "#E1306C"
        )

    # TIKTOK
    with row1_col2:
        social_card(
            "TikTok", 
            "@disdikdki_natal", 
            "Keseruan di balik layar (BTS) dan konten kreatif panitia.", 
            "https://tiktok.com/", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png",
            "#000000"
        )

    # YOUTUBE
    with row2_col1:
        social_card(
            "YouTube", 
            "Komunitas Kristen Disdik DKI", 
            "Live streaming Ibadah Natal dan dokumentasi video high-res.", 
            "https://youtube.com/", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png",
            "#FF0000"
        )

    # FACEBOOK
    with row2_col2:
        social_card(
            "Facebook", 
            "Persekutuan Doa Disdik DKI", 
            "Pengumuman komunitas, album foto, dan sharing keluarga.", 
            "https://facebook.com/", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png",
            "#1877F2"
        )

    st.markdown("---")
    st.success("💡 **Tips:** Klik tombol di atas untuk langsung membuka aplikasi.")

# --- PAGE 3: UPLOAD DOKUMENTASI ---
elif selected_page == "Upload Dokumentasi":
    st.title("📂 Upload Dokumentasi")
    st.write("Halaman ini untuk Panitia atau Anggota mengumpulkan dokumentasi kegiatan.")

    with st.container(border=True):
        st.info("Silakan upload foto/video rapat, latihan paduan suara, atau survei lokasi.")
        
        with st.form("upload_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Nama Pengirim")
            with col_b:
                category = st.selectbox("Kategori Kegiatan", ["Rapat Panitia", "Latihan Paduan Suara", "Survei Lokasi", "Persiapan Acara", "Lainnya"])
            
            uploaded_file = st.file_uploader("Pilih file foto atau video", type=['jpg', 'png', 'mp4', 'mov'])
            
            notes = st.text_area("Catatan Tambahan (Opsional)")
            
            submitted = st.form_submit_button("🚀 Kirim ke Panitia", use_container_width=True)

            if submitted:
                if uploaded_file is not None:
                    st.success(f"✅ Terima kasih {name}! File untuk kategori '{category}' berhasil diterima.")
                    st.balloons()
                else:
                    st.error("⚠️ Mohon pilih file terlebih dahulu sebelum mengirim.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey; font-size: 0.8em;'>Dibuat oleh Tim Multimedia - Natal Dinas Pendidikan DKI Jakarta</div>", unsafe_allow_html=True)
