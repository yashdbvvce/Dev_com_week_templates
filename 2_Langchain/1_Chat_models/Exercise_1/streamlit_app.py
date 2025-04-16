import streamlit as st
import time
from your_code import *

# Initialize chat history (
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input -
if prompt := st.chat_input("What is up?"):
    # Append and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Generating Response"):
        # Generate response
        assistant_response = generate_response(prompt)

        # Display assistant response with typing effect
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response.strip())

        # Append response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response.strip()})
