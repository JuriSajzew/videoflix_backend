class ForwardedForMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Nimm die erste IP, die die tatsächliche Client-IP ist
            request.META['REMOTE_ADDR'] = x_forwarded_for.split(',')[0].strip()
        response = self.get_response(request)
        return response