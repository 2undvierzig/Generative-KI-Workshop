# Generative KI Workshop

Dieses Repository bündelt Materialien für einen praxisnahen Workshop zu Generativer KI. Es enthält ein vollständiges Retrieval-Augmented-Generation (RAG) System, semesterweise gegliederte Unterrichtsnotebooks sowie begleitende Ressourcen für Automatisierung, MCP-Integrationen und Frontend-Demos.

## Verzeichnisüberblick

| Pfad | Inhalt |
| --- | --- |
| [`KI_Workshop_Für_Professoren/`](KI_Workshop_Für_Professoren/) | Produktionsreife RAG-Pipeline inklusive PDF-zu-Markdown-Konverter, Terminal-Chat auf Basis von Ollama & LlamaIndex, konfigurierbarer Model-/Embedding-Auswahl sowie Beispieldaten und Vektorspeicher. |
| [`KI_Workshop_Für_Professoren/archiv/`](KI_Workshop_Für_Professoren/archiv/) | Archivierte Streamlit-Oberfläche, die das gleiche RAG-Backend für eine geführte Chat-Erfahrung in einer Web-App nutzt. |
| [`Sommersemester_25/`](Sommersemester_25/) | Vier ausführliche Jupyter-Notebooks zu Ollama-Grundlagen, LlamaIndex-Tooling, n8n-Agent-Workflows und Blender-MCP-Integration; ergänzende Add-ons, JSON-Workflows sowie Bildressourcen für die Übungen. |
| [`Wintersemester_24_25/`](Wintersemester_24_25/) | Frühere Workshop-Auflage mit ähnlichem Aufbau (Kick-off, LlamaIndex, Gradio) plus Aufgabenplanung und Startskripten; dient als Referenz und Vergleichsbasis. |

## RAG-System für Professoren

Das Verzeichnis [`KI_Workshop_Für_Professoren/`](KI_Workshop_Für_Professoren/) liefert eine komplett dokumentierte Pipeline:

* **Konvertierungsstufe:** [`convert_pdf.py`](KI_Workshop_Für_Professoren/convert_pdf.py) liest PDF-Sammlungen stapelweise ein, extrahiert Text und Bilder mit marker-pdf und legt die Ergebnisse strukturiert in `llm_ready/` ab.
* **Indexierung & Chat:** [`rag_terminal_chat.py`](KI_Workshop_Für_Professoren/rag_terminal_chat.py) baut (oder lädt) Vektorindizes aus Markdown-Dateien, initialisiert Ollama-LLMs samt Embeddings und stellt ein Terminal-Interface bereit, inklusive Health-Checks, Index-Neuaufbau und Chat-Kommandos.
* **Konfiguration:** [`rag_config.py`](KI_Workshop_Für_Professoren/rag_config.py) hinterlegt Modell- und Embedding-Profile (von kompakten Gemma-Varianten bis zu Alternativen wie Llama 3.2 oder Mistral), Chunking-Parameter sowie Retrieval- und Memory-Einstellungen.
* **Onboarding:** Das lokale [README](KI_Workshop_Für_Professoren/README.md) beschreibt den Gesamtworkflow (virtuelle Umgebung, Paketinstallation, Ollama-Setup, PDF-Konvertierung, Start des Chats) und die benötigte Hardware ausführlich.
* **Archiv:** Die [Streamlit-App](KI_Workshop_Für_Professoren/archiv/streamlit_app.py) bewahrt eine Web-Oberfläche, die die gleichen Backing-Komponenten als Chat mit Statusanzeigen, Beispiel-Fragen und Index-Steuerung exponiert.

Beispieldaten (`data/03-1_Initialisierung_Lsg.pdf`) und der persistente Vektorspeicher (`storage/*.json`) sind bereits enthalten, sodass sich das System ohne weitere Vorarbeiten inspizieren lässt.

## Unterrichtsmodule Sommersemester 2025

Die vier Notebooks im Ordner [`Sommersemester_25/`](Sommersemester_25/) bauen aufeinander auf und nutzen gemeinsame Ressourcen (`ressource/`, `n8n_ressource/`, `data/`). Highlights je Kapitel:

