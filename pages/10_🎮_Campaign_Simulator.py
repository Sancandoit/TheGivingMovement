import streamlit as st
import plotly.graph_objects as go

st.title("🎮 What-If Campaign Simulator")

st.markdown("Adjust the sliders to simulate campaign impact on TGM’s engagement.")

# Current average engagement baseline (set to 1% for realism)
base_engagement = 1.0  # %

# Sliders for campaign boosts
followers = st.slider("TikTok Follower Growth (%)", 0, 100, 20)
ugc = st.slider("UGC Campaign Boost (%)", 0, 100, 15)
influencers = st.slider("Influencer Collaboration Impact (%)", 0, 100, 25)

# Apply boosts
simulated_engagement = base_engagement * (1 + followers/100) * (1 + ugc/100) * (1 + influencers/100)

# Display metrics
st.metric("Simulated Engagement Rate", f"{simulated_engagement:.2f}%")

# --- Baseline vs Simulated Comparison Bar ---
fig = go.Figure()

fig.add_trace(go.Bar(
    x=["Current Engagement", "Simulated Engagement"],
    y=[base_engagement, simulated_engagement],
    marker_color=["#000000", "#7BC242"],  # Black = baseline, Green = simulated
    text=[f"{base_engagement:.2f}%", f"{simulated_engagement:.2f}%"],
    textposition="auto"
))

fig.update_layout(
    title="📊 Engagement Rate Comparison",
    yaxis=dict(title="Engagement (%)", range=[0, max(simulated_engagement * 1.2, 2)]),
    xaxis=dict(title=""),
    bargap=0.4
)

st.plotly_chart(fig, use_container_width=True)

st.success("This comparison shows how campaigns could realistically improve engagement.")
