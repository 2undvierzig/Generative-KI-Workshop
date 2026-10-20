# Generative KI Workshop

Dieses Repository bündelt Materialien für einen praxisnahen Workshop zu Generativer KI. Es enthält ein vollständiges Retrieval-Augmented-Generation (RAG) System, semesterweise gegliederte Unterrichtsnotebooks sowie begleitende Ressourcen für Automatisierung, MCP-Integrationen und Frontend-Demos.

## Verzeichnisüberblick

| Pfad | Inhalt |
| --- | --- |
| `KI_Workshop_Für_Professoren/` | Produktionsreife RAG-Pipeline inklusive PDF-zu-Markdown-Konverter, Terminal-Chat auf Basis von Ollama & LlamaIndex, konfigurierbarer Model-/Embedding-Auswahl sowie Beispieldaten und Vektorspeicher.【F:KI_Workshop_Für_Professoren/README.md†L1-L118】【F:KI_Workshop_Für_Professoren/convert_pdf.py†L1-L176】【F:KI_Workshop_Für_Professoren/rag_terminal_chat.py†L1-L200】【F:KI_Workshop_Für_Professoren/rag_config.py†L1-L99】
| `KI_Workshop_Für_Professoren/archiv/` | Archivierte Streamlit-Oberfläche, die das gleiche RAG-Backend für eine geführte Chat-Erfahrung in einer Web-App nutzt.【F:KI_Workshop_Für_Professoren/archiv/streamlit_app.py†L1-L160】
| `Sommersemester_25/` | Vier ausführliche Jupyter-Notebooks zu Ollama-Grundlagen, LlamaIndex-Tooling, n8n-Agent-Workflows und Blender-MCP-Integration; ergänzende Add-ons, JSON-Workflows sowie Bildressourcen für die Übungen.【F:Sommersemester_25/01_Kick-off_SS25.ipynb†L35-L757】【F:Sommersemester_25/02_Tools_MCP_SS25.ipynb†L33-L520】【F:Sommersemester_25/03_N8N_AI_Agents.ipynb†L18-L182】【F:Sommersemester_25/04_Blender_MCP.ipynb†L18-L146】【8c704d†L1-L148】【3c5e1d†L1-L3】【e827b7†L1-L3】
| `Wintersemester_24_25/` | Frühere Workshop-Auflage mit ähnlichem Aufbau (Kick-off, LlamaIndex, Gradio) plus Aufgabenplanung und Startskripten; dient als Referenz und Vergleichsbasis.【F:Wintersemester_24_25/01_Kick-off.ipynb†L32-L214】【F:Wintersemester_24_25/02_llama_index.ipynb†L33-L420】【F:Wintersemester_24_25/03_gradio.ipynb†L33-L208】【F:Wintersemester_24_25/ki-ag-profs.ipynb†L1-L19】

## RAG-System für Professor:innen

Das Verzeichnis `KI_Workshop_Für_Professoren/` liefert eine komplett dokumentierte Pipeline:

* **Konvertierungsstufe:** `convert_pdf.py` liest PDF-Sammlungen stapelweise ein, extrahiert Text und Bilder mit marker-pdf und legt die Ergebnisse strukturiert in `llm_ready/` ab.【F:KI_Workshop_Für_Professoren/convert_pdf.py†L1-L176】
* **Indexierung & Chat:** `rag_terminal_chat.py` baut (oder lädt) Vektorindizes aus Markdown-Dateien, initialisiert Ollama-LLMs samt Embeddings und stellt ein Terminal-Interface bereit, inklusive Health-Checks, Index-Neuaufbau und Chat-Kommandos.【F:KI_Workshop_Für_Professoren/rag_terminal_chat.py†L1-L200】
* **Konfiguration:** `rag_config.py` hinterlegt Modell- und Embedding-Profile (von kompakten Gemma-Varianten bis zu Alternativen wie Llama 3.2 oder Mistral), Chunking-Parameter sowie Retrieval- und Memory-Einstellungen.【F:KI_Workshop_Für_Professoren/rag_config.py†L7-L99】
* **Onboarding:** Das lokale README beschreibt den Gesamtworkflow (virtuelle Umgebung, Paketinstallation, Ollama-Setup, PDF-Konvertierung, Start des Chats) und die benötigte Hardware ausführlich.【F:KI_Workshop_Für_Professoren/README.md†L5-L172】
* **Archiv:** Die `archiv/`-Ordnerstruktur bewahrt eine Streamlit-Oberfläche, die die gleichen Backing-Komponenten als Web-Chat mit Statusanzeigen, Beispiel-Fragen und Index-Steuerung exponiert.【F:KI_Workshop_Für_Professoren/archiv/streamlit_app.py†L1-L160】

Beispieldaten (`data/03-1_Initialisierung_Lsg.pdf`) und der persistente Vektorspeicher (`storage/*.json`) sind bereits enthalten, sodass sich das System ohne weitere Vorarbeiten inspizieren lässt.【78f899†L1-L2】【929d2a†L1-L5】

## Unterrichtsmodule Sommersemester 2025

Die vier Notebooks im Ordner `Sommersemester_25/` bauen aufeinander auf und nutzen gemeinsame Ressourcen (`ressource/`, `n8n_ressource/`, `data/`).【e827b7†L1-L3】【3c5e1d†L1-L3】【b63959†L1-L2】 Highlights je Kapitel:

