#!/usr/bin/env python3
"""
Hauptdatei für das RAG-System
Ermöglicht sowohl Kommandozeilen- als auch Streamlit-Nutzung
"""

import argparse
import logging
from pathlib import Path
from rag_system import RAGSystem

def setup_logging():
    """Konfiguriert das Logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    """Hauptfunktion für die Kommandozeilen-Nutzung"""
    parser = argparse.ArgumentParser(description="RAG-System für Lehrmaterialien")
    parser.add_argument(
        "--mode", 
        choices=["cli", "web"], 
        default="cli",
        help="Ausführungsmodus: cli für Kommandozeile, web für Streamlit"
    )
    parser.add_argument(
        "--reindex", 
        action="store_true",
        help="Erzwingt eine Neuindizierung der Dokumente"
    )
    parser.add_argument(
        "--question", 
        type=str,
        help="Direkte Frage an das System (nur für CLI-Modus)"
    )
    
    args = parser.parse_args()
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    if args.mode == "web":
        # Streamlit-App starten
        import subprocess
        import sys
        
        logger.info("Starte Streamlit-App...")
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
        except KeyboardInterrupt:
            logger.info("Streamlit-App beendet")
    
    else:
        # CLI-Modus
        try:
            logger.info("Initialisiere RAG-System...")
            rag = RAGSystem()
            rag.initialize(force_reindex=args.reindex)
            
            if args.question:
                # Direkte Frage beantworten
                logger.info(f"Beantworte Frage: {args.question}")
                answer = rag.query(args.question)
                print("\n" + "="*50)
                print("ANTWORT:")
                print("="*50)
                print(answer)
                print("="*50)
            else:
                # Interaktiver Modus
                print("\n🎯 RAG-System für Lehrmaterialien")
                print("="*50)
                print("Geben Sie 'quit' oder 'exit' ein, um das Programm zu beenden.")
                print("Geben Sie 'help' ein, um verfügbare Befehle zu sehen.")
                print("="*50)
                
                while True:
                    try:
                        question = input("\n❓ Ihre Frage: ").strip()
                        
                        if question.lower() in ['quit', 'exit', 'q']:
                            print("Auf Wiedersehen! 👋")
                            break
                        
                        if question.lower() == 'help':
                            print("\n📖 Verfügbare Befehle:")
                            print("- quit/exit/q: Programm beenden")
                            print("- help: Diese Hilfe anzeigen")
                            print("- Beliebige Frage: Wird vom System beantwortet")
                            continue
                        
                        if not question:
                            print("⚠️ Bitte geben Sie eine Frage ein.")
                            continue
                        
                        print("\n🤔 Denke nach...")
                        answer = rag.query(question)
                        
                        print("\n💡 Antwort:")
                        print("-" * 30)
                        print(answer)
                        print("-" * 30)
                        
                    except KeyboardInterrupt:
                        print("\n\nAuf Wiedersehen! 👋")
                        break
                    except Exception as e:
                        logger.error(f"Fehler beim Beantworten der Frage: {str(e)}")
                        print(f"❌ Fehler: {str(e)}")
        
        except Exception as e:
            logger.error(f"Fehler beim Initialisieren des RAG-Systems: {str(e)}")
            print(f"❌ Kritischer Fehler: {str(e)}")
            return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 