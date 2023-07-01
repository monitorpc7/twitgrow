from django.urls import path
from .views import get_reply

urlpatterns = [
    path('get-reply/', get_reply, name='get_reply'),
]