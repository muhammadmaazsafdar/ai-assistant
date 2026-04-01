import streamlit as st
from src.features.starred import toggle_star

def render_messages():
    chat_id = st.session_state.active_chat
    messages = st.session_state.chats[chat_id]["messages"]
    starred = st.session_state.chats[chat_id]["starred"]

    for i, message in enumerate(messages):
        if not isinstance(message, dict):
            continue
        if message.get("role") == "system":
            continue

        with st.chat_message(message["role"]):
            st.write(message["content"])

            is_starred = i in starred
            star_label = "⭐ Starred" if is_starred else "☆ Star"

            if st.button(star_label, key=f"star_{chat_id}_{i}"):
                toggle_star(i)
                st.rerun()