

import subprocess


#def windows_to_wsl_path(windows_path):
#    """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
#    return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

def convert_480p(source):
    target = source.replace(".mp4", "_480p.mp4")
#    source_linux = windows_to_wsl_path(source)
#    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)    
#    subprocess.run(cmd, capture_output=True, shell=True)
    result = subprocess.run(cmd, capture_output=True, shell=True)
    print(result.stdout.decode())  # Ausgabe von ffmpeg
    print(result.stderr.decode())   # Fehler von ffmpeg    




def convert_720p(source):
    target = source.replace(".mp4", "_720p.mp4")
#    source_linux = windows_to_wsl_path(source)
#    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)    
#    subprocess.run(cmd, capture_output=True, shell=True)
    result = subprocess.run(cmd, capture_output=True, shell=True)
    print(result.stdout.decode())  # Ausgabe von ffmpeg
    print(result.stderr.decode())   # Fehler von ffmpeg


def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
#    source_linux = windows_to_wsl_path(source)
#    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source, target)
#    subprocess.run(cmd, capture_output=True, shell=True)    
    result = subprocess.run(cmd, capture_output=True, shell=True)
    print(result.stdout.decode())  # Ausgabe von ffmpeg
    print(result.stderr.decode())   # Fehler von ffmpeg


##############################
#import subprocess
#import os
#
#
#def convert_480p(source):
#    # Zielpfad für die 480p-Version
#    target = source.replace(".mp4", "_480p.mp4")
#    
#    # FFMPEG-Befehl für die Umwandlung
#    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#    
#    # Führe den Befehl aus und protokolliere mögliche Fehler
#    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    
#    if result.returncode != 0:
#        print(f"Fehler bei der Umwandlung in 480p: {result.stderr.decode()}")
#    else:
#        print(f"480p-Umwandlung erfolgreich: {target}")
#
#
#def convert_720p(source):
#    # Zielpfad für die 720p-Version
#    target = source.replace(".mp4", "_720p.mp4")
#    
#    # FFMPEG-Befehl für die Umwandlung
#    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#    
#    # Führe den Befehl aus und protokolliere mögliche Fehler
#    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    
#    if result.returncode != 0:
#        print(f"Fehler bei der Umwandlung in 720p: {result.stderr.decode()}")
#    else:
#        print(f"720p-Umwandlung erfolgreich: {target}")
#
#
#def create_thumbnail(source):
#    # Zielpfad für das Thumbnail
#    target = source.replace(".mp4", "_thumbnail.jpg")
#    
#    # FFMPEG-Befehl zur Erstellung eines Thumbnails
#    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source, target)
#    
#    # Führe den Befehl aus und protokolliere mögliche Fehler
#    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    
#    if result.returncode != 0:
#        print(f"Fehler bei der Erstellung des Thumbnails: {result.stderr.decode()}")
#    else:
#        print(f"Thumbnail erfolgreich erstellt: {target}")

