import subprocess

# Deine Funktionen
def windows_to_wsl_path(path):
    # with open("output_log.txt", "a", buffering=1) as log_file:
    #     log_file.write("Log-Nachricht\n")
    #     log_file.flush()  # Force flush after writing
    # print("Test output", flush=True)
    # with open("output_log.txt", "a") as log_file:
    #     log_file.write(f"windows path: {windows_path}")
    # """Konvertiert einen Windows-Pfad in einen WSL-Pfad."""
    # return windows_path.replace("\\", "/").replace("C:", "/mnt/c")
    return path

def execute_command(cmd):
    """Führt einen Shell-Befehl aus und protokolliert Fehler."""
    result = subprocess.run(cmd, capture_output=True, shell=True)
    if result.returncode != 0:
        with open("output_log.txt", "a") as log_file:
            log_file.write(f"Error executing: {cmd}\n{result.stderr.decode('utf-8')}\n")
        print(result.stderr.decode('utf-8'))  # Zeige den Fehler in der Konsole an
    else:
        with open("output_log.txt", "a") as log_file:
            log_file.write(f"Successfully executed: {cmd}\n")
        print(result.stdout.decode('utf-8'))  # Zeige die Ausgabe in der Konsole an
    return result.returncode == 0


def convert_360p(source):
    print(f"Startet converting 360p for {source}")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 360p for {source}\n")
    target = source.replace(".mp4", "_360p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 360p: {source} -> {target}\n")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = f'ffmpeg -i "{source_linux}" -s 640x360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

def convert_480p(source):
    print(f"Startet converting 480p for {source}")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 480p for {source}\n")
    target = source.replace(".mp4", "_480p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 480p: {source} -> {target}\n")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = f'ffmpeg -i "{source_linux}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

def convert_720p(source):
    print(f"Startet converting 720p for {source}")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 720p for {source}\n")
    target = source.replace(".mp4", "_720p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 720p: {source} -> {target}\n")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = f'ffmpeg -i "{source_linux}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

def convert_1080p(source):
    print(f"Startet converting 1080p for {source}")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 1080p for {source}\n")
    target = source.replace(".mp4", "_1080p.mp4")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 1080p: {source} -> {target}\n")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = f'ffmpeg -i "{source_linux}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Creating thumbnail: {source} -> {target}\n")
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
    execute_command(cmd)
