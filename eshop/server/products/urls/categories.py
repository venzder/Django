from django.urls import path
from products.views import (
    category_create_view, category_update_view, CategoryCreateView, CategoriesUpdateView
)

app_name = 'categories'

urlpatterns = [
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CategoriesUpdateView.as_view(), name='update'),

]