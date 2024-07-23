import os
import subprocess

resolutions = ['480', '720', '1080']

def convert_video(source, resolution):
    # Extrahiere den Basisnamen und die Erweiterung des Quelldateipfads
    base_name, ext = os.path.splitext(source)
    # Erzeuge den Zielpfad, indem du '_{resolution}p.mp4' an den Basisnamen anhängst
    target = f"{base_name}_{resolution}p.mp4"
    # ffmpeg-Befehl zum Konvertieren des Videos
    cmd = f'ffmpeg -i "{source}" -s hd{resolution} -c:v libx264 -crf 23 -c:a aac -strict -2 "{target}"'
    # Führe den ffmpeg-Befehl aus
    subprocess.run(cmd, shell=True)
    
def convert_all_resolutions(source):
    for resolution in resolutions:
        convert_video(source, resolution)