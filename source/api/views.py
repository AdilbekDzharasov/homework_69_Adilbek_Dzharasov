import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def main_view(request, method):
    if request.method == 'POST':
        if request.body:
            try:
                return calculator(method, request.body)
            except ValueError:
                response = JsonResponse({'error': 'Passed not a number!'})
                response.status_code = 400
                return response
        else:
            response = JsonResponse({'error': 'Numbers not sent'})
            response.status_code = 400
            return response


def calculator(method, body):
    numbers = json.loads(body)
    A = float(numbers.get("A"))
    B = float(numbers.get("B"))
    if method == 'add':
        return JsonResponse({'answer': "%.2f" % (A + B)})
    elif method == 'subtract':
        return JsonResponse({'answer': "%.2f" % (A - B)})
    elif method == 'multiply':
        return JsonResponse({'answer': "%.2f" % (A * B)})
    elif method == 'divide':
        if B == 0:
            response = JsonResponse({'error': "Can't divide by zero"})
            response.status_code = 400
            return response
        else:
            return JsonResponse({'answer': "%.2f" % (A / B)})


@csrf_exempt
def add_view(request, *args, **kwargs):
    return main_view(request, 'add')


@csrf_exempt
def subtract_view(request, *args, **kwargs):
    return main_view(request, 'subtract')


@csrf_exempt
def multiply_view(request, *args, **kwargs):
    return main_view(request, 'multiply')


@csrf_exempt
def divide_view(request, *args, **kwargs):
    return main_view(request, 'divide')

