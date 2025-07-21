import time

class RequestTimeLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # record when request starts
        response = self.get_response(request)  # process the request
        end_time = time.time()    # record when it finishes
        duration = end_time - start_time
        print(f"⏱️ Request to {request.path} took {duration:.4f} seconds.")
        return response
