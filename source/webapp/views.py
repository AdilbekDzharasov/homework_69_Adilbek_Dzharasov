from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index_view(request, *args, **kwargs):
    return render(request, 'index.html')

