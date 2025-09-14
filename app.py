import streamlit as st
import plotly.graph_objects as go

st.title("🎮 What-If Campaign Simulator")

st.markdown("Adjust the sliders to simulate campaign impact on TGM’s engagement and sustainability.")

# --- Baseline Engagement ---
base_engagement = 1.0  # %

# Sliders for campaign boosts
followers = st.slider("TikTok Follower Growth (%)", 0, 100, 20)
ugc = st.slider("UGC Campaign Boost (%)", 0, 100, 15)
influencers = st.slider("Influencer Collaboration Impact (%)", 0, 100, 25)

# Apply boosts
simulated_engagement = base_engagement * (1 + followers/100) * (1 + ugc/100) * (1 + influencers/100)

# --- Assume Engagement → Sales Impact ---
# For simplicity: every +1% engagement = +5% sales lift
base_revenue = 50_000_000  # USD
sales_multiplier = 5
sales_boost = ((simulated_engagement - base_engagement) * sales_multiplier / 100) * base_revenue
new_revenue = base_revenue + sales_boost

# Donations (10% of profit or $1M minimum)
donation_rate = 0.10
min_donation = 1_000_000
new_donations = max(new_revenue * donation_rate, min_donation)

# Display Engagement Results
st.metric("Simulated Engagement Rate", f"{simulated_engagement:.2f}%")

# --- Engagement Comparison Bar ---
fig = go.Figure()
fig.add_trace(go.Bar(
    x=["Current Engagement", "Simulated Engagement"],
    y=[base_engagement, simulated_engagement],
    marker_color=["#000000", "#7BC242"],
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

# --- Sustainability Impact ---
st.subheader("🌱 Sustainability Impact from Improved Engagement")
st.write(f"📈 With higher engagement, projected revenue rises to **${new_revenue:,.0f}**.")
st.write(f"💚 This translates to estimated donations of **${new_donations:,.0f}** under TGM’s 10% pledge.")

st.success("By linking engagement to sales and sustainability, TGM can show how marketing performance directly fuels social impact.")
