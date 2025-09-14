import streamlit as st

st.title("🎮 What-If Campaign Simulator")

st.markdown("Adjust the sliders to simulate campaign impact on TGM’s engagement.")

# Current average engagement (set to a realistic baseline, e.g., 1%)
base_engagement = 1.0  # %

followers = st.slider("TikTok Follower Growth (%)", 0, 100, 20)
ugc = st.slider("UGC Campaign Boost (%)", 0, 100, 15)
influencers = st.slider("Influencer Collaboration Impact (%)", 0, 100, 25)

# Apply boosts
simulated_engagement = base_engagement * (1 + followers/100) * (1 + ugc/100) * (1 + influencers/100)

# Show results
st.metric("Simulated Engagement Rate", f"{simulated_engagement:.2f}%")
