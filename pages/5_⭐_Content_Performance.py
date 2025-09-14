import streamlit as st
import plotly.express as px
import pandas as pd

st.title("⭐ Content Performance – Engagement Scatter")

data = {
    "Post": [
        "Be bold and comfy", "Homegrown collection", "Staying in = going out",
        "Every mile counts", "Don’t let fit get away", "Family days"
    ],
    "Likes": [456, 399, 287, 257, 264, 228],
    "Comments": [52, 12, 12, 8, 14, 16]
}
df = pd.DataFrame(data)

fig = px.scatter(df, x="Likes", y="Comments", text="Post",
                 size="Likes", color="Comments", hover_name="Post")

st.plotly_chart(fig, use_container_width=True)
st.success("Top-right = most engaging posts. Bottom-left = weakest performers.")
