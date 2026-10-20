#!/usr/bin/env python3
"""
Setup-Skript für das RAG-System
Automatisiert die Installation und erste Konfiguration
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    """Druckt den Header"""
    print("="*60)
    print("🚀 RAG-System Setup")
    print("="*60)
    print("Dieses Skript hilft bei der Einrichtung des RAG-Systems")
    print("mit LlamaIndex, Ollama und marker-pdf.")
    print("="*60)

def check_python_version():
    """Überprüft die Python-Version"""
    print("\n📋 Überprüfe Python-Version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ ist erforderlich!")
        print(f"   Aktuelle Version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} ist kompatibel")
    return True

def check_ollama():
    """Überprüft, ob Ollama installiert ist"""
    print("\n🤖 Überprüfe Ollama-Installation...")
    try:
        result = subprocess.run(["ollama", "--version"], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Ollama ist installiert")
            return True
        else:
            print("❌ Ollama ist nicht korrekt installiert")
            return False
    except (subprocess.TimeoutExpired, FileNotFoundError):
        print("❌ Ollama ist nicht installiert oder nicht im PATH")
        return False

def install_ollama():
    """Gibt Anweisungen zur Ollama-Installation"""
    print("\n📥 Ollama-Installation:")
    print("1. Besuchen Sie: https://ollama.ai/download")
    print("2. Laden Sie Ollama für Ihr Betriebssystem herunter")
    print("3. Installieren Sie Ollama")
    print("4. Starten Sie eine neue Kommandozeile")
    print("5. Führen Sie dieses Setup erneut aus")

def install_python_deps():
    """Installiert Python-Abhängigkeiten"""
    print("\n📦 Installiere Python-Abhängigkeiten...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True)
        print("✅ Python-Abhängigkeiten erfolgreich installiert")
        return True
    except subprocess.CalledProcessError:
        print("❌ Fehler beim Installieren der Python-Abhängigkeiten")
        return False

def download_ollama_models():
    """Lädt die erforderlichen Ollama-Modelle herunter"""
    print("\n🔽 Lade Ollama-Modelle herunter...")
    
    models = [
        ("llama3.1:8b", "LLM-Modell"),
        ("nomic-embed-text", "Embedding-Modell")
    ]
    
    for model, description in models:
        print(f"\n📥 Lade {description} ({model})...")
        try:
            result = subprocess.run(["ollama", "pull", model], 
                                  timeout=1800)  # 30 Minuten Timeout
            if result.returncode == 0:
                print(f"✅ {description} erfolgreich heruntergeladen")
            else:
                print(f"❌ Fehler beim Herunterladen von {description}")
                return False
        except subprocess.TimeoutExpired:
            print(f"⏰ Timeout beim Herunterladen von {description}")
            return False
        except Exception as e:
            print(f"❌ Fehler: {str(e)}")
            return False
    
    return True

def create_directories():
    """Erstellt notwendige Verzeichnisse"""
    print("\n📁 Erstelle Verzeichnisse...")
    directories = ["processed_pdfs", "chroma_db"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Verzeichnis '{directory}' erstellt")

def test_system():
    """Testet das System"""
    print("\n🧪 Teste Systemfunktionalität...")
    
    # Test Ollama-Verbindung
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✅ Ollama-Server ist erreichbar")
        else:
            print("⚠️ Ollama-Server antwortet nicht korrekt")
            return False
    except Exception:
        print("⚠️ Ollama-Server ist nicht erreichbar - starten Sie 'ollama serve'")
        return False
    
    # Test Python-Module
    try:
        import llama_index
        import chromadb
        import streamlit
        print("✅ Alle Python-Module sind verfügbar")
        return True
    except ImportError as e:
        print(f"❌ Fehler beim Importieren: {str(e)}")
        return False

def print_next_steps():
    """Druckt die nächsten Schritte"""
    print("\n🎉 Setup abgeschlossen!")
    print("="*60)
    print("📋 Nächste Schritte:")
    print("1. Starten Sie Ollama (falls nicht bereits gestartet):")
    print("   ollama serve")
    print()
    print("2. Legen Sie PDF-Dateien in den 'data/' Ordner")
    print()
    print("3. Starten Sie das RAG-System:")
    print("   # Web-Interface:")
    print("   python main.py --mode web")
    print()
    print("   # Kommandozeile:")
    print("   python main.py")
    print("="*60)

def main():
    """Hauptfunktion des Setup-Skripts"""
    print_header()
    
    # Python-Version prüfen
    if not check_python_version():
        sys.exit(1)
    
    # Ollama prüfen
    if not check_ollama():
        install_ollama()
        print("\n⚠️ Bitte installieren Sie Ollama und führen Sie das Setup erneut aus.")
        sys.exit(1)
    
    # Verzeichnisse erstellen
    create_directories()
    
    # Python-Abhängigkeiten installieren
    if not install_python_deps():
        sys.exit(1)
    
    # Frage nach Modell-Download
    print("\n❓ Möchten Sie die Ollama-Modelle jetzt herunterladen?")
    print("   (Dies kann einige Minuten dauern und benötigt ~5GB Speicherplatz)")
    choice = input("   [j/N]: ").lower().strip()
    
    if choice in ['j', 'ja', 'y', 'yes']:
        if not download_ollama_models():
            print("\n⚠️ Modell-Download fehlgeschlagen. Sie können dies später manuell durchführen.")
    else:
        print("\n📝 Hinweis: Laden Sie die Modelle später manuell herunter:")
        print("   ollama pull llama3.1:8b")
        print("   ollama pull nomic-embed-text")
    
    # System testen
    print("\n❓ Möchten Sie das System jetzt testen?")
    choice = input("   [j/N]: ").lower().strip()
    
    if choice in ['j', 'ja', 'y', 'yes']:
        if not test_system():
            print("\n⚠️ Systemtest fehlgeschlagen. Bitte überprüfen Sie die Installation.")
    
    print_next_steps()

if __name__ == "__main__":
    main() 