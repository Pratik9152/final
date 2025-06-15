
import streamlit as st
from ui import show_login, show_dashboard
from config import authenticate_user

st.set_page_config(page_title="Gratuity Tracker", layout="wide")

if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

if not st.session_state['authenticated']:
    show_login()
else:
    show_dashboard()
