import os
import subprocess
 
resolutions = ['480', '720', '1080']
 
def convert_all_resolutions(source):
    """
    Konvertiert ein Video in alle definierten Auflösungen.
    """
    
    for resolution in resolutions:
        convert_video(source, resolution)

 
def convert_video(source, resolution):
    """
    Konvertiert ein Video in die angegebene Auflösung.
    """
    base_name, ext = os.path.splitext(source)
    target = f"{base_name}_{resolution}p.m3u8"
    #cmd = ['ffmpeg', '-i', source, '-s', f'hd{resolution}','-c:v', 'libx264','-crf', '23','-c:a', 'aac','-strict', '-2', target]
    cmd = ['ffmpeg', '-i', source, f'hd{resolution}', '-codec:', 'copy', '-start_number', 0, '-hls_time', 10, '-hls_list_size', 0, '-f', 'hls', target]
    
    print(cmd)
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
  