1. **Kick-off & Gradio-Frontend:** Einführung in Ollama-Server, Modell-Deployment, Temperatur-Exploration, Jailbreaking/Red-Teaming, RSS-basierte Finanzanalysen und der Aufbau einer Gradio-Chatoberfläche mit LlamaIndex-Anbindung.【F:Sommersemester_25/01_Kick-off_SS25.ipynb†L35-L757】
2. **Tools & MCP:** Data-Loading mit LlamaIndex, FunctionTool-Beispiele für Rechnerfunktionen, ReAct-Agents, Aufbau eines eigenen MCP-Servers mit FastMCP sowie dessen Integration in LLM-Clients (inklusive SSE-Betrieb).【F:Sommersemester_25/02_Tools_MCP_SS25.ipynb†L55-L520】
3. **n8n AI Agents:** Schritt-für-Schritt-Anleitung zum Bau eines KI-Terminkalender-Assistenten, Google-OAuth-Einrichtung, Gemini-Integration, Memory/Tool-Konfiguration und Automatisierung eines täglichen Newsletter-Workflows mit n8n.【F:Sommersemester_25/03_N8N_AI_Agents.ipynb†L18-L182】
4. **Blender MCP:** Dokumentiert die Inbetriebnahme des Blender-MCP-Add-ons, Cursor-Integration, Modell-Provider-Konfiguration sowie die Steuerung einer Szene via Sprachmodell inklusive Beispielprompts und Visuals.【F:Sommersemester_25/04_Blender_MCP.ipynb†L18-L146】

Zusätzliche Artefakte wie `blender_mcp/addon.py`, n8n-Workflow-JSONs und illustrative Screenshots sind direkt neben den Notebooks abgelegt.【a9c676†L1-L2】【3c5e1d†L1-L3】【e827b7†L1-L3】

## Unterrichtsmodule Wintersemester 2024/25

Diese Ausgabe deckt dieselben Kernkompetenzen mit leicht anderem Fokus und dient als Referenz oder Einstiegsversion:

* **Kick-off:** Startskripte (`start_ollama.bat`, `start_jupyter.bat`) unterstützen beim lokalen Setup; das Notebook führt durch Ollama-Start, erste API-Calls, Debugging und Kontextfenster-Konzepte.【F:Wintersemester_24_25/01_Kick-off.ipynb†L32-L214】
* **LlamaIndex:** Von SimpleDirectoryReader und WebPageReader über FunctionTool-Definitionen bis hin zu VectorStoreIndex, Retriever-Aufbau und Embedding-Konfiguration (z. B. `mxbai-embed-large`).【F:Wintersemester_24_25/02_llama_index.ipynb†L33-L420】
* **Gradio:** Schrittweise Entwicklung einer Gradio-Chatoberfläche, Anbindung an Ollama und Erweiterung um Mehrkomponenten-UIs und Multimodalität.【F:Wintersemester_24_25/03_gradio.ipynb†L33-L208】
* **Planung & Aufgaben:** `ki-ag-profs.ipynb` sammelt To-dos zur Konsolidierung der Kapitel und zur Ausrichtung auf einen praxisnahen Professor:innen-Use-Case.【F:Wintersemester_24_25/ki-ag-profs.ipynb†L1-L19】

Begleitende Daten (`data/Datenfusion.pdf`, `data/secret.txt`) spiegeln die Sommersemester-Struktur und erlauben einen direkten Versionsvergleich.【9c971f†L1-L2】【bed54a†L1-L2】

## Ressourcen & Assets

* **Bildmaterial:** `Sommersemester_25/ressource/` stellt Grafiken für Slides, Debug-Screenshots und Branding bereit, die direkt aus den Notebooks referenziert werden.【e827b7†L1-L3】
* **n8n-Workflows:** `Sommersemester_25/n8n_ressource/` enthält JSON-Exports und Parameter-Screenshots zum schnellen Import in n8n.【3c5e1d†L1-L3】
* **Beispieldaten:** Beide Semesterordner enthalten identische Datenquellen (PDF plus Beispiel-Secret), sodass Übungen reproduzierbar sind.【b63959†L1-L2】【137fa7†L1-L1】【9c971f†L1-L2】【bed54a†L1-L1】

## Weiterführende Nutzung

* Verwende die Sommersemester-Notebooks als Hauptleitfaden für aktuelle Sessions; die Wintersemester-Version dient als abgespeckte Variante für schnelleres Onboarding.
* Der Professuren-Workflow kann direkt produktiv gemacht werden: Er nutzt generische Konfigurationsdateien und austauschbare Modelle, wodurch sich neue Lehrunterlagen nach PDF-Upload unmittelbar erschließen lassen.【F:KI_Workshop_Für_Professoren/README.md†L5-L172】【F:KI_Workshop_Für_Professoren/rag_config.py†L7-L99】
* Dank der vorhandenen Assets (n8n-JSON, Blender-Add-on, Screenshots) lassen sich Live-Demos ohne zusätzlichen Download vorbereiten.【3c5e1d†L1-L3】【a9c676†L1-L2】【e827b7†L1-L3】

