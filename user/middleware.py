import logging

logger = logging.getLogger(__name__)

class ForwardedForMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Nur die erste IP-Adresse extrahieren
            ip = x_forwarded_for.split(',')[0].strip()
            logger.info(f"Extracted IP: {ip}")  # Log-Level auf "info" setzen für Sichtbarkeit
            request.META['REMOTE_ADDR'] = ip
        else:
            logger.debug("No X-Forwarded-For header found")
        
        # Weiterleiten der Anfrage
        response = self.get_response(request)
        return response