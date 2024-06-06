import streamlit as st
from chatbot.chatbot import Chatbot

# Initialize the chatbot
chatbot = Chatbot()

# Initialize session state for chat history if not already initialized
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

st.title("Chat with Doctor Bot")
st.write("This chatbot has a persona of a doctor. Ask your medical questions!")

# Input from the user
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        # Generate response
        response = chatbot.generate_response(user_input)
        
        # Update conversation history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Doctor Bot: {response}")
        
    else:
        st.warning("Please enter a message.")

# Display the conversation history
st.text_area("Conversation", value="\n".join(st.session_state.chat_history), height=300, key="conversation_history")
