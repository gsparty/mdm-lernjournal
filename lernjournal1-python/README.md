# Lernjournal 1 Python

## Repository und Library

https://github.com/gsparty/projekt1-bike-scraper

| Die App scrapt Daten von Tutti, extrahiert relevante Parameter für Fahrradanzeigen und schätzt die Wahrscheinlichkeit eines erfolgreichen Verkaufs sowie die voraussichtliche Verkaufsdauer. | 
Es wird die Wahrscheinlichkeit anzeigen, dass das Motorrad aud Tuti verkauft werden kann und schätzt dessen Dauer|
| Verwendete Library aus PyPi (Name) |
Flask, requests, beautifulsoup4, pandas, scikit-learn, joblib, numpy, gunicorn, pytest, azure|
| Verwendete Library aus PyPi (URL) | |
| https://pypi.org/project/Flask/2.3.2/ | | 
| https://pypi.org/project/requests/2.28.2/ | | 
| https://pypi.org/project/beautifulsoup4/4.11.1/ | | 
| https://pypi.org/project/pandas/1.5.3/ | | 
| https://pypi.org/project/scikit-learn/1.2.1/ | | 
| https://pypi.org/project/joblib/1.2.0/ | | 
| https://pypi.org/project/numpy/1.24.2/ | |
| https://pypi.org/project/gunicorn/20.1.1/ | | 
| https://pypi.org/project/pytest/7.2.2/ | | 
| https://pypi.org/project/azure/4.7.0/ | |

## App, Funktionalität

Die App scrapt Daten von der Plattform Tutti, extrahiert relevante Parameter wie Preis, Zustand und Standort der Fahrräder und nutzt diese, um die Wahrscheinlichkeit eines erfolgreichen Verkaufs sowie die voraussichtliche Verkaufsdauer zu schätzen. Das Modell basiert auf maschinellem Lernen und analysiert historische Verkaufsdaten, um präzise Vorhersagen zu ermöglichen. 

## Dependency Management

Für das Dependency Management wird eine requirements.txt-Datei verwendet, die alle benötigten Bibliotheken mit den jeweiligen Versionen auflistet. Dadurch können alle Abhängigkeiten einfach über den Befehl pip install -r requirements.txt installiert werden, um eine reibungslose Ausführung der Anwendung zu gewährleisten. Durch die Verwendung dieser Datei wird sicherstellt, dass alle Entwickler und Benutzer die gleiche Version der benötigten Bibliotheken verwenden, was zur Stabilität und Kompatibilität der Anwendung beiträgt.

## Deployment

Das Deployment erfolgt über GitHub, um den Code zu versionieren und zu verwalten. Die Webanwendung wurde auf Azure bereitgestellt, damit die Vorhersagen über eine Benutzeroberfläche abgerufen werden können. Der Azure Deployment-Prozess umfasst das Hochladen der Anwendung auf Azure, die Bereitstellung der Umgebung und die Integration des Modells in die Web-App.

