
import streamlit as st
import plotly.express as px

def show_analytics(df):
    st.subheader("📊 Analytics")
    bar = px.bar(df, x="Department", color="Eligible", barmode="group")
    st.plotly_chart(bar, use_container_width=True)
