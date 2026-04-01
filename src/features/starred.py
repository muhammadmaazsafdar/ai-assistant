import streamlit as st

def toggle_star(message_index):
    chat_id = st.session_state.active_chat
    starred = st.session_state.chats[chat_id]["starred"]

    if message_index in starred:
        starred.remove(message_index)
    else:
        starred.append(message_index)

def show_starred():
    chat_id = st.session_state.active_chat
    chat = st.session_state.chats[chat_id]
    starred = chat["starred"]
    messages = chat["messages"]

    if not starred:
        st.caption("No starred messages yet.")
        return

    for idx in starred:
        if idx < len(messages):
            m = messages[idx]
            if isinstance(m, dict) and m.get("role") != "system":
                role = "You" if m["role"] == "user" else "brosAI"
                st.markdown(f"""
                <div class="starred-msg">
                    <strong>{role}:</strong> {m['content']}
                </div>
                """, unsafe_allow_html=True)