from django.contrib import admin
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    
    fieldsets = (
        ('Customised data', {
            "fields": (
                'custom',
                'phone',
                'address',
            ),
        }),
        *UserAdmin.fieldsets,
        
    )