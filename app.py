import streamlit as st
from chatbot.chatbot import Chatbot
from chatbot.persona import personas

# Initialize session state for chat history and selected persona if not already initialized
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'persona' not in st.session_state:
    st.session_state.persona = "doctor"  # Default persona

# Select persona
persona_options = list(personas.keys())
selected_persona = st.selectbox("Choose a persona:", persona_options, index=persona_options.index(st.session_state.persona))

# Update persona in session state if changed
if st.session_state.persona != selected_persona:
    st.session_state.persona = selected_persona
    st.session_state.chat_history = []  # Reset chat history when persona changes

# Initialize the chatbot with the selected persona
chatbot = Chatbot(persona=personas[st.session_state.persona])

st.title("Multi-Persona Chatbot")
st.write(f"This chatbot has a persona of a {st.session_state.persona}. Ask your questions!")

# Input from the user
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Generate response
        response = chatbot.generate_response(user_input)
        
        # Update conversation history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"{st.session_state.persona.capitalize()} Bot: {response}")
        
        # Clear the input field after sending the message
        st.experimental_rerun()
    else:
        st.warning("Please enter a message.")

# Display the conversation history
st.text_area("Conversation", value="\n".join(st.session_state.chat_history), height=300, key="conversation_history")
