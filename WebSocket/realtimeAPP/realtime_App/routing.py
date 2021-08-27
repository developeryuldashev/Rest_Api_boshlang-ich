from django.urls import path
from .RealTimeView import RTWiew

ws_urlpatterns=[
    path('ws/real_data/', RTWiew.as_asgi())
]