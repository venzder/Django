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
from django.contrib.auth.views import LogoutView
from .views import login_view, registration_view, AccountRegistrationView, AccountLoginView, AccountLogoutView

app_name = 'accounts'

urlpatterns = [
    path('', AccountLoginView.as_view(), name='login'),
    path('registration/', AccountRegistrationView.as_view(), name='registration'),
    path('logout/', AccountLogoutView.as_view(), name='logout')
]
