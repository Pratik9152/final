import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <style>
    /* 🔮 Gradient Animated Background */
    body {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Segoe UI', sans-serif;
        color: #222;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ✨ Button Styling */
    .stButton>button {
        background: linear-gradient(to right, #8e2de2, #4a00e0);
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        font-size: 16px;
        font-weight: 600;
        transition: 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #4a00e0, #8e2de2);
        transform: scale(1.05);
        box-shadow: 0 0 10px #aaa;
    }

    /* 🧠 Input Field Styling */
    .stTextInput>div>div>input {
        background-color: #ffffffcc;
        border-radius: 8px;
        padding: 8px;
        font-weight: 500;
    }

    /* 📦 Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.85);
        border-right: 2px solid #ccc;
    }

    /* 📊 DataFrame Headers */
    .css-1cpxqw2.edgvbvh3 {
        background-color: #e0f7fa;
        font-weight: bold;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)
