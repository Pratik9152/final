
import streamlit as st

def apply_filters(df):
    departments = st.multiselect("Filter by Department", df["Department"].unique())
    if departments:
        df = df[df["Department"].isin(departments)]
    return df
