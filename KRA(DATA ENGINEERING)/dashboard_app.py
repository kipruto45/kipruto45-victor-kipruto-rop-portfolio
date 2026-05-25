import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="KRA Data Engineering", layout="wide", page_icon="📊")

st.title("📊 KRA Data Engineering: Revenue & Trade Dashboard")
st.markdown("Centralized overview of tax revenue and customs trade performance.")

st.info("Select a specific sub-project from the sidebar to view detailed analytics.")

st.sidebar.title("Navigation")
projects = [d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.')]
selected_project = st.sidebar.selectbox("Select Project", projects)

st.write(f"### Currently viewing: {selected_project}")
st.write("To view the detailed dashboard for this project, run its specific `dashboard_app.py` if available.")
