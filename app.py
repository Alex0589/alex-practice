import streamlit as st

# Display "Hello, World!"
st.write("Hello, World!")

# Create a text input box
user_input = st.text_input("Type something:")

# Display the user's input
if user_input:
    st.write("You typed:", user_input)
