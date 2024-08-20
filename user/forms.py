from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import SetPasswordForm

class CustomUserCreationForm(UserCreationForm):    
    class Meta:        
        model = CustomUser        
        fields = '__all__'
        


class PasswordResetConfirmForm(SetPasswordForm):
    pass