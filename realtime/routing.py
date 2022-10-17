from django.urls import path
from . import consumer
ws = [
    path('ws/setdata/',consumer.updateData.as_asgi())
]