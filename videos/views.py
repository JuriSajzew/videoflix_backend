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

# Create your views here.
#class ShowVideo(APIView):
#    """
#    view to return videos or delete them
#    """
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
#    def get(self, request, video_name, video_quality):
#        video_path = os.path.join(settings.MEDIA_ROOT, 'videos', video_name + '_' + video_quality + '.m3u8')
#        #thumbnail_path = os.path.join(settings.MEDIA_ROOT, 'videos', video_name + '_thumbnail.jpg')
#        #cutted_path = os.path.join(video_name + '_' + video_quality + '.m3u8')
#         
#        #if os.path.exists(thumbnail_path):
#        #    return JsonResponse({'path': cutted_path}, status=status.HTTP_200_OK)
#        #else:
#        #    return HttpResponse("Video not found", status=404)
#        
#    def delete(self, request, video_name, video_quality):
#        try:
#            video = Video.objects.get(title=video_name)
#            video.delete()
#            return JsonResponse({'success': True})
#        except Video.DoesNotExist:
#            return JsonResponse({'success': False, 'error': 'Video not found'})    
#        except Exception as e:
#            return JsonResponse({'success': False, 'error': str(e)})

class ShowVideo(APIView):
    """
    View to return videos or delete them.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, video_name, resolution):
        video_path = os.path.join(settings.MEDIA_ROOT, 'videos', f'{video_name}_{resolution}p.m3u8')
        
        # Debug-Ausgabe zum Überprüfen des Pfads
        print(f"Video Path: {video_path}")

        if os.path.exists(video_path):
            mime_type, _ = mimetypes.guess_type(video_path)
            response = HttpResponse(open(video_path, 'rb').read(), content_type=mime_type)
            response['Content-Disposition'] = f'attachment; filename="{video_name}_{resolution}p.m3u8"'
            return response
        else:
            return HttpResponse("Video not found", status=404)