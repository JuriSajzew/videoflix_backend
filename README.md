# Videoflix Backend

## Inhaltsverzeichnis
1. [Beschreibung](#beschreibung)
2. [Funktionen](#funktionen)
3. [Technologie-Stack](#technologie-stack)
4. [Installation](#installation)
    * [Voraussetzungen]()
    * [Projekt-Setup]()
    * [Umgebungskonfiguration]()
    * [Datenbankeinrichtung]()
5. [API-Dokumentation](#api-dokumentation)
6. [Frontend](#frontend)
7. [Autor](#autor)
8. [Lizenz](#lizenz)

## Beschreibung
Videoflix ist das Backend einer Video-Plattform, die als Lernprojekt entwickelt wurde, um praktische Erfahrung mit Django und dem Django Rest Framework (DRF) zu sammeln. Dieses Repository umfasst die Datenbank sowie die REST-API, die als Schnittstelle für alle Anfragen des Frontends dient. Das Frontend, entwickelt mit Angular, ist in einem separaten Repository verfügbar und auf meinem [GitHub-Profil](https://github.com/JuriSajzew) öffentlich einsehbar.

## Funktionen
* Video-Upload: Ermöglicht das Hochladen und Verwalten von Videos.
* Benutzerverwaltung und Authentifizierung: Verwaltung von Benutzerkonten, Anmeldung und Zugriffskontrolle.
* REST API für Video-Plattform: Bereitstellung von CRUD-Operationen (Create, Read, Update, Delete) für die Videodatenbank.
* Datenbankintegration: PostgreSQL als primäres Datenbankmanagementsystem.

## Technologie-Stack
* Python: Programmiersprache
* Django: Web-Framework für schnelles Backend-Entwicklung
* Django Rest Framework (DRF): Framework zur Erstellung von RESTful APIs
* PostgreSQL: Datenbank-Management-System
* psycopg2: PostgreSQL-Adapter für Python
* python-dotenv: Verwalten von Umgebungsvariablen

## Installation
### Voraussetzungen
Bevor du startest, stelle sicher, dass folgende Anwendungen installiert sind:
- **Python** (Version 3.x): Download Python
- **PostgreSQL:** Download PostgreSQL
- **pip:** Normalerweise mit Python vorinstalliert, für die Installation zusätzlicher Python-Pakete.
- **Git** (optional, aber empfohlen): Download Git

## Projekt-Setup
1. Repository klonen: Klone dieses Repository in dein lokales Verzeichnis.
```bash
git clone https://github.com/JuriSajzew/videoflix_backend.git
cd videoflix_backend
```
2. Virtuelle Umgebung erstellen: Erstelle eine virtuelle Umgebung und aktiviere sie.
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate  # Für Windows
```

3. Abhängigkeiten installieren: Installiere die benötigten Python-Pakete.
```bash
pip install -r requirements.txt
```

### Umgebungskonfiguration
Um Umgebungsvariablen zu konfigurieren, erstellen wir eine .env-Datei im Hauptverzeichnis des Projekts.
1. **.env-Datei erstellen**: Erstelle eine `.env`-Datei im Hauptverzeichnis des Projekts und füge die folgenden Variablen ein:
```plaintext
    SECRET_KEY=dein_geheimer_key
    DEBUG=True
    DATABASE_NAME=videoflix_db
    DATABASE_USER=dein_datenbank_benutzer
    DATABASE_PASSWORD=dein_datenbank_passwort
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
```

* **SECRET_KEY** : Ein geheimer Schlüssel für Django. Du kannst einen zufälligen Schlüssel generieren, indem du das Django-Admin-Tool nutzt.
* **DATABASE_NAME** : Name der Datenbank (z.B. videoflix_db).
* **DATABASE_USER und DATABASE_PASSWORD** : Zugangsdaten für deine PostgreSQL-Datenbank.
* **DATABASE_HOST und DATABASE_PORT** : Normalerweise localhost und 5432 für eine lokale PostgreSQL-Instanz.

2. **python-dotenv einbinden** : Das Paket python-dotenv stellt sicher, dass Django beim Start alle Variablen aus der .env-Datei lädt. Dieses Paket ist bereits in requirements.txt enthalten.

##Datenbankeinrichtung

1. **PostgreSQL-Datenbank erstellen** : Starte PostgreSQL und erstelle eine neue Datenbank (z.B. videoflix_db).

```sql
CREATE DATABASE videoflix_db;
CREATE USER dein_datenbank_benutzer WITH PASSWORD 'dein_datenbank_passwort';
ALTER ROLE dein_datenbank_benutzer SET client_encoding TO 'utf8';
ALTER ROLE dein_datenbank_benutzer SET default_transaction_isolation TO 'read committed';
ALTER ROLE dein_datenbank_benutzer SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE videoflix_db TO dein_datenbank_benutzer;
```
2. Migration der Datenbank-Tabellen: Migrate die Datenbank, um die Tabellenstrukturen zu erstellen.
```bash
python manage.py migrate
```

3. **Superuser erstellen** : Falls gewünscht, kannst du einen Superuser für die Admin-Oberfläche erstellen.
```bash
python manage.py createsuperuser
```
4. **Server starten** : Starte den Entwicklungsserver.
```bash
python manage.py runserver
```
Der Server läuft jetzt unter `http://localhost:8000`.



## API-Dokumentation
Dieses Backend bietet mehrere Endpunkte, um die Funktionen der Video-Plattform bereitzustellen. Hier ist eine Übersicht der verfügbaren API-Endpunkte:

### Endpunkte

| Pfad                                   | Beschreibung                                                                                    |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| `admin/`                               | Zugriff auf das Django-Admin-Panel                                                              |
| `check_email/`                         | Überprüft, ob eine E-Mail-Adresse bereits registriert ist                                       |
| `login/`                               | Benutzer-Login-Endpoint                                                                         |
| `api/videos/`                          | Ermöglicht CRUD-Operationen auf Videos                                                          |
| `videos/<video_name>/<resolution>/`    | Zeigt ein Video in der angegebenen Auflösung an                                                 |
| `django-rq/`                           | Verwaltung der Hintergrundaufgaben über Django RQ                                               |
| `password_reset/`                      | Startet die Passwort-Zurücksetzung per E-Mail                                                   |
| `password_reset/confirm/`              | Bestätigt die Passwort-Zurücksetzung (angepasste Ansicht)                                       |
| `register/`                            | Registrierung eines neuen Benutzers                                                             |
| `verify-email/`                        | Sendet eine Verifizierungs-E-Mail an neue Benutzer                                              |


## Frontend
Das zugehörige Frontend-Projekt ist separat und wurde mit Angular entwickelt. Du findest es hier auf meinem github.comJuriSajzew/videoflix_frontend.

## Autor
Juri Sajzew
[GitHub-Profil](https://github.com/JuriSajzew)

## Lizenz
Dieses Projekt ist lizenziert unter der MIT-Lizenz - siehe die LICENSE-Datei für weitere Details.
