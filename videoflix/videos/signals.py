from videos.tasks import convert_480p
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
        
        # Berechnung des relativen Pfads
        relative_output_path = os.path.relpath(output_path, settings.MEDIA_ROOT).replace('\\', '/')
        
        Video480p.objects.create(
            video=instance,
            video_file_480p=relative_output_path
        )
        instance.save()
      
        


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Video` object is deleted.
    """
    # if instance.video_file:
    #     if os.path.isfile(instance.video_file.path):
    #         os.remove(instance.video_file.path)
            
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)
    if instance.video_file_480p:
        if os.path.isfile(instance.video_file_480p.path):
            os.remove(instance.video_file_480p.path)