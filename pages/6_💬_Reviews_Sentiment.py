import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.title("💬 Review Sentiment Analysis")

# Default reviews with positive and negative themes
reviews = st.text_area("Some of the sample reviews are as below:", 
"""
Love the quality and mission of the brand
Fabric feels comfortable and sustainable
Impressed by eco-friendly packaging
Delivery took too long
Sizing is inconsistent across products
Return process was difficult
Customer service was unresponsive
Trendy designs and modest fashion options
Great for everyday comfort and gym wear
Shipping delays affected my order experience
""")

# Generate WordCloud
if reviews.strip():
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(reviews)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    st.subheader("Insights")
    st.markdown("""
    **Positive Themes** ✅  
    - Quality fabrics and comfort  
    - Sustainability and eco-friendly practices  
    - Trendy designs and modest fashion options  

    **Negative Themes** ❌  
    - Delivery delays  
    - Inconsistent sizing  
    - Difficult returns and slow customer service  
    """)

    st.success("TGM should highlight positive themes in campaigns and address operational pain points to boost trust.")
