import streamlit as st
from utils.chatbot_personal import chatbot
import requests
    
def talktome():
    st.title("💬 Talk to me")
    st.subheader("You can ask me any question anonymously, and my RAG will answer you")
    st.caption("Powered with Llama3")


    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "I am Guilherme's RAG. How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    if prompt := st.chat_input():

        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        answer = chatbot(str(st.session_state.messages))
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(msg)