from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT 
from django.views.decorators.cache import cache_page 
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Video, Video480p, Video720p
from videos_app.serializers import Video480pSerializer, Video720pSerializer, VideoDetailSerializer, VideoSerializer
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)



class VideoListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, format=None):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    
    
class Video480pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @method_decorator(cache_page(CACHE_TTL))  
    def get(self, request, video_id, format=None):
        video = get_object_or_404(Video, id=video_id)
        video_480p = get_object_or_404(Video480p, video=video)
        serializer = Video480pSerializer(video_480p)
        return Response(serializer.data)
    
class Video720pView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        video = get_object_or_404(Video, id=video_id)
        video_720p = get_object_or_404(Video720p, video=video)
        serializer = Video720pSerializer(video_720p)
        return Response(serializer.data)
    

class VideoView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    @method_decorator(cache_page(CACHE_TTL))
    def get(self, request, video_id, format=None):
        video = get_object_or_404(Video, id=video_id)
        serializer = VideoDetailSerializer(video)
        return Response(serializer.data)
    
    
class UpdateFavouriteView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    def put(self, request, video_id, format=None):
        video = get_object_or_404(Video, id=video_id)
        favourite_status = request.data.get('favourite')
        
         # Check if the 'favourite' field is provided in the request data
        if favourite_status is None:
            return Response({'detail': 'Favourite status is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate that 'favourite' is a boolean
        if not isinstance(favourite_status, bool):
            return Response({'detail': 'Favourite status must be a boolean.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update the 'favourite' field
        video.favourite = favourite_status
        video.save()
        
        serializer = VideoSerializer(video)
        return Response(serializer.data, status=status.HTTP_200_OK)
