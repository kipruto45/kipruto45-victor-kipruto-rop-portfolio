import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
import os

# Page Config
st.set_page_config(page_title="Kenya Banking Sector: Integrated Analytics", layout="wide", page_icon="🏦")

# Sidebar Navigation
st.sidebar.title("Sector Navigator")
bank_selection = st.sidebar.selectbox("Select Institution", ["Kenya Banking Sector (Consolidated)", "KCB Group", "Absa Bank Kenya", "Equity Group"])

st.sidebar.markdown("---")
st.sidebar.button("Refresh Data", on_click=lambda: st.session_state.clear())

# Data Loader Helper
def get_engine(db_name, user, password, port=5432):
    host = "postgres" if os.path.exists("/.dockerenv") else "localhost"
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

if bank_selection == "Kenya Banking Sector (Consolidated)":
    st.title("🏦 Kenya Banking Sector: Consolidated Analytics")
    st.info("Displaying aggregated metrics for all 38+ licensed banks (CBK Supervision Reports).")
    # Link to the sector dashboard or include summary metrics
    st.markdown("[Open Detailed Sector Dashboard](http://localhost:8504)")

elif bank_selection == "KCB Group":

    st.title("🦁 KCB Group Integrated Analytics")
    st.info("Displaying KCB Group Consolidated Performance and M-Pesa Loan Analytics.")
    
elif bank_selection == "Absa Bank Kenya":
    st.title("🏦 Absa Kenya Financial Insights")
    st.info("Displaying Absa Kenya Financial KPIs and Open Banking Analytics.")

elif bank_selection == "Equity Group":
    st.title("🌍 Equity Group Pan-Africa Insights")
    st.info("Displaying Equity Group Digital Adoption and Regional Consolidation.")
