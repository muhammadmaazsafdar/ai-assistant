import streamlit as st
from src.config import PERSONAS
from src.components.chat_list import render_chat_list
from src.features.pdf import process_pdf
from src.features.starred import show_starred
from src.features.export import export_chat

def render_sidebar():
    with st.sidebar:
        st.markdown('<div class="sidebar-title">◆ brosAI</div>', unsafe_allow_html=True)

        render_chat_list()

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Persona**")
        selected_persona = st.selectbox(
            "Choose personality",
            list(PERSONAS.keys()),
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Upload a document**")
        uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
        if uploaded_file is not None:
            process_pdf(uploaded_file)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("**Starred Messages**")
        show_starred()

        st.markdown("<br>", unsafe_allow_html=True)
        export_chat()

        st.markdown("<br>", unsafe_allow_html=True)

        chat_id = st.session_state.active_chat
        messages = st.session_state.chats[chat_id]["messages"]
        message_count = len([m for m in messages if isinstance(m, dict) and m.get("role") != "system"])

        st.markdown(f"""
        <div class="stat-box">
            <div class="stat-label">Messages</div>
            <div class="stat-value">{message_count}</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Model</div>
            <div class="stat-value">Llama 3.1 8B</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Status</div>
            <div class="stat-value" style="color:#34d399">● Online</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🗑️ Clear conversation"):
            st.session_state.chats[chat_id]["messages"] = [
                {"role": "system", "content": PERSONAS[selected_persona]}
            ]
            st.rerun()

        return selected_persona