import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Natal Dinas Pendidikan DKI Jakarta",
    page_icon="🎄",
    layout="wide"
)

# --- 2. SESSION STATE MANAGEMENT (Navigation Logic) ---
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

    /* CURSOR FIXES */
    [data-testid="stAppViewContainer"] {
        caret-color: transparent;
    }
    input, textarea {
        caret-color: auto !important;
    }

    /* NAVIGATION TABS STYLING (Fixed Width & Rectangles) */
    
    /* 1. Hide the radio circle */
    [data-testid="stSidebar"] [role="radiogroup"] > label > div:first-child {
        display: none;
    }
    
    /* 2. Style the rectangle box - UPDATED for Full Width */
    [data-testid="stSidebar"] [role="radiogroup"] > label {
        padding: 12px 20px;
        background-color: white;
        border-radius: 8px;
        margin-bottom: 8px;
        border: 1px solid #e0e0e0;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        
        /* KEY CHANGES FOR UNIFORM SIZE */
        width: 100%;        /* Forces the box to fill the sidebar width */
        display: block;     /* Ensures it behaves like a block element */
        text-align: center; /* Centers the text inside the box */
    }

    /* 3. Hover effect */
    [data-testid="stSidebar"] [role="radiogroup"] > label:hover {
        border-color: #b30000;
        background-color: #fff5f5;
        cursor: pointer;
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
    # Updated Logo (Using 'raw' link to ensure image loads correctly)
    st.image("https://github.com/andrewsihotang/natdis/raw/main/logo_komunitas.png", use_container_width=True)
    
    # REMOVED: st.header("Menu Navigasi")
    
    # REMOVED Label: "Pilih Halaman:" set to hidden
    selected_page = st.radio(
        "Menu Navigasi", 
        ["Beranda", "Media Sosial", "Upload Dokumentasi"],
        key="page",
        label_visibility="collapsed" # This hides the title completely
    )
    
    st.markdown("---")
    
    # Updated Location to be Clickable
    st.markdown("### 📍 Lokasi")
    st.markdown(
        """
        <a href="https://maps.app.goo.gl/KqjqTjCErrECWbKv9" target="_blank" style="text-decoration: none; color: #333;">
        <strong>Gedung Dinas Pendidikan<br>Provinsi DKI Jakarta</strong>
        </a>
        """, 
        unsafe_allow_html=True
    )

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
            st.write("Ikuti akun resmi Instagram, TikTok, YouTube, dan Facebook kami.")
            st.button("👉 Buka Media Sosial", on_click=navigate_to, args=("Media Sosial",), use_container_width=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 📸 Upload Dokumentasi")
            st.write("Kirimkan file foto/video kegiatan latihan atau rapat ke panitia.")
            st.button("👉 Upload File", on_click=navigate_to, args=("Upload Dokumentasi",), use_container_width=True)

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
    row2_col1, row2_col2 = st.columns(2)

    # INSTAGRAM
    with row1_col1:
        social_card(
            "Instagram", 
            "@disdikdki_kriskath", 
            "Akun Resmi Instagram Komunitas Kristen dan Katolik Dinas Pendidikan DKI Jakarta", 
            "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png",
            "#E1306C"
        )

    # TIKTOK
    with row1_col2:
        social_card(
            "TikTok", 
            "@disdik_kristen_katolik", 
            "Akun Resmi Tiktok Komunitas Kristen dan Katolik Dinas Pendidikan DKI Jakarta", 
            "https://www.tiktok.com/@disdik_kristen_katolik", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png",
            "#000000"
        )

    # YOUTUBE
    with row2_col1:
        social_card(
            "YouTube", 
            "Komunitas Kristen Disdik DKI", 
            "Akun Resmi Youtube Komunitas Kristen dan Katolik Dinas Pendidikan DKI Jakarta", 
            "https://www.youtube.com/@kristen_katolik_disdik_dki", 
            "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png",
            "#FF0000"
        )

    # FACEBOOK
    with row2_col2:
        social_card(
            "Facebook", 
            "Persekutuan Doa Disdik DKI", 
            "Akun Resmi Facebook Komunitas Kristen dan Katolik Dinas Pendidikan DKI Jakarta", 
            "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", 
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

