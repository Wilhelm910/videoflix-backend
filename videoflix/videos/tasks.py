import subprocess

def convert_480p(source):
    target = source.replace(".mp4", "_480p.mp4")
    source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
    target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linx, target_linx)
    subprocess.run(cmd,capture_output=True, shell=True)
    return target

def convert_720p(source):
    target = source.replace(".mp4", "_720p.mp4")
    source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
    target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
    cmd = 'ffmpeg -i "{}" -s hd720 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source_linx, target_linx)
    subprocess.run(cmd,capture_output=True, shell=True)
    return target


def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
    source_linx = "/mnt/" + source.replace("\\", "/").replace("C:", "c")
    target_linx = "/mnt/" + target.replace("\\", "/").replace("C:", "c")
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source_linx, target_linx)
    subprocess.run(cmd,capture_output=True, shell=True)
    return target
