from datetime import timedelta
from arrow import now
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer, CustomAuthTokenSerializer, UserEmailSerializer, UserSerializer
from .models import CustomUser, PasswordReset, UserVerification
from rest_framework.permissions import AllowAny
import uuid
from django.contrib.auth import get_user_model
from rest_framework import generics

# Create your views here.
#CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

#@cache_page(CACHE_TTL)

class LoginView(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        if not user.email_verified:
            return Response({'detail': 'Email not verified.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class CustomUserEmailListView(generics.ListAPIView):
    serializer_class = UserEmailSerializer
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class CustomPasswordResetConfirmView(View):
    def post(self, request, token=None):
        if not token:
            return HttpResponse('Token is missing', status=400)
        user =set.get_user_from_token(token)
        if user:
            return render(request, '/email/password_reset_confirm.html', {'user': user, 'token': token})
        else:
            return HttpResponse('Invalid or expired token', status=400)
        
        
    def get_user_from_token(self, token):
        try:
            password_reset = PasswordReset.objects.get(token=token)
            if password_reset.created_at + timedelta(hours=1) < now():
                return None
            return get_user_model().objects.get(email=password_reset.email)
        except PasswordReset.DoesNotExist:
            return None
    
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.validated_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            return Response({'error': 'A user with this email already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        print("Validated data:", serializer.validated_data)
        
        user = serializer.save()
        
        # Erstelle ein Verifizierungstoken
        token = str(uuid.uuid4())
        UserVerification.objects.create(user=user, token=token)
        
        # Sende die Verifizierungs-E-Mail
        verification = UserVerification.objects.get(user=user)
        verification.send_verification_email(request)
        
        return Response({'message': 'User registered. Please check your email for verification.'}, status=status.HTTP_201_CREATED)
    
    print("Serializer errors:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def verify_email(request):
    token = request.GET.get('token')
    print(token)
    
    if not token:
        return Response({'message': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        verification = UserVerification.objects.get(token=token)
        user = verification.user
        user.email_verified = True
        user.save()
        
        # Token ungültig machen
        verification.delete()
        
        return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)
    except UserVerification.DoesNotExist:
        return Response({'message': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@permission_classes([AllowAny])
def check_email(request):
    email = request.data.get('email')
    if CustomUser.objects.filter(email=email).exists():
        return Response({'message': 'Email is registered'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)