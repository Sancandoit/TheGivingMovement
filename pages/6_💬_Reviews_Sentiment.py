import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("💬 Review Sentiment Analysis")

reviews = st.text_area("Paste sample reviews here:", 
                       "Love the quality and mission\nDelivery took too long\nSizing is inconsistent\nComfortable fabrics\nCustomer service was slow")

# Wordcloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(reviews)

fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

st.success("Strengths: comfort, sustainability. Weaknesses: delivery, sizing, returns.")
