import streamlit as st
from PIL import Image

# --- App Config ---
st.set_page_config(
    page_title="The Giving Movement – Digital Footprint Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Load Logo ---
logo = Image.open("assets/TGM_logo.jpg")
st.sidebar.image(logo, use_column_width=True)

# --- Title ---
st.title("🌍 The Giving Movement – Digital Footprint Dashboard")
st.markdown("### Group 6 | Team Members: Sanchit Singh Thapa, Ritika Modi, Kashish Sethi, Aryan Bharali")

# --- Sidebar Info ---
st.sidebar.header("Navigation")
st.sidebar.markdown("Use the sidebar to explore different sections of the dashboard.")

st.write("Welcome to our interactive dashboard. This project analyzes The Giving Movement’s **digital footprint**, comparing engagement, search trends, traffic, and sustainability impact.")
st.write("Navigate through the pages to explore each aspect in detail.")
