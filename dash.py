import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# --- KONFIGURASI GOOGLE DRIVE ---
# ID Folder dari link yang Anda berikan sebelumnya
PARENT_FOLDER_ID = "1nxAejoI_zoYfLhav6xIevj_tzdKDxx4X"

def upload_to_drive(file_obj, file_name, mime_type):
    def upload_to_drive(file_obj, file_name, mime_type):
    """Fungsi untuk mengupload file ke Google Drive via Service Account"""
    try:
        # Cek apakah Secrets sudah ada
        if "gcp_service_account" not in st.secrets:
            st.error("Konfigurasi Secrets tidak ditemukan. Harap setting di Dashboard Streamlit.")
            return None, None

        # Autentikasi
        creds_dict = st.secrets["gcp_service_account"]
        creds = service_account.Credentials.from_service_account_info(
            creds_dict, 
            scopes=['https://www.googleapis.com/auth/drive']
        )
        
        # Gunakan cache_discovery=False untuk menghindari error di beberapa environment
        service = build('drive', 'v3', credentials=creds, cache_discovery=False)

        file_metadata = {
            'name': file_name,
            'parents': [PARENT_FOLDER_ID]
        }
        
        # --- PERUBAHAN PENTING DI SINI (resumable=False) ---
        # Kita matikan resumable upload agar file langsung masuk ke storage pemilik folder
        media = MediaIoBaseUpload(file_obj, mimetype=mime_type, resumable=False)
        
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, webViewLink',
            supportsAllDrives=True 
        ).execute()
        
        return file.get('id'), file.get('webViewLink')
        
    except Exception as e:
        st.error(f"Terjadi kesalahan koneksi ke Google Drive: {e}")
        return None, None

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

    /* CURSOR FIXES */
    [data-testid="stAppViewContainer"] { caret-color: transparent; }
    input, textarea { caret-color: auto !important; }

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
</style>
""", unsafe_allow_html=True)

# --- 4. HEADER FUNCTION ---
def header():
    st.markdown('<p class="main-header">🎄 Natal Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Komunitas Kristen & Katolik - Dinas Pendidikan Provinsi DKI Jakarta</p>', unsafe_allow_html=True)
    st.markdown("---")

# --- 5. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://github.com/andrewsihotang/natdis/raw/main/logo_komunitas.png", use_container_width=True)
    
    selected_page = st.radio(
        "Menu Navigasi", 
        ["Beranda", "Media Sosial", "Upload Dokumentasi"],
        key="page",
        label_visibility="collapsed" 
    )
    
    st.markdown("---")
    
    st.markdown("### 📍 Lokasi")
    st.markdown(
        """
        <a href="https://maps.app.goo.gl/KqjqTjCErrECWbKv9" target="_blank" style="text-decoration: none; color: var(--text-color);">
        <strong>Gedung Dinas Pendidikan<br>Provinsi DKI Jakarta</strong>
        </a>
        """, 
        unsafe_allow_html=True
    )

# --- PAGE 1: BERANDA ---
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
    with row1_col1:
        social_card("Instagram", "@disdikdki_kriskath", "Info terbaru via story.", "https://www.instagram.com/komunitaskristenkatolikdisdik?igsh=MWlid3c5NDlmdTI1eQ%3D%3D&utm_source=qr", "https://github.com/andrewsihotang/natdis/raw/main/logo_instagram.png", "#E1306C")
    with row1_col2:
        social_card("TikTok", "@disdik_kristen_katolik", "BTS dan konten kreatif.", "https://www.tiktok.com/@disdik_kristen_katolik", "https://github.com/andrewsihotang/natdis/raw/main/logo_tiktok.png", "#000000")
        
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        social_card("YouTube", "Komunitas Kristen Disdik DKI", "Live streaming Ibadah.", "https://www.youtube.com/@kristen_katolik_disdik_dki", "https://github.com/andrewsihotang/natdis/raw/main/logo_youtube.png", "#FF0000")
    with row2_col2:
        social_card("Facebook", "Persekutuan Doa Disdik DKI", "Album foto & sharing.", "https://www.facebook.com/share/1Cg6wWBVuM/?mibextid=wwXIfr", "https://github.com/andrewsihotang/natdis/raw/main/logo_facebook.png", "#1877F2")
        
    st.markdown("---")
    st.success("💡 **Tips:** Klik tombol di atas untuk langsung membuka aplikasi.")

# --- PAGE 3: UPLOAD DOKUMENTASI (INTEGRASI GOOGLE DRIVE) ---
elif selected_page == "Upload Dokumentasi":
    st.title("📂 Upload Dokumentasi")
    st.write("Halaman ini untuk Panitia atau Anggota mengumpulkan dokumentasi kegiatan.")

    with st.container(border=True):
        st.info("Silakan upload foto/video. File akan otomatis tersimpan di Google Drive Panitia.")
        
        with st.form("upload_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Nama Pengirim")
            with col_b:
                category = st.selectbox("Kategori Kegiatan", ["Rapat Panitia", "Latihan Paduan Suara", "Survei Lokasi", "Persiapan Acara", "Lainnya"])
            
            uploaded_file = st.file_uploader("Pilih file foto atau video", type=['jpg', 'png', 'mp4', 'mov'])
            
            notes = st.text_area("Catatan Tambahan (Opsional)")
            
            submitted = st.form_submit_button("🚀 Kirim ke Google Drive", use_container_width=True)

            if submitted:
                if uploaded_file is not None and name:
                    with st.spinner('Sedang mengirim file ke Drive... mohon tunggu...'):
                        # Format nama file agar rapi di Drive: [Kategori] - [Nama Pengirim] - [Nama File]
                        final_filename = f"[{category}] - {name} - {uploaded_file.name}"
                        
                        # Proses Upload
                        file_id, file_link = upload_to_drive(uploaded_file, final_filename, uploaded_file.type)
                        
                        if file_id:
                            st.success(f"✅ Berhasil! Terima kasih {name}, file sudah masuk ke sistem.")
                            st.balloons()
                            
                elif not name:
                    st.warning("⚠️ Mohon isi **Nama Pengirim** agar kami tahu siapa yang mengirim.")
                else:
                    st.error("⚠️ Mohon pilih file foto/video terlebih dahulu.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: var(--text-color); opacity: 0.7; font-size: 0.8em;'>Dibuat oleh Tim Multimedia - Natal Dinas Pendidikan DKI Jakarta</div>", unsafe_allow_html=True)

