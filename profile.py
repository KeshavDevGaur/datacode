import streamlit as st

st.set_page_config(page_title="Profile", layout="wide")

st.title("👤 Profile")

st.subheader("Keshav Dev Gaur")

st.divider()

st.write("📊 Skill Progress")

st.progress(0.5)

st.write("""

* Pandas: 50%
* Visualization: 30%
* Machine Learning: 20%
  """)

st.divider()

st.subheader("🏆 Achievements")

st.write("""

* ✅ Completed 3 problems
* 🔥 2-day streak
* 🎯 Beginner Badge
  """)

st.divider()

st.info("Frontend UI only (no backend connected)")
