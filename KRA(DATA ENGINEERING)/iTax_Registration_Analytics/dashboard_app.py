import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="KRA: iTax Business Analytics", layout="wide", page_icon="🏢")

def load_data():
    csv_path = "KRA(DATA ENGINEERING)/iTax_Registration_Analytics/ingestion/itax_registrations.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['registration_date'] = pd.to_datetime(df['registration_date'])
        return df
    return pd.DataFrame()

st.title("🏢 KRA: iTax Business Registration Analytics")
st.markdown("Tracking new business formation rates and taxpayer density by county and sector.")

df = load_data()

if not df.empty:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Registered PINs", len(df))
    col2.metric("Active Taxpayers %", f"{(df['is_active'].mean() * 100):,.1f}%")
    col3.metric("Top County", df['county'].mode()[0])

    st.markdown("---")
    
    tab1, tab2 = st.tabs(["Registration Trends", "Geospatial Density"])
    
    with tab1:
        st.subheader("Monthly Registration Volume")
        df_monthly = df.set_index('registration_date').resample('M').size().reset_index()
        df_monthly.columns = ['Date', 'Count']
        fig_trend = px.area(df_monthly, x='Date', y='Count', title="Business Formation Rate")
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with tab2:
        st.subheader("Taxpayer Concentration by County")
        fig_county = px.treemap(df, path=['county', 'sector'], title="Business Density Map")
        st.plotly_chart(fig_county, use_container_width=True)

else:
    st.info("Generating data...")
    from ingestion.generate_itax_data import generate_itax_data
    generate_itax_data()
    st.rerun()
