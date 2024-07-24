@echo off
echo Starting Django server...
start /b python manage.py runserver

echo Starting Celery worker...
start /b celery -A videoflix worker --loglevel=info

echo Starting Celery beat...
start /b celery -A videoflix beat --loglevel=info

echo Starting Flower...
start /b celery -A videoflix flower --port=5555

echo Opening Flower in browser...
start "" "http://localhost:5555"

pause