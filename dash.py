import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Multimedia Dashboard - Natal Disdik DKI",
    page_icon="🎄",
    layout="wide"
)

# --- CSS STYLING ---
# UPDATE: Penambahan CSS untuk menghilangkan kursor kedap-kedip
st.markdown("""
<style>
    /* 1. Header Styling */
    .main-header {
        font-size: 2.5rem; 
        color: #b30000; 
        text-align: center; 
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem; 
        color: #4a4a4a; 
        text-align: center; 
        margin-bottom: 2rem;
    }

    /* 2. FIX: Hilangkan Kursor Kedap-Kedip (Caret) di area umum */
    [data-testid="stAppViewContainer"] {
        caret-color: transparent;
    }

    /* 3. Kembalikan Kursor saat user mengetik di Input/Textarea */
    input, textarea {
        caret-color: auto !important;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER FUNCTION ---
def header():
    st.markdown('<p class="main-header">🎄 Multimedia & Dokumentasi Division</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Komunitas Kristen & Katolik - Dinas Pendidikan DKI Jakarta</p>', unsafe_allow_html=True)
    st.markdown("---")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Logo_of_Ministry_of_Education_and_Culture_of_Republic_of_Indonesia.svg/1200px-Logo_of_Ministry_of_Education_and_Culture_of_Republic_of_Indonesia.svg.png", width=80)
    
    st.header("Menu")
    page = st.radio("Go to:", ["Overview", "Social Media Hub", "Submit Documentation"])
    
    st.markdown("---")

# --- PAGE 1: OVERVIEW ---
if page == "Overview":
    header()
    
    st.subheader("👋 Welcome, Team!")
    st.write("""
    This is the central hub for the **Multimedia & Documentation Division**. 
    Our goal is to capture and broadcast the Christmas Celebration beautifully.
    """)

    st.markdown("### 📌 Quick Actions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("**🌐 Social Media Hub**")
            st.caption("Access official Instagram, TikTok, and YouTube links.")
            st.write("Go here to follow new accounts.")

    with col2:
        with st.container(border=True):
            st.markdown("**📂 Submit Documentation**")
            st.caption("Upload photos/videos from meetings and rehearsals.")
            st.write("Go here to send files to the drive.")

# --- PAGE 2: SOCIAL MEDIA HUB ---
elif page == "Social Media Hub":
    st.title("🌐 Social Media Ecosystem")
    st.write("Connect with our official channels for the Dinas Pendidikan DKI Jakarta Christian & Catholic Community.")
    st.markdown("---")

    def social_card(platform_name, handle, desc, link, icon_url, color_stripe):
        with st.container(border=True):
            c1, c2 = st.columns([1, 4])
            with c1:
                st.image(icon_url, width=70)
            with c2:
                st.subheader(platform_name)
                st.markdown(f"**Handle:** `{handle}`")
                st.caption(desc)
                st.link_button(f"👉 Follow on {platform_name}", link, use_container_width=True)

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    # INSTAGRAM
    with row1_col1:
        social_card(
            "Instagram", 
            "@disdikdki_kriskath", 
            "Official updates, event posters, and daily stories.", 
            "https://instagram.com/", 
            "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/2048px-Instagram_logo_2016.svg.png",
            "#E1306C"
        )

    # TIKTOK
    with row1_col2:
        social_card(
            "TikTok", 
            "@disdikdki_natal", 
            "Fun moments, behind the scenes (BTS), and trends.", 
            "https://tiktok.com/", 
            "https://cdn.pixabay.com/photo/2021/06/15/12/28/tiktok-6338429_1280.png",
            "#000000"
        )

    # YOUTUBE
    with row2_col1:
        social_card(
            "YouTube", 
            "Komunitas Kristen Disdik DKI", 
            "Live streaming of the Christmas Service and High-res documentation.", 
            "https://youtube.com/", 
            "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/YouTube_Logo_2017.svg/512px-YouTube_Logo_2017.svg.png",
            "#FF0000"
        )

    # FACEBOOK
    with row2_col2:
        social_card(
            "Facebook", 
            "Persekutuan Doa Disdik DKI", 
            "Community announcements, photo albums, and family sharing.", 
            "https://facebook.com/", 
            "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Facebook_f_logo_%282019%29.svg/2048px-Facebook_f_logo_%282019%29.svg.png",
            "#1877F2"
        )

    st.markdown("---")
    st.success("💡 **Tip:** Click the buttons above to open the apps directly.")

# --- PAGE 3: SUBMIT DOCUMENTATION ---
elif page == "Submit Documentation":
    st.title("📂 Upload Documentation")
    st.write("For committee members: Please upload photos/videos taken during meetings, choir practice, or venue surveys.")

    with st.container(border=True):
        with st.form("upload_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Your Name")
            with col_b:
                category = st.selectbox("Activity Category", ["Committee Meeting", "Choir Rehearsal", "Venue Survey", "Pre-Event Setup", "Other"])
            
            uploaded_file = st.file_uploader("Choose a photo or video file", type=['jpg', 'png', 'mp4', 'mov'])
            
            notes = st.text_area("Additional Notes (Optional)")
            
            submitted = st.form_submit_button("🚀 Upload to Division Drive", use_container_width=True)

            if submitted:
                if uploaded_file is not None:
                    st.success(f"✅ Thank you {name}! The file for '{category}' has been received.")
                    st.balloons()
                else:
                    st.error("⚠️ Please select a file to upload.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: grey; font-size: 0.8em;'>Created by Multimedia Division - Komunitas Kristen & Katolik Disdik DKI Jakarta</div>", unsafe_allow_html=True)