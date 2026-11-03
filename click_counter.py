import streamlit as st

if "clicks" not in st.session_state:
    st.session_state.clicks = 0

if st.button("Click me"):
    st.session_state.clicks += 1

st.write(f"Clicks: {st.session_state.clicks}")
