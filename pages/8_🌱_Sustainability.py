import streamlit as st
import datetime

st.title("🌱 Sustainability Impact – The Giving Movement")

# Simulated revenue → donations calculation
# (You can connect to real data later)
annual_revenue_estimate = 50000000  # USD
donation_rate = 0.10
min_donation = 1000000

donations = max(annual_revenue_estimate * donation_rate, min_donation)

# Eco savings (dummy multipliers, replace with real)
products_sold = 250000
water_saved_liters = products_sold * 1500
co2_saved_tons = products_sold * 2

st.subheader("2025 Impact Tracker")
st.metric("Estimated Annual Donations", f"${donations:,.0f}")
st.metric("Water Saved", f"{water_saved_liters:,.0f} L")
st.metric("CO₂ Saved", f"{co2_saved_tons:,.0f} tons")

# Progress Bar to $1M pledge
pledge_goal = 1000000
progress = min(donations / pledge_goal, 1.0)
st.progress(progress)

st.caption(f"As of {datetime.date.today()}, TGM has achieved {progress*100:.1f}% of its $1M pledge.")

st.subheader("What TGM is Already Doing")
st.write("""
- Uses eco-friendly fabrics (recycled polyester, organic cotton, bamboo)  
- Pledges 10% of profits (or $1M minimum) to charity  
- Local UAE manufacturing reduces shipping emissions  
""")

st.subheader("Our Creative Sustainability Suggestions")
st.write("""
- Impact Tracker Dashboard (real-time donations linked to sales)  
- Eco Badges (CO₂ and water savings per product)  
- Circular Fashion Program (discounts for returning old clothes)  
- Sustainable Influencer Partnerships (eco-conscious creators)  
- Community Challenges (#TGMImpact tree-planting campaigns)  
""")

st.success("By quantifying sustainability, TGM can strengthen trust and attract eco-conscious Gen Z and millennials.")
