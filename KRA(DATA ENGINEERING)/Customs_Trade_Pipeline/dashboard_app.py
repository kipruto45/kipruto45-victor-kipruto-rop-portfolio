import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="KRA: Customs & Trade Analytics", layout="wide", page_icon="🚢")

def load_data():
    csv_path = "KRA(DATA ENGINEERING)/Customs_Trade_Pipeline/ingestion/customs_declarations.csv"
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    return pd.DataFrame()

st.title("🚢 KRA: Customs & Trade Intelligence")
st.markdown("Monitoring import/export volumes, duty collection, and contraband risk scoring.")

df = load_data()

if not df.empty:
    latest_year = df['year'].max()
    latest_data = df[df['year'] == latest_year]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Declared Value (B KES)", f"{latest_data['declared_value_m_kes'].sum()/1000:,.1f}B")
    col2.metric("Total Duty Collected (M KES)", f"{latest_data['duty_collected_m_kes'].sum():,.0f}")
    col3.metric("High Risk Shipments", len(latest_data[latest_data['risk_score'] > 80]))

    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["Trade Volume", "Duty Analytics", "Risk Scoring"])
    
    with tab1:
        st.subheader("Commodity Value by Origin Country")
        fig_vol = px.sunburst(latest_data, path=['origin_country', 'commodity'], values='declared_value_m_kes')
        st.plotly_chart(fig_vol, use_container_width=True)
        
    with tab2:
        st.subheader("Duty Collection vs Declared Value")
        fig_duty = px.scatter(latest_data, x='declared_value_m_kes', y='duty_collected_m_kes', color='commodity', 
                              size='volume_tons', hover_name='origin_country')
        st.plotly_chart(fig_duty, use_container_width=True)

    with tab3:
        st.subheader("Customs Risk Heatmap")
        risk_matrix = latest_data.groupby(['origin_country', 'commodity'])['risk_score'].mean().unstack()
        fig_risk = px.imshow(risk_matrix, color_continuous_scale='Reds', title="Mean Risk Score by Corridor")
        st.plotly_chart(fig_risk, use_container_width=True)

else:
    st.info("Generating data...")
    from ingestion.generate_customs_data import generate_customs_data
    generate_customs_data()
    st.rerun()
