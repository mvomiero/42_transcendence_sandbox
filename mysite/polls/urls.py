from django.urls import path

# impoting views from the same directory
from . import views

# The path() function is three arguments, two required: route and view. It's an empty string because it's the root URL.
# The third argument, is a name tag used for referencing the view in other parts of the Django app.
urlpatterns = [
    path("", views.index, name="index"),
]