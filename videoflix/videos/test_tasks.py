# import os
# from tasks import convert_480p, convert_720p, create_thumbnail

# # Pfad zur Video-Datei
# video_path = 'C:\\Users\\Wilhelm\\Desktop\\Python\\videoflix-backend\\videoflix\\media\\videos\\7064867-uhd_3840_2160_30fps_a3VRafz.mp4'

# # Testen der Funktionen
# try:
#     # Konvertiere Video auf 480p
#     result_480p = convert_480p(video_path)
#     print(f"480p Video erstellt: {result_480p}")
    
#     # Konvertiere Video auf 720p
#     result_720p = convert_720p(video_path)
#     print(f"720p Video erstellt: {result_720p}")
    
#     # Erstelle Thumbnail
#     result_thumbnail = create_thumbnail(video_path)
#     print(f"Thumbnail erstellt: {result_thumbnail}")

# except Exception as e:
#     print(f"Ein Fehler ist aufgetreten: {e}")


import os
from tasks import convert_480p, convert_720p, create_thumbnail

# Pfad zur Video-Datei (im WSL-Format)
video_path = '/mnt/c/Users/Wilhelm/Desktop/Python/videoflix-backend/videoflix/media/videos/7064867-uhd_3840_2160_30fps_a3VRafz.mp4'

# Testen der Funktionen
try:
    # Konvertiere Video auf 480p
    result_480p = convert_480p(video_path)
    print(f"480p Video erstellt: {result_480p}")
    
    # Konvertiere Video auf 720p
    result_720p = convert_720p(video_path)
    print(f"720p Video erstellt: {result_720p}")
    
    # Erstelle Thumbnail
    result_thumbnail = create_thumbnail(video_path)
    print(f"Thumbnail erstellt: {result_thumbnail}")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
