from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from user.models import CustomUser
from .models import Video
from .serializers import VideoSerializer

# Create your tests here.
class VideoListViewTest(TestCase):
    def setUp(self):
        # Erstelle einen Benutzer und ein Token für die Authentifizierung
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        
        # Erstelle ein paar Video-Objekte
        Video.objects.create(title='Test Video 1', description='Description 1')
        Video.objects.create(title='Test Video 2', description='Description 2')
        
    def test_get_video_list(self):
        response = self.client.get('/api/videos/')  # Ersetze dies durch den tatsächlichen URL-Pfad deiner View
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Erwartet 2 Videos
        self.assertEqual(response.data[0]['title'], 'Test Video 1')

    def test_post_video(self):
        data = {
            'title': 'New Video',
            'description': 'New Description'
        }
        response = self.client.post('/api/videos/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Video.objects.count(), 3)  # Es sollte nun 3 Videos geben