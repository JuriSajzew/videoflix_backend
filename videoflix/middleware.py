import logging

logger = logging.getLogger(__name__)

class ForwardedForMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
            logger.debug(f"Extracted IP: {ip}")  # Debug-Log hinzufügen
            request.META['REMOTE_ADDR'] = ip
        response = self.get_response(request)
        return response