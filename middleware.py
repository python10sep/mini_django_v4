def simple_middleware(get_response):
    def middleware(request):
        print("[ INFO ] ** BEFORE ** passing request to corresponding view")
        response = get_response(request)
        print("[ INFO ] ** BEFORE ** sending out response")
        return response
    return middleware
