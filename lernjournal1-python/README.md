# Lernjournal 1 Python

## Repository und Library

[http://danie-helloworld-app.azurewebsites.net](http://danie-helloworld-app.azurewebsites.net)

Die App ermöglicht es, Benutzereingaben in Form von Text zu verarbeiten und eine Antwort zurückzugeben, die den Text umkehrt. Dies ist eine einfache "Hello World"-App, die Flask für das Backend und HTML für das Frontend nutzt.

| Verwendete Library aus PyPi (Name) |
Flask, requests, beautifulsoup4, pandas, scikit-learn, joblib, numpy, gunicorn, pytest, azure |
| --- | --- |
| [Flask](https://pypi.org/project/Flask/3.1.0/) |
| [requests](https://pypi.org/project/requests/2.28.2/) |
| [beautifulsoup4](https://pypi.org/project/beautifulsoup4/4.11.1/) |
| [pandas](https://pypi.org/project/pandas/1.5.3/) |
| [scikit-learn](https://pypi.org/project/scikit-learn/1.2.1/) |
| [joblib](https://pypi.org/project/joblib/1.2.0/) |
| [numpy](https://pypi.org/project/numpy/1.24.2/) |
| [gunicorn](https://pypi.org/project/gunicorn/20.1.1/) |
| [pytest](https://pypi.org/project/pytest/7.2.2/) |
| [azure](https://pypi.org/project/azure/4.7.0/) |

## App, Funktionalität

Die App empfängt Benutzereingaben über ein HTML-Formular und gibt die umgekehrte Version des eingegebenen Textes zurück. Die Eingabe wird auf der gleichen Seite verarbeitet und das Ergebnis wird dem Benutzer angezeigt. Diese einfache Funktionalität ist ein Beispiel für eine Webanwendung, die mit Flask entwickelt wurde.

## Dependency Management

Für das Dependency Management wird eine `requirements.txt`-Datei verwendet, die alle benötigten Bibliotheken auflistet, damit diese einfach über den Befehl `pip install -r requirements.txt` installiert werden können. Dadurch wird sichergestellt, dass die gleiche Version der Bibliotheken von allen Benutzern der App verwendet wird, was die Kompatibilität und Stabilität der Anwendung gewährleistet.

## Deployment

Das Deployment erfolgt über GitHub und Azure. Die App wurde auf Azure bereitgestellt, sodass sie online erreichbar ist. Der Deployment-Prozess umfasst das Hochladen der Anwendung auf Azure, die Bereitstellung der Umgebung und das Testen der Funktionsweise der Anwendung. Die App ist nun live und kann über den bereitgestellten Link aufgerufen werden.
