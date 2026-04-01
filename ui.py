import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import PyPDF2
import io
import os

load_dotenv()

st.set_page_config(
    page_title="Aria AI Assistant",
    page_icon="◆",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0a0a0f; }
section[data-testid="stSidebar"] { background: #0f0f18; border-right: 1px solid #1e1e2e; }
.main-header { text-align: center; padding: 2rem 0 1rem; }
.main-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    letter-spacing: -0.02em;
}
.main-header p {
    color: #4a4a6a;
    font-size: 0.9rem;
    font-weight: 300;
    margin-top: 0.4rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.divider { height: 1px; background: linear-gradient(90deg, transparent, #1e1e3e, transparent); margin: 1rem 0 2rem; }
.stChatMessageContent {
    background: #13131f !important;
    border: 1px solid #1e1e3e !important;
    border-radius: 16px !important;
    color: #c4c4e0 !important;
    font-size: 0.95rem !important;
    line-height: 1.7 !important;
    padding: 1rem 1.2rem !important;
}
[data-testid="stChatInput"] {
    background: #0f0f1a !important;
    border: 1px solid #2a2a4a !important;
    border-radius: 16px !important;
    color: #e0e0ff !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: #a78bfa !important;
    box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.15) !important;
}
.sidebar-title { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 600; color: #a78bfa; margin-bottom: 1rem; }
.stat-box { background: #13131f; border: 1px solid #1e1e2e; border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 0.6rem; }
.stat-label { color: #4a4a6a; font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; }
.stat-value { color: #e0e0ff; font-size: 1rem; font-weight: 500; margin-top: 0.2rem; }
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

PERSONAS = {
    "◆ Professional Assistant": "You are a highly professional AI assistant. You are precise, concise, and always helpful. You speak formally and deliver accurate information efficiently.",
    "⚡ Coding Mentor": "You are an expert coding mentor. You explain code clearly, help debug issues, and teach best practices. You use simple language and real examples.",
    "🚀 Startup Advisor": "You are a sharp startup advisor with deep knowledge of business strategy, fundraising, and growth. You give direct, actionable advice like a seasoned entrepreneur.",
    "🎯 Career Coach": "You are a career coach specializing in tech careers. You help with resumes, interviews, salary negotiation, and career growth strategies."
}

with st.sidebar:
    st.markdown('<div class="sidebar-title">◆ ARIA ASSISTANT</div>', unsafe_allow_html=True)

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
        file_name = uploaded_file.name
        if st.session_state.get("loaded_file") != file_name:
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

            st.session_state.chat_history[0] = [
                {
                    "role": "system",
                    "content": f"You are a helpful assistant. Answer questions based on this document:\n\n{pdf_text}"
                }
            ]
            st.session_state.loaded_file = file_name
            st.success("Document loaded! Ask me anything about it.")

    st.markdown("<br>", unsafe_allow_html=True)

    message_count = len([m for m in st.session_state.get("chat_history", []) if isinstance(m, dict) and m.get("role") != "system"])
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
        st.session_state.chat_history = [
            {"role": "system", "content": PERSONAS[selected_persona]}
        ]
        st.rerun()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": PERSONAS[selected_persona]}
    ]

st.markdown("""
<div class="main-header">
    <h1>Aria</h1>
    <p>Your personal AI assistant</p>
</div>
<div class="divider"></div>
""", unsafe_allow_html=True)

for message in st.session_state.chat_history:
    if not isinstance(message, dict):
        continue
    if message.get("role") == "system":
        continue
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.chat_history
    )

    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.rerun()