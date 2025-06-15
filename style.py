import streamlit as st

def apply_custom_styles():
    st.markdown("""
<style>
body {
    background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
.stButton>button {
    background: linear-gradient(to right, #8e2de2, #4a00e0);
    color: white;
    border-radius: 10px;
    padding: 8px 18px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(to right, #4a00e0, #8e2de2);
    transform: scale(1.05);
}
.stTextInput>div>div>input {
    background-color: #ffffffaa;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)