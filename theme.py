
import streamlit as st

def toggle_theme():
    dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
    if dark_mode:
        st.markdown("""
        <style>
        body {
            background-color: #1e1e2f;
            color: #e0e0e0;
        }
        </style>
        """, unsafe_allow_html=True)
