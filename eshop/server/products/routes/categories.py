from django.urls import path
from products.views import (
    category_create_view, category_update_view, CategoryCreateView,
    CategoriesUpdateView, CategoryListView, CategoryDetailView, CategoryDeleteView
)

app_name = 'categories'

urlpatterns = [
    path('', CategoryListView.as_view(), name='list'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='detail'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CategoriesUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='delete'),
]
