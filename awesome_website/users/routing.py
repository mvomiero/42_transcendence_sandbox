# routing.py
from django.urls import path
from users import consumers  # Import your app's consumers

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),  # Update the URL pattern
]

