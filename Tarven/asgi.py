import os 
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tarven.settings")
django_asgi_app = get_asgi_application()

from Chats.middleware import JwtAuthMiddleware
from Chats import routing

application = ProtocolTypeRouter(
    {
        'http':django_asgi_app,
        'websocket':JwtAuthMiddleware(URLRouter(routing.websocket_urlpatterns))
    }
)
