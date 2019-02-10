from django.urls import path
from .views import (
    product_list_view, product_detail_view, category_create_view
)


urlpatterns = [
    path('', product_list_view, name='list'),
    path('categories/create/', category_create_view, name='create'),
    path('<int:pk>/', product_detail_view, name='detail'),
]
