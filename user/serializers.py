from rest_framework import serializers
from user.models import CustomUser
from django.contrib.auth import authenticate

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def __init__(self, *args, **kwargs):
        # Setze das Modell dynamisch, um zyklische Importe zu vermeiden
        if not getattr(self, 'Meta', None) or self.Meta.model is None:
            from user.models import CustomUser
            self.Meta.model = CustomUser
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.email_verified = False  # Setze auf False bei der Registrierung
        user.save()
        return user
    
class CustomAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials.')

        if not user.email_verified:
            raise serializers.ValidationError('Email not verified.')

        data['user'] = user
        return data
    
