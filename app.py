import streamlit as st
from ui import show_dashboard, show_login
from config import authenticate_user
from style import apply_custom_styles
from utils import clear_data
from router import route_app

# 🌈 Apply animated background and styles
st.set_page_config(page_title="Gratuity Tracker", layout="wide")
apply_custom_styles()

# 🔐 Session state init
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "data_uploaded" not in st.session_state:
    st.session_state["data_uploaded"] = False

# 🌟 Sidebar header
st.sidebar.markdown("## 🌟 Gratuity Tracker Pro")
st.sidebar.markdown("---")

# 🔐 Auth check
if not st.session_state["authenticated"]:
    show_login()
else:
    route_app()  # Switch between Dashboard and Analytics

    # 🧹 Optional: Cut all employee data
    st.sidebar.markdown("### 🗑️ Dangerous Action")
    if st.sidebar.button("❌ Cut (Clear All Data)", use_container_width=True):
        clear_data()
        st.success("✅ All employee data removed successfully!")

