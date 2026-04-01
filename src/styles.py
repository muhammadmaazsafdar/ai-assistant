def load_styles():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0a0a0f; }
section[data-testid="stSidebar"] { background: #0f0f18; border-right: 1px solid #1e1e2e; }

.main-header { text-align: center; padding: 4rem 0 2rem; }
.main-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ff6b6b, #a78bfa, #00d2ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    letter-spacing: -0.04em;
    line-height: 1;
}
.main-header p {
    color: #4a4a6a;
    font-size: 0.95rem;
    font-weight: 300;
    margin-top: 0.6rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}

.divider { height: 1px; background: linear-gradient(90deg, transparent, #1e1e3e, transparent); margin: 1.5rem 0 2rem; }

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

.sidebar-title { 
    font-family: 'Syne', sans-serif; 
    font-size: 1.1rem; 
    font-weight: 600; 
    color: #a78bfa; 
    margin-bottom: 1rem; 
}

.chat-item { 
    padding: 0.6rem 0.8rem; 
    border-radius: 8px; 
    cursor: pointer; 
    margin-bottom: 4px; 
    color: #8080a0; 
    font-size: 0.85rem; 
    border: 1px solid transparent; 
}
.chat-item:hover { background: #13131f; border-color: #1e1e2e; color: #c4c4e0; }
.chat-item.active { background: #1a1a2e; border-color: #a78bfa44; color: #e0e0ff; }

.stat-box { 
    background: #13131f; 
    border: 1px solid #1e1e2e; 
    border-radius: 12px; 
    padding: 0.8rem 1rem; 
    margin-bottom: 0.6rem; 
}
.stat-label { 
    color: #4a4a6a; 
    font-size: 0.7rem; 
    text-transform: uppercase; 
    letter-spacing: 0.1em; 
}
.stat-value { 
    color: #e0e0ff; 
    font-size: 1rem; 
    font-weight: 500; 
    margin-top: 0.2rem; 
}

.starred-msg { 
    background: #1a1500; 
    border: 1px solid #a78bfa44; 
    border-radius: 10px; 
    padding: 0.7rem 1rem; 
    margin-bottom: 0.5rem; 
    font-size: 0.85rem; 
    color: #c4c4e0; 
}

footer {visibility: hidden;}
#MainMenu {visibility: hidden;}
</style>
"""