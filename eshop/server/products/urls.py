from django.urls import path
from .views import (
    product_list_view
)


urlpatterns = [
    path('', product_list_view),
]
