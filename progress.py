
import streamlit as st

def render_progress_bar(years):
    percent = min(100, round(years / 5 * 100))
    st.progress(percent)
