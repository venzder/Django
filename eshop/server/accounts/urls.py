# from django.urls import path
# from .views import login, logout, register, edit
#
# app_name = 'accounts'
#
#
# urlpatterns = [
#     path('login/', login, name='login'),
#     path('logout/', logout, name='logout'),
#     path('register/', register, name='register'),
#     path('edit/', edit, name='edit'),
# ]
from django.urls import path
from .views import login_view, registration_view

app_name = 'accounts'

urlpatterns = [
    path('', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
]
