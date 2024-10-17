from django.shortcuts import render
from rest_framework.authtoken.views import APIView, ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import os
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from rest_framework import status
from videos.models import Video
import mimetypes
from rest_framework import generics
from .models import Video
from .serializers import VideoSerializer

class VideoListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class ShowVideo(APIView):
    """
    View to return videos or delete them.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, video_name, resolution):
        video_path = os.path.join(settings.MEDIA_ROOT, 'videos', f'{video_name}_{resolution}p.m3u8')

        if os.path.exists(video_path):
            mime_type, _ = mimetypes.guess_type(video_path)
            response = HttpResponse(open(video_path, 'rb').read(), content_type=mime_type)
            response['Content-Disposition'] = f'attachment; filename="{video_name}_{resolution}p.m3u8"'
            return response
        else:
            return HttpResponse("Video not found", status=404)