from django.urls import path
from product import consumers

websocket_urlpatterns = [
    path('ws/product/', consumers.ProductConsumer.as_asgi()),
]