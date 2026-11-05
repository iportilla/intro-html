import streamlit as st

st.title("Tip Calculator V2")
st.write("Enter your bill and explore additional UI elements.")

name = st.text_input("Your name")
notes = st.text_area(
    "Text area: add notes or requests",
    placeholder="Write any notes about your order or preferences...",
)
bill = st.number_input("Bill amount ($)", min_value=0.0, value=25.0, step=1.0)
tip_percent = st.slider("Tip (%)", min_value=0, max_value=30, value=20)

# List box (single-select)
learning_topic = st.selectbox(
    "List box: select one topic",
    options=["Python", "HTML", "CSS", "Streamlit", "GitHub"],
)

# Multi-select list box
learning_topics = st.multiselect(
    "Multi-select list box: select all topics you are learning",
    options=["Python", "HTML", "CSS", "Streamlit", "GitHub"],
    default=["Python", "HTML"],
)

# Radio button
experience_level = st.radio(
    "Radio button: choose your experience level",
    options=["Beginner", "Intermediate", "Advanced"],
)

# Drop-down
favorite_language = st.selectbox(
    "Drop-down: choose your favorite programming language",
    options=["Python", "JavaScript", "Java", "C#", "Other"],
)

# Check boxes
uses_vscode = st.checkbox("Checkbox: I use VS Code", value=True)
uses_jupyter = st.checkbox("Checkbox: I use Jupyter")
uses_terminal = st.checkbox("Checkbox: I use Terminal")
uses_browser = st.checkbox("Checkbox: I use a Web Browser", value=True)

tip = bill * tip_percent / 100
total = bill + tip

st.subheader("Tip Summary")
st.write(f"Tip: ${tip:.2f}")
st.write(f"Total: ${total:.2f}")

if st.button("Say thanks"):
    if name:
        st.success(f"Thanks, {name}!")
    else:
        st.warning("Enter your name first.")

st.subheader("Your Selections")
st.write(f"Notes: {notes if notes else 'None'}")
st.write(f"Single topic selected: {learning_topic}")
st.write(f"Topics selected: {', '.join(learning_topics) if learning_topics else 'None'}")
st.write(f"Experience level: {experience_level}")
st.write(f"Favorite language: {favorite_language}")

selected_tools = []
if uses_vscode:
    selected_tools.append("VS Code")
if uses_jupyter:
    selected_tools.append("Jupyter")
if uses_terminal:
    selected_tools.append("Terminal")
if uses_browser:
    selected_tools.append("Web Browser")

st.write(f"Tools checked: {', '.join(selected_tools) if selected_tools else 'None'}")
