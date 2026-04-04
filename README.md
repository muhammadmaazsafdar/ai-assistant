# Voya — Personal AI Assistant

> A powerful, multi-persona AI assistant with PDF intelligence, multi-chat support, and a clean dark UI. Built with Python, Groq API, and Streamlit.

🔗 **Live Demo:** [https://aiassistant-45dog.streamlit.app/](https://aiassistant-45dog.streamlit.app/)

---

## What It Does

Voya is a fully deployed AI assistant that goes beyond basic chat. It adapts its personality to your needs, understands your documents, and keeps your conversations organized.

- **4 AI Personas** — Switch between Professional Assistant, Coding Mentor, Startup Advisor, and Career Coach
- **PDF Intelligence** — Upload any PDF and have a conversation with it
- **Multi-Chat** — Run multiple conversations simultaneously, each with its own history
- **Starred Messages** — Star important messages so you never lose key insights
- **Export Chats** — Download any conversation as a `.txt` file
- **Clean Dark UI** — Premium interface built with custom CSS

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13 | Core language |
| Groq API (Llama 3.1 8B) | AI engine |
| Streamlit | Web framework & UI |
| PyPDF2 | PDF text extraction |
| python-dotenv | Environment variable management |

---

## Project Structure

```
ai-assistant/
├── ui.py                  # Main entry point
├── app.py                 # Terminal chatbot version
├── requirements.txt       # Dependencies
└── src/
    ├── config.py          # Personas, constants, model config
    ├── styles.py          # All CSS styling
    ├── core/
    │   ├── chat.py        # Groq API calls & message handling
    │   └── state.py       # Session state initialization
    ├── components/
    │   ├── sidebar.py     # Sidebar UI component
    │   ├── chat_list.py   # Multi-chat management
    │   └── message.py     # Message display & star button
    └── features/
        ├── pdf.py         # PDF upload & text extraction
        ├── starred.py     # Starred messages logic
        └── export.py      # Chat export functionality
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com)

### Installation

```bash
# Clone the repository
git clone https://github.com/muhammadmaazsafdar/ai-assistant.git
cd ai-assistant

# Install dependencies
pip install -r requirements.txt

# Create environment file
echo GROQ_API_KEY=your_key_here > .env

# Run the app
streamlit run ui.py
```

---

## Roadmap

- [ ] Voice input support
- [ ] Image upload and analysis
- [ ] Persistent chat history across sessions
- [ ] n8n automation workflow integration
- [ ] Custom persona creation

---

## Author

**Muhammad Maaz Safdar**
- GitHub: [@muhammadmaazsafdar](https://github.com/muhammadmaazsafdar)
- LinkedIn: (https://www.linkedin.com/in/muhammadmoaaz/)

---

## License

MIT License — free to use and modify.