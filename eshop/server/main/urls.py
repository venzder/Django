from django.urls import path
from .views import (
    index, about, contacts)


urlpatterns = [
    path('', index, name='main'),
    path('about/', about),
    path('contacts/', contacts),
]
