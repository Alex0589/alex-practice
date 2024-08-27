import os
import streamlit as st  # Import the Streamlit library for creating the web app
from openai import OpenAI  # Import the OpenAI library to interact with the OpenAI API

# Initialize the OpenAI client with the API key from the environment variable
# This is necessary to authenticate and interact with the OpenAI API.
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define the model we'll be using.
# In this case, we're using 'gpt-4o-mini'.
model = "gpt-4o-mini"

# Set up the title of the Streamlit app.
# This is what the user will see at the top of the web page.
st.title("Chat with GPT-4o-mini")

# Initialize the chat history.
# 'st.session_state' is used to store variables that should persist across runs of the app.
# Here, we're using it to store the chat messages so they can be displayed even after the app refreshes.
if "messages" not in st.session_state:
    st.session_state.messages = []  # Initialize with an empty list if there are no messages yet

# Display the chat history.
# This loop goes through all the messages stored in 'st.session_state.messages'
# and displays them on the web page.
for message in st.session_state.messages:
    # 'st.chat_message' is used to display each message with a role ('user' or 'assistant')
    with st.chat_message(message["role"]):  
        st.markdown(message["content"])  # Display the content of the message

# Accept user input.
# 'st.chat_input' creates a text input box at the bottom of the page where the user can type their message.
# The user's input is stored in the variable 'prompt'.
if prompt := st.chat_input("Enter your message"):
    # If the user has entered a message, add it to the chat history.
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's message immediately in the chat window.
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Now we generate the assistant's response using the GPT-4o-mini model.
    try:
        # The OpenAI API call is made here.
        # 'client.chat.completions.create' sends the chat history to the model and gets a response.
        response = client.chat.completions.create(
            model=model,  # Specify the model to use
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages  # Send all previous messages in the conversation
            ],
            max_tokens=150  # Limit the response length to 150 tokens (words or parts of words)
        ).choices[0].message.content  # Extract the response content
        
        # Display the assistant's response in the chat window.
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Add the assistant's response to the chat history.
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    except Exception as e:
        # If something goes wrong (like a network issue), display an error message.
        st.error(f"Error generating response: {e}")
