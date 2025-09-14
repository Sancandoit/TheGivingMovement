import streamlit as st
import json

st.title("📱 Social Media Tracker – Live Follower Counts")

try:
    with open("social_data.json", "r") as f:
        data = json.load(f)

    st.subheader("Instagram")
    st.metric("Followers", f"{data['instagram']['followers']:,}")
    st.metric("Posts", f"{data['instagram']['posts']:,}")
    st.caption(f"Last updated: {data['last_updated']}")

    st.subheader("TikTok")
    st.metric("Followers", f"{data['tiktok']['followers']:,}")
    st.metric("Likes", f"{data['tiktok']['likes']:,}")
    st.caption(f"Last updated: {data['last_updated']}")

    st.success("Follower counts auto-refresh via Social Blade scraper.")

except FileNotFoundError:
    st.error("⚠️ social_data.json not found. Run update_social_data.py first.")
