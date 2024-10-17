from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from user.models import CustomUser
from .models import Video
from .serializers import VideoSerializer

# Create your tests here.
class VideoListViewTest(TestCase):
    def setUp(self):
        """
        Create a user and a token for authentication
        """
        # Create a user and a token for authentication
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        video_file = SimpleUploadedFile("test_video.mp4", b"file_content", content_type="video/mp4")
        
        """
        Create a few video objects
        """
        Video.objects.create(title='Test Video 1', description='Description 1', video_file=video_file)
        Video.objects.create(title='Test Video 2', description='Description 2', video_file=video_file)
        
    def test_get_video_list(self):
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Video 1')

    def test_post_video(self):
        video_file = SimpleUploadedFile("new_test_video.mp4", b"new_file_content", content_type="video/mp4")
        
        data = {
            'title': 'New Video',
            'description': 'New Description',
            'video_file': video_file
        }
        response = self.client.post('/api/videos/', data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 3)