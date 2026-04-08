import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Dashboard")

st.write("Browse problems (UI only)")

st.divider()

# Table Header

col1, col2, col3 = st.columns([4,2,2])
col1.write("### Problem")
col2.write("### Difficulty")
col3.write("### Status")

st.divider()

# Dummy Data (UI Only)

problems = [
("Data Cleaning Basics", "Easy", "Not Started"),
("Handling Missing Values", "Easy", "Solved"),
("Sales Analysis", "Medium", "Not Started"),
("Customer Segmentation", "Medium", "Locked"),
("Churn Prediction", "Hard", "Locked"),
]

for p in problems:
c1, c2, c3 = st.columns([4,2,2])
c1.write(p[0])
c2.write(p[1])
c3.write(p[2])

st.divider()

st.info("⚠️ Frontend only — no functionality added yet")
