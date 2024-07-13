from django.urls import path
from .views import get_message, get_data

urlpatterns = [
    path('message/', get_message, name='get_message'),
    path('data/', get_data, name='get_data'),
]
