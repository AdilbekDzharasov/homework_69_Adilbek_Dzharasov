from django.urls import path
from .views import add_view, subtract_view, multiply_view

app_name = 'api'

urlpatterns = [
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply')
]
