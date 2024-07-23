from django.contrib import admin
from .models import Video, Video480p 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'video_file', "thumbnail", )  # Die Felder, die Sie in der Listenansicht anzeigen möchten
    fields = ('created_at', 'title', 'description', 'video_file',  "categories", "group")  # Die Felder, die im Formular angezeigt werden sollen
    readonly_fields = ('created_at',)  # Falls `created_at` nur lesbar sein soll

class Video480pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_480p')

admin.site.register(Video, VideoAdmin)
admin.site.register(Video480p, Video480pAdmin)
    