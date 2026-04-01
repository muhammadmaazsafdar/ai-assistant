import streamlit as st
from groq import Groq
from src.config import MODEL
import os

def get_client():
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    return Groq(api_key=api_key)

def get_active_messages():
    chat_id = st.session_state.active_chat
    return st.session_state.chats[chat_id]["messages"]

def send_message(client, user_input):
    messages = get_active_messages()
    messages.append({"role": "user", "content": user_input})

    clean_history = [
        m for m in messages
        if isinstance(m, dict) and m.get("role") and m.get("content")
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=clean_history
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply