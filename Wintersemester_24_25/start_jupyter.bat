@echo off
REM Pfad zum Anaconda-Installationsverzeichnis anpassen
CALL "C:\ProgramData\miniconda3\Scripts\activate.bat"

REM Wechsel in das gewünschte Verzeichnis unter Verwendung von pushd für UNC-Pfade
pushd "Z:\"

REM Starte Jupyter Lab
jupyter lab
