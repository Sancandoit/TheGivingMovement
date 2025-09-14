import streamlit as st
import pandas as pd

st.title("⚖️ Competitor Ethics Benchmark – TGM vs SQUATWOLF")

st.markdown("""
Beyond digital performance, it is essential to evaluate brands on **ethical and sustainability dimensions**.  
This benchmark compares **The Giving Movement (TGM)** with its competitor **SQUATWOLF** on key responsibility criteria.
""")

# Data for benchmark table
data = {
    "Criteria": [
        "Sustainability Practices",
        "Charity & Donations",
        "Transparency",
        "Diversity & Inclusivity",
        "Community Engagement"
    ],
    "The Giving Movement": [
        "Recycled fabrics, eco packaging, UAE-local production",
        "10% of profits or $1M annually donated to charity",
        "Communicates sustainability impact openly",
        "Inclusive designs, modest fashion options",
        "Strong sustainability-driven campaigns & storytelling"
    ],
    "SQUATWOLF": [
        "Performance fabrics, no strong sustainability narrative",
        "No structured donation commitment reported",
        "Focuses on performance branding, less on ethics",
        "Focus on fitness/lifestyle imagery",
        "Community via gyms & athletes, less cause-driven"
    ]
}

df = pd.DataFrame(data)

# Display as table
st.dataframe(df, use_container_width=True)

st.subheader("Insights")
st.write("""
- **TGM** stands out for its sustainability pledge and donations, making ethics a core brand differentiator.  
- **SQUATWOLF** has stronger global fitness positioning but lacks a clear social or environmental mission.  
- This contrast highlights how **purpose-driven marketing** gives TGM an edge in long-term trust and loyalty.
""")

st.success("Ethics benchmarking shows that TGM is not only competing on style and performance, but also leading on sustainability and responsibility.")
