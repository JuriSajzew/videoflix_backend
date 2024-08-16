
from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        
    def get_video_file(self, obj):
        # Erstelle die vollständige URL für das Video
        request = self.context.get('request')
        m3u8_file = f"{obj.video_file.url.replace('.m3u8')}"
        if request is not None:
            return request.build_absolute_uri(m3u8_file)
        return m3u8_file
        #if request is not None:
        #    return request.build_absolute_uri(obj.video_file.url)
        #return obj.video_file.url