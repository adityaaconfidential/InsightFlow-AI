import streamlit as st

st.set_page_config(page_title="InsightFlow AI", layout="centered")

st.title("InsightFlow AI")
st.write("Welcome to the InsightFlow AI frontend.")

if st.button("Check backend health"):
    st.write("Call the backend health endpoint from here.")
