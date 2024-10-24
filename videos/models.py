from datetime import date
from django.db import models


# Create your models here.
class Video(models.Model):
    CATEGORY_CHOICES = [
        ('documentary', 'Documentary'),
        ('drama', 'Drama'),
        ('romance', 'Romance'),
    ]
    
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    cover_image = models.ImageField(upload_to='covers', blank=True, null=True)
    video_urls = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.title