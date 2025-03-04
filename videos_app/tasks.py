import subprocess  

# Function to convert a Windows file path to a WSL-compatible Linux file path.
def windows_to_wsl_path(windows_path):
    # Open the log file in append mode with line buffering to log a message.
    with open("output_log.txt", "a", buffering=1) as log_file:
        log_file.write("Log-Nachricht\n")
        log_file.flush()  # Ensure the log is written immediately.
    print("Test output", flush=True)  # Print test output to the console with immediate flushing.
    
    # Append the Windows path to the log file.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"windows path: {windows_path}")
    
    """Converts a Windows path to a WSL-compatible path.
    It replaces backslashes with forward slashes and converts the drive letter.
    For example, 'C:\\path\\to\\file' becomes '/mnt/c/path/to/file'."""
    return windows_path.replace("\\", "/").replace("C:", "/mnt/c")

# Function to execute a shell command and log any errors.
def execute_command(cmd):
    """Executes a shell command and logs errors if they occur."""
    # Run the command in the shell, capturing both output and errors.
    result = subprocess.run(cmd, capture_output=True, shell=True)
    if result.returncode != 0:
        # If the command fails (non-zero exit code), log the error message.
        with open("output_log.txt", "a") as log_file:
            log_file.write(f"Error executing: {cmd}\n{result.stderr.decode('utf-8')}\n")
        print(result.stderr.decode('utf-8'))  # Also print the error to the console.
    else:
        # Log successful command execution.
        with open("output_log.txt", "a") as log_file:
            log_file.write(f"Successfully executed: {cmd}\n")
        print(result.stdout.decode('utf-8'))  # Print the command's output to the console.
    return result.returncode == 0  # Return True if the command succeeded.

# Function to convert a video to 360p resolution.
def convert_360p(source):
    print(f"Startet converting 360p for {source}")
    # Log the start of the 360p conversion process.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 360p for {source}\n")
    # Define the target filename by appending '_360p' before the extension.
    target = source.replace(".mp4", "_360p.mp4")
    # Log the conversion details.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 360p: {source} -> {target}\n")
    # Convert Windows paths to WSL-compatible paths.
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    # Construct the ffmpeg command to convert the video to 360p resolution.
    cmd = f'ffmpeg -i "{source_linux}" -s 640x360 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

# Function to convert a video to 480p resolution.
def convert_480p(source):
    print(f"Startet converting 480p for {source}")
    # Log the start of the 480p conversion process.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 480p for {source}\n")
    # Define the target filename by appending '_480p' before the extension.
    target = source.replace(".mp4", "_480p.mp4")
    # Log the conversion details.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 480p: {source} -> {target}\n")
    # Convert Windows paths to WSL-compatible paths.
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    # Construct the ffmpeg command using the 'hd480' preset for 480p conversion.
    cmd = f'ffmpeg -i "{source_linux}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

# Function to convert a video to 720p resolution.
def convert_720p(source):
    print(f"Startet converting 720p for {source}")
    # Log the start of the 720p conversion process.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 720p for {source}\n")
    # Define the target filename by appending '_720p' before the extension.
    target = source.replace(".mp4", "_720p.mp4")
    # Log the conversion details.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 720p: {source} -> {target}\n")
    # Convert Windows paths to WSL-compatible paths.
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    # Construct the ffmpeg command using the 'hd720' preset for 720p conversion.
    cmd = f'ffmpeg -i "{source_linux}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

# Function to convert a video to 1080p resolution.
def convert_1080p(source):
    print(f"Startet converting 1080p for {source}")
    # Log the start of the 1080p conversion process.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"startet converting 1080p for {source}\n")
    # Define the target filename by appending '_1080p' before the extension.
    target = source.replace(".mp4", "_1080p.mp4")
    # Log the conversion details.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Converting to 1080p: {source} -> {target}\n")
    # Convert Windows paths to WSL-compatible paths.
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    # Construct the ffmpeg command using the 'hd1080' preset for 1080p conversion.
    cmd = f'ffmpeg -i "{source_linux}" -s hd1080 -c:v libx264 -crf 23 -c:a aac -strict -2 "{target_linux}"'
    execute_command(cmd)

# Function to create a thumbnail image from a video.
def create_thumbnail(source):
    # Define the target thumbnail filename by replacing the extension with '_thumbnail.jpg'.
    target = source.replace(".mp4", "_thumbnail.jpg")
    # Log the thumbnail creation process.
    with open("output_log.txt", "a") as log_file:
        log_file.write(f"Creating thumbnail: {source} -> {target}\n")
    # Convert Windows paths to WSL-compatible paths.
    source_linux = windows_to_wsl_path(source)
    target_linux = windows_to_wsl_path(target)
    # Construct the ffmpeg command to extract a single frame at 1 second into the video.
    cmd = f'ffmpeg -i "{source_linux}" -ss 00:00:01.000 -vframes 1 "{target_linux}"'
    execute_command(cmd)
