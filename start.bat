@echo off
echo Activating virtual environment...
call env\Scripts\activate.bat

:: Warten, um sicherzustellen, dass die Umgebung aktiviert ist
timeout /t 2 /nobreak >nul

echo Starting Django server...
start /b python manage.py runserver

:: Warten, bis der Server gestartet ist
timeout /t 10 /nobreak >nul

echo Starting Django RQ worker...
start /b python manage.py rqworker --worker-class=videos.simpleworker.SimpleWorker default

:: Warten, bis der Worker gestartet ist
timeout /t 10 /nobreak >nul

echo Starting Django RQ scheduler...
start /b python manage.py rqscheduler

:: Warten, bis der Scheduler gestartet ist
timeout /t 10 /nobreak >nul

echo Opening Django admin interface for monitoring...
start "" "http://127.0.0.1:8000/django-rq/"

:: Warten, bevor die nächste Seite geöffnet wird
timeout /t 5 /nobreak >nul

echo Opening Django admin interface...
start "" "http://127.0.0.1:8000/admin/"

pause