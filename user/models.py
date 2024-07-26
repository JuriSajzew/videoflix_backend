from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    custom = models.CharField(max_length=1000, default='')
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=100, default='')
     
class UserVerification(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def send_verification_email(self, request):
        verification_link = request.build_absolute_uri(f'/verify-email/?token={self.token}')
        send_mail(
            'Verify your email address',
            f'Click the link to verify your email: {verification_link}',
            settings.DEFAULT_FROM_EMAIL,
            [self.user.email],
            fail_silently=False,
        )
 
 
