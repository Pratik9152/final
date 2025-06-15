
import streamlit as st
from ui import show_dashboard
from analytics import show_analytics
from config import authenticate_user

def route_app():
    page = st.sidebar.radio("📂 Navigate", ["Dashboard", "Analytics"])
    if page == "Dashboard":
        show_dashboard()
    elif page == "Analytics":
        show_analytics()
