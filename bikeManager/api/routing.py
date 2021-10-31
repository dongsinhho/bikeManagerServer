from .consumer import WSConsummer
from django.urls import path

ws_urlpatterns = [
    path('ws/edge/', WSConsummer.as_asgi())
]