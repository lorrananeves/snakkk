import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import channel.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snakk_django.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            channel.routing.websocket_urlpatterns
        )
    )
})
