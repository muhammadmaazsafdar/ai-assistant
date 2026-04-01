import PyPDF2
import io
import streamlit as st
from src.config import MAX_PDF_CHARS

def process_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

    pdf_text = pdf_text[:MAX_PDF_CHARS]

    chat_id = st.session_state.active_chat
    st.session_state.chats[chat_id]["messages"][0] = {
        "role": "system",
        "content": f"You are a helpful assistant. Answer questions based on this document:\n\n{pdf_text}"
    }
    st.success(f"Document loaded! ({len(pdf_text)} characters)")