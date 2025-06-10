# mybackend/middleware.py

""" class HTMXMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is an HTMX request
        if 'HX-Request' in request.headers:
            request.htmx = True
        else:
            request.htmx = False
        response = self.get_response(request)
        return response
 """