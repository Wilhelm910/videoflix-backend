from videos_app.tasks import convert_360p, convert_480p, convert_720p, convert_1080p, create_thumbnail
from .models import Thumbnail, Video, Video480p, Video360p, Video720p, Video1080p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
import django_rq
from django.conf import settings
import django_rq

def verify_file_existence(filepath, resolution):
    if not os.path.exists(filepath):
        with open("output_log.txt", "a") as log_file:
            log_file.write(f"{resolution} file not found: {filepath}\n")
        return False
    return True


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("Video wurde erstellt")
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_1080p, instance.video_file.path)
        print("started")
        queue.enqueue(convert_720p, instance.video_file.path)
        queue.enqueue(convert_360p, instance.video_file.path)
        queue.enqueue(convert_480p, instance.video_file.path)
        queue.enqueue(create_thumbnail, instance.video_file.path)
        print(queue)
        print(instance.video_file.path)
        print(convert_480p)
               
        # Relative Pfade erstellen
        video_480p_path = instance.video_file.name.replace(".mp4", "_480p.mp4")
        print(video_480p_path)
        video_360p_path = instance.video_file.name.replace(".mp4", "_360p.mp4")
        print(video_360p_path)
        video_720p_path = instance.video_file.name.replace(".mp4", "_720p.mp4")
        print(video_720p_path)
        video_1080p_path = instance.video_file.name.replace(".mp4", "_1080p.mp4")
        print(video_1080p_path)
        thumbnail_path = instance.video_file.name.replace(".mp4", "_thumbnail.jpg")

        # Datenbankeinträge für die konvertierten Videos erstellen
        video_480p_instance = Video480p(video=instance, video_file_480p=video_480p_path)
        print(video_480p_instance)
        video_480p_instance.save()

        video_360p_instance = Video360p(video=instance, video_file_360p=video_360p_path)
        print(video_360p_instance)
        video_360p_instance.save()

        video_720p_instance = Video720p(video=instance, video_file_720p=video_720p_path)
        print(video_720p_instance)
        video_720p_instance.save()

        video_1080p_instance = Video1080p(video=instance, video_file_1080p=video_1080p_path)
        print(video_1080p_instance)
        video_1080p_instance.save()

        # Thumbnail setzen
        instance.thumbnail = thumbnail_path

        # Verknüpfung der Videoqualitäten mit dem Hauptvideo
        instance.video_480p = video_480p_instance
        instance.video_360p = video_360p_instance
        instance.video_720p = video_720p_instance
        instance.video_1080p = video_1080p_instance
        instance.save()


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
            print("Video wurde gelöscht")
            
            
            
            