# Videoflix Backend
# Videoflix Backend

## Beschreibung
## Beschreibung

**Videoflix** ist das Backend einer Video-Plattform, die als Lernprojekt entwickelt wurde, um tiefere Einblicke in Django und insbesondere in das Django Rest Framework zu erhalten. Dieses Repository enthält die Datenbank und die REST-API, die alle Anfragen des Frontends verarbeitet. Das Frontend wurde mit Angular erstellt und ist separat vom Backend verfügbar. Du findest es öffentlich auf meinem GitHub-Profil.

## Funktionen
## Funktionen

Upload von Videos
Verwaltung von Benutzern und Authentifizierung
API für die Video-Plattform (GET, POST, PUT, DELETE Endpunkte)
PostgreSQL-Datenbankintegration

## Technologie-Stack

* ### Python: Programmiersprache
* ### Django: Web-Framework
* ### Django Rest Framework (DRF): Zum Erstellen von RESTful APIs
* ### PostgreSQL: Datenbank
* ### psycopg2: PostgreSQL-Adapter für Python

## Installation

### Voraussetzungen

Stelle sicher, dass du die folgenden Anwendungen installiert hast:

* Python (Version 3.x)
* Django
* PostgreSQL
* python-dotenv (für Umgebungsvariablen)
* psycopg2 (für die PostgreSQL-Datenbank)

## API-Dokumentation

Die API-Dokumentation ist standardmäßig durch das Django Rest Framework (DRF) bereitgestellt. Sobald der Server läuft, kannst du sie auf http://localhost:8000/api/ einsehen.

## Beispielhafte API-Endpunkte:

* `GET /api/videos/` - Liste aller Videos
* `POST /api/videos/` - Ein neues Video hochladen
* `PUT /api/videos/{id}/` - Ein Video bearbeiten
* `DELETE /api/videos/{id}/` - Ein Video löschen

## Frontend

Das zugehörige Frontend-Projekt ist separat und wurde mit Angular entwickelt. Du findest es hier auf meinem github.comJuriSajzew/videoflix_frontend.

## Autor

Juri Sajzew
GitHub: github.com/JuriSajzew

## Lizenz

Dieses Projekt ist lizenziert unter der MIT-Lizenz - siehe die LICENSE-Datei für weitere Details.
