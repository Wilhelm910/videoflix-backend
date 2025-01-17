
import subprocess
import os

# Deine Funktionen
def windows_to_wsl_path(windows_path):
    """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
    return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

def convert_120p(source):
    target = source.replace(".mp4", "_120p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 120p: {source} -> {target}\n")
    
    # Weiterer Code für die Konvertierung
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)
    subprocess.run(cmd, capture_output=True, shell=True)


def convert_360p(source):
    target = source.replace(".mp4", "_360p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 360p: {source} -> {target}\n")
    
    # Weiterer Code für die Konvertierung
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)
    subprocess.run(cmd, capture_output=True, shell=True)


def convert_720p(source):
    target = source.replace(".mp4", "_720p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 720p: {source} -> {target}\n")
    
    # Weiterer Code für die Konvertierung
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)
    subprocess.run(cmd, capture_output=True, shell=True)


def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Creating thumbnail: {source} -> {target}\n")
    
    # Weiterer Code für das Erstellen des Thumbnails
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source_linux, target_linux)
    subprocess.run(cmd, capture_output=True, shell=True)
# def create_thumbnail(source):
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     target = target.replace("videos", "thumbnails")  # Ändere das Verzeichnis zu 'thumbnails'
#     with open("output_log.txt", "a") as log_file:
#         log_file.write(f"Creating thumbnail: {source} -> {target}\n")
    
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
#     subprocess.run(cmd, capture_output=True, shell=True)

# def create_thumbnail(source):
#     # Basename des Videos extrahieren
#     base_name = os.path.basename(source).replace(".mp4", "_thumbnail.jpg")
#     # Zielverzeichnis festlegen
#     target = os.path.join("thumbnails", base_name)
#     with open("output_log.txt", "a") as log_file:
#         log_file.write(f"Creating thumbnail: {source} -> {target}\n")

#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(os.path.join("media", target))
#     cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
#     subprocess.run(cmd, capture_output=True, shell=True)

# def create_thumbnail(source):
#     # Extrahiere den Basename ohne Pfad
#     base_name = os.path.basename(source).replace(".mp4", "_thumbnail.jpg")
#     # Setze den Zielpfad im 'thumbnails' Verzeichnis
#     target = os.path.join("media", "thumbnails", base_name)  # Absolute Pfad zur mediendatei
#     with open("output_log.txt", "a") as log_file:
#         log_file.write(f"Creating thumbnail: {source} -> {target}\n")

#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
#     subprocess.run(cmd, capture_output=True, shell=True)


# def create_thumbnail(source):
#     # Der Zielordner für Thumbnails
#     target_dir = os.path.join("media", "thumbnails")
    
#     # Stelle sicher, dass der Zielordner existiert
#     if not os.path.exists(target_dir):
#         os.makedirs(target_dir)
    
#     # Extrahiere den Basename ohne Pfad
#     base_name = os.path.basename(source).replace(".mp4", "_thumbnail.jpg")
    
#     # Setze den Zielpfad im 'thumbnails' Verzeichnis
#     target = os.path.join(target_dir, base_name)
    
#     # Logge die Thumbnail-Erstellung
#     with open("output_log.txt", "a") as log_file:
#         log_file.write(f"Creating thumbnail: {source} -> {target}\n")
    
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
    
#     # Führe den ffmpeg-Befehl aus, um das Thumbnail zu erstellen
#     cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
#     subprocess.run(cmd, capture_output=True, shell=True)
    
#     # Gebe den erstellten Pfad zurück
#     return target





#### for linux:

# import subprocess


# def windows_to_wsl_path(windows_path):
#     """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
#     return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

# def convert_120p(source):
#     target = source.replace(".mp4", "_120p.mp4")
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     print(f"Converting to 120p:\n  Source (Windows): {source}\n  Source (WSL): {source_linux}\n  Target (Windows): {target}\n  Target (WSL): {target_linux}")
#     cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux) 
#     subprocess.run(cmd, capture_output=True, shell=True)

# def convert_360p(source):
#     target = source.replace(".mp4", "_360p.mp4")
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     print(f"Converting to 360p:\n  Source (Windows): {source}\n  Source (WSL): {source_linux}\n  Target (Windows): {target}\n  Target (WSL): {target_linux}")
#     cmd = 'ffmpeg -i "{}" -s hd360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)    
#     subprocess.run(cmd, capture_output=True, shell=True)
    
# def convert_720p(source):
#     target = source.replace(".mp4", "_720p.mp4")
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     print(f"Converting to 720p:\n  Source (Windows): {source}\n  Source (WSL): {source_linux}\n  Target (Windows): {target}\n  Target (WSL): {target_linux}")
#     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)    
#     subprocess.run(cmd, capture_output=True, shell=True)

# def create_thumbnail(source):
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     source_linux = windows_to_wsl_path(source)
#     target_linux = windows_to_wsl_path(target)
#     print(f"Creating thumbnail:\n  Source (Windows): {source}\n  Source (WSL): {source_linux}\n  Target (Windows): {target}\n  Target (WSL): {target_linux}")
#     cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source_linux, target_linux)
#     subprocess.run(cmd, capture_output=True, shell=True)    


##### for windows:

# import subprocess

# def convert_120p(source):
#     target = source.replace(".mp4", "_120p.mp4")
#     cmd = 'ffmpeg -i "{}" -s hd120 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)    
#     subprocess.run(cmd, capture_output=True, shell=True)
    
# def convert_720p(source):
#     target = source.replace(".mp4", "_720p.mp4")
#     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)    
#     subprocess.run(cmd, capture_output=True, shell=True)

# def create_thumbnail(source):
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source, target)
#     subprocess.run(cmd, capture_output=True, shell=True)

# import subprocess

# def convert_120p(source):
#     print("started converting")
#     target = source.replace(".mp4", "_120p.mp4")
#     print(f"Converting {source} to 120p: {target}")
#     cmd = 'ffmpeg -i "{}" -s 120x90 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     try:
#         subprocess.run(cmd, capture_output=True, shell=True, check=True)
#         print(f"120p conversion successful: {target}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during 120p conversion: {e.stderr}")
    
# def convert_720p(source):
#     target = source.replace(".mp4", "_720p.mp4")
#     print(f"Converting {source} to 720p: {target}")
#     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
#     try:
#         subprocess.run(cmd, capture_output=True, shell=True, check=True)
#         print(f"720p conversion successful: {target}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error during 720p conversion: {e.stderr}")

# def create_thumbnail(source):
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     print(f"Creating thumbnail for {source}: {target}")
#     cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source, target)
#     try:
#         subprocess.run(cmd, capture_output=True, shell=True, check=True)
#         print(f"Thumbnail created successfully: {target}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error creating thumbnail: {e.stderr}")

