
import streamlit as st

def show_reminder_popup():
    with st.sidebar.expander("🔔 Upcoming Features"):
        st.markdown("- 📧 Email Send Button\n- 📄 PDF Export\n- 📅 Monthly Report Scheduler")
