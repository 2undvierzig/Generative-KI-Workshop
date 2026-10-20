import os
from pathlib import Path

# Ollama Konfiguration
OLLAMA_BASE_URL = "http://localhost:11434"
LLM_MODEL = "llama3.1:8b"
EMBEDDING_MODEL = "nomic-embed-text"

# Datenverzeichnis
DATA_DIR = Path("./data")
CHROMA_DB_PATH = Path("./chroma_db")

# Marker-PDF Konfiguration
MARKER_OUTPUT_DIR = Path("./processed_pdfs")

# Sicherstellen, dass Verzeichnisse existieren
CHROMA_DB_PATH.mkdir(exist_ok=True)
MARKER_OUTPUT_DIR.mkdir(exist_ok=True) 