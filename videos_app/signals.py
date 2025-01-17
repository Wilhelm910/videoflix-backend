from videos_app.tasks import convert_120p,convert_720p, create_thumbnail
from .models import Thumbnail, Video, Video120p, Video360p, Video720p
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
        queue.enqueue("videos_app.tasks.convert_720p", instance.video_file.path)
        queue.enqueue("videos_app.tasks.convert_360p", instance.video_file.path)
        queue.enqueue("videos_app.tasks.convert_120p", instance.video_file.path)
        queue.enqueue("videos_app.tasks.create_thumbnail", instance.video_file.path)
               
        # Relative Pfade erstellen
        video_120p_path = instance.video_file.name.replace(".mp4", "_120p.mp4")
        video_360p_path = instance.video_file.name.replace(".mp4", "_360p.mp4")
        video_720p_path = instance.video_file.name.replace(".mp4", "_720p.mp4")
        thumbnail_path = instance.video_file.name.replace(".mp4", "_thumbnail.jpg")
        
        # Datenbankeinträge für die konvertierten Videos erstellen
        video_120p_instance = Video120p(video=instance, video_file_120p=video_120p_path)
        video_120p_instance.save()
        
        video_360p_instance = Video360p(video=instance, video_file_360p=video_360p_path)
        video_360p_instance.save()

        video_720p_instance = Video720p(video=instance, video_file_720p=video_720p_path)
        video_720p_instance.save()
        
        # Thumbnail setzen
        instance.thumbnail = thumbnail_path
        
        # Verknüpfung der Videoqualitäten mit dem Hauptvideo
        instance.video_120p = video_120p_instance
        instance.video_360p = video_360p_instance
        instance.video_720p = video_720p_instance
        instance.save()


# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print("Video wurde gespeichert")
#     if created:
#         print("Video wurde erstellt")
#         queue = django_rq.get_queue('default', autocommit=True)
#         queue.enqueue("videos_app.tasks.convert_720p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.convert_360p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.convert_120p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.create_thumbnail", instance.video_file.path)
               
#        # Datenbankeinträge für die konvertierten Videos erstellen
#         video_120p_instance = Video120p(video=instance)
#         video_120p_instance.video_file_120p = instance.video_file.path.replace(".mp4", "_120p.mp4")
#         video_120p_instance.save()
        
#         video_360p_instance = Video360p(video=instance)
#         video_360p_instance.video_file_360p = instance.video_file.path.replace(".mp4", "_360p.mp4")
#         video_360p_instance.save()

#         video_720p_instance = Video720p(video=instance)
#         video_720p_instance.video_file_720p = instance.video_file.path.replace(".mp4", "_720p.mp4")
#         video_720p_instance.save()
        
#         thumbnail_path = instance.video_file.path.replace(".mp4", "_thumbnail.jpg")
#        # thumbnail_path = os.path.join('thumbnails', os.path.basename(instance.video_file.path).replace(".mp4", "_thumbnail.jpg"))
#         #thumbnail_path = os.path.join('thumbnails', os.path.basename(instance.video_file.path).replace(".mp4", "_thumbnail.jpg"))

        
#         instance.video_120p = video_120p_instance
#         instance.video_360p = video_360p_instance
#         instance.video_720p = video_720p_instance
#         instance.thumbnail = thumbnail_path
#         #instance.thumbnail.name = thumbnail_path
#         instance.save()

# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print("Video wurde gespeichert")
#     if created:
#         print("Video wurde erstellt")
        
#         # Stelle sicher, dass der Thumbnail-Pfad korrekt gesetzt ist
#         thumbnail_path = os.path.join('thumbnails', os.path.basename(instance.video_file.path).replace(".mp4", "_thumbnail.jpg"))
        
#         # Stelle sicher, dass das Thumbnail korrekt gespeichert wird
#         instance.thumbnail.name = thumbnail_path
        
#         # Weitere Queue-Operationen
#         queue = django_rq.get_queue('default', autocommit=True)
#         queue.enqueue("videos_app.tasks.convert_720p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.convert_360p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.convert_120p", instance.video_file.path)
#         queue.enqueue("videos_app.tasks.create_thumbnail", instance.video_file.path)
        
