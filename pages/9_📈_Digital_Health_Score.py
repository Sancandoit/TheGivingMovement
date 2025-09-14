import streamlit as st
import plotly.graph_objects as go

st.title("📈 Digital Health Score – The Giving Movement")

categories = ["SEO", "Social Engagement", "Traffic", "Content Quality", "Sustainability"]

# Example scores (0–100 scale)
tgm_scores = [60, 20, 40, 55, 85]
squatwolf_scores = [70, 65, 75, 60, 50]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=tgm_scores,
      theta=categories,
      fill='toself',
      name='The Giving Movement'
))
fig.add_trace(go.Scatterpolar(
      r=squatwolf_scores,
      theta=categories,
      fill='toself',
      name='SQUATWOLF'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0, 100])
  ),
  showlegend=True
)

st.plotly_chart(fig, use_container_width=True)

st.success("TGM excels in sustainability but lags in engagement and traffic. This radar view highlights the gaps.")
