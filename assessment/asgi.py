"""
ASGI config for assessment project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
import core.routing
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "assessment.settings")

asgi_application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": asgi_application,
        "websocket": AuthMiddlewareStack(URLRouter(core.routing.websocket_urlpatterns),)
    }
)
