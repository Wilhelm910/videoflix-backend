from videos_app.tasks import convert_480p, create_thumbnail
from .models import Video, Video480p, Video720p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
import django_rq
from django.conf import settings
import django_rq



@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("Video wurde erstellt")
        queue = django_rq.get_queue('default', autocommit=True)
        queue.enqueue(convert_480p, instance.video_file.path)
        queue.enqueue("videos.tasks.convert_720p", instance.video_file.path)
        queue.enqueue("videos.tasks.create_thumbnail", instance.video_file.path)
               
       # Datenbankeinträge für die konvertierten Videos erstellen
        video_480p_instance = Video480p(video=instance)
        video_480p_instance.video_file_480p = instance.video_file.path.replace(".mp4", "_480p.mp4")
        video_480p_instance.save()

        video_720p_instance = Video720p(video=instance)
        video_720p_instance.video_file_720p = instance.video_file.path.replace(".mp4", "_720p.mp4")
        video_720p_instance.save()
        
        thumbnail_path = instance.video_file.path.replace(".mp4", "_thumbnail.jpg")
        
        instance.video_480p = video_480p_instance
        instance.video_720p = video_720p_instance
        instance.thumbnail = thumbnail_path
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
            