#         # Weitere Datenbankeinträge für die konvertierten Videos
#         video_120p_instance = Video120p(video=instance)
#         video_120p_instance.video_file_120p = instance.video_file.path.replace(".mp4", "_120p.mp4")
#         video_120p_instance.save()
        
#         video_360p_instance = Video360p(video=instance)
#         video_360p_instance.video_file_360p = instance.video_file.path.replace(".mp4", "_360p.mp4")
#         video_360p_instance.save()

#         video_720p_instance = Video720p(video=instance)
#         video_720p_instance.video_file_720p = instance.video_file.path.replace(".mp4", "_720p.mp4")
#         video_720p_instance.save()

#         # Speichern Sie die Konvertierung und das Thumbnail
#         instance.video_120p = video_120p_instance
#         instance.video_360p = video_360p_instance
#         instance.video_720p = video_720p_instance
#         instance.save()



# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print('Video wurde gespeichert')
#     if created:
#         print('Video erstellt', sender, instance)
#         convert_120p(instance.video_file.path)
#         video_120p_instance = Video120p(video=instance)
#         #instance.video_120p = video_120p_instance
#         video_120p_instance.video_file_120p = instance.video_file.path.replace(".mp4", "_120p.mp4")
#         video_120p_instance.save()
        
#         convert_720p(instance.video_file.path)
#         video_720p_instance = Video720p(video=instance)
#         #instance.video_720p = video_720p_instance
#         video_720p_instance.video_file_720p = instance.video_file.path.replace(".mp4", "_720p.mp4")
#         video_720p_instance.save()
        
#         create_thumbnail(instance.video_file.path)
#         thumbnail_instance = Thumbnail(video=instance)
#         #instance.thumbnail = thumbnail_instance
#         thumbnail_instance = instance.video_file.path.replace(".mp4", "_thumbnail.jpg")
#         thumbnail_instance.save()

# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print('Video wurde gespeichert')
#     if created:
#         print('Video erstellt', sender, instance)
        
#         # Konvertierung zu 120p
#         path_120p = convert_120p(instance.video_file.path)
#         video_120p_instance = Video120p(video=instance, video_file_120p=path_120p)
#         video_120p_instance.save()
#         print(f'120p Video gespeichert: {path_120p}')
        
#         # Konvertierung zu 720p
#         path_720p = convert_720p(instance.video_file.path)
#         video_720p_instance = Video720p(video=instance, video_file_720p=path_720p)
#         video_720p_instance.save()
#         print(f'720p Video gespeichert: {path_720p}')
        
#         # Thumbnail-Erstellung
#         thumbnail_path = create_thumbnail(instance.video_file.path)
#         thumbnail_instance = Thumbnail(video=instance, thumbnail_file=thumbnail_path)
#         thumbnail_instance.save()
#         print(f'Thumbnail gespeichert: {thumbnail_path}')

#         # Aktualisierung des Video-Objekts, um den Thumbnail-Pfad zu setzen
#         instance.thumbnail = thumbnail_instance
#         instance.save()
#         print(f'Video-Thumbnail aktualisiert: {instance.thumbnail}')

   
# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print('Video wurde gespeichert')
#     if created:
#         print('Video erstellt', sender, instance)
        
#         # Konvertierung zu 120p
#         path_120p = convert_120p(instance.video_file.path)
#         video_120p_instance = Video120p(video=instance, video_file_120p=path_120p)
#         video_120p_instance.save()
        
#         # Konvertierung zu 720p
#         path_720p = convert_720p(instance.video_file.path)
#         video_720p_instance = Video720p(video=instance, video_file_720p=path_720p)
#         video_720p_instance.save()
        
#         # Thumbnail-Erstellung
#         thumbnail_path = create_thumbnail(instance.video_file.path)
#         instance.thumbnail.name = thumbnail_path  # Speichern des Pfads im `thumbnail`-Feld des Videos
#         instance.save()  # Das Video mit dem aktualisierten Thumbnail speichern
     


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
            

