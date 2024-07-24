import os
import subprocess
from celery import shared_task
import logging

#resolutions = ['480', '720', '1080']
#
#@shared_task
#def convert_video(source, resolution):
#    """
#    Konvertiert ein Video in die angegebene Auflösung.
#    """
#    # Extrahiere den Basisnamen und die Erweiterung des Quelldateipfads
#    base_name, ext = os.path.splitext(source)
#    # Erzeuge den Zielpfad, indem du '_{resolution}p.mp4' an den Basisnamen anhängst
#    target = f"{base_name}_{resolution}p.mp4"
#    # ffmpeg-Befehl zum Konvertieren des Videos
#    cmd = f'ffmpeg -i "{source}" -s hd{resolution} -c:v libx264 -crf 23 -c:a aac -strict -2 "{target}"'
#    # Führe den ffmpeg-Befehl aus
#    subprocess.run(cmd, shell=True)
#    return target
 
@shared_task   
def convert_all_resolutions(source):
    """
    Konvertiert ein Video in alle definierten Auflösungen.
    """
    for resolution in resolutions:
        convert_video(source, resolution)
        
# Setze das Logging-Level für deine Anwendung
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

resolutions = ['480', '720', '1080']

@shared_task
def convert_video(source, resolution):
    """
    Konvertiert ein Video in die angegebene Auflösung.
    """
    base_name, ext = os.path.splitext(source)
    target = f"{base_name}_{resolution}p.mp4"
    
    cmd = f'ffmpeg -i "{source}" -s hd{resolution} -c:v libx264 -crf 23 -c:a aac -strict -2 "{target}"'
    
    # Logge den Befehl zur Überprüfung
    logger.info(f"Running command: {cmd}")
    
    # Führe den ffmpeg-Befehl aus und logge die Ausgaben
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(result.stdout.decode())
        logger.error(result.stderr.decode())
    except subprocess.CalledProcessError as e:
        logger.error(f"Error occurred: {e}")
        raise
    
    return target