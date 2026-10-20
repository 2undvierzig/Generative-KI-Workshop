import streamlit as st
import logging
from pathlib import Path
from rag_system import RAGSystem
from config import DATA_DIR, LLM_MODEL, EMBEDDING_MODEL

# Streamlit-Seite konfigurieren
st.set_page_config(
    page_title="RAG-System für Lehrmaterialien",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS für besseres Design
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .status-box {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
</style>
""", unsafe_allow_html=True)

# Haupttitel
st.markdown('<h1 class="main-header">📚 RAG-System für Lehrmaterialien</h1>', unsafe_allow_html=True)

# Sidebar für Systemkonfiguration
with st.sidebar:
    st.header("⚙️ Systemkonfiguration")
    st.info(f"**LLM Modell:** {LLM_MODEL}")
    st.info(f"**Embedding Modell:** {EMBEDDING_MODEL}")
    st.info(f"**Datenverzeichnis:** {DATA_DIR}")
    
    st.header("📁 Verfügbare Dokumente")
    pdf_files = list(DATA_DIR.glob("*.pdf"))
    if pdf_files:
        for pdf in pdf_files:
            st.write(f"• {pdf.name}")
    else:
        st.warning("Keine PDF-Dateien gefunden")
    
    st.header("🔄 Systemaktionen")
    if st.button("🔄 Index neu erstellen", type="secondary"):
        st.session_state.force_reindex = True
        st.rerun()

# Initialisierung des RAG-Systems
@st.cache_resource
def initialize_rag_system(force_reindex=False):
    """Initialisiert das RAG-System und cached es"""
    try:
        with st.spinner("Initialisiere RAG-System..."):
            rag = RAGSystem()
            rag.initialize(force_reindex=force_reindex)
        return rag, None
    except Exception as e:
        return None, str(e)

# RAG-System initialisieren
force_reindex = st.session_state.get('force_reindex', False)
if force_reindex:
    st.session_state.force_reindex = False
    st.cache_resource.clear()

rag_system, error = initialize_rag_system(force_reindex)

# Status anzeigen
if error:
    st.markdown(f'<div class="status-box error-box">❌ <strong>Fehler beim Initialisieren:</strong> {error}</div>', 
                unsafe_allow_html=True)
    st.stop()
elif rag_system:
    st.markdown('<div class="status-box success-box">✅ <strong>RAG-System erfolgreich initialisiert!</strong></div>', 
                unsafe_allow_html=True)

# Hauptbereich für Fragen und Antworten
st.header("💬 Fragen Sie das System")

# Session State für Chat-Historie
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Chat-Interface
col1, col2 = st.columns([3, 1])

with col1:
    question = st.text_input(
        "Stellen Sie eine Frage zu den Lehrmaterialien:",
        placeholder="z.B. Was sind die wichtigsten Konzepte der objektorientierten Programmierung?"
    )

with col2:
    ask_button = st.button("🔍 Fragen", type="primary", use_container_width=True)

# Beispielfragen
with st.expander("💡 Beispielfragen"):
    example_questions = [
        "Was ist der Unterschied zwischen Klassen und Objekten?",
        "Erkläre das Konzept der Vererbung in der OOP",
        "Was sind die wichtigsten Operatoren in der Programmierung?",
        "Wie funktioniert die Initialisierung von Objekten?",
        "Was sind Beziehungen zwischen Klassen?"
    ]
    
    for i, eq in enumerate(example_questions):
        if st.button(f"📝 {eq}", key=f"example_{i}"):
            question = eq
            ask_button = True

# Frage verarbeiten
if (ask_button or question) and question and rag_system:
    with st.spinner("Bearbeite Ihre Frage..."):
        try:
            answer = rag_system.query(question)
            
            # Zur Chat-Historie hinzufügen
            st.session_state.chat_history.append({
                "question": question,
                "answer": answer
            })
            
            # Aktuelle Antwort anzeigen
            st.subheader("🤖 Antwort:")
            st.write(answer)
            
        except Exception as e:
            st.error(f"Fehler beim Beantworten der Frage: {str(e)}")

# Chat-Historie anzeigen
if st.session_state.chat_history:
    st.header("📝 Chat-Historie")
    
    # Button zum Löschen der Historie
    if st.button("🗑️ Historie löschen"):
        st.session_state.chat_history = []
        st.rerun()
    
    # Historie in umgekehrter Reihenfolge anzeigen (neueste zuerst)
    for i, chat in enumerate(reversed(st.session_state.chat_history)):
        with st.expander(f"Frage {len(st.session_state.chat_history) - i}: {chat['question'][:50]}..."):
            st.write("**Frage:**", chat['question'])
            st.write("**Antwort:**", chat['answer'])

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; font-size: 0.8rem;'>
        🚀 RAG-System basierend auf LlamaIndex, Ollama und marker-pdf<br>
        📧 Für Fragen und Support wenden Sie sich an den Administrator
    </div>
    """, 
    unsafe_allow_html=True
) 