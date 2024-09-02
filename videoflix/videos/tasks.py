# # import subprocess
# # import os

# # def convert_480p(source):
# #     target = source.replace(".mp4", "_480p.mp4")
# #     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
# #     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
# #     cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linx, target_linx)
# #     result = subprocess.run(cmd, capture_output=True, shell=True)

# #     if result.returncode != 0:
# #         raise RuntimeError(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
# #     else:
# #         print(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
# #     return target

# # def convert_720p(source):
# #     target = source.replace(".mp4", "_720p.mp4")
# #     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
# #     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
# #     cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linx, target_linx)
# #     result = subprocess.run(cmd, capture_output=True, shell=True)

# #     if result.returncode != 0:
# #         raise RuntimeError(f"Failed to convert video to 720p: {result.stderr.decode('utf-8')}")
# #     else:
# #         print(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
# #     return target


# # def create_thumbnail(source):
# #     target = source.replace(".mp4", "_thumbnail.jpg")
# #     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
# #     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
# #     cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source_linx, target_linx)
# #     result = subprocess.run(cmd, capture_output=True, shell=True)

# #     if result.returncode != 0:
# #         raise RuntimeError(f"Failed to create thumbnail: {result.stderr.decode('utf-8')}")
# #     else:
# #         print(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
# #     return target

# import subprocess
# import logging
# import os

# # Verzeichnis für die Logs
# log_directory = 'C:\\Users\\Wilhelm\\Desktop\\Python\\videoflix-backend\\logs'

# # Erstelle das Verzeichnis, wenn es nicht existiert
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)

# # Pfad zur Log-Datei
# log_file_path = os.path.join(log_directory, 'app.log')

# # Logging-Konfiguration
# logging.basicConfig(
#     level=logging.INFO,
#     filename=log_file_path,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def convert_480p(source):
#     target = source.replace(".mp4", "_480p.mp4")
#     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
#     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
#     cmd = f'ffmpeg -i "{source_linx}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linx}"'
    
#     result = subprocess.run(cmd, capture_output=True, shell=True)
    
#     if result.returncode != 0:
#         logging.error(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#         raise RuntimeError(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#     else:
#         logging.info(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
    
#     return target

# def convert_720p(source):
#     target = source.replace(".mp4", "_720p.mp4")
#     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
#     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
#     cmd = f'ffmpeg -i "{source_linx}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linx}"'
    
#     # Speichern der Ausgabe in einer Datei
#     with open('/tmp/ffmpeg_output_720p.txt', 'w') as f:
#         result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

#     if result.returncode != 0:
#         logging.error(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#         raise RuntimeError(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#     else:
#         logging.info(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
    
#     return target

# def create_thumbnail(source):
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
#     target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
#     cmd = f'ffmpeg -i "{source_linx}" -ss 00:00:01.000 -vframes 1 "{target_linx}"'
    
#     # Speichern der Ausgabe in einer Datei
#     with open('/tmp/ffmpeg_output_thumbnail.txt', 'w') as f:
#         result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

#     if result.returncode != 0:
#         logging.error(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#         raise RuntimeError(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#     else:
#         logging.info(f"FFmpeg Ausgabe: {result.stdout.decode('utf-8')}")
    
#     return target
##########################################################################################################

# import subprocess
# import logging
# import os

# # Verzeichnis für die Logs
# log_directory = 'C:\\Users\\Wilhelm\\Desktop\\Python\\videoflix-backend\\logs'

# # Erstelle das Verzeichnis, wenn es nicht existiert
# if not os.path.exists(log_directory):
#     os.makedirs(log_directory)

# # Pfad zur Log-Datei
# log_file_path = os.path.join(log_directory, 'app.log')

# # Logging-Konfiguration
# logging.basicConfig(
#     level=logging.INFO,
#     filename=log_file_path,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# def windows_to_wsl_path(windows_path):
#     """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
#     return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

# def convert_480p(source):
#     print("Current PATH:", os.getenv('PATH'))
#     target = source.replace(".mp4", "_480p.mp4")
#     source_linx = windows_to_wsl_path(source)
#     target_linx = windows_to_wsl_path(target)
#     cmd = f'ffmpeg -i "{source_linx}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linx}"'
    
#     result = subprocess.run(cmd, capture_output=True, shell=True)
    
#     if result.returncode != 0:
#         logging.error(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#         raise RuntimeError(f"Failed to convert video to 480p: {result.stderr.decode('utf-8')}")
#     else:
#         logging.info(f"FFmpeg Output: {result.stdout.decode('utf-8')}")
    
#     return target

# def convert_720p(source):
#     print("Current PATH:", os.getenv('PATH'))
#     target = source.replace(".mp4", "_720p.mp4")
#     source_linx = windows_to_wsl_path(source)
#     target_linx = windows_to_wsl_path(target)
#     cmd = f'ffmpeg -i "{source_linx}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linx}"'
    
#     # Speichern der Ausgabe in einer Datei
#     with open('/mnt/c/Users/Wilhelm/Desktop/Python/videoflix-backend/logs/ffmpeg_output_720p.txt', 'w') as f:
#         result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

#     if result.returncode != 0:
#         logging.error(f"Failed to convert video to 720p. Check ffmpeg_output_720p.txt for details.")
#         raise RuntimeError(f"Failed to convert video to 720p. Check ffmpeg_output_720p.txt for details.")
#     else:
#         logging.info(f"FFmpeg Output: {result.stdout.decode('utf-8')}")
    
#     return target

# def create_thumbnail(source):
#     print("Current PATH:", os.getenv('PATH'))
#     target = source.replace(".mp4", "_thumbnail.jpg")
#     source_linx = windows_to_wsl_path(source)
#     target_linx = windows_to_wsl_path(target)
#     cmd = f'ffmpeg -i "{source_linx}" -ss 00:00:01.000 -vframes 1 "{target_linx}"'
    
#     # Speichern der Ausgabe in einer Datei
#     with open('/mnt/c/Users/Wilhelm/Desktop/Python/videoflix-backend/logs/ffmpeg_output_thumbnail.txt', 'w') as f:
#         result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.STDOUT)

#     if result.returncode != 0:
#         logging.error(f"Failed to create thumbnail. Check ffmpeg_output_thumbnail.txt for details.")
#         raise RuntimeError(f"Failed to create thumbnail. Check ffmpeg_output_thumbnail.txt for details.")
#     else:
#         logging.info(f"FFmpeg Output: {result.stdout.decode('utf-8')}")
    
#     return target



import subprocess


def windows_to_wsl_path(windows_path):
    """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
    return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

def convert_480p(source):
    target = source.replace(".mp4", "_480p.mp4")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)    
    subprocess.run(cmd, capture_output=True, shell=True)
    
def convert_720p(source):
    target = source.replace(".mp4", "_720p.mp4")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linux, target_linux)    
    subprocess.run(cmd, capture_output=True, shell=True)

def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source_linux, target_linux)
    subprocess.run(cmd, capture_output=True, shell=True)    

#    # Speichere den erstellten Thumbnail-Pfad in der Datenbank
#     video = Video.objects.get(video_file=source)
#     video.thumbnail = target
#     video.save()