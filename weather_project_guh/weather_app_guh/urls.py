from django.urls import path  # Import the path function for defining URL patterns
from . import views  # Import views from the current package

urlpatterns = [
    path('', views.home),  # URL pattern for the home view; this will match the root URL
]