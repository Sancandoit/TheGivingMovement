import streamlit as st
from PIL import Image

# --- Custom CSS Loader ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- App Config ---
st.set_page_config(
    page_title="The Giving Movement – Digital Footprint Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Apply Custom Styling ---
local_css("assets/styles.css")

# --- Load Logo ---
logo = Image.open("assets/TGM_logo.jpg")
st.sidebar.image(logo, use_container_width=True)

# --- Homepage Content from README ---
try:
    with open("README.md", "r", encoding="utf-8") as f:
        st.markdown(f.read(), unsafe_allow_html=True)
except FileNotFoundError:
    st.error("README.md not found. Please ensure it exists in the project root.")
