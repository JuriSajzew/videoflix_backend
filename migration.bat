@echo off
cd /d "C:\developer\Videoflix\videoflix_backend"
python manage.py makemigrations
python manage.py migrate
pause