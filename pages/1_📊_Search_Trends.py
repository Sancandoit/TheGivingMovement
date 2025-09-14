import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Google Search Trends")

st.markdown("""
This section shows **Google Trends** comparison for The Giving Movement (TGM) 
and a competitor (SQUATWOLF) over the last 12 months in UAE.
""")

months = ["Sep '24","Oct '24","Nov '24","Dec '24",
          "Jan '25","Feb '25","Mar '25","Apr '25",
          "May '25","Jun '25","Jul '25","Aug '25"]

# Example data (replace with pytrends for live pulls)
tgm_interest = [80, 75, 70, 95, 85, 65, 60, 70, 68, 90, 72, 65]
squatwolf_interest = [55, 60, 58, 62, 64, 61, 66, 70, 68, 72, 71, 74]

df = pd.DataFrame({"Month": months, 
                   "The Giving Movement": tgm_interest, 
                   "SQUATWOLF": squatwolf_interest})

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df["Month"], df["The Giving Movement"], marker="o", label="The Giving Movement", color="#7BC242")
ax.plot(df["Month"], df["SQUATWOLF"], marker="o", label="SQUATWOLF", color="blue")
ax.set_title("Google Trends – UAE (12 Months)")
ax.set_ylabel("Search Interest (0–100)")
ax.legend()
st.pyplot(fig)
