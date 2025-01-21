from django.contrib import admin
from .models import Video, Video480p, Video360p, Video720p, Video1080p 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'video_file', "thumbnail", )  # Die Felder, die Sie in der Listenansicht anzeigen möchten
    fields = ('created_at', 'title', 'description', 'video_file',  "categories", "group", "favourite")  # Die Felder, die im Formular angezeigt werden sollen
    readonly_fields = ('created_at',)  # Falls `created_at` nur lesbar sein soll

class Video480pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_480p')
    
class Video360pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_360p')
class Video720pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_720p')

class Video1080pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_1080p')

admin.site.register(Video, VideoAdmin)
admin.site.register(Video480p, Video480pAdmin)
admin.site.register(Video360p, Video360pAdmin)
admin.site.register(Video720p, Video720pAdmin)
admin.site.register(Video1080p, Video1080pAdmin)
    