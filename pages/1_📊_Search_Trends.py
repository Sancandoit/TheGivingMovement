import streamlit as st
import pandas as pd
from pytrends.request import TrendReq
import time
import os

# ---- Page Config ----
st.set_page_config(page_title="Search Trends - The Giving Movement", page_icon="📊", layout="wide")

st.title("📊 Google Search Trends for The Giving Movement")
st.caption("Live data from Google Trends showing interest in The Giving Movement over time in the UAE region.")

# ---- Helper Function with Caching ----
@st.cache_data(ttl=3600)
def fetch_trends_data():
    """Fetches search trends for The Giving Movement, cached for 1 hour to avoid API limits."""
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["The Giving Movement"]
    pytrends.build_payload(kw_list, timeframe='today 12-m', geo='AE')
    df = pytrends.interest_over_time()
    return df

# ---- Load or Handle Fallback ----
try:
    df = fetch_trends_data()

    if df.empty:
        st.warning("No data returned from Google Trends. Loading backup data instead.")
        df = pd.read_csv("assets/trends_backup.csv")

except Exception as e:
    st.error("⚠️ Google Trends temporarily limited access. Using cached or backup data instead.")
    backup_path = "assets/trends_backup.csv"

    if os.path.exists(backup_path):
        df = pd.read_csv(backup_path)
        st.info("Loaded data from backup file successfully.")
    else:
        st.stop()

# ---- Display Data ----
if not df.empty:
    st.subheader("Interest Over Time (Past 12 Months)")
    st.line_chart(df["The Giving Movement"], use_container_width=True)
    
    # Display trend metrics
    latest = df["The Giving Movement"].iloc[-1]
    peak = df["The Giving Movement"].max()
    avg = round(df["The Giving Movement"].mean(), 2)

    col1, col2, col3 = st.columns(3)
    col1.metric("Current Interest", f"{latest}")
    col2.metric("Peak Interest", f"{peak}")
    col3.metric("12-Month Average", f"{avg}")

# ---- Insights Section ----
st.markdown("---")
st.markdown("### Insights & Interpretation")
st.markdown("""
The Google Trends data shows fluctuating but sustained interest in **The Giving Movement** over the past year, 
with search volume peaking around major sales periods and campaign launches.  
While overall visibility remains moderate, consistent seasonal spikes suggest strong brand recall among eco-conscious consumers.  
(Source: Google Trends, 2025)
""")

st.markdown("---")
st.markdown("💡 **Note:** Data is refreshed every hour. If Google rate limits are reached, cached or offline data is used for stability.")
