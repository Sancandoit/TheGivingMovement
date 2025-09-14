import streamlit as st
from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Google Search Trends – Live Data")

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["The Giving Movement", "SQUATWOLF"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='AE', gprop='')

df = pytrends.interest_over_time()

if not df.empty:
    st.line_chart(df[kw_list])
    st.success("Live data pulled from Google Trends (last 12 months, UAE).")
else:
    st.warning("Google Trends API limit reached. Showing no data.")
