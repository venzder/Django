from django.urls import path
from products.views import (
    RestCategoryListView
)

app_name = 'rest_categories'

urlpatterns = [
    path('', RestCategoryListView.as_view(), name='list'),
]
