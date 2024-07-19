from videos.tasks import convert_480p, create_thumbnail
from .models import Video, Video480p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
import django_rq
from django.conf import settings

# @receiver(post_save, sender=Video)
# def video_post_save(sender, instance, created, **kwargs):
#     print("Video wurde gespeichert")
#     if created:
#         print("New video created")
#         # queue = django_rq.get_queue("default", autocommit=True)
#         # queue.enqueue(convert_480p, instance.video_file.path)
#         # convert_480p(instance.video_file.path)
#         output_path = convert_480p(instance.video_file.path)
#         instance.video_file_480p.name = output_path.replace(os.path.abspath(os.path.dirname(__file__)), '').replace('\\', '/')
#         instance.save()
   
        
@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("New video created")
        output_path = convert_480p(instance.video_file.path)
        relative_output_path = os.path.relpath(output_path, settings.MEDIA_ROOT).replace('\\', '/')
        
        # Erstelle ein Thumbnail für das Video
        thumbnail_path = create_thumbnail(instance.video_file.path)
        relative_thumbnail_path = os.path.relpath(thumbnail_path, settings.MEDIA_ROOT).replace('\\', '/')
          # Speichere den Thumbnail-Pfad im Video-Objekt
        instance.thumbnail = relative_thumbnail_path
        instance.save()  # Update das Video-Objekt, um das Thumbnail zu speichern
        
        Video480p.objects.create(
            video=instance,
            video_file_480p=relative_output_path
        )
        instance.save()
      
        


# @receiver(post_delete, sender=Video)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `Video` object is deleted.
#     """
#     # if instance.video_file:
#     #     if os.path.isfile(instance.video_file.path):
#     #         os.remove(instance.video_file.path)
            
#     if instance.video_file:
#         if os.path.isfile(instance.video_file.path):
#             os.remove(instance.video_file.path)
#     if instance.video_file_480p:
#         if os.path.isfile(instance.video_file_480p.path):
#             os.remove(instance.video_file_480p.path)

@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes files from the filesystem when the corresponding `Video` object is deleted.
    """
    # Löschen der Video-Datei
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
    
    # Löschen der zugehörigen Video480p-Datei
    try:
        video_480p = Video480p.objects.get(video=instance)
        if video_480p.video_file_480p:
            if os.path.isfile(video_480p.video_file_480p.path):
                os.remove(video_480p.video_file_480p.path)
    except Video480p.DoesNotExist:
        # Video480p existiert nicht, nichts zu tun
        pass