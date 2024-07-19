import subprocess

def convert_480p(source):
    target = source.replace(".mp4", "_480p.mp4")
    cmd = 'ffmpeg -i "{}" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd)
    return target


def create_thumbnail(source):
    target = source.replace(".mp4", "_thumbnail.jpg")
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -vframes 1 "{}"'.format(source, target)
    subprocess.run(cmd)
    return target
