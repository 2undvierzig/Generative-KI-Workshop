# HAWKI UML-Generator mit Node.js

Dieses Projekt implementiert einen PlantUML-Generator mit der `node-plantuml` Bibliothek für das HAWKI-System.

## 🚀 Installation

1. **Node.js installieren** (falls noch nicht vorhanden):
   ```bash
   # Download von https://nodejs.org/
   ```

2. **Abhängigkeiten installieren**:
   ```bash
   npm install
   ```

## 📋 Verfügbare Skripte

### 1. Einfacher Test (wie in Ihrem Beispiel)
```bash
npm run test
```
Führt `test-generator.js` aus und generiert `diagram.png` und `diagram.svg` mit einem einfachen Klassendiagramm.

### 2. Erweiterter Generator
```bash
npm start
```
Führt `uml-generator.js` aus und generiert komplexere HAWKI-Architekturdiagramme im `generated/` Verzeichnis.

### 3. Web-Server starten
```bash
node server.js
```
Startet einen Express.js-Server auf http://localhost:3000 mit einer Web-API für PlantUML-Generierung.

## 📊 Verwendung

### Einfache Datei-Generierung (wie in Ihrem Code)
```javascript
const plantuml = require('node-plantuml');
const fs = require('fs');

// UML-Text laden
const umlSource = `
@startuml
Class01 <|-- Class02
@enduml
`;

// Rendern als PNG
const gen = plantuml.generate({ format: 'png' });
gen.out.pipe(fs.createWriteStream('diagram.png'));
gen.in.end(umlSource);
```

### Erweiterte Verwendung mit Promise
```javascript
const { generateDiagram } = require('./uml-generator');

async function example() {
    const umlSource = `
    @startuml
    class Benutzer {
        +String name
        +anmelden()
    }
    @enduml
    `;
    
    await generateDiagram(umlSource, 'mein-diagramm.png', 'png');
    console.log('Diagramm generiert!');
}
```

### Web-API verwenden
```javascript
// POST /api/generate-uml
fetch('http://localhost:3000/api/generate-uml', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        umlSource: '@startuml\nClass01 <|-- Class02\n@enduml',
        format: 'png'
    })
})
.then(response => response.blob())
.then(blob => {
    // Diagramm als Blob erhalten
});
```

## 📁 Projektstruktur

```
├── package.json           # Node.js Abhängigkeiten
├── uml-generator.js       # Hauptgenerator mit erweiterten Funktionen
├── test-generator.js      # Einfacher Test (wie in Ihrem Beispiel)
├── server.js             # Express.js Web-Server mit API
├── index.html            # Frontend (bestehend)
├── generated/            # Generierte Diagramme (wird erstellt)
└── temp/                 # Temporäre Dateien für Downloads
```

## 🔧 Unterstützte Formate

- **PNG**: `format: 'png'`
- **SVG**: `format: 'svg'`
- **PDF**: `format: 'pdf'` (experimentell)
- **EPS**: `format: 'eps'` (experimentell)

## 🌐 Web-API Endpunkte

### POST /api/generate-uml
Generiert ein Diagramm und sendet es als Stream zurück.

**Request:**
```json
{
    "umlSource": "@startuml\nClass01 <|-- Class02\n@enduml",
    "format": "png"
}
```

**Response:** Binärdaten des Diagramms

### POST /api/generate-file
Generiert ein Diagramm und bietet es als Download an.

### GET /api/example-uml
Gibt ein Beispiel-UML für das HAWKI-System zurück.

## ⚡ Vorteile des Node.js-Ansatzes

1. **Lokale Generierung**: Keine Abhängigkeit von externen PlantUML-Servern
2. **Bessere Performance**: Direkter Zugriff auf PlantUML
3. **Offline-Fähigkeit**: Funktioniert ohne Internetverbindung
4. **Erweiterte Kontrolle**: Vollständige Kontrolle über Generierungsprozess
5. **Integration**: Einfache Integration in bestehende Node.js-Projekte

## 🐛 Troubleshooting

### Java-Installation prüfen
Die `node-plantuml` Bibliothek benötigt Java:
```bash
java -version
```

### Abhängigkeiten neu installieren
```bash
rm -rf node_modules package-lock.json
npm install
```

### Debug-Modus
```javascript
const gen = plantuml.generate({ format: 'png', debug: true });
```

## 📝 Beispiele

Siehe `test-generator.js` für den einfachsten Ansatz und `uml-generator.js` für erweiterte Funktionen.

Das Projekt kann sowohl als eigenständige Lösung als auch als Backend für die bestehende HTML-Seite verwendet werden. 