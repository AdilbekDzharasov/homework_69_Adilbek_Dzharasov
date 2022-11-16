import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        if request.body:
            try:
                numbers = json.loads(request.body)
                A = float(numbers.get('A'))
                B = float(numbers.get('B'))
                return JsonResponse({'answer': A + B})
            except ValueError:
                response = JsonResponse({'error': 'Passed not a number!'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'Numbers not sent'})
            response.status_code = 400
            return response


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    if request.method == "POST":
        if request.body:
            try:
                numbers = json.loads(request.body)
                A = float(numbers.get("A"))
                B = float(numbers.get("B"))
                return JsonResponse({'answer': A - B})
            except ValueError:
                response = JsonResponse({'error': 'Passed not a number!'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'Numbers not sent'})
            response.status_code = 400
            return response

