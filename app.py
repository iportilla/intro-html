import streamlit as st

st.title("Tip Calculator")
st.write("Enter your bill to see the tip and total.")

name = st.text_input("Your name")
bill = st.number_input("Bill amount ($)", min_value=0.0, value=25.0, step=1.0)
tip_percent = st.slider("Tip (%)", min_value=0, max_value=30, value=20)

tip = bill * tip_percent / 100
total = bill + tip

st.write(f"Tip: ${tip:.2f}")
st.write(f"Total: ${total:.2f}")

if st.button("Say thanks"):
    if name:
        st.success(f"Thanks, {name}!")
    else:
        st.warning("Enter your name first.")
