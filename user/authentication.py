from rest_framework import authentication
from django.contrib.auth import authenticate

class EmailVerifiedAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Verwende die Standard-Authentifizierung
        user = authenticate(request)

        if user:
            # Prüfe, ob der Benutzer E-Mail verifiziert ist
            if not getattr(user, 'email_verified', False):
                return None  # Benutzer ist nicht authentifiziert

        return (user, None)