import streamlit as st

st.set_page_config(page_title="DataCode", layout="wide")

# ---------------- HEADER ----------------

st.title("🚀 DataCode")
st.subheader("LeetCode for Data Science")

st.write("""
Practice data science like coding platforms.
No theory — only real-world learning.
""")

st.divider()

# ---------------- HERO SECTION ----------------

col1, col2 = st.columns(2)

with col1:
st.header("📊 Learn by Practice")
st.write("""
- Work on real datasets
- Improve Pandas & ML
- Build job-ready skills
""")
st.page_link("pages/1_Dashboard.py", label="Go to Dashboard →")

with col2:
st.header("👤 Track Progress")
st.write("""
- Monitor your growth
- Earn achievements
- Stay consistent
""")
st.page_link("pages/2_Profile.py", label="View Profile →")

st.divider()

# ---------------- FEATURES ----------------

st.header("🔥 Features")

c1, c2, c3 = st.columns(3)

with c1:
st.subheader("📂 Real Datasets")
st.write("Practice on real-world data")

with c2:
st.subheader("⚡ Instant Feedback")
st.write("Know your performance instantly")

with c3:
st.subheader("📈 Progress Tracking")
st.write("Track your learning journey")

st.divider()

st.success("🚀 Start your Data Science journey now!")
