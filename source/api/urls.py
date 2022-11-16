from django.urls import path
from .views import add_view

app_name = 'api'

urlpatterns = [
    path('add/', add_view, name='add')
]
