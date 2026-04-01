import streamlit as st
from dotenv import load_dotenv

from src.styles import load_styles
from src.core.state import init_state
from src.core.chat import get_client, send_message
from src.components.sidebar import render_sidebar
from src.components.message import render_messages

load_dotenv()

st.set_page_config(
    page_title="brosAI",
    page_icon="◆",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(load_styles(), unsafe_allow_html=True)

init_state()

selected_persona = render_sidebar()

client = get_client()

chat_id = st.session_state.active_chat
messages = st.session_state.chats[chat_id]["messages"]
message_count = len([m for m in messages if isinstance(m, dict) and m.get("role") != "system"])

if message_count == 0:
    st.markdown("""
    <div class="main-header">
        <h1>brosAI</h1>
        <p>Your personal AI assistant</p>
    </div>
    <div class="divider"></div>
    """, unsafe_allow_html=True)

render_messages()

user_input = st.chat_input("Ask me anything...")

if user_input:
    send_message(client, user_input)
    st.rerun()