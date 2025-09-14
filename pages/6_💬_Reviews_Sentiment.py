import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("💬 Reviews & Sentiment Analysis")

st.markdown("Customer feedback shows a mix of praise for **sustainability and comfort**, and frustration with **delivery and returns**.")

# Sample data – replace with scraped reviews
positive_comments = [
    "Love the quality and comfort",
    "Eco-friendly fabrics make me feel good",
    "Fast delivery and helpful customer service",
    "Stylish and sustainable"
]
negative_comments = [
    "Returns process is confusing",
    "Delivery delays frustrate me",
    "Sizing is inconsistent",
    "Customer service is slow"
]

text = " ".join(positive_comments + negative_comments)
wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="Dark2").generate(text)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.success("**Insight:** Strengths = quality, mission, comfort. Weaknesses = returns, delivery, sizing. Marketing should highlight strengths while operations fix the weak points.")
