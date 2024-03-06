from django.http import JsonResponse


def handler404(request, exception) -> JsonResponse:
    message = "Route not found."
    response = JsonResponse(data={"error": message})
    response.status_code = 404
    return response


def handler500(request) -> JsonResponse:
    message = "Internal server error."
    response = JsonResponse(data={"error": message})
    response.status_code = 500
    return response
