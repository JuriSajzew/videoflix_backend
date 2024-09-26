from time import sleep
import os
import subprocess
from videos.models import Video
 
resolutions = ['480', '720', '1080']
BASE_URL_VIDEO = "https://juri-sajzew.developerakademie.org/media/videos"
 
def convert_all_resolutions(source, video_id):
    """
    Converts a video to all defined resolutions.
    """
    sleep(1)
    print(f"Converting video with ID: {video_id}")
    
    video = Video.objects.filter(pk=video_id).first()
    
    # Check if the video object exists
    if video is None:
        print(f"Video mit ID {video_id} wurde nicht gefunden.")
        return
     
    try:
        video_urls = {}
        for resolution in resolutions:
            target = convert_video(source, resolution)
            resolution_key = f'{resolution}p'
            video_urls[resolution_key] = f"{BASE_URL_VIDEO}/{os.path.basename(target)}"
        
        video.video_urls = video_urls
        video.save()
        print(f"Video URLs updated: {video.video_urls}")
        
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        raise

 
def convert_video(source, resolution):
    """
    Konvertiert ein Video in die angegebene Auflösung.
    """
    base_name, ext = os.path.splitext(source)
    target = f"{base_name}_{resolution}p.m3u8"
    
    cmd = ['ffmpeg',
           '-i', source,
           '-s', f'hd{resolution}',
           '-c:v', 'copy',
           '-start_number', '0',
           '-hls_time', '10',
           '-hls_list_size', '0',
           '-f', 'hls', 
           target
        ]
    
    #print(cmd)
    print(f"Executing command: {' '.join(cmd)}")
    try:
        # Execute the command and get the output and error
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Check the return value
        if result.returncode != 0:
            raise RuntimeError(f"ffmpeg failed with return code {result.returncode}")  
        return target
    except Exception as e:
        
        print(f"An error occurred: {e}")
        raise
  