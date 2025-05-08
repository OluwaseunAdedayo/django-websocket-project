import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from product.routing import websocket_urlpatterns  # Import your WebSocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envdjango.settings')
django.setup()  # <--- ensures Django apps are ready before loading Channels

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns  # Handles WebSocket
        )
    ),
})


