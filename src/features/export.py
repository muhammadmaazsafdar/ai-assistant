import streamlit as st

def export_chat():
    chat_id = st.session_state.active_chat
    messages = st.session_state.chats[chat_id]["messages"]
    chat_name = st.session_state.chats[chat_id]["name"]

    text = f"Chat: {chat_name}\n"
    text += "=" * 40 + "\n\n"

    for m in messages:
        if not isinstance(m, dict):
            continue
        if m.get("role") == "system":
            continue
        role = "You" if m["role"] == "user" else "brosAI"
        text += f"{role}:\n{m['content']}\n\n"

    st.download_button(
        label="⬇️ Export chat",
        data=text,
        file_name=f"{chat_name}.txt",
        mime="text/plain"
    )