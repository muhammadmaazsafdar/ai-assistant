import streamlit as st
from src.config import PERSONAS, DEFAULT_PERSONA
import uuid

def create_new_chat():
    chat_id = str(uuid.uuid4())[:8]
    st.session_state.chats[chat_id] = {
        "name": f"Chat {len(st.session_state.chats) + 1}",
        "messages": [
            {"role": "system", "content": PERSONAS[DEFAULT_PERSONA]}
        ],
        "starred": []
    }
    st.session_state.active_chat = chat_id
    st.rerun()

def rename_chat(chat_id, new_name):
    st.session_state.chats[chat_id]["name"] = new_name

def delete_chat(chat_id):
    if len(st.session_state.chats) == 1:
        return
    del st.session_state.chats[chat_id]
    st.session_state.active_chat = list(st.session_state.chats.keys())[0]
    st.rerun()

def render_chat_list():
    st.markdown("**Chats**")

    if st.button("＋ New Chat", use_container_width=True):
        create_new_chat()

    st.markdown("<br>", unsafe_allow_html=True)

    for chat_id, chat in list(st.session_state.chats.items()):
        is_active = chat_id == st.session_state.active_chat
        col1, col2 = st.columns([5, 1])

        with col1:
            label = f"{'◆ ' if is_active else ''}{chat['name']}"
            if st.button(label, key=f"chat_{chat_id}", use_container_width=True):
                st.session_state.active_chat = chat_id
                st.rerun()

        with col2:
            if st.button("🗑", key=f"del_{chat_id}"):
                delete_chat(chat_id)