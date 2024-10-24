from django.utils.deprecation import MiddlewareMixin

class RealIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # X-Forwarded-For enthält eine Liste von IP-Adressen, getrennt durch Komma
            ip = x_forwarded_for.split(',')[0]  # Nimm die erste IP-Adresse
        else:
            ip = request.META.get('REMOTE_ADDR')  # Wenn kein X-Forwarded-For-Header vorhanden ist
        request.META['REMOTE_ADDR'] = ip  # Setze die IP-Adresse neu