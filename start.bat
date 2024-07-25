@echo off
echo Starting Django server...
start /b python manage.py runserver

echo Starting Django RQ worker...
start /b python manage.py rqworker --worker-class=videos.simpleworker.SimpleWorker default

echo Starting Django RQ scheduler...
start /b python manage.py rqscheduler

echo Opening Django admin interface for monitoring...
start "" "http://127.0.0.1:8000/django-rq/"

pause