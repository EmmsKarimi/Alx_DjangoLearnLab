from django.urls import path
from .views import get_notifications

urlpatterns = [
    path('', get_notifications, name='notifications'),
]
