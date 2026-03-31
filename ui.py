import streamlit as st
from groq import Groq

from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("My AI Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are an AI Assistant that handles multiple tasks at once and is always respectful to customers."}
    ]

# Block 1 - Display messages
for message in st.session_state.chat_history:
    if message["role"] == "system":
        continue
    st.chat_message(message["role"]).write(message["content"])

# Block 2 - Handle new input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append({"role":"user","content":user_input})
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.chat_history
    )
    
    reply = response.choices[0].message.content
    st.session_state.chat_history.append({"role":"assistant","content":reply})
    
    st.rerun()