import streamlit as st
from config import authenticate_user
from utils import process_file, save_processed_data
from analytics import show_analytics
from notifications import show_reminder_popup
from filters import apply_filters
from progress import render_progress_bar

def show_login():
    st.title("🔐 Admin Login")
    user = st.text_input("Username", key="username_input")
    pwd = st.text_input("Password", type="password", key="password_input")

    if st.button("Login"):
        if authenticate_user(user, pwd):
            st.session_state['authenticated'] = True
            st.success("✅ Login successful! Redirecting...")
            st.experimental_rerun()
        else:
            st.error("❌ Invalid credentials. Please try again.")

def show_dashboard():
    st.title("🏢 Gratuity Tracker Dashboard")

    show_reminder_popup()

    uploaded_file = st.sidebar.file_uploader("📤 Upload Employee CSV", type=["csv"])

    if uploaded_file:
        df, summary = process_file(uploaded_file)
        save_processed_data(df)
        st.session_state["data_uploaded"] = True
        st.success("✅ File uploaded and processed successfully.")
        st.write(summary)

        df = apply_filters(df)

        st.markdown("### 🎯 Eligibility Report")
        st.dataframe(df.style.applymap(lambda x: 'background-color: #d1ffd6' if x == "✅ Eligible (Exited)" else '', subset=["Gratuity Status"]))

        st.markdown("### ⏳ Years Progress")
        for i, row in df.iterrows():
            st.markdown(f"**{row['Name']} ({row['Emp Code']})** — `{row['Years Completed']} years`")
            render_progress_bar(row['Years Completed'])

        show_analytics(df)

    else:
        st.info("📁 Upload a CSV to get started. You can also use the sample template.")
