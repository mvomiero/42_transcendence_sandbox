# users/urls.py

from django.urls import path, include
from users.views import dashboard, register, profile_update
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import users.routing

urlpatterns = [
	path('', dashboard, name='dashboard'),
	path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
	path("register/", register, name="register"),
	path("profile_update/", profile_update, name="profile_update")
]

# Channels routing configuration for WebSocket connections
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            users.routing.websocket_urlpatterns
        )
    ),
})