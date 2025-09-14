import streamlit as st

st.title("🎮 What-If Campaign Simulator")

st.markdown("Adjust the sliders to simulate campaign impact on TGM’s engagement.")

followers = st.slider("TikTok Follower Growth (%)", 0, 100, 20)
ugc = st.slider("UGC Campaign Boost (%)", 0, 100, 15)
influencers = st.slider("Influencer Collaboration Impact (%)", 0, 100, 25)

base_engagement = 0.01  # 0.01%

# Each slider value is a % increase, so divide by 100 once
simulated_engagement = base_engagement * (1 + followers/100) * (1 + ugc/100) * (1 + influencers/100)

st.metric("Simulated Engagement Rate", f"{simulated_engagement:.2f}%")

st.success("Use this simulator to see how different campaigns can improve engagement.")
