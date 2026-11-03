import random
import streamlit as st

st.title("Guess the Number")
st.write("I'm thinking of a whole number from 1 to 9.")

# TODO 1: If "secret" isn't in st.session_state yet,
# store a random number and set "attempts" to 0.

guess = st.number_input("Your guess", min_value=1, max_value=9, step=1)

if st.button("Guess"):
    # TODO 2: Add 1 to the number of attempts.

    # TODO 3: Compare guess to the secret number.
    # Show "Too low", "Too high", or a success message.
    pass

# TODO 4: Display the number of attempts.

if st.button("New game"):
    # TODO 5: Pick a new secret number and reset attempts to 0.
    # Then call st.rerun() to refresh the page.
    pass
