from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Video, Video480p
from videos.serializer import Video480pSerializer, VideoSerializer


# CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)

# @cache_page(CACHE_TTL)


class VideoListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    
class Video480pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, video_id, format=None):
        print(video_id)
        video = get_object_or_404(Video, id=video_id)
        print(video)
        video_480p = get_object_or_404(Video480p, video=video)
        serializer = Video480pSerializer(video_480p)
        print(serializer.data)
        return Response(serializer.data)