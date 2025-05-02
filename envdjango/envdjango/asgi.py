import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from product.routing import websocket_urlpatterns  # Import your WebSocket routes

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'envdjango.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),       # HTTP routes
    "websocket": AuthMiddlewareStack(     # WebSocket routes
        URLRouter(websocket_urlpatterns)
    ),
})

