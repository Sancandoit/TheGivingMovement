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

# --- Title ---
st.title("🌍 The Giving Movement – Digital Footprint Dashboard")
st.markdown("### Group 6 | Team Members: Sanchit Singh Thapa, Ritika Modi, Kashish Sethi, Aryan Bharali")

# --- Sidebar Info ---
st.sidebar.header("Navigation")
st.sidebar.markdown("Use the sidebar to explore different sections of the dashboard.")

st.write("Welcome to our interactive dashboard. This project analyzes The Giving Movement’s **digital footprint**, comparing engagement, search trends, traffic, and sustainability impact.")
st.write("Navigate through the pages to explore each aspect in detail.")
