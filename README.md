# Videoflix Backend

## Contents
1. [Description](#description)
2. [Functions](#functions)
3. [Technology stack](#technology-stack)
4. [Installation](#installation)
    * [Prerequisites](#prerequisites)
    * [Project setup](#project-setup)
    * [environment configuration](#environment-configuration)
    * [Database setup](#database-setup)
5. [API documentation](#api-documentation)
6. [Frontend](#frontend)
7. [Author](#author)
8. [Licence](#licence)

## Description
Videoflix is the backend of a video platform that was developed as a learning project to gain practical experience with Django and the Django Rest Framework (DRF). This repository includes the database and the REST API, which serves as the interface for all frontend requests. The frontend, developed with Angular, is available in a separate repository and can be viewed publicly on my [GitHub profile](https://github.com/JuriSajzew).

## Functions
* **Video upload** : Allows you to upload and manage videos.
* **User management and authentication** : User account management, login and access control.
* **REST API for video platform** : Provision of CRUD operations (Create, Read, Update, Delete) for the video database.
* **Database integration** : PostgreSQL as primary database management system.

## Technology stack
* **Python** : Programming language
* **Django** : Web framework for fast backend development
* **Django Rest Framework (DRF)** : Framework for creating RESTful APIs
* **PostgreSQL** : database management system
* **psycopg2** : PostgreSQL adapter for Python
* **python-dotenv** : Managing environment variables

## Installation
### Prerequisites
Before you start, make sure that the following applications are installed:
* **Python (version 3.x)** : [Download Python](https://www.python.org/downloads/)
* **PostgreSQL** : [Download PostgreSQL](https://www.postgresql.org/download/)
* **pip** : Normally pre-installed with Python, for installation of additional Python packages.
* **Git** (optional, but recommended): [Download Git](https://git-scm.com/downloads)

### Project setup
1. `Clone repository`: Clone this repository to your local directory.
```bash
git clone https://github.com/JuriSajzew/videoflix_backend.git
cd videoflix_backend
```
2. `Create a virtual environment`: Create a virtual environment and activate it.
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate  # Für Windows
```

3. `Install dependencies`: Install the required Python packages.
```bash
pip install -r requirements.txt
```

### environment configuration
To configure environment variables, we create an .env file in the root directory of the project.
1. `Create **.env file**`: Create an `.env` file in the root directory of the project and add the following variables:
```plaintext
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_NAME=videoflix_db
    DATABASE_USER=your_database_user
    DATABASE_PASSWORD=your_database_passwort
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
```

* **SECRET_KEY** : A secret key for Django. You can generate a random key by using the Django admin tool.
* **DATABASE_NAME** : Name of the database (e.g. videoflix_db).
* **DATABASE_USER und DATABASE_PASSWORD** : Access data for your PostgreSQL database.
* **DATABASE_HOST und DATABASE_PORT** : Normally localhost and 5432 for a local PostgreSQL instance.


2. **Integrate python-dotenv** : The python-dotenv package ensures that Django loads all variables from the .env file at startup. This package is already included in requirements.txt.

### Database setup
1. **Create PostgreSQL database** : Start PostgreSQL and create a new database (e.g. videoflix_db).
```sql
CREATE DATABASE videoflix_db;
CREATE USER dein_datenbank_benutzer WITH PASSWORD 'dein_datenbank_passwort';
ALTER ROLE dein_datenbank_benutzer SET client_encoding TO 'utf8';
ALTER ROLE dein_datenbank_benutzer SET default_transaction_isolation TO 'read committed';
ALTER ROLE dein_datenbank_benutzer SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE videoflix_db TO dein_datenbank_benutzer;
```
2. Migrate the database tables: Migrate the database to create the table structures.
```bash
python manage.py migrate
```

3. **Create superuser** : If desired, you can create a superuser for the admin interface.
```bash
python manage.py createsuperuser
```
4. **Start server** : Start the development server.
```bash
python manage.py runserver
```
The server is now running under `http://localhost:8000`.

## API documentation
This backend offers several endpoints to provide the functions of the video platform. Here is an overview of the available API endpoints:

### End points

| Path                                   | Description                                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------|
| `admin/`                               | Access to the Django admin panel                                                             |
| `check_email/`                         | Checks if an email address is already registered                                       |
| `login/`                               | User login endpoint                                                                         |
| `api/videos/`                          | Enables CRUD operations on videos                                                          |
| `videos/<video_name>/<resolution>/`    | Displays a video in the specified resolution                                                 |
| `django-rq/`                           | Management of background tasks via Django RQQ                                               |
| `password_reset/`                      | Starts the password reset via email                                                   |
| `password_reset/confirm/`              | Confirms the password reset (customised view)                                       |
| `register/`                            | Registration of a new user                                                             |
| `verify-email/`                        | Sends a verification email to new users                                              |


## Frontend
The corresponding frontend project is separate and was developed with Angular. You can find it here on my [Videoflix_Frontend](github.comJuriSajzew/videoflix_frontend).

## Author
Juri Sajzew
[GitHub-Profil](https://github.com/JuriSajzew)

## Licence
This project is licensed under the MIT licence see the [LICENSE](licence) file for more details.
