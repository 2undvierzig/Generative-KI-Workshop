# HAWKI-System UML-Diagramm Viewer

Dieser einfache Viewer ermöglicht die Darstellung und Bearbeitung des HAWKI-System UML-Diagramms mit Hilfe des offiziellen PlantUML-Servers.

## Funktionen

- Anzeige des HAWKI-System UML-Diagramms
- Wechsel zwischen SVG- und PNG-Ausgabeformat
- Bearbeitung des PlantUML-Quelltextes direkt im Browser
- Sofortige Aktualisierung des Diagramms nach Änderungen

## Verwendung

1. Öffnen Sie die `index.html` Datei in einem Webbrowser
2. Das Diagramm wird automatisch geladen und angezeigt
3. Sie können den PlantUML-Quelltext im Textfeld bearbeiten
4. Klicken Sie auf "Diagramm neu rendern", um Ihre Änderungen anzuzeigen
5. Wählen Sie zwischen SVG- und PNG-Format mit den entsprechenden Schaltflächen

## Technische Details

- Die Anwendung verwendet den offiziellen PlantUML-Server für das Rendering
- Es ist keine Installation erforderlich, nur ein Webbrowser mit Internetverbindung
- Der PlantUML-Quelltext wird per URL-Parameter an den Server gesendet
- Das Diagramm wird direkt im Browser angezeigt

## Hinweis

Diese Anwendung sendet den UML-Quelltext an den öffentlichen PlantUML-Server (plantuml.com). 
Für sensible Diagramme sollten Sie einen eigenen PlantUML-Server einrichten oder eine lokale Rendering-Lösung verwenden. 