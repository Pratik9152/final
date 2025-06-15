import streamlit as st
from ui import show_dashboard, show_login
from config import authenticate_user
from style import apply_custom_styles
from utils import clear_data
from router import route_app

# 🌐 Set page and apply full animated styles
st.set_page_config(page_title="Gratuity Tracker", layout="wide")
apply_custom_styles()

# 🔐 Initialize session states
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "data_uploaded" not in st.session_state:
    st.session_state["data_uploaded"] = False

# 🌟 Sidebar Header
st.sidebar.markdown("## 🌟 Gratuity Tracker Pro")
st.sidebar.markdown("---")

# 🔐 Login + Routing Logic
if not st.session_state["authenticated"]:
    show_login()
else:
    route_app()  # Renders Dashboard or Analytics based on user navigation

    # 🧹 Admin Cut Button: Clears All Data
    st.sidebar.markdown("### 🗑️ Dangerous Action")
    if st.sidebar.button("❌ Cut (Clear All Data)", use_container_width=True):
        clear_data()
        st.success("✅ All employee data has been cleared!")
