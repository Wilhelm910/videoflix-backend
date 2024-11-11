#from videos.tasks import convert_480p, create_thumbnail
#from .models import Video, Video480p, Video720p
#from django.dispatch import receiver
#from django.db.models.signals import post_save, post_delete
#import os
#import django_rq
#from django.conf import settings
#import django_rq



#@receiver(post_save, sender=Video)
#def video_post_save(sender, instance, created, **kwargs):
#    print("Video wurde gespeichert")
#    if created:
#        print("Video wurde erstellt")
#        queue = django_rq.get_queue('default', autocommit=True)
#        queue.enqueue(convert_480p, instance.video_file.path)
#        queue.enqueue("videos.tasks.convert_720p", instance.video_file.path)
#        queue.enqueue("videos.tasks.create_thumbnail", instance.video_file.path)
               
       # Datenbankeinträge für die konvertierten Videos erstellen
#        video_480p_instance = Video480p(video=instance)
#        video_480p_instance.video_file_480p = instance.video_file.path.replace(".mp4", "_480p.mp4")
#        video_480p_instance.save()

#        video_720p_instance = Video720p(video=instance)
#        video_720p_instance.video_file_720p = instance.video_file.path.replace(".mp4", "_720p.mp4")
#        video_720p_instance.save()
        
#        thumbnail_path = instance.video_file.path.replace(".mp4", "_thumbnail.jpg")
        
#        instance.video_480p = video_480p_instance
#        instance.video_720p = video_720p_instance
#        instance.thumbnail = thumbnail_path
#        instance.save()


#@receiver(post_delete, sender=Video)
#def auto_delete_file_on_delete(sender, instance, **kwargs):
#    """
#    Deletes file from filesystem
#    when corresponding `Video` object is deleted.
#    """
#    if instance.video_file:
#        if os.path.isfile(instance.video_file.path):
#            os.remove(instance.video_file.path)
            

#############################################

from videos.tasks import convert_480p, create_thumbnail
from .models import Video, Video480p, Video720p
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import os
import django_rq
from django.conf import settings


@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    print("Video wurde gespeichert")
    if created:
        print("Video wurde erstellt")
        queue = django_rq.get_queue('default', autocommit=True)
        
        # Konvertierungen in die Queue einfügen
#        queue.enqueue(convert_480p, instance.video_file.name)  # Nur Name, nicht der absolute Pfad
#        queue.enqueue("videos.tasks.convert_720p", instance.video_file.name)
#        queue.enqueue("videos.tasks.create_thumbnail", instance.video_file.name)
        queue.enqueue(convert_480p, os.path.join(settings.MEDIA_ROOT, instance.video_file.name))  # Absoluter Pfad
        queue.enqueue("videos.tasks.convert_720p", os.path.join(settings.MEDIA_ROOT, instance.video_file.name))
        queue.enqueue("videos.tasks.create_thumbnail", os.path.join(settings.MEDIA_ROOT, instance.video_file.name))



        
        # Datenbankeinträge für die konvertierten Videos erstellen
        # Relative Pfade erstellen
 #       relative_480p_path = os.path.join("videos", instance.video_file.name.replace(".mp4", "_480p.mp4"))
 #       relative_720p_path = os.path.join("videos", instance.video_file.name.replace(".mp4", "_720p.mp4"))
 #       relative_thumbnail_path = os.path.join("thumbnails", instance.video_file.name.replace(".mp4", "_thumbnail.jpg"))
 # Relative Pfade für konvertierte Videos und Thumbnail im Ordner "videos" speichern
        relative_480p_path = instance.video_file.name.replace(".mp4", "_480p.mp4")
        relative_720p_path = instance.video_file.name.replace(".mp4", "_720p.mp4")
        relative_thumbnail_path = instance.video_file.name.replace(".mp4", "_thumbnail.jpg")  



      
        # Video480p und Video720p Instanzen mit relativen Pfaden speichern
        video_480p_instance = Video480p(video=instance, video_file_480p=relative_480p_path)
        video_480p_instance.save()
        
        video_720p_instance = Video720p(video=instance, video_file_720p=relative_720p_path)
        video_720p_instance.save()

        # Haupt-Video-Instanz aktualisieren mit Thumbnail-Pfad
        instance.thumbnail = relative_thumbnail_path
        instance.save()


@receiver(post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Löscht Dateien vom Dateisystem, wenn das zugehörige `Video`-Objekt gelöscht wird.
    """
    if instance.video_file:
        video_path = os.path.join(settings.MEDIA_ROOT, instance.video_file.name)
        if os.path.isfile(video_path):
            os.remove(video_path)

