"""
ASGI config for facelink project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
import django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facelink.settings')
django.setup()  # Add this line if missing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.routing import websocket_urlpatterns  # Import WebSocket routes
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'facelink.settings')


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
