from django.contrib import admin
from .models import Video, Video480p 
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Video)
admin.site.register(Video480p)

# class VideoResource(resources.ModelResource):
#     class Meta:
#         model = Video
 
# @admin.register(Video)      
# class VideoAdmin(ImportExportModelAdmin):
#     pass
    
# admin.site.register(VideoAdmin)
    