from django.urls import path
from products.views import (
    product_list_view, product_detail_view, product_create_view, product_update_view
)

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='create'),
    path('<int:pk>/update/', product_update_view, name='update'),
]
