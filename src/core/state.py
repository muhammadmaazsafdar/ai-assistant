from src.config import PERSONAS, DEFAULT_PERSONA
import uuid
import streamlit as st

def init_state():
    if "chats" not in st.session_state:
        chat_id = str(uuid.uuid4())[:8]
        st.session_state.chats = {
            chat_id: {
                "name": "New Chat",
                "messages": [
                    {"role": "system", "content": PERSONAS[DEFAULT_PERSONA]}
                ],
                "starred": []
            }
        }
        st.session_state.active_chat = chat_id

    if "active_chat" not in st.session_state:
        st.session_state.active_chat = list(st.session_state.chats.keys())[0]