from django.urls import path

from django.urls import path
from .views import photos_list

urlpatterns = [
    path('photos/', photos_list, name='photos-list'),
    
    # Add other URLs as needed
]