1. **Kick-off & Gradio-Frontend:** [`01_Kick-off_SS25.ipynb`](Sommersemester_25/01_Kick-off_SS25.ipynb) führt in Ollama-Server, Modell-Deployment, Temperatur-Exploration, Jailbreaking/Red-Teaming, RSS-basierte Finanzanalysen und den Aufbau einer Gradio-Chatoberfläche mit LlamaIndex-Anbindung ein.
2. **Tools & MCP:** [`02_Tools_MCP_SS25.ipynb`](Sommersemester_25/02_Tools_MCP_SS25.ipynb) demonstriert Data-Loading mit LlamaIndex, FunctionTool-Beispiele für Rechnerfunktionen, ReAct-Agents, den Aufbau eines eigenen MCP-Servers mit FastMCP sowie dessen Integration in LLM-Clients (inklusive SSE-Betrieb).
3. **n8n AI Agents:** [`03_N8N_AI_Agents.ipynb`](Sommersemester_25/03_N8N_AI_Agents.ipynb) beschreibt Schritt für Schritt den Bau eines KI-Terminkalender-Assistenten, Google-OAuth-Einrichtung, Gemini-Integration, Memory/Tool-Konfiguration und die Automatisierung eines täglichen Newsletter-Workflows mit n8n.
4. **Blender MCP:** [`04_Blender_MCP.ipynb`](Sommersemester_25/04_Blender_MCP.ipynb) dokumentiert die Inbetriebnahme des Blender-MCP-Add-ons, Cursor-Integration, Modell-Provider-Konfiguration sowie die Steuerung einer Szene via Sprachmodell inklusive Beispielprompts und Visuals.

Zusätzliche Artefakte wie [`blender_mcp/addon.py`](Sommersemester_25/blender_mcp/addon.py), n8n-Workflow-JSONs und illustrative Screenshots sind direkt neben den Notebooks abgelegt.

## Unterrichtsmodule Wintersemester 2024/25

Diese Ausgabe deckt dieselben Kernkompetenzen mit leicht anderem Fokus und dient als Referenz oder Einstiegsversion:

* **Kick-off:** [`01_Kick-off.ipynb`](Wintersemester_24_25/01_Kick-off.ipynb) begleitet den lokalen Setup-Prozess mit Startskripten (`start_ollama.bat`, `start_jupyter.bat`), ersten API-Calls, Debugging und Kontextfenster-Konzepten.
* **LlamaIndex:** [`02_llama_index.ipynb`](Wintersemester_24_25/02_llama_index.ipynb) behandelt SimpleDirectoryReader, WebPageReader, FunctionTool-Definitionen, VectorStoreIndex, Retriever-Aufbau und Embedding-Konfiguration (z. B. `mxbai-embed-large`).
* **Gradio:** [`03_gradio.ipynb`](Wintersemester_24_25/03_gradio.ipynb) entwickelt schrittweise eine Gradio-Chatoberfläche, bindet Ollama an und erweitert sie um Mehrkomponenten-UIs sowie Multimodalität.
* **Planung & Aufgaben:** [`ki-ag-profs.ipynb`](Wintersemester_24_25/ki-ag-profs.ipynb) sammelt To-dos zur Konsolidierung der Kapitel und zur Ausrichtung auf einen praxisnahen Professor:innen-Use-Case.

Begleitende Daten (`data/Datenfusion.pdf`, `data/secret.txt`) spiegeln die Sommersemester-Struktur und erlauben einen direkten Versionsvergleich.

## Ressourcen & Assets

* **Bildmaterial:** [`Sommersemester_25/ressource/`](Sommersemester_25/ressource/) stellt Grafiken für Slides, Debug-Screenshots und Branding bereit, die direkt aus den Notebooks referenziert werden.
* **n8n-Workflows:** [`Sommersemester_25/n8n_ressource/`](Sommersemester_25/n8n_ressource/) enthält JSON-Exports und Parameter-Screenshots zum schnellen Import in n8n.
* **Beispieldaten:** Beide Semesterordner enthalten identische Datenquellen (PDF plus Beispiel-Secret), sodass Übungen reproduzierbar sind.

## Weiterführende Nutzung

* Verwende die Sommersemester-Notebooks als Hauptleitfaden für aktuelle Sessions; die Wintersemester-Version dient als abgespeckte Variante für schnelleres Onboarding.
* Der Professuren-Workflow kann direkt produktiv gemacht werden: Er nutzt generische Konfigurationsdateien und austauschbare Modelle, wodurch sich neue Lehrunterlagen nach PDF-Upload unmittelbar erschließen lassen.
* Dank der vorhandenen Assets (n8n-JSON, Blender-Add-on, Screenshots) lassen sich Live-Demos ohne zusätzlichen Download vorbereiten.