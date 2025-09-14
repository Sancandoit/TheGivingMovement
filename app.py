import streamlit as st
from PIL import Image
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/styles.css")

# --- App Config ---
st.set_page_config(
    page_title="The Giving Movement – Digital Footprint Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Apply custom CSS styling
local_css("assets/styles.css")
# --- Load Logo ---
logo = Image.open("assets/TGM logo.jpg")
st.sidebar.image(logo, use_column_width=True)

# --- Homepage Content from README ---
with open("README.md") as f:
    st.markdown(f.read(), unsafe_allow_html=True)
