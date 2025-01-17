from django.contrib import admin
from .models import Video, Video120p, Video360p, Video720p 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'video_file', "thumbnail", )  # Die Felder, die Sie in der Listenansicht anzeigen möchten
    fields = ('created_at', 'title', 'description', 'video_file',  "categories", "group", "favourite")  # Die Felder, die im Formular angezeigt werden sollen
    readonly_fields = ('created_at',)  # Falls `created_at` nur lesbar sein soll

class Video120pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_120p')
    
class Video360pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_360p')
class Video720pAdmin(admin.ModelAdmin):
    list_display = ('video', 'video_file_720p')

admin.site.register(Video, VideoAdmin)
admin.site.register(Video120p, Video120pAdmin)
admin.site.register(Video360p, Video360pAdmin)
admin.site.register(Video720p, Video720pAdmin)
    