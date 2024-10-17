from rest_framework.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

from user.models import UserVerification
from user.serializers import CustomAuthTokenSerializer

# Create your tests here.
class UserRegistrationTest(APITestCase):
    
    def setUp(self):
        self.register = reverse('register')
        self.valid_user_data = {
            'email': 'testuser@example.com',
            'username': 'testuser@example.com',
            'password': 'TestPassword123',
            'first_name': 'John',
            'last_name': 'Doe'  
        }
        self.existing_user_data = {
            'email': 'existinguser@example.com',
            'username': 'existinguser@example.com',
            'password': 'ExistingPassword123',
            'first_name': 'Jane',
            'last_name': 'Smith'
        }
        # Erstelle einen bestehenden Benutzer für das Duplikat-Test
        self.existing_user = get_user_model().objects.create_user(**self.existing_user_data)
        
        
    def test_register_successful(self):
        """
        Test, ob ein Benutzer erfolgreich registriert wird
        """
        response = self.client.post(self.register, self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'User registered. Please check your email for verification.')

        # Überprüfe, ob der Benutzer in der Datenbank existiert
        user = get_user_model().objects.get(email=self.valid_user_data['email'])
        self.assertIsNotNone(user)

        # Überprüfe, ob das Verifizierungstoken erstellt wurde
        verification = UserVerification.objects.filter(user=user).first()
        self.assertIsNotNone(verification)
        
    def test_register_existing_email(self):
        """
        Test, ob die Registrierung mit einer bereits existierenden E-Mail fehlschlägt
        """
        response = self.client.post(self.register, self.existing_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        self.assertIn('username', response.data)
        self.assertEqual(str(response.data['username'][0]), 'A user with that username already exists.')
        
    def test_register_invalid_email(self):
        """Test, ob die Registrierung mit ungültigen Daten fehlschlägt"""
        invalid_data = {
            'email': 'invalid-email',  # Ungültige E-Mail
            'username': 'invalid-email',  # Ungültige E-Mail
            'password': 'ValidPassword1234',       # Zu kurzes Passwort
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = self.client.post(self.register, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)  # Überprüfe, ob der Fehler im Email-Feld ist
        
User = get_user_model()

class CustomAuthTokenSerializerTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
        self.user.email_verified = True
        self.user.save()

    def test_valid_credentials(self):
        serializer = CustomAuthTokenSerializer(data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data['user'], self.user)

    def test_invalid_credentials(self):
        serializer = CustomAuthTokenSerializer(data={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_email_not_verified(self):
        unverified_user = User.objects.create_user(
            username='unverifieduser',
            password='testpassword',
            email='unverified@example.com'
        )
        unverified_user.email_verified = False
        unverified_user.save()

        serializer = CustomAuthTokenSerializer(data={
            'username': 'unverifieduser',
            'password': 'testpassword'
        })

        with self.assertRaises(ValidationError) as context:
            serializer.is_valid(raise_exception=True)

        # Prüfe den Inhalt des non_field_errors-Schlüssels in der Exception
        self.assertIn('non_field_errors', context.exception.detail)
        self.assertEqual(context.exception.detail['non_field_errors'][0], 'Email not verified.')


    def test_missing_fields(self):
        serializer = CustomAuthTokenSerializer(data={})
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
