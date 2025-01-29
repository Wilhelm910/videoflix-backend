

from rest_framework import serializers
from .models import Video, Video1080p, Video480p, Video360p, Video720p

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'created_at', 'title', 'description', 'thumbnail', "categories", "favourite", "group"]  # Ohne 'video_file'

class VideoDetailSerializer(serializers.ModelSerializer):
    video_file = serializers.FileField()  # Zeigt die Video-Datei an
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video_file', 'thumbnail', "categories", "favourite", "group"]
        

class Video480pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video480p
        #fields = ['video_file_480p']
        fields = ['id','video_file_480p']
        
class Video360pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video360p
        fields = ['id','video_file_360p']
        
class Video720pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video720p
        fields = ['id','video_file_720p']
        
class Video1080pSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video1080p
        fields = ['id','video_file_1080p']


