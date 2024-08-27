import os
import streamlit as st
from openai import OpenAI

# Initialize the OpenAI client with the API key from the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set a default model
model = "gpt-4o-mini"

st.title("Interactive RPG Storytelling with GPT-4o-mini")

# Sidebar for character information
with st.sidebar:
    st.header("Your Character")
    character_name = st.text_input("Character Name", "Hero")
    character_class = st.selectbox("Class", ["Warrior", "Mage", "Rogue", "Bard"])
    character_level = st.slider("Level", 1, 20, 1)

# Story container
st.write(f"**Welcome, {character_name} the {character_class}, Level {character_level}**")

# Initialize story history
if "story" not in st.session_state:
    st.session_state.story = [
        {"role": "system", "content": "You are a brave adventurer embarking on a new quest. Choose your path wisely."}
    ]

# Display story messages
for message in st.session_state.story:
    with st.container():
        st.markdown(f"**{message['role'].capitalize()}:** {message['content']}")

# Input columns for user actions
col1, col2 = st.columns(2)

with col1:
    user_action = st.text_input("What will you do?", "")

with col2:
    st.write("")

if st.button("Take Action"):
    if user_action:
        # Add user action to the story
        st.session_state.story.append({"role": "user", "content": user_action})
        
        # Display user's action
        with st.container():
            st.markdown(f"**You:** {user_action}")
        
        # Generate story continuation using GPT-4o-mini
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": f"You are a {character_class} named {character_name}."},
                    *st.session_state.story
                ],
                max_tokens=200
            ).choices[0].message.content
            
            # Display AI response in the story
            with st.container():
                st.markdown(f"**Narrator:** {response}")
            
            # Add response to the story history
            st.session_state.story.append({"role": "assistant", "content": response})
        
        except Exception as e:
            st.error(f"Error generating response: {e}")

# End the adventure or continue
if st.button("End Adventure"):
    st.write("**Your adventure has come to an end. Thank you for playing!**")
    st.session_state.story.clear()
