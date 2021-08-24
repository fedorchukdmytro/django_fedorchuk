import time


from .models import Logger


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _t = time.time()
        response = self.get_response(request)
        execution_time = (time.time() - _t)
        if request.path == "/admin/":
            Logger.objects.create(method=request.method, path=request.path, execution_time=execution_time)

        return response
