class CustomMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("middleware before request processing")
        response = self.get_response(request)
        print("middleware after request processing")

        return response



