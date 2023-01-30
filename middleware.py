def simple_middleware(get_response):
    def middleware(request):
        print("[ INFO ] func-middleware ** before ** request processing")
        response = get_response(request)
        print("[ INFO ] func-middleware ** after ** request processing")
        return response
    return middleware
