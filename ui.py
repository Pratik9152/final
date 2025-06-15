
import streamlit as st
import pandas as pd
from utils import process_file
from analytics import show_analytics
from notifications import show_reminder_popup

def show_login():
    st.title("🔐 Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        from config import authenticate_user
        if authenticate_user(user, pwd):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Invalid credentials.")

def show_dashboard():
    st.sidebar.title("📁 File Upload")
    st.sidebar.download_button("📥 Download Sample", "Emp Code,Name,Department,Joining Date,Exit Date\n", file_name="sample.csv")
    show_reminder_popup()
    uploaded_file = st.sidebar.file_uploader("Upload Employee CSV", type=["csv"])
    if uploaded_file:
        df, summary = process_file(uploaded_file)
        st.success("✅ File processed")
        st.write(summary)
        st.dataframe(df)
        show_analytics(df)
