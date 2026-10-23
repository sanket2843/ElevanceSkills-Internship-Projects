
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Google Play Store Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("Google Play Store Data Analytics")
st.write(
    "Welcome to my ElevanceSkills Data Analytics Internship Project."
)

st.header("Project Overview")
st.write(
    "This project analyzes Google Play Store applications, "
    "ratings, reviews, installations, and estimated revenue "
    "using Python, Pandas, Plotly, and Power BI."
)

st.subheader("Internship Tasks")
st.markdown("""
- **Task 1:** Power BI Dashboard
- **Task 2:** Category and Installation Analysis
- **Task 3:** Date-Based Data Analysis
- **Task 4:** Application Data Visualization
- **Task 5:** Ratings and Reviews Comparison
- **Task 6:** Dual-Axis Chart for Installations and Estimated Revenue
""")

st.info(
    "This website presents an overview of the internship projects. "
    "The original Power BI dashboard and analysis notebooks are "
    "available in the linked project repository and Google Drive folder."
)

st.subheader("Project Links")

st.link_button(
    "View GitHub Repository",
    "https://github.com/sanket2843/ElevanceSkills-Internship-Projects"
)

st.link_button(
    "Open Google Drive Project Folder",
    "https://drive.google.com/drive/folders/1pG-rwroLcjIsaDA72qQVyTtF6fn3xgmw?usp=sharing"
)
