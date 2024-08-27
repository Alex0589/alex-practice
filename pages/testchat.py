import streamlit as st
import openai

# Set the title of the application
st.title("GPT-4o-Mini Chatbot")

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the chat client
    client = openai.ChatCompletion()

    # Generate AI response
    response = client.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.messages
        ],
        max_tokens=150
    )
    
    generated_text = response['choices'][0]['message']['content']
    
    # Display AI response in chat message container
    with st.chat_message("assistant"):
        st.markdown(generated_text)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": generated_text})
